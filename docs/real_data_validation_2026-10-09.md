# Real-data verification — 9 October 2026

The previously attached Ghana 2022 Individual Recode archive was located and analysed locally. Microdata were extracted outside the repository and are not included in changes, logs or deliverables. The source-file checksum and aggregate comparisons are in `real_data_validation_2026-10-09.json`.

## Reproduced results

- Valid anaemia sample: 7,557; BMI-complete sample: 7,550.
- Weighted prevalence: 41.122474%; Taylor CI: 39.605026% to 42.639923%. The one-decimal manuscript presentation (41.1%, 39.6–42.6%) matches. At two decimals, the lower bound conventionally rounds to 39.61%; the historical 39.60% value was retained pending the numerical lock.
- Standard concentration index: -0.0358307533; Erreygers index: -0.0589379693.
- Pregnancy, overweight, obesity, Bono and Oti adjusted odds ratios and confidence limits match the locked two-decimal values.
- BMI decomposition share: 77.704803%; absolute contribution: -0.045731. Its 200-replicate confidence interval reproduces -0.061716 to -0.030045. The other recorded domain intervals also reproduce.
- Baseline null/adjusted ICC, MOR, variance and PCV match the manuscript. The null optimizer reported success; the adjusted BFGS run reported precision loss. The final seeded BFGS fits (seed 20261008, gradient tolerance 1e-5) both converged, with maximum absolute gradients below 1e-5. Their reported ICC, MOR, variance and PCV remain unchanged. The stricter 1e-6 precision-loss diagnostic remains recorded.
- The stored decile curve checkpoints match the empirical rerun at the displayed precision. The source SVG now uses a finer 101-point empirical population-share grid, with no individual identifiers or wealth scores exported.

## Inequality-bootstrap discrepancy

The locked CI is -0.0914 to -0.0212. The preserved complete-case 200-replicate output in the author's existing checkout also gives -0.089667 to -0.023481, not the locked CI. It is therefore not justified to claim that the locked CI came from that complete-case run.

The full-sample stratified PSU percentile bootstrap, seed 20261008, gives:

| Replicates | 95% CI lower | 95% CI upper |
|---:|---:|---:|
| 200 | -0.088845 | -0.022368 |
| 1,000 | -0.090551 | -0.024057 |
| 5,000 | -0.092372 | -0.024942 |

The original interval's precise settings/provenance are not preserved. This could reflect different seeds, replicate counts or an alternative implementation; none should be invented. All checked intervals remain negative, so the direction of inequality is unchanged. A documented 5,000-replicate interval is available for an author-approved correction; the manuscript's locked numbers have not been silently replaced.

## Software verification

The faster bootstrap resampler is tested against the original implementation for exact sampled rows, identifiers and order under ten seeds. All 21 unit tests pass. Domain bootstrap values reproduce the historical outputs. Empty dependency namespaces are now reported as incomplete installations rather than successful imports.

## Remaining decisions

Confirm the inequality interval before updating the manuscript and figure annotation; confirm author roles/approval; then rebuild the Overleaf/preprint and journal-upload versions from the updated source.

## Reproduction commands and environment

The revalidation used Python 3.12 and the package versions in `requirements-validation.txt`. Use the documented authorized local IR file via `DHS_IR_PATH`; no microdata are distributed.

```bash
python -m pip install -r requirements-validation.txt
python run_analysis.py --multilevel --bootstrap-reps 200 --inequality-bootstrap-reps 5000
python src/06_project_diagnostics.py
```

The option for full-sample inequality replicates is separate from the decomposition replicate count. Keeping the decomposition at 200 reproduces its locked intervals; the 5,000-replicate full-sample interval is a proposed correction pending author approval, not a silent replacement of the manuscript interval. The 5,000-replicate computation was run separately during this audit; the full pipeline's saved core bootstrap table records its original 200-replicate run.
