# Final Submission Checklist — Journal of Public Health

> **Working package — not submission-ready.** The 9 October review found citation and reporting defects and outstanding scientific/author confirmations. See `docs/repair_audit_2026-10-09.md` and `submission/author_confirmation.md`. Historical checked items below do not certify the updated pipeline or current authorship declarations.

## Manuscript length

- JPH main manuscript: approximately **2,883 words before references** in the repaired working manuscript
- Structured abstract: approximately **172 words**
- Original Paper limit verified against the current journal instructions: **2,000–3,000 words**
- Main display limit verified: **no more than 4 tables/figures combined**

## Main manuscript

- [x] Title finalized
- [x] Structured abstract
- [x] Keywords
- [x] Introduction
- [x] Methods
- [x] Results
- [x] Journal-specific Discussion subheadings
- [x] Conclusion
- [x] Ethics statement
- [x] Data availability statement
- [x] Funding statement
- [x] Conflict-of-interest statement
- [x] AI-use disclosure
- [x] Expanded and verified core references
- [x] Main tables selected
- [x] Main figures selected
- [x] Figure legends included
- [x] Alt text placed directly under each main figure legend

## Main displays

The four-display limit is satisfied with:

1. Table I — weighted characteristics and anaemia prevalence
2. Table II — adjusted survey-weighted logistic regression
3. Figure 1 — concentration curve
4. Figure 2 — regional anaemia prevalence

Additional results remain in supplementary material.

## Reproducibility

- [x] Core prevalence and concentration-index pipeline rerun successfully
- [x] Adjusted survey-weighted logistic model reproduced
- [x] 200-replicate decomposition bootstrap completed
- [x] Reproducible decomposition specification documented
- [x] VB multilevel model reproduced locked heterogeneity estimates
- [x] MAP non-convergence documented and excluded from manuscript replication
- [x] Raw DHS data remain outside the repository

## Supplementary material

- [x] Validated decomposition table
- [x] Community-level heterogeneity table
- [x] Wealth-gradient figure
- [x] Validated decomposition figure
- [x] Interpretation cautions

## Reporting quality

- [x] STROBE mapping created
- [x] Selection/measurement-bias limitation included
- [x] Generalisability statement included
- [x] Cross-sectional design clearly stated
- [x] Causal language avoided
- [x] Anaemia not described as iron-deficiency anaemia
- [x] BMI finding not described as causally protective
- [x] Decomposition percentages described as statistical contributions

## Data governance

- [x] Raw DHS data absent from manuscript/repository materials
- [x] Restricted data extensions excluded in `.gitignore`
- [x] Ghana DHS ZIP filename patterns excluded
- [x] `data/raw/` and `data/processed/` excluded
- [x] Data availability directs users to The DHS Program

## Still required before actual submission

- [x] Insert corresponding author's email: kyereofosu2003@gmail.com
- [ ] Add postal code to affiliation if required by the submission form
- [ ] Confirm ORCID placement if desired
- [ ] Confirm CRediT roles with all four authors
- [x] Confirm Clement Acheampong's affiliation: KNUST, Department of Statistics and Actuarial Science
- [x] Confirm second author: Wilhemina Adoma Pels, KNUST, Department of Statistics and Actuarial Science
- [x] Confirm final author order: Gideon Ofosu Kyere; Wilhemina Adoma Pels; Prince Apaah; Clement Acheampong
- [ ] Convert Tables I–II to the journal's preferred editable Word/table format
- [ ] Export Figures 1–2 as journal-compatible high-resolution files (preferably TIFF/EPS/JPG as requested)
- [ ] Add page/line numbering only if requested by the submission system
- [x] Verify expanded bibliography against final source records
- [ ] Upload an official STROBE checklist if the submission system requests it
- [ ] Perform final grammar/typesetting proofread

## Submission package files

- `submission/jph_title_page.md`
- `submission/jph_main_manuscript.md`
- `submission/jph_cover_letter.md`
- `submission/jph_figure_legends_alt_text.md`
- `submission/strobe_mapping.md`
- `supplementary/supplementary_material.md`

## Final interpretation lock

Anaemia remains highly prevalent among Ghanaian women of reproductive age and is disproportionately concentrated among poorer women. Nutritional status accounts for a large share of the measured socioeconomic inequality, while pregnancy, region, and residual community context remain important correlates.

Do not strengthen this wording into causal claims during journal revision.

## Real-data verification update — 9 October 2026

The authorized IR archive from the earlier conversation was located and reanalysed. The core point estimates, adjusted associations, decomposition share/intervals and multilevel summaries reproduce. The empirical curve was regenerated, and both final seeded multilevel fits converge at BFGS gradient tolerance 1e-5 without changing reported estimates. The faster PSU resampler preserves exact sampled rows and order. All 21 unit tests pass.

See `docs/real_data_validation_2026-10-09.md` for the current status; earlier “data unavailable” and outstanding-convergence notes above describe the prior review stage. The original inequality interval remains a provenance discrepancy. A documented full-sample 5,000-replicate interval is available but awaits approval under the numerical lock. Author roles and final approval are also unconfirmed. Keep this a draft until those decisions and the final file rebuild are completed.
