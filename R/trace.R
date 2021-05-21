# jtrace analyses

# set up ----
library(tidyverse)
library(brms)
library(readxl)
library(tidytext)
library(janitor)
library(patchwork)
library(tidybayes)
library(here)

# set parameters
set.seed(888) # for reproducibility
options(
    mc.cores = 4, chains = 4, iter = 500, seed = 888,
    ggplot2.discrete.fill = wesanderson::wes_palettes$Darjeeling1,
    ggplot2.discrete.colour = wesanderson::wes_palettes$Darjeeling1,
    ggplot2.continuous.fill = wesanderson::wes_palettes$Darjeeling1,
    ggplot2.continuous.colour = wesanderson::wes_palettes$Darjeeling1
)
source("R/utils.R")

# import data ----
trials <- readRDS(here("Data", "trials.rds")) %>% 
    mutate(
        test_language = ifelse(group=="ENG-SPA", "Spanish", "Catalan"),
        zipf = log10(frequency)+3,
        pthn_log = log(pthn),
        overlap_stress = ifelse(overlap_stress==1, "Same", "Different")
    )
responses <- readRDS(here("Data", "responses.rds"))


# by Serene (some fixes by Gonzalo) ----

filedir <- here("Data", "jtrace")
# directory with save files (
## 1 file per input word, with 1 output word per column
## files should be named with input word orthography and language (e.g. "gato_spanish.xlsx")
## files should be xlsx (csv doesn't deal well with special characters like ^ and @)
## folder should not contain any other files

# Note: it's effortful to have to convert to xlsx (jTRACE doesn't allow direct xlsx export), but it's the most reliable method to preserve special characters I've found so far. Would welcome ideas

# Export jTRACE output with Top 100 items and 100 cycles (arbritary value)
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
    names(temp)[1] <- "output" # (rename col) output item
    names(temp)[2] <- "activation" # (rename col) max activation value
    
    temp <- temp %>%
        filter(!output == "cycle") %>% # remove row corresponding to cycle number
        mutate(input = fnames[i]) %>% # specify input word
        arrange(desc(activation)) %>%
        filter(!activation <= 0) # remove low activation (maybe even apply a higher threshold? TBD)
    trace_output <- bind_rows(trace_output, temp)
}

trace_output <- trace_output %>%
    mutate(input = str_remove(input, ".xlsx")) %>%
    separate(input, c("input", "language"), "_")

# xlsx file with 1 column for TRACE transcriptions and 1 column for orthography (English words) 
df_transcription <- read_excel(here("Stimuli", "trace.xlsx")) %>%
    select(trace_eng, ort_eng) %>%
    unique()

# Match the jTRACE output transcriptions with their orthography
trace_output <- left_join(trace_output, df_transcription, by = c("output" = "trace_eng")) %>%
    rename(output_word = ort_eng) %>% 
    mutate(language = str_to_sentence(language))

# Cleaned file with participant answers, 1 row per trial per participant

# count the number of participants who gave each answer in response to a given trial
df_match <- responses %>%
    rename(answer = input_text) %>% 
    group_by(test_language, word, answer) %>%
    summarise(n_participant = n(), .groups = "drop") %>%
    group_by(test_language, word) %>%
    mutate(pct_participant = n_participant/sum(n_participant)) %>%
    #  filter(!n_participant == 1) # remove answers only given by 1 participant as idiosyncratic answers?
    ## Predicting participant responses by jTRACE 
    # Presented words and the answer that was given by the most number of participants for that trial.
    full_join(trace_output, ., by = c("input" = "word", "output_word" = "answer", "language" = "test_language")) %>%
    semi_join(., trace_output, by = c("input", "language")) %>% 
    # replace NAs with 0
    replace_na(replace = list(pct_participant = 0, activation = 0, n_participant = 0)) %>% 
    as_tibble() %>% 
    relocate(input, language, output, output_word, n_participant, pct_participant) %>% 
    arrange(input, -activation) %>% 
    # this is also constrained by the size of TRACE's lexicon, so subset only the words that do appear in the lexicon
    semi_join(df_transcription, by = c("output_word" = "ort_eng")) %>% 
    mutate(group = ifelse(language=="Catalan", "ENG-CAT", "ENG-SPA")) %>% 
    left_join(select(trials, group, input = word1, test_language, vowel_ratio,
                     consonant_ratio, onset, overlap_stress, frequency, pthn))

