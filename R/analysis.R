#### analysis ------------------------------------------------------------------

#### set up --------------------------------------------------------------------

# load packages
library(tidyverse)  # for manipulating variables
library(janitor)    # for cleaning variable names
library(data.table) # for importing data
library(mice)       # for imputing data
library(broom)      # for extracting model outputs
library(car)        # for performing F-tests
library(here)       # for locating paths
library(lmtest)     # for significance testing
library(patchwork)  # for arranging plots
library(gt)         # for nice tables

# create/load functions
source(here("Code", "functions.R")) # wrapper functions

# set parameters
set.seed(888) # for reproducibility

#### import data ---------------------------------------------------------------
dat <- fread(here("Data", "04_accuracy.csv"), na.strings = c("", "NA")) %>% 
    # typos are considered correct responses
    mutate_at(vars(onset, stress_overlap, group), as.factor) %>% 
    # center predictors
    mutate_at(
        vars(lv, consonant_ratio, vowel_ratio, consonant_ratio2, vowel_ratio2, pthn, freq, similarity_ipa, similarity_code),
        function(x) scale(x, center = TRUE, scale = TRUE)[,1]) %>% 
    # impute missing data
    mice(m = 5, print = FALSE, method = "pmm") %>% 
    complete() %>% 
    as_tibble() %>% 
    arrange(trial_id, group)

contrasts(dat$group) <- c(-0.5, -0.5, 1)

#### fit models ----------------------------------------------------------------
fit0 <- glm(cbind(correct, n) ~ pthn + vowel_ratio + consonant_ratio, data = dat, family = binomial)
fit1 <- update(fit0, .~. - pthn) # drop PTHN
fit2 <- update(fit1, .~. - vowel_ratio) # drop vowel ratio
fit3 <- update(fit2, .~. - consonant_ratio) # drop consonant ratio
fit4 <- glm(cbind(correct, n) ~ lv, data = dat, family = binomial)
fit5 <- glm(cbind(correct, n) ~ similarity_code, data = dat, family = binomial)
fit6 <- glm(cbind(correct, n) ~ similarity_ipa, data = dat, family = binomial)
fit0_spa <- glm(cbind(correct, n) ~ pthn + vowel_ratio + consonant_ratio, data = filter(dat, group=="SPA-CAT"), family = binomial)
fit1_spa <- update(fit0_spa, .~. - pthn) # drop PTHN
fit2_spa <- update(fit1_spa, .~. - vowel_ratio) # drop vowel ratio
fit3_spa <- update(fit2_spa, .~. - consonant_ratio) # drop consonant ratio
fit4_spa <- glm(cbind(correct, n) ~ lv, data = filter(dat, group=="SPA-CAT"), family = binomial)
fit5_spa <- glm(cbind(correct, n) ~ similarity_code, data = filter(dat, group=="SPA-CAT"), family = binomial)
fit6_spa <- glm(cbind(correct, n) ~ similarity_ipa, data = filter(dat, group=="SPA-CAT"), family = binomial)
fit0_eng <- glm(cbind(correct, n) ~ pthn + vowel_ratio + consonant_ratio, data = filter(dat, group!="SPA-CAT"), family = binomial)
fit1_eng <- update(fit0_eng, .~. - pthn) # drop PTHN
fit2_eng <- update(fit1_eng, .~. - vowel_ratio) # drop vowel ratio
fit3_eng <- update(fit2_eng, .~. - consonant_ratio) # drop consonant ratio
fit4_eng <- glm(cbind(correct, n) ~ lv, data = filter(dat, group!="SPA-CAT"), family = binomial)
fit5_eng <- glm(cbind(correct, n) ~ similarity_code, data = filter(dat, group!="SPA-CAT"), family = binomial)
fit6_eng <- glm(cbind(correct, n) ~ similarity_ipa, data = filter(dat, group!="SPA-CAT"), family = binomial)

fit0.2 <- glm(cbind(correct, n) ~ pthn + group*vowel_ratio2 + group*consonant_ratio2, data = dat, family = binomial)
fit1.2 <- update(fit0.2, .~. - pthn) # drop PTHN
fit2.2 <- update(fit1.2, .~. - vowel_ratio) # drop vowel ratio
fit3.2 <- update(fit2.2, .~. - consonant_ratio) # drop consonant ratio
fit4.2 <- glm(cbind(correct, n) ~ lv, data = dat, family = binomial)

