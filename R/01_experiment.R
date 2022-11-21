# import data ------------------------------------------------------------------
get_exp_raw <- function(){
    # set parameters
    spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")
    
    responses_path <- list.files("data/experiment/raw/", full.names = TRUE)
    
    filenames <- list.files("data/experiment/raw") %>% 
        str_extract(".*?\\_") %>% 
        str_remove("_")
    
    # participant files
    exp_raw <- responses_path %>% 
        map(fread, na.string = "") %>%  # import participant files
        map(mutate, participant = str_trunc(participant, width = 10, side = "right")) %>% 
        set_names(filenames) %>% # label each dataset with the participant's ID
        bind_rows(.id = "filename") %>% # merge datasets
        as_tibble() %>%
        clean_names() %>% 
        rename(participant_id = participant) %>% 
        # select relevant variables and rename if necessary
        select(
            participant_id, test_language, trial_id, word, soundfile, key_pressed, 
            response = input_text, key_press_time, error, age, date, city,
            matches("language_l|language_s|language_c|demo_|setup_"),
            -matches("_rt|_time"), key_press_time
        ) %>% 
        rename(demo_impairment = demo_language_key_keys) %>% 
        rename_all(gsub, pattern = "_key_keys|key_keys", replacement = "") %>% 
        # clean text input by participants (because of typos of need to translate) and redefine location    
        group_by(participant_id) %>% 
        mutate(
            across(c(starts_with("demo_"), starts_with("l"), starts_with("setup_"), age, city, setup_location, setup_noise), first_non_na),
            date = max(date, na.rm = TRUE)
        ) %>% 
        ungroup() %>% 
        mutate(
            across(c(starts_with("language_"), city, starts_with("demo_"), starts_with("l")), clean_input_text),
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
                country %in% "UK" & test_language %in% "Catalan" ~ "cat-ENG",
                country %in% "UK" & test_language %in% "Spanish" ~ "spa-ENG",
                TRUE ~ "cat-SPA"
            ),
            language_l2 = ifelse(is.na(language_l2), "None", language_l2),
            language_l1 = ifelse(str_detect(group, "ENG"), "ENG", "SPA")
        ) %>%
        ungroup() %>% 
        rename_with(~gsub(pattern = "demo_|language_|setup_", replacement = "", .), everything()) %>% 
        select(-trial_id)
    
    return(exp_raw)
}

# process responses ------------------------------------------------------------
get_exp_processed <- function(exp_raw, stimuli){
    
    exp_processed <- exp_raw %>%
        group_by(participant_id) %>% 
        mutate(
            age = max(age, na.rm = TRUE),
            key_press_time = key_press_time-1,
            response = str_to_lower(response),
            date = as_datetime(date),
            vision = !vision
        ) %>%
        # for each participant, select the first non-missing value of the following variables:
        group_by(participant_id) %>%
        mutate(across(matches("language_|demo_|setup_"), first_non_na)) %>%
        group_by(participant_id, word) %>%
        mutate(correction = first_non_na(error) %in% "yes") %>% # for each participant and trial, convert first non-missing argument into logical)
        ungroup() %>%
        drop_na(test_language) %>% # filter out rows without relevant info
        relocate(
            participant_id, group, test_language, country, 
            word, response, key_pressed, key_press_time, error
        ) %>% 
        # aggregate by trial (take only one data point per trial)
        group_by(
            participant_id, group, date, test_language,
            word, age, sex, l1, l2, l2oral, l2written, catalan_oral,
            catalan_written, spanish_oral, spanish_written,
            country, city, vision, impairment, location, noise
        ) %>%
        summarise(
            response = last_non_na(response),
            typing_onset = first_non_na(key_press_time),
            typing_offset = last_non_na(key_press_time),
            .groups = "drop"
        ) %>%
        ungroup() %>% 
        select(participant_id, group, date, age, word_1 = word, response, 
               l1, l2, l2oral, l2written, catalan_written, catalan_oral,
               spanish_oral, spanish_written,
               has_vision_problems = vision, has_language_problems = impairment) 
    
    return(exp_processed)
}


