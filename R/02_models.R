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

# get model posterior draws (fixed effects)
get_model_draws_fixed <- function(fit){
    post <- gather_draws(fit, `b_.*`, `sd_.*`, regex = TRUE)
    return(post)
}


# get model posterior expected predictions (fixed effects)
get_model_epreds_fixed <- function(fit, ndraws = 100){
    nd <- expand.grid(
        pthn_std = c(-1, 1),
        frequency_zipf_std = 0,
        lv_std = seq(
            min(fit$data$lv_std, na.rm = TRUE),
            max(fit$data$lv_std, na.rm = TRUE),
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
            pthn_std = c(-1, 1),
            frequency_zipf_std = 0,
            lv_std = seq(
                min(fit$data$lv_std, na.rm = TRUE),
                max(fit$data$lv_std, na.rm = TRUE),
                by = 0.1
            ),
            group = NA
        )
        m_re_participants <- add_epred_draws(
            nd_re_participants, 
            fit, 
            re_formula = ~ (1 + frequency_zipf_std + pthn_std*lv_std | participant),
            ndraws = ndraws
        ) 
    }
    
    # by word
    m_re_words <- NULL
    if ("word" %in% group){
        nd_re_words <- expand.grid(
            word = unique(fit$data$word),
            pthn_std = c(-1, 1),
            frequency_zipf_std = 0,
            lv_std = seq(min(fit$data$lv_std, na.rm = TRUE), max(fit$data$lv_std, na.rm = TRUE), by = 0.1),
            group = NA
        )
        m_re_words <- add_epred_draws(nd_re_words, fit, re_formula = ~ (1| word), ndraws = ndraws) 
    }
    m_re <- list(participants = m_re_participants, words = m_re_words)
    
    return(m_re)
}


get_model_draws_random <- function(fit, ndraws = 100, group = c("participant", "word")){
    
    draws_participant <- NULL
    if ("participant" %in% group){
        draws_participant <- gather_draws(fit, r_participant[participant, .param], ndraws = ndraws)
    }
    draws_word <- NULL
    if ("word" %in% group){
        draws_word <- gather_draws(fit, r_word[word, .param], ndraws = ndraws)
    }
    draws <- list(participants = draws_participant, words = draws_word)
    return(draws)
}

