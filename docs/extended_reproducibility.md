# Extended Reproducibility Runs

The validated core pipeline is:

```bash
python run_analysis.py
```

## Inequality decomposition and bootstrap

Run:

```bash
python run_analysis.py --extended
```

This adds the reproducible decomposition and a 200-replicate stratified PSU bootstrap.

The executable decomposition specification uses DHS age-group indicators, years of
schooling, rural residence, pregnancy status, continuous parity, BMI plus BMI squared,
employment, and current union status.

The validated 200-replicate BMI contribution was **-0.045731** with bootstrap interval
**-0.061716 to -0.030045**.

See `docs/decomposition_reproducibility_validation.md` for the full comparison with
the earlier locked decomposition table.

## Multilevel community model

The reproducibility estimator is **variational Bayes (VB)**:

```bash
python run_analysis.py --multilevel
```

The validated VB run reproduced the locked heterogeneity values almost exactly:

| Model | SD | Variance | ICC | MOR |
|---|---:|---:|---:|---:|
| Null | 0.386982 | 0.149755 | 4.3538% | 1.4465 |
| Adjusted | 0.326441 | 0.106564 | 3.1375% | 1.3653 |

Proportional change in variance: **28.8411%**.

These agree with the rounded manuscript values of SD 0.387/0.327, variance 0.150/0.107,
ICC 4.35%/3.14%, MOR 1.45/1.37, and PCV 28.8%.

### Numerical warning

`statsmodels` emitted a VB convergence warning during the validation run, even though
the reproduced variance components matched the locked results almost exactly. This
warning is part of the reproducibility record and should not be hidden.

The MAP/Laplace implementation is available only as a diagnostic:

```bash
python src/04_multilevel_heterogeneity.py --method map
```

In validation, MAP failed to converge and collapsed the random-effect variance toward
zero, so it should not be used to reproduce the manuscript heterogeneity estimates.
