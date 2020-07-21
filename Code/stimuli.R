#### 00_stimuli-amplitude: analyse audio amplitude

#### set up ######################################

# load packages
library(dplyr)
library(tidyr)
library(data.table)
library(purrr)
library(stringr)
library(readxl)
library(tibble)
library(ggplot2)
library(ggridges)
library(gghighlight)
library(patchwork)
library(wesanderson)
library(janitor)
library(audio)
library(PraatR)
library(here)

# load/create functions
source(here("R", "functions.R"))

# set parameters
time_bin_duration <- 0.001
# time-step (s), 
formant_arguments <- list(0.001,  5, 5500, time_bin_duration, 50)
# include frame number, include time, time decimals, include intensity, intensity decimals, include n formants, freq decimals, include bandwidths
table_arguments <- list(TRUE, TRUE, 3, TRUE, 5, FALSE, 3, TRUE) 
# time step (s), pitch floor, pitch ceiling
pitch_arguments <- list(0.001, 50, 800) 

# set paths
audio_paths         <- list.files(here("Stimuli", "Sounds"), full.names = TRUE)
formant_paths       <- str_replace(audio_paths, "Sounds/", "Formants/") %>% str_replace(., ".wav", ".Formant")
formant_table_paths <- str_replace(audio_paths, "Sounds/", "/Formants/Tables/") %>% str_replace(., ".wav", "_table.txt")
pitch_path          <- str_replace(audio_paths, "Sounds/", "Pitch/") %>% str_replace(., ".wav", ".Pitch")
pitch_tier_path     <- str_replace(audio_paths, "Sounds/", "Pitch/PitchTiers/") %>% str_replace(., ".wav", ".PitchTier")

#### import data #################################
trials <- read_xlsx(here("Stimuli", "trials.xlsx")) %>% select(-translation_english_phonology)

#### analyse formats #############################
formants <- extract_formants(file = here("Stimuli", "Sounds")) %>%
  mutate(soundfile = paste0("Sounds/", file, ".wav")) %>%
  left_join(trials, formants, by = "soundfile") %>%
  select(trial_id, word, orthography, phonology, time, intensity, f1, f2, language, practice, soundfile)

formants_mean <- formants %>%
  group_by(trial_id, word, language, practice) %>%
  summarise(duration = max(time, na.rm = TRUE),
            mean_f1 = mean(f1, na.rm = TRUE),
            mean_f2 = mean(f2, na.rm = TRUE)) %>%
  ungroup() %>%
  right_join(trials)

formants_summary <- formants_mean %>%
  group_by(language) %>%
  summarise(duration = max(duration, na.rm = TRUE),
            f1 = mean(mean_f1, na.rm = TRUE),
            f2 = mean(mean_f2, na.rm = TRUE),
            sd_f1 = sd(mean_f1, na.rm = TRUE),
            sd_f2 = sd(mean_f2, na.rm = TRUE),
            min_f1 = min(mean_f1, na.rm = TRUE),
            min_f2 = min(mean_f2, na.rm = TRUE),
            max_f1 = max(mean_f1, na.rm = TRUE),
            max_f2 = max(mean_f2, na.rm = TRUE)) %>%
  ungroup()

# analyse amplitude
amplitude <- formants %>%
    mutate(intensity = -intensity) %>%
    bind_rows(praat_data)

amplitude_means <- amplitude %>%
  filter(intensity > 0) %>%
  group_by(trial_id, word, language) %>%
  summarise(intensity = mean(intensity, na.rm = TRUE))
              
#### analyse F0/pitch ############################

pitch <- extract_pitch(file = here("Stimuli", "Sounds")) %>%
  mutate(soundfile = paste0("Sounds/", file, ".wav")) %>%
  as_tibble() %>%
  right_join(trials, by = "soundfile") %>%
  select(trial_id, word, time, f0, language, practice, soundfile)
  
pitch_mean <- pitch %>%
  group_by(word, trial_id, language, soundfile) %>%
  summarise(f0 = mean(f0, na.rm = TRUE))

 #### merge data #################################
merged <- trials %>%
  left_join(formants_mean) %>%
  left_join(amplitude_means) %>%
  left_join(pitch_mean)

