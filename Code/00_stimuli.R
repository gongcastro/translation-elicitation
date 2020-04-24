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
library(janitor)
library(audio)
library(PraatR)
library(here)

# set parameters
time_bin_duration <- 0.001
# time-step (s), 
formant_arguments <- list(0.001,  5, 5500, time_bin_duration, 50)
# include frame number, include time, time decimals, include intensity, intensity decimals, include n formants, freq decimals, include bandwidths
table_arguments <- list(TRUE, TRUE, 3, TRUE, 5, FALSE, 3, TRUE) 
# time step (s), pitch floor, pitch ceiling
pitch_arguments <- list(0.001, 50, 800) 

# set paths
audio_paths <- list.files(here("Stimuli", "Sounds"), full.names = TRUE)
formant_paths <- str_replace(audio_paths, "Sounds/", "Formants/") %>% str_replace(., ".wav", ".Formant")
formant_table_paths <- str_replace(audio_paths, "Sounds/", "/Formants/Tables/") %>% str_replace(., ".wav", "_table.txt")
pitch_path <- str_replace(audio_paths, "Sounds/", "Pitch/") %>% str_replace(., ".wav", ".Pitch")
pitch_tier_path <- str_replace(audio_paths, "Sounds/", "Pitch/PitchTiers/") %>% str_replace(., ".wav", ".PitchTier")

#### import data #################################
trials <- read_xlsx(here("Stimuli", "trials.xlsx"))
subtlex <- fread(here("Data", "00_subtlex.csv")) %>% as_tibble()

#### analyse frequency (SUBTLEX) #################
frequency <- left_join(trials, subtlex, by = c("orthography" = "word", "language"))

#### analyse formats #############################

map2(.x = audio_paths, .y = formant_paths,
    ~praat("To Formant (burg)...",
           arguments = formant_arguments,
           input = .x,
           output = .y,
           overwrite = TRUE))

map2(.x = formant_paths, .y = formant_table_paths,
     ~praat("Down to Table...",
            arguments = table_arguments,
            input = .x,
            output = .y,
            filetype = "tab-separated",
            overwrite = TRUE))

praat_data <- map(formant_table_paths, fread, na.strings = c("--undefined--")) %>%
  set_names(trials$soundfile) %>%
  bind_rows(.id = "soundfile") %>%
  clean_names() %>%
  select(soundfile, time_s, intensity, f1_hz, f2_hz) %>%
  rename(time = time_s, F1 = f1_hz, F2 = f2_hz) %>%
  as_tibble() %>%
  right_join(trials, by = "soundfile") %>%
  select(trial_id, word, intensity, orthography, phonology, time, F1, F2, language, practice, soundfile)


formants <- praat_data %>%
    group_by(trial_id, word, language, practice) %>%
    summarise(duration = max(time, na.rm = TRUE),
              mean_f1 = mean(F1, na.rm = TRUE),
              mean_f2 = mean(F2, na.rm = TRUE)) %>%
    ungroup()

formant_means <- formants %>%
    group_by(language) %>%
    summarise(f1 = mean(mean_f1, na.rm = TRUE),
              f2 = mean(mean_f2, na.rm = TRUE),
              sd_f1 = sd(mean_f1, na.rm = TRUE),
              sd_f2 = sd(mean_f2, na.rm = TRUE))

# analyse amplitude
amplitude <- praat_data %>%
    mutate(intensity = -intensity) %>%
    bind_rows(praat_data)

amplitude_means <- amplitude %>%
  group_by(trial_id, word, language) %>%
  summarise(intensity = mean(intensity, na.rm = TRUE))
              
#### analyse F0/pitch ############################
map2(audio_paths, pitch_path,
    ~praat("To Pitch...",
           arguments = pitch_arguments,
           input = .x,
           output = .y,
           overwrite = TRUE))

map2(pitch_path, pitch_tier_path,
    ~praat("Down to PitchTier",
           input = .x,
           output = .y,
           overwrite = TRUE,
           filetype="headerless spreadsheet"))

pitch <- map(pitch_tier_path, fread) %>%
  set_names(trials$soundfile) %>%
  bind_rows(.id = "soundfile") %>%
  rename(time = V1, f0 = V2) %>%
  as_tibble() %>%
  right_join(trials, by = "soundfile") %>%
  select(trial_id, word, time, f0, language, practice, soundfile)
  
pitch_mean <- pitch %>%
  group_by(word, trial_id, language, soundfile) %>%
  summarise(f0 = mean(f0, na.rm = TRUE))

 #### merge data #################################
merged <- frequency %>%
  left_join(formants) %>%
  left_join(amplitude_means) %>%
  left_join(pitch_mean)
  
