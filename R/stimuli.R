# trial information

# set up ----

# load packages
library(tidyverse)
library(data.table)
library(readxl)
library(janitor)

# load/create functions
source("R/utils.R")

# set parameters
individual_plots <- FALSE

# clearpond ----
# relative frequencies and phonological neighbours
clearpond <- map(
  list(`ENG-CAT` = "Data/clearpond/clearpond_english.csv",
    `ENG-SPA` = "Data/clearpond/clearpond_english.csv",
    `SPA-CAT` = "Data/clearpond/clearpond_spanish.csv"),
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

# trace ----
# jTRACE transcriptions
trace <- read_xlsx("Stimuli/trace.xlsx") %>% 
  distinct(ort_eng, .keep_all = TRUE) %>% 
  rename(word2 = ort_eng, phon_trace = trace_eng)

# trials ----
trials <- map(
  c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
  function(x) read_xlsx("Stimuli/trials.xlsx", sheet = x)
) %>% 
  bind_rows(.id = "group") %>% 
  clean_names() %>% 
  select(trial_id, group, word1, word2, consonant_ratio, vowel_ratio, onset, overlap_stress) %>% 
  left_join(clearpond) %>% 
  left_join(trace)

# export ----
saveRDS(trials, "Data/trials.rds")
write.csv(trials, "Data/trials.csv", row.names = FALSE)


