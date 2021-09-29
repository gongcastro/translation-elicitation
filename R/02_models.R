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
        save_model = here("Stan", "fit_responses_0.stan"),
        file = here("Results", "fit_responses_0.rds")
    )
    fit_1 <- brm(
        model_formulas$f_1,
        data = responses,
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        save_model = here("Stan", "fit_responses_1.stan"),
        file = here("Results", "fit_responses_1.rds")
    )
    fit_2 <- brm(
        model_formulas$f_2,
        data = responses,
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        save_model = here("Stan", "fit_responses_2.stan"),
        file = here("Results", "fit_responses_2.rds")
    )
    fit_3 <- brm(
        model_formulas$f_3,
        data = responses,
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        save_model = here("Stan", "fit_responses_3.stan"),
        file = here("Results", "fit_responses_3.rds")
    )
    fit_4 <- brm(
        model_formulas$f_4,
        data = responses,
        prior = model_prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        save_model = here("Stan", "fit_responses_4.stan"),
        file = here("Results", "fit_responses_4.rds")
    )
    
    fits <- list(fit_0 = fit_0, fit_1 = fit_1, fit_1 = fit_2, fit_1 = fit_3, fit_1 = fit_4)
    
    return(fits)
}

# compre models
get_model_loos <- function(fits){
    loos <- map(fits, loo)
    loos_comp <- loo_compare(loos)
    return(loos_comp)
}