# participant data -------------------------------------------------------------
get_exp_participants <- function(
        exp_processed,
        min_valid_trials = 0.80,
        min_age = 18,
        max_age = 26,
        blocked_languages = c("Italian", "Spanish", "French")
){
    
    extra_info <- exp_processed %>% 
        distinct(
            participant_id, group, date, age, 
            l2, l2oral, l2written, spanish_oral,
            spanish_written, catalan_oral, catalan_written, 
            has_language_problems, has_vision_problems
        )
    
    exp_participants <- read_xlsx("data/experiment/processed/02_coded.xlsx") %>% 
        # code valid and correct responses
        mutate(
            participant_id = str_trunc(participant_id, width = 10, side = "right"),
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct_coded = response_type %in% c("correct", "typo")
        ) %>%
        # get proportion of correct trials per participant
        group_by(participant_id, group) %>%
        summarise(
            n_trials = n(), # total number of trials
            n_trials_valid = sum(valid_response, na.rm = TRUE), # total number of valid trials
            n_trials_correct = sum(correct_coded, na.rm = TRUE), # total number of correct trials
            prop_correct = n_trials_correct/n_trials_valid, # proportion of correct trial (out of valid trials)
            .groups = "drop"
        ) %>% 
        # add extra info
        left_join(extra_info) %>% 
        # participant is valid if has completed >= 80% trials (valid)
        mutate(
            invalid_participant_trials = ifelse(
                group %in% c("cat-ENG", "cat-SPA"),
                n_trials_valid < min_valid_trials*86, 
                n_trials_valid < min_valid_trials*103
            ),
            valid_participant = ifelse(
                # if Catalan list, at least 68 valid trials
                group %in% c("cat-ENG", "cat-SPA"),
                between(age, min_age, max_age) & 
                    n_trials_valid >= min_valid_trials*86 & !has_language_problems,
                # if Spanish list, at least 82 valid trials
                between(age, min_age, max_age) &
                    n_trials_valid >= min_valid_trials*103 & !has_language_problems
            ) &
                # L2 is not a blocked one
                l2 %!in% blocked_languages,
        ) %>%
        rename(
            l_2 = l2,
            l_2_oral_comp = l2oral,
            l_2_writ_prod = l2written,
            cat_oral_comp = catalan_oral,
            cat_writ_prod = catalan_written,
            spa_oral_comp = spanish_oral,
            spa_writ_prod = spanish_written,
        ) %>% 
        select(
            group, participant_id, date, age, 
            l_2, l_2_oral_comp, l_2_writ_prod,
            cat_oral_comp, cat_writ_prod,
            spa_oral_comp, spa_writ_prod,
            valid_participant, n_trials, n_trials_valid
        ) %>% 
        arrange(date)
    
    saveRDS(exp_participants, "results/participants.rds")
    
    return(exp_participants)
}


# process responses ------------------------------------------------------------
get_exp_responses <- function(exp_participants, stimuli){
    
    # filter valid participants
    valid_participants <- exp_participants %>%
        filter(valid_participant) %>% 
        pull(participant_id)
    
    stimuli_tmp <- stimuli %>% 
        select(group, translation, translation_id, word_1, word_2, 
               sampa_1, sampa_2, freq_2, freq_zipf_2, lv, nd) %>% 
        mutate(word_1 = replace_non_ascii(word_1))
    
    # process responses
    exp_responses <- read_xlsx("data/experiment/processed/02_coded.xlsx") %>% 
        rename(
            response = input_text,
            word_1 = word
        ) %>% 
        mutate(
            participant_id = str_trunc(participant_id, width = 10, side = "right"),
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct = response_type %in% c("correct", "type"),
            group = as.factor(group)
        ) %>% 
        filter(
            participant_id %in% valid_participants, # participant is valid
            valid_response # response is valid 
        ) %>% 
        left_join(stimuli_tmp) %>% 
        relocate(group, trial_id) %>% 
        # typos are considered correct responses
        arrange(trial_id, group) %>% 
        mutate(group = as.factor(group)) %>% 
        drop_na(correct) %>% 
        select(group, participant_id, word_1, response, correct)
    
    saveRDS(exp_responses, "results/exp_responses.rds")
    
    return(exp_responses)
}

