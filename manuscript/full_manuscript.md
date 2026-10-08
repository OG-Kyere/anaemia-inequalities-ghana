# Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana

## Abstract

### Background
Anaemia remains highly prevalent among women of reproductive age in Ghana, but national averages may conceal important socioeconomic and geographic disparities. This study quantified wealth-related and geographic inequalities in anaemia and assessed the measured factors contributing to those inequalities.

### Methods
We analysed nationally representative data from women aged 15–49 years in Ghana with valid haemoglobin-based anaemia measurements. Survey weights, strata, and primary sampling units were incorporated into descriptive and regression analyses. Wealth-related inequality was assessed using concentration curves and the Erreygers-corrected concentration index. The index was decomposed to estimate the statistical contribution of measured demographic, socioeconomic, reproductive, and nutritional factors. Survey-weighted logistic regression was used to estimate adjusted associations with anaemia, and multilevel logistic models quantified residual community-level heterogeneity.

### Results
Among 7,557 women with valid anaemia measurements, the survey-weighted prevalence of anaemia was **41.1% (95% CI 39.6%–42.6%)**. Prevalence declined from **46.6%** among women in the poorest wealth quintile to **38.8%** among those in the richest quintile. The Erreygers-corrected concentration index was **-0.0589** (bootstrap 95% CI **-0.0914 to -0.0212**), indicating a disproportionate concentration of anaemia among poorer women. BMI/nutritional status made the largest measured contribution to wealth-related inequality (**77.7%**), followed by education (**15.6%**). In adjusted analyses, current pregnancy was associated with higher odds of anaemia (aOR **1.77**, 95% CI **1.43–2.21**), while overweight (aOR **0.73**, 95% CI **0.62–0.87**) and obesity (aOR **0.60**, 95% CI **0.49–0.72**) were associated with lower odds compared with normal weight. Regional heterogeneity persisted, with higher adjusted odds in Oti and lower odds in Bono relative to Greater Accra. The adjusted cluster-level intraclass correlation coefficient was approximately **3.1%**, with a median odds ratio of **1.37**.

### Conclusion
Anaemia among women of reproductive age in Ghana is both socioeconomically and geographically patterned. Poorer women bear a disproportionate burden, with nutritional status accounting for a large share of the measured wealth-related inequality. Persistent regional and community-level heterogeneity suggests that reducing anaemia will require equity-focused, nutritionally informed, and geographically targeted interventions.

**Keywords:** Anaemia; women of reproductive age; socioeconomic inequality; concentration index; decomposition analysis; multilevel modelling; Ghana

---

## Introduction

Anaemia remains a major public-health concern among women of reproductive age, particularly in low- and lower-middle-income settings. The World Health Organization estimates that approximately 30% of women aged 15–49 years and 37% of pregnant women are affected globally, with the African Region among the most heavily affected. Anaemia has multiple causes, including micronutrient deficiencies, infection and inflammation, gynaecological and obstetric conditions, and inherited blood disorders, and its distribution is therefore shaped by both biological and social determinants.

Ghana has made only modest progress in reducing anaemia among women of reproductive age. Nationally representative estimates indicate that prevalence declined from about 45% in 2003 to 41.1% in 2022, leaving the burden persistently high. Recent analysis of the 2022 Ghana Demographic and Health Survey also reported substantially higher prevalence among pregnant than non-pregnant women and identified BMI, wealth, parity, and geographic location among the factors associated with anaemia.

Most existing Ghanaian analyses, however, have focused on prevalence and individual-level determinants. That approach can identify correlates of anaemia but does not directly quantify how unequally anaemia is distributed across the socioeconomic hierarchy, which characteristics statistically account for that inequality, or how much unexplained variation persists across communities and regions. These questions are important because a national average can mask concentration of disease among disadvantaged groups and substantial geographic heterogeneity.

Health-inequality methods provide a complementary framework. Concentration curves and concentration indices summarize whether a health outcome is disproportionately concentrated among poorer or richer groups, while decomposition methods quantify the contribution of measured characteristics to the observed socioeconomic gradient. For a binary outcome such as anaemia, the Erreygers-corrected concentration index is useful because it accounts for the bounded nature of the outcome. Multilevel models can further quantify residual variation between communities after measured individual and household characteristics have been considered.

