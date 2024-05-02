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
        iter = 1000,
        cores = 4,
        chains = 4,
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

# get ROC curve of Bayesian model
get_roc_curve <- function(newdata, object, ...) {
    
    # enquote response variable and get brmsfit family
    resp_var <- formula(object)[["formula"]][[2]]
    resp_var <- enquo(resp_var)
    model_fam <- object[["family"]][["family"]]
    
    # object must be a brmsfit object with a supported family
    supported <- c("bernoulli", "binomial", "categorical", "cumulative", "sratio", "cratio", "acat")
    stopifnot(is.brmsfit(object))
    if (!(model_fam %in% supported)) stop(paste0("model family must be one of: ", paste0(supported, collapse = ", ")))
    
    if (model_fam %in% c("binomial", "bernoulli")) {
        roc_values <- add_epred_draws(newdata, object, ndraws = 50) %>% 
            ungroup() %>% 
            mutate(!!resp_var := as.factor(!!resp_var)) %>% 
            # generate a ROC curve for each posterior draw
            split(.$.draw) %>%
            map_dfr(~roc_curve(., truth = !!resp_var, .epred, event_level = "second"), .id = ".draw") 
        
    } else {
        cat_symbols <- syms(as.character(unique(get_y(object))))
        roc_values <- add_epred_draws(newdata, object, ...) %>% 
            ungroup() %>% 
            mutate(!!resp_var := as.factor(!!resp_var)) %>%
            # spread predictions for different categories across different columns
            pivot_wider(names_from = .category, values_from = .epred) %>% 
            # generate a ROC curve for each posterior draw
            split(.$.draw) %>% 
            map_dfr(~roc_curve(., truth = !!resp_var, !!!cat_symbols), .id = ".draw")
    }
    
    return(roc_values)
}

logit_to_prob <- function(x, variable) ifelse(grepl("intercept", tolower(variable)), plogis(x), x/4)
