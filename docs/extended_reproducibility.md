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

This adds the primary decomposition and a 200-replicate stratified PSU bootstrap.

For a quicker test:

```bash
python run_analysis.py --extended --bootstrap-reps 20
```

Expected locked point contributions:

| Domain | Locked contribution |
|---|---:|
| BMI / nutritional status | -0.0458 |
| Education | -0.0102 |
| Residence | -0.0038 |
| Parity | -0.0032 |
| Pregnancy status | -0.0022 |
| Age | -0.0002 |
| Employment | +0.00003 |
| Marital/union status | +0.0013 |
| Residual | +0.0051 |

Expected 200-replicate bootstrap interval for BMI contribution:
**-0.0592 to -0.0318**.

Expected bootstrap interval for the Erreygers index:
**-0.0914 to -0.0212**.

## Multilevel community model

Run the MAP/Laplace implementation:

```bash
python run_analysis.py --multilevel
```

Or variational Bayes:

```bash
python run_analysis.py --multilevel --multilevel-method vb
```

Locked heterogeneity values used in the manuscript:

| Model | SD | Variance | ICC | MOR |
|---|---:|---:|---:|---:|
| Null | 0.387 | 0.150 | 4.35% | 1.45 |
| Adjusted | 0.327 | 0.107 | 3.14% | 1.37 |

Locked proportional change in variance: **28.8%**.

### Important validation rule

Do not replace the locked multilevel manuscript values merely because another
estimator produces different numbers. First establish whether the new executable
implementation uses the same estimator, likelihood approximation, priors, and
covariate coding as the original analysis.

If MAP and VB do not reproduce the locked estimates closely, record the discrepancy
and align the executable implementation with the original estimator before changing
the manuscript.