This study therefore examined socioeconomic and geographic inequalities in anaemia among women aged 15–49 years in Ghana. Specifically, we aimed to estimate nationally representative anaemia prevalence across socioeconomic and geographic groups; quantify wealth-related inequality in anaemia; identify the measured characteristics contributing to that inequality; estimate adjusted associations with anaemia; and determine whether residual community-level heterogeneity remained after adjustment.

---

## Methods

### Study design and data source
This study is a secondary analysis of nationally representative cross-sectional data from the 2022 Ghana Demographic and Health Survey. The survey used a stratified multistage sampling design, with enumeration areas serving as primary sampling units and households sampled within clusters.

### Study population
The Ghana 2022 Individual Recode file contained 15,014 women aged 15–49 years. The primary analytic sample consisted of women with a valid DHS anaemia classification in `v457`. Women with missing or invalid anaemia measurements were excluded. Analyses involving BMI excluded records with unavailable or flagged anthropometric values.

### Outcome
The primary outcome was **any anaemia**, derived from `v457`. Women classified as having mild, moderate, or severe anaemia were coded as anaemic, and women classified as not anaemic were coded as non-anaemic. Altitude-adjusted haemoglobin (`v456`) was retained as a continuous secondary outcome.

### Socioeconomic exposure
Household socioeconomic position was assessed using the DHS wealth index. Wealth quintile (`v190`) was used for descriptive and regression analyses, while the continuous wealth score (`v191`) was used to rank women for concentration-index analysis.

### Covariates
Prespecified covariates included age group, educational attainment, urban/rural residence, region, current pregnancy status, parity, BMI category, current employment, and marital status. BMI was classified as underweight (<18.5 kg/m²), normal weight (18.5–24.9 kg/m²), overweight (25.0–29.9 kg/m²), and obesity (≥30.0 kg/m²).

### Survey design
Sampling weights were calculated as:

[
w_i=rac{v005_i}{1{,}000{,}000}.
]

Primary sampling units were defined by `v021`, and strata by `v022`. Population-level estimates incorporated weights, clustering, and stratification.

### Descriptive analysis
Participant characteristics were summarized with unweighted counts and survey-weighted percentages. Survey-weighted anaemia prevalence and 95% confidence intervals were estimated overall and by sociodemographic, reproductive, nutritional, and geographic characteristics.

### Socioeconomic inequality analysis
Women were ranked from poorest to richest using the continuous wealth score. The standard concentration index was defined as:

[
CI=rac{2}{mu}operatorname{Cov}(y,r),
]

where (y) is anaemia status, (mu) is its weighted mean, and (r) is fractional wealth rank.

Because anaemia is a bounded binary outcome, the Erreygers-corrected concentration index was used as the primary inequality measure. Negative values indicate concentration of anaemia among poorer women. Uncertainty was estimated using stratified primary-sampling-unit bootstrap resampling within DHS strata.

### Decomposition analysis
The Erreygers index was decomposed using a survey-weighted linear probability model. The model included age, education, residence, pregnancy status, parity, BMI, employment, and marital status. Wealth itself was not included as a determinant because it defined the socioeconomic ranking. The reproducible decomposition used DHS five-year age-group indicators, years of schooling, residence, pregnancy status, continuous parity, BMI, employment, and current union status. BMI was modelled with linear and quadratic terms. Domain-specific contributions and bootstrap intervals were calculated.

### Survey-weighted regression
Adjusted associations with anaemia were estimated using survey-weighted logistic regression. The fully adjusted model included age group, education, wealth quintile, residence, pregnancy status, parity, BMI category, employment, marital status, and region. Results are reported as adjusted odds ratios (aORs) with 95% confidence intervals. Overall Wald tests were used for categorical factors.

### Multilevel analysis
Two-level logistic mixed models were fitted with women nested within DHS sampling clusters. The intraclass correlation coefficient was calculated using:

[
ICC=rac{sigma_u^2}{sigma_u^2+pi^2/3}.
]

The median odds ratio quantified between-cluster heterogeneity, and the proportional change in variance compared the null and adjusted models. The multilevel analysis was treated as complementary to the design-based survey analysis.

### Sensitivity analyses
Sensitivity analyses included alternative BMI specifications, pregnancy-stratified analyses, continuous haemoglobin as a secondary outcome, alternative anaemia severity specifications where feasible, and inspection of regional influence.

