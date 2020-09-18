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
library(mice)       # for imputing data
library(lme4)       # for fitting multilevel generalised linear models
library(broom.mixed)
library(car)        # for performing F-tests
library(here)       # for locating paths
library(patchwork)

# create/load functions
source(here("Code", "functions.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility

#### import data ##########################################
dat <- fread(here("Data", "04_accuracy.csv"), na.strings = c("", "NA")) %>%
    as_tibble() %>% 
    mutate_at(vars(onset, stress_overlap, group), as.factor) %>% 
    mutate_at(vars(lv, consonant_ratio, vowel_ratio, pthn, freq),
              function(x) scale(x, center = TRUE, scale = FALSE)[,1]) %>% 
    mice(m = 5, print = FALSE, method = "pmm") %>% # impute missing data
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(dat$onset) <- c(-0.5, 0.5)
contrasts(dat$stress_overlap) <- c(-0.5, 0.5)

#### fit models ###########################################

fit0 <- glm(cbind(correct, n-correct) ~ 1, data = dat, family = binomial)
fit1 <- update(fit0, . ~ . + pthn)
fit2 <- update(fit1, . ~ . + vowel_ratio)
fit3 <- update(fit2, . ~ . + consonant_ratio)
fit4 <- update(fit0, . ~ . + lv)

selection <- anova(fit0, fit1, fit2, fit3)
with(anova(fit0, fit1, fit2, fit3), pchisq(Deviance, Df, lower.tail = FALSE)) 


selection2 <- anova(fit3, fit4)
anova <- Anova(fit3, type = "III", test.statistic = "F")

output  <- tidy(fit4, conf.int = TRUE)
#### model predictions ####################################

dat_preds <- expand_grid(pthn = unique(dat$pthn),
                         vowel_ratio = seq(min(dat$vowel_ratio, na.rm = TRUE),
                                           max(dat$vowel_ratio, na.rm = TRUE),
                                           by = 0.01),
                         consonant_ratio = seq(min(dat$consonant_ratio, na.rm = TRUE),
                                               max(dat$consonant_ratio, na.rm = TRUE),
                                               by = 0.01)) %>% 
    mutate(pred = predict(fit3, newdata = ., type = "response"),
           ppred = 1 / (1 + exp(-pred)),
           vowel_ratio = cut_interval(vowel_ratio, n = 4,
                                      labels = c("0-25th", "26-50th", "51-75th", "76-100th"))) 

dat_preds2 <- expand_grid(pthn = unique(dat$pthn),
                         lv = seq(min(dat$lv, na.rm = TRUE),
                                           max(dat$lv, na.rm = TRUE),
                                           by = 0.01)) %>% 
    mutate(pred = predict(fit4, newdata = ., type = "response"),
           ppred = 1 / (1 + exp(-pred)))


dat %>%
    mutate(vowel_ratio = cut_interval(vowel_ratio, n = 4, labels = c("0-25th", "26-50th", "51-75th", "76-100th"))) %>% 
    ggplot(aes(consonant_ratio, proportion, size = pthn, colour = vowel_ratio)) +
    geom_point(alpha = 0.25) +
    stat_summary(data = dat_preds, aes(y = pred), fun = "mean", geom = "line", size = 1) +
    labs(x = "Consonant ratio", y = "p(correct translation)", colour = "Vowel ratio percentile", size = "PTHN") +
    scale_color_brewer(palette = "Spectral") +
    
    
    dat %>%
    ggplot(aes(lv, proportion, size = pthn)) +
    geom_point(alpha = 0.25) +
    stat_summary(data = dat_preds2, aes(y = pred), fun = "mean", geom = "line", size = 1) +
    labs(x = "Phonological Levenshtein distance", y = "p(Correct translation)", size = "PTHN") &
    
    plot_layout(guides = "collect") &

    plot_annotation(tag_levels = "A") &
    theme(legend.position = "right",
          legend.text = element_text(size = 9),
          panel.background = element_rect(fill = "white"),
          panel.grid = element_line(colour = "grey", linetype = "dotted"),
          text = element_text(colour = "black"),
          axis.text = element_text(colour = "black")) &
    ggsave(here("Figures", "predictions.png"), width = 10)





