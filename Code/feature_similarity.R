#### feature symylarity ##################################

#### set up ##############################################

# load packages
library(dplyr)
library(readxl)
library(stringr)
library(janitor)
library(here)

# set params
diacritics <- c("_0", "_?", "~", '̃', "_d", '̪', "_h", "ʰ")

#### import data #########################################
phonemes <- read_xlsx(here("Data", "Phon_list.xlsx"), sheet = "PhoneCoding.broad") %>% 
    clean_names()
phon_codes <- phonemes$code %>%
    set_names(phonemes$ipa)


words <- read_xlsx(here("Data", "TranElicit_word_lists.xlsx"), sheet = "English-Spanish.Task") %>% 
    clean_names() %>% 
    mutate_at(vars(contains("phon")), str_remove, "[[:punct:]]") %>% 
    mutate(max_len = max(nchar(word1), nchar(word2)),
           phon_list1 = strsplit(phon1, ""),
           phon_list2 = strsplit(phon2, "")) %>% 
    mutate_at(vars(phon_list1, phon_list2), lapply, function(x) phon_codes[unlist(x)]) %>% 
    rowwise() %>% 
    mutate(matches = ifelse(nchar(word1) > nchar(word2), sum(phon_list1 %in% phon_list2), sum(phon_list2 %in% phon_list1))) %>% 
    ungroup() %>% 
    mutate(matches_prop = matches/max_len)



