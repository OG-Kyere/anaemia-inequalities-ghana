# Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana

This repository holds the analysis, aggregate results, figures, and manuscript files for a study of anaemia inequalities among women aged 15–49 years in Ghana.

The main question is not only how common anaemia is, but **who carries more of the burden and where the differences persist**. The analysis therefore combines national prevalence estimation with socioeconomic inequality measures, adjusted regression, and community-level modelling.

## Data source

The study uses the **2022 Ghana Demographic and Health Survey (GDHS)**.

> **Important:** DHS microdata are restricted-use data and are **not** included here. Anyone reproducing the analysis must obtain independent access from The DHS Program.

## Analytic sample

- Full Ghana 2022 Individual Recode file: 15,014 women
- Women with a valid anaemia classification: 7,557
- Survey-weighted anaemia prevalence: 41.12%

## What the analysis covers

- complex-survey prevalence estimation
- concentration curve and Erreygers-corrected concentration index
- decomposition of wealth-related inequality
- survey-weighted logistic regression
- multilevel analysis of cluster-level heterogeneity
- geographic and sensitivity analyses

The concentration-index work asks whether anaemia is disproportionately concentrated among poorer women. The multilevel component asks a different question: how much variation remains between communities after measured individual and household characteristics are taken into account.

## Repository structure

```text
data/           Access instructions only; no restricted microdata
docs/           Protocol, statistical analysis plan, and audit notes
figures/        Aggregate publication figures
results/        Aggregate tables and model summaries
manuscript/     Manuscript development files
supplementary/  Supplementary methods and results
submission/     Journal-targeted submission materials
```

## Current status

The 9 October repair review is documented in `docs/repair_audit_2026-10-09.md`. Code and manuscript checks now distinguish working-file correctness from scientific validation and submission readiness. The historical DHS reruns below predate these repairs; updated-data exports still need authorized-data revalidation.


The descriptive, inequality, adjusted-regression, decomposition, and multilevel pipelines have been **validated by fresh local reruns against the authorized 2022 Ghana DHS IR file**. The regenerated sample sizes, prevalence estimate, concentration indices, adjusted odds ratios, 200-replicate decomposition bootstrap, and variational-Bayes community heterogeneity estimates reproduce the validated analysis.

A journal-targeted manuscript, supplementary package, and submission-asset exporter have been prepared for *Journal of Public Health* (Oxford University Press).

## Data governance

Raw DHS files, extracted row-level datasets, and derived row-level data must stay outside Git. The repository's `.gitignore` excludes the Ghana IR dataset, common statistical data formats, and downloaded Ghana DHS ZIP archives.

## Authors

**Gideon Ofosu Kyere**  
Kwame Nkrumah University of Science and Technology, Ghana

**Wilhemina Adoma Pels**  
Kwame Nkrumah University of Science and Technology, Ghana

**Prince Apaah**  
Kwame Nkrumah University of Science and Technology, Ghana

**Clement Acheampong**  
Kwame Nkrumah University of Science and Technology, Ghana

## Running checks

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python src/06_project_diagnostics.py
python tests/smoke_pipeline.py
```

The smoke test uses temporary synthetic data and does not validate Ghana DHS results. Continuous integration runs these same data-free checks.

The runner resolves scripts and output paths against the repository, so it can be launched from another directory. Core runs now include the full-sample concentration bootstrap. `--bootstrap-reps` applies to the core and extended runs; use the documented default 200 for a reproduction attempt, never the two-replicate smoke-test setting for scientific inference.

`submission/jph_main_manuscript.md` is the canonical working manuscript. `manuscript/full_manuscript.md` mirrors it; component drafts are historical. Numbering changes are documented in `submission/reference_numbering_map.json`.

## Remaining submission gates

- Confirm author contributions and final approval in `submission/author_confirmation.md`.
- Revalidate the updated pipeline with authorized data; resolve the full-sample bootstrap provenance and multilevel convergence issues described in the repair audit.
- Regenerate the empirical concentration curve and run `python src/05_prepare_submission_assets.py --require-reproduced` before journal submission. The ordinary exporter can create a clearly labelled preview from stored SVG points.
- Complete journal-format files, author positions/postal address and the official STROBE checklist. The earlier downloadable preprint uses an older reference order and must be rebuilt before submission.

## Real-data verification update — 9 October 2026

The authorized IR archive from the earlier conversation was located and reanalysed. The core point estimates, adjusted associations, decomposition share/intervals and multilevel summaries reproduce. The empirical curve was regenerated, and both final seeded multilevel fits converge at BFGS gradient tolerance 1e-5 without changing reported estimates. The faster PSU resampler preserves exact sampled rows and order. All 21 unit tests pass.

See `docs/real_data_validation_2026-10-09.md` for the current status; earlier “data unavailable” and outstanding-convergence notes above describe the prior review stage. The original inequality interval remains a provenance discrepancy. A documented full-sample 5,000-replicate interval is available but awaits approval under the numerical lock. Author roles and final approval are also unconfirmed. Keep this a draft until those decisions and the final file rebuild are completed.


## Update — 10 October 2026

The corresponding author approved the 5,000-replicate inequality interval (-0.0924 to -0.0249); it is now applied throughout the current manuscript and figures. Earlier pending-approval statements above describe the historical review stage. See `docs/approved_interval_update_2026-10-10.md`. Author contributions and final approval remain provisional.
