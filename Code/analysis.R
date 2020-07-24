#### analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(tidyverse)  # for basically everything
library(patchwork)  # for arranging plots
library(readxl)     # for importing Excel spreadsheets
library(purrr)      # for working with lists
library(janitor)    # for cleaning vairable names
library(lubridate)  # for working with dates
library(data.table) # for importing data
library(stringdist) # for calculating Levenshtein distance
library(brms)       # for fitting Bayesian models
library(mice)       # for imputing data
library(tidybayes)  # for sampling from the posterior in Bayesian models
library(modelr)     # for predicting scores from models
library(here)       # for locating files in the repository with reproducibilidy

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
           accuracy = stringdist(input_text, ort, method = "dl"),
           correct = ifelse(accuracy==0, 1, 0)) %>% 
    select(-matches("engspa|engcat|spacat|phon")) %>% 
    select(participant, group, trial_id, word, ort, input_text, accuracy, correct, typing_offset, similarity, similarity_dl, match_count, shared_onset, consec_onset, consec_longest, freq, pthn)

# export data
fwrite(dat_merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE)

#### participant data ###################################
dat_participants <- read_xlsx(here("Data", "01_processed_coded.xlsx")) %>% 
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
dat_accuracy <- read_xlsx(here("Data", "01_processed_coded.xlsx")) %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           test_language = as.factor(test_language)) %>%
    filter(participant %in% valid_participants, # participant is valid
           valid_response, # response is valid 
           word %!in% practice_trials) %>% # not a practice trial
    mutate_at(vars(freq, pthn, similarity, similarity_dl, match_count), function(x) scale(x)[,1]) %>% # standardise continuous predictors
    mutate_at(vars(group), as.factor)

contrasts(dat_accuracy$group) <- contr.helmert(c("UK-SPA", "UK-CAT", "SPA-CAT"))/2
contrasts(dat_accuracy$shared_onset) <- contr.sum(c(0, 1))/2

