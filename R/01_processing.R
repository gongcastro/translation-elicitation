# preprocessing

# set up ----

# load packages
library(tidyverse) # for manipulating variables
library(readxl) # for importing Excel spreadsheets
library(janitor) # for cleaning variable names
library(lubridate) # for working with dates
library(data.table) # for importing data
library(here) # for locating files

# create/load functions
source(here("R", "utils.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility
practice_trials <- c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)
spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")

# import trial data ----

# import trials
trials <- readRDS(here("Data", "stimuli.rds"))

# process data ----
# participant files
filenames <- list.files(here("Data", "Raw")) %>% 
    str_extract(".*?\\_") %>% 
    str_remove("_")

processed <- list.files(here("Data", "Raw"), full.names = TRUE) %>% 
    map(fread, na.string = "") %>%  # import participant files
    map(mutate, participant = as.character(participant)) %>% 
    set_names(filenames) %>% # label each dataset with the participant's ID
    bind_rows(.id = "filename") %>% # merge datasets
    as_tibble() %>%
    clean_names() %>% 
    # select relevant variables and rename if necessary
    select(
        participant, test_language, trial_id, word, soundfile, key_pressed, input_text, key_press_time, error, age, date, city,
        matches("language_l|language_s|language_c|demo_|setup_"),
        -matches("_rt|_time"),
        key_press_time
    ) %>% 
    rename(demo_impairment = demo_language_key_keys) %>% 
    rename_all(gsub, pattern = "_key_keys|key_keys", replacement = "") %>% 
    # clean text input by participants (because of typos of need to translate) and redefine location    
    group_by(participant) %>% 
    mutate_at(
        vars(
            starts_with("demo_"),
            starts_with("l"),
            starts_with("setup_"),
            age, city, setup_location, setup_noise
        ),
        first_non_na) %>% 
    mutate(date = max(date, na.rm = TRUE)) %>% 
    ungroup() %>% 
    mutate_at(vars(starts_with("language_"), city, starts_with("demo_"), starts_with("l")), clean_input_text) %>% 
    mutate(
        city = str_to_sentence(city),
        country = ifelse(city %in% spanish_cities, "Spain", "UK"),
        date = as_datetime(ymd_hms(date)),
        demo_sex = case_when(
            country %in% "UK" & demo_sex %in% "M" ~ "Male",
            country %in% "UK" & demo_sex %in% "F" ~ "Female",
            country %in% "Spain" & demo_sex %in% "M" ~ "Female",
            country %in% "Spain" & demo_sex %in% "H" ~ "Male"
        ),
        language_l1 = case_when(
            country %in% "Spain" & language_l1 %in% "E" ~ "Spanish",
            country %in% "UK" & language_l1 %in% "E" ~ "English"
        ),
        demo_education = as.numeric(demo_education),
        demo_vision = ifelse(
            country %in% "UK",
            !(demo_vision %in% "N"),
            demo_vision %in% "S"
        ),
        demo_impairment = !(demo_impairment %in% "N"),
        group = case_when(
            country %in% "UK" & test_language %in% "Catalan" ~ "ENG-CAT",
            country %in% "UK" & test_language %in% "Spanish" ~ "ENG-SPA",
            TRUE ~ "SPA-CAT"
        ),
        language_l2 = ifelse(is.na(language_l2), "None", language_l2),
        language_l1 = ifelse(str_detect(group, "ENG"), "ENG", "SPA")
    ) %>%
    ungroup() %>% 
    rename_all(gsub, pattern = "demo_|language_|setup_", replacement = "")

#### clean data ----------------------------------------------------------------
clean <- processed %>%
    group_by(participant) %>% 
    mutate(
        age = max(age, na.rm = TRUE),
        key_press_time = key_press_time-1,
        input_text = str_to_lower(input_text),
        date = as_datetime(date)
    ) %>%
    # for each participant, select the first non-missing value of the following variables:
    group_by(participant) %>%
    mutate_at(vars(matches("language_|demo_|setup_")), first_non_na) %>%
    group_by(participant, trial_id) %>%
    mutate(correction = first_non_na(error) %in% "yes") %>% # for each participant and trial, convert first non-missing argument into logical)
    ungroup() %>%
    drop_na(test_language) %>% # filter out rows without relevant info
    relocate(participant, group, test_language, country, trial_id, word, input_text, key_pressed, key_press_time, error) %>% 
    # aggregate by trial (take only one data point per trial)
    group_by(participant, group, date, trial_id, test_language, word, age, sex, l1, l2, l2oral, l2written, country, city, vision, impairment, location, noise) %>%
    summarise(
        input_text = last_non_na(input_text),
        typing_onset = first_non_na(key_press_time),
        typing_offset = last_non_na(key_press_time),
        .groups = "drop"
    ) %>%
    ungroup()

#### merge with trial-level data -----------------------------------------------
merged <- clean %>%
    left_join(trials) %>% 
    select(participant, group, trial_id, test_language, country, word, target_word = word2, trace = phon_trace, input_text,
           lv, typing_offset, vowel_ratio, consonant_ratio, pthn, frequency)

# export data
saveRDS(merged, file = here("Data", "processed.rds"))
fwrite(merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE) # this data is to be manually coded

#### participant data ----------------------------------------------------------
participants <- read_xlsx(here("Data", "02_coded.xlsx"), na = "") %>% 
    rowwise() %>% 
    mutate(
        valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
        correct_coded = response_type %in% c("correct", "typo")
    ) %>%
    group_by(participant, group) %>%
    summarise(
        n = n(),
        n_valid = sum(valid_response, na.rm = TRUE),
        n_correct = sum(correct_coded, na.rm = TRUE),
        prop_correct = n_correct/n_valid,
        .groups = "drop"
    ) %>% 
    left_join(
        distinct(processed, participant, group, country, date, test_language, age, sex, l2, l2oral, l2written, spanish_oral, spanish_written, catalan_oral, catalan_written, impairment, vision)
    ) %>% 
    # participant is valid if has completed >= 80% trials (valid)
    mutate(
        invalid_participant_trials = ifelse(test_language %in% "Catalan", n_valid < 0.80*86, n_valid < 0.80*103),
        valid_participant = ifelse(
            test_language %in% "Catalan",
            between(age, 18, 26) & n_valid >= 0.80*86 & !impairment,
            between(age, 18, 26) & n_valid >= 0.80*103 & !impairment) & l2 %!in% c("Italian", "Spanish")
    )

valid_participants <- filter(participants, valid_participant) %>% pull(participant)

fwrite(participants, here("Data", "03_participants.csv"), sep = ",", dec = ".")
saveRDS(participants, file = here("Data", "participants.rds"))

#### prepare accuracy data -----------------------------------------------------
responses <- read_xlsx(here("Data", "02_coded.xlsx"), na = "NA") %>% 
    mutate(
        valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
        correct = response_type %in% c("correct", "type"),
        group = as.factor(group)
    ) %>%
    filter(
        participant %in% valid_participants, # participant is valid
        valid_response, # response is valid 
        word %!in% practice_trials # not a practice trial
    ) %>% 
    left_join(trials) %>% 
    mutate(
        frequency = log10(frequency)+3,
        onset = ifelse(str_detect(onset, "Same"), "Same", "Different"),
        overlap_stress = ifelse(overlap_stress==1, "Overlap", "No overlap")
    ) %>% 
    relocate(group, trial_id) %>% 
    arrange(group, trial_id) 

fwrite(responses, here("Data", "04_responses.csv"), sep = ",", dec = ".", row.names = FALSE) # this data is to be manually coded
saveRDS(responses, file = here("Data", "responses.rds"))




