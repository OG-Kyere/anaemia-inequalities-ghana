# Main-paper strengthening and appendix promotion — 21 October 2026

## What changed and why

This follow-up builds on PR #2 at commit `d5548d2570f4f5d0dda302423a385d4fcf7dbb06`. The supplied 24-page PDF contains similarity-report front matter followed by a 17-page manuscript. The manuscript's appendix tables and figure captions were read and visually inspected. The PDF is a review source only; it is not committed or redistributed.

The central contribution should be visible in the main paper: wealth-related inequality, its statistical decomposition and residual community heterogeneity. The validated appendix tables were therefore promoted into **main Table III**, with clearly separate panels:

- **A:** all nine decomposition domains/residual, signed absolute contributions, percentages and 200-replicate bootstrap intervals;
- **B:** null and adjusted unweighted multilevel summaries, including sample sizes, variance, ICC, MOR and PCV.

Both panels retain their own model interpretation; the table does not pool estimators or imply the same sample. The concentration curve moves to Supplementary Figure S1, while its index and confidence interval stay in the main Results. The regional prevalence plot becomes main Figure 1. No SVG file was edited.

The resulting main display plan is **Tables I–III and Figure 1**, four numbered displays. [JPH author instructions](https://academic.oup.com/jpubhealth/pages/instructions_for_authors), checked 21 October 2026, specify 2,000–3,000 words and no more than four tables/figures. Panel formatting remains subject to the journal's final editorial assessment.

## Stronger reporting

- Added the decomposition sample (7,550) and its observed index (-0.058853), distinguishing it from the full-sample index.
- Brought the key validated factor-level Wald statistics into Results: pregnancy 26.65 (df 1), BMI 35.47 (df 3), region 45.49 (df 15), all p < 0.001; wealth p = 0.852 and education p = 0.933.
- Stated sample sizes for the null (7,557) and adjusted (7,550) community models, and explained the adjusted MOR.
- Corrected “77.7% of measured inequality” to “77.7% of the observed inequality” in both abstracts; the value and denominator calculation are unchanged.
- Sharpened the practical implications around monitoring by wealth/region and investigating aetiology; BMI is not a weight-gain treatment target.
- Made the unweighted multilevel limitation and the effect of different null/adjusted samples explicit. The 28.8% variance difference is descriptive, not a causal proportion explained.
- Kept approximate community-model uncertainty and diagnostics supplementary. Did not promote older exploratory BMI-category numbers or replace the validated decomposition with historical estimates.
- Retained all eight methodology equations and the verified 15-reference bibliography from the first revision.

The main text is **2,857 words** by whitespace count excluding headings, including equation notation; abstract, table bodies, legends and references are separate. The structured abstract remains below 200 words.

## Source-of-truth checks

Promoted values match the stored aggregate CSVs:
`inequality_decomposition_point.csv`, `inequality_decomposition_bootstrap_intervals.csv`, `inequality_decomposition_meta.csv`, `community_heterogeneity_vb.csv` and `adjusted_logistic_wald_tests.csv` under `results/reproduced/`.

Every value in promoted panels A and B is compared to those aggregate sources at the displayed precision. Pregnancy's small positive upper decomposition bound remains **0.000020**: its interval includes zero. Smaller-domain uncertainty must remain visible alongside their point percentages.

The older `results/inequality_decomposition.md` and `results/sensitivity_and_geographic_checks.md` contain exploratory values (including 77.8%) that were not promoted. Primary values remain 77.7% for BMI and 15.6% for education.

## Files and export consistency

Updated canonical manuscript, working mirror, standalone abstract, supplement, figure legends, display/assembly guides, manifest, checklist and STROBE mapping. Added `results/table3_inequality_and_heterogeneity.md`.

Updated only submission-asset export/diagnostic code, not statistical estimation code. Selected exports now include editable CSVs for Table III's two panels and Supplementary Table S1; main Figure 1 is regional prevalence, and Supplementary Figure S1 is the concentration curve. Existing SVG paths remain stable.

CI now exercises the real asset exporter from stored aggregate outputs before project diagnostics. No data download or analytic rerun is required for those exports.

## Validation

- **Eight manuscript tests** cover citation integrity, table parsing, promoted estimates against locked aggregates, both exported CSV panels and main/supplementary placement.
- Separate checks verify synchronized manuscripts/abstracts, unchanged eight-equation blocks and reference list, main word count, and preservation of the stored results/figures/statistical estimation code.
- Local CSV export functions are exercised directly. Full image export is exercised in CI because Matplotlib is absent from the bundled local runtime.
- No DHS microdata was accessed, uploaded or committed. No empirical estimates were recalculated.
- No author-role confirmation, journal submission or merge is implied. This remains a draft for scientific and author review.

The initial revision report in `docs/manuscript_revision_2026-10-21.md` describes the first commit; this follow-up supersedes its display-placement and word-count statements.