### Missing data
Most prespecified socioeconomic and reproductive covariates were complete among women with valid anaemia measurements. Seven women with unavailable or flagged BMI information were excluded from analyses requiring BMI.

---

## Results

### Study population and prevalence
Of 15,014 women in the Individual Recode file, 7,557 had valid anaemia measurements. The survey-weighted prevalence of anaemia was **41.1% (95% CI 39.6%–42.6%)**.

Anaemia prevalence decreased across wealth groups, from **46.6% (95% CI 43.5%–49.7%)** in the poorest quintile to **38.8% (95% CI 35.2%–42.5%)** in the richest. Prevalence also declined with education, from **45.4%** among women with no education to **36.8%** among those with higher education. Rural women had higher prevalence than urban women (**43.4% vs 39.4%**), and currently pregnant women had higher prevalence than women who were not pregnant or were unsure (**51.4% vs 40.4%**). Prevalence was highest among underweight women (**49.3%**) and lowest among women with obesity (**33.9%**).

### Socioeconomic inequality
The standard concentration index was **-0.0358**, and the Erreygers-corrected concentration index was **-0.0589** (bootstrap 95% CI **-0.0914 to -0.0212**). The concentration curve lay predominantly above the equality line, indicating disproportionate concentration of anaemia among poorer women.

### Decomposition
BMI/nutritional status made the largest measured contribution to wealth-related inequality, accounting for approximately **77.7%** of the observed Erreygers index. Education contributed **15.6%**, residence **6.8%**, parity **4.9%**, and pregnancy status **3.8%**. The BMI-domain contribution remained negative in the 200-replicate bootstrap (**-0.0457**, 95% bootstrap interval **-0.0617 to -0.0300**). Bootstrap intervals for the smaller domains included zero.

### Adjusted associations
In the fully adjusted survey-weighted logistic model, pregnancy status, BMI category, and region showed the strongest overall evidence of association with anaemia.

Currently pregnant women had higher adjusted odds of anaemia than women who were not pregnant or were unsure (aOR **1.77**, 95% CI **1.43–2.21**). Compared with normal-weight women, overweight women had lower adjusted odds (aOR **0.73**, 95% CI **0.62–0.87**) and women with obesity had lower adjusted odds (aOR **0.60**, 95% CI **0.49–0.72**). Underweight women had aOR **1.18** (95% CI **0.96–1.47**).

Relative to Greater Accra, women in Oti had higher adjusted odds of anaemia (aOR **1.48**, 95% CI **1.11–1.98**), whereas women in Bono had lower adjusted odds (aOR **0.61**, 95% CI **0.41–0.90**).

Overall Wald tests were significant for pregnancy status, BMI category, and region (all (p<0.001) for pregnancy/BMI and (p<0.001) for region), while wealth quintile ((p=0.852)) and education ((p=0.933)) were not significant after adjustment.

### Community-level heterogeneity
Regional prevalence ranged from approximately **30.1% in Bono** to **51.8% in Oti**.

The null two-level model yielded cluster variance **0.150**, ICC **4.35%**, and MOR **1.45**. After adjustment, cluster variance declined to **0.107**, ICC to **3.14%**, and MOR to **1.37**. The proportional reduction in cluster variance was approximately **28.8%**.

---

## Discussion

This nationally representative analysis found that approximately two in five Ghanaian women of reproductive age were anaemic and that the burden was unequally distributed across socioeconomic and geographic groups. Anaemia was concentrated among poorer women, and the concentration-index decomposition suggested that nutritional status accounted for the largest measured share of the wealth-related inequality.

The adjusted regression results help distinguish population-level inequality from conditional associations. The crude gradients by wealth and education attenuated after simultaneous adjustment, while pregnancy, BMI, and region remained more prominent. This does not imply that socioeconomic circumstances are irrelevant. Instead, it suggests that wealth-related inequality may be expressed through the unequal distribution of nutritional, reproductive, and geographic characteristics.

The higher odds among pregnant women are biologically plausible because pregnancy increases iron requirements and expands plasma volume. However, the cross-sectional design precludes causal inference and does not capture all potential determinants, including iron stores, infection, supplementation adherence, or inherited blood disorders.

