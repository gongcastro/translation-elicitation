# Model details

We fitted a Bayesian multilevel regression model using the R package
`brms` (Bürkner 2017), with correct responses (`correct`, 0 is incorrect
response, 1 if correct response) as the response variable with a
Bernoulli distribution and a logit link function. We modelled the
probability of an average participant providing a correct response,
conditional to a set of predictors (aka. fixed effects) and their
interactions:

-   PTHN (`pthn`, 0-Inf): number of phonological neighbours with higher
    frequency of the target word. Extracted from the CLEARPOND database.
    Standardised before entering the regression model.
-   Phonological similarity (`lv`, 0-1): Inverse Levenshtein distance
    between the IPA transcription of the presented word and its correct
    translation in the target language, calculated using the
    `stringdist` function of the `stringdist` package (van der
    Loo 2014). Standardised before entering the regression model.
-   Shared phonological onset (`onset`, Same/Different): Whether the
    presented and the target word share phonological onset, as judged by
    experimenters, and sum coded as *D**i**f**f**e**r**e**n**t* =  − 0.5
    and *S**a**m**e* =  + 0.5.

We added participants (`participants`) and as a grouping variable (aka.,
random effects), therefore adding participant-level adjustments to the
model. We specified random intercepts slopes for all fixed effects
within the `participant` grouping variable.

We performed multiple imputation via predictive mean matching using the
`mice` function of the `mice` package (Van Buuren and
Groothuis-Oudshoorn 2011) to impute missing values in the response
variable or the predictors.

The model was implemented using the following formula (`fit_3`):

$$ $$

The estimation of the model was performed using Bayesian inference via
Hamiltonian Monte-Carlo in Stan (Carpenter et al. 2017), with 4 chains,
2,000 iterations each (1,000 warm-ups iterations). The output of this
model is the approximated posterior distribution of all the parameters
estimated, therefore indicating the probability of each combination of
values of the parameters, conditional to the observed data.

We compared this (extended model) to other models dropping one predictor
at a time using Leave-one-out cross-validation (LOO-CV), using the `loo`
and `loo_compare` functions of the `brms` package. We compared our
extended model against the following models:

-   fit_0: `~ 1 + (1 | participant) + (1 | word)`
-   fit_1:
    `~ 1 + frequency_zipf + (1 + frequency_zipf | participant) + (1 | word)`
-   fit_2:
    `~ 1 + frequency_zipf + pthn + (1 + frequency_zipf + pthn | participant) + (1 | word)`
-   fit_3:
    `~ 1 + frequency_zipf + pthn + lv + (1 + frequency_zipf + pthn + lv | participant) + (1 | word)`
-   fit_4:
    `~ 1 + frequency_zipf + pthn + lv + pthn:lv + (1 + frequency_zipf + pthn + pthn:lv + lv | participant) + (1 | word)`
-   fit_5:
    `~ 1 + frequency_zipf + pthn + lv + pthn:lv + group + (1 + frequency_zipf + pthn + pthn:lv + lv | participant) + (1 | word)`
-   fit_6:
    `~ 1 + frequency_zipf + pthn + lv + pthn:lv + group + group:lv + (1 + frequency_zipf + pthn + pthn:lv + lv | participant) + (1 | word)`

# Model implementation

## Stan code

