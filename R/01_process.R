#### 01_preprocess: Pre-process data ################

#### set up #########################################

# load packages
library(tidyverse)
library(lubridate)
library(purrr)
library(readxl)
library(data.table)
library(stringdist)
library(mice)
library(lme4)
library(car)
library(janitor)
library(patchwork)
library(here)

# create/load functions
source(here("R", "functions.R"))

# set parameters
practice_trials <- c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)
spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")

#### import data ####################################
trials <- read_xlsx(here("Stimuli", "trials.xlsx")) # trial-level data

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
dat_merged <- dat_aggregated %>%
    left_join(trials, by = c("trial_id", "test_language" = "language", "word")) %>%
    mutate(length = ifelse(nchar(orthography) >= nchar(input_text), nchar(orthography), nchar(input_text)),
           damerau = stringdist(input_text, orthography, method = "dl"),
           correct_answer = ifelse(damerau==0, "yes", "no"),
           accuracy = stringsim(orthography, input_text, method = "dl")/length)

#### filter data ########################################

#### prepare data for analysis ##########################
dat_prepared <- dat_merged %>%
    # match each trial with its corresponding value of TE Levenshtein/similarity score
    mutate(lev = case_when(l1=="English" & test_language=="Spanish" ~ lev_engspa,
                           l1=="English" & test_language=="Catalan" ~ lev_engcat,
                           l1=="Spanish" & test_language=="Catalan" ~ lev_spacat),
           sim = case_when(l1=="English" & test_language=="Spanish" ~ sim_engspa,
                           l1=="English" & test_language=="Catalan" ~ sim_engcat,
                           l1=="Spanish" & test_language=="Catalan" ~ sim_spacat),
           test_language = as.factor(test_language)) %>%
    select(participant, trial_id, word, phonology, l1, test_language, accuracy, typing_onset, sim, lev, frequency_zipf) %>% 
    mutate_at(vars(frequency_zipf, lev, sim), function(x) scale(x)[,1])
    
contrasts(dat_prepared$test_language) <- contr.sum(c("Catalan", "Spanish"))/2

#### export data #########################
fwrite(dat_prepared, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE)

#### fit models ##########################
fit0 <- lmer(accuracy ~ frequency_zipf +
                 (1 | participant) +
                 (1 | trial_id),
             data = dat_imputed)

fit1 <- lmer(accuracy ~ frequency_zipf*sim +
                 (1 + sim | participant) +
                 (1 + sim | trial_id), na.action = na.omit,
             data = dat_imputed)

mod_selection <- anova(fit0, fit1)

coefs <- Anova(fit1, type = "III", test.statistic = "F")
