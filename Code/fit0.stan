// generated with brms 2.13.0
functions {

  /* zero-one-inflated beta log-PDF of a single response 
   * Args: 
   *   y: response value 
   *   mu: mean parameter of the beta part
   *   phi: precision parameter of the beta part
   *   zoi: zero-one-inflation probability
   *   coi: conditional one-inflation probability
   * Returns:  
   *   a scalar to be added to the log posterior 
   */ 
   real zero_one_inflated_beta_lpdf(real y, real mu, real phi,
                                    real zoi, real coi) {
     row_vector[2] shape = [mu * phi, (1 - mu) * phi]; 
     if (y == 0) { 
       return bernoulli_lpmf(1 | zoi) + bernoulli_lpmf(0 | coi); 
     } else if (y == 1) {
       return bernoulli_lpmf(1 | zoi) + bernoulli_lpmf(1 | coi);
     } else { 
       return bernoulli_lpmf(0 | zoi) + beta_lpdf(y | shape[1], shape[2]);
     } 
   }
}
data {
  int<lower=1> N;  // number of observations
  vector[N] Y;  // response variable
  int<lower=1> K;  // number of population-level effects
  matrix[N, K] X;  // population-level design matrix
  // data for group-level effects of ID 1
  int<lower=1> N_1;  // number of grouping levels
  int<lower=1> M_1;  // number of coefficients per level
  int<lower=1> J_1[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_1_1;
  int prior_only;  // should the likelihood be ignored?
}
transformed data {
  int Kc = K - 1;
  matrix[N, Kc] Xc;  // centered version of X without an intercept
  vector[Kc] means_X;  // column means of X before centering
  for (i in 2:K) {
    means_X[i - 1] = mean(X[, i]);
    Xc[, i - 1] = X[, i] - means_X[i - 1];
  }
}
parameters {
  vector[Kc] b;  // population-level effects
  real Intercept;  // temporary intercept for centered predictors
  real<lower=0> phi;  // precision parameter
  real<lower=0,upper=1> zoi;  // zero-one-inflation probability
  real<lower=0,upper=1> coi;  // conditional one-inflation probability
  vector<lower=0>[M_1] sd_1;  // group-level standard deviations
  vector[N_1] z_1[M_1];  // standardized group-level effects
}
transformed parameters {
  vector[N_1] r_1_1;  // actual group-level effects
  r_1_1 = (sd_1[1] * (z_1[1]));
}
model {
  // initialize linear predictor term
  vector[N] mu = Intercept + Xc * b;
  for (n in 1:N) {
    // add more terms to the linear predictor
    mu[n] += r_1_1[J_1[n]] * Z_1_1[n];
  }
  for (n in 1:N) {
    // apply the inverse link function
    mu[n] = inv_logit(mu[n]);
  }
  // priors including all constants
  target += normal_lpdf(b | 0, 1);
  target += lognormal_lpdf(Intercept | 0.15, 0.2);
  target += normal_lpdf(phi | 1.5, 1)
    - 1 * normal_lccdf(0 | 1.5, 1);
  target += beta_lpdf(zoi | 10, 10);
  target += beta_lpdf(coi | 10, 10);
  target += cauchy_lpdf(sd_1 | 0, 5)
    - 1 * cauchy_lccdf(0 | 0, 5);
  target += std_normal_lpdf(z_1[1]);
  // likelihood including all constants
  if (!prior_only) {
    for (n in 1:N) {
      target += zero_one_inflated_beta_lpdf(Y[n] | mu[n], phi, zoi, coi);
    }
  }
}
generated quantities {
  // actual population-level intercept
  real b_Intercept = Intercept - dot_product(means_X, b);
}
