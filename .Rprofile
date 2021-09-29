source("renv/activate.R")

library(targets)

make <- function(){
    job::job({{ targets::tar_make() }})
}
