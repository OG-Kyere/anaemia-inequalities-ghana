# Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana

This repository contains the reproducible workflow, aggregate results, figures, and manuscript materials for a biostatistics study of socioeconomic and geographic inequalities in anaemia among women aged 15–49 years in Ghana.

## Study aim

The project quantifies wealth-related inequality in anaemia, identifies measured contributors to observed disparities, estimates adjusted associations, and assesses geographic and community-level heterogeneity.

## Data source

The analysis uses the **2022 Ghana Demographic and Health Survey (GDHS)**.

> **Important:** DHS microdata are restricted-use data and are **not** included in this repository. Reproduction requires independent authorization from The DHS Program.

## Analytic sample

- Full Ghana 2022 Individual Recode file: 15,014 women
- Women with valid anaemia classification: 7,557
- Survey-weighted anaemia prevalence: 41.12%

## Analyses

- complex-survey prevalence estimation
- concentration curve and Erreygers-corrected concentration index
- decomposition of wealth-related inequality
- survey-weighted logistic regression
- multilevel cluster-heterogeneity analysis
- geographic and sensitivity analyses

## Repository structure

```
data/           Access instructions only; no restricted microdata
docs/           Protocol, statistical analysis plan, audits
figures/        Aggregate publication figures
results/        Aggregate tables and model summaries
manuscript/     Manuscript development files
supplementary/  Supplementary methods and results
submission/     Journal-targeted submission materials
```

## Current status

Core analyses are complete. A journal-targeted manuscript and supplementary package have been prepared for *Journal of Public Health* (Oxford University Press). Final submission tasks include inserting the corresponding author's email, final journal formatting, and a clean-environment reproducibility run.

## Data governance

Raw DHS files, extracted row-level datasets, and derived row-level data must remain outside Git. The repository's `.gitignore` explicitly excludes the Ghana IR dataset and downloaded DHS ZIP archives.

## Author

Gideon Ofosu Kyere  
Kwame Nkrumah University of Science and Technology, Ghana
