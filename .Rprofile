source("renv/activate.R")

library(targets)

make <- function(){
    job::job(
        title = "Translation Elicitation", {{ 
            targets::tar_make() 
        }}
    )
}

message("Run make() to update the project")
