#### analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(dplyr)      # for manipulating variables
library(tidyr)      # for reshaping datasets
library(ggplot2)    # for visualising plots
library(stringr)    # for manipulating string characters
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

#### process data ####################################

# participant files
filenames <- list.files(here("Data", "Raw")) %>% 
    str_extract(".*?\\_") %>% 
    str_remove("_")

dat_processed <- list.files(here("Data", "Raw"), full.names = TRUE) %>% 
    map(fread, na.string = "") %>%  # import participant files
    map(mutate, participant = as.character(participant)) %>% 
    set_names(filenames) %>% # label each dataset with the participant's ID
    bind_rows() %>% # merge datasets
    as_tibble() %>%
    clean_names() %>% 
    # select relevant variables and rename if necessary
    select(participant, test_language, trial_id, word, soundfile, key_pressed, input_text, key_press_time, error, age, date, city,
           matches("language_l|language_s|language_c|demo_|setup_"), -matches("_rt|_time")) %>% 
    rename(demo_impairment = demo_language_key_keys) %>% 
    rename_all(gsub, pattern = "_key_keys|key_keys", replacement = "") %>% 
    # clean text input by participants (because of typos of need to translate) and redefine location    
    group_by(participant) %>% 
    mutate_at(vars(starts_with("demo_"), starts_with("l"), starts_with("setup_"), age, city, setup_location, setup_noise), first_non_na) %>% 
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

#### clean data ###############################################
dat_clean <- dat_processed %>%
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
trials <- fread(here("Data", "00_trial_stats.csv"), na.strings = "") # trial-level data

dat_merged <- dat_clean %>%
    left_join(trials, by = c("trial_id", "test_language" = "language", "word")) %>% 
    mutate(similarity_phon = case_when(country=="UK" & test_language=="Spanish" ~ similarity_engspa,
                                  country=="UK" & test_language=="Catalan" ~ similarity_engcat,
                                  TRUE ~ similarity_spacat),
           similarity_ort = case_when(country=="UK" ~ stringsim(orthography, translation_english_orthography, method = "dl"),
                                     country=="Spain" ~ stringsim(orthography, translation_spanish_orthography, method = "lv")),
           close_substitutions = case_when(country=="UK" & test_language=="Spanish" ~ close_substitutions_engspa,
                                  country=="UK" & test_language=="Catalan" ~ close_substitutions_engcat,
                                  TRUE ~ close_substitutions_spacat),
           same_onset = case_when(country=="UK" & test_language=="Spanish" ~ same_onset_engspa,
                                  country=="UK" & test_language=="Catalan" ~ same_onset_engcat,
                                  TRUE ~ same_onset_spacat),
           consecutive_longest = case_when(country=="UK" & test_language=="Spanish" ~ consecutive_longest_engspa,
                                           country=="UK" & test_language=="Catalan" ~ consecutive_longest_engspa,
                                           TRUE ~ consecutive_longest_spacat),
           pthn = ifelse(l1 %in% "ENG", pthn_eng, pthn_spa),
           freq = ifelse(l1 %in% "ENG", freq_eng, freq_spa),
           accuracy = stringdist(input_text, orthography, method = "dl"),
           correct = ifelse(accuracy==0, 1, 0)) %>% 
    select(participant, group, trial_id, word, orthography, input_text, accuracy, correct, typing_offset, similarity_phon, similarity_ort, close_substitutions, same_onset, consecutive_longest, freq, pthn)

# export data
fwrite(dat_merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE) # this data is to be manually coded

#### participant data ###################################
dat_participants <- fread(here("Data", "01_processed_coded.csv"), na.strings = "") %>% 
    rowwise() %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo")) %>%
    group_by(participant, group, country) %>%
    summarise(n = n(),
              n_valid = sum(valid_response, na.rm = TRUE),
              n_correct = sum(correct_coded, na.rm = TRUE),
              prop_correct = n_correct/n_valid,
              .groups = "drop") %>% 
    left_join(distinct(dat_processed, participant, date, test_language, age, sex, l2, l2oral, l2written, spanish_oral, spanish_written, catalan_oral, catalan_written, impairment, vision)) %>% 
    # participant is valid if has completed >= 80% trials (valid)
    mutate(invalid_participant_trials = ifelse(test_language %in% "Catalan", n_valid < 0.80*86, n_valid < 0.80*103),
           valid_participant = ifelse(test_language %in% "Catalan",
                                      between(age, 18, 26) & n_valid >= 0.80*86 & !impairment,
                                      between(age, 18, 26) & n_valid >= 0.80*103 & !impairment))


