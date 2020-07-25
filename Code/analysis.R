#### analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(dplyr)  # for basically everything
library(tidyr)
library(ggplot2)
library(stringr)
library(patchwork)  # for arranging plots
library(readxl)     # for importing Excel spreadsheets
library(purrr)      # for working with lists
library(janitor)    # for cleaning variable names
library(lubridate)  # for working with dates
library(data.table) # for importing data
library(stringdist) # for calculating Levenshtein distance
library(brms)       # for fitting Bayesian models
library(mice)       # for imputing data
library(tidybayes)  # for sampling from the posterior in Bayesian models
library(modelr)     # for predicting scores from models
library(here)       # for locating files in the repository with reproducibility

# create/load functions
source(here("Code", "functions.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility
practice_trials <- c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)
spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")

#### import data ####################################

# participant files
filenames <- list.files(here("Data", "Raw")) %>% 
    str_extract(".*?\\_") %>% 
    str_remove("_")

dat_raw <- list.files(here("Data", "Raw"), full.names = TRUE) %>% 
    map(fread, na.string = "") %>%  # import participant files
    map(mutate, participant = as.character(participant)) %>% 
    set_names(filenames) %>% # label each dataset with the participant's ID
    bind_rows() %>% # merge datasets
    as_tibble() %>%
    clean_names() %>% 
    # select relevant variables and rename if necessary
    select(participant, test_language, trial_id, word, soundfile, key_pressed, input_text, key_press_time, error, age, date, city,
           matches("language_l|demo_|setup_"), -contains("_rt")) %>% 
    rename(demo_impairment = demo_language_key_keys) %>% 
    rename_all(gsub, pattern = "_key_keys|key_keys", replacement = "") %>% 
    # clean text input by participants (because of typos of need to translate) and redefine location    
    group_by(participant) %>% 
    mutate_at(vars(starts_with("demo_"), starts_with("l"), starts_with("setup_"), city, setup_location, setup_noise), first_non_na) %>% 
    mutate(date = max(date, na.rm = TRUE)) %>% 
    ungroup() %>% 
    mutate_at(vars(starts_with("language_"), city, starts_with("demo_"), starts_with("l")), clean_input_text) %>% 
    mutate(city = str_to_sentence(city),
           country = ifelse(city %in% spanish_cities, "Spain", "UK"),
           date = as_datetime(ymd_hms(date)),
           demo_sex = case_when(country %in% "UK" & demo_sex %in% "M" ~ "Male",
                                country %in% "UK" & demo_sex %in% "F" ~ "Female",
                                country %in% "Spain" & demo_sex %in% "M" ~ "Female",
                                country %in% "Spain" & demo_sex %in% "H" ~ "Male"),
           language_l1 = case_when(country %in% "Spain" & language_l1 %in% "E" ~ "Spanish",
                                   country %in% "UK" & language_l1 %in% "E" ~ "English"),
           demo_education = as.numeric(demo_education),
           demo_vision = ifelse(country %in% "UK", !(demo_vision %in% "N"), demo_vision %in% "S"),
           demo_impairment = !(demo_impairment %in% "N"),
           group = case_when(country %in% "UK" & test_language %in% "Catalan" ~ "ENG-CAT",
                             country %in% "UK" & test_language %in% "Spanish" ~ "ENG-SPA",
                             TRUE ~ "SPA-CAT"),
           language_l2 = ifelse(is.na(language_l2), "None", language_l2),
           language_l1 = ifelse(str_detect(group, "ENG"), "ENG", "SPA")) %>%
    ungroup() %>% 
    rename_all(gsub, pattern = "demo_|language_|setup_", replacement = "")


#### process data ###############################################
dat_processed <- dat_raw %>%
    group_by(participant) %>% 
    mutate(age = max(age, na.rm = TRUE),
           key_press_time = key_press_time-1,
           input_text = str_to_lower(input_text),
           date = as_datetime(date)) %>%
    # for each participant, select the first non-missing value of the following variables:
    group_by(participant) %>%
    mutate_at(vars(matches("language_|demo_|setup_")), first_non_na) %>%
    group_by(participant, trial_id) %>%
    mutate(correction = ifelse(first_non_na(error) %in% "yes", TRUE, FALSE)) %>% # for each participant and trial, convert first non-missing argument into logical)
    ungroup() %>%
    drop_na(test_language) %>% # filter out rows without relevant info
    relocate(participant, group, test_language, country, trial_id, word, input_text, key_pressed, key_press_time, error) %>% 
    # aggregate by trial (take only one data point per trial)
    group_by(participant, group, date, trial_id, test_language, word, age, sex, l1, l2, l2oral, l2written, country, city, vision, impairment, location, noise) %>%
    summarise(input_text = last_non_na(input_text),
              typing_onset = first_non_na(key_press_time),
              typing_offset = last_non_na(key_press_time),
              .groups = "drop") %>%
    ungroup()

#### merge with trial-level data ########################
trials <- read_xlsx(here("Stimuli", "trials.xlsx")) # trial-level data

dat_merged <- dat_processed %>%
    left_join(trials, by = c("trial_id", "test_language" = "language", "word")) %>% 
    mutate(similarity = case_when(country=="UK" & test_language=="Spanish" ~ similarity_engspa,
                                  country=="UK" & test_language=="Catalan" ~ similarity_engcat,
                                  TRUE ~ similarity_spacat),
           similarity_dl = case_when(country=="UK" ~ stringsim(ort, ort_eng, method = "dl"),
                                     country=="Spain" ~ stringsim(ort, ort_spa, method = "dl")),
           match_count = case_when(country=="UK" & test_language=="Spanish" ~ match_count_engspa,
                                   country=="UK" & test_language=="Catalan" ~ match_count_engcat,
                                   TRUE ~ match_count_spacat),
           shared_onset = case_when(country=="UK" & test_language=="Spanish" ~ shared_onset_engspa,
                                    country=="UK" & test_language=="Catalan" ~ shared_onset_engcat,
                                    TRUE ~ shared_onset_spacat),
           consec_onset = case_when(country=="UK" & test_language=="Spanish" ~ consec_onset_engspa,
                                    country=="UK" & test_language=="Catalan" ~ consec_onset_engcat,
                                    TRUE ~ consec_onset_spacat),
           consec_longest = case_when(country=="UK" & test_language=="Spanish" ~ consec_longest_engspa,
                                      country=="UK" & test_language=="Catalan" ~ consec_longest_engspa,
                                      TRUE ~ consec_longest_spacat),
           pthn = ifelse(l1 %in% "ENG", pthn_eng, pthn_spa),
           freq = ifelse(l1 %in% "ENG", freq_eng, freq_spa),
           accuracy = stringdist(input_text, ort, method = "dl"),
           correct = ifelse(accuracy==0, 1, 0)) %>% 
    select(-matches("engspa|engcat|spacat|phon")) %>% 
    select(participant, group, trial_id, word, ort, input_text, accuracy, correct, typing_offset, similarity, similarity_dl, match_count, shared_onset, consec_onset, consec_longest, freq, pthn)

# export data
fwrite(dat_merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE)

#### participant data ###################################
dat_participants <- fread(here("Data", "01_processed_coded.csv"), na.strings = "") %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo")) %>%
    group_by(participant, group) %>%
    summarise(n = n(),
              n_valid = sum(valid_response, na.rm = TRUE),
              n_correct = sum(correct_coded, na.rm = TRUE),
              prop_correct = n_correct/n_valid,
              .groups = "drop") %>% 
    left_join(distinct(dat_processed, participant, test_language, age, sex, l2, l2oral, l2written, impairment)) %>% 
    mutate(valid_participant = ifelse(test_language %in% "Catalan",
                                      between(age, 18, 26) & n_valid >= 0.80*86 & !impairment,
                                      between(age, 18, 26) & n_valid >= 0.80*103 & !impairment))

valid_participants <- filter(dat_participants, valid_participant) %>% pull(participant)

####  prepare accuracy data ###############################
dat_accuracy <- fread(here("Data", "01_processed_coded.csv"), na.strings = "") %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           correct_coded = as.numeric(correct_coded),
           group = as.factor(group)) %>%
    filter(participant %in% valid_participants, # participant is valid
           valid_response, # response is valid 
           word %!in% practice_trials) %>% # not a practice trial %>% 
    group_by(trial_id, word, freq, pthn, match_count, similarity_dl, similarity, group) %>% 
    summarise(correct = sum(correct_coded, na.rm = TRUE),
              n = n(),
              proportion = prod(correct, 1/n, na.rm = TRUE),
              .groups = "drop") %>% 
    mutate(freq = log10(freq)+3) %>%  
    mutate_at(vars(freq, pthn, similarity, similarity_dl, match_count), function(x) scale(x)[,1]) %>% # standardise continuous predictors
    mutate_at(vars(group), as.factor)

