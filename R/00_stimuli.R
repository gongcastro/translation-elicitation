# relative frequencies and phonological neighbours
get_clearpond <- function(clearpond_path){
    clearpond <- clearpond_path %>% 
        map(
            function(x){
                read.csv(x) %>% 
                    clean_names() %>% 
                    select(
                        "word",
                        "pho_word", 
                        "freq_per_million", 
                        "pthn"
                    )
            }
        ) %>% 
        bind_rows(.id = "group") %>% 
        as_tibble() %>%
        distinct(
            word, 
            group, 
            .keep_all = TRUE
        ) %>% 
        rename(
            word2 = word,
            phon_clearpond = pho_word,
            frequency = freq_per_million
        )
    return(clearpond)
}

# get Leveshtein similarity scores
get_levenshtein <- function(stimuli_path){
    
    levenshtein <- c(
        "ENG-SPA" = "English-Spanish", 
        "ENG-CAT" = "English-Catalan",
        "SPA-CAT" = "Spanish-Catalan"
    ) %>% 
        map(
            function(x) read_xlsx(stimuli_path, sheet = x)
        ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(
            group, 
            word1, 
            word2, 
            ipa1,
            ipa2
        ) %>% 
        mutate(
            n_char = ifelse(
                nchar(ipa1) > nchar(ipa2),
                nchar(ipa1),
                nchar(ipa2)
            ),
            lv = stringsim(
                ipa1, 
                ipa2, 
                method = "lv"
            )
        )
    
    return(levenshtein)
}

# get audio duration
get_duration <- function(
    stimuli_path,
    audios_path
){
    stimuli <- c(
        "ENG-SPA" = "English-Spanish",
        "ENG-CAT" = "English-Catalan", 
        "SPA-CAT" = "Spanish-Catalan"
    ) %>% 
        map(
            ~read_xlsx(
                stimuli_path, 
                sheet = .
            )
        ) %>% 
        bind_rows(.id = "group") %>% 
        select(
            word1, 
            group, 
            file
        ) %>% 
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
    
    stimuli <- c(
        "ENG-SPA" = "English-Spanish",
        "ENG-CAT" = "English-Catalan",
        "SPA-CAT" = "Spanish-Catalan"
    ) %>% 
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(-trial_id) %>% 
        left_join(clearpond) %>%
        left_join(levenshtein) %>% 
        mutate(
            word1 = replace_non_ascii(word1),
            frequency_zipf = log10(frequency)+3,
            duration = durations,
            # assign a numeric ID to each unique translation pair
            translation = paste0(word1, " /", ipa1, "/ - ", word2, " /", ipa2, "/"),
            translation_id = as.integer(as.factor(translation)),
            # does lexical frequency need to be imputed?
            is_imputed = is.na(frequency_zipf)
        ) %>% 
        select(
            group,
            translation,
            translation_id,
            word1, 
            word2,
            ipa1, 
            ipa2, 
            frequency, 
            frequency_zipf,
            pthn, 
            lv, 
            duration
        ) %>% 
        # impute missing data
        mice(
            m = 5, 
            print = FALSE,
            method = "pmm"
        ) %>% 
        complete() %>% 
        as_tibble()
    
    saveRDS(stimuli, "results/stimuli.rds")
    
    return(stimuli)
}