#### impute missing data ##################################
dat_imputed <- mice(dat_accuracy, m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble()

#### fit models #########################################
priors_dist <- c(prior(lognormal(0.0774, 0.50), class = "Intercept"), # main intercept
                 prior(beta(10, 10), class = "zoi"), # distributional parameter for Beta distribution
                 prior(beta(10, 10), class = "coi"), # distributional parameter for Beta distribution
                 prior(normal(1.5, 1), class = "phi")) # distributional parameter for Beta distribution
priors_random <- c(prior(cauchy(0, 5), class = "sd")) # positive SDs
priors_fixed <- c(prior(normal(0, 5), class = "b")) # fixed and random slopes

# null model (only frequency)
fit0_null <- brm(formula = bf(proportion ~ inv_lo + (1 | group)),
                 prior = c(priors_dist),
                 data = dat_imputed,
                 cores = 2,
                 file = here("Results", "fit0_null.rds"), 
                 control = list(adapt_delta = 0.95),
                 save_model = here("Code", "fit0_null.stan"),
                 save_all_pars = TRUE,
                 family = bernoulli("identity"))

# null model (only frequency)
fit1_freq <- update(fit0_null, . ~ . + freq + (1 + freq | group),
                     file = here("Results", "fit1_freq.rds"),
                     prior = c(priors_dist, priors_random),
                     newdata = dat_imputed,
                     save_model = here("Code", "Models", "fit1_freq.stan"))

# random intercepts
fit2_count <- update(fit0_null, . ~ . + freq*match_count - (1 | group) + (1 + freq*match_count | group),
                     file = here("Results", "fit2_count.rds"),
                     prior = c(priors_dist, priors_random),
                     newdata = dat_imputed,
                     save_model = here("Code", "Models", "fit2_count.stan"))

# match count
fit3_dl <- update(fit0_null, . ~ . + freq*similarity_dl - (1 | group) + (1 + freq*similarity_dl | group),
                     file = here("Results", "fit3_dl.rds"),
                     prior = c(priors_dist, priors_random),
                     newdata = dat_imputed,
                     save_model = here("Code", "Models", "fit3_dl.stan"))

# similarity
fit4_sim <- update(fit0_null, . ~ . + freq*similarity - (1 | group) + (1 + freq*similarity | group),
                  file = here("Results", "fit4_sim"),
                  prior = c(priors_dist, priors_random),
                  newdata = dat_imputed,
                  save_model = here("Code", "Models", "fit4_sim.stan"))


# compute k-fold validation and compare models
loo_comp <- loo(fit0_null, fit1_groups, fit2_count, fit3_dl, fit4_sim)

# posterior predictive checks (what do our models predict?)
design_matrix <- expand_grid(group = c("ENG-CAT", "ENG-SPA", "SPA-CAT"),
                             match_count = unique(dat_imputed$match_count),
                             similarity = seq_range(dat_imputed$similarity, n = 10),
                             similarity_dl = seq_range(dat_imputed$similarity, n = 10)) 

int <- mean_hdi(.value, .width = 0.95, .exclude = c(".chain", ".iteration", ".draw", ".row"))


#### examine posterior #####################################

posterior <- fit4_sim %>% 
    gather_draws(b_Intercept, b_freq, b_similarity, `b_freq:similarity`, phi, coi, zoi) %>% 
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
    #geom_point() +
    stat_slab(colour = "black") + 
    ggsave(here("Figures", "coefs.png"))

#### Analyse random effects structure #####################
groups <- fit4_sim %>%
    spread_draws(r_group[group, parameter]) %>% 
    median_qi(r_group, .width = .50) %>% 
    rename(.estimate = r_group) %>%
    select(-c(.width, .point, .interval)) %>% 
    pivot_wider(names_from = parameter, values_from = c(.estimate, .lower, .upper)) %>% 
    clean_names()

group_cors <- fit4_sim %>% 
    gather_draws(`cor_group__Intercept__freq`,
                 `cor_group__Intercept__similarity`,
                 `cor_group__Intercept__freq:similarity`,
                 `cor_group__freq__similarity`,
                 `cor_group__freq__freq:similarity`,
                 `cor_group__similarity__freq:similarity`) %>% 
    median_qi(.value, .width = .50) %>% 
    mutate(.variable = str_remove(.variable, ".*?__")) %>% 
    select(-c(.width, .point, .interval)) %>% 
    separate(.variable, c("var1", "var2"), "__")

ggplot(groups, aes(x = estimate_intercept, y = estimate_freq, colour = group)) +
    geom_errorbar(aes(xmin = lower_intercept, xmax = upper_intercept), size = 0.5, width = 0) +
    geom_errorbar(aes(ymin = lower_freq, ymax = upper_freq), size = 0.5, width = 0) +
    geom_abline(slope = filter(group_cors, var1 %in% "Intercept", var2 %in% "freq") %>% pull(.value), size = 0.75) +
    labs(x = "Intercept", y = "Frequency", colour = "Group") +
    scale_color_brewer(palette = "Set1") +
    
    ggplot(groups, aes(x = estimate_intercept, y = estimate_similarity, colour = group)) +
    geom_errorbar(aes(xmin = lower_intercept, xmax = upper_intercept), size = 0.5, width = 0) +
    geom_errorbar(aes(ymin = lower_similarity, ymax = upper_similarity), size = 0.5, width = 0) +
    geom_abline(slope = filter(group_cors, var1 %in% "Intercept", var2 %in% "similarity") %>% pull(.value), size = 0.75) +
    labs(x = "Intercept", y = "Similarity", colour = "Group") +
    scale_color_brewer(palette = "Set1") +
    
    ggplot(groups, aes(x = estimate_intercept, y = estimate_freq_similarity, colour = group)) +
    geom_errorbar(aes(xmin = lower_intercept, xmax = upper_intercept), size = 0.5, width = 0) +
    geom_errorbar(aes(ymin = lower_freq_similarity, ymax = upper_freq_similarity), size = 0.5, width = 0) +
    geom_abline(slope = filter(group_cors, var1 %in% "Intercept", var2 %in% "freq:similarity") %>% pull(.value), size = 0.75) +
    labs(x = "Intercept", y = "Frequency:Similarity", colour = "Group") +
    scale_color_brewer(palette = "Set1") +
    
    guide_area() +
    
    plot_layout(guides = "collect") &
    plot_annotation(tag_levels = "A") &
    theme_custom &
    theme(legend.key = element_rect(fill = "transparent")) &
    ggsave(here("Figures", "groups.png"), width = 5)

 dat_accuracy %>%  
    pivot_longer(data = ., cols = c(match_count, similarity_dl, similarity), names_to = "measure", values_to = "value") %>% 
    mutate(measure = case_when(measure %in% "match_count" ~ "Match count",
                               measure %in%  "similarity_dl" ~ "Ort. similarity",
                               measure %in%  "similarity" ~ "Phon. similarity")) %>% 
    ggplot(aes(x = value, y = freq)) +
    facet_grid(measure~group) +
    stat_density_2d(aes(fill = after_stat(density)), geom = "raster", contour = FALSE) +
    geom_rug(alpha = 0.25, size = 0.1, length = unit(0.1, "cm")) +
    geom_smooth(method = "lm", colour = "red", fill = "grey", size = 0.5) +
    #geom_point(dat = dat_imputed) +
    labs(x = "Lexical similarity", y = "Frequency", fill = "Density") +
    theme_custom +
    theme(legend.position = "top") +
    ggsave(here("Figures", "correlations.png"), height = 6)


