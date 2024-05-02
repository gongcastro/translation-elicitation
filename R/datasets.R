#' Get participants
#' 
get_participants <- function(exp_participants, quest_participants) {
    out <- list(Experiment = exp_participants,
                Questionnaire = quest_participants) |> 
        bind_rows(.id = "source")
    
    return(out)
}

#' Get dataset for analysis 2
#'
get_dataset_1 <- function(exp_responses, quest_responses, stimuli) {
    
    dataset_1 <- prepare_data(exp_responses, quest_responses, stimuli) |> 
        dplyr::filter(group %in% c("cat-ENG", "spa-ENG"),
                      source=="Experiment") |> 
        drop_na()|> 
        mutate(across(c(freq_zipf_2, neigh_n, neigh_n_h, avg_sim, avg_sim_h, lv),
                      \(x) scale(x)[, 1],
                      .names = "{.col}_std"),
               group = as.factor(group))
    
    # a priori contrasts for groups
    contrasts(dataset_1$group) <- c(0.5, -0.5)
    
    return(dataset_1)
}

#' Get dataset for analysis 2
#'
get_dataset_2 <- function(exp_responses, quest_responses, stimuli) {
    
    dataset_2 <- prepare_data(exp_responses, quest_responses, stimuli) |> 
        dplyr::filter(source=="Questionnaire") |> 
        drop_na() |> 
        mutate(across(c(freq_zipf_2, neigh_n, neigh_n_h, avg_sim, avg_sim_h, lv),
                      \(x) scale(x)[, 1],
                      .names = "{.col}_std"),
               group = as.factor(group))
    
    # a priori contrasts for groups
    contrasts(dataset_2$group) <- c(0.5, -0.5)
    
    return(dataset_2)
}

#' Get dataset for analysis 3
#'
get_dataset_3 <- function(exp_responses, quest_responses, stimuli) {
    
    dataset_3 <- prepare_data(exp_responses, quest_responses, stimuli) |> 
        dplyr::filter(group %in% c("cat-SPA")) |> 
        drop_na() |> 
        mutate(across(c(freq_zipf_2, neigh_n, neigh_n_h, avg_sim, avg_sim_h, lv),
                      \(x) scale(x)[, 1],
                      .names = "{.col}_std"),
               across(c(group, source), as.factor))

    return(dataset_3)
}

prepare_data <- function(exp_responses, quest_responses, stimuli) {
    
    stimuli_tmp <- clean_stimuli(stimuli)
    
    out <- list(exp_responses, quest_responses) |>
        set_names(c("Experiment", "Questionnaire")) |> 
        bind_rows(.id = "source") |> 
        select(source, participant_id, group, word_1, response, correct,
               response_type) |> 
        left_join(stimuli_tmp, by = join_by(group, word_1))
    
    return(out)
}

clean_stimuli <- function(stimuli) {
    
    out <- stimuli |> 
        select(group, translation, translation_id, word_1, word_2, 
               sampa_1, sampa_2, freq_zipf_2, 
               lv, neigh_n, neigh_n_h, avg_sim, avg_sim_h) |> 
        mutate(word_1 = replace_non_ascii(word_1))
    
    return(out)
}
