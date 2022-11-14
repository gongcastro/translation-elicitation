
# generate PCT corpora from Clearpond 
make_pct_corpus <- function(){
    
    # load headers
    corpus_spa_headers <- readLines(
        here("data", "clearpond", "spanishCPdatabase2", "clearpondHeaders_SP.txt"),
        warn = FALSE
    )
    
    corpus_eng_headers <- readLines(
        here("data", "clearpond", "englishCPdatabase2", "clearpondHeaders_EN.txt"),
        warn = FALSE
    )
    
    # load corpora
    suppressWarnings({
        corpus_spa <- here("data", "clearpond", "spanishCPdatabase2", "spanishCPdatabase2.txt") %>% 
            read_tsv(col_names = corpus_spa_headers, show_col_types = FALSE) %>% 
            clean_names() %>% 
            select(Spelling = word, Transcription = phono, Frequency = frequency) %>% 
            write_csv(
                here("data", "pct", "pct-corpus_spa.csv")
            )
    })
    
    message("Spanish corpus generated")
    
    suppressWarnings({
        
        here("data", "clearpond", "englishCPdatabase2", "englishCPdatabase2.txt") %>% 
            read_tsv(col_names = corpus_eng_headers, show_col_types = FALSE) %>% 
            clean_names() %>% 
            select(
                Spelling = word, 
                Transcription = phono, 
                Frequency = frequency
            ) %>% 
            write_csv(
                here("data", "pct", "pct-corpus_eng.csv")
            )
    })
    
    message("English corpus generated")
    
}


# generate PCT corpora from Clearpond 
get_neighbours_cp <- function(group = c("spa-ENG", "cat-ENG", "cat-SPA")){
    suppressWarnings({
        neighbours <- lapply(
            group,
            function(x) {
                here("data", "pct", paste0("pct-neighbours_", x, ".csv")) %>% 
                    read_csv(na = "", col_types = "cdcd") %>% 
                    clean_names() 
            }
        ) %>% 
            bind_rows() %>% 
            rename(neighbours = neighbors) %>% 
            mutate(neighbours = str_split(neighbours, pattern = ","))
    })
    
    return(neighbours)
    
}


# get shared phonemes
get_shared_phonemes <- function(x, y){
    length(
        intersect(
            unlist(strsplit(x, split = "")),
            unlist(strsplit(y, split = ""))
        )
    )
}

# get Leveshtein similarity scores
get_levenshtein <- function(stimuli_path){
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    levenshtein <- groups %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        set_names(groups) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(group, word_1, word_2, sampa_1, sampa_2) %>% 
        mutate(
            across(starts_with("sampa_"), clean_sampa),
            n_char = ifelse(
                nchar(sampa_1) > nchar(sampa_2),
                nchar(sampa_1), 
                nchar(sampa_2)
            ),
            lv = stringsim(sampa_1, sampa_2, method = "lv"),
            lv_dist = stringdist(sampa_1, sampa_2, method = "lv")
        )
    
    return(levenshtein)
}

# get audio duration
get_duration <- function(stimuli_path, audios_path){
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        set_names(groups) %>% 
        bind_rows(.id = "group") %>% 
        select(word_1, group, file) %>% 
        mutate(file = here("stimuli", "sounds", file))
    
    audios <- map(stimuli$file, load.wave) 
    
    lengths <- map_dbl(audios, length)/2
    
    sampling_rate <- audios %>% 
        map_dbl(attr, "rate") %>% 
        unique()
    
    duration <- lengths/sampling_rate
    
    return(duration)
}


# get within-language 
get_neighbours <- function(stimuli_path, type){
    
    stopifnot("type must be one of 'within' or 'across'" = type %in% c("within", "across"))
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        set_names(groups) %>% 
        bind_rows(.id = "group")
    
    corpus <- paste0("data/pct/pct-corpus_", c("eng", "spa"), ".csv") %>% 
        set_names("eng", "spa") %>% 
        map(
            function(x){
                suppressMessages({
                    read_csv(x, name_repair = make_clean_names) %>% 
                        mutate(transcription = str_remove_all(transcription, "\\.")) %>% 
                        distinct(transcription) %>% 
                        pull(transcription)
                })
            }
        )
    
    stimuli_split <- split(stimuli, f = stimuli$group)
    corpus_split <- corpus[c("eng", "spa", "eng")] %>% 
        set_names(names(stimuli_split))
    
    if (type=="within") {
        neighbours <- map2(
            stimuli_split, corpus_split, 
            ~find_neighbours(.x[["sampa_2"]], .y)
        ) %>% 
            bind_rows(.id = "group")
    }
    
    if (type=="across") {
        neighbours <- map2(
            stimuli_split, corpus_split, 
            ~find_neighbours(.x[["sampa_1"]], .y)
        ) %>% 
            bind_rows(.id = "group")
    }
    
    return(neighbours)
}


# process stimuli and add information
get_stimuli <- function(stimuli_path, neighbours, levenshtein, durations, stimuli_exclude){
    
    groups <- c("spa-ENG", "cat-ENG", "cat-SPA")
    
    stimuli <- groups %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        set_names(groups) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(group, word_1, word_2, ipa_flat_1, ipa_flat_2, sampa_1, sampa_2, practice_trial, file, freq_rel_2)  %>% 
        left_join(select(levenshtein, -c(sampa_1, sampa_2))) %>% 
        mutate(
            practice_trial = as.logical(practice_trial),
            freq_zipf_2 = log10(freq_rel_2)+3,
            freq_2 = freq_rel_2,
            duration = durations,
            # assign a numeric ID to each unique translation pair
            translation = paste0(word_1, " /", ipa_flat_1, "/ - ", word_2, " /", ipa_flat_2, "/"),
            translation_id = as.integer(as.factor(translation)),
            # does lexical frequency need to be imputed?
            is_imputed = is.na(freq_zipf_2),
            sampa_1 = str_remove_all(sampa_1, "\\."),
            sampa_2 = str_remove_all(sampa_2, "\\.")
        ) %>% 
        select(
            group, translation, translation_id, word_1, word_2, 
            sampa_1, sampa_2, ipa_flat_1, ipa_flat_2,
            freq_2, freq_zipf_2, 
            lv, lv_dist,
            duration, practice_trial
        ) %>% 
        left_join(
            rename(
                neighbours,
                sampa_1 = token, 
                nd = neighbour_dens,
                nd_list = neighbour_list
            )
        ) %>%         
        # mutate(is_imputed = is.na(frequency_zipf)) %>% 
        # # impute missing data
        # mice(m = 5, print = FALSE, method = "pmm", ) %>% 
        # complete() %>% 
        as_tibble() %>% 
        filter(!(word_1 %in% stimuli_exclude))
    
    saveRDS(stimuli, "results/stimuli.rds")
    
    return(stimuli)
}
