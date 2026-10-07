# Community-Level Heterogeneity in Anaemia

## Objective

To quantify how much anaemia risk varies across DHS sampling clusters after accounting for measured individual-level characteristics.

## Model

A two-level logistic mixed model was fitted with women nested within DHS sampling clusters.

### Null model

The null model contained only a random intercept for cluster.

Estimated cluster-level standard deviation:

**0.387**

Estimated cluster-level variance:

**0.150**

Using the logistic latent-variable approximation,

[
ICC = \frac{\sigma_u^2}{\sigma_u^2 + \pi^2/3},
]

the estimated intraclass correlation coefficient was:

**ICC = 4.35%**

The corresponding median odds ratio was:

**MOR = 1.45**

Approximate interval based on uncertainty in the random-effect standard deviation:

- ICC: **3.91% to 4.84%**
- MOR: **1.42 to 1.48**

### Adjusted model

The adjusted model included:

- age group
- education
- wealth quintile
- urban/rural residence
- current pregnancy
- parity
- BMI category
- employment
- marital status
- region

Estimated cluster-level standard deviation:

**0.327**

Estimated cluster-level variance:

**0.107**

Adjusted cluster heterogeneity:

- **ICC = 3.14%**
- **MOR = 1.37**

Approximate interval:

- ICC: **2.82% to 3.50%**
- MOR: **1.34 to 1.39**

## Proportional change in variance

The cluster-level variance declined from 0.150 to 0.107 after adjustment.

[
PCV = \frac{0.150 - 0.107}{0.150} \approx 28.8\%.
]

Thus, the measured individual, socioeconomic, reproductive, nutritional, and regional factors explain approximately **28.8% of the between-cluster variance**.

## Interpretation

There is meaningful residual community-level heterogeneity in anaemia risk.

Even after adjustment, two otherwise similar women from clusters at different points of the residual risk distribution can differ appreciably in their odds of anaemia. The adjusted MOR of approximately **1.37** indicates modest but non-trivial contextual clustering.

The ICC is relatively small in absolute terms, but this is common for binary health outcomes and should not be interpreted as evidence that community context is unimportant. The persistence of residual cluster variance suggests that unmeasured contextual factors may contribute to geographic disparities.

## Methodological note

The multilevel model is used to characterize cluster-level heterogeneity rather than to replace the design-based survey analysis.

National prevalence and inequality estimates remain based on the DHS survey design. The mixed model is a complementary contextual analysis.

## Conclusion

Measured covariates explain part, but not all, of the geographic clustering in anaemia. Residual community-level heterogeneity remains after adjustment, supporting the inclusion of a multilevel component in the study.