`stan stan_model // generated with brms 2.16.1 functions {  /* compute correlated group-level effects   * Args:    *   z: matrix of unscaled group-level effects   *   SD: vector of standard deviation parameters   *   L: cholesky factor correlation matrix   * Returns:    *   matrix of scaled group-level effects   */    matrix scale_r_cor(matrix z, vector SD, matrix L) {     // r is stored in another dimension order than z     return transpose(diag_pre_multiply(SD, L) * z);   } } data {   int<lower=1> N;  // total number of observations   int Y[N];  // response variable   int<lower=1> K;  // number of population-level effects   matrix[N, K] X;  // population-level design matrix   // data for group-level effects of ID 1   int<lower=1> N_1;  // number of grouping levels   int<lower=1> M_1;  // number of coefficients per level   int<lower=1> J_1[N];  // grouping indicator per observation   // group-level predictor values   vector[N] Z_1_1;   vector[N] Z_1_2;   vector[N] Z_1_3;   vector[N] Z_1_4;   vector[N] Z_1_5;   vector[N] Z_1_6;   vector[N] Z_1_7;   int<lower=1> NC_1;  // number of group-level correlations   // data for group-level effects of ID 2   int<lower=1> N_2;  // number of grouping levels   int<lower=1> M_2;  // number of coefficients per level   int<lower=1> J_2[N];  // grouping indicator per observation   // group-level predictor values   vector[N] Z_2_1;   int prior_only;  // should the likelihood be ignored? } transformed data {   int Kc = K - 1;   matrix[N, Kc] Xc;  // centered version of X without an intercept   vector[Kc] means_X;  // column means of X before centering   for (i in 2:K) {     means_X[i - 1] = mean(X[, i]);     Xc[, i - 1] = X[, i] - means_X[i - 1];   } } parameters {   vector[Kc] b;  // population-level effects   real Intercept;  // temporary intercept for centered predictors   vector<lower=0>[M_1] sd_1;  // group-level standard deviations   matrix[M_1, N_1] z_1;  // standardized group-level effects   cholesky_factor_corr[M_1] L_1;  // cholesky factor of correlation matrix   vector<lower=0>[M_2] sd_2;  // group-level standard deviations   vector[N_2] z_2[M_2];  // standardized group-level effects } transformed parameters {   matrix[N_1, M_1] r_1;  // actual group-level effects   // using vectors speeds up indexing in loops   vector[N_1] r_1_1;   vector[N_1] r_1_2;   vector[N_1] r_1_3;   vector[N_1] r_1_4;   vector[N_1] r_1_5;   vector[N_1] r_1_6;   vector[N_1] r_1_7;   vector[N_2] r_2_1;  // actual group-level effects   // compute actual group-level effects   r_1 = scale_r_cor(z_1, sd_1, L_1);   r_1_1 = r_1[, 1];   r_1_2 = r_1[, 2];   r_1_3 = r_1[, 3];   r_1_4 = r_1[, 4];   r_1_5 = r_1[, 5];   r_1_6 = r_1[, 6];   r_1_7 = r_1[, 7];   r_2_1 = (sd_2[1] * (z_2[1])); } model {   // likelihood including constants   if (!prior_only) {     // initialize linear predictor term     vector[N] mu = Intercept + rep_vector(0.0, N);     for (n in 1:N) {       // add more terms to the linear predictor       mu[n] += r_1_1[J_1[n]] * Z_1_1[n] + r_1_2[J_1[n]] * Z_1_2[n] + r_1_3[J_1[n]] * Z_1_3[n] + r_1_4[J_1[n]] * Z_1_4[n] + r_1_5[J_1[n]] * Z_1_5[n] + r_1_6[J_1[n]] * Z_1_6[n] + r_1_7[J_1[n]] * Z_1_7[n] + r_2_1[J_2[n]] * Z_2_1[n];     }     target += bernoulli_logit_glm_lpmf(Y | Xc, mu, b);   }   // priors including constants   target += normal_lpdf(b | 0, 0.1);   target += normal_lpdf(Intercept | 0, 0.1);   target += cauchy_lpdf(sd_1 | 0, 0.1)     - 7 * cauchy_lccdf(0 | 0, 0.1);   target += std_normal_lpdf(to_vector(z_1));   target += lkj_corr_cholesky_lpdf(L_1 | 8);   target += cauchy_lpdf(sd_2 | 0, 0.1)     - 1 * cauchy_lccdf(0 | 0, 0.1);   target += std_normal_lpdf(z_2[1]); } generated quantities {   // actual population-level intercept   real b_Intercept = Intercept - dot_product(means_X, b);   // compute group-level correlations   corr_matrix[M_1] Cor_1 = multiply_lower_tri_self_transpose(L_1);   vector<lower=-1,upper=1>[NC_1] cor_1;   // additionally sample draws from priors   real prior_b = normal_rng(0,0.1);   real prior_Intercept = normal_rng(0,0.1);   real prior_sd_1 = cauchy_rng(0,0.1);   real prior_cor_1 = lkj_corr_rng(M_1,8)[1, 2];   real prior_sd_2 = cauchy_rng(0,0.1);   // extract upper diagonal of correlation matrix   for (k in 1:M_1) {     for (j in 1:(k - 1)) {       cor_1[choose(k - 1, 2) + j] = Cor_1[j, k];     }   }   // use rejection sampling for truncated priors   while (prior_sd_1 < 0) {     prior_sd_1 = cauchy_rng(0,0.1);   }   while (prior_sd_2 < 0) {     prior_sd_2 = cauchy_rng(0,0.1);   } }`

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-burkner2017brms" class="csl-entry">

Bürkner, Paul-Christian. 2017. “Brms: An r Package for Bayesian
Multilevel Models Using Stan.” *Journal of Statistical Software* 80 (1):
1–28.

</div>

<div id="ref-carpenter2017stan" class="csl-entry">

Carpenter, Bob, Andrew Gelman, Matthew D Hoffman, Daniel Lee, Ben
Goodrich, Michael Betancourt, Marcus A Brubaker, Jiqiang Guo, Peter Li,
and Allen Riddell. 2017. “Stan: A Probabilistic Programming Language.”
*Grantee Submission* 76 (1): 1–32.

</div>

<div id="ref-carpenter2017stan" class="csl-entry">

———. 2017. “Stan: A Probabilistic Programming Language.” *Grantee
Submission* 76 (1): 1–32.

</div>

<div id="ref-van2011mice" class="csl-entry">

Van Buuren, Stef, and Karin Groothuis-Oudshoorn. 2011. “Mice:
Multivariate Imputation by Chained Equations in r.” *Journal of
Statistical Software* 45 (1): 1–67.

</div>

<div id="ref-van2011mice" class="csl-entry">

———. 2011. “Mice: Multivariate Imputation by Chained Equations in r.”
*Journal of Statistical Software* 45 (1): 1–67.

</div>

<div id="ref-loo2014stringdist" class="csl-entry">

van der Loo, M. P. J. 2014. “The Stringdist Package for Approximate
String Matching.” *The R Journal* 6: 111–22.
<https://CRAN.R-project.org/package=stringdist>.

</div>

</div>
