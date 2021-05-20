# analysis

# set up ----

# load packages
library(tidyverse) # for manipulating variables
library(janitor) # for cleaning variable names
library(brms) # for fitting Bayesian models
library(tidybayes) # for processing Bayesian models
library(mice) # for multiple imputation

# set parameters
set.seed(888) # for reproducibility
options(mc.cores = 4, chains = 4, iter = 500, seed = 888)

# import data ----
d <- readRDS("Data/accuracy.rds") %>% 
    # typos are considered correct responses
    mutate_at(vars(onset, overlap_stress, group), as.factor) %>% 
    # center predictors
    mutate_at(
        vars(consonant_ratio, vowel_ratio, pthn, frequency),
        function(x) scale(x, center = TRUE, scale = TRUE)[,1]) %>% 
    # impute missing data
    mice(m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(d$group) <- c(-0.5, -0.5, 1)
contrasts(d$onset) <- c(-0.5, 0.5)
contrasts(d$overlap_stress) <- c(-0.5, 0.5)

# fit models ----
# formula
f <- bf(
    correct ~ pthn + frequency + consonant_ratio + vowel_ratio + onset + overlap_stress +
        (1 + pthn + frequency + consonant_ratio + vowel_ratio + onset + overlap_stress | participant) +
        (1 | trial_id),
    family = bernoulli(link = "logit")
)
# prior
priors <- c(
    prior(normal(0, 1), class = "Intercept"),
    prior(normal(0, 1), clas = "b"),
    prior(cauchy(0, 3), class= "sd", group = "participant"),
    prior(constant(1), class = "sd", group = "trial_id"),
    prior(lkj(5), class = "cor")
)
# fit model
fit <- brm(
    formula = f, data = d, prior = priors,
    backend = "cmdstanr",
    file = "Results/fit.rds"
)
s <- broom.mixed::tidy(fit, effects = "fixed") %>% 
    mutate(
        estimate = ifelse(term=="(Intercept)", inv_logit_scaled(estimate), estimate/4),
        conf.low = ifelse(term=="(Intercept)", inv_logit_scaled(conf.low), conf.low/4),
        conf.high = ifelse(term=="(Intercept)", inv_logit_scaled(conf.high), conf.high/4)
    )
saveRDS(s, "Results/coefficients.rds")

# posterior ----
# fixed effects
p_fix <- gather_draws(fit, `b_.*`, regex = TRUE) %>% 
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

p_ran <- gather_draws(fit, r_participant[participant, param]) %>% 
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
    pthn = seq(min(d$pthn, na.rm = TRUE), max(d$pthn, na.rm = TRUE), by = 0.1),
    onset = unique(d$onset),
    overlap_stress = unique(d$overlap_stress),
    vowel_ratio = c(-1, 1),
    consonant_ratio = c(-1, 1)
) %>% 
    mutate(frequency = 0)
m <- add_fitted_draws(nd, fit, n = 20, re_formula = NA) %>% 
    mutate_at(vars(ends_with("_ratio")),
              function(x) ifelse(x>0, paste0(x, " SD"), paste0("-", x, " SD")))

ggplot(m, aes(pthn, .value, 
              colour = interaction(consonant_ratio, vowel_ratio, sep = "/"),
              fill = interaction(consonant_ratio, vowel_ratio, sep = "/"))) +
    facet_grid(~overlap_stress~onset) +
    stat_lineribbon(.width = 0.95, alpha = 0.25, size = 0) +
    stat_summary(fun = mean, geom = "line", size = 1) +
    labs(x = "Phonological neighbourhood density\n(higher frequency neighbours)",
         y = "P(Correct)", colour = "Consonant similarity / Vowel similarity",
         fill = "Consonant similarity / Vowel similarity") +
    theme_ggdist() +
    theme(
        legend.position = "top"
    )
