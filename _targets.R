library(targets)
library(tarchetypes)

source("scripts/R/utils.R")
source("scripts/R/00_stimuli.R")
source("scripts/R/01_responses.R")
source("scripts/R/02_models.R")

# set parameters
tar_option_set(
    packages = c(
        "dplyr", "tidyr", "stringr", "ggplot2", "tibble", "forcats", "multilex", "keyring",
        "readxl", "janitor", "mice", "here", "lubridate", "purrr", "scales", "stringdist",
        "brms", "tidybayes", "gt", "patchwork", "wesanderson", "papaja", "knitr", "data.table",
        "audio", "tidytext", "bayesplot", "GGally", "performance"
    )
)

list(
    # stimuli
<<<<<<< HEAD
    tar_target(clearpond_path, list(`ENG-CAT` = here("data", "clearpond", "clearpond_english.csv"), `ENG-SPA` = here("Data", "clearpond", "clearpond_english.csv"), `SPA-CAT` = here("Data", "clearpond", "clearpond_spanish.csv")),),
=======
    tar_target(clearpond_path, list(`ENG-CAT` = here("data", "clearpond", "clearpond_english.csv"), `ENG-SPA` = here("Data", "clearpond", "clearpond_english.csv"), `SPA-CAT` = here("data", "clearpond", "clearpond_spanish.csv")),),
>>>>>>> c92465ffee5b01a15c56bc645bd58fd50fe89122
    tar_target(clearpond, get_clearpond(clearpond_path)),
    tar_target(stimuli_path, here("stimuli", "trials.xlsx")),
    tar_target(levenshtein, get_levenshtein(stimuli_path = stimuli_path)),
    tar_target(audios_path, here("stimuli", "sounds")),
    tar_target(durations, get_duration(stimuli_path = stimuli_path, audios_path = audios_path)),
    tar_target(stimuli, get_stimuli(stimuli_path = stimuli_path, clearpond = clearpond, levenshtein = levenshtein, durations = durations)),
    tar_target(practice_trials, c(109, 147, 159, 167, 179, 1, 26, 70, 86, 96)),
    
    # responses
    tar_target(responses_path, list.files(here("data", "raw"), full.names = TRUE)),
    tar_target(responses_processed, get_responses_processed(responses_path = responses_path, stimuli = stimuli, practice_trials = practice_trials)),
    tar_target(responses_clean, get_responses_clean(responses_processed = responses_processed, stimuli = stimuli)),
<<<<<<< HEAD
    tar_target(responses_coded_path, here("data", "processed", "02_coded.xlsx")),
=======
    tar_target(responses_coded_path, here("data", "responses-processed.xlsx")),
>>>>>>> c92465ffee5b01a15c56bc645bd58fd50fe89122
    tar_target(responses_coded, read_xlsx(responses_coded_path)),
    tar_target(participants, get_participants(responses_processed = responses_processed,responses_coded = responses_coded)),
    tar_target(responses, get_responses(responses_coded = responses_coded, practice_trials = practice_trials, participants = participants, stimuli = stimuli)),
    
    # models
    tar_target(
        model_formulas,
        formulas <- list(
            f_0 = bf(correct ~ 1 + 
                         (1 | participant) + 
                         (1 | word)),
            f_1 = bf(correct ~ 1 + frequency_zipf + 
                         (1 + frequency_zipf | participant) + 
                         (1 | word)),
            f_2 = bf(correct ~ 1 + frequency_zipf + pthn + 
                         (1 + frequency_zipf + pthn | participant) + 
                         (1 | word)),
            f_3 = bf(correct ~ 1 + frequency_zipf + pthn + lv +
                         (1 + frequency_zipf + pthn + lv | participant) + 
                         (1 | word)),
            f_4 = bf(correct ~ 1 + frequency_zipf + pthn + lv + pthn:lv + 
                         (1 + frequency_zipf + pthn*lv | participant) +
                         (1 | word)),
            f_5 = bf(correct ~ 1 + frequency_zipf +  pthn + lv + lv:pthn + group +
                         (1 + frequency_zipf + pthn + lv + lv:pthn | participant) + 
                         (1 | word)),
            f_6 = bf(correct ~ 1 + frequency_zipf + pthn + lv + lv:pthn + group + group:lv +
                         (1 + frequency_zipf + pthn + lv + lv:pthn + group:lv | participant) + 
                         (1 | word))
        )
    ),
    tar_target(
        model_prior,
        # prior
        c(prior(normal(0, 0.1), class = "Intercept"),
          prior(normal(0, 0.1), clas = "b"),
          prior(cauchy(0, 0.1), class = "sd", group = "participant"),
          prior(cauchy(0, 0.1), class = "sd", group = "word"),
          prior(lkj(8), class = "cor"))
    ),
    tar_target(model_fits, get_model_fits(responses = responses, model_formulas = model_formulas, model_prior = model_prior)),
    tar_target(model_loos, get_model_loos(model_fits)),
    tar_target(posterior_draws_fixed, get_model_draws_fixed(model_fits$fit_6)),
    tar_target(posterior_epreds_fixed, get_model_epreds_fixed(model_fits$fit_6)),
    tar_target(posterior_draws_random, get_model_draws_random(model_fits$fit_6)),
    tar_target(posterior_epreds_random, get_model_epreds_random(model_fits$fit_6, group = c("participant"))),
    
    # render report.Rmd
    tar_render(docs_stimuli, "docs/00_stimuli.Rmd"),
    tar_render(docs_participants, "docs/01_participants.Rmd"),
    tar_render(docs_analysis, "docs/02_data-analysis.Rmd"),
    tar_render(docs_results, "docs/03_results.Rmd"),
    
    
    # render manuscript.Rmd
    tar_render(manuscript, "manuscript/manuscript.Rmd")
)



