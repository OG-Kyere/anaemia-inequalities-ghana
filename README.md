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

\`\`\`text
data/           Access instructions only; no restricted microdata
docs/           Protocol, statistical analysis plan, and audit notes
figures/        Aggregate publication figures
results/        Aggregate tables and model summaries
manuscript/     Manuscript development files
supplementary/  Supplementary methods and results
submission/     Journal-targeted submission materials
\`\`\`

## Current status

The descriptive, inequality, adjusted-regression, decomposition, and multilevel pipelines have been **validated by fresh local reruns against the authorized 2022 Ghana DHS IR file**. The regenerated sample sizes, prevalence estimate, concentration indices, adjusted odds ratios, 200-replicate decomposition bootstrap, and variational-Bayes community heterogeneity estimates reproduce the validated analysis.

A journal-targeted manuscript, supplementary package, and submission-asset exporter have been prepared for *Journal of Public Health* (Oxford University Press).

## Data governance

Raw DHS files, extracted row-level datasets, and derived row-level data must stay outside Git. The repository's \`.gitignore\` excludes the Ghana IR dataset, common statistical data formats, and downloaded Ghana DHS ZIP archives.

## Authors

**Gideon Ofosu Kyere**  
Kwame Nkrumah University of Science and Technology, Ghana

**Clement Acheampong**  
Affiliation to be confirmed before submission.

Academic supervision: **Dr. Wilhemina Adoma Pels**.
