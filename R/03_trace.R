# jtrace analyses

# set up ----
library(tidyverse)
library(jtracer)
library(readxl) # for importing Excel spreadsheets
library(patchwork) # for arranging plots
library(stringdist) # for Levenshtein distance
library(brms) # for fitting Bayesian models
library(tidybayes) # for manipulating MCMC draws
library(tidytext) # for reordering levels in ggplot2
library(janitor) # for cleaning column names
library(here) # for locating files

# set parameters
set.seed(888) # for reproducibility
source(here("R", "utils.R")) # custom functions

#### import data ----
# import trials
trials <- readRDS(here("Data", "stimuli.rds")) %>% 
    mutate(
        test_language = ifelse(group=="ENG-SPA", "Spanish", "Catalan"),
        zipf = log10(frequency)+3,
        pthn_log = log(pthn),
        overlap_stress = ifelse(overlap_stress==1, "Same", "Different"),
        jtrace = ipa
    )
# import participant responses
responses <- readRDS(here("Data", "responses.rds"))

# by Serene (some fixes by Gonzalo) ----

# TRACE simulations ----

# import TRACE simulations
filedir <- here("Data", "jtrace")
## 1 file per input word, with 1 output word per column
## files should be named with input word orthography and language (e.g. "gato_spanish.xlsx")
## files should be xlsx (csv doesn't deal well with special characters like ^ and @)
## folder should not contain any other files

# Note: it's effortful to have to convert to xlsx (jTRACE doesn't allow direct xlsx export), but it's the most reliable method to preserve special characters I've found so far. Would welcome ideas

# Export jTRACE output with Top 100 items and 100 cycles (arbitrary value)
# Max ad-hoc activation

fnames <- dir(filedir) # extract list of file names in directory
trace_output <- data.frame() # create empty data frame
# for loop to extract highest activations for each input word
for (i in 1:length(fnames)){
    filename <- paste(filedir, fnames[i], sep = "/") # get file name
    temp <- read_excel(filename) # read file
    
    temp <- apply(temp,2,max) # get highest value in each column
    temp <- as.data.frame(temp)
    temp <- cbind(newColName = rownames(temp), temp) # change index column (which has output items) into column 1 for easier organisation
    rownames(temp) <- 1:nrow(temp)
    names(temp)[1] <- "trace_eng" # (rename col) output item
    names(temp)[2] <- "trace_activation" # (rename col) max activation value
    
    temp <- temp %>%
        filter(!trace_eng=="cycle") %>% # remove row corresponding to cycle number
        mutate(input = fnames[i], # specify input word
               trace_activation = as.numeric(trace_activation)) %>% 
        arrange(desc(trace_activation)) %>%
        filter(!trace_activation <= 0) # remove low activation (maybe even apply a higher threshold? TBD)
    
    trace_output <- bind_rows(trace_output, temp)
}

trace_output <- trace_output %>%
    mutate(input = str_remove(input, ".xlsx")) %>%
    separate(input, c("input", "language"), "_") %>%
    as_tibble()

# TRACE lexicon
# xlsx file with 1 column for TRACE transcriptions and 1 column for orthography (English words) 
df_lexicon <- read_excel(here("Data", "trace_transcription.xlsx"), sheet = "lexicon") %>%
    select(trace_eng, ort_eng) %>%
    unique()

# match the jTRACE output transcriptions with their orthography
trace_output_phon <- left_join(trace_output, df_lexicon, by = c("trace_eng")) %>%
    rename(output_word = ort_eng)

# TRACE input
df_trial_phon <- read_excel(here("Data", "trace_transcription.xlsx"), sheet = "trials") %>%
    select(ort_presented, trace_presented, language) %>%
    mutate(language = tolower(language)) %>%
    unique()

trace_output_phon <- left_join(trace_output_phon, df_trial_phon, by = c("input" = "ort_presented", "language"))

# add lexical frequencies
df_clearpond <- read_excel(here("Data", "trace_transcription.xlsx"), sheet = "clearpond") %>%
    select(Word, Freq_per_million, PTHN) %>%
    clean_names() %>%
    rename(frequency = freq_per_million) %>%
    unique() %>%
    mutate(word = tolower(word))

# merge TRACE data
trace_output_stats <- left_join(
    trace_output_phon, df_clearpond,
    by = c("output_word" = "word")
) %>%
    mutate(
        n_char = ifelse(
            nchar(trace_eng) > nchar(trace_presented),
            nchar(trace_eng),
            nchar(trace_presented)),
        lv = stringsim(trace_eng, trace_presented, method = "lv")
    )

