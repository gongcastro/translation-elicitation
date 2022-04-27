<<<<<<< HEAD
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
=======
# get SUBTLEX lexical frequencies ----
get_subtlex <- function(){
    
    paths <- list(
        English = here("data", "subtlex", "SUBTLEX-UK.txt"),
        Spanish = here("data", "subtlex", "SUBTLEX-ESP.txt"),
        Catalan = here("data", "subtlex", "SUBTLEX-CAT.txt")
    )
    
    # import SUBTLEX-UK (English)
    subtlex_eng <- paths$English %>% 
        fread(
            verbose = FALSE,
            showProgress = TRUE
        ) %>%
        as_tibble() %>% 
        clean_names() %>% 
        rename(
            word = spelling,
            frequency_count = freq_count,
            frequency_zipf = log_freq_zipf
        ) %>% 
        select(word, frequency_count, frequency_zipf)
    
    
    # import SUBTLEX-ESP (Spanish)
    subtlex_spa <- paths$Spanish %>%
        fread(
            verbose = FALSE,
            showProgress = FALSE,
            select = 1:4
        ) %>% 
        clean_names() %>%
        mutate(frequency_zipf = log10(freq_per_million)+3) %>% 
        rename(frequency_count = freq_count) %>% 
        select(
            word, 
            frequency_count, 
            frequency_zipf
        ) %>% 
        drop_na() 
    
    
    # import SUBTLEX-CAT (Catalan)
    subtlex_cat <- paths$Catalan %>%
        fread(
            verbose = FALSE,
            showProgress = FALSE, dec = "."
        ) %>% 
        clean_names() %>% 
        rename(
            word = words, 
            frequency_count = abs_wf, 
            frequency_zipf = zipf
        ) %>% 
        mutate(frequency_count = as.numeric(str_remove_all(frequency_count, ","))) %>% 
        select(word, frequency_count, frequency_zipf)
    
    # merge datasets
    frequency <- list(
        English = subtlex_eng,
        Spanish = subtlex_spa,
        Catalan = subtlex_cat
    ) %>% 
        bind_rows(.id = "test_language") %>% 
        select(word, test_language, frequency_count, frequency_zipf) 
    
}


# import subtlex
import_subtlex <- function() {
    df <- here("data") %>% 
        list.files(
            pattern = "SUBTLEX",
            full.names = TRUE, 
            recursive = TRUE
        ) %>%
        map(~clean_names(read_xlsx(., na = c("", "NA")))) %>%
        set_names(c("Catalan", "Spanish", "English"))
    
    df$English$freq_rel <- 10^(df$English$freq_zipf-3)
    
    df <- df %>%
        bind_rows(.id = "language") %>%
        select(word, language, freq_rel) %>%
        mutate(freq_zipf = 3+log10(freq_rel))
    
    return(df)
}

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
            lv = stringsim(ipa1, ipa2, method = "lv")
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
        map(~read_xlsx(stimuli_path, sheet = .)) %>% 
        bind_rows(.id = "group") %>% 
        select(
            word1, 
            group, 
            file
        ) %>% 
        mutate(file = here("stimuli", "sounds", file))
    
    audios <- map(stimuli$file, load.wave) 
    
    lengths <- map_dbl(audios, length)/2
    
    sampling_rate <- audios %>% 
        map_dbl(attr, "rate") %>% 
        unique()
    
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
            frequency_zipf = log10(frequency)+3,
            duration = durations
        ) %>% 
        select(
            group,
            word1, 
            word2, 
            ipa1, 
            ipa2,
            frequency,
            frequency_zipf, 
            pthn, 
            lv,
            duration,
            problematic
        ) %>% 
        mutate(
            is_imputed = is.na(frequency_zipf),
        ) %>% 
        # impute missing data
        mice(m = 5, print = FALSE, method = "pmm") %>% 
        complete() %>% 
        as_tibble()
    
    saveRDS(stimuli, "results/stimuli.rds")
    
    return(stimuli)
}
>>>>>>> eb2ad2e01316fbb4878ef163afbb685d3a91ad49
