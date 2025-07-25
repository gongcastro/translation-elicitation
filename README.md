
# Translation Elicitation

More info in the Open Science Framework repository.

## How to make this repository work on your local machine

There are two possibilities to reproduce the computational environment of this study: (a) Using the Docker image (recommended), (b) manual setup.

### Docker setup

1) Install [Docker Desktop](https://www.docker.com/) in your local machine. (You may have to restart your machine after installation).
2) Open Docker Desktop. In the search bar (Ctrl+K or cmd+K), search `gongcastro/translation-elicitation` and click "Run".
4) Open a terminal and run the following command:

```bash
docker run --rm -ti \
    -e ROOT=true \
    -e PASSWORD=rstudio \
    -p 8787:8787 \
    --name rstudio gongcastro/translation-elicitation:latest
```
5) Open a browser and navigate to [http://localhost:8787](http://localhost:8787). A login page will show up. Use "rstudio" as username and password.
6) After login, you will see an RStudio session in which you can run `make()` to run the code and get all outputs.

### Manual setup

#### 1. Downloading the repository

You can either download the project as a .zip file by clocking on the green button that says "Code", or if you feel comfortable with Git, you can clone the repository from your console running:

``` bash
git clone https://github.com/gongcastro/translation-elicitation.git
```

#### 2. Install R dependencies with renv

You will need to install [R 4.3.3](https://cran.r-project.org/bin/windows/base/old/4.3.3/). Other versions of R may work, but have not been tested in the present project.

We used the R package [renv](https://rstudio.github.io/renv/articles/renv.html) to keep track of the dependencies of the project. renv allows to install and update the R packages necessary to run the project in a project-specific environment. Packages installed using renv in this project will only be installed or updated in the context of this project. The R packages you had installed for other projects will remain unaffected.

1. Open the repository folder in a new window (if using Positron) or as a new project (if using RStudio).
2. In the R console, run the following lines of code:

``` r
# install.packages("renv") # in case yopu need to install renv
renv::activate() # this will create the renv infrastructure if missing
renv::restore() # this will install/update/move the necessary R pakcages into this project
```

#### 3. Running the code with targets

We use the R package [targets](https://books.ropensci.org/targets/) to keep track of what code should be run, and in what order. The `_targets.R` script contains the main commands in the workflow. Each command is indicated inside of a call to the `tar_target()` function, and is called a *target*. For readability, we have defined most of the functions used inside the targets on separate scripts, hosted in the "scripts" folder of the project. To run the code, run the following command in your R console:

```r
targets::tar_make()
```

Once targets have run, you can import the generated objects using the `tar_load()` function. For instance, `tar_load(dataset_1)` and `tar_load(exp_1_m0)` will load the model from main dataset and model of Experiment 1. 


## How is this repository organised?

This repository is organised as follows:

- **assets**: Psychopy code used to implement the experimental tasks of Experiments 1, 2, and 3.
    + Version for **Spanish speakers**: [https://gitlab.pavlovia.org/gongcastro/translationelicitationspa](https://gitlab.pavlovia.org/gongcastro/translationelicitationspa>).
    + Version for **English speakers**: [https://gitlab.pavlovia.org/SiowSerene/translationelicitation_eng](https://gitlab.pavlovia.org/SiowSerene/translationelicitation_eng).
- **data**: raw and processed data from the behavioural task in Experiments 1, 2, and 3.
- **docs**: Quarto documents for the manuscript and appendix.
- **out**: outputs of the models and manuscript-ready datasets to make figures and tables.
- **scripts**: R code used to process and analyse the data.
- **sounds**: audios used in the behavioural task.


