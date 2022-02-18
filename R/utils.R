# evaluate if x is NOT an element of y
"%!in%" <- function(x, y) !(x %in% y)

# find first/last non-missing value in vector
first_non_na <- function(x) ifelse(is.logical(first(x[!is.na(x)])), NA, first(x[!is.na(x)]))
last_non_na <- function(x) ifelse(is.logical(last(x[!is.na(x)])), NA, last(x[!is.na(x)]))
# add_big_mark <- function(x) format(x, big.mark = ",", scientific = FALSE)
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

#  custom theme
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


# download clearpond
# import_clearpond <- function(language = c("english", "dutch", "french", "spanish", "german")){
#     require(tidyverse)
#     require(janitor)
#     urls <- tribble(
#         ~lang, ~url, ~data, ~header,
#         "english", "https://clearpond.northwestern.edu/englishCPdatabase2.zip", "englishCPdatabase2.txt", "clearpondHeaders_EN.txt",
#         "dutch", "https://clearpond.northwestern.edu/dutchCPdatabase2.zip", "dutchCPdatabase2.txt", "clearpondHeaders_NL.txt",
#         "french", "https://clearpond.northwestern.edu/frenchCPdatabase2.zip", "frenchCPdatabase2.txt", "clearpondHeaders_FR.txt",
#         "german", "https://clearpond.northwestern.edu/germanCPdatabase2.zip", "germanCPdatabase2.txt", "clearpondHeaders_DE.txt",
#         "spanish", "https://clearpond.northwestern.edu/spanishCPdatabase2.zip", "spanishCPdatabase2.txt", "clearpondHeaders_SP.txt"
#     ) %>% 
#         filter(lang %in% language)
#     
#     dir <- tempdir()
#     files <- replicate(tempfile(), n = length(urls$lang))
#     d <- pmap(
#         .l = list(url = as.list(urls$url), file = as.list(files), data = as.list(urls$data), header = as.list(urls$header)),
#         .f = function(url = .l[[1]], file = .l[[2]], data = .l[[3]], header = .l[[4]]) {
#             download.file(url, destfile = file)
#             unzip(zipfile = file, exdir = dir)
#             headers <- c("word", read.delim(paste0(dir, .Platform$file.sep, header))[,1])
#             d <- read.delim(paste0(dir, .Platform$file.sep, data)) %>% 
#                 `colnames<-`(., headers) %>% 
#                 as_tibble() %>% 
#                 mutate_at(vars(ends_with("W")), ~str_split(., pattern = ";"))
#             return(d)
#         }
#     ) %>% 
#         set_names(language) %>% 
#         bind_rows(.id = "language") %>% 
#         clean_names()
#     return(d)
# }

# import subtlex
import_subtlex <- function() {
    df <- list.files("data", pattern = "SUBTLEX", full.names = TRUE, recursive = TRUE) %>%
        map(~janitor::clean_names(readxl::read_xlsx(., na = c("", "NA")))) %>%
        set_names(c("Catalan", "Spanish", "English"))
    df$English$freq_rel <- 10^(df$English$freq_zipf-3)
    df <- df %>%
        bind_rows(.id = "language") %>%
        select(word, language, freq_rel) %>%
        mutate(freq_zipf = 3+log10(freq_rel))
    return(df)
}


# import_trials
import_trials <- function(path = "stimuli/trials.xlsx", subtlex = NULL){
    if (is.null(subtlex)) subtlex <- import_subtlex()
    trials <- readxl::excel_sheets(path)[-1] %>% 
        map(~readxl::read_xlsx(path, sheet = ., na = c("", "NA"))) %>% 
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
        select(
            list, trial_id, word1, word2, jtrace1, jtrace2, consonant_ratio, 
            vowel_ratio, onset, overlap_stress, starts_with("freq_")
        )
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
