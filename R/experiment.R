#' Import and preprocess raw data from Experiments 1 and 3
#'
get_exp_raw <- function(exp_raw_files) {
  # set parameters
  spanish_cities <- c(
    "Lorca",
    "Albacete",
    "Cieza",
    "Cartagena",
    "Murcia",
    "España",
    "Málaga",
    "Oviedo",
    "Santander",
    "Granada"
  )

  filenames <- basename(exp_raw_files) |>
    str_extract(".*?\\_") |>
    str_remove("_")

  # participant files
  exp_raw <- exp_raw_files |>
    set_names(filenames) |> # label each dataset with the participant's ID
    map(arrow::read_csv_arrow, na = c("", " ")) |> # import participant files
    map_dfr(
      mutate,
      participant = str_trunc(participant, width = 10, side = "right"),
      .id = "filename"
    ) |>
    janitor::clean_names() |>
    rename(
      participant_id = participant,
      demo_impairment = demo_language_key_keys,
      response = input_text
    ) |>
    rename_with(gsub, pattern = "_key_keys|key_keys", replacement = "") |>
    # select relevant variables and rename if necessary
    select(
      participant_id,
      test_language,
      trial_id,
      word,
      soundfile,
      key_pressed,
      response,
      key_press_time,
      error,
      age,
      date,
      city,
      matches("language_l|language_s|language_c|demo_|setup_"),
      -matches("_rt|_time"),
      key_press_time
    ) |>
    # clean text input by participants (because of typos of need to translate) and redefine location
    mutate(
      across(
        c(
          starts_with("demo_"),
          starts_with("l"),
          starts_with("setup_"),
          age,
          city,
          setup_location,
          setup_noise
        ),
        first_non_na
      ),
      date = max(date, na.rm = TRUE),
      .by = participant_id
    ) |>
    mutate(
      across(
        c(
          starts_with("language_"),
          city,
          starts_with("demo_"),
          starts_with("l")
        ),
        clean_input_text
      ),
      city = str_to_sentence(city),
      country = if_else(city %in% spanish_cities, "Spain", "UK"),
      date = lubridate::as_datetime(lubridate::ymd_hms(date)),
      demo_sex = case_when(
        country == "UK" & demo_sex == "M" ~ "Male",
        country == "UK" & demo_sex == "F" ~ "Female",
        country == "Spain" & demo_sex == "M" ~ "Female",
        country == "Spain" & demo_sex == "H" ~ "Male"
      ),
      language_l1 = case_when(
        country == "Spain" & language_l1 == "E" ~ "Spanish",
        country == "UK" & language_l1 == "E" ~ "English"
      ),
      demo_education = as.numeric(demo_education),
      demo_vision = if_else(
        country == "UK",
        !(demo_vision == "N"),
        demo_vision == "S"
      ),
      demo_impairment = !(demo_impairment == "N"),
      group = case_when(
        country == "UK" & test_language == "Catalan" ~ "cat-ENG",
        country == "UK" & test_language == "Spanish" ~ "spa-ENG",
        .default = "cat-SPA"
      ),
      language_l2 = if_else(is.na(language_l2), "None", language_l2),
      language_l1 = if_else(str_detect(group, "ENG"), "ENG", "SPA"),
      across(matches("language_"), str_trim),
      across(matches("language_"), \(x) if_else(x == "No", "None", x)),
      across(matches("writ|oral"), as.integer)
    ) |>
    rename_with(
      \(x) gsub(pattern = "demo_|language_|setup_", replacement = "", x),
      everything()
    ) |>
    select(-trial_id)

  return(exp_raw)
}

#' Process responses from Experiments 1 and 3
#'
get_exp_processed <- function(exp_raw, stimuli) {
  exp_processed <- exp_raw |>
    mutate(
      age = max(age, na.rm = TRUE),
      key_press_time = key_press_time - 1,
      response = str_to_lower(response),
      date = lubridate::as_datetime(date),
      vision = !vision,
      across(matches("language_|demo_|setup_"), first_non_na),
      .by = participant_id
    ) |>
    # for each participant, select the first non-missing value of the following variables:
    mutate(
      correction = first_non_na(error) == "yes",
      .by = c(participant_id, word)
    ) |> # for each participant and trial, convert first non-missing argument into logical)
    drop_na(test_language) |> # filter out rows without relevant info
    relocate(
      participant_id,
      group,
      test_language,
      country,
      word,
      response,
      key_pressed,
      key_press_time,
      error
    ) |>
    # aggregate by trial (take only one data point per trial)
    summarise(
      response = last_non_na(response),
      typing_onset = first_non_na(key_press_time),
      typing_offset = last_non_na(key_press_time),
      .by = c(
        participant_id,
        group,
        date,
        test_language,
        word,
        age,
        sex,
        l1,
        l2,
        l2oral,
        l2written,
        catalan_oral,
        catalan_written,
        spanish_oral,
        spanish_written,
        country,
        city,
        vision,
        impairment,
        location,
        noise
      )
    ) |>
    select(
      participant_id,
      group,
      date,
      age,
      gender = sex,
      word_1 = word,
      response,
      l1,
      l2,
      l2oral,
      l2written,
      catalan_written,
      catalan_oral,
      spanish_oral,
      spanish_written,
      has_vision_problems = vision,
      has_language_problems = impairment
    )

  return(exp_processed)
}


