#' Download CLEARPOND
#' 
download_clearpond <- function(.language = c("english", "dutch", "french", "spanish", "german")){
    urls <- tribble(
        ~lang, ~url, ~data, ~header,
        "english", "https://clearpond.northwestern.edu/englishCPdatabase2.zip", "englishCPdatabase2.txt", "clearpondHeaders_EN.txt",
        "dutch", "https://clearpond.northwestern.edu/dutchCPdatabase2.zip", "dutchCPdatabase2.txt", "clearpondHeaders_NL.txt",
        "french", "https://clearpond.northwestern.edu/frenchCPdatabase2.zip", "frenchCPdatabase2.txt", "clearpondHeaders_FR.txt",
        "german", "https://clearpond.northwestern.edu/germanCPdatabase2.zip", "germanCPdatabase2.txt", "clearpondHeaders_DE.txt",
        "spanish", "https://clearpond.northwestern.edu/spanishCPdatabase2.zip", "spanishCPdatabase2.txt", "clearpondHeaders_SP.txt"
    ) %>%
        dplyr::filter(lang %in% .language)
    
    dir <- tempdir()
    files <- replicate(tempfile(), n = length(urls$lang))
    d <- pmap(.l = list(url = as.list(urls$url), 
                        file = as.list(files),
                        data = as.list(urls$data),
                        header = as.list(urls$header)),
              .f = function(url = .l[[1]],
                            file = .l[[2]],
                            data = .l[[3]], 
                            header = .l[[4]]) {
                  download.file(url, destfile = file)
                  unzip(zipfile = file, exdir = dir)
                  headers <- c("word", read.delim(paste0(dir, .Platform$file.sep, header))[,1])
                  d <- read.delim(
                      paste0(dir, .Platform$file.sep, data)) %>%
                      `colnames<-`(., headers) %>%
                      as_tibble() %>%
                      mutate_at(vars(ends_with("W")), ~str_split(., pattern = ";")
                      )
                  return(d)
              }
    ) %>%
        set_names(language) %>%
        bind_rows(.id = "language") %>%
        janitor::clean_names()
    
    return(d)
}

#' Download CLEARPOND
#' 
download_clearpond <- function(.language = c("english", "dutch", "french", "spanish", "german")){
    urls <- tribble(
        ~lang, ~url, ~data, ~header,
        "english", "https://clearpond.northwestern.edu/englishCPdatabase2.zip", "englishCPdatabase2.txt", "clearpondHeaders_EN.txt",
        "dutch", "https://clearpond.northwestern.edu/dutchCPdatabase2.zip", "dutchCPdatabase2.txt", "clearpondHeaders_NL.txt",
        "french", "https://clearpond.northwestern.edu/frenchCPdatabase2.zip", "frenchCPdatabase2.txt", "clearpondHeaders_FR.txt",
        "german", "https://clearpond.northwestern.edu/germanCPdatabase2.zip", "germanCPdatabase2.txt", "clearpondHeaders_DE.txt",
        "spanish", "https://clearpond.northwestern.edu/spanishCPdatabase2.zip", "spanishCPdatabase2.txt", "clearpondHeaders_SP.txt"
    ) %>%
        dplyr::filter(lang %in% .language)
    
    dir <- tempdir()
    files <- replicate(tempfile(), n = length(urls$lang))
    d <- pmap(.l = list(url = as.list(urls$url), 
                        file = as.list(files),
                        data = as.list(urls$data),
                        header = as.list(urls$header)),
              .f = function(url = .l[[1]],
                            file = .l[[2]],
                            data = .l[[3]], 
                            header = .l[[4]]) {
                  download.file(url, destfile = file)
                  unzip(zipfile = file, exdir = dir)
                  headers <- c("word", read.delim(paste0(dir, .Platform$file.sep, header))[,1])
                  d <- read.delim(
                      paste0(dir, .Platform$file.sep, data)) %>%
                      `colnames<-`(., headers) %>%
                      as_tibble() %>%
                      mutate_at(vars(ends_with("W")), ~str_split(., pattern = ";")
                      )
                  return(d)
              }
    ) %>%
        set_names(language) %>%
        bind_rows(.id = "language") %>%
        janitor::clean_names()
    
    return(d)
}


