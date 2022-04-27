library(targets)
library(tarchetypes)

# load functions
source("R/utils.R", encoding = "UTF-8")
source("R/00_stimuli.R", encoding = "UTF-8")
source("R/01_responses.R", encoding = "UTF-8")
source("R/02_models.R", encoding = "UTF-8")

# set number of cores to use with brms
options(
    mc.cores = 1,
    encoding = "UTF-8"
)

# set parameters
tar_option_set(
    # manifest dependencies (via tar_renv)
    packages = c(
        "dplyr", 
        "tidyr", 
        "stringr",
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
        "httr"
    ), 
)

list(
    # stimuli ----
    
    # get SUBTLEX data
    tar_target(
        subtlex,
        get_subtlex()
    ),
    
    # get data on lexical frequency and phonological neighbourhood density
    tar_target(
        clearpond_path, 
        lst(
            `ENG-CAT` = here("data", "clearpond", "clearpond_english.csv"), 
            `ENG-SPA` = here("data", "clearpond", "clearpond_english.csv"), 
            `SPA-CAT` = here("data", "clearpond", "clearpond_spanish.csv")
        )
    ),
    tar_target(
        clearpond, 
        get_clearpond(clearpond_path)
    ),
    tar_target(
        stimuli_path, 
        "stimuli/trials.xlsx", 
        format = "file"
    ),
    
    # get data on cross-language Levenshtein distance
    tar_target(
        levenshtein, 
        get_levenshtein(stimuli_path = stimuli_path)
    ),
    
    # get audio durations
    tar_target(
        audios_path, 
        "stimuli/sounds"
    ),
    tar_target(
        durations, 
        get_duration(
            stimuli_path = stimuli_path,
            audios_path = audios_path
        )
    ),
    
    # join all stimuli data
    tar_target(
        stimuli, 
        get_stimuli(
            stimuli_path = stimuli_path, 
            clearpond = clearpond,
            levenshtein = levenshtein,
            durations = durations)
    ),
    tar_target(
        practice_trials, 
        c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)
    ),
    
    # responses ----
    tar_target(
        responses_path,
        list.files("data/raw", full.names = TRUE)
    ),
    tar_target(
        responses_processed, 
        get_responses_processed(
            responses_path = responses_path, 
            stimuli = stimuli,
            practice_trials = practice_trials)
    ),
    tar_target(
        responses_clean, 
        get_responses_clean(
            responses_processed = responses_processed, 
            stimuli = stimuli
        )
    ),
    # manually coded responses
    tar_target(
        responses_coded_path,
        "data/processed/02_coded.xlsx"
    ),
    tar_target(
        responses_coded, 
        read_xlsx(responses_coded_path)
    ),
    tar_target(
        participants, 
        get_participants(
            responses_processed = responses_processed,
            responses_coded = responses_coded
        )
    ),
    tar_target(
        responses,
        get_responses(
            responses_coded = responses_coded, 
            practice_trials = practice_trials,
            participants = participants, 
            stimuli = stimuli
        )
    ),
    
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
                    frequency_zipf_std +
                    (1 + frequency_zipf_std | participant_id) + 
                    (1 | translation_id)
            ),
            f_2 = bf(
                correct ~ 1 + 
                    frequency_zipf_std +
                    pthn_std + 
                    (1 + frequency_zipf_std + pthn_std | participant_id) +
                    (1 | translation_id)
            ),
            f_3 = bf(
                correct ~ 1 + 
                    frequency_zipf_std +
                    pthn_std + 
                    lv_std +
                    (1 + frequency_zipf_std + pthn_std + lv_std | participant_id) +
                    (1 | translation_id)
            ),
            f_4 = bf(
                correct ~ 1 + 
                    frequency_zipf_std +
                    pthn_std + 
                    lv_std + 
                    pthn_std:lv_std + 
<<<<<<< HEAD
                    (1 + frequency_zipf_std + pthn_std*lv_std | participant_id) + 
                    (1 | translation_id)
            )
=======
                    (1 + frequency_zipf_std + pthn_std*lv_std | participant) + 
                    (1 | word)
            ),
            f_5 = bf(
                correct ~ 1 + 
                    frequency_zipf_std +
                    pthn_std + 
                    lv_std + 
                    lv_std:pthn_std + 
                    group +
                    (1 + frequency_zipf_std + pthn_std + lv_std + lv_std:pthn_std | participant) + 
                    (1 + group | word)
            ),
            f_6 = bf(
                correct ~ 1 +
                    frequency_zipf_std +
                    pthn_std + 
                    lv_std + 
                    lv_std:pthn_std + 
                    group + 
                    group:lv_std +
                    (1 + frequency_zipf_std + pthn_std + lv_std + lv_std:pthn_std + group +group:lv_std | participant) + 
                    (1 | word))
>>>>>>> eb2ad2e01316fbb4878ef163afbb685d3a91ad49
        )
    ),
    # model prior
    tar_target(
        model_prior,
        c(
            prior(normal(0, 0.1), class = "Intercept"),
            prior(normal(0, 0.1), class = "b"),
            prior(cauchy(0, 0.1), class = "sd"),
            prior(lkj(8), class = "cor")
        )
    ),
    
    # fit models
    tar_target(
        fit_0, 
        get_model_fit(
            name = "fit_0",
            formula = model_formulas$f_0,
            data = responses,
            prior = model_prior[c(1, 3), ]
        )
    ),
    tar_target(
        fit_1, 
        get_model_fit(
            name = "fit_1", 
            formula = model_formulas$f_1, 
            data = responses, 
            prior = model_prior
        )
    ),
    tar_target(
        fit_2, 
        get_model_fit(
            name = "fit_2", 
            formula = model_formulas$f_2, 
            data = responses, 
            prior = model_prior
        )
    ),
    tar_target(
        fit_3, 
        get_model_fit(
            name = "fit_3", 
            formula = model_formulas$f_3,
            data = responses,
            prior = model_prior
        )
    ),
    tar_target(
        fit_4,
        get_model_fit(
            name = "fit_4", 
            formula = model_formulas$f_4,
            data = responses, 
            prior = model_prior
        )
    ),
    
    # leave-one-out cross-validation (compare models' predictive accuracy)
    tar_target(
        model_loos, 
        get_model_loos(
            lst(
                fit_0,
                fit_1,
                fit_2,
                fit_3,
                fit_4
            )
        )
    ),
    
<<<<<<< HEAD
    # posterior draws of population- and group-level effects, and predictions
    tar_target(
        posterior_draws_fixed,
        get_model_draws_fixed(fit_4)
    ),
    tar_target(
        posterior_epreds_fixed, 
        get_model_epreds_fixed(fit_4)
    ),
    tar_target(
        posterior_draws_random,
        get_model_draws_random(fit_4)
    ),
    tar_target(
        posterior_epreds_random, 
        get_model_epreds_random(
            fit_4, 
            group = "participant"
        )
    )
    
    # render docs ----
    # tar_render(readme, "README.Rmd"),
    # 
    # tar_render(docs, "docs/index.Rmd"),
=======
    # render docs ----
    tar_render(readme, "README.Rmd")
    # 
    # tar_render(docs, "docs/index.Rmd")
>>>>>>> eb2ad2e01316fbb4878ef163afbb685d3a91ad49
    # 
    # tar_render(manuscript, "manuscript/manuscript.Rmd")
)



