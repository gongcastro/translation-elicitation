library(targets)
library(tarchetypes)

source("R/utils.R")
source("R/00_stimuli.R")
source("R/01_responses.R")
source("R/02_models.R")

# set parameters
tar_option_set(
    packages = c(
        "dplyr", "tidyr", "stringr", "ggplot2", "tibble", "forcats", "multilex", "keyring",
        "readxl", "janitor", "mice", "here", "lubridate", "purrr", "scales", "stringdist",
        "brms", "tidybayes", "gt", "patchwork", "wesanderson", "papaja", "knitr", "data.table",
        "audio", "tidytext", "bayesplot"
    )
)

list(
    
    # stimuli
    tar_target(clearpond_path, list(`ENG-CAT` = here("Data", "clearpond", "clearpond_english.csv"), `ENG-SPA` = here("Data", "clearpond", "clearpond_english.csv"), `SPA-CAT` = here("Data", "clearpond", "clearpond_spanish.csv")),),
    tar_target(clearpond, get_clearpond(clearpond_path)),
    tar_target(stimuli_path, here("Stimuli", "trials.xlsx")),
    tar_target(levenshtein, get_levenshtein(stimuli_path = stimuli_path)),
    tar_target(audios_path, here("Stimuli/Sounds")),
    tar_target(durations, get_duration(stimuli_path = stimuli_path, audios_path = audios_path)),
    tar_target(stimuli, get_stimuli(stimuli_path = stimuli_path, clearpond = clearpond, levenshtein = levenshtein, durations = durations)),
    tar_target(practice_trials, c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)),
    
    # responses
    tar_target(responses_path, list.files(here("Data", "Raw"), full.names = TRUE)),
    tar_target(responses_processed, get_responses_processed(responses_path = responses_path, stimuli = stimuli, practice_trials = practice_trials)),
    tar_target(responses_clean, get_responses_clean(responses_processed = responses_processed, stimuli = stimuli)),
    tar_target(responses_coded_path, here("Data", "02_coded.xlsx")),
    tar_target(responses_coded, read_xlsx(responses_coded_path)),
    tar_target(participants, get_participants(responses_processed = responses_processed,responses_coded = responses_coded)),
    tar_target(responses, get_responses(responses_coded = responses_coded, practice_trials = practice_trials, participants = participants, stimuli = stimuli)),
    
    # models
    tar_target(
        model_formulas,
        formulas <- list(
            f_0 = bf(correct ~ 1 + 
                         (1 | participant),
                     family = bernoulli(link = "logit")),
            f_1 = bf(correct ~ 1 + 
                         frequency_zipf + 
                         (1 + frequency_zipf | participant),
                     family = bernoulli(link = "logit")),
            f_2 = bf(correct ~ 1 + 
                         frequency_zipf +
                         pthn + 
                         (1 + frequency_zipf + pthn | participant),
                     family = bernoulli(link = "logit")),
            f_3 = bf(correct ~ 1 +
                         frequency_zipf +
                         pthn*lv +
                         (1 + frequency_zipf + pthn*lv | participant),
                     family = bernoulli(link = "logit"))
        )
    ),
    tar_target(
        model_prior,
        # prior
        c(
            prior(normal(0, 0.1), class = "Intercept"),
            prior(normal(0, 0.1), clas = "b"),
            prior(cauchy(0, 0.1), class = "sd", group = "participant"),
            prior(lkj(8), class = "cor")
        )
    ),
    tar_target(
        model_fits,
        get_model_fits(responses = responses, model_formulas = model_formulas, model_prior = model_prior)
    ),
    tar_target(
        model_loos,
        get_model_loos(model_fits)
    ),
    tar_target(
        posterior_draws_fixed,
        get_model_draws_fixed(model_fits$fit_3)
    ),
    tar_target(
        posterior_epreds_fixed,
        get_model_epreds_fixed(model_fits$fit_3)
    ),
    tar_target(
        posterior_epreds_random,
        get_model_epreds_random(model_fits$fit_3)
    ),
    
    # render report.Rmd
    # tar_render(report, "Rmd/report.Rmd"),
    
    # render manuscript.Rmd
    tar_render(manuscript, "Rmd/manuscript.Rmd")
)



