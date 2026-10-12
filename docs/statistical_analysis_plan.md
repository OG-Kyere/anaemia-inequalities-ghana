# Statistical Analysis Plan

## 1. Data audit

After access is granted, the Ghana 2022 Individual Recode file will be audited for:

- variable availability and labels
- valid haemoglobin/anaemia observations
- missingness
- sampling design variables
- out-of-range values
- consistency with the DHS final report

A variable dictionary will be frozen before inferential modelling.

## 2. Survey design

Analyses intended to represent the Ghanaian population will use:

- sampling weight: `v005 / 1,000,000`
- primary sampling unit: `v021`
- stratum: `v022` or the appropriate Ghana-specific stratification variable

## 3. Outcome definitions

### Primary outcome

Binary anaemia:

- 0 = not anaemic
- 1 = mild, moderate, or severe anaemia

### Secondary outcome

Anaemia severity using the ordered DHS categories where sample sizes permit.

## 4. Descriptive analysis

Estimate survey-weighted:

- overall anaemia prevalence
- prevalence by wealth quintile
- prevalence by education
- prevalence by residence
- prevalence by region
- prevalence by age
- prevalence by pregnancy status
- prevalence by parity
- prevalence by nutritional status

Report weighted percentages with 95% confidence intervals.

## 5. Socioeconomic inequality

Construct a fractional household-wealth rank.

The principal inequality measure will be a concentration index appropriate for a bounded binary outcome. The preferred primary estimator is the **Erreygers corrected concentration index**.

A concentration curve will display the cumulative distribution of anaemia against cumulative socioeconomic rank.

## 6. Decomposition analysis

Decompose measured wealth-related inequality into contributions from prespecified covariates.

Candidate domains:

- education
- residence
- region
- age
- employment
- marital status
- pregnancy status
- parity
- nutritional status

Interpret decomposition estimates as statistical contributions to observed inequality, not causal effects.

## 7. Multilevel modelling

Women will be modelled as nested within DHS sampling clusters.

Primary model:

```
logit[P(Y_ij = 1)] = beta_0 + beta'X_ij + u_j
u_j ~ Normal(0, \sigma_u^2)
```

Model sequence:

1. Null model
2. Individual demographic/reproductive factors
3. Socioeconomic factors
4. Geographic/contextual factors
5. Fully adjusted model

Report adjusted odds ratios with 95% confidence intervals.

Where appropriate, quantify residual cluster heterogeneity using the intraclass correlation coefficient and/or median odds ratio.

## 8. Missing data

Patterns and extent of missingness will be documented before modelling.

Complete-case analysis will be used only if missingness is minimal and plausibly ignorable. Multiple imputation may be considered if important covariates contain meaningful missingness and the assumptions are defensible.

## 9. Sensitivity analyses

Planned sensitivity analyses include:

- continuous haemoglobin where scientifically appropriate
- alternative anaemia severity modelling
- exclusion or stratification of pregnant women
- alternative covariate parameterisations
- comparison of conventional and bounded-outcome inequality indices
- assessment of influential regions or sparse categories

## 10. Statistical reporting

Effect estimates will be accompanied by 95% confidence intervals. Emphasis will be placed on magnitude, uncertainty, and consistency rather than dichotomous p-value interpretation.

## 11. Reproducibility

Analysis scripts will be version-controlled. Raw DHS microdata will remain local and will never be committed to GitHub.
