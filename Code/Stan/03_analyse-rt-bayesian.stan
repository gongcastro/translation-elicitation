// 03_analyse-rt-bayesian: Analyse RTs

data{
  int<lower=1> N; // number of data points
  real rt[N];     // reaction time
  real lev[N];    // Levenshtein distance
}

parameters{
  vector[2] beta;        // intercept and slope
  read<lower=0> sigma_e; // error sd
}

model{
  real mu;
  for (i in 1:N) {
    mu <- beta[1] + beta[2]*lev[i];
    rt[i] ~ lognormal(mu, sigma_e);
  }
}