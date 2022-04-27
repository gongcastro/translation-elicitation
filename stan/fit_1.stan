// generated with brms 2.16.1
functions {
 /* compute correlated group-level effects
  * Args: 
  *   z: matrix of unscaled group-level effects
  *   SD: vector of standard deviation parameters
  *   L: cholesky factor correlation matrix
  * Returns: 
  *   matrix of scaled group-level effects
  */ 
  matrix scale_r_cor(matrix z, vector SD, matrix L) {
    // r is stored in another dimension order than z
    return transpose(diag_pre_multiply(SD, L) * z);
  }
}
data {
  int<lower=1> N;  // total number of observations
  int Y[N];  // response variable
  int<lower=1> K;  // number of population-level effects
  matrix[N, K] X;  // population-level design matrix
  // data for group-level effects of ID 1
  int<lower=1> N_1;  // number of grouping levels
  int<lower=1> M_1;  // number of coefficients per level
  int<lower=1> J_1[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_1_1;
  vector[N] Z_1_2;
  int<lower=1> NC_1;  // number of group-level correlations
  // data for group-level effects of ID 2
  int<lower=1> N_2;  // number of grouping levels
  int<lower=1> M_2;  // number of coefficients per level
  int<lower=1> J_2[N];  // grouping indicator per observation
  // group-level predictor values
  vector[N] Z_2_1;
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
  vector<lower=0>[M_1] sd_1;  // group-level standard deviations
  matrix[M_1, N_1] z_1;  // standardized group-level effects
  cholesky_factor_corr[M_1] L_1;  // cholesky factor of correlation matrix
  vector<lower=0>[M_2] sd_2;  // group-level standard deviations
  vector[N_2] z_2[M_2];  // standardized group-level effects
}
transformed parameters {
  matrix[N_1, M_1] r_1;  // actual group-level effects
  // using vectors speeds up indexing in loops
  vector[N_1] r_1_1;
  vector[N_1] r_1_2;
  vector[N_2] r_2_1;  // actual group-level effects
  // compute actual group-level effects
  r_1 = scale_r_cor(z_1, sd_1, L_1);
  r_1_1 = r_1[, 1];
  r_1_2 = r_1[, 2];
  r_2_1 = (sd_2[1] * (z_2[1]));
}
model {
  // likelihood including constants
  if (!prior_only) {
    // initialize linear predictor term
    vector[N] mu = Intercept + rep_vector(0.0, N);
    for (n in 1:N) {
      // add more terms to the linear predictor
      mu[n] += r_1_1[J_1[n]] * Z_1_1[n] + r_1_2[J_1[n]] * Z_1_2[n] + r_2_1[J_2[n]] * Z_2_1[n];
    }
    target += bernoulli_logit_glm_lpmf(Y | Xc, mu, b);
  }
  // priors including constants
  target += normal_lpdf(b | 0, 0.1);
  target += normal_lpdf(Intercept | 0, 0.1);
  target += cauchy_lpdf(sd_1 | 0, 0.1)
    - 2 * cauchy_lccdf(0 | 0, 0.1);
  target += std_normal_lpdf(to_vector(z_1));
  target += lkj_corr_cholesky_lpdf(L_1 | 8);
  target += cauchy_lpdf(sd_2 | 0, 0.1)
    - 1 * cauchy_lccdf(0 | 0, 0.1);
  target += std_normal_lpdf(z_2[1]);
}
generated quantities {
  // actual population-level intercept
  real b_Intercept = Intercept - dot_product(means_X, b);
  // compute group-level correlations
  corr_matrix[M_1] Cor_1 = multiply_lower_tri_self_transpose(L_1);
  vector<lower=-1,upper=1>[NC_1] cor_1;
  // additionally sample draws from priors
  real prior_b = normal_rng(0,0.1);
  real prior_Intercept = normal_rng(0,0.1);
  real prior_sd_1 = cauchy_rng(0,0.1);
  real prior_cor_1 = lkj_corr_rng(M_1,8)[1, 2];
  real prior_sd_2 = cauchy_rng(0,0.1);
  // extract upper diagonal of correlation matrix
  for (k in 1:M_1) {
    for (j in 1:(k - 1)) {
      cor_1[choose(k - 1, 2) + j] = Cor_1[j, k];
    }
  }
  // use rejection sampling for truncated priors
  while (prior_sd_1 < 0) {
    prior_sd_1 = cauchy_rng(0,0.1);
  }
  while (prior_sd_2 < 0) {
    prior_sd_2 = cauchy_rng(0,0.1);
  }
}
