#### te_analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(tidyverse)
library(readxl)
library(purrr)
library(janitor)
library(lubridate)
library(data.table)
library(stringdist)
library(mice)
library(lme4)
library(lmerTest)
library(groupdata2)
library(car)
library(cvms)
library(patchwork)
library(here)

# create/load functions
source(here("Code", "te_functions.R"))

# set parameters
set.seed(888)
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

#### logs #######################################################
# participant info
logs <- dat_aggregated %>%
    group_by(participant, date, test_language, age, sex, l1, l2, l2oral, l2written, country, city, vision, impairment, location, noise) %>% 
    summarise(n = n()) %>% 
    rowwise() %>% 
    mutate(exclude_trials = ifelse(test_language %in% "Catalan", n < 76*0.80, n < 97*0.80)) %>% 
    ungroup() 
fwrite(logs, here("Data", "01_logs.csv"), sep = ",", dec = ".", row.names = FALSE)

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
    select(-matches("engspa|engcat|spacat|ort|phon"))

#### filter data ########################################

#### prepare data for analysis ##########################
dat_prepared <- dat_merged %>%
    # match each trial with its corresponding value of TE Levenshtein/similarity score
    mutate(test_language = as.factor(test_language)) %>%
    select(participant, trial_id, word, input_text, test_language, accuracy, correct, typing_onset, similarity, match_count, shared_onset, consec_onset, consec_longest, freq) %>% 
    mutate_at(vars(freq, similarity), function(x) scale(x)[,1])
    
contrasts(dat_prepared$test_language) <- contr.sum(c("Catalan", "Spanish"))/2
contrasts(dat_prepared$shared_onset) <- contr.sum(c(0, 1))/2

#### export data #########################
fwrite(dat_prepared, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE)

#### fit models ##########################
fit0 <- lmer(sqrt(accuracy) ~ freq + (1 | participant) + (1 | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))
fit1 <- lmer(log(accuracy) ~ freq + match_count + (1 | participant) + (1 + match_count | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))
fit2 <- lmer(log(accuracy) ~ freq + shared_onset + (1 | participant) + (1 + shared_onset | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))
fit3 <- lmer(log(accuracy) ~ freq + consec_onset + (1 | participant) + (1 + consec_onset | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))
fit4 <- lmer(log(accuracy) ~ freq + consec_longest + (1 | participant) + (1 + consec_longest | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))
fit5 <- lmer(log(accuracy) ~ freq + similarity + (1 | participant) + (1 + similarity | trial_id), REML = FALSE, data = dat_prepared, control = lmerControl(optimizer = "bobyqa"))

mod_selection <- anova(fit0, fit1, fit2, fit3, fit4, fit5)

dat_cross <- fold(dat_prepared, k = 4, cat_col = "test_language", id_col = "participant")


