# analysis

# set up ----

# load packages
library(tidyverse) # for manipulating variables
library(janitor) # for cleaning variable names
library(brms) # for fitting Bayesian models
library(tidybayes) # for processing Bayesian models
library(mice) # for multiple imputation
library(job) # for running code in the background
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
    mutate_at(vars(onset, overlap_stress, group), as.factor) %>% 
    drop_na(correct, vowel_ratio, consonant_ratio, participant, pthn, frequency_zipf)

contrasts(responses$group) <- c(-0.5, -0.5, 1)
contrasts(responses$onset) <- c(-0.5, 0.5)

# fit models ----
# formula
formulas <- list(
    f_0 = bf(correct ~ 1 + frequency + (1 | participant), family = bernoulli(link = "logit")),
    f_1 = bf(correct ~ 1+ frequency + pthn + (1 + pthn | participant), family = bernoulli(link = "logit")),
    f_2 = bf(correct ~ 1 + frequency + pthn*consonant_ratio + (1 + pthn*consonant_ratio | participant), family = bernoulli(link = "logit")),
    f_3 = bf(correct ~ 1 + frequency + pthn*vowel_ratio + (1 + pthn*vowel_ratio | participant), family = bernoulli(link = "logit")),
    f_4 = bf(correct ~ 1 + frequency + pthn + consonant_ratio + vowel_ratio + pthn:consonant_ratio + pthn:vowel_ratio + (1 + pthn + consonant_ratio + vowel_ratio + pthn:consonant_ratio + pthn:vowel_ratio | participant), family = bernoulli(link = "logit"))
)
# prior
priors <- c(
    prior(normal(0, 3), class = "Intercept"),
    prior(normal(0, 3), clas = "b"),
    prior(cauchy(0, 3), class = "sd", group = "participant"),
    prior(lkj(5), class = "cor")
)

# fit models
job(
    title = "Fit models",
    fits = {
        fit_0 = brm(formulas$f_0, data = responses, prior = priors[c(1, 3),], save_pars = save_pars(all = TRUE), file = here("Results", "fit_responses_0.rds"))
        fit_1 = brm(formulas$f_1, data = responses, prior = priors, save_pars = save_pars(all = TRUE), file = here("Results", "fit_responses_1.rds"))
        fit_2 = brm(formulas$f_2, data = responses, prior = priors, save_pars = save_pars(all = TRUE), file = here("Results", "fit_responses_2.rds"))
        fit_3 = brm(formulas$f_3, data = responses, prior = priors, save_pars = save_pars(all = TRUE), file = here("Results", "fit_responses_3.rds"))
        fit_4 = brm(formulas$f_4, data = responses, prior = priors, save_pars = save_pars(all = TRUE), file = here("Results", "fit_responses_4.rds"))
        export = c(fit_0, fit_1, fit_2, fit_3, fit_4)
    },
    import = c(formulas)
)
fits <- as.list(fits) %>%  set_names(paste0("fit_", length(formulas)))

# model comparison
# model fit is the best
loos <- map(fits, loo)
loos_comp <- loo_compare(loos)
saveRDS(list(loos = loos, comparison = loos_comp), here("Results", "loo.rds"))

