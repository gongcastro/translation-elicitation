#' Import CLEARPOND database
#'
import_clearpond <- function(cp_c_path_eng,
                             cp_c_path_spa,
                             cp_h_path_eng,
                             cp_h_path_spa) {
  suppressWarnings({
    header <- readLines(file.path(cp_h_path_eng), warn = FALSE)
    eng <- read_tsv(file.path(cp_c_path_eng),
      col_names = header,
      progress = FALSE,
      show_col_types = FALSE
    ) |>
      janitor::clean_names()

    header <- readLines(file.path(cp_h_path_spa), warn = FALSE)
    spa <- read_tsv(file.path(cp_c_path_spa),
      col_names = header,
      progress = FALSE,
      show_col_types = FALSE
    ) |>
      janitor::clean_names()

    out <- bind_rows(
      lst(
        "English" = eng,
        "Spanish" = spa
      ),
      .id = "language"
    ) |>
      rename(
        sampa = phono,
        freq = frequency
      ) |>
      mutate(
        sampa = str_remove_all(sampa, "\\."),
        freq_zipf = log10(1e6 * freq / n()) + 3,
        .by = c(language)
      ) |>
      select(language, word, sampa, freq_zipf)
  })

  return(out)
}

#' Import list of trials and process
#'
get_trial_list <- function(trial_list_path) {
  groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
  names(groups) <- groups

  import_trials <- function(groups, path) {
    read_xlsx(
      path = path,
      sheet = groups,
      .name_repair = janitor::make_clean_names
    )
  }

  trial_list <- groups |>
    map_dfr(import_trials, trial_list_path, .id = "group") |>
    select(
      group, word_1, word_2, ipa_1, ipa_2,
      sampa_1, sampa_2, practice_trial, file
    ) |>
    mutate(across(matches("sampa"), \(x) gsub("[[:punct:]]", "", x)),
      target_language = if_else(group == "cat-SPA", "Spanish", "English"),
      practice_trial = as.logical(practice_trial)
    )

  return(trial_list)
}

#' Get Leveshtein similarity scores
#'
get_levenshtein <- function(trial_list) {
  out <- trial_list |>
    mutate(
      lv = stringdist::stringsim(sampa_1, sampa_2, method = "lv"),
      lv_dist = stringdist::stringdist(sampa_1, sampa_2, method = "lv")
    ) |>
    select(group, matches("word|sampa|lv"))

  return(out)
}

#' Get phonological neighbours
#'
get_neighbours <- function(word_1, word_2, freq_2, language_2,
                           corpus, neighbour_threshold = 1,
                           higher_frequency = FALSE) {
  get_neighbours_helper <- function(pw, tw, tf, cw, cf, threshold) {
    dist_mat <- stringdistmatrix(pw, cw)
    n_list <- cw[which(dist_mat <= threshold)]
    return(n_list)
  }

  n <- length(word_1)
  out <- vector(mode = "list", length = n)
  pb <- cli::cli_progress_bar("Finding neighbours...", total = n)
  corpus_split <- split(corpus, corpus$target_language)

  for (i in 1:n) {
    ci <- corpus_split[[language_2[i]]]
    if (higher_frequency) {
      cw <- ci[ci$freq_zipf_2 >= freq_2[i], ]$sampa
      cf <- ci[ci$freq_zipf_2 >= freq_2[i], ]$freq_zipf_2
    } else {
      cw <- ci$sampa
      cf <- ci$freq_zipf_2
    }
    dist_mat <- stringdistmatrix(word_1[i], cw)
    out[[i]] <- ci[which(dist_mat <= neighbour_threshold), ]$word_2
    cli::cli_progress_update()
  }
  cli::cli_progress_done()

  return(out)
}

#' Get phonological neighbours
#'
get_avg_sim <- function(word_1, word_2, freq_2, language_2,
                        corpus, higher_frequency = FALSE) {
  n <- length(word_1)
  out <- vector(mode = "double", length = n)
  pb <- cli::cli_progress_bar("Averaging similarity...", total = n)

  corpus_split <- split(corpus, corpus$target_language)

  for (i in 1:n) {
    ci <- corpus_split[[language_2[i]]]
    if (higher_frequency) {
      cw <- ci[ci$freq_zipf_2 >= freq_2[i], ]$sampa
      cf <- ci[ci$freq_zipf_2 >= freq_2[i], ]$freq_zipf_2
    } else {
      cw <- ci$sampa
      cf <- ci$freq_zipf_2
    }
    sim_mat <- stringsimmatrix(word_1[i], cw)
    out[i] <- mean(sim_mat, na.rm = TRUE)
    cli::cli_progress_update()
  }
  cli::cli_progress_done()

  return(out)
}

