#' Import and preprocess raw data from Experiment 2
#'
get_quest_raw <- function(quest_raw_files){
  
  # process raw data
  quest_raw <- file.path(quest_raw_files) |> 
    set_names(c("Catalan", "Spanish")) |> 
    map_df(readr::read_csv,
           show_col_types = FALSE,
           col_names = TRUE, 
           name_repair = janitor::make_clean_names, 
           skip = 1,
           .id = "language") |> 
    dplyr::filter(response_type=="IP Address") |> 
    rename(any_of(colnames_dict())) |> 
    select(participant_id, language, date, finished, consent, captcha,
           age, sex, education,
           l1, l2, l3, l2_oral_comp, l2_writ_prod, l3_oral_comp, l3_writ_prod,
           cat_oral_comp, cat_writ_prod, spa_oral_comp, spa_writ_prod, 
           living_spa, living_cat, has_language_problems,
           city, env_location, env_noise, has_vision_problems,
           starts_with("knowledge_"),
           starts_with("translation_"),
           starts_with("confidence"),
           -matches("_p_")) |> 
    rename_with(\(x) str_remove(x, "_confidence"),
                starts_with("confidence")) |> 
    rename(confidence_gorrion = confidence_globo_2,
           knowledge_gorrion = knowledge_globo_2,
           translation_gorrion = translation_globo_2) |> 
    drop_na(participant_id)
  
  return(quest_raw)
}

colnames_dict <- function() {
  c(participant_id = "what_is_your_prolific_id_this_response_should_auto_fill_with_the_correct_id_please_key_it_in_manually_if_it_does_not_appear",
    date = "recorded_date",
    consent = "signature_please_tick_below_to_indicate_your_digital_signature",
    captcha = "q_recaptcha_score",
    l1 = "what_is_your_native_language",
    l2 = "do_you_know_any_other_second_language_different_than_the_one_you_indicated_before_if_yes_choose_yes_and_type_which_one_in_the_text_box_below_yes_text",
    l3 = "do_you_know_any_other_third_language_different_than_the_one_you_indicated_before_if_yes_choose_yes_and_type_which_one_in_the_text_box_below_yes_text",
    l2_oral_comp = "on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_your_second_language",
    l2_writ_prod = "on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_your_second_language",
    l3_oral_comp = "on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_your_third_language",
    l3_writ_prod = "on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_your_third_language",
    cat_oral_comp = "on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_catalan",
    cat_writ_prod = "on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_catalan",
    spa_oral_comp = "on_a_scale_of_1_5_how_would_you_rate_your_oral_comprehension_proficiency_in_spanish",
    spa_writ_prod = "on_a_scale_of_1_5_how_would_you_rate_your_written_proficiency_in_spanish",
    living_spa = "how_long_have_you_spent_in_any_region_where_spanish_is_spoken_spain_or_latin_america_including_your_childhood_pick_the_option_that_best_describes_your_situation",
    living_cat = "how_long_have_you_spent_in_any_region_where_catalan_is_spoken_catalonia_valencia_balearic_islands_including_your_childhood_pick_the_option_that_best_describes_your_situation",
    has_language_problems = "have_you_been_diagnosed_with_any_language_e_g_dyslexia_or_hearing_impairment",
    city = "what_city_do_you_live_in",
    env_location = "where_are_you_completing_this_study_selected_choice",
    env_noise = "how_noisy_is_the_environment_in_which_you_are_completing_this_experiment",
    has_vision_problems = "do_you_have_normal_or_corrected_to_normal_vision")
}

