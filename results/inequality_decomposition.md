# Decomposition of Wealth-Related Anaemia Inequality

## Purpose

The Erreygers corrected concentration index for anaemia was decomposed to assess which measured characteristics contribute to the observed pro-poor concentration of anaemia.

The decomposition used a survey-weighted linear probability model because additive decomposition of the concentration index requires an additive outcome model. Wealth itself was used to rank women and was therefore not included as an explanatory determinant.

The model included age, years of education, residence, pregnancy status, parity, BMI, employment, and marital/union status. Age and BMI were modelled with linear and quadratic terms.

## Overall inequality

Erreygers corrected concentration index:

**E = -0.0589**

Negative values indicate that anaemia is disproportionately concentrated among poorer women.

## Point-estimate decomposition

| Domain | Absolute contribution to E | Contribution as % of total E |
|---|---:|---:|
| BMI / nutritional status | -0.0458 | **77.8%** |
| Education | -0.0102 | **17.3%** |
| Residence | -0.0038 | **6.5%** |
| Parity | -0.0032 | **5.5%** |
| Pregnancy status | -0.0022 | **3.7%** |
| Age | -0.0002 | 0.3% |
| Employment | +0.00003 | -0.04% |
| Marital/union status | +0.0013 | -2.3% |
| Residual / unexplained | +0.0051 | **-8.7%** |

The measured determinants jointly account for approximately **108.7%** of the observed concentration index. Contributions can sum to more than 100% when some terms act in the opposite direction and the residual offsets part of the explained inequality.

## Design-respecting bootstrap uncertainty

A stratified PSU bootstrap was used as a sensitivity analysis by resampling primary sampling units with replacement within DHS strata and retaining the original sampling weights.

Approximate 95% bootstrap intervals from 200 replicates:

| Domain | Point contribution | 95% bootstrap interval |
|---|---:|---:|
| BMI / nutritional status | -0.0458 | **-0.0592 to -0.0318** |
| Education | -0.0102 | -0.0316 to 0.0080 |
| Residence | -0.0038 | -0.0246 to 0.0164 |
| Pregnancy status | -0.0022 | -0.0047 to 0.0003 |
| Parity | -0.0032 | -0.0136 to 0.0097 |
| Age | -0.0002 | -0.0043 to 0.0034 |
| Employment | +0.00003 | -0.0007 to 0.0008 |
| Marital/union status | +0.0013 | -0.0024 to 0.0051 |
| Residual | +0.0051 | -0.0206 to 0.0303 |

The bootstrap interval for the BMI / nutritional-status contribution remains entirely below zero, whereas the intervals for the smaller domains are wider and include zero.

## Main interpretation

The dominant measured contributor is **BMI / nutritional status**. This contribution is robust both to bootstrap resampling and to alternative BMI parameterisation using clinical BMI categories.

Education is the second-largest point contribution, but its bootstrap interval is wide, so its magnitude should be interpreted cautiously.

The decomposition supports a pattern in which wealth-related anaemia inequality is expressed primarily through the unequal socioeconomic distribution of nutritional status, with smaller contributions from education, residence, parity, and pregnancy status.

## Important cautions

1. These are **statistical contributions**, not causal effects.
2. Decomposition results depend on model specification.
3. A large BMI contribution does not imply that higher BMI is protective in a causal sense.
4. Region is handled separately in the geographic and adjusted-regression analyses.
5. Bootstrap intervals are sensitivity estimates based on stratified PSU resampling and should be reported transparently as such.
