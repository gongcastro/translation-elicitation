# models

get_model_fit <- function(name, formula, prior, ...){
    
    stan_path <- here("stan", paste0(name, ".stan"))
    results_path <- here("results", paste0(name, ".rds"))
    
    brm(
        formula = formula,
        family = bernoulli("logit"),
        prior = prior,
        save_pars = save_pars(all = TRUE),
        backend = "cmdstanr",
        iter = 6000,
        cores = 1,
        chains = 1,
        seed = 888,
        control = list(adapt_delta = 0.95),
        save_model = stan_path,
        file = results_path,
        sample_prior = "yes",
        ...
    )
}

# leave-one-out cross-validation
get_model_loos <- function(fits){
    path <- here("results", "model_loos.rds")
    if (file.exists(path)){
        loo <- readRDS(here(path))
    } else {
        loo <- loo_compare(map(fits, loo))
        saveRDS(loo, path)
    }
    return(loo)
}



