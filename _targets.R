library(targets)
library(tarchetypes)

# load functions
source("R/utils.R", encoding = "UTF-8")
source("R/00_stimuli.R", encoding = "UTF-8")
source("R/01_experiment.R", encoding = "UTF-8")
source("R/02_questionnaire.R", encoding = "UTF-8")
source("R/03_merged.R", encoding = "UTF-8")
source("R/04_models.R", encoding = "UTF-8")

# set number of cores to use with brms
options(
    mc.cores = 4,
    brms.backend = "cmdstanr"
)

# set parameters
tar_option_set(
    # manifest dependencies (via tar_renv)
    packages = c(
        "arrow",
        "dplyr", 
        "tidyr", 
        "stringr",
        "readr",
        "ggplot2",
        "tibble", 
        "forcats",
        "readxl",
        "janitor", 
        "mice", 
        "here", 
        "lubridate", 
        "purrr", 
        "scales", 
        "stringdist",
        "brms", 
        "tidybayes",
        "gt", 
        "patchwork", 
        "papaja", 
        "knitr", 
        "data.table",
        "audio",
        "tidytext",
        "bayesplot",
        "parameters",
        "httr",
        "ggrepel"
    )
)

conflicted::conflict_prefer("filter", "dplyr")
conflicted::conflict_prefer("first", "dplyr")
conflicted::conflict_prefer("last", "dplyr")
conflicted::conflict_prefer("between", "dplyr")

list(
    # stimuli ------------------------------------------------------------------
    
    tar_target(stimuli_path, "stimuli/trials.xlsx", format = "file"),
    
    tar_target(
        stimuli_exclude,
        c(
            "corona", # problematic, given COVID-19
            "moneda", # 2 correct responses: money, coin
            "lengua", # 2 correct responses: language, tongue
            "porc"    # 2 correct responses: pork, pig
        )
    ),
    
    # get data on cross-language Levenshtein distance
    tar_target(levenshtein, get_levenshtein(stimuli_path = stimuli_path)),
    
    # get audio durations
    tar_target(audios_path, "stimuli/sounds"),
    
    tar_target(durations, get_duration(stimuli_path = stimuli_path, audios_path = audios_path)),
    
    tar_target(neighbours, get_neighbours(stimuli_path, "across")),
    
    # join all stimuli data
    tar_target(
        stimuli, 
        get_stimuli(
            stimuli_path = stimuli_path, 
            levenshtein = levenshtein,
            durations = durations,
            neighbours = neighbours,
            stimuli_exclude = stimuli_exclude
        )
    ),
    
    # experiment responses -----------------------------------------------------
    tar_target(exp_raw, get_exp_raw()),
    tar_target(exp_processed, get_exp_processed(exp_raw, stimuli)),
    tar_target(exp_participants, get_exp_participants(exp_processed)),
    tar_target(exp_responses, get_exp_responses(exp_participants, stimuli)),
    
    # questionnaire responses --------------------------------------------------
    tar_target(quest_raw, get_quest_raw()),
    tar_target(quest_processed, get_quest_processed(quest_raw)),
    tar_target(quest_participants, get_quest_participants(quest_processed)),
    tar_target(quest_responses, get_quest_responses(quest_processed, quest_participants, stimuli)),
    
    # merge datasets -----------------------------------------------------------
    tar_target(dataset_1, get_dataset_1(exp_responses, quest_responses, stimuli)),
    tar_target(dataset_2, get_dataset_2(exp_responses, quest_responses, stimuli)),
    tar_target(dataset_3, get_dataset_3(exp_responses, quest_responses, stimuli)),
    
    # models -------------------------------------------------------------------
    
    tar_target(
        model_prior,
        c(prior(normal(0, 0.1), class = "Intercept"),
          prior(normal(0, 0.1), class = "b"),
          prior(exponential(3), class = "sd"),
          prior(lkj(5), class = "cor"))
    ),
    
    ## analysis 1
    tar_target(
        fit_1,
        brm(
            bf(correct ~ 1 + freq_zipf_2_std + nd_std*lv_std + group + lv_std:group +  
                   (1 + freq_zipf_2_std + nd_std*lv_std | participant_id) +
                   (1 + group | translation_id)),
            data = dataset_1,
            family = bernoulli("logit"),
            prior = model_prior,
            save_pars = save_pars(all = TRUE),
            iter = 1000, chains = 4, seed = 888,
            control = list(adapt_delta = 0.95),
            save_model = "stan/fit_1.stan",
            file = "results/fit_1",
            sample_prior = "yes"
        )
    ),
    
    # analysis 2
    tar_target(
        fit_2,
        brm(
            bf(correct ~ 1 + freq_zipf_2_std + nd_std*lv_std + group + 
                   (1 + freq_zipf_2_std + nd_std*lv_std | participant_id) +
                   (1 + group | translation_id)),
            data = dataset_2,
            family = bernoulli("logit"),
            prior = model_prior,
            save_pars = save_pars(all = TRUE),
            iter = 1000, chains = 4, seed = 888,
            control = list(adapt_delta = 0.95),
            save_model = "stan/fit_2.stan",
            file = "results/fit_2",
            sample_prior = "yes"
        )
    ),
    
    
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


