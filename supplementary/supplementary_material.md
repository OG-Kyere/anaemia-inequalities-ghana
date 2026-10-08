# Supplementary Material

## Supplementary Methods

### Survey design

All descriptive prevalence and survey-weighted regression analyses incorporated the DHS individual women's sampling weight, primary sampling unit, and sampling stratum. The individual sampling weight was calculated as `v005 / 1,000,000`.

### Wealth-related inequality

Women were ranked from lowest to highest socioeconomic position using the continuous DHS household wealth score. The Erreygers-corrected concentration index was used as the primary inequality measure because anaemia was binary and bounded.

Uncertainty in the corrected concentration index and decomposition estimates was examined using stratified primary-sampling-unit bootstrap resampling.

### Decomposition

The decomposition used an additive survey-weighted linear probability model. Wealth was used to construct the socioeconomic ranking and was not entered as an explanatory determinant.

The primary decomposition included:
- age;
- education;
- residence;
- pregnancy status;
- parity;
- BMI;
- employment;
- marital/union status.

BMI and age were entered using linear and quadratic terms in the primary specification.

### Multilevel analysis

Women were nested within DHS clusters. Random-intercept logistic models were used to quantify between-cluster heterogeneity.

The intraclass correlation coefficient was calculated using the latent-variable approximation:

[
ICC=rac{sigma_u^2}{sigma_u^2+pi^2/3}.
]

The median odds ratio was used to express cluster heterogeneity on the odds-ratio scale.

---

## Supplementary Table S1. Decomposition of wealth-related inequality

| Domain | Absolute contribution | % of observed Erreygers index | 95% bootstrap interval |
|---|---:|---:|---:|
| BMI / nutritional status | -0.0458 | 77.8% | -0.0592 to -0.0318 |
| Education | -0.0102 | 17.3% | -0.0316 to 0.0080 |
| Residence | -0.0038 | 6.5% | -0.0246 to 0.0164 |
| Parity | -0.0032 | 5.5% | -0.0136 to 0.0097 |
| Pregnancy status | -0.0022 | 3.7% | -0.0047 to 0.0003 |
| Age | -0.0002 | 0.3% | -0.0043 to 0.0034 |
| Employment | +0.00003 | -0.04% | -0.0007 to 0.0008 |
| Marital/union status | +0.0013 | -2.3% | -0.0024 to 0.0051 |
| Residual | +0.0051 | -8.7% | -0.0206 to 0.0303 |

The measured components sum to more than 100% because some terms act in the opposite direction and the residual offsets part of the explained inequality.

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

## Supplementary Table S3. BMI functional-form sensitivity

The primary decomposition model treated BMI using linear and quadratic terms.

When BMI was represented using clinical categories instead:
- BMI-domain contribution to the Erreygers index: **-0.0430**;
- proportion of observed inequality attributed to BMI domain: **73.1%**.

The result was similar to the primary specification (77.8%), suggesting that the large BMI contribution was not solely due to the chosen functional form.

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
