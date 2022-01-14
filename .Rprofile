source("renv/activate.R")

library(targets, quietly = TRUE)

# run all targets as an RStudio job
make <- function(){
    job::job(
        title = "Translation Elicitation", {{ 
            targets::tar_make() 
        }}
    )
}

# load all built targets (and packages)
tar_load_all <- function(){
    invisible({
        suppressMessages({
            tar_load_globals()
        })
        tars <- tar_objects()
        message("Loading targets: ", paste0(tars, collapse = ", "))
        lapply(tars, tar_load_raw, envir = .GlobalEnv)
    })
}

message("Run make() to update the project\nRun tar_load_all() to load all built targets")
