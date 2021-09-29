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

get_trace <- function(trace_path){
    trace <- trace_path %>% 
        read_xlsx() %>%
        distinct(ort_eng, .keep_all = TRUE) %>% 
        rename(word2 = ort_eng, phon_trace = trace_eng)
    return(trace)
}

get_levenshtein <- function(stimuli_path){
    levenshtein <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        function(x) read_xlsx(stimuli_path, sheet = x)
    ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        select(trial_id, group, ipa1, ipa2) %>% 
        mutate(
            n_char = ifelse(nchar(ipa1) > nchar(ipa2), nchar(ipa1), nchar(ipa2)),
            lv = stringsim(ipa1, ipa2, method = "lv")
        )
    
    return(levenshtein)
}

get_stimuli <- function(
    stimuli_path,
    clearpond,
    trace,
    levenshtein
){
    
    # trials ----
    stimuli <- map(
        c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
        function(x) read_xlsx(stimuli_path, sheet = x)
    ) %>% 
        bind_rows(.id = "group") %>% 
        clean_names() %>% 
        left_join(clearpond) %>%
        left_join(levenshtein) %>% 
        left_join(trace) %>% 
        mutate(frequency_zipf = log10(frequency)+3) %>% 
        select(trial_id, group, word1, word2, ipa1, ipa2, phon_trace, frequency, frequency_zipf, pthn, lv,
               consonant_ratio, vowel_ratio, onset, overlap_stress)
    
    return(stimuli)
}
