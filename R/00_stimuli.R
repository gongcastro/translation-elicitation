# trial information

# set up ----

# load packages
library(tidyverse)
library(readxl) # to import  Excel spreadsheets
library(janitor) # to clean column names
library(stringdist) # to compute Levenshtein distance
library(here) # to locate files

# load/create functions
source(here("R", "utils.R"))

# set parameters
individual_plots <- FALSE

# clearpond ----
# relative frequencies and phonological neighbours
clearpond <- map(
  list(
    `ENG-CAT` = here("Data", "clearpond", "clearpond_english.csv"),
    `ENG-SPA` = here("Data", "clearpond", "clearpond_english.csv"),
    `SPA-CAT` = here("Data", "clearpond", "clearpond_spanish.csv")
  ),
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
trace <- read_xlsx(here("Stimuli", "trace.xlsx")) %>% 
  distinct(ort_eng, .keep_all = TRUE) %>% 
  rename(word2 = ort_eng, phon_trace = trace_eng)

# levenshtein distance ----
lv <- map(
  c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
  function(x) read_xlsx(here("Stimuli", "trials.xlsx"), sheet = x)
) %>% 
  bind_rows(.id = "group") %>% 
  clean_names() %>% 
  select(trial_id, group, ipa1, ipa2) %>% 
  mutate(
    n_char = ifelse(nchar(ipa1) > nchar(ipa2), nchar(ipa1), nchar(ipa2)),
    lv = stringsim(ipa1, ipa2, method = "lv")
  )


# trials ----
stimuli <- map(
  c("ENG-SPA" = "English-Spanish", "ENG-CAT" = "English-Catalan", "SPA-CAT" = "Spanish-Catalan"),
  function(x) read_xlsx(here("Stimuli", "trials.xlsx"), sheet = x)
) %>% 
  bind_rows(.id = "group") %>% 
  clean_names() %>% 
  left_join(clearpond) %>%
  left_join(lv) %>% 
  left_join(trace) %>% 
  mutate(frequency_zipf = log10(frequency)+3) %>% 
  select(trial_id, group, word1, word2, phon_trace, frequency, frequency_zipf, pthn, lv,
         consonant_ratio, vowel_ratio, onset, overlap_stress)
  

# export ----
saveRDS(stimuli, here("Data", "stimuli.rds"))


