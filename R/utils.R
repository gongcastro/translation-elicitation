#' Get first non-missing value in vector
#'
first_non_na <- function(x) {
  ifelse(is.logical(first(x[!is.na(x)])), NA, first(x[!is.na(x)]))
}

#' Get last non-missing value in vector
#'
last_non_na <- function(x) {
  ifelse(is.logical(last(x[!is.na(x)])), NA, last(x[!is.na(x)]))
}

#' Custom ggplot2 theme
#'
theme_custom <- function() {
  theme(
    panel.background = element_rect(fill = "transparent"),
    panel.grid = element_blank(),
    panel.grid.major.y = element_line(colour = "grey", linetype = "dotted"),
    panel.border = element_rect(fill = "transparent", colour = "black"),
    text = element_text(colour = "black", size = 15),
    axis.text = element_text(colour = "black")
  )
}

#' Remove non-ASCII characters (diacritic accents)
#'
replace_non_ascii <- function(x) {
  str_replace_all(
    x,
    enc2utf8(c(
      "á" = "a",
      "é" = "e",
      "í" = "i",
      "ó" = "o",
      "ú" = "u",
      "à" = "a",
      "è" = "e",
      "ò" = "o",
      "ñ" = "n",
      "ç" = "c",
      "ü" = "u"
    ))
  )
}

#' Evaluate participant-level inclusion criteria
#'
validate_participants <- function(
  x,
  min_valid_trials = 0.80,
  blocked_languages = c("Italian", "Spanish", "French"),
  age_range = c(18, 26)
) {
  max_cat_trials <- 86 # max of Catalan trials
  max_spa_trials <- 103 # max number of Spanish trials

  to_remove <- c(
    "is_valid_age",
    "min_valid_ntrials",
    "is_valid_ntrials",
    "is_valid_langproblems",
    "is_valid_l2"
  )
  out <- x |>
    mutate(
      is_valid_age = between(age, age_range[1], age_range[2]),
      min_valid_ntrials = if_else(
        group == "spa-ENG",
        .env$min_valid_trials * max_spa_trials,
        .env$min_valid_trials * max_cat_trials
      ),
      is_valid_ntrials = n_trials_valid >= min_valid_ntrials,
      is_valid_langproblems = !has_language_problems,
      is_valid_l2 = !(l2 %in% blocked_languages),
      valid_status = case_when(
        !is_valid_age ~ "Invalid age",
        !is_valid_ntrials ~ "Insufficient trials",
        !is_valid_l2 ~ "Blocked L2",
        !is_valid_langproblems ~ "Language impairment",
        .default = "Valid"
      )
    ) |>
    select(-any_of(to_remove))

  return(out)
}


#' Proportion adjusted from boundary values (Gelman, Hill & Vehtari, 2020)
#'
prop_adj <- function(x, n) {
  e <- (x + 2) / (n + 4)
  return(e)
}

#' Adjusted standard error of proportion (Gelman, Hill & Vehtari, 2020)
#'
prop_adj_se <- function(x, n) {
  e <- (x + 2) / (n + 4)
  se <- sqrt(e * (1 - e) / (n + 4))
  return(se)
}

#' Adjusted standard error of proportion (Gelman, Hill & Vehtari, 2020)
#'
prop_adj_ci <- function(x, n, .width = 0.95) {
  e <- (x + 2) / (n + 4)
  se <- sqrt(e * (1 - e) / (n + 4))
  ci <- e + qnorm(c((1 - .width) / 2, (1 - (1 - .width) / 2))) * se
  ci[1] <- ifelse(ci[1] < 0, 0, ci[1]) # truncate at 0
  ci[2] <- ifelse(ci[2] > 1, 1, ci[2]) # truncate at 1
  return(ci)
}
