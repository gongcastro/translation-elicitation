#### analysius: Process and analyse data #########

#### set up #########################################

# load packages
library(dplyr)      # for manipulating variables
library(tidyr)      # for reshaping datasets
library(ggplot2)    # for visualising plots
library(stringr)    # for manipulating string characters
library(readxl)     # for importing Excel spreadsheets
library(purrr)      # for working with lists
library(janitor)    # for cleaning variable names
library(lubridate)  # for working with dates
library(forcats)    # for working with factors
library(data.table) # for importing data
library(stringdist) # for calculating Levenshtein distance
library(here)       # for locating files in the repository with reproducibility

# create/load functions
source(here("Code", "functions.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility
practice_trials <- c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)
spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")

#### import trial data ###############################

# frequency and phonological neighbourhoods for English (from CLEARPOND)
clearpond_eng <- fread(here("Data", "clearpond_Eng.csv"), na.strings = "") %>%
    select(-matches("spa")) %>% 
    distinct(Word_eng, .keep_all = TRUE)
clearpond_spa <- fread(here("Data", "clearpond_Spa.csv"), na.strings = "") %>%
    rename(pthn_spa = PTHN) %>% 
    distinct(Word, .keep_all = TRUE)


# word pair comparison statistics - similarity, same_onset, consecutive_longest, close_substitutions
# statistics for each language pair are different columns
# only includes statistics for words that appear in trials for the specific language
similarity_engspa <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "English-Spanish") %>%
    select(-c("Phon_eng", "Phon_spa", "check_diff")) 
similarity_engcat <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "English-Catalan") %>%
    select(-c("Phon_eng", "Phon_cat", "check_diff"))
similarity_spacat <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "Spanish-Catalan") %>%
    select(-c("Phon_cat", "Phon_spa", "check_diff"))

# replace name to match up to trial list - similarity is calculated for pork
similarity_engcat$Word_eng[similarity_engcat$Word_eng=="pork"]<-"pig/pork"

trials <- read_xlsx(here("Data", "trials.xlsx")) %>% 
    left_join(clearpond_spa, by = c("translation_spanish_orthography" = "Word")) %>% 
    left_join(clearpond_eng, by = c("translation_english_orthography" = "Word_eng")) %>% 
    clean_names() %>% 
    select(trial_id, word, orthography, phonology, starts_with("translation_"), language, practice, starts_with("pthn"), matches("freq_eng|freq_per")) %>% 
    rename(freq_spa = freq_per_million) %>% 
    left_join(similarity_engspa, by = c("translation_english_orthography" = "Word_eng", "translation_spanish_orthography" = "Word_spa")) %>% 
    left_join(similarity_engcat, by = c("translation_english_orthography" = "Word_eng", "translation_catalan_orthography" = "Word_cat")) %>% 
    left_join(similarity_spacat, by = c("translation_spanish_orthography" = "Word_spa", "translation_catalan_orthography" = "Word_cat")) %>% 
    rename_all(str_replace, "translation_", "word_") %>%
    relocate(trial_id, practice, word, orthography, phonology, language)
    
fwrite(trials, here("Data", "00_trial_stats.csv"), sep = ",", dec = ".", row.names = FALSE)

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
           matches("language_l|language_s|language_c|demo_|setup_"), -matches("_rt|_time"), key_press_time) %>% 
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

dat_merged <- dat_clean %>%
    left_join(trials, by = c("trial_id", "test_language" = "language", "word")) %>% 
    mutate(similarity_phon = case_when(country=="UK" & test_language=="Spanish" ~ similarity_engspa,
                                  country=="UK" & test_language=="Catalan" ~ similarity_engcat,
                                  TRUE ~ similarity_spacat),
           similarity_ort = case_when(country=="UK" & test_language=="Catalan" ~ similarity_ort_engcat,
                                      country=="UK" & test_language=="Spanish" ~ similarity_ort_engspa,
                                      TRUE ~ similarity_ort_spacat),
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
           freq = ifelse(l1 %in% "ENG", freq_eng, freq_spa))%>% 
    select(participant, group, trial_id, test_language, country, word, input_text, typing_offset, similarity_phon, similarity_ort, close_substitutions, same_onset, consecutive_longest, freq, pthn)

# export data
fwrite(dat_merged, here("Data", "01_processed.csv"), sep = ",", dec = ".", row.names = FALSE) # this data is to be manually coded

#### participant data ###################################
dat_participants <- fread(here("Data", "03_accuracy_coded.csv"), na.strings = "") %>% 
    rowwise() %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo")) %>%
    group_by(participant, group) %>%
    summarise(n = n(),
              n_valid = sum(valid_response, na.rm = TRUE),
              n_correct = sum(correct_coded, na.rm = TRUE),
              prop_correct = n_correct/n_valid,
              .groups = "drop") %>% 
    left_join(distinct(dat_processed, participant, country, date, test_language, age, sex, l2, l2oral, l2written, spanish_oral, spanish_written, catalan_oral, catalan_written, impairment, vision)) %>% 
    # participant is valid if has completed >= 80% trials (valid)
    mutate(invalid_participant_trials = ifelse(test_language %in% "Catalan", n_valid < 0.80*86, n_valid < 0.80*103),
           valid_participant = ifelse(test_language %in% "Catalan",
                                      between(age, 18, 26) & n_valid >= 0.80*86 & !impairment,
                                      between(age, 18, 26) & n_valid >= 0.80*103 & !impairment))


fwrite(dat_participants, here("Data", "02_participants.csv"), sep = ",", dec = ".")

valid_participants <- filter(dat_participants, valid_participant) %>% pull(participant)

#### prepare accuracy data ###############################
dat_accuracy <- fread(here("Data", "03_accuracy_coded.csv"), na.strings = c("", "NA")) %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           correct_coded = as.numeric(correct_coded),
           group = as.factor(group)) %>%
    filter(participant %in% valid_participants, # participant is valid
           valid_response, # response is valid 
           word %!in% practice_trials) %>%  # not a practice trial %>% 
    group_by(trial_id, test_language, word, freq, pthn, consecutive_longest, same_onset, close_substitutions, similarity_ort, similarity_phon, group) %>% 
    summarise(correct = sum(correct_coded, na.rm = TRUE),
              n = n(),
              proportion = prod(correct, 1/n, na.rm = TRUE),
              .groups = "drop") %>% 
    mutate(freq = log10(freq)+3,
           same_onset = ifelse(str_detect(same_onset, "same"), "Same", "Different")) %>% 
    relocate(group, trial_id) %>% 
    arrange(group, trial_id)

fwrite(dat_accuracy, here("Data", "04_accuracy.csv"), sep = ",", dec = ".", row.names = FALSE) # this data is to be manually coded

    
