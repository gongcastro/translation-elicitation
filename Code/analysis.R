#### te_analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(tidyverse)
library(patchwork)
library(readxl)
library(purrr)
library(janitor) # for cleaning vairable names
library(lubridate) # for working with dates
library(data.table) # for importing data
library(stringdist) # for calculating Levenshtein distance
library(brms) # for fitting Bayesian models
library(tidybayes) # for sampling from the posterior in Bayesian models
library(modelr) # for predicting scores from models
library(here) # for locating files in the repository with reproducibilidy

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
           demo_sex = case_when(country %in% "UK" & demo_sex %in% "m" ~ "Male",
                                country %in% "UK" & demo_sex %in% "f" ~ "Female",
                                country %in% "Spain" & demo_sex %in% "m" ~ "Female",
                                country %in% "Spain" & demo_sex %in% "h" ~ "Male"),
           language_l1 = case_when(country %in% "Spain" & language_l1 %in% "e" ~ "Spanish",
                                   country %in% "UK" & language_l1 %in% "e" ~ "English"),
           demo_education = as.numeric(demo_education),
           demo_vision = ifelse(country %in% "UK", !(demo_vision %in% "N"), demo_vision %in% "S"),
           demo_impairment = !(demo_impairment %in% "N")) %>%
    ungroup() %>% 
    rename_all(gsub, pattern = "demo_|language_|setup_", replacement = "")


#### process data ###############################################
dat_processed <- dat_raw %>%
    group_by(participant) %>% 
    mutate(age = max(age, na.rm = TRUE),
           key_press_time = key_press_time-1,
           input_text = str_to_lower(input_text),
           date = as_datetime(date)) %>%
    filter(word %!in% practice_trials) %>% # filter out practice trials
    # for each participant, select the first non-missing value of the following variables:
    group_by(participant) %>%
    mutate_at(vars(matches("language_|demo_|setup_")), first_non_na) %>%
    group_by(participant, trial_id) %>%
    mutate(correction = ifelse(first_non_na(error) %in% "yes", TRUE, FALSE)) %>% # for each participant and trial, convert first non-missing argument into logical)
    ungroup() %>%
    drop_na(test_language) %>% # filter out rows without relevant info
    relocate(participant, test_language, country, trial_id, word, input_text, key_pressed, key_press_time, error)
    
#### aggregate ##################################################
dat_aggregated <- dat_processed %>%
    # for each participant and trial, select first and last non-missing values
    group_by(participant, date, trial_id, test_language, word, age, sex, l1, l2, l2oral, l2written, country, city, vision, impairment, location, noise) %>%
    summarise(input_text = last_non_na(input_text),
              typing_onset = first_non_na(key_press_time),
              typing_offset = last_non_na(key_press_time),
              .groups = "drop") %>%
    ungroup()

#### merge with trial-level data ########################
trials <- read_xlsx(here("Stimuli", "trials.xlsx")) # trial-level data

dat_merged <- dat_aggregated %>%
    left_join(trials, by = c("trial_id", "test_language" = "language", "word")) %>% 
    mutate(similarity = case_when(country=="UK" & test_language=="Spanish" ~ similarity_engspa,
                                  country=="UK" & test_language=="Catalan" ~ similarity_engcat,
                                  TRUE ~ similarity_spacat),
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
           accuracy = stringdist(input_text, ort, method = "dl"),
           correct = ifelse(accuracy==0, 1, 0)) %>% 
    select(-matches("engspa|engcat|spacat|ort|phon")) %>% 
    select(participant, country, trial_id, word, input_text, test_language, accuracy, correct, typing_onset, similarity, match_count, shared_onset, consec_onset, consec_longest, freq)

#### export data #####################
fwrite(dat_merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE)

####  prepare accuracy data ##########
# import manually coded data
dat_coded <- read_xlsx(here("Data", "01_processed_coded.xlsx")) %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"))


#### prepare data for analysis ##########################
dat_accuracy <- dat_coded %>%
    mutate(test_language = as.factor(test_language)) %>%
    mutate_at(vars(freq, similarity), function(x) scale(x)[,1]) %>% 
    filter(valid_response) %>% 
    group_by(trial_id, country, test_language,  word, similarity, match_count, shared_onset, consec_onset, consec_longest, freq) %>% 
    summarise(n = n(),
              proportion = mean(correct_coded, na.rm = TRUE),
              .groups = "drop") %>%
    mutate_at(vars(match_count, consec_onset, consec_longest), function(x) scale(x)[,1]) %>% 
    mutate_at(vars(country, test_language), as.factor)

