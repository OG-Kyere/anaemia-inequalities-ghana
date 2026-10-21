# Manuscript revision report — 21 October 2026

## Scope and baseline

Baseline: `ce38832e18143b03d67a07d3c8d8a0aaf2fafb0c` on `main`.
This is an editorial and methodological clarification for review. No analysis was rerun. No DHS microdata was accessed, downloaded, uploaded or included in this change.

The referenced “Anaemia Research Summary” chat returned only assistant content-reference placeholders; its browser page remained at a loading shell. The exact earlier verified passages could not be recovered. The equations and gap wording in this revision were independently reconstructed and checked against the baseline analysis code and primary methods references. They must not be described as verbatim recovered chat text.

## Changes

| File | Change |
|---|---|
| `submission/jph_main_manuscript.md` | Focused Introduction gap; eight numbered Methods equations; bibliographic completeness updates. |
| `manuscript/full_manuscript.md` | Synchronized copy of the canonical manuscript, retaining its source banner. |
| `submission/reference_numbering_map.json` | Reference strings synchronized; all original/current numbers retained. |
| `submission/reference_verification.md` | Added current-number audit of all 15 references, evidence links, year/volume distinctions and limits; retained historical audit. |
| `docs/manuscript_revision_2026-10-21.md` | This change report. |

The Introduction acknowledges existing Ghana determinants work, multicountry severity models and geographic analyses. It distinguishes Salifu et al.'s between-survey prevalence decomposition from wealth-ranked inequality decomposition within 2022 Ghana data. The contribution is the combination of complementary questions, without a claim to be the first study or a systematic review of all literature.

## Equation verification

| Equation | Quantity | Implementation checked |
|---|---|---|
| 1 | DHS sampling weight and weighted prevalence | `src/common.py`: loading weights, weighted means and Taylor-linearised prevalence. |
| 2 | Weighted fractional wealth midrank, including ties | `src/common.py:weighted_midrank`. |
| 3 | Standard concentration index and binary Erreygers correction, E = 4 × mean × C = 8 × weighted covariance | `src/common.py:concentration_indices`; Erreygers reference 11. |
| 4–5 | Weighted linear probability model; additive covariance contributions and residual | `src/03_inequality_decomposition.py`; references 11–12. Age indicators and BMI/BMI-squared remain grouped; wealth remains the rank variable rather than a determinant. |
| 6 | Weighted logistic model, aORs and design-based confidence limits | `src/02_adjusted_logistic.py`: weighted GLM and stratified PSU sandwich covariance. |
| 7–8 | Random-intercept logistic model; ICC, MOR and proportional variance change | `src/04_multilevel_heterogeneity.py`; reference 13. Preserves unweighted variational Bayes, priors and convergence disclosure. |

Decomposition percentages use the complete-case sample's observed E as denominator. The covariance formulation avoids undefined covariate concentration indices when a covariate mean is zero. PCV remains descriptive; the null/adjusted sample difference is preserved, not silently refitted. All causal guardrails remain in place.

## Bibliography outcome

All 15 entries were checked against WHO, DHS, publisher pages, primary-paper records or publisher-deposited Crossref metadata. Added web-report URLs/access dates, WHO guideline ISBN and issue numbers for the three methodological papers. No new reference was added or removed; citation numbering is unchanged. Frontiers publication years of 2024 remain correct despite volume/DOI labels containing 2023; Baye's 2025 volume citation remains despite online publication in December 2024.

The full evidence and retrieval limitations are in `submission/reference_verification.md`. The novelty argument is an inference about the cited studies' scope. Metadata verification is not a blanket validation of cited findings.

## Validation completed

- Existing `tests/test_manuscript.py`: **4 tests passed**, using the bundled Python runtime.
- Separate baseline comparisons: abstract unchanged; Results through declarations unchanged; main-display text/legends unchanged.
- Canonical manuscript and working mirror are identical after removal of the mirror's existing source banner.
- All 15 references cited, consecutive reference numbers, correct first-appearance order, no orphan/unused citations; numbering-map text matches the bibliography.
- Eight sequential equation tags and paired display-math delimiters checked.
- Introduction through Conclusion: **2,666 words** by whitespace count excluding heading lines, including equation notation. This is a transparent count, not a fresh certification of journal formatting requirements.
- Git tree comparison must show changes only to the five listed files; all other tracked blobs, including analysis code, aggregate results, tables, figures, supplementary material and historical component drafts, are preserved.

Locked examples retained: n = 7,557; prevalence 41.1% (39.6–42.6%); E = -0.0589 (-0.0924 to -0.0249); BMI contribution 77.7%; existing adjusted odds ratios and community heterogeneity values. The result files and figures are not regenerated.

## Review limits

No statistical rerun, new empirical finding, Word/PDF export, Overleaf edit, journal submission or merge is included. Historical component drafts retain their existing warnings to use the canonical source. Existing author-confirmation and publication-formatting requirements remain outside this revision. Reviewers should assess the reconstructed wording and equations before merging.
