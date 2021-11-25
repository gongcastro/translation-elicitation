tar_load(responses)

library(stringdist)

threshold <- 0.6

d <- responses %>% 
    mutate(
        overlap_lv = stringsim(input_text, word1, method = "lv"),
        overlap_osa = stringsim(input_text, word1, method = "osa"),
        overlap_hamming = stringsim(input_text, word1, method = "hamming"),
        overlap_jw = stringsim(input_text, word1, method = "jw"),
        overlap_cosine = stringsim(input_text, word1, method = "cosine")
    ) %>% 
    mutate(
        is_correct_exact = input_text==word2,
        is_correct_manual = correct,
        is_correct_lv = overlap_lv >= threshold,
        is_correct_osa = overlap_lv >= threshold,
        is_correct_hamming = overlap_lv >= threshold,
        is_correct_cosine = overlap_lv >= threshold
    ) %>% 
    select(group, trial_id, word, participant, matches("is_correct")) %>% 
    pivot_longer(c(matches("is_correct"), -is_correct_manual), names_to = "method", values_to = "is_correct") %>% 
    mutate(method = str_to_sentence(str_remove(method, "is_correct_"))) %>% 
    group_by(group, word, method) %>% 
    summarise(
        is_correct_manual = sum(is_correct_manual),
        is_correct = sum(is_correct),
        n = n(),
        prop_correct_manual = is_correct_manual/n,
        prop_correct = is_correct/n,
        .groups = "drop"
    )
    
ggplot(d, aes(prop_correct_manual, prop_correct, colour = group)) +
    facet_wrap(~method) +
    # geom_rug(sides = "tr") +
    geom_point(size = 0.75, alpha = 0.5) +
    labs(x = "% correct (manual classification)",
         y = "% correct (automatic classification) \n Similarity threshold: 60%") +
    scale_x_continuous(labels = percent) +
    scale_y_continuous(labels = percent) +
    coord_equal() +
    theme_ggdist()
