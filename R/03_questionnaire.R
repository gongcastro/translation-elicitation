get_questionnaire_data_raw <- function(){
    
    # process raw data
    raw_data <- list.files("data/questionnaire/00_raw", full.names = TRUE) %>% 
        set_names(c("Catalan", "Spanish")) %>% 
        map_df(
            ~read_csv(., show_col_types = FALSE, col_names = TRUE, name_repair = make_clean_names, skip = 1),
            .id = "language"
        ) %>% 
        filter(response_type=="IP Address") %>% 
        select(
            participant_id = what_is_your_prolific_id_this_response_should_auto_fill_with_the_correct_id_please_key_it_in_manually_if_it_does_not_appear,
            language,
            recorded_date,
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
            language_problems = have_you_been_diagnosed_with_any_language_e_g_dyslexia_or_hearing_impairment,
            city = what_city_do_you_live_in,
            env_location = where_are_you_completing_this_study_selected_choice,
            env_noise = how_noisy_is_the_environment_in_which_you_are_completing_this_experiment,
            vision_problems = do_you_have_normal_or_corrected_to_normal_vision,
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
        ) %>% 
        mutate(
            group = case_when(
                l_1=="English" & language=="Catalan" ~ "cat-ENG",
                l_1=="English" & language=="Spanish" ~ "spa-ENG", 
                l_1=="Spanish" & language=="Catalan" ~ "cat-SPA"
            ),
            language = str_remove(language, "questionnaire_"),
            consent = consent=="I acknowledge that this box indicates my digital signature.",
            recorded_date = as_datetime(recorded_date),
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
            nchar(participant_id) > 12,
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
        add_count(participant_id, name = "num_trials") %>% 
        relocate(participant_id, group)
    
    write_feather(raw_data, "data/questionnaire/01_tidy.feather")
    write.csv(raw_data, "data/questionnaire/01_tidy.csv", row.names = FALSE)
    
    return(raw_data)
}

#### participant info ##########################################################

# select participant-level variables
get_questionnaire_participants <- function(questionnaire_data_raw) {
    participants <- questionnaire_data_raw %>% 
        select(-c(finished:captcha, word:confidence)) %>% 
        distinct(participant_id, .keep_all = TRUE)
    
    write_feather(participants, "data/questionnaire/02_participants.feather")
    
    return(participants)
}


#### get responses ############################################################

# responses in long format
get_questionnaire_data_processed <- function(questionnaire_data_raw) {
    responses <- select(questionnaire_data_raw, participant_id, language, word, translation, knowledge, confidence)
    write_feather(responses, "data/questionnaire/03_responses-raw.feather")
    write.csv(responses, "data/questionnaire/03_responses-raw.csv", row.names = FALSE)
    
    return(responses)
}

#### corrected responses #######################################################

# process and clean coded data
get_questionnaire_data_clean <- function(questionnaire_participants) {
    
    data_clean <- read_csv("data/questionnaire/04_responses-coded.csv", col_types = "cccclicc") %>% 
        rename(participant_id = participant) %>% 
        left_join(select(questionnaire_participants, participant_id, group)) %>% 
        select(-comments) %>% 
        mutate(
            correct = response_type %in% c("correct", "typo"),
            valid = response_type %in% c("correct", "typo", "wrong", "false_friend")
        ) %>% 
        filter(valid) %>% 
        add_count(participant_id, name = "num_trials") %>% 
        filter(
            participant_id != "5eeb58e...",
            num_trials >= max(.$num_trials)*0.80
        ) %>% 
        select(participant_id, group, word_1 = word, response = translation, knowledge, confidence, correct)
    
    write_feather(data_clean, "data/questionnaire/05_clean.feather")
    write.csv(data_clean, "data/questionnaire/05_clean.csv", row.names = FALSE)
    
    return(data_clean)
    
}


# join with predictors dataset
get_questionnaire_responses <- function(questionnaire_data_clean, stimuli) {
    
    stimuli_tmp <- stimuli %>% 
        select(group, translation, translation_id, word_1, word_2, 
               sampa_1, sampa_2, freq_2, freq_zipf_2, lv, nd) %>% 
        mutate(word_1 = replace_non_ascii(word_1))
    
    responses <- questionnaire_data_clean %>% 
        left_join(stimuli_tmp) %>% 
        mutate(
            # center predictors
            confidence_ctr = scale(confidence, scale = FALSE)[,1],
            freq_zipf_2_std = scale(freq_zipf_2)[, 1],
            nd_std = scale(nd)[, 1],
            lv_std = scale(lv)[, 1]
        ) %>% 
        drop_na(freq_zipf_2_std, nd_std, lv_std)
    
    write_feather(responses, "data/questionnaire/06_responses.feather")
    write.csv(responses, "data/questionnaire/05_responses.csv", row.names = FALSE)
    
    return(responses)
    
}

