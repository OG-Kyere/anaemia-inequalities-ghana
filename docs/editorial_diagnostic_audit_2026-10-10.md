# Editorial and diagnostic audit: 10 October 2026

The current manuscript, abstract, supplementary material, figure descriptions and draft cover letter were reviewed for spelling, grammar, consistency and interpretation. The Humanizer skill (blader/humanizer, version 3.1.0) was downloaded and read before editing: https://github.com/blader/humanizer/blob/main/SKILL.md. It was applied in a neutral academic register. Scientific terms, statistical association language, numerical ranges, reference titles and the AI-use disclosure were preserved.

## Changes

- Replaced staged openings, inflated wording and repeated conclusions with direct statements.
- Removed unnecessary bold emphasis from numerical results in the prose. Table emphasis was retained.
- Used British spelling consistently outside reference titles.
- Rewrote the wealth-adjustment interpretation to avoid implying a causal pathway or mediation.
- Kept planned haemoglobin/severity analyses clearly distinct from completed analyses.
- Simplified the exploratory BMI sensitivity description without presenting it as a newly verified sensitivity result.
- Restored the Overleaf decomposition-table footnote specifying its sample (7,550) and complete-case Erreygers denominator (-0.058853).
- Made PDF captions and estimator diagnostics follow the repository text.

## Verification

The baseline and post-edit project diagnostics pass: dependency imports, syntax, all 21 unit tests, references in first-appearance order, author order, data-governance checks, authorised DHS sample/prevalence/index checks and generated image quality. The isolated synthetic full-pipeline smoke test checks execution from outside the repository. Numerical tokens and citation sequence in the main manuscript are unchanged; all 15 reference entries are unchanged. The canonical manuscript and mirror match, and the standalone abstract matches the manuscript (148 words by whitespace count, excluding headings).

The saved 5,000-replicate full-sample bootstrap quantiles match the approved interval record (seed 20261008). Both saved final multilevel optimizers report success and gradients below tolerance. These checks inspect the authorised-data results; the editorial pass does not claim to rerun every statistical model or to verify an author's contribution or approval.

## Items requiring author confirmation

Two rounding discrepancies were identified and presented to the corresponding author. The two-decimal prevalence CI lower limit is stored as 39.60%, while the saved unrounded output rounds to 39.61%. The adjusted cluster SD is stored as 0.327, while the saved unrounded output rounds to 0.326. They remain unchanged pending explicit approval under the existing numerical lock. The headline one-decimal prevalence CI (39.6–42.6%) is unaffected.

Contributor roles and final manuscript approval remain pending for all four authors. The funding, competing-interest and AI-review declarations require author confirmation before submission, as already documented in `submission/author_confirmation.md`.

## Document build

The final PDF compilation, visual inspection and ZIP integrity results are recorded in the delivered project's `BUILD_CHECKS.md`. No restricted microdata are included in the repository or Overleaf package. Historical audit records are retained as history.