#' Import CLEARPOND
#'
import_clearpond <- function(cp_c_path_eng, 
                             cp_c_path_spa,
                             cp_h_path_eng,
                             cp_h_path_spa) {
    suppressWarnings({
        header <- readLines(file.path(cp_h_path_eng), warn = FALSE)
        eng <- read_tsv(file.path(cp_c_path_eng), 
                        col_names = header,
                        progress = FALSE, 
                        show_col_types = FALSE) |> 
            janitor::clean_names() 
        
        header <- readLines(file.path(cp_h_path_spa), warn = FALSE)
        spa <- read_tsv(file.path(cp_c_path_spa), 
                        col_names = header,
                        progress = FALSE,
                        show_col_types = FALSE) |> 
            janitor::clean_names() 
        
        out <- bind_rows(lst("English" = eng,
                             "Spanish" = spa),
                         .id = "language") |>  
            rename(sampa = phono,
                   freq = frequency) |> 
            mutate(sampa = str_remove_all(sampa, "\\."),
                   freq_relative = 1e6 * freq/n(),
                   freq_zipf = log10(freq_relative) + 3,
                   .by = c(language)) |> 
            select(language, word, sampa, freq_zipf)
    })
    
    return(out)
}

import_ipa_dict <- function(ipa_dict_eng_path,
                            ipa_dict_spa_path) {
    nms <- c("word", "ipa")
    eng <- read_tsv(ipa_dict_eng_path,
                    col_names = nms,
                    show_col_types = FALSE) 
    
    spa <- read_tsv(ipa_dict_spa_path, 
                    col_names = nms, 
                    show_col_types = FALSE)

    x <- bind_rows(list(English = eng, Spanish = spa), 
                   .id = "language") |> 
        mutate(ipa = str_remove_all(ipa, "\\/"),
               sampa = ipa::ipa(str_remove_all(ipa, "[[:punct]]| |:|ˈ")))
    
    return(x)   
}


import_subtlex <- function(subtlex_eng_path,
                           subtlex_spa_path,
                           min_zipf = 2){
    
    read_subtlex <- function(x, range = NULL) {
        read_xlsx(file.path(x),
                  na = c("NA", "", "na"),
                  range = range,
                  .name_repair = janitor::make_clean_names)
    }
    
    # english
    pb <- cli::cli_progress_bar("Importing SUBTLEX")
    
    eng <- read_subtlex(subtlex_eng_path) |> 
        mutate(freq_million = freq_count / n_distinct(spelling)) |> 
        select(word = spelling, 
               freq_count, 
               freq_million, 
               freq_zipf = log_freq_zipf) |> 
        drop_na()
    
    cli::cli_progress_step("Imported SUBTLEX-UK")
    
    # spanish
    spa <- map_df(c("A1:D31447", "F1:I31447", "K1:N31447"), 
                  \(x) read_subtlex(subtlex_spa_path,
                                    range = x)) |> 
        drop_na() |> 
        mutate(freq_zipf = log10(freq_per_million)+3) |> 
        select(word, 
               freq_count, 
               freq_million = freq_per_million,
               freq_zipf) |> 
        drop_na()
    
    cli::cli_progress_step("Imported SUBTLEX-ESP")
    
    cli::cli_progress_done()
    
    # merge
    x <- bind_rows(list(English = eng, Spanish = spa), 
                   .id = "language") |> 
        arrange(language, word, -freq_zipf) |> 
        mutate(lang_code = if_else(language=="English", "en", "es")) |> 
        dplyr::filter(freq_zipf >= min_zipf)
    
    return(x)
}