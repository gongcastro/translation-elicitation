#' Fit Bayesian regression model in brms
#'
get_model_fit <- function(name, formula, prior, ...) {
  results_path <- file.path("results", paste0(name, ".rds"))

  out <- brms::brm(
    formula = formula,
    family = bernoulli("logit"),
    save_pars = save_pars(all = TRUE),
    iter = 1000,
    cores = 4,
    chains = 4,
    seed = 1234,
    silent = 1,
    control = list(adapt_delta = 0.95),
    file = results_path,
    file_refit = "on_change",
    ...
  )

  return(out)
}

#' Leave-one-out cross-validation
#'
get_model_loos <- function(fits) {
  path <- here::here("results", "model_loos.rds")
  if (file.exists(path)) {
    loo <- readRDS(here(path))
  } else {
    loo <- loo::loo_compare(map(fits, loo))
    saveRDS(loo, path)
  }
  return(loo)
}


#' Get expected posterior predictions
#'
get_epreds <- function(
  model,
  data,
  n = 100,
  lv = seq(0, 1, length.out = 100),
  neigh_n_h = c(0, 2, 4, 8, 12),
  ...
) {
  knowledge <- unique(model$data$knowledge)
  confidence <- unique(model$data$confidence)
  freq_zipf_2 <- mean(data$freq_zipf_2, na.rm = TRUE)
  group <- unique(model$data$group)
  nd <- tidyr::expand_grid(
    freq_zipf_2,
    neigh_n_h,
    lv,
    knowledge,
    confidence,
    group
  )
  if ("experiment" %in% colnames(model$data)) {
    nd <- tidyr::expand_grid(nd, experiment = unique(model$data$experiment))
  }
  epreds <- tidybayes::add_epred_draws(nd, model, re_formula = NA, ...)
  return(epreds)
}

#' Rescale standardised variable to original scale
#'
rescale <- function(x, data_mean, data_sd) {
  y <- (x * data_sd) + data_mean
  return(y)
}
