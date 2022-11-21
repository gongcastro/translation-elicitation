# import data ------------------------------------------------------------------
get_quest_raw <- function(){
    
    # process raw data
    quest_raw <- list.files("data/questionnaire/00_raw", full.names = TRUE) %>% 
        set_names(c("Catalan", "Spanish")) %>% 
        map_df(
            ~read_csv(., show_col_types = FALSE, col_names = TRUE, name_repair = make_clean_names, skip = 1),
            .id = "language"
        ) %>% 
        filter(response_type=="IP Address") %>% 
        select(
            participant_id = what_is_your_prolific_id_this_response_should_auto_fill_with_the_correct_id_please_key_it_in_manually_if_it_does_not_appear,
            language,
            date = recorded_date,
            finished,
            consent = signature_please_tick_below_to_indicate_your_digital_signature,
            captcha = q_recaptcha_score,
            age,
            sex,
            education,
            what_city_do_you_live_in,
            do_you_have_normal_or_corrected_to_normal_vision,
            have_you_been_diagnosed_with_any_language_e_g_dyslexia_or_hearing_impairment,
            where_are_you_completing_this_study_selected_choice,
            how_noisy_is_the_environment_in_which_you_are_completing_this_experiment,
            l_1 = what_is_your_native_language,
            l_2 = do_you_know_any_other_second_language_different_than_the_one_you_indicated_before_if_yes_choose_yes_and_type_which_one_in_the_text_box_below_yes_text,
            l_3 = do_you_know_any_other_third_language_different_than_the_one_you_indicated_before_if_yes_choose_yes_and_type_which_one_in_the_text_box_below_yes_text,
            l_2_oral_comp = on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_your_second_language,
            l_2_writ_prod = on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_your_second_language,
            l_3_oral_comp = on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_your_third_language,
            l_3_writ_prod = on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_your_third_language,
            cat_oral_comp = on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_catalan,
            cat_writ_prod = on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_catalan,
            spa_oral_comp = on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_spanish,
            spa_writ_prod = on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_spanish,
            living_spa = how_long_have_you_spent_in_any_region_where_spanish_is_spoken_spain_or_latin_america_including_your_childhood_pick_the_option_that_best_describes_your_situation,
            living_cat = how_long_have_you_spent_in_any_region_where_catalan_is_spoken_catalonia_valencia_balearic_islands_including_your_childhood_pick_the_option_that_best_describes_your_situation,
            has_language_problems = have_you_been_diagnosed_with_any_language_e_g_dyslexia_or_hearing_impairment,
            city = what_city_do_you_live_in,
            env_location = where_are_you_completing_this_study_selected_choice,
            env_noise = how_noisy_is_the_environment_in_which_you_are_completing_this_experiment,
            has_vision_problems = do_you_have_normal_or_corrected_to_normal_vision,
            starts_with("knowledge_"),
            starts_with("translation_"),
            starts_with("confidence"),
            -matches("_p_")
        ) %>% 
        rename_with(~str_remove(., "_confidence"), starts_with("confidence")) %>% 
        rename(
            confidence_gorrion = confidence_globo_2,
            knowledge_gorrion = knowledge_globo_2,
            translation_gorrion = translation_globo_2
        ) 
    
    write_feather(quest_raw, "data/questionnaire/01_raw.feather")
    write.csv(quest_raw, "data/questionnaire/01_raw.csv", row.names = FALSE)
    
    return(quest_raw)
}

