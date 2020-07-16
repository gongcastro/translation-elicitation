#### 03_analyse-acc: Analyse accuracy ####

#### set up ##############################

# load packages
library(tidyverse)
library(data.table)
library(lme4)
library(lmerTest)
library(broom.mixed)
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

fit0 <- lmer(accuracy ~ same_onset + phon_overlap + n_consecutive_phon + phon_neigh + frequency_zipf +
                 (1 | test_language/participant) +
                 (1 | trial_id),
             data = dat)

fit1 <- lmer(accuracy ~ frequency_zipf*sim +
                 (1 + sim | participant) +
                 (1 + sim | trial_id), na.action = na.omit,
             data = dat)

#### compare models ########################
comp <- anova(fit0, fit1) %>%
    as_tibble() %>%
    clean_names() %>%
    mutate(model = paste0("model", 0:1)) %>%
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
    mutate(term = c("Intercept", "Frequency", "Levenshtein", "Frequency \u00D7 Levenshtein"),
           sig = p.value < 0.05,
           sig = ifelse(sig, "p < 0.05", "p \u2265 0.05")) %>%
    clean_names()

predictions <- ranef(fit1) %>%
    map(~rename(., intercept = "(Intercept)")) %>% 
    map(~rename(., slope = "sim")) %>%
    map(~rownames_to_column(., "participant")) %>%
    map(~mutate_at(., 1, as.character))

dat_predictions <-  left_join(dat, predictions$participant) %>%
    mutate(accuracty = accuracy*100)

#### visualise data #######################

# coefficients
ggplot(coefs, aes(fct_inorder(term), estimate, colour = term)) +
    geom_point(size = 3) +
    geom_hline(yintercept = 0, linetype = "dotted") +
    geom_errorbar(aes(ymin = estimate-std_error, ymax = estimate+std_error), width = 0, size = 1) +
    geom_errorbar(aes(ymin = ci_low, ymax = ci_hight), width = 0, size = 7, alpha = 0.5) +
    coord_flip() +
    labs(x = "Estimate", y = "Term") +
    scale_colour_brewer(palette = "Set1") +
    theme_custom +
    theme(axis.title.y = element_blank(),
          legend.position = "none",
          legend.title = element_blank()) +
    ggsave(here("Figures", "05_coefs-acc.png"), height = 3, width = 8)

# predictions by participant
ggplot(dat_predictions, aes(lev, accuracy)) +
    geom_smooth(aes(group = participant), method = "lm", formula = "y ~ x", se = FALSE, size = 0.5, colour = "grey70") +
    geom_smooth(aes(group = 1), method = "lm", formula = "y ~ x", colour = "red", fill = "red") +
    labs(x = "Levenshtein distance", y = "Accuracy", colour = "Participant", fill = "Participant") +
    theme_custom +
    ggsave(here("Figures", "05_predictions-acc.png"), height = 4, width = 8)

# predictions by item
ggplot(dat_predictions, aes(lev, accuracy, z = frequency_zipf)) +
    geom_smooth(aes(group = participant), method = "lm", formula = "y ~ x", se = FALSE, alpha = 0.5, colour = "grey", size = 0.25) +
    stat_summary(data = dat, aes(y = accuracy), fun = "mean", geom = "point", colour = "red", alpha = 0.5) +
    geom_smooth(method = "lm", formula = "y ~ x", colour = "red", fill = "red") +
    labs(x = "Levenshtein distance", y = "Accuracy", colour = "Frequency", fill = "Frequency") +
    theme_custom +
    scale_colour_gradientn(colours = wes_palette("Zissou1")) +
    scale_fill_gradientn(colours = wes_palette("Zissou1")) +
    ggsave(here("Figures", "05_predictions-rts.png"))

vc_participant <- VarCorr(fit1)$participant
vc_trial <- VarCorr(fit1)$trial







