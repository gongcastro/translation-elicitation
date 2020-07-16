#### 03-analyse-rts: Analyse reaction times

#### set up ###############################

# load packages
library(dplyr)
library(data.table)
library(tidyr)
library(ggplot2)
library(patchwork)
library(wesanderson)
library(brms)
library(modelr)
library(tidybayes)
library(ggridges)
library(janitor)
library(here)

# load functions
source(here("R", "functions.R"))

#### load data #############################
dat <- fread(here("Data", "04_prepared.csv")) %>%
    select(participant, trial_id, typing_onset, lev_center, frequency_center) %>%
    rename(rt = typing_onset,
           lev = lev_center,
           frequency = frequency_center)

#### fit model #############################
fit <- brm(rt ~ lev + frequency, data = dat)

dat_fitted <- tibble(lev = seq(from = min(dat$lev), to = max(dat$lev),  length.out = 101),
                     frequency = seq(from = min(dat$frequency), to = max(dat$frequency), length.out = 101)) %>%
    add_fitted_draws(newdata = ., model = fit) %>% 
    bind_cols()
dat_predicted <- tibble(lev = seq(from = min(dat$lev), to = max(dat$lev),  length.out = 101),
                        frequency = seq(from = min(dat$frequency), to = max(dat$frequency), length.out = 101)) %>%
    add_predicted_draws(newdata = ., model = fit) %>% 
    bind_cols()

fit_dat <- left_join(dat_fitted, dat_predicted)

#### visualise data ########################

# preditions
ggplot(fit_dat, aes(lev, .value)) +
    stat_lineribbon(.width = c(0.67, 0.89, 0.97)) +
    labs(x = "Levenstein distance", y = "P(RT | Levenshtein)", fill = "Credible interval") +
    scale_fill_manual(values = wes_palette("Zissou1", 3)) +
    theme_custom +
    theme(legend.position = "top")

# coefficients
fit %>%
    gather_draws(b_Intercept, b_lev, b_frequency) %>%
    ggplot(., aes(x = .value, y = .variable, fill = .variable)) +
    geom_vline(xintercept = 0) +
    stat_halfeyeh() +
    geom_vline(xintercept = c(-.8, .8), linetype = "dashed") +
    scale_fill_brewer(palette = "Set1") +
    scale_colour_brewer(palette = "Set1") +
    labs(x = "Estimate", y = "Coefficient") +
    theme_custom +
    theme(axis.title.y = element_blank())

# posterior
dat %>%
    data_grid(lev, frequency) %>%
    add_fitted_draws(fit, dpar = c("mu", "sigma")) 
    ggplot(aes(x = .value, y = lev)) +
    stat_dist_slabh(aes(dist = "norm", arg1 = mu, arg2 = sigma), 
                    slab_color = "gray65", alpha = 1/5, fill = NA) +
    labs(x = "Mu", y  = "Sigma") +
    geom_rug(sides = "b") +
    scale_fill_brewer(palette = "Set1") +
    scale_colour_brewer(palette = "Set1") +
    theme_custom
        
