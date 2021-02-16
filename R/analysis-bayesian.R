#### analysis: fit Bayesian models ---------------------------------------------

#### set up --------------------------------------------------------------------

# load packages
library(tidyverse)
library(janitor)
library(mice)
library(broom)
library(brms)
library(tidybayes)
library(modelr)
library(scales)
library(here)

# create/load functions
source(here("R", "utils.R")) # wrapper functions

# set parameters
set.seed(888) # for reproducibility
options(mc.cores = 4)

#### import data ---------------------------------------------------------------
d <- readRDS(here("Results", "accuracy.rds")) %>% 
    # typos are considered correct responses
    mutate_at(vars(onset, stress_overlap, group), as.factor) %>% 
    # centre predictors
    mutate_at(
        vars(pthn, freq, lv, consonant_ratio, vowel_ratio),
        function(x) scale(x)[,1]) %>% 
    # impute missing data
    mice(m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(d$onset) <- c(-0.5, 0.5)
contrasts(d$stress_overlap) <- c(-0.5, 0.5)
contrasts(d$group) <- c(-0.5, -0.5, 1)

#### fit models ----------------------------------------------------------------
fit_pthn <- brm(
    correct | trials(n) ~ pthn,
    family = binomial("logit"),
    prior = c(prior(normal(0, 1), class = "Intercept"),
              prior(normal(0, 1), class = "b")),
    data = d,
    file = here("Results", "fit_pthn.rds"), 
    save_model = here("Stan", "fit_pthn.stan")
)

fit_onset <- update(
    fit_pthn, . ~ . + onset, newdata = d,
    file = here("Results", "fit_onset.rds"), 
    save_model = here("Stan", "fit_onset.stan")
)

fit_stress <- update(
    fit_pthn, . ~ . + stress_overlap, newdata = d,
    file = here("Results", "fit_stress.rds"), 
    save_model = here("Stan", "fit_stress.stan")
)

fit_consonant <- update(
    fit_pthn, . ~ . + consonant_ratio, newdata = d,
    file = here("Results", "fit_consonant.rds"), 
    save_model = here("Stan", "fit_consonant.stan")
)

fit_vowel <- update(
    fit_pthn, . ~ . + vowel_ratio, newdata = d,
    file = here("Results", "fit_vowel.rds"), 
    save_model = here("Stan", "fit_vowel.stan")
)

fit_lv <- update(
    fit_pthn, . ~ . + lv, newdata = d,
    file = here("Results", "fit_lv.rds"), 
    save_model = here("Stan", "fit_lv.stan")
)

wgts <- model_weights(fit_pthn, fit_onset, fit_stress, fit_consonant, fit_vowel, fit_lv)


#### examine prior/posterior ---------------------------------------------------
post <- gather_draws(fit, `b_.*`, regex = TRUE) 

ggplot(post, aes(.value/4, .variable)) +
    geom_vline(xintercept = 0, linetype = "dashed") +
    stat_slab(aes(fill = stat(cut_cdf_qi(
        cdf, .width = c(.5, .8, .95, 0.99), # quantiles
        labels = percent_format(accuracy = 1))))) +
    labs(x = "Value", y = "Variable", fill = "CrI") +
    scale_fill_brewer(palette = "Oranges", direction = -1, na.translate = FALSE) +
    theme_custom() +
    theme(axis.title = element_blank()) +
    ggsave(here("Figures", "posterior.png"))


#### predictive checks ---------------------------------------------------------

# prior predictive checks
post_preds <- expand_grid(
    n = 1,
    freq = 0,
    pthn = seq(-1, 1, 0.1),    
    onset = unique(d$onset),
    stress_overlap = unique(d$stress_overlap),
    vowel_ratio =  c(-1, 1),
    consonant_ratio =  c(-1, 1)
) %>%   
    add_fitted_draws(fit, newdata = ., n = 50) %>% 
    ungroup() 

ggplot(post_preds, aes(
    pthn, .value,
    colour = interaction(consonant_ratio, vowel_ratio, sep = " - "),
    fill = interaction(consonant_ratio, vowel_ratio, sep = " - "))
) +
    facet_grid(onset~stress_overlap) +
    stat_lineribbon(.width = 0.95, alpha = 0.5, colour = NA,
                    aes(group = interaction(consonant_ratio, vowel_ratio, sep = " - "))) +
    stat_summary(fun = "mean", geom = "line") +
    #geom_line(aes(group = interaction(consonant_ratio, vowel_ratio, .draw)), alpha = 0.5) +
    labs(x = "PTHN (SD)", y = "P(Correct)",
         colour = "C-V ratio",
         fill = "C-V ratio") +
    scale_color_brewer(palette = "Set1") +
    scale_fill_brewer(palette = "Set1") +
    theme_custom() +
    theme(legend.position = "top") +
    ggsave(here("Figures", "means.png"), width = 5)


