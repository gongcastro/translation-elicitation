# models

get_model_fits <- function(
    responses,
    model_formulas,
    model_prior,
    iter = 500,
    cores = 4,
    chains = 4,
    seed = 888
){
    # set parameters
    options(mc.cores = cores, chains = chains, iter = iter, seed = seed)
    
    # fit models
    fit_0 <- brm(
        model_formulas$f_0,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior[c(1, 3),],
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        seed = 888,
        save_model = here("Stan", "fit_responses_0.stan"),
        file = here("Results", "fit_responses_0.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_1 <- brm(
        model_formulas$f_1,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        seed = 888,
        save_model = here("Stan", "fit_responses_1.stan"),
        file = here("Results", "fit_responses_1.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_2 <- brm(
        model_formulas$f_2,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        seed = 888,
        save_model = here("Stan", "fit_responses_2.stan"),
        file = here("Results", "fit_responses_2.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_3 <- brm(
        model_formulas$f_3,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        sample_prior = "yes",
        seed = 888,
        save_model = here("Stan", "fit_responses_3.stan"),
        file = here("Results", "fit_responses_3.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_4 <- brm(
        model_formulas$f_4,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        sample_prior = "yes",
        seed = 888,
        save_model = here("Stan", "fit_responses_4.stan"),
        file = here("Results", "fit_responses_4.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_5 <- brm(
        model_formulas$f_5,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        sample_prior = "yes",
        seed = 888,
        save_model = here("Stan", "fit_responses_5.stan"),
        file = here("Results", "fit_responses_5.rds"), 
        control = list(adapt_delta = 0.95)
    )
    fit_6 <- brm(
        model_formulas$f_6,
        data = responses,
        family = bernoulli("logit"),
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        sample_prior = "yes",
        seed = 888,
        save_model = here("Stan", "fit_responses_6.stan"),
        file = here("Results", "fit_responses_6.rds"), 
        control = list(adapt_delta = 0.95)
    )
    
    fits <- lst(fit_0, fit_1, fit_2, fit_3, fit_4, fit_5, fit_6)
    
    return(fits)
}


# compare models
get_model_loos <- function(fits){
    path <- here("Results", "model_loos.rds")
    if (file.exists(path)){
        loo <- readRDS(here(path))
    } else {
        loo <- loo_compare(map(fits, loo))
        saveRDS(loo, path)
    }
    return(loo)
}

# get model posterior draws (fixed effects)
get_model_draws_fixed <- function(fit){
    post <- gather_draws(fit, `b_.*`, `sd_.*`, regex = TRUE)
    return(post)
}


# get model posterior expected predictions (fixed effects)
get_model_epreds_fixed <- function(fit, ndraws = 100){
    nd <- expand.grid(
        pthn = c(-1, 1),
        frequency_zipf = 0,
        lv = seq(
            min(fit$data$lv, na.rm = TRUE),
            max(fit$data$lv, na.rm = TRUE),
            by = 0.1
        ),
        group = unique(fit$data$group)
    )
    m <- add_epred_draws(nd, fit, ndraws = 100, re_formula = NA)
    return(m)
}

# get model posterior expected predictions (random effects)
get_model_epreds_random <- function(fit, ndraws = 100, group = c("participant", "word")){
    
    # by participant
    m_re_participants <- NULL
    if ("participant" %in% group){
        nd_re_participants <- expand.grid(
            participant = unique(fit$data$participant),
            pthn = c(-1, 1),
            frequency_zipf = 0,
            lv = seq(
                min(fit$data$lv, na.rm = TRUE),
                max(fit$data$lv, na.rm = TRUE),
                by = 0.1
            ),
            group = NA
        )
        m_re_participants <- add_epred_draws(
            nd_re_participants, 
            fit, 
            re_formula = ~ (1 + frequency_zipf + pthn*lv | participant),
            ndraws = ndraws
        ) 
    }
    
    # by word
    m_re_words <- NULL
    if ("word" %in% group){
        nd_re_words <- expand.grid(
            word = unique(fit$data$word),
            pthn = c(-1, 1),
            frequency_zipf = 0,
            lv = seq(
                min(fit$data$lv, na.rm = TRUE),
                max(fit$data$lv, na.rm = TRUE),
                by = 0.1
            ),
            group = NA
        )
        m_re_words <- add_epred_draws(
            nd_re_words, 
            fit, 
            re_formula = ~ (1| word),
            ndraws = ndraws
        ) 
    }
    m_re <- list(participants = m_re_participants, words = m_re_words)
    
    return(m_re)
}


