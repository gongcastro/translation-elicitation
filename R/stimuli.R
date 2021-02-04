#### stimuli: analyse audio files ----------------------------------------------

#### set up --------------------------------------------------------------------

# load packages
library(tidyverse)
library(data.table)
library(readxl)
library(janitor)
library(here)

# load/create functions
source(here("R", "utils.R"))

# set parameters
individual_plots <- FALSE

# set paths
audio_paths <- list.files(here("Stimuli", "Sounds"), full.names = TRUE)
formant_paths <- str_replace_all(audio_paths, c("Sounds/" = "Formants/", ".wav" = ".Formant"))
formant_table_paths <- str_replace_all(audio_paths, c("Sounds/" = "/Formants/Tables/", ".wav" = "_table.txt"))
pitch_path  <- str_replace_all(audio_paths, c("Sounds/" = "Pitch/", ".wav" = ".Pitch"))
pitch_tier_path <- str_replace_all(audio_paths, c("Sounds/" = "Pitch/PitchTiers/",".wav" = ".PitchTier"))

#### import data ---------------------------------------------------------------
trials <- read_xlsx(here("Stimuli", "trials.xlsx")) %>%
  select(-translation_english_phonology)

audio_data <- extract_formants(file = here("Stimuli", "Sounds")) %>% 
  mutate(soundfile = paste0("Sounds/", file, ".wav")) %>% 
  right_join(trials, by = "soundfile") 
  
#### analyse formats -----------------------------------------------------------
amplitude <- audio_data %>% 
  select(trial_id, word, orthography, phonology, time, intensity, language, practice, soundfile) 

amplitude_means <- amplitude %>%
  filter(intensity > 0) %>%
  group_by(trial_id, word, language) %>%
  summarise(
    duration = max(time, na.rm = TRUE),
    intensity = mean(intensity, na.rm = TRUE),
    .groups= "drop"
  )

#### analyse F0/pitch ----------------------------------------------------------
pitch <- extract_pitch(file = here("Stimuli", "Sounds")) %>%
  select(trial_id, word, time, f0, language, practice, soundfile)

pitch_mean <- pitch %>%
  group_by(word, trial_id, language, soundfile) %>%
  summarise(
    f0 = mean(f0, na.rm = TRUE),
    .groups = "drop"
  )

#### merge data ----------------------------------------------------------------
merged <- trials %>%
  left_join(amplitude_means) %>%
  left_join(pitch_mean)

#### export data ---------------------------------------------------------------
saveRDS(merged, here("Results", "stimuli.rds"))


#### visualise data ------------------------------------------------------------
# frequency
ggplot(merged, aes(language, frequency_zipf, fill = language, colour = language)) +
  geom_violin() +
  geom_boxplot(width = 0.1, fill = "white", colour = "black") +
  geom_jitter(width = 0.1, colour = "black", shape = 1, stroke = 1, alpha = 0.5) +
  labs(
    x = "Language", y = "Lexical frequency (Zipf score)",
    colour = "Language", fill = "Language"
  ) +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom() +
  theme(
    legend.position = "none",
    axis.title.x = element_blank()
  ) +
  ggsave(here("Figures", "frequency.png"), width = 3.5)


# duration
ggplot(merged, aes(language, duration, fill = language, colour = language)) +
  geom_violin() +
  geom_boxplot(width = 0.1, fill = "white", colour = "black") +
  geom_jitter(width = 0.1, colour = "black", shape = 1, stroke = 1, alpha = 0.5) +
  labs(
    x = "Language", y = "Duratoin (s)",
    colour = "Language", fill = "Language"
  ) +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom() +
  theme(
    legend.position = "none",
    axis.title.x = element_blank()
  ) +
  ggsave(here("Figures", "duration.png"), width = 3.5)

# intensity
ggplot(merged, aes(x = language, y = intensity, fill = language)) +
  geom_violin(size = 1, alpha = 0.5, colour = "transparent") +
  geom_boxplot(width = 0.1, size = 0.6, fill = "white", colour = "black", outlier.colour = "transparent") +
  geom_point(size = 1, position = position_jitter(width = 0.1), colour = "black", alpha = 0.1) +
  labs(x = "Language", y = "Intensity (dB)", fill = "Language",
       title = "Mean intensity") +
  scale_fill_brewer(palette = "Set1") + 
  scale_y_continuous(labels = function(x) round(x, 20)) +
  theme_custom()

if (individual_plots) {
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
}

# pitch
ggplot(pitch, aes(x = time, y = f0, colour = language, fill = language)) +
  geom_line(aes(group = trial_id), alpha = 0.15, size = 0.5) +
  geom_smooth(method = "gam") +
  labs(x = "Time (s)", y = "F0/Pitch (Hz)", colour = "Language", fill = "Language",
       title = "Pitch across time") +
  scale_color_brewer(palette = "Set1") +
  scale_fill_brewer(palette = "Set1") +
  theme_custom()



