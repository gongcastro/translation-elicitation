# library(dplyr)
# library(tidyr)
# library(readr)
# library(ggplot2)
# library(brms)
# library(tidybayes)
# library(readxl)
# 
# exp_data <- file.path("data", "experiment", "processed", "02_coded.xlsx") |> 
#     read_xlsx() |> 
#     mutate(word_1 = )
# 
# stimuli <- file.path("data", "stimuli.csv") |> 
#     read_csv(show_col_types = FALSE) |> 
#     select(group, translation_id, word_1, word_2, freq_zipf_2, avg_sim_h, lv, practice_trial) |> 
#     mutate(across(c(word_1, word_2), replace_non_ascii)) 
# 
# scale_variable <- function(x) scale(x)[,1]
# 
# dataset <- exp_data |> 
#     select(group, participant_id, group, word_1, response = input_text, correct)  |>  
#     left_join(stimuli, by = join_by(group, word_1)) |> 
#     dplyr::filter(!isTRUE(practice_trial),
#                   group %in% c("cat-ENG", "spa-ENG", "cat-SPA")) |>  
#     drop_na() |> 
#     mutate(across(c(freq_zipf_2, avg_sim_h, lv), 
#                   scale_variable, 
#                   .names = "{.col}_std"),
#            group = as.factor(group))
# 
# contrasts(dataset$group) <- cbind(
#     "cateng_spaeng" = c(0.5, 0, -0.5),
#     "spa_eng" = c(0.25, 0.5, -0.25)
# )
# 
# model_prior <- c(prior(normal(0, 0.1), class = "Intercept"),
#                  prior(normal(0, 0.1), class = "b"),
#                  prior(exponential(3), class = "sd"),
#                  prior(lkj(5), class = "cor"))
# 
# m0 <- brm(bf(correct ~ 1 + freq_zipf_2_std + avg_sim_h_std*lv_std + group + lv_std:group +  
#                  (1 + freq_zipf_2_std + avg_sim_h_std*lv_std | participant_id) +
#                  (1 + group | translation_id)),
#           data = dataset,
#           family = bernoulli("logit"),
#           prior = model_prior,
#           save_pars = save_pars(all = TRUE),
#           backend = "cmdstanr",
#           iter = 1000, chains = 4, seed = 1234,
#           control = list(adapt_delta = 0.95),
#           file = file.path("results", "2024_04_21-fit_1.rds"))
# 
# 
