# Submission Readiness — Journal of Public Health

## Status

The scientific and reproducibility work is complete. The remaining steps are administrative and file-export tasks.

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

Confirmed authors: **Gideon Ofosu Kyere and Clement Acheampong**.  
Academic supervisor: **Dr. Wilhemina** (acknowledged separately; not listed as an author at this stage).

## Remaining before submission

1. Insert the corresponding-author email in the title page and cover letter.
2. Clement Acheampong's affiliation confirmed: KNUST, Department of Statistics and Actuarial Science.
3. Dr. Wilhemina's affiliation confirmed: KNUST, Department of Statistics and Actuarial Science; full professional name still to confirm.
4. Decide whether to show ORCID on the title page.
5. Run `python src/05_prepare_submission_assets.py` locally and inspect the generated CSV/PNG/TIFF files.
6. Upload the required manuscript, tables, figures, supplement, and any STROBE file requested by the submission portal.

No further statistical analysis is required unless the journal requests revisions.