#### visualise data ##############################
# frequency
plot_frequency <- ggplot(merged, aes(frequency_zipf, language, fill = language, colour = language)) +
  stat_density_ridges(alpha = 0.5,
                      jittered_points = TRUE,
                      position = position_points_jitter(width = 0.05, height = 0),
                      point_shape = "|",
                      point_size = 2,
                      point_alpha = 0.5,
                      quantile_lines = TRUE,
                      quantiles = c(0.5)) +
  labs(x = "SUBTLEX frequency (Zipf score)", y = "Language",
       colour = "Language", fill = "Language", title = "Frequency") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom

# duration
plot_duration <- ggplot(merged, aes(x = language, y = duration, fill = language)) +
  geom_violin(size = 1, alpha = 0.5, colour = "transparent") +
  geom_boxplot(width = 0.1, size = 0.6, fill = "white", colour = "black") +
  geom_point(size = 1, position = position_jitter(width = 0.1), colour = "black", alpha = 0.1) +
  labs(x = "Language", y = "Duration (s)", fill = "Language",
       title = "Duration") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom

# formants
plot_formants <- ggplot(merged, aes(colour = language, shape = language)) +
  geom_point(aes(x = mean_f2, y = mean_f1), size = 2, alpha = 0.5) +
  geom_errorbar(data = formants_summary, aes(x = f2, ymin = f1-sd_f1, ymax = f1+sd_f1), size = 1) +
  geom_errorbarh(data = formants_summary, aes(y = f1, xmin = f2-sd_f2, xmax = f2+sd_f2), size = 1) +
  geom_point(data = formants_summary, aes(f2, f1), size = 4) +
  labs(x = "F2 (Hz)", y = "F1 (Hz)", colour = "Language", shape = "Language",
       title = "Formants") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  scale_x_continuous(trans = "reverse") +
  scale_y_continuous(trans = "reverse") +
  theme_custom

praat_data %>%
  pivot_longer(c(f1, f2), names_to = "formant", values_to = "frequency") %>%
  split(.$soundfile) %>%
  map(~ggplot(data = ., aes(x = time, y = frequency, colour = formant)) +
        geom_line(alpha = 0.5) +
        geom_smooth(aes(linetype = formant)) +
        labs(x = "Time (s)", y = "Frequency (Hz)",
             colour = "Formant", fill = "Formant", linetype = "Formant",
             title = str_to_upper(distinct(., orthography)),
             subtitle = paste0("Language: ", distinct(., language),
                               " / Phonology (IPA): ", distinct(., phonology))) +
        scale_color_brewer(palette = "Set1") +
        scale_fill_brewer(palette = "Set1") +
        theme_custom +
        ggsave(here("Figures",
                    paste0(
                      str_replace(unique(.$soundfile), ".wav", ".png") %>% str_replace(., "Sounds", "Formants"))),
               width = 6, height = 5)
  )

# amplitude/intensity
amplitude %>%
    split(.$soundfile) %>%
    map(~ggplot(., aes(time, intensity)) +
            geom_line() +
            labs(x = "Time", y = "Intensity (dB)",
                 title = str_to_upper(distinct(., orthography)),
                 subtitle = paste0("Language: ", distinct(., language),
                                   " / Phonology (IPA): ", distinct(., phonology))) +
            theme(panel.background = element_rect(fill = "transparent"),
                  panel.border = element_rect(fill = "transparent", colour = "black"),
                  panel.grid = element_blank(),
                  text = element_text(size = 12),
                  axis.text = element_text(colour = "black"),
                  legend.position = c(0.1, 0.9),
                  legend.direction = "horizontal") +
            ggsave(here("Figures",
                        paste0(
                            str_replace(unique(.$soundfile), ".wav", ".png") %>% str_replace(., "Sounds", "Amplitude"))),
                   width = 6, height = 5)
    )

plot_amplitude <- ggplot(merged, aes(x = language, y = intensity, fill = language)) +
  geom_violin(size = 1, alpha = 0.5, colour = "transparent") +
  geom_boxplot(width = 0.1, size = 0.6, fill = "white", colour = "black", outlier.colour = "transparent") +
  geom_point(size = 1, position = position_jitter(width = 0.1), colour = "black", alpha = 0.1) +
  labs(x = "Language", y = "Intensity (dB)", fill = "Language",
       title = "Mean intensity") +
  scale_fill_brewer(palette = "Set1") + 
  scale_y_continuous(labels = function(x) round(x, 20)) +
  theme_custom

