library(cli)
library(dplyr)

#' Get participants
#'
get_participants <- function(exp_participants, que_participants) {
  out <- list(
    Experiment = exp_participants,
    Questionnaire = que_participants
  ) |>
    bind_rows(.id = "source")

  return(out)
}

#' Get dataset for analysis
#'
get_dataset <- function(experiment, exp_responses, que_responses, stimuli) {
  if (!(experiment %in% 1:3)) {
    cli_abort("{.code experiment} must be one of 1, 2, or 3")
  }

  dataset <- prepare_data(exp_responses, que_responses, stimuli)

  if (experiment == 1) {
    out <- dataset |>
      dplyr::filter(source == "Experiment", group != "cat-SPA") |>
      mutate(group = factor(group, levels = c("cat-ENG", "spa-ENG")))
    contrasts(out$group) <- c(0.5, -0.5)
  } else if (experiment == 2) {
    out <- dplyr::filter(dataset, group == "cat-SPA")
  } else {
    out <- dataset |>
      dplyr::filter(source == "Questionnaire") |>
      mutate(group = factor(group, levels = c("cat-ENG", "spa-ENG")))
    contrasts(out$group) <- c(0.5, -0.5)
  }

  if (nrow(out) == 0) {
    cli_abort("Dataset has no rows")
  }

  return(out)
}

#' Merge data from Experiment and from Questionnaire and select relevant variables
#'
prepare_data <- function(exp_responses, que_responses, stimuli) {
  stimuli_tmp <- clean_stimuli(stimuli)

  relevant_vars <- c(
    "source",
    "participant_id",
    "group",
    "word_1",
    "response",
    "correct",
    "response_type",
    "confidence",
    "knowledge"
  )

  out <- list(
    Experiment = exp_responses,
    Questionnaire = que_responses
  ) |>
    bind_rows(.id = "source") |>
    dplyr::filter(valid_participant, valid_response) |>
    select(any_of(relevant_vars)) |>
    inner_join(stimuli_tmp, by = join_by(group, word_1)) |>
    mutate(
      across(
        c(freq_zipf_2, neigh_n, neigh_n_h, avg_sim, avg_sim_h, lv),
        \(x) scale(x)[, 1],
        .names = "{.col}_std"
      ),
      group = as.factor(group)
    )

  return(out)
}

#' Get relevant stimuli properties
#'
clean_stimuli <- function(stimuli) {
  out <- stimuli |>
    select(
      group,
      translation,
      translation_id,
      word_1,
      word_2,
      sampa_1,
      sampa_2,
      ipa_1,
      ipa_2,
      freq_zipf_2,
      lv,
      neigh_n,
      neigh_n_h,
      avg_sim,
      avg_sim_h
    ) |>
    mutate(word_1 = replace_non_ascii(word_1))

  return(out)
}
