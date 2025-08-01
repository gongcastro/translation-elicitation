FROM rocker/rstudio:4.3.3

# add system
RUN apt-get update && \
    apt-get install -y libxml2-dev \
    libglpk-dev \
    libgmp3-dev \
    build-essential \
    gfortran \
    gcc \
    g++ \
    make\
    pandoc \
    pandoc-citeproc \
    curl \
    gdebi-core \
    libssl-dev \
    libzmq3-dev \
    libpng-dev \
    libsodium-dev \
    ssh-askpass \
    ssh-askpass-gnome \
    default-libmysqlclient-dev \
    libmagick++-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libcurl4-openssl-dev

# copy the whole directory to /rstudio (working directory in Posit Cloud)
COPY . /home/rstudio/
WORKDIR /home/rstudio/

# install Quarto
RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN gdebi --non-interactive quarto-linux-amd64.deb
RUN rm /home/rstudio/quarto-linux-amd64.deb

# install and configure renv
RUN Rscript -e 'install.packages("remotes", repos = c(CRAN = "https://cloud.r-project.org"))'
RUN Rscript -e 'remotes::install_version("renv", version = "1.0.0", repos = c("https://rstudio.r-universe.dev", "https://cloud.r-project.org"))'
ENV RENV_PATHS_LIBRARY=renv/library
RUN Rscript -e 'renv::restore()'

# install basic R dependencies
RUN Rscript -e 'Sys.setenv(R_INSTALL_STAGED = FALSE)'
RUN Rscript -e 'install.packages("cli", repos = c("https://r-lib.r-universe.dev", "https://cloud.r-project.org"))'
RUN Rscript -e 'install.packages("targets", repos = c("https://ropensci.r-universe.dev", "https://cloud.r-project.org"))'

# install cmdstanr
RUN Rscript -e 'cmdstanr::install_cmdstan()'

# expose RStudio IDE on this port
# http://localhost:8787
EXPOSE 8787
