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
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        sample_prior = "yes",
        seed = 888,
        save_model = here("Stan", "fit_responses_3.stan"),
        file = here("Results", "fit_responses_3.rds"), 
        control = list(adapt_delta = 0.95)
    )
    
    
    fits <- list(fit_0 = fit_0, fit_1 = fit_1, fit_2 = fit_2, fit_3 = fit_3)
    
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
        )
    )
    m <- add_epred_draws(nd, fit, ndraws = 100, re_formula = NA)
    return(m)
}

# get model posterior expected predictions (random effects)
get_model_epreds_random <- function(fit, ndraws = 10){
    nd_re <- expand.grid(
        participant = unique(fit$data$participant),
        pthn = c(-1, 1),
        frequency_zipf = 0,
        lv = seq(
            min(fit$data$lv, na.rm = TRUE),
            max(fit$data$lv, na.rm = TRUE),
            by = 0.1
        )
    )
    m_re <- add_epred_draws(nd_re, fit, ndraws = 10) 
    return(m_re)
}


