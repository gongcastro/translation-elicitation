library(tidyverse)
library(dplyr)
library(purrr)
library(ggplot2)
library(readxl)

############# READ DATA

filedir <- setwd('C:/Users/ss122/Desktop/Levenshtein/TranslationElicitation/data') # set working directory as folder containing output files
fnames <- dir(filedir) # retrieve file names
csv <- lapply(fnames, read.csv) # read csv files (reads into list format)
TE <- bind_rows(csv, .id = "column_label") # bind into one data frame

# https://stackoverflow.com/questions/46518781/reading-multiple-csv-files-as-data-frames-in-r
# https://stackoverflow.com/questions/2851327/convert-a-list-of-data-frames-into-one-data-frame

# Split data into practice trials and experimental trials 
#TE_practice <- subset(TE, TE$practice_trials.thisIndex >= 0) # practice trials
TE_experiment <- subset(TE, is.na(TE$practice_trials.thisIndex)) # experimental trials


############# TIDY DATASET TO RELEVANT COLUMN AND ROWS

# Filter only final answers (remove intermittent key presses)
TE_answer <- TE_experiment %>%
  filter(!is.na(trial_id)) %>% # remove rows not associated with experimental trials
  filter(!inputText == "") %>% # remove blank rows (no input text data)
  # select only variables of interest (task-relevant)
  select(participant, test_language, trial_id, word, inputText) %>% 
  group_by(participant, trial_id, word) %>%
  slice(n()) %>% # selects only final row in grouping variable (each participant's final answer)
  ungroup() %>%
  rename(answer = inputText)


# Attach list of correct answers to trials
trials <- read_excel("C:/Users/ss122/Desktop/Levenshtein/TranslationElicitation/trials.xlsx")
trials <- trials %>%
  select(trial_id, translation_english_orthography, language, 
         levenshtein_engspa, levenshtein_engcat, similarity_engspa, similarity_engcat) %>%
  rename(correct = translation_english_orthography)

TE_answer <- inner_join(TE_answer, trials, by = c("trial_id", c("test_language" = "language")))

#For options that have multiple translations, combine
TE_answer$answer[TE_answer$answer=="pig"]<-"pig/pork"
TE_answer$answer[TE_answer$answer=="pork"]<-"pig/pork"


############# FILTER PARTICIPANTS  (temporarily ignore for pilot sample)
# Demographics screening (language background)
#TE_participant <- TE %>%
  # select only variables of interest (demographics)
#  select(participant, language_native_key.keys, language_home_key.keys, 
#         language_prof_oral_spanish_key.keys, language_prof_oral_catalan_key.keys,
#         language_prof_written_spanish_key.keys, language_prof_written_catalan_key.keys)  %>%
#  filter(!is.na(language_prof_oral_spanish_key.keys))  #%>%
#  filter(language_native_key.keys == "e")  %>% # Native language must be English
#  filter(language_home_key.keys == "e")  %>% # Home language must be English
#  filter(language_prof_oral_spanish_key.keys <= 2)  %>% # Spanish proficiency must be low or not speak
#  filter(language_prof_written_spanish_key.keys <= 2)  %>%
#  filter(language_prof_oral_catalan_key.keys <= 2)  %>% # Catalan proficiency must be low or not speak
#  filter(language_prof_written_catalan_key.keys <= 2) 

# Age criteria - 18 to 40 years old
#TE_participant_age <- TE %>%
# select(participant, age) %>% 
#  filter(age >= 18) %>%
#  filter(age <= 40)

# List of participants fulfilling both language and age inclusion criteria
#TE_participant <- semi_join(TE_participant, TE_participant_age, by = "participant")

# Check - are participants answering in English?
# Database of English words, Source: https://github.com/dwyl/english-words
Englishdict <- read.delim("C:/Users/ss122/Desktop/Levenshtein/TranslationElicitation/words_alpha.txt")
TE_non_English <- anti_join(TE_answer, Englishdict, by = c("answer" = "a")) 
problem_participant <- TE_non_English %>%
  group_by(participant) %>%
  tally() %>% # count how many of each participant's answers are not in English
  filter(n > 30) # Identify participants who don't answer in English / make large numbers of typing mistakes
# exclude participant with many problematic answers
#TE_participant <- anti_join(TE_participant, problem_participant, by = "participant")


# Filter data by all the participant exclusion criteria
#TE_cleaned <- semi_join(TE_answer, TE_participant, by = "participant")
TE_cleaned <- anti_join(TE_answer, problem_participant, by = "participant")
TE_cleaned$participant <- as.factor(TE_cleaned$participant)

#write.csv(TE_cleaned, "cleaned_translationelicitation.csv")


