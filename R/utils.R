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
# ggplot custom theme
theme_custom <- function(){
    theme(
        panel.background = element_rect(fill = "transparent"),
        panel.grid = element_blank(),
        #panel.grid = element_line(colour = "grey", linetype = "dotted"),
        panel.border = element_rect(fill = "transparent", colour = "black"),
        text = element_text(colour = "black", size = 15),
        axis.text = element_text(colour = "black")
    )
}

# remove special characters
replace_non_ascii <- function(x){
    str_replace_all(
        x,
        c(
            "á" = "a",
            "é" = "e",
            "í" = "i",
            "ó" = "o",
            "ú" = "u",
            "à" = "a",
            "è" = "e",
            "ò" = "o",
            "ñ" = "n",
            "ç" = "c"
        )
        )
}

# extract formants
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

# extract pitch
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

# download clearpond
import_clearpond <- function(language = c("english", "dutch", "french", "spanish", "german")){
    require(tidyverse)
    require(janitor)
    urls <- tribble(
        ~lang, ~url, ~data, ~header,
        "english", "https://clearpond.northwestern.edu/englishCPdatabase2.zip", "englishCPdatabase2.txt", "clearpondHeaders_EN.txt",
        "dutch", "https://clearpond.northwestern.edu/dutchCPdatabase2.zip", "dutchCPdatabase2.txt", "clearpondHeaders_NL.txt",
        "french", "https://clearpond.northwestern.edu/frenchCPdatabase2.zip", "frenchCPdatabase2.txt", "clearpondHeaders_FR.txt",
        "german", "https://clearpond.northwestern.edu/germanCPdatabase2.zip", "germanCPdatabase2.txt", "clearpondHeaders_DE.txt",
        "spanish", "https://clearpond.northwestern.edu/spanishCPdatabase2.zip", "spanishCPdatabase2.txt", "clearpondHeaders_SP.txt"
    ) %>% 
        filter(lang %in% language)
    
    dir <- tempdir()
    files <- replicate(tempfile(), n = length(urls$lang))
    d <- pmap(
        .l = list(url = as.list(urls$url), file = as.list(files), data = as.list(urls$data), header = as.list(urls$header)),
        .f = function(url = .l[[1]], file = .l[[2]], data = .l[[3]], header = .l[[4]]) {
            download.file(url, destfile = file)
            unzip(zipfile = file, exdir = dir)
            headers <- c("word", read.delim(paste0(dir, .Platform$file.sep, header))[,1])
            d <- read.delim(paste0(dir, .Platform$file.sep, data)) %>% 
                `colnames<-`(., headers) %>% 
                as_tibble() %>% 
                mutate_at(vars(ends_with("W")), ~str_split(., pattern = ";"))
            return(d)
        }
    ) %>% 
        set_names(language) %>% 
        bind_rows(.id = "language") %>% 
        clean_names()
    return(d)
}

# import subtlex
import_subtlex <- function() {
    df <- list.files("Data", pattern = "SUBTLEX", full.names = TRUE, recursive = TRUE) %>% 
        map(
            function(x) {
                readxl::read_xlsx(x, na = c("", "NA")) %>% 
                    janitor::clean_names()
            }
        ) %>% 
        set_names(c("Catalan", "Spanish", "English"))
    df$English$freq_rel <- zipf_to_relative(df$English$freq_zipf)
    df <- df %>% 
        bind_rows(.id = "language") %>% 
        select(word, language, freq_rel) %>% 
        mutate(freq_zipf = 3 + log10(freq_rel))
    return(df)
}

# relative frequency to zipf
relative_to_zipf <- function(x){
    3 + log10(x)
}

# zipf frequency to relative
zipf_to_relative <- function(x){
    10^(x-3)
}

# import_trials
import_trials <- function(path = "Stimuli/trials.xlsx", subtlex = NULL){
    if (is.null(subtlex)) subtlex <- import_subtlex()
    trials <- map(
        readxl::excel_sheets(path)[-1],
        function(x) readxl::read_xlsx(path, sheet = x, na = c("", "NA"))
    ) %>% 
        set_names(c("Spanish-English", "Catalan-English", "Catalan-Spanish")) %>% 
        map2(
            .y = list(
                filter(subtlex, language=="English"),
                filter(subtlex, language=="English"),
                filter(subtlex, language=="Spanish")
            ),
            function(x, y) left_join(x, y, by = c("word2" = "word"))
        ) %>% 
        bind_rows(.id = "list") %>% 
        select(list, trial_id, word1, word2, jtrace1, jtrace2, consonant_ratio, vowel_ratio, onset, overlap_stress, starts_with("freq_"))
    return(trials)
}

# proportion adjusted from boundary values (Gelman, Hill & Vehtari, 2020)
prop_adj <- function(x, n){
    e <- (x+2)/(n+4)
    return(e)
}

# adjusted standard error of proportion (Gelman, Hill & Vehtari, 2020)
prop_adj_se <- function(x, n) {
    e <- (x+2)/(n+4)
    se <- sqrt(e*(1-e)/(n+4))
    return(se)
}

# adjusted standard error of proportion (Gelman, Hill & Vehtari, 2020)
prop_adj_ci <- function(x, n, .width = 0.95) {
    e <- (x+2)/(n+4)
    se <- sqrt(e*(1-e)/(n+4))
    ci <-  e + qnorm(c((1-.width)/2, (1-(1-.width)/2)))*se
    ci[1] <- ifelse(ci[1]<0, 0, ci[1]) # truncate at 0
    ci[2] <- ifelse(ci[2]>1, 1, ci[2]) # truncate at 1
    return(ci)
}