#### visualise data ##############################
# frequency
plot_frequency <- ggplot(merged, aes(zipf, language, fill = language, colour = language)) +
  stat_density_ridges(alpha = 0.5,
                      colour = "black",
                      jittered_points = TRUE,
                      position = position_points_jitter(width = 0.05, height = 0),
                      point_shape = "|",
                      point_size = 3,
                      point_alpha = 1,
                      quantile_lines = TRUE,
                      quantiles = c(0.25, 0.5, 0.75)) +
  labs(x = "SUBTLEX frequency (Zipf score)", y = "Language",
       colour = "Language", fill = "Language", title = "Frequency") +
  scale_color_brewer(palette = "Dark2") +
  scale_fill_brewer(palette = "Dark2") +
  theme(panel.background = element_rect(fill = "transparent"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        panel.grid = element_blank(),
        text = element_text(size = 12),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.title.y = element_blank(),
        axis.text = element_text(colour = "black"),
        legend.direction = "horizontal") +
  ggsave(here("Figures", "00_stimuli-frequency.png"))

# duration
plot_duration <- ggplot(merged, aes(x = language, y = duration, fill = language)) +
  geom_violin(size = 1, alpha = 0.5, colour = "transparent") +
  geom_boxplot(width = 0.1, size = 1, fill = "white", colour = "black") +
  geom_point(size = 2, position = position_jitter(width = 0.1), colour = "black", alpha = 0.3) +
  labs(x = "Language", y = "Duration (s)", fill = "Language",
       title = "Duration") +
  scale_fill_brewer(palette = "Dark2") +
  theme(panel.background = element_rect(fill = "transparent"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        panel.grid = element_blank(),
        text = element_text(size = 12),
        axis.text = element_text(colour = "black"),
        legend.direction = "horizontal") +
  ggsave(here("Figures", "00_stimuli-duration.png"))

# formants
plot_formants <- ggplot(merged, aes(colour = language, shape = language)) +
    geom_point(aes(x = mean_f2, y = mean_f1), size = 2, alpha = 0.5) +
    geom_errorbar(data = formant_means, aes(x = f2, ymin = f1-sd_f1, ymax = f1+sd_f1), size = 1) +
    geom_errorbarh(data = formant_means, aes(y = f1, xmin = f2-sd_f2, xmax = f2+sd_f2), size = 1) +
    geom_point(data = formant_means, aes(f2, f1), size = 4) +
    labs(x = "F2 (Hz)", y = "F1 (Hz)", colour = "Language", shape = "Language",
         title = "Formants") +
    scale_colour_brewer(palette = "Dark2") +
    scale_x_continuous(trans = "reverse") +
    scale_y_continuous(trans = "reverse") +
    theme(panel.background = element_rect(fill = "transparent"),
          panel.border = element_rect(fill = "transparent", colour = "black"),
          panel.grid = element_blank(),
          text = element_text(size = 12),
          axis.text = element_text(colour = "black"),
          legend.position = c(0.1, 0.8),
          legend.direction = "horizontal") +
    ggsave(here("Figures", "00_stimuli-formants.png"))

praat_data %>%
  pivot_longer(c(F1, F2), names_to = "formant", values_to = "frequency") %>%
  split(.$soundfile) %>%
  map(~ggplot(data = ., aes(x = time, y = frequency, colour = formant)) +
        geom_line(alpha = 0.5) +
        geom_smooth(aes(linetype = formant)) +
        labs(x = "Time (s)", y = "Frequency (Hz)",
             colour = "Formant", fill = "Formant", linetype = "Formant",
             title = str_to_upper(distinct(., orthography)),
             subtitle = paste0("Language: ", distinct(., language),
                               " / Phonology (IPA): ", distinct(., phonology))) +
        scale_color_brewer(palette = "Dark2") +
        scale_fill_brewer(palette = "Dark2") +
        theme(panel.background = element_rect(fill = "transparent"),
              panel.border = element_rect(fill = "transparent", colour = "black"),
              panel.grid = element_blank(),
              text = element_text(size = 12),
              axis.text = element_text(colour = "black"),
              legend.position = c(0.3, 0.9),
              legend.direction = "horizontal") +
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

plot_amplitude <- ggplot(amplitude_summary, aes(x = language, y = intensity, fill = language)) +
  geom_violin(size = 1, alpha = 0.5, colour = "transparent") +
  geom_boxplot(width = 0.1, size = 1, fill = "white", colour = "black") +
  geom_point(size = 2, position = position_jitter(width = 0.1), colour = "black", alpha = 0.3) +
  labs(x = "Language", y = "Intensity (dB)", fill = "Language",
       title = "Mean intensity") +
  scale_fill_brewer(palette = "Dark2") +
  theme(panel.background = element_rect(fill = "transparent"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        panel.grid = element_blank(),
        text = element_text(size = 12),
        axis.text = element_text(colour = "black"),
        legend.direction = "horizontal") +
  ggsave(here("Figures", "00_stimuli-amplitude.png"))

# pitch
plot_pitch <- ggplot(pitch, aes(x = time, y = f0, colour = language, fill = language)) +
  geom_line(aes(group = trial_id), alpha = 0.15, size = 0.5) +
  geom_smooth() +
  labs(x = "Time (s)", y = "F0/Pitch (Hz)", colour = "Language", fill = "Language",
       title = "Pitch across time") +
  scale_color_brewer(palette = "Dark2") +
  scale_fill_brewer(palette = "Dark2") +
  theme(panel.background = element_rect(fill = "transparent"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        panel.grid = element_blank(),
        text = element_text(size = 12),
        axis.text = element_text(colour = "black"),
        legend.position = c(0.7, 0.9),
        legend.direction = "horizontal") +
  ggsave(here("Figures", "00_stimuli-pitch.png"))


# arrange plots
plot_frequency + guide_area() + plot_duration + plot_formants + plot_amplitude + plot_pitch +
  plot_layout(guides = "collect") +
  ggsave(here("Figures", "00_stimuli.png"))
  