# Final number of participants
N <- nlevels(TE_cleaned$participant) # total

N_language <- TE_cleaned %>%
  select(test_language, participant) %>%
  unique() %>%
  group_by(test_language) %>%
  tally() # number who answered each language version

N_Spa <- N_language$n[N_language$test_language == "Spanish"] # answered Spanish version
N_Cat <- N_language$n[N_language$test_language == "Catalan"] # answered Catalan version



########### IDENTIFYING CORRECT ANSWERS USING DAMERAU LEVENSHTEIN

# is there any reason to use python version, or will R do perfectly well?
library(stringdist)

# Use Damerau Levenshtein to compare participant answers to target translation
TE_cleaned$Damerau <- stringdist(TE_cleaned$answer, TE_cleaned$correct, method="dl")
TE_cleaned$CorrectAnswer <- ifelse(TE_cleaned$Damerau == 0, "yes", "no")
# Damerau Levenshtein allows wriggle room for typos (max 1 edit operation - insertion, deletion, substitution, transposition)
# But also has issues
# Tricky to deal with - a single letter change can be a typo or different word (bowl-owl, scissor-scissors)

# check if accepted words are really typos or a different word
TE_typos <- TE_cleaned %>%
  filter(Damerau > 0 & Damerau <= 1)
TE_typos <- semi_join(TE_typos, Englishdict, by = c("answer" = "a"))


# Calculate percentage correct
TE_correct_Spa <- TE_cleaned %>%
  filter(test_language == "Spanish") %>%
  rename(levenshtein = levenshtein_engspa, similarity = similarity_engspa) %>%
  group_by(trial_id, test_language, word, correct, levenshtein, similarity) %>%
  tally(CorrectAnswer == "yes") %>%
  mutate(Total = N_Spa) %>%
  mutate(PercentageCorrect = n/Total)

TE_correct_Cat <- TE_cleaned %>%
  filter(test_language == "Catalan") %>%
  rename(levenshtein = levenshtein_engcat, similarity = similarity_engcat) %>%
  group_by(trial_id, test_language, word, correct, levenshtein, similarity) %>%
  tally(CorrectAnswer == "yes") %>%
  mutate(Total = N_Cat) %>%
  mutate(PercentageCorrect = n/Total)

TE_summary <- rbind(TE_correct_Spa, TE_correct_Cat)


####### PLOTS 
hist(TE_summary$PercentageCorrect)


fontsize    = 14
# arguments for stat_smooth function
sconflevel  = 0.95
sformula    = "y ~ x"
smethod     = "loess"
# settings for the plots
pdpi        = 200
pwdt        = 8
phgt        = 4
plot_theme  = theme(plot.title       = element_text(hjust = 0.5, size= fontsize),
                    text             = element_text(size=fontsize), # set text size for all text in the plot
                    axis.line        = element_line(size = 0.5, colour = "grey40"), # set axis line attributes
                    axis.text        = element_text(size = fontsize),
                    legend.position  = c(0.15, 0.9), # set legend position relative to x and y axis (normalized units)
                    legend.direction = "horizontal",
                    panel.background = element_rect(fill = "white", colour = "white")) # set panel background and box colour
                      

# Plot the behavioural response against Levenshtein output

ggplot(data = TE_summary, mapping = aes(x = levenshtein, y = PercentageCorrect)) +
  geom_point() +
  # https://ggplot2.tidyverse.org/reference/geom_smooth.html
  stat_smooth(formula = sformula,  # formula for the smooth line (default y ~ x)
              method  = smethod,   # method to use for the smooth line  (default loess)
              se      = TRUE,      # show confidence interval bars around linear fit (default TRUE)
              level   = sconflevel # level for the confidence interval (default 0.95)
  ) +
  labs (title="Translation Elicitation Task", x="Levenshtein Score", y="Percentage of correct answers") +
  # https://ggplot2.tidyverse.org/reference/theme.html
  plot_theme
#ggsave(paste(pfolder, 'levenshtein_plot.png', sep=''), dpi=pdpi, width=pwdt, height=phgt)


# Plot the behavioural response against Levenshtein output

ggplot(data = TE_summary, mapping = aes(x = similarity, y = PercentageCorrect)) +
  geom_point() +
  stat_smooth(formula = sformula,  # formula for the smooth line (default y ~ x)
              method  = smethod,   # method to use for the smooth line  (default loess)
              se      = TRUE,      # show confidence interval bars around linear fit (default TRUE)
              level   = sconflevel # level for the confidence interval (default 0.95)
  ) +
  labs (title="Translation Elicitation Task", x="Similarity Score", y="Percentage of correct answers") +
  plot_theme
