#' Get first non-missing value in vector
#' 
first_non_na <- function(x){
    ifelse(is.logical(first(x[!is.na(x)])), NA, first(x[!is.na(x)]))
}

#' Get last non-missing value in vector
#' 
last_non_na <- function(x){
    ifelse(is.logical(last(x[!is.na(x)])), NA, last(x[!is.na(x)]))
}

#' Custom ggplot2 theme
#' 
theme_custom <- function(){
    theme(panel.background = element_rect(fill = "transparent"),
          panel.grid = element_blank(),
          panel.grid.major.y = element_line(colour = "grey", linetype = "dotted"),
          panel.border = element_rect(fill = "transparent", colour = "black"),
          text = element_text(colour = "black", size = 15),
          axis.text = element_text(colour = "black"))
}

#' Remove non-ASCII characters (diacritic accents)
#' 
replace_non_ascii <- function(x){
    str_replace_all(
        x,
        enc2utf8(c(
            "á" = "a",
            "é" = "e",
            "í" = "i",
            "ó" = "o",
            "ú" = "u",
            "à" = "a",
            "è" = "e",
            "ò" = "o",
            "ñ" = "n",
            "ç" = "c",
            "ü" = "u"
        ))
    )
}















