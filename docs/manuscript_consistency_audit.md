# Manuscript Consistency Audit

## Status

**Core numerical consistency: PASS**

The manuscript, result tables, and figures were checked against the locked analysis outputs.

## Locked study numbers

| Quantity | Locked value |
|---|---:|
| Full IR sample | 15,014 |
| Valid anaemia sample | 7,557 |
| Complete BMI model sample | 7,550 |
| Overall weighted prevalence | 41.12% |
| Overall 95% CI | 39.60%–42.64% |
| Erreygers concentration index | -0.0589 |
| Bootstrap 95% CI | -0.0914 to -0.0212 |
| BMI decomposition contribution | 77.8% |
| Education contribution | 17.3% |
| Pregnancy aOR | 1.77 |
| Pregnancy 95% CI | 1.43–2.21 |
| Overweight aOR | 0.73 |
| Obesity aOR | 0.60 |
| Oti aOR | 1.48 |
| Bono aOR | 0.61 |
| Null ICC | 4.35% |
| Adjusted ICC | 3.14% |
| Adjusted MOR | 1.37 |
| Proportional change in cluster variance | 28.8% |

## Cross-file checks

### Abstract vs Results
PASS. Primary prevalence, concentration index, BMI contribution, pregnancy estimate, BMI estimates, and adjusted ICC agree.

### Table 1 vs Results
PASS. Wealth, education, residence, pregnancy, BMI, and overall prevalence values agree.

### Table 2 vs Results
PASS. Pregnancy, overweight, obesity, Oti, and Bono estimates agree.

### Decomposition vs Discussion
PASS. BMI and education contributions agree. Discussion language correctly treats contributions as statistical rather than causal.

### Community heterogeneity
PASS. Null and adjusted variances, ICCs, MORs, and proportional change in variance agree.

### Figures
PASS for values represented in the SVG figures:
- concentration curve: Erreygers index and CI;
- regional plot: prevalence range and national reference;
- wealth gradient: quintile prevalence estimates;
- decomposition plot: locked absolute contributions.

## Issues fixed during manuscript assembly

1. Mathematical expressions were normalized to valid LaTeX syntax.
2. The complete-case regression sample is distinguished from the primary anaemia sample.
3. The BMI finding is consistently described as an association, not a causal protective effect.
4. Socioeconomic inequality is distinguished from adjusted wealth coefficients.
5. Multilevel estimates are described as complementary contextual analyses rather than design-based national estimates.

## Remaining items before journal submission

1. Add full methodological references.
2. Confirm journal-specific ethics wording against the Ghana DHS final report and DHS data-access statement.
3. Choose the target journal and reformat title page, abstract headings, references, tables, and figures.
4. Add author affiliation, correspondence email, ORCID, and any co-authors.
5. Run a final reproducibility check from a fresh environment using only repository code plus locally supplied DHS data.
6. Add page/figure/table numbering according to the target journal.

## Interpretation guardrails

- Do not call the anaemia outcome iron-deficiency anaemia.
- Do not state that obesity protects against anaemia.
- Do not describe decomposition percentages as causal mediation.
- Do not infer individual-level effects from the concentration index.
- Do not claim geographic causation from regional associations.
- Do not upload raw or row-level DHS data to GitHub.