#ggsave(paste(pfolder, 'levenshtein_plot.png', sep=''), dpi=pdpi, width=pwdt, height=phgt)


# Kolmogorov-Smirnov Test for similarity
# https://towardsdatascience.com/when-to-use-the-kolmogorov-smirnov-test-dd0b2c8a8f61
#ks.test(TE_summary$PercentageCorrect, TE_summary$levenshtein)



######### FALSE FRIENDS

# Identify answers given by multiple participants
TE_incorrect_Spa <- TE_cleaned %>%
  filter(test_language == "Spanish") %>%
  rename(levenshtein_correct = levenshtein_engspa, similarity_correct = similarity_engspa) %>%
  group_by(trial_id, test_language, word, correct, answer, levenshtein_correct, similarity_correct) %>%
  tally() %>%
  filter(n > 0) %>%
  mutate(Total = N_Spa) %>% # total number of participants
  mutate(PercentageAnswered = n/Total)

TE_incorrect_Cat <- TE_cleaned %>%
  filter(test_language == "Catalan") %>%
  rename(levenshtein_correct = levenshtein_engspa, similarity_correct = similarity_engspa) %>%
  group_by(trial_id, test_language, word, correct, answer, levenshtein_correct, similarity_correct) %>%
  tally() %>%
  filter(n > 0) %>%
  mutate(Total = N_Cat) %>% # total number of participants
  mutate(PercentageAnswered = n/Total)

TE_summary_incorrect <- rbind(TE_incorrect_Spa, TE_incorrect_Cat)

# list of correct answer
correct_answers <- TE_answer %>%
  select(word, correct) %>%
  unique()

# Filter only incorrect answers
TE_summary_incorrect <- anti_join(TE_summary_incorrect, correct_answers, by = c("word", "answer" = "correct"))
# Identify common incorrect answers
TE_summary_incorrect <- subset(TE_summary_incorrect, TE_summary_incorrect$PercentageAnswered > 0.5)


# Are the common answers because of false friends?

### Similarities in certain features in word

# calculate word lengths
TE_summary_incorrect <- TE_summary_incorrect %>%
  group_by(trial_id, test_language, word, answer, levenshtein_correct, similarity_correct) %>%
  modify_if(is.factor, as.character) %>%
  mutate(wordLen = nchar(word)) %>% # calculate word length
  mutate(answerLen = nchar(answer)) # calculate word length

# Do common answers share particular features with presented word?
TE_summary_incorrect <- TE_summary_incorrect %>%
  mutate(word.onset = (strsplit(word, split = "") [[1]])[1]) %>% 
  mutate(answer.onset = (strsplit(answer, split = "") [[1]])[1]) %>%
  mutate(same.onset = ifelse(word.onset == answer.onset, "yes", "no")) %>%# do they have the same onset?
  mutate(word.end = (strsplit(word, split = "") [[1]])[wordLen]) %>% 
  mutate(answer.end = (strsplit(answer, split = "") [[1]])[answerLen]) %>%
  mutate(same.end = ifelse(word.end == answer.end, "yes", "no")) # do they have the same final letter?
# https://stackoverflow.com/questions/28725531/how-to-compare-the-first-letters-of-a-strings-in-r

### Overall string similarity

falsefriends_Lev <- read_excel("C:/Users/ss122/Desktop/Levenshtein/TranslationElicitation/falsefriends.xlsx")
falsefriends_Lev <- falsefriends_Lev %>%
  select(trial_id, test_language, word, answer, correct, levenshtein_answer, similarity_answer)

TE_summary_incorrect <- left_join(TE_summary_incorrect, falsefriends_Lev)

TE_summary_incorrect <- TE_summary_incorrect %>%
  select(trial_id, test_language, word, answer, correct, PercentageAnswered, levenshtein_answer, levenshtein_correct, similarity_answer, similarity_correct, same.onset, same.end)


# Compare levenshtein score of word-correct vs word-answer

TE_summary_incorrect_long <- TE_summary_incorrect %>%
  ungroup() %>%
  select(trial_id, test_language, word, answer, correct, levenshtein_answer, levenshtein_correct) %>%
  gather(key = "type", value = "levenshtein", -c(trial_id, test_language,word,answer,correct))

TE_summary_incorrect_long$type <- factor(TE_summary_incorrect_long$type, levels = c("levenshtein_answer", "levenshtein_correct"), labels = c("Participant Answer", "Correct Answer"))

ggplot(TE_summary_incorrect_long, aes(x = type, y = levenshtein)) +
  labs (title="Levenshtein Distance from Presented Word", x="", y="Levenstein Score") +
  geom_boxplot()


#View(TE_summary_incorrect)
