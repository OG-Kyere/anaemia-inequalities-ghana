# Submission Package Manifest

> **Working package — not submission-ready.** The 9 October review found citation and reporting defects and outstanding scientific/author confirmations. See `docs/repair_audit_2026-10-09.md` and `submission/author_confirmation.md`. Historical checked items below do not certify the updated pipeline or current authorship declarations.

## Core upload files

| Item | Repository source | Status |
|---|---|---|
| Title page | `submission/jph_title_page.md` | Working draft; see submission gates |
| Main manuscript | `submission/jph_main_manuscript.md` | Working draft; see submission gates |
| Structured abstract | `submission/jph_abstract_200_words.md` | Working draft; see submission gates |
| Cover letter | `submission/jph_cover_letter.md` | Working draft; see submission gates |
| Supplementary material | `supplementary/supplementary_material.md` | Working draft; see submission gates |
| STROBE mapping | `submission/strobe_mapping.md` | Ready; convert to official checklist format if portal requests |
| Reference verification | `submission/reference_verification.md` | Complete |

## Main-paper displays

| Display | Source | Upload preparation |
|---|---|---|
| Table I | `results/table1_weighted_characteristics.md` | Export locally to editable CSV/Word table |
| Table II | `results/table2_full_adjusted_model.md` | Export locally to editable CSV/Word table |
| Table III (panels A and B) | `results/table3_inequality_and_heterogeneity.md` | Export both panels to editable CSV/Word tables under one numbered display |
| Table IV | `results/table4_overall_wald_tests.md` | Editable Word table in the main paper |
| Figures 1–4 | All four original SVG assets | Embedded in main paper; paired high-resolution PNG/TIFF exports |

Use:

```bash
python src/05_prepare_submission_assets.py
```

Generated upload files appear under `submission/generated/`, which is intentionally ignored by Git.

## Display placement and reading layout

At the author's explicit request, all four tables and all four figures appear in the main manuscript. The text uses two columns, with full-width sections for wide editable tables and figures. This author-review layout supersedes the earlier four-display journal selection; it will need adaptation if a target journal enforces that limit. The supplement contains supporting methods and diagnostics only. No estimates or original SVG assets were changed.

## Final lock

Do not reintroduce the earlier decomposition percentages (77.8%, 17.3%, etc.). The final executable specification uses 77.7% for BMI/nutritional status and 15.6% for education.


## Authorship

- Authors: **Gideon Ofosu Kyere; Wilhemina Adoma Pels; Prince Apaah; Clement Acheampong**
- Corresponding author: **Gideon Ofosu Kyere**
- All authors are affiliated with the Department of Statistics and Actuarial Science, Kwame Nkrumah University of Science and Technology, Kumasi, Ghana.
- Corresponding email: **kyereofosu2003@gmail.com**
- Specific CRediT roles remain to be confirmed by all authors before journal submission.

## Real-data verification update — 9 October 2026

The authorized IR archive from the earlier conversation was located and reanalysed. The core point estimates, adjusted associations, decomposition share/intervals and multilevel summaries reproduce. The empirical curve was regenerated, and both final seeded multilevel fits converge at BFGS gradient tolerance 1e-5 without changing reported estimates. The faster PSU resampler preserves exact sampled rows and order. All 21 unit tests pass.

See `docs/real_data_validation_2026-10-09.md` for the current status; earlier “data unavailable” and outstanding-convergence notes above describe the prior review stage. The original inequality interval remains a provenance discrepancy. A documented full-sample 5,000-replicate interval is available but awaits approval under the numerical lock. Author roles and final approval are also unconfirmed. Keep this a draft until those decisions and the final file rebuild are completed.
