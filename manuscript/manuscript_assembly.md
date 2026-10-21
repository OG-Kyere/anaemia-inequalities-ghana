# Manuscript assembly guide

Use `submission/jph_main_manuscript.md` as the canonical manuscript and `manuscript/full_manuscript.md` as its synchronized working mirror. Historical component drafts are not assembly sources.

## Current paper

Title: **Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana**.

Order: title page; structured abstract; keywords; Introduction; Methods; Results; Discussion; Conclusion; declarations; references; main tables; figure legends; supplementary material. Preserve the four journal-specific Discussion subheadings.

## Main displays

1. Table I: participant characteristics and weighted prevalence.
2. Table II: adjusted survey-weighted logistic associations.
3. Table III: panel A, validated wealth-related inequality decomposition; panel B, separate unweighted community-level models.
4. Figure 1: regional prevalence (`figures/figure2_regional_prevalence.svg`).

Main Table III source: `results/table3_inequality_and_heterogeneity.md`. Its panels retain separate headings, sample sizes and estimator notes.

## Supplement

Use `supplementary/supplementary_material.md`: overall Wald tests (Table S1); concentration curve (Figure S1); wealth gradient (Figure S2); decomposition chart (Figure S3); approximate multilevel uncertainty and estimator diagnostics. See `manuscript/figure_plan.md` for source mappings.

Do not present planned continuous-haemoglobin or severity analyses as completed. Do not substitute older exploratory decomposition values for the validated results.

## Export

Run `python src/05_prepare_submission_assets.py --require-reproduced` for selected editable CSV tables and 600-dpi image exports from stored aggregates. Generated assets stay in ignored `submission/generated/`. These exports do not re-estimate results or require microdata. The concentration-curve aggregate is required by the flag.

Final Word/RTF formatting, author roles, author approval and journal submission remain separate steps. Restricted DHS microdata must not be redistributed.
