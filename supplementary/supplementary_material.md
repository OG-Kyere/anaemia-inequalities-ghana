# Supplementary Material

## Supplementary Methods

### Survey design

All descriptive prevalence and survey-weighted regression analyses incorporated the DHS individual women's sampling weight, primary sampling unit, and sampling stratum. The individual sampling weight was calculated as `v005 / 1,000,000`.

### Wealth-related inequality

Women were ranked from lowest to highest socioeconomic position using the continuous DHS household wealth score. The Erreygers-corrected concentration index was used as the primary inequality measure because anaemia was binary and bounded.

Uncertainty in the corrected concentration index and decomposition estimates was examined using stratified primary-sampling-unit bootstrap resampling.

### Decomposition

The decomposition used an additive survey-weighted linear probability model. Wealth was used to construct the socioeconomic ranking and was not entered as an explanatory determinant.

The reproducible decomposition included:
- DHS five-year age-group indicators;
- years of schooling;
- residence;
- pregnancy status;
- continuous parity;
- BMI;
- employment;
- current union status.

BMI was entered using linear and quadratic terms. Wealth was used only to rank women.

### Multilevel analysis

Women were nested within DHS clusters. Random-intercept logistic models were used to quantify between-cluster heterogeneity.

The intraclass correlation coefficient was calculated using the latent-variable approximation:

\[
ICC=\frac{\sigma_u^2}{\sigma_u^2+\pi^2/3}.
\]

The median odds ratio was used to express cluster heterogeneity on the odds-ratio scale.

---

## Supplementary Table S1. Decomposition of wealth-related inequality

| Domain | Absolute contribution | % of observed Erreygers index | 95% bootstrap interval |
|---|---:|---:|---:|
| BMI / nutritional status | -0.045731 | 77.7% | -0.061716 to -0.030045 |
| Education | -0.009184 | 15.6% | -0.025104 to 0.006950 |
| Residence | -0.004023 | 6.8% | -0.023362 to 0.013460 |
| Parity | -0.002892 | 4.9% | -0.014688 to 0.009773 |
| Pregnancy status | -0.002221 | 3.8% | -0.005493 to 0.000020 |
| Age | +0.000570 | -1.0% | -0.003250 to 0.004169 |
| Employment | +0.000021 | -0.04% | -0.000592 to 0.000687 |
| Marital/union status | +0.001203 | -2.0% | -0.002581 to 0.005772 |
| Residual | +0.003405 | -5.8% | -0.017297 to 0.025089 |

The decomposition uses 7,550 BMI-complete women and a complete-case Erreygers index of -0.058853. The percentages are relative to that negative index, so positive contributions appear as negative percentages and offset part of the measured pro-poor inequality.

---

## Supplementary Table S2. Community-level heterogeneity

| Measure | Null model | Adjusted model |
|---|---:|---:|
| Cluster-level SD | 0.387 | 0.327 |
| Cluster-level variance | 0.150 | 0.107 |
| ICC | 4.35% | 3.14% |
| Median odds ratio | 1.45 | 1.37 |
| Proportional change in variance | — | 28.8% |

Approximate uncertainty:
- null-model ICC: 3.91%–4.84%;
- adjusted ICC: 2.82%–3.50%;
- null-model MOR: 1.42–1.48;
- adjusted MOR: 1.34–1.39.

---

## BMI functional-form sensitivity (narrative)

The primary decomposition model treated BMI using linear and quadratic terms.

The principal executable decomposition uses continuous BMI with a quadratic term. Earlier exploratory work with clinical BMI categories gave a similar substantive conclusion, but the fully reproducible specification reported above should be used for the final manuscript and supplementary tables.

---

## Supplementary Figure S1

**Wealth gradient in survey-weighted anaemia prevalence.**

Repository file: `figures/figure3_wealth_gradient.svg`.

---

## Supplementary Figure S2

**Decomposition of the Erreygers-corrected concentration index.**

Repository file: `figures/figure4_decomposition.svg`.

---

## Supplementary interpretation note

All decomposition percentages represent statistical contributions to observed socioeconomic inequality. They should not be interpreted as causal mediation effects.

Likewise, the inverse adjusted association between higher BMI categories and anaemia should not be interpreted as evidence that excess adiposity prevents anaemia.

## Supplementary Table S3. Overall Wald tests

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

The multilevel models were not survey-weighted. Variational Bayes reproduced the stored estimates, but the optimizer emitted a convergence warning. Matching stored values does not establish convergence. The MAP/Laplace fit failed to converge and is diagnostic only. See `docs/multilevel_reproducibility_validation.md`.