#' Get participant-level information from participants in Experiments 1 and 3
#'
get_exp_participants <- function(exp_processed, ...) {
  extra_info <- distinct(exp_processed, participant_id, .keep_all = TRUE)

  valid_response_types <- c("correct", "typo", "wrong", "false_friend")
  correct_codes <- c("correct", "typo")

  exp_participants <- file.path("data", "experiment-manual-coded.xlsx") |>
    read_xlsx() |>
    # code valid and correct responses
    mutate(
      participant_id = str_trunc(participant_id, width = 10, side = "right"),
      valid_response = response_type %in% valid_response_types,
      correct_coded = response_type %in% correct_codes
    ) |>
    # get proportion of correct trials per participant
    summarise(
      n_trials = n(), # total number of trials
      # total number of valid trials
      n_trials_valid = sum(valid_response, na.rm = TRUE),
      # total number of correct trials
      n_trials_correct = sum(correct_coded, na.rm = TRUE),
      # proportion of correct trial (out of valid trials)
      prop_correct = n_trials_correct / n_trials_valid,
      .by = c(participant_id, group)
    ) |>
    # add extra info
    inner_join(extra_info, by = join_by(participant_id, group)) |>
    # participant is valid if has completed >= 80% trials (valid)
    validate_participants() |>
    rename(
      l2_oral_comp = l2oral,
      l2_writ_prod = l2written,
      cat_oral_comp = catalan_oral,
      cat_writ_prod = catalan_written,
      spa_oral_comp = spanish_oral,
      spa_writ_prod = spanish_written
    ) |>
    select(
      group,
      participant_id,
      date,
      age,
      gender,
      l2,
      l2_oral_comp,
      l2_writ_prod,
      cat_oral_comp,
      cat_writ_prod,
      spa_oral_comp,
      spa_writ_prod,
      valid_status,
      n_trials,
      n_trials_valid
    ) |>
    arrange(date)

  out_path <- file.path("data", "participants.csv")
  arrow::write_csv_arrow(exp_participants, out_path)
  cli_alert_success("Saved {.emph exp_participants} as {.file {out_path}}")

  return(exp_participants)
}


#' Make dataset with responses from Experiments 1 and 3
#'
get_exp_responses <- function(exp_participants, stimuli) {
  stimuli_tmp <- clean_stimuli(stimuli)

  valid_response_types <- c("correct", "typo", "wrong", "false_friend")
  correct_codes <- c("correct", "typo")

  # process responses
  exp_responses <- file.path("data", "experiment-manual-coded.xlsx") |>
    read_xlsx() |>
    rename(response = input_text, word_1 = word) |>
    mutate(
      participant_id = str_trunc(participant_id, width = 10, side = "right"),
      valid_response = response_type %in% valid_response_types,
      correct = response_type %in% correct_codes,
      group = as.factor(group)
    ) |>
    # this step filters out invalid presented words
    inner_join(stimuli_tmp, join_by(group, word_1)) |>
    left_join(
      select(exp_participants, participant_id, group, valid_status),
      by = join_by(participant_id, group)
    ) |>
    relocate(group, trial_id) |>
    # typos are considered correct responses
    arrange(trial_id, group) |>
    mutate(valid_participant = valid_status == "Valid") |>
    drop_na(correct) |>
    select(
      group,
      participant_id,
      word_1,
      response,
      correct,
      response_type,
      valid_status,
      valid_response,
      valid_participant
    )

  out_path <- file.path("data", "experiment.csv")
  arrow::write_csv_arrow(exp_responses, out_path)
  cli_alert_success("Saved {.emph exp_responses} as {.file {out_path}}")

  return(exp_responses)
}

#' Clean input text
#'
clean_input_text <- function(x) {
  {
    {
      x
    }
  } %>%
    str_to_sentence() %>%
    str_replace("Lshift|space|minus", "") %>%
    as.character() %>%
    as_tibble(x = .) %>%
    mutate(
      .,
      value = case_when(
        nchar(value) > 12 ~ "Several",
        value %in% c("Francés", "Frances", "Basic french") ~ "French",
        value %in% c("Italiano", "Italino") ~ "Italian",
        value %in% c("Alemán") ~ "German",
        value %in% c("NrLondon") ~ "London",
        value %in% c("Rnorthampton") ~ "London",
        value %in% c("Newcastleminusuponminustyne") ~ "Newcastle upon Tyne",
        value %in% c("Newcastlespaceuk") ~ "Newcastle",
        value %in% c("Miltonkeynes") ~ "Milton Keynes",
        value %in% c("Irthlingboroug") ~ "Irthlingborough",
        value %in% c("spalding", "berkshire", "bedfordshire") ~
          str_to_sentence(value),
        value %in% c("No", "Cuál", "Space") ~ NA_character_,
        TRUE ~ value
      )
    ) %>%
    pull(value)
}
