# Supplementary material

## Supplementary Methods

### Survey design

Descriptive prevalence and survey-weighted regression analyses incorporated the DHS individual women's sampling weight, primary sampling unit and sampling stratum. The individual sampling weight was calculated as `v005 / 1,000,000`.

### Wealth-related inequality

Women were ranked from lowest to highest socioeconomic position using the continuous DHS household wealth score. The Erreygers-corrected concentration index was used as the primary inequality measure because anaemia was binary and bounded.

Uncertainty was examined using stratified primary-sampling-unit bootstrap resampling: 5,000 replicates for the full-sample corrected concentration index and 200 for the decomposition (seed 20261008). The full-sample percentile 95% interval was -0.0924 to -0.0249.

### Decomposition

The decomposition used an additive survey-weighted linear probability model. Wealth was used to construct the socioeconomic ranking and was not entered as an explanatory determinant.

The decomposition model included:
- DHS five-year age-group indicators;
- years of schooling;
- residence;
- pregnancy status;
- continuous parity;
- BMI;
- employment;
- current union status.

BMI was entered using linear and quadratic terms.

### Multilevel analysis

Women were nested within DHS clusters. Random-intercept logistic models were used to quantify between-cluster heterogeneity.

The intraclass correlation coefficient was calculated using the latent-variable approximation:

\[
ICC=\frac{\sigma_u^2}{\sigma_u^2+\pi^2/3}.
\]

The median odds ratio was used to express cluster heterogeneity on the odds-ratio scale.

---

## Main-paper results

All four results tables and all four figures are included in the main manuscript. This supplement retains supporting methodology, approximate multilevel uncertainty and estimator diagnostics.

## Additional multilevel uncertainty

Approximate uncertainty:
- null-model ICC: 3.91%–4.84%;
- adjusted ICC: 2.82%–3.50%;
- null-model MOR: 1.42–1.48;
- adjusted MOR: 1.34–1.39.


These approximate uncertainty summaries are distinct from design-based survey confidence intervals.
---

## BMI functional-form sensitivity (narrative)

The primary decomposition used linear and quadratic terms for continuous BMI. Earlier exploratory analyses using clinical BMI categories gave a similar substantive conclusion. The specification reported above is the reproducible primary analysis.

---




## Supplementary interpretation note

All decomposition percentages represent statistical contributions to observed socioeconomic inequality. They should not be interpreted as causal mediation effects.

Likewise, the inverse adjusted association between higher BMI categories and anaemia should not be interpreted as evidence that excess adiposity prevents anaemia.


## Multilevel estimator diagnostics

The multilevel models were not survey-weighted. The initial BFGS fit at gradient tolerance 1e-6 reported precision loss for the adjusted model. Both final fits converged with seed 20261008 and gradient tolerance 1e-5; their maximum absolute gradients were below that tolerance. Cluster variance, ICC, MOR and proportional change in variance were unchanged at the reported precision. The MAP/Laplace fit failed to converge and is included only as a diagnostic comparison. See `docs/real_data_validation_2026-10-09.md` and `docs/multilevel_reproducibility_validation.md`.
