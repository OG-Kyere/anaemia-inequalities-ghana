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

## Primary results promoted to the main paper

The validated decomposition and community-level heterogeneity results are now presented in main Table III, panels A and B, respectively. Panel A uses 7,550 women and a complete-case Erreygers index of -0.058853; panel B reports the null (n = 7,557) and adjusted (n = 7,550) unweighted models. Numerical estimates are unchanged.
---

## Additional multilevel uncertainty

Approximate uncertainty:
- null-model ICC: 3.91%–4.84%;
- adjusted ICC: 2.82%–3.50%;
- null-model MOR: 1.42–1.48;
- adjusted MOR: 1.34–1.39.


These are approximate summaries carried forward from the earlier analysis, not design-based survey confidence intervals. They are not newly estimated here.
---

## BMI functional-form sensitivity (narrative)

The primary decomposition used linear and quadratic terms for continuous BMI. Earlier exploratory analyses using clinical BMI categories gave a similar substantive conclusion. The specification reported above is the reproducible primary analysis.

---

## Supplementary Figure S1

**Concentration curve for anaemia by household wealth rank.**


The curve plots the cumulative share of anaemia against the cumulative weighted population ranked from poorest to richest. The 45-degree line indicates equality. The curve lies predominantly above this line, indicating a disproportionate concentration of anaemia among poorer women. The Erreygers-corrected concentration index was -0.0589 (95% bootstrap CI -0.0924 to -0.0249).

**Alt text:** Line graph comparing the anaemia concentration curve with a diagonal equality line. The anaemia curve lies mostly above the equality line, showing that poorer women account for a larger share of anaemia than their population share.

Source: `figures/figure1_concentration_curve.svg`

---

## Supplementary Figure S2

**Wealth gradient in survey-weighted anaemia prevalence.**

Repository file: `figures/figure3_wealth_gradient.svg`.

---

## Supplementary Figure S3

**Decomposition of the Erreygers-corrected concentration index.**

Repository file: `figures/figure4_decomposition.svg`.

---

## Supplementary interpretation note

All decomposition percentages represent statistical contributions to observed socioeconomic inequality. They should not be interpreted as causal mediation effects.

Likewise, the inverse adjusted association between higher BMI categories and anaemia should not be interpreted as evidence that excess adiposity prevents anaemia.

## Supplementary Table S1. Overall Wald tests

| Factor | Wald chi-square | df | p-value |
|---|---:|---:|---:|
| Age group | 9.96 | 6 | 0.126 |
| Education | 0.44 | 3 | 0.933 |
| Wealth quintile | 1.36 | 4 | 0.852 |
| Residence | 0.19 | 1 | 0.663 |
| Pregnancy status | 26.65 | 1 | **<0.001** |
| Parity | 0.81 | 3 | 0.847 |
| BMI category | 35.47 | 3 | **<0.001** |
| Employment | 0.07 | 1 | 0.789 |
| Marital status | 4.15 | 5 | 0.529 |
| Region | 45.49 | 15 | **<0.001** |

## Multilevel estimator diagnostics

The multilevel models were not survey-weighted. The initial BFGS fit at gradient tolerance 1e-6 reported precision loss for the adjusted model. Both final fits converged with seed 20261008 and gradient tolerance 1e-5; their maximum absolute gradients were below that tolerance. Cluster variance, ICC, MOR and proportional change in variance were unchanged at the reported precision. The MAP/Laplace fit failed to converge and is included only as a diagnostic comparison. See `docs/real_data_validation_2026-10-09.md` and `docs/multilevel_reproducibility_validation.md`.
