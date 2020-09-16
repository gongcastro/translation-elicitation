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

# create/load functions
source(here("Code", "functions.R")) # helper functions

# set parameters
set.seed(888) # for reproducibility

#### import data ##########################################
dat <- fread(here("Data", "04_accuracy.csv"), na.strings = c("", "NA")) %>%
    as_tibble() %>% 
    mutate_at(vars(onset, stress_overlap, group), as.factor) %>% 
    mutate_at(vars(consonant_ratio, vowel_ratio, pthn, freq),
              function(x) scale(x, center = TRUE, scale = FALSE)[,1]) %>% 
    mice(m = 5, print = FALSE, method = "pmm") %>% # impute missing data
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(dat$onset) <- c(-0.5, 0.5)
contrasts(dat$stress_overlap) <- c(-0.5, 0.5)

#### fit models ###########################################

fit0 <- glmer(cbind(correct, n-correct) ~ 1 + (1 | group),
              data = dat, family = binomial)
fit1 <- glmer(cbind(correct, n-correct) ~ 1 + pthn + (1 + pthn | group),
              data = dat, family = binomial)
fit2 <- glmer(cbind(correct, n-correct) ~ 1 + pthn + vowel_ratio + (1 + pthn + vowel_ratio | group),
              data = dat, family = binomial)
fit3 <- glmer(cbind(correct, n-correct) ~ 1 + pthn + vowel_ratio + consonant_ratio + (1 + pthn + vowel_ratio + consonant_ratio | group),
              data = dat, family = binomial)

selection <- anova(fit0, fit1, fit2, fit3)

anova <- Anova(fit3, type = "III", test.statistic = "Chisq")

output  <- tidy(fit3, conf.int = TRUE)
#### model predictions ####################################

dat_preds <- expand_grid(pthn = unique(dat$pthn),
                         vowel_ratio = seq(min(dat$vowel_ratio, na.rm = TRUE),
                                           max(dat$vowel_ratio, na.rm = TRUE),
                                           by = 0.01),
                         consonant_ratio = seq(min(dat$consonant_ratio, na.rm = TRUE),
                                               max(dat$consonant_ratio, na.rm = TRUE),
                                               by = 0.01),
                         group = unique(dat$group)) %>% 
    mutate(pred = predict(fit3, newdata = ., type = "response")) %>% 
    mutate(vowel_ratio = cut_interval(vowel_ratio, n = 4, labels = c("0-25th", "26-50th", "51-75th", "76-100th"))) 

dat %>%
    mutate(vowel_ratio = cut_interval(vowel_ratio, n = 4, labels = c("0-25th", "26-50th", "51-75th", "76-100th"))) %>% 
    ggplot(aes(consonant_ratio, proportion, size = pthn, colour = vowel_ratio)) +
    facet_wrap(~group, ncol = 2) +
    geom_point(alpha = 0.25) +
    stat_summary(data = dat_preds, aes(y = pred), fun = "mean", geom = "line", size = 1) +
    labs(x = "Consonant ratio", y = "P. correct translation", colour = "Vowel ratio percentile", size = "PTHN") +
    scale_color_brewer(palette = "Spectral") +
    guides(colour = guide_legend(ncol = 2),
           size = guide_legend(direction = "horizontal", ncol = 3, title.position = "top")) +
    theme(legend.position = c(0.75, 0.25),
          legend.title = element_text(size = 9),
          legend.text = element_text(size = 9),
          legend.margin = margin(0.05, unit = "cm"),
          panel.background = element_rect(fill = "white"),
          panel.grid = element_line(colour = "grey", linetype = "dotted")) +
    ggsave(here("Figures", "predictions.png"), height = 4, width = 5)