# process responses ------------------------------------------------------------
get_quest_processed <- function(quest_raw) {
    
    quest_processed <- quest_raw %>% 
        mutate(
            group = case_when(
                l_1=="English" & language=="Catalan" ~ "cat-ENG",
                l_1=="English" & language=="Spanish" ~ "spa-ENG", 
                l_1=="Spanish" & language=="Catalan" ~ "cat-SPA"
            ),
            language = str_remove(language, "questionnaire_"),
            consent = consent=="I acknowledge that this box indicates my digital signature.",
            recorded_date = as_datetime(date),
            finished = toupper(finished),
            city = str_to_sentence(city),
            captcha = captcha > 0.7,
            finished = as.logical(finished),
            across(starts_with("translation_"), tolower),
            across(starts_with("confidence_"), as.integer),
            across(c(starts_with("knowledge_"), ends_with("_problems")), ~.=="Yes"),
            across(c(l_1, l_2, l_3), function(x) {
                str_split(x, ", ") %>% 
                    map_chr(1) %>% 
                    str_trim() %>% 
                    str_to_sentence() %>% 
                    na_if("No") %>% 
                    ifelse(is.na(.), "None", .) %>% 
                    unlist()
            }),
            across(c(ends_with("_prod"), ends_with("_comp")), ~as.integer(unlist(str_extract_all(., "(\\d)+"))))
        ) %>% 
        filter(
            finished,
            consent,
            captcha 
        ) %>% 
        pivot_longer(
            -c(participant_id:living_cat, group),
            names_to = c(".value", "word"),
            names_pattern = "(.*)_(.*)"
        ) %>% 
        mutate(
            participant_id = str_trunc(participant_id, width = 10, side = "right"),
            word = ifelse(word=="ulleras", "ulleres", word)
        ) %>%
        arrange(participant_id, knowledge, confidence) %>% 
        drop_na(knowledge) %>% 
        add_count(participant_id, name = "n_trials") %>% 
        relocate(participant_id, group)
    
    write_feather(quest_processed, "data/questionnaire/02_processed.feather")
    write.csv(quest_processed, "data/questionnaire/02_processed.csv", row.names = FALSE)
    
    return(quest_processed)
}

# participant info -------------------------------------------------------------

# select participant-level variables
get_quest_participants <- function(
        quest_processed,
        min_valid_trials = 0.80,
        min_age = 18,
        max_age = 26,
        blocked_languages = c("Italian", "Spanish", "French")
) {
    
    extra_info <- quest_processed %>% 
        distinct(participant_id, group, .keep_all = TRUE) %>% 
        mutate(date = as_datetime(date))
    
    quest_participants <- read_csv("data/questionnaire/04_responses-coded.csv", col_types = "cccclicc") %>% 
        rename(participant_id = participant) %>% 
        # code valid and correct responses
        mutate(
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct_coded = response_type %in% c("correct", "typo")
        ) %>%
        # get proportion of correct trials per participant
        group_by(participant_id) %>%
        summarise(
            n_trials = n(), # total number of trials
            n_trials_valid = sum(valid_response, na.rm = TRUE), # total number of valid trials
            n_trials_correct = sum(correct_coded, na.rm = TRUE), # total number of correct trials
            prop_correct = n_trials_correct/n_trials_valid, # proportion of correct trial (out of valid trials)
            .groups = "drop"
        ) %>% 
        left_join(extra_info) %>% 
        mutate(
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
                l_2 %!in% blocked_languages,
        ) %>%
        select(
            group, participant_id, date, age, 
            l_2, l_2_oral_comp, l_2_writ_prod,
            cat_oral_comp, cat_writ_prod,
            spa_oral_comp, spa_writ_prod,
            valid_participant, n_trials, n_trials_valid
        ) %>% 
        arrange(date)
    
    write_feather(quest_participants, "data/questionnaire/02_participants.feather")
    write_feather(quest_participants, "data/questionnaire/questionnaire_participants.rds")
    
    return(quest_participants)
}


# process responses ------------------------------------------------------------

# join with predictors dataset
get_quest_responses <- function(quest_processed, quest_participants, stimuli) {
    
    
    stimuli_tmp <- stimuli %>% 
        select(group, translation, translation_id, word_1, word_2, 
               sampa_1, sampa_2, freq_2, freq_zipf_2, lv, nd) %>% 
        mutate(word_1 = replace_non_ascii(word_1))
    
    # filter valid participants
    valid_participants <- quest_participants %>%
        filter(
            valid_participant,
            participant_id != "5eeb58e..."
        ) %>% 
        pull(participant_id)
    
    quest_responses <- read_csv("data/questionnaire/04_responses-coded.csv", col_types = "cccclicc") %>% 
        rename(participant_id = participant) %>% 
        left_join(select(quest_participants, participant_id, group)) %>% 
        # code valid and correct responses
        mutate(
            valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
            correct = response_type %in% c("correct", "typo"),
            group = as.factor(group)
        ) %>% 
        filter(
            participant_id %in% valid_participants,
            valid_response
        ) %>% 
        select(participant_id, group, word_1 = word, response = translation, knowledge, confidence, correct)
    
    write_feather(quest_responses, "data/questionnaire/06_responses.feather")
    write.csv(quest_responses, "data/questionnaire/06_responses.csv", row.names = FALSE)
    write_rds(quest_responses, "data/questionnaire/questionnaire_responses.rds")
    
    return(quest_responses)
    
}