# pitch
plot_pitch <- ggplot(pitch, aes(x = time, y = f0, colour = language, fill = language)) +
  geom_line(aes(group = trial_id), alpha = 0.15, size = 0.5) +
  geom_smooth(method = "gam", formula = "y ~ s(x, bs = 'cs')") +
  labs(x = "Time (s)", y = "F0/Pitch (Hz)", colour = "Language", fill = "Language",
       title = "Pitch across time") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom

# similarity
plot_similarity <- merged %>%
  pivot_longer(cols = c(lev_engspa, sim_engspa, lev_spacat, sim_engcat, lev_engcat, sim_spacat, lev_spacat),
               names_to = c("measure", "language_pair"), values_to = "score",names_sep = "_") %>%
  mutate(measure = ifelse(measure == "lev", "Distance", "Similarity"),
         language_pair = case_when(language_pair=="engspa" ~ "English-Spanish",
                                   language_pair=="engcat" ~ "English-Catalan",
                                   language_pair=="spacat" ~ "Spanish-Catalan")) %>%
  ggplot(aes(x = score, y = language_pair, fill = language, colour = language)) +
  facet_wrap(~measure) +
  stat_density_ridges(alpha = 0.5,
                      jittered_points = TRUE,
                      position = position_points_jitter(width = 0.05, height = 0),
                      point_shape = "|",
                      point_size = 2,
                      point_alpha = 0.5,
                      quantile_lines = TRUE,
                      quantiles = c(0.5)) +
  labs(x = "Similarity score", y = "Language pair",
       colour = "Measure", fill = "Measure",
       title = "Phonological overlap across translation equivalents") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom +
  theme(axis.title.y = element_blank())

# plot diff
dat_diff <- merged %>%
    mutate(diff_engcat = sim_engcat-lev_engcat,
           diff_engspa = sim_engspa-lev_engspa,
           diff_spacat = sim_spacat-lev_spacat) %>%
    pivot_longer(cols = c(lev_engspa, sim_engspa, lev_spacat, sim_engcat, lev_engcat, sim_engcat),
                 names_to = c("measure", "language_pair"), values_to = "score", names_sep = "_") %>%
    select(trial_id, measure, language_pair, score, diff_engspa, diff_engcat, diff_spacat) %>%
    pivot_longer(starts_with("diff_"), names_to = "language_pair1", values_to = "diff") %>%
    mutate(language_pair1 = str_remove(language_pair1, "diff_"),
           language_pair1 = language_pair==language_pair1) %>%
    filter(language_pair1) %>%
    mutate(measure = case_when(measure=="lev" ~ "L",
                               measure=="sim" ~ "S"),
           language_pair = case_when(language_pair=="engspa" ~ "English-Spanish",
                                     language_pair=="engcat" ~ "English-Catalan",
                                     language_pair=="spacat" ~ "Spanish-Catalan"),
           diff_abs = abs(diff)) %>%
    filter(language_pair != "Spanish-Catalan")

plot_diff <- ggplot(dat_diff, aes(measure, y = score, colour = diff)) +
  geom_violin(alpha = 0.5, colour = NA, width = 0.2, fill = "black") +
  geom_line(aes(group = trial_id), alpha = 0.4, size = 0.75) +
  geom_boxplot(fill = "white", colour = "black", width = 0.05) +
  labs(x = "Measure", y = "Score", colour = "Difference") +
  scale_colour_gradientn(colours = wes_palette("Zissou1")) +
  scale_fill_brewer(palette = "Set1") +
  theme_custom +
  theme(legend.position = c(0.1, 0.7)) +
  ggsave(here("twitter.png"), height = 5, width = 6)
  
  ggplot(dat_diff, aes(measure, y = score, colour = diff)) +
  facet_wrap(~language_pair, ncol = 1) +
  geom_violin(alpha = 0.5, colour = NA, width = 0.2, fill = "black") +
  geom_line(aes(group = trial_id, alpha = diff_abs)) +
  geom_boxplot(fill = "white", colour = "black", width = 0.05) +
  labs(x = "Measure", y = "Score", colour = "Difference") +
  scale_colour_gradientn(colours = wes_palette("Zissou1")) +
  scale_fill_brewer(palette = "Set1") +
  theme_custom +
  theme(legend.position = "none") +
  
  plot_layout(ncol = 2) +
  ggsave(here("Figures", "04_diff.png"), height = 6)

# arrange plots
plot_frequency + plot_duration + plot_diff + plot_amplitude + plot_pitch +
  plot_layout(guides = "collect") +
  ggsave(here("Figures", "00_stimuli.png"), width = 9, height = 5)
  
