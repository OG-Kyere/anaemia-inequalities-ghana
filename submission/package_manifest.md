# Submission Package Manifest

## Core upload files

| Item | Repository source | Status |
|---|---|---|
| Title page | `submission/jph_title_page.md` | Ready except corresponding email and unresolved affiliation details |
| Main manuscript | `submission/jph_main_manuscript.md` | Ready |
| Structured abstract | `submission/jph_abstract_200_words.md` | Ready |
| Cover letter | `submission/jph_cover_letter.md` | Ready except corresponding email / final author details |
| Supplementary material | `supplementary/supplementary_material.md` | Ready |
| STROBE mapping | `submission/strobe_mapping.md` | Ready; convert to official checklist format if portal requests |
| Reference verification | `submission/reference_verification.md` | Complete |

## Main-paper displays

| Display | Source | Upload preparation |
|---|---|---|
| Table I | `results/table1_weighted_characteristics.md` | Export locally to editable CSV/Word table |
| Table II | `results/table2_full_adjusted_model.md` | Export locally to editable CSV/Word table |
| Figure 1 | `figures/figure1_concentration_curve.svg` | Export locally to high-resolution PNG/TIFF |
| Figure 2 | `figures/figure2_regional_prevalence.svg` | Export locally to high-resolution PNG/TIFF |

Use:

```bash
python src/05_prepare_submission_assets.py
```

Generated upload files appear under `submission/generated/`, which is intentionally ignored by Git.

## Supplementary displays

- wealth-gradient figure;
- validated decomposition figure;
- decomposition table;
- community-level heterogeneity table;
- interpretation and reproducibility notes.

## Final lock

Do not reintroduce the earlier decomposition percentages (77.8%, 17.3%, etc.). The final executable specification uses 77.7% for BMI/nutritional status and 15.6% for education.


## Authorship

- Authors: **Gideon Ofosu Kyere; Clement Acheampong**
- Corresponding author: **Gideon Ofosu Kyere**
- Academic supervisor acknowledged separately: **Dr. Wilhemina**
- Still to confirm: Clement's affiliation and Dr. Wilhemina's full professional details.
