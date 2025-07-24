#' Download CLEARPOND
#'
download_clearpond <- function(
  .language = c("english", "dutch", "french", "spanish", "german")
) {
  urls <- tribble(
    ~lang,
    ~url,
    ~data,
    ~header,
    "english",
    "https://clearpond.northwestern.edu/englishCPdatabase2.zip",
    "englishCPdatabase2.txt",
    "clearpondHeaders_EN.txt",
    "dutch",
    "https://clearpond.northwestern.edu/dutchCPdatabase2.zip",
    "dutchCPdatabase2.txt",
    "clearpondHeaders_NL.txt",
    "french",
    "https://clearpond.northwestern.edu/frenchCPdatabase2.zip",
    "frenchCPdatabase2.txt",
    "clearpondHeaders_FR.txt",
    "german",
    "https://clearpond.northwestern.edu/germanCPdatabase2.zip",
    "germanCPdatabase2.txt",
    "clearpondHeaders_DE.txt",
    "spanish",
    "https://clearpond.northwestern.edu/spanishCPdatabase2.zip",
    "spanishCPdatabase2.txt",
    "clearpondHeaders_SP.txt"
  ) %>%
    dplyr::filter(lang %in% .language)

  dir <- tempdir()
  files <- replicate(tempfile(), n = length(urls$lang))
  d <- pmap(
    .l = list(
      url = as.list(urls$url),
      file = as.list(files),
      data = as.list(urls$data),
      header = as.list(urls$header)
    ),
    .f = function(
      url = .l[[1]],
      file = .l[[2]],
      data = .l[[3]],
      header = .l[[4]]
    ) {
      download.file(url, destfile = file)
      unzip(zipfile = file, exdir = dir)
      headers <- c(
        "word",
        read.delim(paste0(dir, .Platform$file.sep, header))[, 1]
      )
      d <- read.delim(
        paste0(dir, .Platform$file.sep, data)
      ) %>%
        `colnames<-`(., headers) %>%
        as_tibble() %>%
        mutate_at(vars(ends_with("W")), ~ str_split(., pattern = ";"))
      return(d)
    }
  ) %>%
    set_names(language) %>%
    bind_rows(.id = "language") %>%
    janitor::clean_names()

  return(d)
}
