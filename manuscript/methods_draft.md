# Methods Draft

## Study design and data source

This study is a secondary analysis of nationally representative cross-sectional data from the 2022 Ghana Demographic and Health Survey. The analysis focuses on women aged 15–49 years with valid haemoglobin-based anaemia measurements.

The survey used a stratified multistage sampling design. Enumeration areas served as primary sampling units, and households were sampled within clusters. All analyses intended to produce population-level estimates account for the DHS sampling weights, clustering, and stratification.

## Study population

The Ghana 2022 Individual Recode file contained 15,014 women aged 15–49 years. The primary analytic sample consisted of women with a valid DHS anaemia classification in `v457`.

Women with missing or invalid anaemia measurements were excluded from the main analysis. Analyses involving BMI excluded records with unavailable or flagged anthropometric values.

## Outcome

The primary outcome was **any anaemia**, derived from the DHS anaemia classification variable `v457`.

Women classified as having mild, moderate, or severe anaemia were coded as anaemic, while women classified as not anaemic were coded as non-anaemic.

Altitude-adjusted haemoglobin, available in `v456`, was retained as a continuous sensitivity outcome.

## Main socioeconomic exposure

Household socioeconomic position was assessed using the DHS wealth index.

Two representations were used:

- `v190`: household wealth quintile for descriptive and regression analyses;
- `v191`: continuous household wealth score for socioeconomic ranking in concentration-index analyses.

## Covariates

Prespecified covariates included:

- age group;
- educational attainment;
- urban/rural residence;
- region;
- current pregnancy status;
- parity;
- BMI category;
- current employment;
- marital status.

BMI was derived from `v445` after removal of DHS special codes and classified as:

- underweight: <18.5 kg/m2;
- normal weight: 18.5–24.9 kg/m2;
- overweight: 25.0–29.9 kg/m2;
- obesity: >=30.0 kg/m2.

Covariates were selected a priori based on substantive relevance rather than stepwise significance testing.

## Survey design specification

The DHS sampling weight was calculated as:

[
w_i = rac{v005_i}{1,000,000}.
]

Primary sampling units were identified using `v021`, and sampling strata using `v022`.

Survey-weighted means, proportions, standard errors, and confidence intervals were estimated using the full complex sampling design.

## Descriptive analysis

Participant characteristics were summarized using unweighted counts and survey-weighted percentages.

Survey-weighted anaemia prevalence and 95% confidence intervals were estimated overall and across age, education, wealth, residence, pregnancy status, parity, BMI, employment, marital status, and region.

## Socioeconomic inequality analysis

Wealth-related inequality in anaemia was assessed using concentration-curve methods.

Women were ranked from poorest to richest using the continuous DHS wealth score.

The standard concentration index was calculated as:

[
CI = rac{2}{mu}operatorname{Cov}(y,r),
]

where (y) denotes anaemia status, (mu) its weighted mean, and (r) the fractional wealth rank.

Because anaemia is a bounded binary outcome, the primary inequality measure was the Erreygers corrected concentration index.

A negative concentration index indicates concentration of anaemia among socioeconomically disadvantaged women.

Uncertainty for the corrected concentration index was assessed using stratified primary-sampling-unit bootstrap resampling within DHS strata.

## Decomposition analysis

The Erreygers concentration index was decomposed to quantify the statistical contribution of measured determinants to observed wealth-related inequality.

A survey-weighted linear probability model was used because additive decomposition requires an additive outcome model.

The decomposition model included age, education, residence, pregnancy status, parity, BMI, employment, and marital status. Wealth itself was not included as a determinant because it defined the socioeconomic ranking.

Age and BMI were modelled flexibly using linear and quadratic terms in the primary decomposition.

Domain-specific contributions were calculated from the elasticity of anaemia with respect to each determinant and the determinant-specific concentration index.

Uncertainty in domain contributions was assessed using stratified PSU bootstrap resampling.

## Survey-weighted regression

Adjusted associations with anaemia were estimated using survey-weighted logistic regression.

The fully adjusted model included age group, education, wealth quintile, residence, pregnancy status, parity, BMI category, employment, marital status, and region.

Results are reported as adjusted odds ratios with 95% confidence intervals.

Overall Wald tests were used to assess categorical factors.

## Multilevel analysis

To quantify community-level heterogeneity, two-level logistic mixed models were fitted with women nested within DHS sampling clusters.

The null model contained only a random intercept for cluster.

The adjusted model included the same individual-level covariates as the main regression model.

The intraclass correlation coefficient was calculated using the logistic latent-variable approximation:

[
ICC = rac{sigma_u^2}{sigma_u^2 + pi^2/3}.
]

The median odds ratio was calculated as a measure of between-cluster heterogeneity.

The proportional change in variance between the null and adjusted models was used to quantify the proportion of cluster-level variance explained by measured covariates.

The multilevel analysis was treated as complementary to, rather than a replacement for, the design-based survey analysis.

## Sensitivity analyses

Planned and completed sensitivity analyses included:

- modelling BMI using alternative functional forms;
- examining BMI categories instead of continuous nonlinear terms in the decomposition;
- pregnancy-stratified analyses;
- continuous haemoglobin as a secondary outcome;
- alternative anaemia severity specifications where sample sizes permitted;
- inspection of regional influence on adjusted estimates.

## Missing data

Missingness was evaluated before modelling.

Most prespecified socioeconomic and reproductive covariates were complete among women with valid anaemia measurements. Records with unavailable or flagged BMI values were excluded only from analyses requiring BMI.

## Statistical interpretation

The analysis emphasizes effect magnitude, uncertainty, and consistency across methods.

Adjusted regression and decomposition results are interpreted as associations and statistical contributions, respectively, and not as causal effects.
