library(targets)
library(tarchetypes)
library(here)
library(dplyr)
library(tidyr)
library(stringr)
library(readr)
library(purrr)
library(ggplot2)
library(ggdist)
library(beeswarm)
library(readxl)
library(brms)
library(cmdstanr)
library(stringdist)
library(cli)
library(quarto)


# load functions
invisible({
  lapply(
    list.files("scripts", pattern = ".R$", full.names = TRUE),
    \(x) source(x, encoding = "UTF-8")
  )
})

# set number of cores to use with brms
options(mc.cores = 4, brms.backend = "cmdstanr")


list(
  # CLEARPOND database -----
  tar_target(clearpond, import_clearpond()),

  # stimuli -----
  tar_target(trial_list_path, here("data", "trials.xlsx"), format = "file"),
  tar_target(trial_list, get_trial_list(trial_list_path)),
  # exclude some stimuli:
  # corona: problematic after COVID-19
  # moneda: two possible correct responses (money, coin)
  # lengua: two correct responses (language, tongue)
  # porc: two possible correct responses (pork, pig)
  # ola: homophone with translation of "hello" ("hola")
  # galeta: two possible correct responses (biscuit, cookie)
  tar_target(
    stimuli_exclude,
    c("corona", "moneda", "lengua", "porc", "ola", "biscuit")
  ),
  # get data on cross-language Levenshtein distance
  tar_target(levenshtein, get_levenshtein(trial_list)),

  # get audio durations
  tar_target(audios_path, here("sounds")),
  tar_target(durations, get_duration(trial_list, audios_path)),

  # join all stimuli data
  tar_target(
    stimuli,
    get_stimuli(
      trial_list = trial_list,
      levenshtein = levenshtein,
      durations = durations,
      corpus = clearpond,
      stimuli_exclude = stimuli_exclude
    )
  ),
  tar_target(stimuli_file, write_csv(stimuli, here("out", "stimuli.csv"))),

  # experiment responses -----------------------------------------------------
  tar_file(
    exp_raw_files,
    list.files(here("data", "raw", "experiment"), full.names = TRUE),
  ),
  tar_target(exp_raw, get_exp_raw(exp_raw_files)),
  tar_target(exp_processed, get_exp_processed(exp_raw, stimuli)),
  tar_target(exp_participants, get_exp_participants(exp_processed)),
  tar_target(exp_responses, get_exp_responses(exp_participants, stimuli)),
  tar_target(
    exp_participants_file,
    write_csv(exp_participants, here("out", "exp_participants.csv"))
  ),
  tar_target(
    exp_responses_file,
    write_csv(exp_responses, here("out", "exp_responses.csv"))
  ),

  # questionnaire responses --------------------------------------------------
  tar_files(
    que_raw_files,
    list.files(
      here("data", "raw", "questionnaire"),
      full.names = TRUE,
      pattern = "quest"
    ),
  ),
  tar_target(que_raw, get_que_raw(que_raw_files)),
  tar_target(que_processed, get_que_processed(que_raw)),
  tar_target(que_participants, get_que_participants(que_processed)),
  tar_target(
    que_responses,
    get_que_responses(que_processed, que_participants, stimuli)
  ),
  tar_target(
    que_participants_file,
    write_csv(que_participants, here("out", "que_participants.csv"))
  ),
  tar_target(
    que_responses_file,
    write_csv(que_responses, here("out", "que_responses.csv"))
  ),

  # merge datasets -----------------------------------------------------------
  tar_target(
    participants,
    get_participants(exp_participants, que_participants)
  ),
  tar_target(
    participants_file,
    write_csv(participants, here("out", "participants.csv"))
  ),
  tar_target(dataset_1, get_dataset(1, exp_responses, que_responses, stimuli)),
  tar_target(dataset_2, get_dataset(2, exp_responses, que_responses, stimuli)),
  tar_target(dataset_3, get_dataset(3, exp_responses, que_responses, stimuli)),
  tar_target(dataset_12, {
    dataset_12 <- bind_rows(
      list("Experiment 1" = dataset_1, "Experiment 2" = dataset_2),
      .id = "experiment"
    )
    dataset_12$experiment <- as.factor(dataset_12$experiment)
    contrasts(dataset_12$experiment) <- c(-0.5, 0.5)
    return(dataset_12)
  }),
  tar_target(
    dataset_1_file,
    write_csv(dataset_1, here("out", "dataset-1.csv"))
  ),
  tar_target(
    dataset_2_file,
    write_csv(dataset_2, here("out", "dataset-2.csv"))
  ),
  tar_target(
    dataset_3_file,
    write_csv(dataset_3, here("out", "dataset-3.csv"))
  ),

  # models -------------------------------------------------------------------

  tar_target(
    model_prior,
    c(
      prior(normal(0, 0.1), class = "b"),
      prior(exponential(3), class = "sd"),
      prior(lkj(5), class = "cor")
    )
  ),

  # analysis of Experiment 1
  tar_target(
    exp_1_m0,
    get_model_fit(
      "exp_1_m0",
      correct ~
        freq_zipf_2_std +
          neigh_n_h_std * lv_std +
          group +
          (1 + freq_zipf_2_std + neigh_n_h_std * lv_std | participant_id),
      prior = model_prior,
      data = dataset_1
    )
  ),

  # analysis of Experiment 2
  tar_target(
    exp_2_m0,
    get_model_fit(
      "exp_2_m0",
      correct ~
        freq_zipf_2_std +
          neigh_n_h_std * lv_std +
          (1 + freq_zipf_2_std + neigh_n_h_std * lv_std | participant_id),
      prior = model_prior,
      data = dataset_2
    )
  ),

  # analysis of Experiment 3
  tar_target(
    exp_3_m0,
    get_model_fit(
      "exp_3_m0",
      correct ~
        freq_zipf_2_std +
          neigh_n_h_std * lv_std +
          group +
          (1 + freq_zipf_2_std + neigh_n_h_std * lv_std | participant_id),
      prior = model_prior,
      data = dataset_3
    )
  ),
  tar_target(
    exp_3_m1,
    get_model_fit(
      "exp_3_m1",
      correct ~
        freq_zipf_2_std +
          neigh_n_h_std * lv_std +
          group +
          (1 + freq_zipf_2_std + neigh_n_h_std * lv_std | participant_id),
      prior = model_prior,
      data = filter(dataset_3, !knowledge)
    )
  ),
  tar_target(
    exp_12_m0,
    get_model_fit(
      "exp_12_m0",
      correct ~
        freq_zipf_2_std +
          neigh_n_h_std * lv_std * experiment +
          (1 + freq_zipf_2_std + neigh_n_h_std * lv_std | participant_id),
      prior = model_prior,
      data = dataset_12
    )
  )
)
