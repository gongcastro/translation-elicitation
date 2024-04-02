# dataset for analysis 1
get_dataset_1 <- function(exp_responses, quest_responses, stimuli) {
    
    stimuli_tmp <- stimuli %>%
        select(group, translation_id, word_1, word_2, freq_zipf_2, nd, lv, practice_trial) %>% 
        mutate(across(c(word_1, word_2), replace_non_ascii)) 
    
    scale_variable <- function(x) scale(x)[,1]
    
    dataset_1 <- list(exp_responses, quest_responses) %>%
        set_names(c("Experiment", "Questionnaire")) %>% 
        bind_rows(.id = "source") %>% 
        select(source, participant_id, group, word_1, response, correct) %>% 
        left_join(stimuli_tmp) %>% 
        filter(
            !isTRUE(practice_trial),
            group %in% c("cat-ENG", "spa-ENG"),
        ) %>% 
        drop_na() %>% 
        mutate(
            across(c(freq_zipf_2, nd, lv), scale_variable, .names = "{.col}_std"),
            group = as.factor(group)
        )
    
    # a priori contrasts for groups
    contrasts(dataset_1$group) <- c("cateng_spaeng" = c(0.5, -0.5))
    
    return(dataset_1)
}

# dataset for analysis 2
get_dataset_2 <- function(exp_responses, quest_responses, stimuli) {
    
    stimuli_tmp <- stimuli %>%
        select(group, translation_id, word_1, word_2, freq_zipf_2, nd, lv, practice_trial) %>% 
        mutate(across(c(word_1, word_2), replace_non_ascii)) 
    
    scale_variable <- function(x) scale(x)[,1]
    
    dataset_2 <- list(exp_responses, quest_responses) %>%
        set_names(c("Experiment", "Questionnaire")) %>% 
        bind_rows(.id = "source") %>% 
        select(source, participant_id, group, word_1, response, correct) %>% 
        left_join(stimuli_tmp) %>% 
        filter(
            !isTRUE(practice_trial),
            group %in% c("cat-ENG", "spa-ENG", "cat-SPA"),
        ) %>% 
        drop_na() %>% 
        mutate(
            across(c(freq_zipf_2, nd, lv), scale_variable, .names = "{.col}_std"),
            group = as.factor(group)
        )
    
    # a priori contrasts for groups
    contrasts(dataset_2$group) <- cbind(
        "cateng_spaeng" = c(0.5, 0, -0.5),
        "spa_eng" = c(0.25, 0.5, -0.25)
        )
    
    return(dataset_2)
}

# dataset for analysis 3
get_dataset_3 <- function(exp_responses, quest_responses, stimuli) {
    
    stimuli_tmp <- stimuli %>%
        select(group, translation_id, word_1, word_2, freq_zipf_2, nd, lv, practice_trial) %>% 
        mutate(across(c(word_1, word_2), replace_non_ascii)) 
    
    scale_variable <- function(x) scale(x)[,1]
    
    dataset_3 <- list(exp_responses, quest_responses) %>%
        set_names(c("Experiment", "Questionnaire")) %>% 
        bind_rows(.id = "source") %>% 
        select(source, participant_id, group, word_1, response, correct) %>% 
        left_join(stimuli_tmp) %>% 
        filter(
            !isTRUE(practice_trial),
            group %in% c("cat-ENG", "spa-ENG", "cat-SPA"),
        ) %>% 
        drop_na() %>% 
        mutate(
            across(c(freq_zipf_2, nd, lv), scale_variable, .names = "{.col}_std"),
            across(c(source, group), as.factor)
        )
    
    # a priori contrasts for groups
    contrasts(dataset_3$group) <- cbind(
        "cateng_spaeng" = c(0.5, 0, -0.5),
        "spa_eng" = c(0.25, 0.5, -0.25)
    )
    
    # a priori contrasts for groups
    contrasts(dataset_3$source) <- cbind(
        "exp_quest" = c(-0.5, 0.5)
    )
    
    return(dataset_3)
}
