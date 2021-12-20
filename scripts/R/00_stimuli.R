# relative frequencies and phonological neighbours
get_clearpond <- function(clearpond_path){
    clearpond <- clearpond_path %>% 
        map(
            function(x){
                read.csv(x) %>% 
                    clean_names() %>% 
                    select("word", "pho_word", "freq_per_million", "pthn")
            }
        ) %>% 
        bind_rows(.id = "group") %>% 
        as_tibble() %>%
        distinct(word, group, .keep_all = TRUE) %>% 
        rename(word2 = word, phon_clearpond = pho_word, frequency = freq_per_million)
    
    return(clearpond)
}

get_levenshtein <- function(stimuli_path){

    levenshtein <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        ~read_xlsx(stimuli_path, sheet = .)
    ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(group, word1, word2, ipa1, ipa2) %>% 
        mutate(
            n_char = ifelse(nchar(ipa1) > nchar(ipa2), nchar(ipa1), nchar(ipa2)), # number of characters
            lv = stringsim(ipa1, ipa2, method = "lv") # Levenshtein similarity (proportion)
        )
    
    return(levenshtein)
}


# get audio duration
get_duration <- function(stimuli_path, audios_path){
    stimuli <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        ~read_xlsx(stimuli_path, sheet = .)) %>% 
        bind_rows(.id = "group") %>% 
        select(word1, group, file) %>% 
        mutate(file = here("stimuli", file))
    
    audios <- map(stimuli$file, load.wave) # load audio
    lengths <- map_dbl(audios, length)/2 # get number of samples (only one channel)
    sampling_rate <- unique(map_dbl(audios, ~attr(., "rate"))) # get sampling rates
    duration <- lengths/sampling_rate # get duration (in seconds)
    return(duration)
}

get_stimuli <- function(stimuli_path, clearpond, levenshtein, durations, save = TRUE){
    
    stimuli <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        ~read_xlsx(stimuli_path, sheet = .)
    ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(-trial_id) %>% 
        left_join(clearpond) %>%
        left_join(levenshtein) %>% 
        mutate(
            frequency_zipf = log10(frequency)+3, # transform frequencies to Zipf scores
            duration = durations
        ) %>% 
        select(group, word1, word2, ipa1, ipa2, frequency, frequency_zipf, pthn, lv, duration) 
    
    if (save) saveRDS(stimuli, here("results", "stimuli.rds"))
    
    return(stimuli)
}
