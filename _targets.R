library(targets)
library(tarchetypes)

# load functions
source("R/utils.R", encoding = "UTF-8")
source("R/00_stimuli.R", encoding = "UTF-8")
source("R/01_responses.R", encoding = "UTF-8")
source("R/02_models.R", encoding = "UTF-8")
source("R/03_questionnaire.R", encoding = "UTF-8")


# set number of cores to use with brms
options(
    mc.cores = 1
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
        "multilex",
        "keyring",
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
        "wesanderson", 
        "papaja", 
        "knitr", 
        "data.table",
        "audio",
        "tidytext",
        "bayesplot",
        "performance",
        "httr",
        "ggrepel"
    ), 
)

conflicted::conflict_prefer("filter", "dplyr")
conflicted::conflict_prefer("first", "dplyr")
conflicted::conflict_prefer("last", "dplyr")
conflicted::conflict_prefer("between", "dplyr")

list(
    # stimuli ----
    
    tar_target(stimuli_path, "stimuli/trials.xlsx", format = "file"),
    
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
            neighbours = neighbours
        )
    ),
    
    # responses ----
    tar_target(responses_path, list.files("data/raw", full.names = TRUE)),
    
    tar_target(responses_processed, get_responses_processed(responses_path = responses_path, stimuli = stimuli)),
    
    tar_target(responses_clean, get_responses_clean(responses_processed = responses_processed, stimuli = stimuli)),
    
    # manually coded responses
    tar_target(responses_coded_path, "data/processed/02_coded.xlsx"),
    
    tar_target(responses_coded, read_xlsx(responses_coded_path)),
    
    tar_target(participants, get_participants(responses_processed = responses_processed, responses_coded = responses_coded)),
    
    tar_target(responses, get_responses(responses_coded = responses_coded, participants = participants, stimuli = stimuli),),
    
    # models ----
    
    # model formulas (adding fixed effects, one at a time)
    tar_target(
        model_formulas,
        lst(
            f_0 = bf(
                correct ~ 1 + 
                    (1 | participant_id) + 
                    (1 | translation_id)
            ),
            f_1 = bf(
                correct ~ 1 + 
                    freq_zipf_2_std +
                    (1 + freq_zipf_2_std | participant_id) + 
                    (1 | translation_id)
            ),
            f_2 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std + 
                    (1 + freq_zipf_2_std + nd_std | participant_id) +
                    (1 | translation_id)
            ),
            f_3 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std + lv_std + 
                    (1 + freq_zipf_2_std + nd_std + lv_std | participant_id) +
                    (1 | translation_id)
            ),
            f_4 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std*lv_std + 
                (1 + freq_zipf_2_std + nd_std*lv_std | participant_id) +
                    (1 | translation_id)
            )
        )
    ),
    
    # model prior
    tar_target(
        model_prior,
        c(
            prior(normal(0, 0.1), class = "Intercept"),
            prior(normal(0, 0.1), class = "b"),
            prior(exponential(3), class = "sd"),
            prior(lkj(8), class = "cor")
        )
    ),
    
    # fit models
    tar_target(fit_0, get_model_fit(name = "fit_0", formula = model_formulas$f_0, data = responses, prior = model_prior[c(1, 3),])),
    tar_target(fit_1, get_model_fit(name = "fit_1", formula = model_formulas$f_1, data = responses, prior = model_prior)),
    tar_target(fit_2, get_model_fit(name = "fit_2", formula = model_formulas$f_2, data = responses, prior = model_prior)),
    tar_target(fit_3, get_model_fit(name = "fit_3", formula = model_formulas$f_3, data = responses, prior = model_prior)),
    tar_target(fit_4, get_model_fit(name = "fit_4", formula = model_formulas$f_4, data = responses, prior = model_prior)),

    # leave-one-out cross-validation (compare models' predictive accuracy)
    tar_target(model_loos, loo_compare(map(lst(fit_0, fit_1, fit_2, fit_3, fit_4),loo))),
    
    #### study 2: questionnaire ################################################
    
    tar_target(questionnaire_data_raw, get_questionnaire_data_raw()),
    
    tar_target(questionnaire_participants, get_questionnaire_participants(questionnaire_data_raw)),
    
    tar_target(questionnaire_data_processed, get_questionnaire_data_processed(questionnaire_data_raw)),
    
    tar_target(questionnaire_data_clean, get_questionnaire_data_clean(questionnaire_participants)),
    
    tar_target(questionnaire_responses, get_questionnaire_responses(questionnaire_data_clean, stimuli)),
    
    
    # models ----
    
    # model formulas (adding fixed effects, one at a time)
    tar_target(
        questionnaire_model_formulas,
        lst(
            questionnaire_f_0 = bf(
                correct ~ 1 + 
                    (1 | participant_id) + 
                    (1 | translation_id)
            ),
            questionnaire_f_1 = bf(
                correct ~ 1 + 
                    freq_zipf_2_std +
                    (1 + freq_zipf_2_std | participant_id) + 
                    (1 | translation_id)
            ),
            questionnaire_f_2 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std + 
                    (1 + freq_zipf_2_std + nd_std | participant_id) +
                    (1 | translation_id)
            ),
            questionnaire_f_3 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std + lv_std + 
                    (1 + freq_zipf_2_std + nd_std + lv_std | participant_id) +
                    (1 | translation_id)
            ),
            questionnaire_f_4 = bf(
                correct ~ 1 + freq_zipf_2_std + nd_std*lv_std + nd_std + 
                    (1 + freq_zipf_2_std + nd_std*lv_std | participant_id) + 
                    (1  | translation_id)
            )
        )
    ),
    
    # fit models
    tar_target(questionnaire_fit_0, get_model_fit(name = "questionnaire_fit_0", formula = questionnaire_model_formulas$questionnaire_f_0, data = questionnaire_responses, prior = model_prior[c(1, 3),])),
    tar_target(questionnaire_fit_1, get_model_fit(name = "questionnaire_fit_1", formula = questionnaire_model_formulas$questionnaire_f_1, data = questionnaire_responses, prior = model_prior)),
    tar_target(questionnaire_fit_2, get_model_fit(name = "questionnaire_fit_2", formula = questionnaire_model_formulas$questionnaire_f_2, data = questionnaire_responses, prior = model_prior)),
    tar_target(questionnaire_fit_3, get_model_fit(name = "questionnaire_fit_3", formula = questionnaire_model_formulas$questionnaire_f_3, data = questionnaire_responses, prior = model_prior)),
    tar_target(questionnaire_fit_4, get_model_fit(name = "questionnaire_fit_4", formula = questionnaire_model_formulas$questionnaire_f_4, data = questionnaire_responses, prior = model_prior)),

    # leave-one-out cross-validation (compare models' predictive accuracy)
    tar_target(questionnaire_model_loos, loo_compare(map(lst(questionnaire_fit_0, questionnaire_fit_1, questionnaire_fit_2, questionnaire_fit_3, questionnaire_fit_4),loo)))
    
    # # render docs ----
    # tar_render(readme, "README.Rmd", priority = 0),
    # #
    # tar_render(docs, "docs/index.Rmd", priority = 0),
    # #
    # tar_render(manuscript, "manuscript/manuscript.Rmd", priority = 0)
)