# save data
saveRDS(df_match, "Data/jtrace.rds")

# fit model ----
# set contrasts
d <- df_match %>% 
    mutate_at(vars(activation, consonant_ratio, vowel_ratio, pthn, frequency),
              function(x) scale(x)[,1]) %>% 
    mutate_at(vars(onset, overlap_stress), as.factor)
contrasts(d$onset) <- c(-0.5, 0.5)
contrasts(d$overlap_stress) <- c(-0.5, 0.5)

f <- bf(pct_participant ~ activation*(consonant_ratio + vowel_ratio + onset + pthn) +
            (1 + activation | input),
        family = zero_one_inflated_beta("logit"))

prior <- c(
    prior(normal(0, 3), class = "Intercept"),
    prior(normal(0, 3), class = "b"),
    prior(cauchy(0, 5), class = "sd"),
    prior(normal(10, 2), class = "phi"),
    prior(beta(5, 5), class = "zoi"),
    prior(beta(5, 5), class = "coi")
)

fit <- brm(formula = f, data = d, prior = prior, backend = "cmdstan")

# posterior ---
p_fix <- gather_draws(fit, `b_.*`, regex = TRUE) # fixed effects posterior
p_ran <- gather_draws(fit, `r_group.*`, regex = TRUE) # random effects posterior

# marginal effects

# export model
saveRDS(list(fit = fit, fixed = p_fix, random = p_ran), "Results/fit_jtrace.rds")



# by Gonzalo ----

# fit model

# experimental trials ----
trials <- readRDS("Data/trials.rds") %>% 
    as_tibble() %>% 
    select(group, input = word1, target = word2, phon_trace)

# process TRACE data ----
trace <- map(
    list.files("Data/jtrace", full.names = TRUE),
    function(x){
        read_xlsx(x) %>% 
            pivot_longer(-cycle, names_to = "response", values_to = "activation")
    }
) %>%
    set_names(list.files("Data/jtrace")) %>% 
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
responses <- readRDS("Data/responses.rds") %>% 
    filter(valid_response, group %in% c("ENG-CAT", "ENG-SPA")) %>% 
    rename(response = input_text, input = word) %>% 
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
merged <- list(TRACE = trace_top, Participants = responses) %>% 
    bind_rows(.id = "source") %>% 
    mutate(
        # to reorder variable within panels
        input_label = paste0(input, " (", group, ")"),
        response_reordered = reorder_within(response, activation, input_label),
    )



merged %>% 
    filter(input=="jaqueta") %>% 
    mutate(correct = ifelse(correct, "Correct", "Incorrect")) %>% 
    ggplot(aes(response_reordered, activation, fill = correct)) +
    facet_wrap(~source, scales = "free_y", ncol = 2) +
    geom_col(colour = "white") +
    labs(x = "Top 10 candidates", y = "Maximum TRACE activation", colour= "Correct?",
         title = "Participants responses and TRACE activated candidates",
         subtitle = "Input: Catalan word JAQUETA /ʒəˈkɛ.tə/\nCorrect response is JACKET (dMaKIt, in TRACE notation)") +
    coord_flip() +
    scale_x_reordered() +
# scale_y_continuous(limits = c(0, 1)) +
theme_custom() +
    theme(
        legend.position = "top",
        legend.title = element_blank(),
        panel.grid.major.x = element_line(colour = "grey", linetype = "dotted")
    ) +
    ggsave("Figures/trace_example_jacket.png")