The strong inverse pattern between BMI and anaemia must also be interpreted cautiously. Higher BMI should not be considered causally protective. BMI is a crude marker of nutritional status and does not measure micronutrient sufficiency. The decomposition result is better understood as evidence that nutritional status is strongly socially patterned and linked statistically to the observed inequality.

Geographic heterogeneity was also substantial. Anaemia prevalence varied by more than 20 percentage points between the lowest- and highest-prevalence regions, and cluster-level heterogeneity persisted after adjustment. The remaining contextual variance may reflect unmeasured differences in food environments, malaria transmission, access to care, sanitation, environmental exposures, or other community-level factors.

These findings support equity-focused anaemia control. Ghanaian programmes should continue to prioritize pregnant and nutritionally vulnerable women while also directing attention to socioeconomically disadvantaged and high-burden geographic populations. National prevalence alone may be insufficient for monitoring progress; inequality measures can show whether improvements are reaching women at the lower end of the socioeconomic distribution.

### Strengths and limitations
Strengths include use of recent nationally representative data, explicit accounting for the DHS survey design, complementary inequality and multilevel methods, bootstrap uncertainty for inequality estimates, and sensitivity analysis of the dominant BMI contribution.

Limitations include the cross-sectional design, inability of haemoglobin alone to establish anaemia aetiology, lack of iron-status and other biological biomarkers for the full sample, the imperfect nature of BMI as a nutritional marker, and model dependence of decomposition estimates. The primary analysis also uses the anaemia classification embedded in the 2022 DHS; WHO updated haemoglobin cut-offs in 2024, so future analyses may examine how newer thresholds affect prevalence and inequality estimates.

---

## Conclusion

Anaemia remains a substantial public-health problem among women of reproductive age in Ghana and is unequally distributed across socioeconomic and geographic groups. Poorer women bear a disproportionate share of the burden, with nutritional status accounting for a large portion of the measured wealth-related inequality. Pregnancy and regional location remain important correlates, and meaningful community-level heterogeneity persists after adjustment.

Reducing anaemia in Ghana will therefore require not only population-wide interventions but also equity-focused, nutritionally informed, and geographically targeted strategies.

---

## Ethics statement

The study used de-identified secondary data from the 2022 Ghana Demographic and Health Survey. Access to the microdata was granted by The DHS Program under its data-use terms. The original survey obtained appropriate ethical approvals and informed consent from participants. No attempt was made to identify individual participants.

## Data availability

The data analysed in this study are available from The DHS Program upon reasonable request and approval. Restricted DHS microdata are not redistributed through this repository.

## Funding

No external funding was received for this study.

## Competing interests

The author declares no competing interests.

## Author contributions

**Conceptualization:** Gideon Ofosu Kyere  
**Methodology:** Gideon Ofosu Kyere  
**Formal analysis:** Gideon Ofosu Kyere  
**Data curation:** Gideon Ofosu Kyere  
**Writing – original draft:** Gideon Ofosu Kyere  
**Writing – review and editing:** Gideon Ofosu Kyere

## Figures

- Figure 1: `../figures/figure1_concentration_curve.svg`
- Figure 2: `../figures/figure2_regional_prevalence.svg`
- Figure 3: `../figures/figure3_wealth_gradient.svg`
- Figure 4: `../figures/figure4_decomposition.svg`

## Core references

1. World Health Organization. Anaemia. Fact sheet. Updated 10 February 2025.
2. World Health Organization. Guideline on haemoglobin cutoffs to define anaemia in individuals and populations. Geneva: WHO; 2024.
3. World Health Organization. Accelerating anaemia reduction: a comprehensive framework for action. Geneva: WHO; 2023.
4. Agulu GG, Ahissou NCA, Kamiya Y, Baiden F, Matsui M. Anaemia prevalence and risk factors among nonpregnant and pregnant women of reproductive age in Ghana: an analysis of the Ghana demographic and health survey data. *Tropical Medicine and Health*. 2025;53(1):118. doi:10.1186/s41182-025-00792-8.
5. Ghana Statistical Service, Ghana Health Service, and ICF. Ghana Demographic and Health Survey 2022.
6. World Health Organization. Best practices for haemoglobin measurement in population-level anaemia surveys. Geneva: WHO; 2024.

> The final submission version should add the methodological references for concentration indices, the Erreygers correction, decomposition methods, multilevel ICC/MOR, and DHS survey analysis before journal submission.
