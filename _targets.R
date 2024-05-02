suppressWarnings({
    library(tarchetypes)
    library(dplyr)
    library(tidyr)
    library(stringr)
    library(ggplot2)
    library(ggdist)
    library(beeswarm)
    library(readxl)
    library(brms)
    library(cmdstanr)
    library(stringdist)
    library(cli)
    library(readr)
    library(purrr)
})

# load functions
invisible({
    lapply(list.files("R", pattern = ".R$", full.names = TRUE), 
           \(x) source(x, encoding = "UTF-8"))
})

# set number of cores to use with brms
options(mc.cores = 4,
        brms.backend = "cmdstanr")


list(
    # CLEARPOND database
    tar_target(cp_download, download_clearpond()),
    tar_target(cp_c_path_eng, "data-raw/clearpond/englishCPdatabase2.txt", format = "file"),
    tar_target(cp_h_path_eng, "data-raw/clearpond/clearpondHeaders_EN.txt", format = "file"),
    tar_target(cp_c_path_spa, "data-raw/clearpond/spanishCPdatabase2.txt", format = "file"),
    tar_target(cp_h_path_spa, "data-raw/clearpond/clearpondHeaders_SP.txt", format = "file"),
    
    tar_target(clearpond, import_clearpond(cp_c_path_eng,
                                           cp_c_path_spa,
                                           cp_h_path_eng,
                                           cp_h_path_spa)),
    
    # stimuli ------------------------------------------------------------------
    tar_target(trial_list_path, file.path("stimuli", "trials.xlsx"),
               format = "file"),
    tar_target(trial_list, get_trial_list(trial_list_path)),
    # exclude some stimuli:
    # corona: problematic after COVID-19
    # moneda: two possible correct responses (money, coin)
    # lengua: two correct responses (language, tongue)
    # porc: two possible correct responses (pork, pig)
    # ola: homophone with translation of "hello" ("hola")
    # galeta: two possible correct responses (biscuit, cookie)
    tar_target(stimuli_exclude, 
               c("corona", "moneda", "lengua", "porc", "ola", "biscuit")),
    # get data on cross-language Levenshtein distance
    tar_target(levenshtein, get_levenshtein(trial_list)),
    
    # get audio durations
    tar_target(audios_path, "stimuli/sounds"),
    tar_target(durations, get_duration(trial_list, audios_path)),
    
    # join all stimuli data
    tar_target(stimuli, 
               get_stimuli(trial_list = trial_list, 
                           levenshtein = levenshtein,
                           durations = durations,
                           corpus = clearpond,
                           stimuli_exclude = stimuli_exclude)),
    
    # experiment responses -----------------------------------------------------
    tar_target(exp_raw_files_path, "data-raw/experiment/"),
    tar_target(exp_raw_files,
               list.files(exp_raw_files_path, full.names = TRUE),
               format = "file"),
    tar_target(exp_raw, get_exp_raw(exp_raw_files)),
    tar_target(exp_processed, get_exp_processed(exp_raw, stimuli)),
    tar_target(exp_participants, get_exp_participants(exp_processed)),
    tar_target(exp_responses, get_exp_responses(exp_participants, stimuli)),
    
    # questionnaire responses --------------------------------------------------
    tar_target(quest_raw_files_path, "data-raw/questionnaire/"),
    tar_target(question_raw_files,
               list.files(quest_raw_files_path, full.names = TRUE),
               format = "file"),
    tar_target(quest_raw, get_quest_raw(question_raw_files)),
    tar_target(quest_processed, get_quest_processed(quest_raw)),
    tar_target(quest_participants, get_quest_participants(quest_processed)),
    tar_target(quest_responses, get_quest_responses(quest_processed, quest_participants, stimuli)),
    
    # merge datasets -----------------------------------------------------------
    tar_target(participants, get_participants(exp_participants, quest_participants)),
    tar_target(dataset_1, get_dataset_1(exp_responses, quest_responses, stimuli)),
    tar_target(dataset_2, get_dataset_2(exp_responses, quest_responses, stimuli)),
    tar_target(dataset_3, get_dataset_3(exp_responses, quest_responses, stimuli)),
    
    # models -------------------------------------------------------------------
    
    tar_target(model_prior,
               c(prior(normal(0, 0.1), class = "Intercept"),
                 prior(normal(0, 0.1), class = "b"),
                 prior(exponential(3), class = "sd"),
                 prior(lkj(5), class = "cor"))),
    
    ## analysis 1
    tar_target(fit_0a,
               brm(correct ~
                       1  + neigh_n_h_std + lv_std + 
                       (1 + neigh_n_h_std + lv_std | participant_id),
                   data = dataset_1,
                   family = bernoulli("logit"),
                   prior = model_prior,
                   save_pars = save_pars(all = TRUE),
                   iter = 1000, chains = 4, seed = 888,
                   control = list(adapt_delta = 0.95),
                   file_refit = "on_change",
                   file = file.path("results", "fit_0a"))),
    tar_target(fit_1a,
               brm(correct ~
                       1  + neigh_n_h_std * lv_std + 
                       (1 + neigh_n_h_std * lv_std | participant_id),
                   data = dataset_1,
                   family = bernoulli("logit"),
                   prior = model_prior,
                   save_pars = save_pars(all = TRUE),
                   iter = 1000, chains = 4, seed = 888,
                   control = list(adapt_delta = 0.95),
                   file_refit = "on_change",
                   file = file.path("results", "fit_1a"))),
    tar_target(fit_0,
               brm(correct ~
                       1 + freq_zipf_2_std + neigh_n_std + lv_std + 
                       (1 + freq_zipf_2_std + neigh_n_std + lv_std | participant_id),
                   data = dataset_1,
                   family = bernoulli("logit"),
                   prior = model_prior,
                   save_pars = save_pars(all = TRUE),
                   iter = 1000, chains = 4, seed = 888,
                   control = list(adapt_delta = 0.95),
                   file_refit = "on_change",
                   file = file.path("results", "fit_0"))),
    
    tar_target(fit_1,
               brm(correct ~
                       1 + freq_zipf_2_std + neigh_n_std*lv_std +  
                       (1 + freq_zipf_2_std + neigh_n_std*lv_std | participant_id),
                   data = dataset_1,
                   family = bernoulli("logit"),
                   prior = model_prior,
                   save_pars = save_pars(all = TRUE),
                   iter = 1000, chains = 4, seed = 888,
                   control = list(adapt_delta = 0.95),
                   file_refit = "on_change",
                   file = file.path("results", "fit_1"))),
    
    # analysis 2
    tar_target(fit_2,
               brm(bf(correct ~
                          1 + freq_zipf_2_std + avg_sim_h_std*lv_std + group + 
                          (1 + freq_zipf_2_std + avg_sim_h_std*lv_std | participant_id) +
                          (1 + group | translation_id)),
                   data = dataset_2,
                   family = bernoulli("logit"),
                   prior = model_prior,
                   save_pars = save_pars(all = TRUE),
                   iter = 1000, chains = 4, seed = 888,
                   control = list(adapt_delta = 0.95),
                   save_model = file.path("stan", "fit_2.stan"),
                   file = file.path("results", "fit_2"))),
    
    
    # get model parameters
    tar_target(parameters_1, model_parameters(fit_1, ci_method = "hdi", test = "pd", verbose = FALSE, ci = 0.95)),
    tar_target(parameters_2, model_parameters(fit_2, ci_method = "hdi", test = "pd", verbose = FALSE, ci = 0.95))
    
    # # render docs ----
    # tar_render(readme, "README.Rmd", priority = 0),
    # #
    # tar_render(docs, "docs/index.Rmd", priority = 0),
    # #
    # tar_render(manuscript, "manuscript/manuscript.Rmd", priority = 0)
)