#### impute missing data ##################################
dat_imputed <- mice(dat_accuracy, m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

#### fit models #########################################
priors <- c(prior(normal(0, 0.001), class = "Intercept"),
            prior(normal(0, 5), class = "b"), 
            prior(cauchy(0, 5), class = "sd"))

# null model (only frequency)
fit0_null <- brm(formula = bf(correct | trials(n) ~ pthn + (1 | group/trial_id)),
                 prior = priors,
                 family = binomial("logit"),
                 data = dat_imputed,
                 chains = 1,
                 iter = 5000,
                 cores = 4,
                 file = here("Results", "fit0_null.rds"), 
                 control = list(adapt_delta = 0.95),
                 save_model = here("Code", "fit0_null.stan"),
                 save_all_pars = TRUE)
`
# null model (only frequency)
fit1_count <- update(fit0_null, . ~ . -pthn + pthn*match_count - (1 | group/trial_id) + (1 + match_count | group/trial_id),
                     file = here("Results", "fit1_count.rds"),
                     prior = c(priors, prior(lkj(2), class = "cor")),
                     newdata = dat_imputed,
                     cores = 4,
                     save_model = here("Code", "Models", "fit1_count.stan"))

# random intercepts
fit2_dl <- update(fit0_null, . ~ . -pthn + pthn*similarity_dl - (1 | group/trial_id) + (1 + similarity_dl | group/trial_id),
                  file = here("Results", "fit2_dl.rds"),
                  prior = c(priors, prior(lkj(2), class = "cor")),
                  newdata = dat_imputed,
                  cores = 4,
                  save_model = here("Code", "Models", "fit2_dl.stan"))

# match count
fit3_sim <- update(fit0_null, . ~ . -pthn + pthn*similarity - (1 | group/trial_id) + (1 + similarity | group/trial_id),
                   file = here("Results", "fit3_sim.rds"),
                   prior = c(priors, prior(lkj(2), class = "cor")),
                   newdata = dat_imputed,
                   cores = 4,
                   save_model = here("Code", "Models", "fit3_sim.stan"))

# compute k-fold validation and compare models
loo_comp <- loo(fit0_null, fit1_count, fit2_dl, fit3_sim)


#### examine posterior #####################################
posterior <- fit3_sim %>% 
    gather_draws(b_Intercept, b_pthn, b_similarity, `b_pthn:similarity`) %>% 
    ungroup() %>% 
    mutate_at(vars(.chain, .variable), function(x) factor(x, levels = unique(x), ordered = TRUE))

posterior_summary <- posterior %>% 
    group_by(.variable) %>% 
    median_hdi(.width = c(0.95, 0.89, 0.67, 0.50))
    
posterior %>%
    filter(.iteration < 2000) %>% 
    ggplot(aes(.iteration, .value, colour = .chain)) +
    facet_wrap(~.variable, scales = "free_y") +
    geom_line() +
    labs(x = "Iteration", y = "Value", colour = "Chain") +
    theme_custom +
    theme(legend.position = "top") +
    ggsave(here("Figures", "convergence.png"))

posterior %>%
    ggplot(aes(.value, .variable)) +
    geom_vline(xintercept = 0, linetype = "dashed") +
    stat_slab(fill = "black") + 
    stat_interval(.width = c(0.95, 0.89, 0.67, 0.5), position = position_nudge(y = -0.15)) +
    labs(x = "Estimate", y = "Coefficient", colour = "Credible interval",
         title = "Posterior distribution of coefficients of fixed effects") +
    scale_colour_brewer(palette = "Blues") +
    theme_custom +
    theme(panel.grid.major.y = element_line(colour = "grey"),
          legend.position = "top",
          legend.key = element_rect(fill = "transparent")) +
    ggsave(here("Figures", "coefs.png"))



#### posterior predictive checks ##########################

# posterior predictive checks (what do our models predict?)
predictions <- expand_grid(n = 1,
                           pthn = seq_range(dat_imputed$pthn, n = 4),
                           similarity = seq_range(dat_imputed$similarity, n = 100)) %>% 
    add_fitted_draws(fit3_sim, newdata = ., re_formula = NA, scale = "response", n = 1000) %>% 
    mutate(pthn_cat = factor(pthn, levels = unique(.$pthn), labels = paste0("Q", seq(4, 1)))) %>% 
    ungroup() 


predictions %>%
    ggplot(aes(similarity, .value)) +
    stat_lineribbon(.width = c(0.95, 0.89, 0.67, 0.5)) +
    geom_vline(xintercept = 0, colour= "grey") +
    geom_hline(yintercept = 0.5, colour= "grey") +
    stat_summary(data = mutate(dat_imputed, pthn = cut_interval(pthn, n = 4, labels = paste0("Q", seq(4, 1)))),
                 aes(y = proportion), fun = "mean", geom = "point", size = 0.5) +
    facet_wrap(~pthn_cat) +
    
    labs(x = "Phonological similarity", y = "Probability of correct translation",
         fill = "Credible interval",
         title = "Effect of phonological similarity on probability of correct translation",
         subtitle = "Model predictions are displayed for different quartiles of PTHN") +
    scale_fill_brewer() +
    theme_custom +
    theme(legend.position = "top") +
    ggsave(here("Figures", "predictions.png"))

#### analyse random effects structure #####################
cors_items <- spread_draws(fit3_sim, `cor_group:trial_id__Intercept__similarity`) %>%
    median_hdi() %>% 
    clean_names()

items <- ranef(fit3_sim)$`group:trial_id` %>% 
    as_tibble() %>% 
    clean_names() %>% 
    rename_all(str_replace, "q2_5", "lower") %>% 
    rename_all(str_replace, "q97_5", "upper") %>%
    bind_cols(dat_imputed)

groups <- spread_draws(fit3_sim, r_group[group, param]) %>% 
    pivot_wider(names_from = param, values_from = r_group) %>% 
    clean_names()

# item correlations
ggplot(items, aes(x = estimate_intercept, y = estimate_similarity, colour = group, fill = group)) +
    geom_point(size = 2, alpha = 0.5, show.legend = FALSE) +
    geom_smooth(method = "lm", formula = "y ~ x") +
    labs(x = "Intercept", y = "Similarity slope", colour = "Group", fill = "Group",
         title = "Correlation between intercepts and similarity slopes",
         subtitle = paste0("r = ", round(cors_items$cor_group_trial_id_intercept_similarity, 2),
                           ", Median 95% HDI = [", round(cors_items$lower, 2), "-", round(cors_items$upper, 2), "]",
                           ", R² = ", round(cors_items$cor_group_trial_id_intercept_similarity^2, 2))) +
    scale_colour_brewer(palette = "Set1") +
    scale_fill_brewer(palette = "Set1") +
    theme_custom +
    theme(legend.position = c(0.01, 0.9),
          legend.direction = "horizontal",
          legend.justification = 0) +
    ggsave(here("Figures", "random_items.png"))

# group correlations
ggplot(groups, aes(x = intercept, y = similarity, colour = group)) +
    facet_wrap(~group) +
    stat_density_2d_filled(colour = "transparent", contour_var = "ndensity", n = 100, h = 1) +
    labs(x = "Intercept", y = "Similarity slope", fill = "Probability density") +
    scale_fill_viridis_d(option = "plasma") +
    theme_custom +
    theme(legend.position = "none",
          panel.border = element_blank()) +
    ggsave(here("Figures", "random_groups.png"))
    
    