fwrite(dat_participants, here("Data", "01_participants.csv"), sep = ",", dec = ".")

valid_participants <- filter(dat_participants, valid_participant) %>% pull(participant)

#### prepare accuracy data ###############################
dat_accuracy <- fread(here("Data", "01_processed_coded.csv"), na.strings = "") %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           correct_coded = as.numeric(correct_coded),
           group = as.factor(group)) %>%
    filter(participant %in% valid_participants, # participant is valid
           valid_response, # response is valid 
           word %!in% practice_trials) %>% # not a practice trial %>% 
    group_by(trial_id, word, freq, pthn, consecutive_longest, same_onset, close_substitutions, similarity_ort, similarity_phon, group) %>% 
    summarise(correct = sum(correct_coded, na.rm = TRUE),
              n = n(),
              proportion = prod(correct, 1/n, na.rm = TRUE),
              .groups = "drop") %>% 
    mutate(freq = log10(freq)+3) %>%  
    mutate_at(vars(freq, pthn, similarity_phon, similarity_ort, consecutive_longest, close_substitutions), function(x) scale(x)[,1]) %>% # standardise continuous predictors
    mutate(group = as.factor(group),
           same_onset = factor(same_onset, levels = c("different", "same_vowel", "same_consonant")))
    
#### impute missing data ##################################
dat_imputed <- mice(dat_accuracy, m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(dat_imputed$same_onset) <- cbind(c(-1, 0.5, 0.5), c(0, 0.5, -0.5))

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
                 file = here("Results", "fit0_null.rds"), 
                 control = list(adapt_delta = 0.95),
                 save_model = here("Code", "Models", "fit0_null.stan"),
                 save_all_pars = TRUE)

# null model (only frequency)
fit1_onset <- update(fit0_null, . ~ . + same_onset - (1 | group/trial_id) + (1 + same_onset | group/trial_id),
                     file = here("Results", "fit1_onset.rds"),
                     prior = c(priors, prior(lkj(2), class = "cor")),
                     newdata = dat_imputed,
                     save_model = here("Code", "Models", "fit1_onset.stan"))

# random intercepts
fit2_consec <- update(fit1_onset, . ~ . + consecutive_longest - (1 + same_onset | group/trial_id) + (1 + same_onset + consecutive_longest | group/trial_id),
                  file = here("Results", "fit2_consec.rds"),
                  newdata = dat_imputed,
                  save_model = here("Code", "Models", "fit2_consec.stan"))

# match count
fit3_phon <- update(fit2_consec, . ~ . + similarity_phon -  (1 + same_onset + consecutive_longest | group/trial_id) +  (1 + same_onset + consecutive_longest + similarity_phon | group/trial_id),
                   file = here("Results", "fit3_phon.rds"),
                   newdata = dat_imputed,
                   save_model = here("Code", "Models", "fit3_phon.stan"))

# orthographic similarity (Damerau-Levenshtein distance)
fit4_ort <- update(fit0_null, . ~ . + similarity_ort - (1 | group/trial_id) + (1 + similarity_ort | group/trial_id),
                     file = here("Results", "fit4_ort.rds"),
                     newdata = dat_imputed,
                     save_model = here("Code", "Models", "fit4_ort.stan"))

# prior
fit_prior <- update(fit0_null,
                    newdata = dat_imputed,
                    sample_prior = "only",
                    file = here("Results", "fit_prior.rds"), 
                    save_model = here("Code", "Models", "fit_prior.stan"))

# compute k-fold validation and compare models
comparison_loo <- loo(fit0_null, fit1_onset, fit2_consec, fit3_phon, fit4_ort)
comparison_waic <- list(fit0_null = fit0_null, fit1_onset = fit1_onset, fit2_consec = fit2_consec, fit3_phon = fit3_phon, fit4_ort = fit4_ort) %>%
    map(WAIC) %>% 
    map_dbl("waic")


saveRDS(comparison_waic, here("Results", "model_comparison.rds"))

#### examine posterior #####################################
posterior <- fit3_phon %>% 
    gather_draws(`b_.*`, regex = TRUE) %>% 
    ungroup() %>% 
    mutate_at(vars(.chain, .variable), function(x) factor(x, levels = unique(x), ordered = TRUE))

