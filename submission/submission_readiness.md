# Submission Readiness — Journal of Public Health

> **Working package — not submission-ready.** The 9 October review found citation and reporting defects and outstanding scientific/author confirmations. See `docs/repair_audit_2026-10-09.md` and `submission/author_confirmation.md`. Historical checked items below do not certify the updated pipeline or current authorship declarations.

## Status

The data-free code and manuscript repairs are complete. Authorized-data revalidation, convergence review and author confirmations remain before submission.

## Manuscript package

Prepared and internally aligned:

- `submission/jph_title_page.md`
- `submission/jph_main_manuscript.md`
- `submission/jph_abstract_200_words.md`
- `submission/jph_cover_letter.md`
- `submission/jph_figure_legends_alt_text.md`
- `submission/strobe_mapping.md`
- `submission/reference_verification.md`
- `supplementary/supplementary_material.md`

## Validated analysis

- Survey-weighted prevalence and subgroup estimates reproduced.
- Erreygers concentration index reproduced.
- Survey-weighted adjusted logistic regression reproduced.
- 200-replicate decomposition bootstrap completed.
- Variational-Bayes multilevel heterogeneity estimates reproduced.
- MAP/Laplace non-convergence documented and not used for manuscript replication.

## Locked headline results

- Anaemia prevalence: **41.12% (95% CI 39.60%–42.64%)**
- Erreygers index: **-0.0589**
- BMI/nutritional-status decomposition share: **77.7%**
- BMI-domain bootstrap interval: **-0.0617 to -0.0300**
- Pregnancy aOR: **1.77 (95% CI 1.43–2.21)**
- Overweight aOR: **0.73 (95% CI 0.62–0.87)**
- Obesity aOR: **0.60 (95% CI 0.49–0.72)**
- Adjusted cluster ICC: **3.14%**
- Adjusted MOR: **1.37**
- PCV: **28.8%**

## Authorship status

Confirmed authors: **Gideon Ofosu Kyere, Wilhemina Adoma Pels, Prince Apaah and Clement Acheampong**.

## Remaining before submission

1. Corresponding-author email confirmed: **kyereofosu2003@gmail.com**.
2. Clement Acheampong's affiliation confirmed: KNUST, Department of Statistics and Actuarial Science.
3. Wilhemina Adoma Pels confirmed as second author; all authors are affiliated with KNUST, Department of Statistics and Actuarial Science.
4. Decide whether to show ORCID on the title page.
5. Confirm specific CRediT roles with all four authors.
6. Run `python src/05_prepare_submission_assets.py` locally and inspect the generated CSV/PNG/TIFF files.
7. Upload the required manuscript, tables, figures, supplement, and any STROBE file requested by the submission portal.

Run the corrected pipeline with authorized data and resolve the scientific checks in the repair audit before submission.