#' Get audio duration
#'
get_duration <- function(trial_list, audios_path) {
  trials <- trial_list |>
    select(word_1, group, file) |>
    mutate(file = file.path("stimuli", "sounds", file))

  audios <- map(trials$file, audio::load.wave, .progress = TRUE)
  lengths <- map_dbl(audios, length, .progress = TRUE) / 2
  sampling_rate <- unique(map_dbl(audios, attr, "rate", .progress = TRUE))
  duration <- lengths / sampling_rate

  return(duration)
}

#' Process stimuli and add information
#'
get_stimuli <- function(trial_list, levenshtein, corpus,
                        durations, stimuli_exclude) {
  corpus_tmp <- corpus |>
    select(
      word_2 = word,
      sampa,
      freq_zipf_2 = freq_zipf,
      target_language = language
    )

  levenshtein_tmp <- select(levenshtein, -c(sampa_1, sampa_2))

  stimuli <- trial_list |>
    mutate(duration = durations) |>
    left_join(levenshtein_tmp,
      by = join_by(group, word_1, word_2)
    ) |>
    left_join(select(corpus_tmp, -sampa),
      by = join_by(word_2, target_language)
    ) |>
    mutate(
      practice_trial = as.logical(practice_trial),
      # assign a numeric ID to each unique translation pair
      translation = paste0(
        word_1, " /", ipa_1, "/ - ",
        word_2, " /", ipa_2, "/"
      ),
      translation_id = as.integer(as.factor(translation)),
      # does lexical frequency need to be imputed?
      is_imputed = is.na(freq_zipf_2)
    ) |>
    select(
      group, target_language, translation, translation_id, word_1, word_2,
      sampa_1, sampa_2, ipa_1, ipa_2,
      freq_zipf_2, lv, lv_dist,
      duration, practice_trial
    ) |>
    dplyr::filter(!(word_1 %in% stimuli_exclude)) |>
    mutate(
      avg_sim = get_avg_sim(
        word_1 = sampa_1,
        word_2 = sampa_2,
        freq_2 = freq_zipf_2,
        language_2 = target_language,
        corpus = corpus_tmp
      ),
      avg_sim_h = get_avg_sim(
        word_1 = sampa_1,
        word_2 = sampa_2,
        freq_2 = freq_zipf_2,
        language_2 = target_language,
        corpus = corpus_tmp,
        higher_frequency = TRUE
      ),
      neigh_lst = get_neighbours(
        word_1 = sampa_1,
        word_2 = sampa_2,
        freq_2 = freq_zipf_2,
        language_2 = target_language,
        corpus = corpus_tmp
      ),
      neigh_lst_h = get_neighbours(
        word_1 = sampa_1,
        word_2 = sampa_2,
        freq_2 = freq_zipf_2,
        language_2 = target_language,
        corpus = corpus_tmp,
        higher_frequency = TRUE
      ),
      neigh_n = map_int(neigh_lst, length),
      neigh_n_h = map_int(neigh_lst_h, length)
    )
  # mutate(is_imputed = is.na(frequency_zipf)) |>
  # # impute missing data
  # mice(m = 5, print = FALSE, method = "pmm", ) |>
  # complete() |>

  out_path <- file.path("data", "stimuli.csv")
  out_stimuli <- stimuli |>
    rowwise() |>
    mutate(across(
      matches("neigh_lst"),
      \(x) paste0(unlist(x), collapse = ", ")
    )) |>
    ungroup()
  arrow::write_csv_arrow(out_stimuli, out_path)
  cli_alert_success("Saved {.emph stimuli} as {.file {out_path}}")

  return(stimuli)
}


levenshtein <- function(a, b) {
  distances <- matrix(0, length(a) + 1, length(b) + 1)
  distances[, 1] <- 0:length(a)
  distances[1, ] <- 0:length(b)

  for (row in 2:(length(a) + 1)) {
    for (col in 2:(length(b) + 1)) {
      distances[row, col] <- min(c(
        distances[row - 1, col - 1] + as.integer(a[row - 1] != b[col - 1]),
        distances[row, col - 1] + 1,
        distances[row - 1, col] + 1
      ))
    }
  }

  return(distances[length(a) + 1, length(b) + 1])
}

levenshtein_norm <- function(...) {
  dist <- levenshtein(...)
  max_length <- max(length(c(...)))
  return(1 - distances[length(a) + 1, length(b) + 1] / max_length)
}
