#### utils: helper functions ---------------------------------------------------

# evaluate if x is NOT an element of y
"%!in%" <- function(x, y) !(x %in% y)

# find first/last non-missing value in vector
first_non_na <- function(x) ifelse(is.logical(first(x[!is.na(x)])), NA, first(x[!is.na(x)]))
last_non_na <- function(x) ifelse(is.logical(last(x[!is.na(x)])), NA, last(x[!is.na(x)]))
add_big_mark <- function(x) format(x, big.mark = ",", scientific = FALSE)
clean_input_text <- function(x) {
    {{ x }} %>% 
        str_to_sentence() %>%
        str_replace("Lshift|space|minus", "") %>%
        as.character() %>% 
        as_tibble(x = .) %>% 
        mutate(. , value = case_when( 
            nchar(value) > 12 ~ "Several",
            value %in% c("Francés", "Frances", "Basic french") ~ "French",
            value %in% c("Italiano", "Italino") ~ "Italian",
            value %in% c("Alemán") ~ "German",
            value %in% c("NrLondon") ~ "London",
            value %in% c("Rnorthampton") ~ "London",
            value %in% c("Newcastleminusuponminustyne") ~ "Newcastle upon Tyne",
            value %in% c("Newcastlespaceuk") ~ "Newcastle",
            value %in% c("Miltonkeynes") ~ "Milton Keynes",
            value %in% c("Irthlingboroug") ~ "Irthlingborough",
            value %in% c("spalding", "berkshire", "bedfordshire") ~ str_to_sentence(value),
            value %in% c("No", "Cuál", "Space") ~ NA_character_,
            TRUE ~ value)) %>% 
        pull(value)
}
#### ggplot custom theme ##################################
theme_custom <- function(){
    theme(
        panel.background = element_rect(fill = "transparent"),
        panel.grid = element_line(colour = "grey", linetype = "dotted"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        text = element_text(colour = "black", size = 15),
        axis.text = element_text(colour = "black")
    )
}

#### extract formants #####################################
extract_formants <- function(
    file,
    time_step = 0.001,
    n = 2,
    max_freq = 5500,
    window_length = 0.001,
    pre = 50,
    include_frames = TRUE,
    include_time = TRUE,
    dec = 3,
    include_intensity = TRUE,
    dec_intensity = 5,
    include_n_formats = FALSE,
    dec_freq = 3,
    include_bandwidths = FALSE) {
    require(PraatR)
    require(rlang)
    require(purrr)
    require(stringr)
    require(dplyr)
    require(data.table)
    require(janitor)
    
    file_paths <- list.files({{ file }}, pattern = ".wav", full.names = TRUE)
    file_names <- list.files({{ file }}, pattern = ".wav", full.names = FALSE)
    
    pb <- progress_estimated(length(file_paths)*2)
    arguments1 <- list({{ time_step }}, {{ n }}, {{ max_freq }}, {{ window_length }}, {{ pre }})
    arguments2 <- list({{ include_frames }}, {{ include_time }}, {{ dec }}, {{ include_intensity }}, {{ dec_intensity }}, {{ include_n_formats }}, {{ dec_freq }}, {{ include_bandwidths }}) 
    
    dir <- tempdir()
    dir_formants <- paste(dir, file_names, sep = "/") %>% str_replace(., ".wav", ".Formant")
    dir_formants_table <- paste(dir, file_names, sep = "/")  %>% str_replace(., ".wav", ".txt")
    
    
    fun1 <- function(x, y) {
        pb$tick()$print()
        praat("To Formant (burg)...",
              arguments = arguments1,
              input = x,
              output = y,
              overwrite = TRUE)
    }
    
    fun2 <- function(x, y){
        pb$tick()$print()
        praat("Down to Table...",
              arguments = arguments2,
              input = x,
              output = y,
              filetype = "tab-separated",
              overwrite = TRUE)
    }
    
    invisible(
        map2(.x = as.list(file_paths),
             .y = as.list(dir_formants),
             .f = ~fun1(.x, .y))
    )
    
    invisible(
        map2(.x = as.list(dir_formants),
             .y = as.list(dir_formants_table),
             .f = ~fun2(.x, .y))
    )
    
    map(.x = dir_formants_table,
        .f = ~fread(., header = TRUE, sep = "\t", dec = ".", na.strings = "--undefined--")) %>%
        set_names(str_remove(file_names, ".wav")) %>%
        bind_rows(.id = "file") %>%
        clean_names() %>%
        rename_all(~str_remove(., "_hz")) %>%
        rename_all(~str_remove(., "_s")) 
    
    
}

#### extract pitch ######################################
extract_pitch <- function(
    file,
    time_step = 0.001,
    pitch_floor = 50,
    pitch_ceiling = 800
) {
    require(PraatR)
    require(rlang)
    require(purrr)
    require(stringr)
    require(dplyr)
    require(data.table)
    require(janitor)
    
    file_paths <- list.files({{ file }}, pattern = ".wav", full.names = TRUE)
    file_names <- list.files({{ file }}, pattern = ".wav", full.names = FALSE)
    
    pb <- progress_estimated(length(file_paths)*2)
    arguments <- list({{ time_step }}, {{ pitch_floor }}, {{ pitch_ceiling }})
    
    dir <- tempdir()
    dir1 <- paste(dir, file_names, sep = "/") %>% str_replace(., ".wav", ".Pitch")
    dir2 <- paste(dir, file_names, sep = "/")  %>% str_replace(., ".wav", ".PitchTier")
    
    fun1 <- function(x, y) {
        pb$tick()$print()
        praat("To Pitch...",
              arguments = arguments,
              input = x,
              output = y,
              overwrite = TRUE)
    }
    
    fun2 <- function(x, y) {
        pb$tick()$print()
        praat("Down to PitchTier",
              input = x,
              output = y,
              overwrite = TRUE,
              filetype="headerless spreadsheet")
    }
    
    
    invisible(map2(.x = as.list(file_paths),
                   .y = as.list(dir1),
                   .f = ~fun1(.x, .y)))
    invisible(map2(.x = as.list(dir1),
                   .y = as.list(dir2),
                   .f = ~fun2(.x, .y)))
    map(.x = as.list(dir2),
        .f = ~fread(., header = FALSE, sep = "\t", dec = ".", na.strings = "--undefined--")) %>%
        set_names(str_remove(file_names, ".wav")) %>%
        bind_rows(.id = "file") %>%
        clean_names() %>%
        rename(time = v1, f0 = v2)
    
}