# compare model fits
comparison <- lrtest(fit4, fit0, fit1, fit2, fit3) %>% 
    as.data.frame() %>% 
    mutate(aic = AIC(fit4, fit0, fit1, fit2, fit3)[,2],
           bic = BIC(fit4, fit0, fit1, fit2, fit3)[,2]) %>% 
    clean_names() %>% 
    rownames_to_column("model")

comparison_eng <- lrtest(fit4_eng, fit0_eng, fit1_eng, fit2_eng, fit3_eng) %>% 
    as.data.frame() %>% 
    mutate(aic = AIC(fit4_eng, fit0_eng, fit1_eng, fit2_eng, fit3_eng)[,2],
           bic = BIC(fit4_eng, fit0_eng, fit1_eng, fit2_eng, fit3_eng)[,2]) %>% 
    clean_names() %>% 
    rownames_to_column("model")

comparison_spa <- lrtest(fit4_spa, fit0_spa, fit1_spa, fit2_spa, fit3_spa) %>% 
    as.data.frame() %>% 
    mutate(aic = AIC(fit4_spa, fit0_spa, fit1_spa, fit2_spa, fit3_spa)[,2],
           bic = BIC(fit4_spa, fit0_spa, fit1_spa, fit2_spa, fit3_spa)[,2]) %>% 
    clean_names() %>% 
    rownames_to_column("model")


comps <- bind_rows(comparison, comparison_eng, comparison_spa, .id = "subset") %>% 
    select(subset, model, aic, bic, log_lik, chisq, pr_chisq) %>% 
    pivot_longer(3:5, names_to = "index", values_to = "value") %>% 
    mutate(model = as.factor(model),
           model = factor(model, labels = c("LV", "PTHN+V+C", "V+C", "C", "Null"), ordered = TRUE), 
           index = str_to_upper(index),
           value = abs(value),
           subset = case_when(subset==1 ~ "All", subset==2 ~ "UK", TRUE ~ "Spain"))
# get tidy model outputs for the complete model
output  <- tidy(fit0, conf.int = TRUE) %>% clean_names()

#### model predictions ####################################

# get predictions from complete model
dat_preds <- expand_grid(
    pthn = unique(dat$pthn),
    vowel_ratio = seq(
        min(dat$vowel_ratio, na.rm = TRUE),
        max(dat$vowel_ratio, na.rm = TRUE),
        by = 0.01
    ),
    consonant_ratio = seq(
        min(dat$consonant_ratio, na.rm = TRUE),
        max(dat$consonant_ratio, na.rm = TRUE),
        by = 0.01
    )
) %>% 
    mutate(
        pred = predict(fit0, newdata = ., type = "response"),
        vowel_ratio = cut_interval(
            vowel_ratio, n = 4,
            labels = c("0-25th", "26-50th", "51-75th", "76-100th")
        )
    ) 

dat_preds2b <- expand_grid(
    pthn = unique(dat$pthn),
    group = unique(dat$group),
    vowel_ratio2 = seq(
        min(dat$vowel_ratio2, na.rm = TRUE),
        max(dat$vowel_ratio2, na.rm = TRUE),
        by = 0.01
    ),
    consonant_ratio2 = seq(
        min(dat$consonant_ratio2, na.rm = TRUE),
        max(dat$consonant_ratio2, na.rm = TRUE),
        by = 0.01
    )
) %>%  
    mutate(pred = predict(fit0.2, newdata = ., type = "response"),
           vowel_ratio2 = cut_interval(
               vowel_ratio2,
               n = 4,
               labels = c("0-25th", "26-50th", "51-75th", "76-100th")
           ) 
    )

# get predictions from Levenshtein model
dat_preds2 <- expand_grid(
    pthn = unique(dat$pthn),
    lv = seq(
        min(dat$lv, na.rm = TRUE),
        max(dat$lv, na.rm = TRUE),
        by = 0.01)
) %>% 
    mutate(pred = predict(fit4, newdata = ., type = "response")) 
