
# For compiling the different statistics for Translation Elicitation

library(readxl)
library(dplyr)
library(here)

trials <- read_excel(here("Data", "trials.xlsx")) # trial list

# Frequency and phonological neighbourhoods for English (from CLEARPOND)
clearpond <- read.csv(here("Data", "clearpond_Eng.csv") )

# Word pair comparison statistics - similarity, same_onset, consecutive_longest, close_substitutions
# Statistics for each language pair are different columns
# Only includes statistics for words that appear in trials for the specific language
similarity_engspa <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "English-Spanish") %>%
  select(-c("Phon_eng", "Phon_spa", "check_diff")) 
similarity_engcat <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "English-Catalan") %>%
  select(-c("Phon_eng", "Phon_cat", "check_diff"))
similarity_spacat <- read_excel(here("Data", "Output_similarity.xlsx"), sheet = "Spanish-Catalan") %>%
  select(-c("Phon_cat", "Phon_spa", "check_diff"))

# replace name to match up to trial list - similarity is calculated for pork
similarity_engcat$Word_eng[similarity_engcat$Word_eng=="pork"]<-"pig/pork"


trials <- left_join(trials, clearpond, by = c("translation_english_orthography" = "Word_eng"))
trials <- left_join(trials, similarity_engspa, by = c("translation_english_orthography" = "Word_eng", "translation_spanish_orthography" = "Word_spa"))
trials <- left_join(trials, similarity_engcat, by = c("translation_english_orthography" = "Word_eng", "translation_catalan_orthography" = "Word_cat"))
trials <- left_join(trials, similarity_spacat, by = c("translation_spanish_orthography" = "Word_spa", "translation_catalan_orthography" = "Word_cat"))

write.table(trials, here("Data", "trial_stats.csv"), sep = ",", dec = ".", row.names = FALSE)