responses <- trace_output_stats %>% 
    # transform relative frequency to Zipf score
    mutate(frequency_zipf = relative_to_zipf(frequency)) %>% 
    # center predictors
    mutate_at(
        vars(lv, pthn, frequency),
        function(x) scale(x, center = TRUE, scale = TRUE)[,1]) %>% 
    complete() %>% 
    as_tibble() %>% 
    drop_na(lv, pthn, frequency_zipf)


# fit models ----
# formula
f_0 <- bf(trace_activation ~ 1 + frequency + (1 | input), family = exponential())
f_1 <- bf(trace_activation ~ 1 + frequency + pthn + (1 | input), family = exponential())
f_2 <- bf(trace_activation ~ 1 + frequency + pthn*lv + (1 | input), family = exponential())

# Note: these models are not predicting the correct answer,
# but instead predicting the activation value each output
# item will receive for a given input word.

# prior
priors <- c(
    prior(normal(0, 3), class = "Intercept"),
    prior(normal(0, 3), clas = "b"),
    prior(cauchy(0, 3), class= "sd")
)

# fit models
fit_0 <- brm(f_0, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_jtrace_0.rds"))
fit_1 <- brm(f_1, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_jtrace_1.rds"))
fit_2 <- brm(f_2, data = responses, prior = priors, backend = "cmdstanr",
             file = here("Results", "fit_jtrace_2.rds"))

# model comparison
loos <- list(fit_0 = loo(fit_0), fit_1 = loo(fit_1), fit_2 = loo(fit_2))
loos_comp <- loo_compare(loos$fit_0, loos$fit_1, loos$fit_2)
saveRDS(list(loos = loos, comparison = loos_comp), here("Results", "loo_trace.rds"))


# posterior ---
p_fix <- gather_draws(fit_2, `b_.*`, regex = TRUE) # fixed effects posterior
p_ran <- gather_draws(fit_2, r_input[input, param]) # random effects posterior
# export model
saveRDS(list(fit = fit_2, fixed = p_fix, random = p_ran),
        here("Results", "fit_jtrace.rds"))

# marginal effects ----
nd <- expand_grid(
    frequency = 0,
    pthn = seq(
        min(responses$pthn, na.rm = TRUE),
        max(responses$pthn, na.rm = TRUE),
        len = 100
    ),
    lv = c(-1, 1)
)
m <- add_fitted_draws(nd, fit_2, re_formula = NA, n = 50) %>%
    mutate(lv = paste0(lv, " SD"))

ggplot(m, aes(pthn, .value, colour = lv, fill = lv)) +
    stat_lineribbon(alpha = 0.5, colour = NA, size = 0, .width = 0.95) +
    stat_summary(fun = mean, geom = "line", size = 1) +
    labs(x = "Phon. neigh. density.", y = "Max. TRACE activation",
         colour = "Phon. similarity", fill = "Phon. similarity") +
    theme_custom() +
    theme(legend.position = "top")


# TRACE vs. participant responses ----
translation_task <- read.csv(here("Data", "translation_engdata_cleaned.csv")) %>%
    mutate(test_language = tolower(test_language))

# count the number of participants who gave each answer in response to a given trial
df_answer <- translation_task %>%
    group_by(test_language, word, answer) %>%
    summarise(n_participant = n(), .groups = "drop") %>%
    group_by(test_language, word) %>%
    mutate(pct_participant = n_participant/sum(n_participant)*100) #%>%
#  filter(!n_participant == 1) # remove answers only given by 1 participant as idiosyncratic answers?

df_match <- full_join(trace_output_stats, df_answer, by = c("input" = "word", "output_word" = "answer", "language" = "test_language")) %>%
    semi_join(., trace_output, by = c("input", "language"))

# answers
# presented words and the answer that was given by the most number of
# participants for that trial")

# If "trace_activation" is <NA>, the word is not in the currently-used jTRACE lexicon
df_match %>%
    filter(language=="spanish") %>% 
    arrange(input, desc(pct_participant)) %>%
    group_by(input) %>%
    slice(1) %>%
    select(input, output_word, pct_participant, trace_activation) %>%
    arrange(desc(pct_participant))

df_match %>%
    filter(language == "catalan") %>% 
    arrange(input, desc(pct_participant)) %>%
    group_by(input) %>%
    slice(1) %>%
    select(input, output_word, pct_participant, trace_activation) %>%
    arrange(desc(pct_participant)) %>% 
    # replace NAs with 0s
    replace_na(list(pct_participant = 0, trace_activation = 0))

# However, this is also constrained by the size of TRACE's lexicon, so subset only the words that do appear in the lexicon
df_match_trace <- semi_join(df_match, df_lexicon, by = c("output_word" = "ort_eng"))


# plot
ggplot(df_match_trace, aes(x = trace_activation, y = pct_participant)) +
    geom_smooth() +
    geom_point(shape = 1, size = 2, alpha = 0.5, stroke = 1) +
    labs(x = "TRACE activation", y = "Answered by participants") +
    labs("jTRACE activation against % participants who gave word as response") +
    
# correlation test
cor.test(df_match_trace$trace_activation, df_match_trace$pct_participant)


# plot by word
ggplot(df_match_trace, aes(x = trace_activation, y = pct_participant)) +
    geom_smooth() +
    geom_point() +
    xlab("jTRACE activation value for the word") +
    ylab("% participants who responded with the word") +
    ggtitle("jTRACE activation against % participants who gave word as response") +
    facet_wrap(language~input)



# by Gonzalo ----

# fit model

# experimental trials ----
trials <- readRDS(here("Data", "stimuli.rds")) %>% 
    as_tibble() %>% 
    select(group, input = word1, target = word2, phon_trace)

# process TRACE data ----
trace <- map(
    list.files(here("Data", "jtrace"), full.names = TRUE),
    function(x){
        read_xlsx(x) %>% 
            pivot_longer(-cycle, names_to = "response", values_to = "activation")
    }
) %>%
    set_names(list.files(here("Data", "jtrace"))) %>% 
    bind_rows(.id = "target") %>% 
    separate(target, c("input", "language"), sep = "_") %>% 
    mutate(language = str_remove(language, ".xlsx"),
           language = str_to_sentence(language))

# get top candidates
trace_top <- trace %>% 
    group_by(input, language, response) %>% 
    summarise(
        activation = max(activation, na.rm = TRUE),
        .groups = "drop"
    ) %>% 
    group_by(input, language) %>% 
    slice_max(activation, n = 10) %>% 
    ungroup() %>% 
    mutate(group = ifelse(language=="Catalan", "ENG-CAT", "ENG-SPA")) %>% 
    select(-language) %>% 
    # add experimental trials
    left_join(trials) %>% 
    mutate(correct = response==phon_trace) %>% 
    select(group, input, response, activation, correct)

# experimental results ----
responses <- read.csv(here("Data", "translation_engdata_cleaned.csv")) %>%
    mutate(test_language = str_to_sentence(test_language),
           correct = CorrectAnswer=="yes",
           group = ifelse(test_language=="Catalan", "ENG-CAT", "ENG-SPA")) %>% 
    as_tibble() %>% 
    select(participant, group, test_language, trial_id, word, answer, correct) %>% 
    rename(response = answer, input = word) %>% 
    count(group, input, response, correct) %>% 
    group_by(group, input) %>%
    mutate(total = sum(n),
           activation = n/total) %>% 
    group_by(group, input) %>% 
    slice_max(activation, n = 10) %>% 
    ungroup() %>% 
    select(group, input, response, correct, activation) %>% 
    filter(input %in% trace_top$input)

# merge everything and show example
transcriptions <- read_xlsx(
    here("Data", "trace_transcription.xlsx"),
    sheet = "lexicon") %>% 
    mutate(source = "TRACE", group = "ENG-CAT")
merged <- list(TRACE = trace_top, Participants = responses) %>% 
    bind_rows(.id = "source") %>% 
    left_join(transcriptions, by = c("response" = "trace_eng", "source", "group")) %>% 
    mutate(
        response = ifelse(is.na(ort_eng), response, ort_eng),
        # to reorder variable within panels
        input_label = paste0(input, " (", group, ")"),
        response_reordered = reorder_within(response, activation, input_label)
    )


merged %>% 
    filter(input=="bol", group=="ENG-CAT") %>% 
    mutate(correct = ifelse(correct, "Correct", "Incorrect")) %>% 
    ggplot(aes(response_reordered, activation, fill = correct)) +
    facet_wrap(~source, scales = "free_y", ncol = 2) +
    geom_col(colour = "white") +
    labs(x = "Top candidates", y = "Responses / TRACE activation", colour= "Correct?",
         subtitle = "Input: Catalan word BOL /bol/\nCorrect response is BOWL /bəʊɫ/") +
    coord_flip() +
    scale_x_reordered() +
    scale_y_continuous(limits = c(0, 1), labels = scales::percent) +
    scale_fill_manual(values = wesanderson::wes_palettes$Darjeeling1) +
    theme_custom() +
    theme(
        legend.position = "top",
        legend.title = element_blank(),
        panel.grid.major.x = element_line(colour = "grey", linetype = "dotted")
    ) +
    ggsave(here("Figures", "trace_example_bowl.png"))


