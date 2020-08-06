#### analysis #############################################

#### set up ###############################################

# load packages
library(dplyr)      # for manipulating variables
library(tidyr)      # for reshaping data sets
library(ggplot2)    # for visualising data
library(tibble)     # for more informative data sets
library(stringr)    # for manipulating character strings
library(purrr)      # for working with lists
library(janitor)    # for cleaning variable names
library(data.table) # for importing data
library(brms)       # for fitting Bayesian models
library(mice)       # for imputing data
library(bayesplot)  # for plotting MCMC
library(tidybayes)  # for sampling from the posterior in Bayesian models
library(modelr)     # for predicting scores from models
library(here)       # for locating paths

# create/load functions
source(here("Code", "functions.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility

#### import data ##########################################
dat_accuracy <- fread(here("Data", "04_prepared.csv"), na.strings = c("", "NA")) %>%
    as_tibble() %>% 
    mutate_at(vars(same_onset, group), as.factor)

#### impute missing data ##################################
dat_imputed <- mice(dat_accuracy, m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(dat_imputed$same_onset) <- c(-0.5, 0.5)

#### fit models #########################################
priors <- c(prior(normal(0, 1), class = "Intercept"),
            prior(normal(0, 1), class = "b"), 
            prior(cauchy(0, 1), class = "sd"),
            prior(lkj(2), class = "cor"))



fit1_pthn <- brm(formula = bf(correct | trials(n) ~ pthn + (1 + pthn | group)),
                  prior = priors,
                  family = binomial("logit"),
                  data = dat_imputed,
                  cores = 4,
                  file = here("Results", "fit0_prior.rds"), 
                  control = list(adapt_delta = 0.95),
                  save_model = here("Code", "Models", "fit0_prior.stan"),
                  save_all_pars = TRUE)


# null model (only frequency)
fit2_onset <- update(fit1_pthn, bf(correct | trials(n) ~ pthn*same_onset + (1 + pthn*same_onset | group)),
                     file = here("Results", "fit2_onset.rds"),
                     newdata = dat_imputed,
                     cores = 4,
                     save_model = here("Code", "Models", "fit2_onset.stan"))

# match count
fit3_close <- update(fit1_pthn,  bf(correct | trials(n) ~ pthn*close_substitutions + (1 + pthn*close_substitutions | group)),
                     file = here("Results", "fit3_close.rds"),
                     newdata = dat_imputed,
                     cores = 4,
                     save_model = here("Code", "Models", "fit3_close.stan"))

fit4_phon <- update(fit1_pthn, bf(correct | trials(n) ~ pthn*similarity_phon + (1 + pthn*similarity_phon | group)),
                     file = here("Results", "fit4_phon.rds"),
                     newdata = dat_imputed,
                     cores = 4,
                     save_model = here("Code", "Models", "fit4_phon.stan"))

# orthographic similarity (Damerau-Levenshtein distance)
fit5_ort <- update(fit1_pthn, bf(correct | trials(n) ~ pthn*similarity_ort + (1 + pthn*similarity_ort | group)),
                   file = here("Results", "fit5_ort.rds"),
                   newdata = dat_imputed,
                   cores = 4,
                   save_model = here("Code", "Models", "fit5_ort.stan"))

# null model (only frequency)
fit0_prior <- update(fit4_phon,
                     newdata = dat_imputed,
                     sample_prior = "only",
                     cores = 4,
                     file = here("Results", "fit0_prior.rds"), 
                     save_model = here("Code", "Models", "fit0_prior.stan"))


# compute k-fold validation and compare models
loos <- loo(fit1_pthn, fit2_onset, fit3_close, fit4_phon, fit5_ort)

r2 <- list(fit1_pthn, fit2_onset, fit3_close, fit4_phon, fit5_ort) %>% 
    set_names(c("fit1_pthn", "fit2_onset", "fit3_close", "fit4_phon", "fit5_ort")) %>% 
    map(., bayes_R2) %>%
    map(., as.data.frame) %>% 
    map(remove_rownames) %>% 
    bind_rows(.id = "model") %>% 
    arrange(Estimate) %>% 
    clean_names()
saveRDS(loos, here("Results", "loos.rds"))
saveRDS(r2, here("Results", "r2.rds"))

#### examine prior/posterior #####################################
prior <- fit0_prior %>% 
    gather_draws(`b_.*`, regex = TRUE) %>% 
    ungroup() %>% 
    mutate_at(vars(.chain, .variable), function(x) factor(x, levels = unique(x), ordered = TRUE))

posterior <- fit4_phon %>% 
    gather_draws(`b_.*`, regex = TRUE) %>% 
    ungroup() %>% 
    mutate_at(vars(.chain, .variable), function(x) factor(x, levels = unique(x), ordered = TRUE))

fwrite(posterior, here("Results", "posterior_draws.csv"), sep = ",", dec = ".", row.names = FALSE)
fwrite(prior, here("Results", "prior_draws.csv"), sep = ",", dec = ".", row.names = FALSE)

#### predictive checks ##############################

# prior predictive checks
prior_preds <- expand_grid(n = 1,
                           pthn = median(dat_imputed$pthn, na.rm = TRUE),                           
                           similarity_phon = seq_range(dat_imputed$similarity_phon, n = 100)) %>%   
    add_fitted_draws(fit0_prior, newdata = ., re_formula = NA, scale = "response", n = 100) %>% 
    ungroup() 
# posterior predictive checks
posterior_preds <- expand_grid(n = 1,
                               group = unique(dat_imputed$group),
                               pthn = median(dat_imputed$pthn, na.rm = TRUE),                           
                               similarity_phon = seq_range(dat_imputed$similarity_phon, n = 100)) %>%   
    add_fitted_draws(fit4_phon, newdata = ., re_formula = NA, scale = "response", n = 100, ) %>% 
    ungroup() 

fwrite(prior_preds, here("Results", "prior_predictions.csv"), sep = ",", dec = ".", row.names = FALSE)
fwrite(posterior_preds, here("Results", "posterior_predictions.csv"), sep = ",", dec = ".", row.names = FALSE)


#### analyse random effects structure #####################

# get group-level effects
group_effects <- gather_draws(fit4_phon, r_group[group, param])
    
# get correlations between group-level effects
corrs <- gather_draws(fit4_phon, `cor_.*`, regex = TRUE)

# export data
fwrite(group_effects, here("Results", "group_effects.csv"), sep = ",", dec = ".", row.names = FALSE)
fwrite(corrs, here("Results", "corrs.csv"), sep = ",", dec = ".", row.names = FALSE)

