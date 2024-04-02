#' Generate PCT corpora from Clearpond 
#' 
make_pct_corpus <- function(){
    
    # load headers
    cp_h_paths <- file.path("data/stimuli/clearpond",
                            c("spanishCPdatabase2/clearpondHeaders_SP.txt",
                              "englishCPdatabase2/clearpondHeaders_EN.txt"))
    names(cp_h_paths) <- c("spa", "eng")
    cp_spa_h <- readLines(cp_paths["spa"], warn = FALSE)
    cp_eng_h <- readLines(cp_paths["eng"], warn = FALSE)
    
    
    # load Spanish corpora
    cp_paths <- file.path("data/stimuli/clearpond",
                          c("spanishCPdatabase2/spanishCPdatabase2.txt",
                            "englishCPdatabase2/englishCPdatabase2.txt"))
    
    names(cp_paths) <- c("spa", "eng")
    cp_spa <- read_csv(cp_paths["spa"], 
                       col_names = cp_spa_h,
                       progress = FALSE,
                       show_col_types = FALSE) |> 
        janitor::clean_names() |> 
        select(Spelling = word, Transcription = phono, Frequency = frequency) |> 
        write_csv(file.path("data", "pct", "pct-corpus_spa.csv"))
    
    cli::cli_alert_success("Spanish corpus generated")
    
    # load English corpora
    cp_spa <- read_tsv(cp_paths["eng"], 
                       col_names = cp_eng_h,
                       progress = FALSE,
                       show_col_types = FALSE) |> 
        janitor::clean_names() |> 
        select(Spelling = word, Transcription = phono, Frequency = frequency) |> 
        write_csv(file.path("data", "pct", "pct-corpus_eng.csv"))
    
    cli::cli_alert_success("English corpus generated")
    
}


#' Generate PCT corpora from Clearpond
#' 
get_neighbours_cp <- function(group = c("spa-ENG", "cat-ENG", "cat-SPA")){
    
    neigh_helper <- function(x) {
        file.path("data/stimuli/pct", 
                  paste0("pct-neighbours_", x, ".csv")) |> 
            read_csv(na = "", col_types = "cdcd") |> 
            janitor::clean_names() 
    }
    
    neighbours <- map(group, neigh_helper) |> 
        set_names(group) |> 
        bind_rows(.id = "group") |> 
        rename(neighbours = neighbors) |> 
        mutate(neighbours = str_split(neighbours, pattern = ","))
    
    return(neighbours)
    
}


#' Get shared phonemes
#' 
get_shared_phonemes <- function(x, y){
    px <- unlist(strsplit(x, split = ""))
    py <- unlist(strsplit(y, split = ""))
    return(length(intersect(px, py)))
}

#' Get Leveshtein similarity scores
#' 
get_levenshtein <- function(stimuli_path){
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    out <- groups |> 
        map(\(x) read_xlsx(stimuli_path, sheet = x)) |> 
        set_names(groups) |> 
        bind_rows(.id = "group") |> 
        janitor::clean_names() |> 
        select(group, word_1, word_2, sampa_1, sampa_2) |> 
        mutate(across(starts_with("sampa_"), clean_sampa),
               n_char = if_else(nchar(sampa_1) > nchar(sampa_2),
                                nchar(sampa_1), 
                                nchar(sampa_2)),
               lv = stringdist::stringsim(sampa_1, sampa_2, method = "lv"),
               lv_dist = stringdist::stringdist(sampa_1, sampa_2, method = "lv"))
    
    return(out)
}

#' Get audio duration
#' 
get_duration <- function(stimuli_path, audios_path){
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups |> 
        map(\(x) read_xlsx(stimuli_path, sheet = x)) |> 
        set_names(groups) |> 
        bind_rows(.id = "group") |> 
        select(word_1, group, file) |> 
        mutate(file = file.path("stimuli", "sounds", file))
    
    audios <- map(stimuli$file, audio::load.wave) 
    lengths <- map_dbl(audios, length, .progress = TRUE) / 2
    sampling_rate <- unique(map_dbl(audios, attr, "rate", .progress = TRUE))
    duration <- lengths / sampling_rate
    
    return(duration)
}


