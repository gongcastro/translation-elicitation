source("renv/activate.R")

suppressMessages({
    library(targets, quietly = TRUE)
    library(cli)
})

options(repos = c(stan = "https://mc-stan.org/r-packages/",
                  ropensci = "https://ropensci.r-universe.dev",
                  CRAN = "https://cloud.r-project.org"),
        scipen = 4)

if (interactive()) {
    cli_h1("Translation Elicitation")
    cli_text("")
    cli_text(R.version$version.string)
    cli_text("Run {.code make()} to update the project")
    cli_text("GitHub repository: {.url https://github.com/gongcastro/translation-elicitation}")
}