contrasts(dat_accuracy$test_language) <- contr.sum(c("Catalan", "Spanish"))/2
contrasts(dat_accuracy$country) <- contr.sum(c("UK", "Spain"))/2
contrasts(dat_accuracy$shared_onset) <- contr.sum(c(0, 1))/2

#### logs #######################################################

# participant info
logs <- dat_accuracy %>%
    group_by(participant, date, test_language, age, sex, l1, l2, l2oral, l2written, country, city, vision, impairment, location, noise) %>% 
    summarise(n = n()) %>% 
    rowwise() %>% 
    mutate(exclude_trials = ifelse(test_language %in% "Catalan", n < 76*0.80, n < 97*0.80)) %>% 
    ungroup() 
fwrite(logs, here("Data", "01_logs.csv"), sep = ",", dec = ".", row.names = FALSE)

#### fit models #########################################
priors <- c(prior(lognormal(0.15, 0.20), class = "Intercept"),
            prior(normal(0, 1), class = "b"), # fixed and random slopes
            prior(cauchy(0, 5), class  = "sd"), # standard deviation
            prior(beta(10, 10), class = "zoi"), # distributional parameter for Beta distribution
            prior(beta(10, 10), class = "coi"), # distributional parameter for Beta distribution
            prior(normal(1.5, 1), class = "phi")) # distributional parameter for Beta distribution
            
# null model (only frequency)
fit0 <- brm(formula = bf(proportion ~ freq + (1 | trial_id)),
            prior = priors,
            data = dat_accuracy,
            chains = 1,
            iter = 6000,
            cores = 2,
            file = here("Results", "fit0.rds"), 
            control = list(adapt_delta = 0.95),
            save_model = here("Code", "fit0.stan"),
            family = "zero_one_inflated_beta")

# match count
fit1 <- update(fit0, . ~ . + match_count - (1 | trial_id) + (1 + match_count | trial_id),
                         file = here("Results", "fit1.rds"), 
                         newdata = dat_accuracy,
                         save_model = here("Code", "fit1.stan"))

# shared onset
fit2 <- update(fit1, . ~ . + shared_onset - (1 + match_count | trial_id) + (1 + match_count + shared_onset | trial_id),
               file = here("Results", "fit2.rds"), 
               newdata = dat_accuracy,
               save_model = here("Code", "fit2.stan"))

# similarity
fit3 <- update(fit2, . ~ . + similarity - (1 + match_count + shared_onset | trial_id) + (1 + match_count + shared_onset + similarity | trial_id),
                          file = here("Results", "fit3.rds"), 
                          newdata = dat_accuracy,
                          save_model = here("Code", "fit3.stan"))

# compute k-fold validation and compare models
fit0 <- add_criterion(fit0, criterion = "kfold", K = 10, overwrite = TRUE)
fit1 <- add_criterion(fit1, criterion = "kfold", K = 10, overwrite = TRUE)
fit2 <- add_criterion(fit2, criterion = "kfold", K = 10, overwrite = TRUE)
fit3 <- add_criterion(fit3, criterion = "kfold", K = 10, overwrite = TRUE)

selection <- loo_compare(fit0, fit1, fit2, fit3)

# posterior predictive checks (what do our models predict?)
posterior_check <- expand_grid(freq = seq_range(dat_accuracy$freq, n = 10),
                               match_count = seq_range(dat_accuracy$match_count, n = 10),
                               trial_id = unique(dat_accuracy$trial_id)) %>%
    add_predicted_draws(model = fit3, n = 100, prediction = "proportion",
                        allow_new_levels = TRUE) %>% 
    mean_qi(.width = 0.5)

posterior_check %>%  
    ggplot(aes(match_count, proportion)) +
    stat_lineribbon(.width = c(0.95, 0.89, 0.5), alpha = 0.5) +
    #stat_summary(aes(group = trial_id), fun = "median", geom = "point", alpha = 0.1, size = 0.1) +
    scale_fill_brewer(palette = "Blues")


