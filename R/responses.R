#### Response patterns ###################

#### set up ##############################

# load packages
library(dplyr)
library(tidyr)
library(ggplot2)
library(data.table)
library(here)

# set params
set.seed(888)

#### get response patterns ###############
dat <- fread(here("Data", "03_accuracy_coded.csv"), na.strings = c("", "NA")) %>%
    as_tibble() %>% 
    mutate_at(vars(same_onset, group), as.factor) %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           correct_coded = ifelse(correct_coded, "Correct", "Wrong"),
           group = as.factor(group),) %>%
    filter(valid_response) %>% 
    group_by(trial_id, word, group, input_text) %>%
    summarise(n = n(), .groups = "drop") %>% 
    arrange(trial_id, -n) %>% 
    mutate(input_text = fct_inorder(input_text)) %>% 
    group_by(trial_id) %>% 
    slice_head(n = 5) %>% 
    ungroup()

target_trials <- dat %>%
    group_by(trial_id) %>% 
    slice_max(order_by = n, n = 2) %>% 
    group_by(trial_id) %>% 
    summarise(n = min(n), .groups = "drop") %>% 
    filter(n > 5)

#### visualise data ######################
dat %>%
    filter(trial_id %in% target_trials$trial_id) %>% 
    ggplot(aes(x = input_text, y = n, fill = group)) +
    facet_wrap(word~group, scales = "free_x", ncol = 3) +
    geom_col() +
    labs(x = "Typed response", y = "Counts", fill = "Correct?") +
    theme_classic() +
    theme(legend.title = element_blank(),
          legend.position = "top",
          axis.text.x = element_text(angle = 90))+
    ggsave(here("Figures", "response_patterns.png"), height = 49, width = 15)
    