# plot predictions
dat %>%
    mutate(vowel_ratio = cut_interval(
        vowel_ratio,
        n = 4,
        labels = c("0-25th", "26-50th", "51-75th", "76-100th"))
    ) %>% 
    ggplot(aes(consonant_ratio, proportion, colour = vowel_ratio, fill = vowel_ratio)) +
    geom_point(alpha = 0.5, shape = 1, size = 2) +
    stat_summary(data = dat_preds, aes(y = pred), fun = "mean", geom = "line") +
    labs(x = "Consonant ratio", y = "p(correct translation)",
         colour = "Vowel ratio percentile", fill = "Vowel ratio percentile") +
    scale_color_brewer(palette = "Set1") +
    
    dat %>%
    ggplot(aes(lv,  as.numeric(correct)-1)) +
    geom_point(alpha = 0.5, shape = 1, size = 2) +
    stat_summary(data = dat_preds2, aes(y = pred),
                 fun = "mean", geom = "line", size = 1) +
    labs(x = "Phonological Levenshtein distance",
         y = "p(correct translation)", size = "PTHN") +
    plot_layout(guides = "collect") &
    plot_annotation(tag_levels = "A") &
    theme(legend.position = "top",
          axis.title = element_text(face = "bold"),
          legend.text = element_text(size = 9),
          panel.background = element_rect(fill = "white"),
          panel.grid = element_line(colour = "grey", linetype = "dotted"),
          text = element_text(colour = "black"),
          axis.text = element_text(colour = "black")) &
    ggsave(here("Figures", "predictions.png"), height = 5, width = 10)


dat %>%
    mutate(vowel_ratio2 = cut_interval(
        vowel_ratio2,
        n = 4,
        labels = c("0-25th", "26-50th", "51-75th", "76-100th"))
    ) %>% 
    ggplot(aes(consonant_ratio2, proportion, colour = group, fill = group)) +
    facet_wrap(~vowel_ratio2) +
    geom_point(alpha = 0.5, shape = 1, size = 2) +
    stat_summary(data = dat_preds2b, aes(y = pred), fun = "mean", geom = "line") +
    labs(x = "Consonant ratio", y = "p(correct translation)",
         colour = "Group", fill = "Group") +
    scale_color_brewer(palette = "Set1") 

dat %>%
    mutate(consonant_ratio2 = cut_interval(
        consonant_ratio2,
        n = 4,
        labels = c("0-25th", "26-50th", "51-75th", "76-100th")
    )
    ) 
    ggplot(aes(vowel_ratio2, proportion, colour = group)) +
    facet_wrap(~consonant_ratio2) +
    geom_point(alpha = 0.5, shape = 1, size = 2) +
    stat_summary(data = dat_preds2b, aes(y = pred),
                 fun = "mean", geom = "line", size = 1) 
    labs(x = "Vowel similarity ratio", colour = "Group",
         y = "p(correct translation)", size = "PTHN") +
    
    plot_layout(guides = "collect") &
    plot_annotation(tag_levels = "A") &
    theme(legend.position = "top",
          axis.title = element_text(face = "bold"),
          legend.text = element_text(size = 9),
          panel.background = element_rect(fill = "white"),
          panel.grid = element_line(colour = "grey", linetype = "dotted"),
          text = element_text(colour = "black"),
          axis.text = element_text(colour = "black")) &
    ggsave(here("Figures", "predictions_b.png"), height = 5, width = 10)

# plot model fit indices
comps %>%
    ggplot(aes(model, y = value, fill = model)) +
    facet_grid(subset~index, scales = "free") +
    geom_col() +
    geom_text(aes(x = model, y = value+300, label = round(value, 2)), size = 3) +
    labs(x = "Model", y = "Value") +
    scale_fill_brewer(palette = "Set1") +
    theme(legend.position = "none",
          axis.title = element_text(face = "bold"),
          legend.title = element_blank(),
          legend.text = element_text(size = 9),
          panel.background = element_rect(fill = "white"),
          panel.grid = element_line(colour = "grey", linetype = "dotted"),
          text = element_text(colour = "black"),
          axis.text = element_text(colour = "black")) +
    ggsave(here("Figures", "fit.png"), width = 9)


