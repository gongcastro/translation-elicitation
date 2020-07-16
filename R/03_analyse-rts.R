#### 03_analyse-rts: Analyse RTs #########

#### set up ##############################

# load packages
library(data.table)
library(dplyr)
library(purrr)
library(tibble)
library(lme4)
library(broom.mixed)
library(emmeans)
library(ggplot2)
library(wesanderson)
library(patchwork)
library(janitor)
library(here)

# load/create functions
source(here("R", "functions.R"))

#### load data ###########################
dat <- fread(here("Data", "04_prepared.csv"), na.strings = "") %>%
    as_tibble() %>%
    mutate_at(1:2, factor)

#### LMM: Reaction times #################

fit0 <- lmer(
    log(typing_onset) ~ frequency_center +
        (1 | participant) +
        (1 | trial_id),
    data = dat
)

fit1 <- lmer(
    log(typing_onset) ~ frequency_center*lev_center +
        (1 + lev_center | participant) +
        (1 + lev_center | trial_id),
    data = dat
)

fit2 <- lmer(
    log(typing_onset) ~ frequency_center*sim_center +
        (1 + sim_center | participant) +
        (1 + sim_center | trial_id),
    data = dat
)

#### compare models ########################
comp <- anova(fit0, fit1, fit2) %>%
    as_tibble() %>%
    clean_names() %>%
    mutate(model = paste0("model", 0:2)) %>%
    select(model, everything(), p = pr_chisq)

confints <- confint.merMod(fit1, method = "Wald") %>%
    as_tibble() %>%
    clean_names()

coefs <- tidy(fit1) %>%
    arrange(desc(effect)) %>%
    cbind(confints) %>%
    filter(effect=="fixed") %>%
    rename(ci_low = x2_5_percent,
           ci_hight = x97_5_percent) %>%
    select(-c(group, effect)) %>%
    mutate(term = c("Intercept", "Frequency", "Levenshtein", "Frequency x Levenshtein"))

predictions <- ranef(fit1) %>%
    map(~rename(., intercept = "(Intercept)")) %>%
    map(~rename(., slope = "lev_center")) %>%
    
    map(~rownames_to_column(., "participant")) %>%
    map(~mutate_at(., 1, as.character))

dat_predictions <-  left_join(dat, predictions$participant)

#### visualise data #######################

# coefficients
ggplot(coefs, aes(term, estimate)) +
    geom_point(size = 3) +
    geom_hline(yintercept = 0, linetype = "dotted") +
    geom_errorbar(aes(ymin = estimate-std.error, ymax = estimate+std.error), width = 0, size = 1) +
    geom_errorbar(aes(ymin = ci_low, ymax = ci_hight), width = 0, size = 7, alpha = 0.5) +
    coord_flip() +
    labs(x = "Estimate", y = "Term") +
    theme_custom +
    theme(axis.title.y = element_blank()) +
    ggsave(here("Figures", "05_coefs-rts.png"))

# predictions by participant
ggplot(dat_predictions, aes(lev, log(typing_onset))) +
    geom_smooth(aes(group = participant), method = "lm", formula = "y ~ x", se = FALSE, size = 0.5, colour = "grey70") +
    geom_smooth(method = "lm", formula = "y ~ x", colour = "red", fill = "red") +
    labs(x = "Levenshtein distance", y = "Typing onset (ms)") +
    theme_custom +
    ggsave(here("Figures", "05_predictions-rts.png"))

# predictions by item
ggplot(dat_predictions, aes(lev, log(typing_onset), colour = frequency_zipf)) +
    geom_point(alpha = 0.7) +
    geom_smooth(method = "lm", formula = "y ~ x", colour = "black", fill = "black") +
    labs(x = "Levenshtein distance", y = "Typing onset (ms)", colour = "Frequency", fill = "Participant") +
    theme_custom +
    scale_colour_gradientn(colours = wes_palette("Zissou1")) +
    ggsave(here("Figures", "05_predictions-rts.png"))
    
    
    



