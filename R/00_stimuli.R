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

# get Leveshtein similarity scores
get_levenshtein <- function(stimuli_path){
    
    levenshtein <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        function(x) read_xlsx(stimuli_path, sheet = x)
    ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(group, word1, word2, ipa1, ipa2) %>% 
        mutate(
            n_char = ifelse(nchar(ipa1) > nchar(ipa2), nchar(ipa1), nchar(ipa2)),
            lv = stringsim(ipa1, ipa2, method = "lv")
        )
    
    return(levenshtein)
}

# get audio duration
get_duration <- function(
    stimuli_path,
    audios_path
){
    stimuli <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        ~read_xlsx(stimuli_path, sheet = .)) %>% 
        bind_rows(.id = "group") %>% 
        select(word1, group, file) %>% 
        mutate(file = here("stimuli", "sounds", file))
    
    audios <- map(stimuli$file, load.wave) 
    lengths <- map_dbl(audios, length)/2
    sampling_rate <- unique(map_dbl(audios, ~attr(., "rate")))
    duration <- lengths/sampling_rate
    return(duration)
}

# process stimuli and add information
get_stimuli <- function(
    stimuli_path,
    clearpond,
    levenshtein,
    durations
){
    
    stimuli <- c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan") %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(-trial_id) %>% 
        left_join(clearpond) %>%
        left_join(levenshtein) %>% 
        mutate(
            frequency_zipf = log10(frequency)+3,
            duration = durations
        ) %>% 
        select(group, word1, word2, ipa1, ipa2, frequency, frequency_zipf, pthn, lv, duration) %>% 
        mutate(
            is_imputed = is.na(frequency_zipf),
        ) %>% 
        # impute missing data
        mice(m = 5, print = FALSE, method = "pmm") %>% 
        complete() %>% 
        as_tibble()
    
    return(stimuli)
}