#' Get neighbours based on Levenshtein distance
#' 
find_neighbours <- function(stimuli, corpus, neighbour_threshold = 1) {
    
    cli_progress_bar("Finding neighbours", total = 3, type = "tasks")
    
    cli_progress_step("Removing punctuation marks")
    x <- str_remove_all(stimuli$sampa_1, "[:punct:]")
    
    cli_progress_step("Calculating Levenshtein distances")
    dist <- stringdistmatrix(x, corpus) <= neighbour_threshold
    dist_n <- rowSums(dist)
    
    cli_progress_step("Calculating Levenshtein similarities")
    sim <- rowMeans(stringsimmatrix(x, corpus))
    
    cli_progress_step("Classifiying neigbours (threshold = {neighbour_threshold})")
    dist_list <- tapply(dist, rep(1:nrow(dist), ncol(dist)), function(i) i)
    dist_list <- lapply(dist_list, \(x) corpus[which(x)])
    
    neighbours <- stimuli |> 
        select(group, trial_id, sampa_1) |> 
        mutate(neigh_n = dist_n,
               neigh_sim = sim,
               neigh_list = dist_list)
    
    return(neighbours)
}

#' Get within-language
#' 
get_neighbours <- function(stimuli_path, type){
    
    stopifnot("type must be one of 'within' or 'across'" = type %in% c("within", "across"))
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups |> 
        map(\(x) read_xlsx(stimuli_path, sheet = x)) |> 
        set_names(groups) |> 
        bind_rows(.id = "group")
    
    read_xp_helper <- function(x){
        read_csv(x, name_repair = janitor::make_clean_names, show_col_types = FALSE) |> 
            mutate(transcription = str_remove_all(transcription, "\\.")) |> 
            distinct(transcription) |> 
            pull(transcription)
    }
    
    corpus <- file.path(paste0("data/stimuli/pct/pct-corpus_",
                               c("eng", "spa"), ".csv")) |> 
        set_names(c("eng", "spa")) |> 
        map(read_xp_helper)
    
    stimuli_split <- split(stimuli, f = stimuli$group)
    corpus_split <- corpus[c("eng", "spa", "eng")] |> 
        set_names(names(stimuli_split))
    
    if (type=="within") {
        neighbours <- map2(stimuli_split, corpus_split, 
                           \(x, y) find_neighbours(x[["sampa_2"]], y),
                           .progress = TRUE) |> 
            bind_rows(.id = "group")
    }
    
    if (type=="across") {
        neighbours <- map2(stimuli_split, corpus_split, 
                           \(x, y) find_neighbours(x, y),
                           .progress = TRUE) |> 
            bind_rows(.id = "group")
    }
    
    return(neighbours)
}


#' Process stimuli and add information
#'
get_stimuli <- function(stimuli_path, neighbours, levenshtein,
                        durations, stimuli_exclude){
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups |> 
        map(\(x) read_xlsx(stimuli_path, sheet = x)) |> 
        set_names(groups) |> 
        bind_rows(.id = "group") |> 
        janitor::clean_names() |> 
        select(group, word_1, word_2, ipa_flat_1, ipa_flat_2,
               sampa_1, sampa_2, practice_trial, file, freq_rel_2)  |> 
        left_join(select(levenshtein, -c(sampa_1, sampa_2)),
                  by = join_by(group, word_1, word_2)) |> 
        mutate(practice_trial = as.logical(practice_trial),
               freq_zipf_2 = log10(freq_rel_2)+3,
               freq_2 = freq_rel_2,
               duration = durations,
               # assign a numeric ID to each unique translation pair
               translation = paste0(word_1, " /", ipa_flat_1, "/ - ",
                                    word_2, " /", ipa_flat_2, "/"),
               translation_id = as.integer(as.factor(translation)),
               # does lexical frequency need to be imputed?
               is_imputed = is.na(freq_zipf_2),
               sampa_1 = str_remove_all(sampa_1, "\\."),
               sampa_2 = str_remove_all(sampa_2, "\\.")) |> 
        select(group, translation, translation_id, word_1, word_2, 
               sampa_1, sampa_2, ipa_flat_1, ipa_flat_2,
               freq_2, freq_zipf_2, 
               lv, lv_dist,
               duration, practice_trial) |> 
        left_join(mutate(neighbours, sampa_1 = str_remove_all(sampa_1, "[[:punct:]]")),
                  by = join_by(group, sampa_1)) |>         
        # mutate(is_imputed = is.na(frequency_zipf)) |> 
        # # impute missing data
        # mice(m = 5, print = FALSE, method = "pmm", ) |> 
        # complete() |> 
        as_tibble() |> 
        dplyr::filter(!(word_1 %in% stimuli_exclude))
    
    saveRDS(stimuli, file.path("results", "stimuli.rds"))
    
    return(stimuli)
}
