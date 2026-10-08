# Manuscript Consistency Audit

## Status

**Reproducibility and numerical consistency: PASS, with one documented estimator warning**

The manuscript, result tables, figures, and executable scripts were checked against fresh reruns using the authorized 2022 Ghana DHS IR file.

## Validated core numbers

| Quantity | Validated value |
|---|---:|
| Full IR sample | 15,014 |
| Valid anaemia sample | 7,557 |
| Complete adjusted-model sample | 7,550 |
| Overall weighted prevalence | 41.12% |
| Overall 95% CI | 39.60%–42.64% |
| Standard concentration index | -0.035831 |
| Erreygers concentration index | -0.058938 |
| Pregnancy aOR | 1.77 |
| Overweight aOR | 0.73 |
| Obesity aOR | 0.60 |
| Oti aOR | 1.48 |
| Bono aOR | 0.61 |

## Validated decomposition

The final executable decomposition uses DHS age-group indicators, years of schooling, residence, pregnancy status, continuous parity, BMI plus BMI squared, employment, and current union status.

| Domain | Point contribution | 95% bootstrap interval |
|---|---:|---:|
| BMI / nutritional status | -0.045731 | -0.061716 to -0.030045 |
| Education | -0.009184 | -0.025104 to 0.006950 |
| Residence | -0.004023 | -0.023362 to 0.013460 |
| Parity | -0.002892 | -0.014688 to 0.009773 |
| Pregnancy status | -0.002221 | -0.005493 to 0.000020 |
| Age | +0.000570 | -0.003250 to 0.004169 |
| Employment | +0.000021 | -0.000592 to 0.000687 |
| Marital/union status | +0.001203 | -0.002581 to 0.005772 |
| Residual | +0.003405 | -0.017297 to 0.025089 |

The BMI contribution is 77.7% of the observed Erreygers index in the complete-case decomposition sample.

## Validated multilevel heterogeneity

The variational-Bayes implementation reproduced the stored cluster-level heterogeneity estimates:

| Measure | Null model | Adjusted model |
|---|---:|---:|
| Cluster SD | 0.386982 | 0.326441 |
| Cluster variance | 0.149755 | 0.106564 |
| ICC | 4.3538% | 3.1375% |
| MOR | 1.4465 | 1.3653 |
| PCV | — | 28.8411% |

The MAP/Laplace implementation failed to converge and is diagnostic only. `statsmodels` emitted a VB convergence warning, but the reproduced heterogeneity quantities matched the stored results to the reported precision. That warning is retained in the reproducibility record.

## Cross-file checks

- Abstract and Results use the validated prevalence, inequality, and decomposition summary.
- Table 1 and Table 2 remain consistent with the validated survey-weighted results.
- Supplementary Table S1 uses the validated 200-replicate decomposition.
- Supplementary Table S2 uses the validated VB heterogeneity estimates.
- Figure 4 has been regenerated to use the validated decomposition values.
- Interpretation remains non-causal throughout.

## Remaining submission items

1. Insert the final corresponding-author email.
2. Confirm final author list and ORCID placement.
3. Export editable journal tables and publication-resolution figures.
4. Run final journal formatting and reference verification.
5. Include the AI-use disclosure exactly as required by the target journal.

## Interpretation guardrails

- Do not call the anaemia outcome iron-deficiency anaemia.
- Do not state that overweight or obesity protects against anaemia.
- Do not describe decomposition percentages as causal mediation.
- Do not infer individual-level effects from the concentration index.
- Do not claim geographic causation from regional associations.
- Do not upload raw or row-level DHS data to GitHub.