fwrite(posterior, here("Results", "posterior_draws.csv"), sep = ",", dec = ".", row.names = FALSE)

#### prior predictive checks ##############################
predictions_prior <- expand_grid(n = 1,
                                 pthn = c(-1, 1),
                                 same_onset = c("different", "same_vowel", "same_consonant"),
                                 consecutive_longest = c(-1, 1),
                                 similarity_phon = seq_range(dat_imputed$similarity_phon, n = 100)) %>% 
    add_fitted_draws(fit_prior, newdata = ., re_formula = NA, scale = "response", n = 1000) %>% 
    ungroup() %>%
    mutate(same_onset = factor(same_onset, labels = c("Different", "Same (Vowel)", "Same (Consonant)")),
           pthn = factor(pthn, labels = c("Small neighbourhood", "Big neightbourhood")),
           consecutive_longest = factor(consecutive_longest, labels = c("-1 SD", "+1 SD")))

fwrite(predictions_prior, here("Results", "prior_predictions.csv"), sep = ",", dec = ".", row.names = FALSE)

#### posterior predictive checks ##########################

# posterior predictive checks (what do our models predict?)
predictions <- expand_grid(n = 1,
                           pthn = c(-1, 1),
                           same_onset = c("different", "same_vowel", "same_consonant"),
                           consecutive_longest = c(-1, 1),
                           similarity_phon = seq_range(dat_imputed$similarity_phon, n = 100)) %>% 
    add_fitted_draws(fit3_phon, newdata = ., re_formula = NA, scale = "response", n = 1000) %>% 
    ungroup() %>%
    mutate(same_onset = factor(same_onset, labels = c("Different", "Same (Vowel)", "Same (Consonant)")),
                               pthn = factor(pthn, labels = c("Small neighbourhood", "Big neightbourhood")),
           consecutive_longest = factor(consecutive_longest, labels = c("-1 SD", "+1 SD")))

fwrite(predictions, here("Results", "posterior_predictions.csv"), sep = ",", dec = ".", row.names = FALSE)


#### analyse random effects structure #####################

item_effects <- ranef(fit3_phon)$`group:trial_id` %>% 
    as.data.frame() %>% 
    rownames_to_column("trial_id") %>% 
    clean_names() %>% 
    separate(trial_id, c("group", "trial_id"), sep = "_") %>% 
    rename_all(str_replace, "q2_5", "lower") %>% 
    rename_all(str_replace, "q97_5", "upper") %>% 
    as_tibble() %>% 
    rename_all(str_remove, "est_") %>% 
    rename_all(str_replace, "same_onset", "sameonset") %>% 
    rename_all(str_replace, "consecutive_longest", "consecutivelongest") %>% 
    rename_all(str_replace, "similarity_phon", "similarityphon") %>% 
    pivot_longer(cols = -c(trial_id, group), names_to = "estimate_param", values_to = "value") %>% 
    separate(estimate_param, c("estimate", "param"), sep = "_")  

    

group_effects <- ranef(fit3_phon)$`group` %>% 
    as.data.frame() %>% 
    rownames_to_column("group") %>% 
    clean_names() %>% 
    rename_all(str_replace, "q2_5", "lower") %>% 
    rename_all(str_replace, "q97_5", "upper") %>% 
    as_tibble() %>% 
    rename_all(str_remove, "est_") %>% 
    rename_all(str_replace, "same_onset", "sameonset") %>% 
    rename_all(str_replace, "consecutive_longest", "consecutivelongest") %>% 
    rename_all(str_replace, "similarity_phon", "similarityphon") %>% 
    pivot_longer(cols = -group, names_to = "estimate_param", values_to = "value") %>% 
    separate(estimate_param, c("estimate", "param"), sep = "_")  


corrs <- gather_draws(fit3_phon, `cor_.*`, regex = TRUE) %>%
    median_hdi() %>% 
    select(-matches("width|point|interval")) %>% 
    clean_names()



fwrite(item_effects, here("Results", "item_effects.csv"), sep = ",", dec = ".", row.names = FALSE)
fwrite(group_effects, here("Results", "group_effects.csv"), sep = ",", dec = ".", row.names = FALSE)
fwrite(corrs, here("Results", "corrs.csv"), sep = ",", dec = ".", row.names = FALSE)


