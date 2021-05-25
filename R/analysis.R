# analysis

# set up ----

# load packages
library(tidyverse) # for manipulating variables
library(janitor) # for cleaning variable names
library(brms) # for fitting Bayesian models
library(tidybayes) # for processing Bayesian models
library(mice) # for multiple imputation
library(here) # for locating files

# set parameters
set.seed(888) # for reproducibility
options(mc.cores = 4, chains = 4, iter = 500, seed = 888)
source(here("R", "utils.R"))

# import data ----
responses <- readRDS(here("Data", "responses.rds")) %>% 
    # typos are considered correct responses
    # transform relative frequency to Zipf score
    mutate(frequency_zipf = relative_to_zipf(frequency)) %>% 
    # center predictors
    mutate_at(
        vars(lv, consonant_ratio, vowel_ratio, pthn, frequency),
        function(x) scale(x, center = TRUE, scale = TRUE)[,1]) %>% 
    # impute missing data
    mice(m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group) %>% 
    mutate_at(vars(onset, overlap_stress, group), as.factor)

contrasts(responses$group) <- c(-0.5, -0.5, 1)
contrasts(responses$onset) <- c(-0.5, 0.5)

# fit models ----
# formula
f_0 <- bf(correct ~ 1 + (1 | participant), family = bernoulli(link = "logit"))
f_1 <- bf(correct ~ pthn + (1 + pthn | participant), family = bernoulli(link = "logit"))
f_2 <- bf(correct ~ pthn*lv + (1 + pthn*lv | participant), family = bernoulli(link = "logit"))
f_3 <- bf(correct ~ pthn*lv*onset + (1 + pthn*lv*onset | participant), family = bernoulli(link = "logit"))

# prior
priors <- c(
    prior(normal(0, 3), class = "Intercept"),
    prior(normal(0, 3), clas = "b"),
    prior(cauchy(0, 3), class= "sd", group = "participant"),
    prior(lkj(5), class = "cor")
)

# fit models
fit_0 <- brm(f_1, data = responses, prior = priors[c(1, 3),], backend = "cmdstanr",
             file = here("Results", "fit_responses_0.rds"))
fit_1 <- brm(f_1, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_responses_1.rds"))
fit_2 <- brm(f_2, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_responses_2.rds"))
fit_3 <- brm(f_3, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_responses_3.rds"))


# model comparison
# model fit is the best
loos <- list(fit_0 = loo(fit_0), fit_1 = loo(fit_1), fit_2 = loo(fit_2), fit_3 = loo(fit_3))
loos_comp <- loo_compare(loos$fit_0, loos$fit_1, loos$fit_2, loos$fit_3)
saveRDS(list(loos = loos, comparison = loos_comp), here("Results", "loo.rds"))

# posterior ----
# fixed effects
p_fix <- gather_draws(fit_4, `b_.*`, regex = TRUE) %>% 
    mutate(.value = ifelse(.variable=="b_Intercept", inv_logit_scaled(.value), .value/4))
ggplot(p_fix, aes(.value)) +
    facet_wrap(~.variable) +
    geom_vline(xintercept = 0, colour = "red") +
    stat_halfeye() +
    labs(x = "Value", y = "Variable") +
    theme_ggdist() +
    theme(
        axis.title = element_blank(),
        panel.grid.major.y = element_line(colour = "grey")
    )

p_ran <- gather_draws(fit_4, r_participant[participant, param]) %>% 
    mutate(.value = ifelse(param=="Intercept", inv_logit_scaled(.value), .value/4)) %>% 
    mean_qi(.width = 0.89)

ggplot(p_ran, aes(.value, participant, xmin = .lower, xmax = .upper)) +
    facet_wrap(~param, scales = "free") +
    geom_errorbar(width = 0, alpha = 0.5, colour = "grey") +
    geom_point(size = 0.5, alpha = 0.5) +
    geom_vline(xintercept = 0, colour = "red") +
    labs(x = "Value", y = "Participant", colour = "Response") +
    theme_ggdist() +
    theme(
        legend.position = c(0.6, 0.15),
        legend.title = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank()
    )

# marginal effects ----
nd <- expand_grid(
    pthn = seq(min(responses$pthn, na.rm = TRUE), max(responses$pthn, na.rm = TRUE), by = 0.1),
    onset = unique(responses$onset),
    lv = c(-1, 1)
) %>% 
    mutate(frequency = 0)
m <- add_fitted_draws(nd, fit_4, n = 20, re_formula = NA) %>% 
    mutate_at(vars(ends_with("_ratio")),
              function(x) ifelse(x>0, paste0(x, " SD"), paste0("-", x, " SD")))

ggplot(m, aes(pthn, .value, 
              colour = interaction(lv, sep = "/"),
              fill = interaction(lv, sep = "/"))) +
    facet_grid(~onset) +
    stat_lineribbon(.width = 0.95, alpha = 0.25, size = 0) +
    stat_summary(fun = mean, geom = "line", size = 1) +
    labs(x = "Phonological neighbourhood density\n(higher frequency neighbours)",
         y = "P(Correct)", colour = "Levenshtein distance",
         fill = "Levenshtein distance") +
    theme_ggdist() +
    theme(
        legend.position = "top"
    )