#' Process responses from Experiment 2
#'
get_quest_processed <- function(quest_raw) {
  
  split_languages <- function(x) {
    y <- str_trim(map(str_split(x, ", "), 1))
    y <- na_if(str_to_sentence(y), "No")
    y <- unlist(if_else(is.na(y), "None", y))
    return(y)
  }
  
  quest_processed <- quest_raw |> 
    mutate(group = case_when(l1=="English" & language=="Catalan" ~ "cat-ENG",
                             l1=="English" & language=="Spanish" ~ "spa-ENG", 
                             l1=="Spanish" & language=="Catalan" ~ "cat-SPA"),
           language = str_remove(language, "questionnaire_"),
           consent = consent=="I acknowledge that this box indicates my digital signature.",
           recorded_date = lubridate::as_datetime(date),
           finished = toupper(finished),
           city = str_to_sentence(city),
           captcha = captcha > 0.7,
           finished = as.logical(finished),
           across(starts_with("translation_"), tolower),
           across(starts_with("confidence_"), as.integer),
           across(c(starts_with("knowledge_"), ends_with("_problems")),
                  \(x) x=="Yes"),
           across(c(l1, l2, l3), split_languages),
           age = as.integer(age),
           across(c(ends_with("_prod"), ends_with("_comp")), 
                  \(x) as.integer(unlist(str_extract_all(x, "(\\d)+"))))) |> 
    relocate(matches("knowlegde_|translation_|confidence_"), 
             .after = last_col()) |> 
    dplyr::filter(finished, consent, captcha) |> 
    pivot_longer(-c(participant_id:has_vision_problems),
                 names_to = c(".value", "word"),
                 names_pattern = "(.*)_(.*)") |> 
    mutate(participant_id = str_trunc(participant_id, width = 10, side = "right"),
           word = ifelse(word=="ulleras", "ulleres", word),
           date = lubridate::as_date(date),
           group = case_when(language=="Catalan" & l1=="English" ~ "cat-ENG",
                             language=="Catalan" & l1=="Spanish" ~ "cat-SPA",
                             language=="Spanish" & l1=="English" ~ "spa-ENG",
                             .default = "Other")) |> 
    relocate(all_of(c("knowledge", "translation", "confidence")), 
             .after = last_col()) |> 
    relocate(participant_id, group) |> 
    arrange(participant_id, knowledge, confidence) |> 
    drop_na(knowledge) |> 
    add_count(participant_id, name = "n_trials")
  
  return(quest_processed)
}

#' Get participant-level information from participants in Experiment 2
#' 
get_quest_participants <- function(quest_processed,
                                   min_valid_trials = 0.80,
                                   age_range = c(18, 26),
                                   blocked_languages = c("Italian",
                                                         "Spanish", 
                                                         "French")) {
  
  extra_info <- quest_processed |> 
    distinct(participant_id, group, .keep_all = TRUE) |> 
    mutate(date = lubridate::as_datetime(date)) |> 
    select(-n_trials)
  
  valid_codes <- c("correct", "typo", "wrong", "false_friend")
  correct_codes <- c("correct", "typo")
  max_cat_trials <- 86 # max of Catalan trials
  max_spa_trials <- 103 # max number of Spanish trials
  
  responses_coded_path <- file.path("data-raw", "questionnaire", "04_responses-coded.csv")
  
  quest_participants <- read_csv(responses_coded_path,
                                 col_types = "cccclicc")  |> 
    rename(participant_id = participant) |> 
    # code valid and correct responses
    mutate(valid_response = response_type %in% valid_codes,
           correct_coded = response_type %in% correct_codes) |> 
    # get proportion of correct trials per participant
    summarise(n_trials = n(), 
              # total number of valid trials
              n_trials_valid = sum(valid_response, na.rm = TRUE), 
              # total number of correct trials
              n_trials_correct = sum(correct_coded, na.rm = TRUE),
              # proportion of correct trial (out of valid trials)
              prop_correct = n_trials_correct/n_trials_valid, 
              .by = participant_id) |>  
    inner_join(extra_info, by = join_by(participant_id)) |>
    validate_participants(min_valid_trials, blocked_languages, age_range) |> 
    select(group, participant_id, date, age, 
           l2, l2_oral_comp, l2_writ_prod,
           cat_oral_comp, cat_writ_prod,
           spa_oral_comp, spa_writ_prod,
           valid_status, n_trials, n_trials_valid) |>  
    arrange(date)
  
  return(quest_participants)
}



#' Make dataset with responses from Experiment 2
#' 
get_quest_responses <- function(quest_processed, quest_participants, stimuli) {
  
  stimuli_tmp <- clean_stimuli(stimuli)
  
  valid_codes <- c("correct", "typo", "wrong", "false_friend")
  correct_codes <- c("correct", "typo")
  
  responses_coded_path <- file.path("data", "questionnaire-manual-coded.csv")
  
  quest_responses <- read_csv(responses_coded_path, col_types = "cccclicc") |>  
    rename(participant_id = participant) |> 
    left_join(select(quest_participants, participant_id, group, valid_status),
              by = join_by(participant_id)) |> 
    # code valid and correct responses
    mutate(valid_response = response_type %in% valid_codes,
           correct = response_type %in% correct_codes,
           valid_participant = valid_status=="Valid") |> 
    select(participant_id, group, word_1 = word, 
           response = translation, knowledge, confidence, correct, 
           response_type, valid_participant, valid_response)
  
  out_path <- file.path("data", "questionnaire.csv")
  arrow::write_csv_arrow(quest_responses, out_path)   
  cli_alert_success("Saved {.emph quest_responses} as {.file {out_path}}")
  
  return(quest_responses)
  
}

