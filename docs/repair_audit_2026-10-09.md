# Repository repair audit — 9 October 2026

Base: commit `422f05e55e55c5a8812daff1863136f30ef91f63`.

## Repairs

- Corrected stale citation-to-reference links left after literature expansion. All 15 references now have supporting in-text mentions and are numbered by first appearance. The original/current numbering map is saved in `submission/reference_numbering_map.json`.
- Added the missing ethics statement to the canonical submission manuscript. Synchronized `manuscript/full_manuscript.md`; labelled component drafts as historical and corrected obsolete abstract decomposition shares.
- Repaired escaped Markdown fences and malformed LaTeX equations/control characters.
- Kept interpretation non-causal and made the unweighted nature, priors and convergence limitation of the contextual VB models explicit.
- Removed claims that planned haemoglobin/severity sensitivity analyses have completed executable results. Kept recorded exploratory findings distinct from reproduced analyses.
- Converted the empty supplementary “Table S3” heading to a narrative sensitivity heading and added the existing numerical overall Wald table as S3.
- Made script and output locations relative to the repository, so runs from another directory work.
- Removed output-directory creation when analysis modules are merely imported.
- Preserved missing binary/categorical covariates when constructing the decomposition frame.
- Added input checks for invalid weights, empty domains, undefined standard concentration indices and singleton-PSU variance calculations. Existing valid-input definitions remain intact.
- Added a full-sample stratified PSU concentration-index bootstrap and aggregate empirical curve coordinates to the core pipeline. Their outputs are separate from BMI-complete decomposition output.
- Added weighted subgroup shares and full-covariance overall Wald tests to the reproducible exports.
- Persisted multilevel optimizer status/message rather than presenting a successful script exit as proof of convergence.
- Fixed the figure exporter to work without a graphical desktop, strip Markdown from CSV cells and use source aggregate tables instead of duplicated regional arrays.
- The exporter labels stored curve points as a preview until an empirical aggregate curve is available. `--require-reproduced` prevents exporting that preview as a final empirical curve.
- Strengthened diagnostics for citations, ethics, model-weighting disclosure, author confirmation and incomplete export sets; added data-free continuous integration.

## Validation

All 20 unit tests passed. All analysis stages passed the isolated synthetic smoke test. Snapshot exports succeeded, were visually inspected, and include 600-dpi PNG/TIFF figures, CSV tables without Markdown markup and an explicit provenance record. The empirical-curve requirement correctly rejects missing authorized-data output.


Unit tests cover survey weighting, tied ranks, zero outcomes, missing data, domain variances, malformed inputs, full-sample bootstrap repeatability, decomposition missingness, citation sequencing, Markdown tables and joint Wald tests.

The full core/decomposition/multilevel runner was also exercised on isolated synthetic Stata data from outside the repository. Synthetic data are not Ghana DHS data and are never included in repository changes or deliverables. The smoke test uses only two bootstrap replicates to exercise software; it is not an uncertainty analysis.

## Items that cannot be certified here

1. **Authorized-data revalidation:** no `DHS_IR_PATH` was supplied in this review. Locked aggregate results were retained; they were not newly reproduced. The historical validation records remain historical evidence.
2. **Bootstrap population:** the executable decomposition bootstrap uses 7,550 BMI-complete women and an Erreygers index of -0.058853. The primary prevalence/inequality analysis uses 7,557 women and index -0.058938. The recorded -0.0914 to -0.0212 interval must be checked against its original full-sample provenance or the new full-sample bootstrap. Do not silently attach a complete-case interval to the full-sample estimate.
3. **Empirical curve:** the repository stores coarse concentration-curve points. Regenerate `concentration_curve.csv` using authorized data and export with `--require-reproduced` before submission. Existing locked SVGs are not represented as freshly validated empirical outputs.
4. **Multilevel convergence:** VB previously emitted a convergence warning and MAP failed. A successful smoke test or matching rounded values does not resolve the scientific convergence issue. Refit/diagnose using authorized data and report the actual optimizer status.
5. **Authorship:** roles and final approval must come from the four authors. See `submission/author_confirmation.md`. No contributor roles or approval were invented.
6. **Submission declarations:** confirm AI review, originality, exclusive submission, interests, funding, positions/designations and postal address. The cover letter remains a draft.
7. **Journal format:** the Markdown source uses numbered citation identifiers; a typesetter can render them as superscripts. The earlier Overleaf/PDF files retain the earlier reference order and should not be submitted as the current manuscript. Final journal upload formatting and its official STROBE checklist still require completion.

The repository is a repaired working project, not a certified submission-ready or newly scientifically validated package.

## Real-data verification update — 9 October 2026

The authorized IR archive from the earlier conversation was located and reanalysed. The core point estimates, adjusted associations, decomposition share/intervals and multilevel summaries reproduce. The empirical curve was regenerated, and both final seeded multilevel fits converge at BFGS gradient tolerance 1e-5 without changing reported estimates. The faster PSU resampler preserves exact sampled rows and order. All 21 unit tests pass.

See `docs/real_data_validation_2026-10-09.md` for the current status; earlier “data unavailable” and outstanding-convergence notes above describe the prior review stage. The original inequality interval remains a provenance discrepancy. A documented full-sample 5,000-replicate interval is available but awaits approval under the numerical lock. Author roles and final approval are also unconfirmed. Keep this a draft until those decisions and the final file rebuild are completed.


## Update — 10 October 2026

The corresponding author approved the 5,000-replicate inequality interval (-0.0924 to -0.0249); it is now applied throughout the current manuscript and figures. Earlier pending-approval statements above describe the historical review stage. See `docs/approved_interval_update_2026-10-10.md`. Author contributions and final approval remain provisional.
