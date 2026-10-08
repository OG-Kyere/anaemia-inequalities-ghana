# Multilevel Reproducibility Validation

Date validated: **2026-10-08**

Two estimators were tested for the two-level random-intercept logistic models.

## MAP / Laplace

The MAP/Laplace fit failed to converge for both the null and adjusted models. The
estimated cluster standard deviations collapsed toward zero, producing ICCs near zero
and MORs of 1.0. These estimates do not reproduce the stored analysis and are not used
for manuscript replication.

## Variational Bayes

The variational-Bayes implementation reproduced the locked heterogeneity measures
almost exactly.

| Quantity | Reproduced VB | Locked rounded value | Status |
|---|---:|---:|---|
| Null cluster SD | 0.386982 | 0.387 | PASS |
| Null variance | 0.149755 | 0.150 | PASS |
| Null ICC | 0.043538 | 0.0435 | PASS |
| Null MOR | 1.446477 | 1.45 | PASS |
| Adjusted cluster SD | 0.326441 | 0.327 | PASS |
| Adjusted variance | 0.106564 | 0.107 | PASS |
| Adjusted ICC | 0.031375 | 0.0314 | PASS |
| Adjusted MOR | 1.365312 | 1.37 | PASS |
| PCV | 0.288411 | 0.288 | PASS |

Null-model sample: **7,557**.

Adjusted-model sample: **7,550**.

## Numerical warning

`statsmodels` emitted a `ConvergenceWarning` for the VB optimizer. The warning is
retained in the reproducibility record. Despite it, the variance-component estimates
replicated the previously stored results to the reported precision.

Accordingly, VB is the reproducibility estimator for the manuscript's cluster-level
heterogeneity measures, while MAP is retained only as a diagnostic comparison.
