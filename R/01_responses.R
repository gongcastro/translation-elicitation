# preprocess responses
get_responses_processed <- function(responses_path, stimuli, seed = 888){
    # set parameters
    set.seed(seed) # for reproducibility
    spanish_cities <- c("Lorca", "Albacete", "Cieza", "Cartagena", "Murcia", "España", "Málaga", "Oviedo", "Santander", "Granada")
    
    filenames <- list.files(here("data", "raw")) %>% 
        str_extract(".*?\\_") %>% 
        str_remove("_")
    
    # participant files
    processed <- responses_path %>% 
        map(fread, na.string = "") %>%  # import participant files
        map(mutate, participant = as.character(participant)) %>% 
        set_names(filenames) %>% # label each dataset with the participant's ID
        bind_rows(.id = "filename") %>% # merge datasets
        as_tibble() %>%
        clean_names() %>% 
        rename(participant_id = participant) %>% 
        # select relevant variables and rename if necessary
        select(
            participant_id, test_language, trial_id, word, soundfile, key_pressed, 
            input_text, key_press_time, error, age, date, city,
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
    
    return(processed)
}

# clean responses
get_responses_clean <- function(responses_processed, stimuli){
    clean <- responses_processed %>%
        group_by(participant_id) %>% 
        mutate(
            age = max(age, na.rm = TRUE),
            key_press_time = key_press_time-1,
            input_text = str_to_lower(input_text),
            date = as_datetime(date)
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
            word, input_text, key_pressed, key_press_time, error
        ) %>% 
        # aggregate by trial (take only one data point per trial)
        group_by(
            participant_id, group, date, test_language,
            word, age, sex, l1, l2, l2oral, l2written, 
            country, city, vision, impairment, location, noise
        ) %>%
        summarise(
            input_text = last_non_na(input_text),
            typing_onset = first_non_na(key_press_time),
            typing_offset = last_non_na(key_press_time),
            .groups = "drop"
        ) %>%
        ungroup()
    
    stimuli_transformed <- stimuli %>% 
        mutate(
            word = word_1 %>% 
                gsub("á", "a", .) %>% 
                gsub("é", "e", .) %>% 
                gsub("í", "i", .) %>% 
                gsub("ó", "o", .) %>% 
                gsub("ú", "u", .) %>% 
                gsub("ü", "u", .) %>% 
                gsub("à", "a", .) %>% 
                gsub("è", "e", .) %>% 
                gsub("ò", "o", .) %>% 
                gsub("ñ", "n", .) %>% 
                gsub("ç", "c", .)
        )
    
    # merge with trial-level data
    merged <- clean %>%
        left_join(stimuli_transformed) %>% 
        filter(!practice_trial) %>% 
        select(
            participant_id, group, test_language, country, word, target_word = word_2,
            input_text, lv, typing_offset, nd, freq_2
        ) 
    
    return(merged)
}


#### participant data ##########################################################
get_participants <- function(
        responses_processed,
        responses_coded,
        min_valid_trials = 0.80,
        min_age = 18,
        max_age = 26,
        blocked_languages = c("Italian", "Spanish", "French")
){
    
    extra_info <- responses_processed %>% 
        distinct(
            participant_id, group, country, date, 
            test_language, age, sex, 
            l2, l2oral, l2written, spanish_oral,
            spanish_written, catalan_oral, catalan_written, 
            impairment, vision
        )
    
    participants <- responses_coded %>% 
        # code valid and correct responses
        rowwise() %>% 
        mutate(
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct_coded = response_type %in% c("correct", "typo")
        ) %>%
        ungroup() %>% 
        # get proportion of correct trials per participant
        group_by(participant_id, group) %>%
        summarise(
            n = n(), # total number of trials
            n_valid = sum(valid_response, na.rm = TRUE), # total number of valid trials
            n_correct = sum(correct_coded, na.rm = TRUE), # total number of correct trials
            prop_correct = n_correct/n_valid, # proportion of correct trial (out of valid trials)
            .groups = "drop"
        ) %>% 
        # add extra info
        left_join(extra_info) %>% 
        # participant is valid if has completed >= 80% trials (valid)
        mutate(
            invalid_participant_trials = ifelse(
                test_language %in% "Catalan", 
                n_valid < min_valid_trials*86, 
                n_valid < min_valid_trials*103
            ),
            valid_participant = ifelse(
                # if Catalan list, at least 68 valid trials
                test_language %in% "Catalan",
                between(age, min_age, max_age) & 
                    n_valid >= min_valid_trials*86 & !impairment,
                # if Spanish list, at least 82 valid trials
                between(age, min_age, max_age) &
                    n_valid >= min_valid_trials*103 & !impairment
            ) &
                # L2 is not a blocked one
                l2 %!in% blocked_languages
        ) 
    
    saveRDS(participants, "results/participants.rds")
    
    return(participants)
}


# processed responses
get_responses <- function(responses_coded, participants, stimuli){
    # filter valid participants
    valid_participants <- participants %>%
        filter(valid_participant) %>% 
        pull(participant_id)
    
    stimuli_transformed <- stimuli %>% 
        mutate(
            word = word_1 %>% 
                gsub("á", "a", .) %>% 
                gsub("é", "e", .) %>% 
                gsub("í", "i", .) %>% 
                gsub("ó", "o", .) %>% 
                gsub("ú", "u", .) %>% 
                gsub("ü", "u", .) %>% 
                gsub("à", "a", .) %>% 
                gsub("è", "e", .) %>% 
                gsub("ò", "o", .) %>% 
                gsub("ñ", "n", .) %>% 
                gsub("ç", "c", .)
        )
    
    # process responses
    responses <- responses_coded %>% 
        mutate(
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct = response_type %in% c("correct", "type"),
            group = as.factor(group)
        ) %>%
        filter(
            participant_id %in% valid_participants, # participant is valid
            valid_response # response is valid 
        ) %>% 
        left_join(stimuli_transformed) %>% 
        relocate(group, trial_id) %>% 
        arrange(group, trial_id) %>%  
        # typos are considered correct responses
        mutate(
            # center predictors
            freq_zipf_2_std = scale(freq_zipf_2)[, 1],
            nd_std = scale(nd)[, 1],
            lv_std = scale(lv)[, 1]
        ) %>% 
        arrange(trial_id, group) %>% 
        mutate(group = as.factor(group)) %>% 
        drop_na(correct, participant_id, nd_std, freq_zipf_2_std) %>% 
        # case-wise corrections
        # for some (probably encoding-related) reason, sourcing this script fails
        # when using stringdist::stringsim on the raw character vectors of flat IPA transcriptions
        # we calculated the values in the console and then fed them directly 
        mutate(
            word_2 = case_when(
                (group %in% "cat-SPA" & word=="puerco" & input_text=="puerco") ~ input_text,
                (group %in% "cat-ENG" & word=="porc" & input_text=="pork") ~ input_text,
                (group %in% "cat-SPA" & word=="bol" & input_text=="cuenco") ~ input_text,
                (group %in% "cat-SPA" & word=="fulla" & input_text=="folio") ~ input_text,
                (group %in% "spa-ENG" & word=="lengua" & input_text=="language") ~ input_text,
                (group %in% "spa-ENG" & word=="pantalon" & input_text=="pants") ~ input_text,
                TRUE ~ word_2
            ),
            ipa_flat_2 = case_when(
                (group %in% "cat-SPA" & word_2=="puerco") ~ "...",
                (group %in% "cat-ENG" & word_2=="pork") ~ "...",
                (group %in% "cat-SPA" & word_2=="cuenco") ~ "...",
                (group %in% "cat-SPA" & word_2=="folio") ~ "...",
                (group %in% "spa-ENG" & word_2=="language") ~ "...",
                (group %in% "spa-ENG" & word_2=="pants") ~ "...",
                TRUE ~ ipa_flat_2
            ),
            lv = case_when(
                (group %in% "cat-SPA" & word_2=="puerco") ~ 1/3,
                (group %in% "cat-ENG" & word_2=="pork") ~ 3/4,
                (group %in% "cat-SPA" & word_2=="cuenco") ~ 0,
                (group %in% "cat-SPA" & word_2=="folio") ~ 1/5,
                (group %in% "spa-ENG" & word_2=="language") ~ 3/7,
                (group %in% "spa-ENG" & word_2=="pants") ~ 3/8,
                TRUE ~ lv
            )
        )
    
    
    # a priori contrasts for each group
    contrasts(responses$group) <- cbind(
        "eng_spa" = c(-0.25, -0.25, 0.5), 
        "cateng_spaeng" = c(0.5, -0.5, 0)
    )
    
    saveRDS(responses, "results/responses.rds")
    
    return(responses)
}

