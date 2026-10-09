# Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana

## Abstract

### Background
Anaemia remains common among Ghanaian women of reproductive age, but national estimates may conceal socioeconomic and geographic inequalities. We quantified wealth-related inequality in anaemia and examined its measured contributors and community-level variation.

### Methods
We conducted a cross-sectional analysis of nationally representative data for women aged 15–49 years with valid anaemia measurements. Survey-weighted prevalence, Erreygers-corrected concentration indices, decomposition analysis, survey-weighted logistic regression, and multilevel logistic models were used.

### Results
Among 7,557 women, anaemia prevalence was **41.1% (95% CI 39.6–42.6%)**, declining from **46.6%** in the poorest wealth quintile to **38.8%** in the richest. The Erreygers index was **-0.0589** (95% bootstrap CI **-0.0914 to -0.0212**), indicating concentration among poorer women. BMI/nutritional status contributed **77.7%** of measured inequality. Pregnancy was associated with higher adjusted odds of anaemia (aOR **1.77**, 95% CI **1.43–2.21**). Regional and residual community-level heterogeneity persisted after adjustment.

### Conclusions
Anaemia in Ghana is socioeconomically and geographically patterned. Equity-focused, nutritionally informed, and geographically targeted interventions are warranted.

**Keywords:** anaemia; women of reproductive age; socioeconomic inequality; concentration index; Ghana

## Introduction

Anaemia remains one of the most common haematological and nutritional public-health problems affecting women of reproductive age. The World Health Organization (WHO) estimates that roughly three in ten women aged 15–49 years worldwide are anaemic, with pregnant women and populations in low- and middle-income countries carrying a particularly large burden.[1,2] Anaemia is not a single disease entity. It can arise from iron and other micronutrient deficiencies, infection and inflammation, blood loss, gynaecological and obstetric conditions, and inherited disorders. Its distribution therefore reflects both biological vulnerability and wider social conditions.

Ghana continues to experience a substantial burden. The 2022 Ghana Demographic and Health Survey (GDHS) reported anaemia in about two in five women of reproductive age.[3] Recent Ghanaian work using the same national survey has also documented higher prevalence among pregnant women and associations with nutritional status, parity, wealth and geographic location.[4] These studies establish the continuing importance of anaemia, but conventional prevalence comparisons and determinant models do not directly quantify how unequally the burden is distributed across the socioeconomic hierarchy.

Multicountry analyses have examined anaemia severity using multilevel models,[5,6] while spatial studies have described geographic variation in anaemia among women across sub-Saharan Africa and within Ethiopia.[7,8] Subnational mapping in West and Central Africa provides a further geographic perspective.[9] Decomposition has also been used to examine changes in anaemia prevalence between survey periods in selected countries, including Ghana,[10] a different question from decomposing wealth-related inequality within one survey.

That distinction matters for public-health planning. A national prevalence may decline while disadvantaged groups remain behind, and a non-significant adjusted wealth coefficient does not necessarily mean that population-level socioeconomic inequality has disappeared. Socioeconomic position is related to nutritional, educational, reproductive and geographic characteristics that may also be associated with anaemia. Measures designed specifically for health inequality can therefore provide information that ordinary regression coefficients do not.

Concentration curves and concentration indices summarize the distribution of a health outcome across the full socioeconomic ranking. For bounded outcomes such as binary anaemia status, the Erreygers correction provides an interpretable normalized measure of inequality.[11] Decomposition methods can then estimate the statistical contribution of measured characteristics to the observed concentration of disease.[12] Multilevel models add a further perspective by quantifying variation between communities that remains after individual characteristics are considered.[13]

This study examined socioeconomic and geographic inequalities in anaemia among women aged 15–49 years in Ghana. We aimed to estimate nationally representative prevalence across population groups, quantify wealth-related inequality, identify measured contributors to that inequality, estimate adjusted associations with anaemia, and determine whether meaningful community-level heterogeneity persisted after adjustment.

## Methods

### Study design and data source

We conducted a secondary cross-sectional analysis of the 2022 GDHS, a nationally representative household survey implemented using a stratified multistage sampling design.[3] Enumeration areas served as primary sampling units, and households were selected within clusters. The Individual Recode file contained 15,014 women aged 15–49 years.

The primary analytic population comprised women with a valid haemoglobin-based anaemia classification. Of the 15,014 women in the Individual Recode file, 7,557 met this criterion. Analyses requiring BMI excluded seven additional women with unavailable or flagged BMI information.

### Outcome

The primary outcome was **any anaemia**, derived from the DHS anaemia classification variable. Women classified as having mild, moderate or severe anaemia were coded as anaemic, and women classified as not anaemic were coded as non-anaemic. The classification was based on the haemoglobin definition embedded in the 2022 GDHS. WHO published updated haemoglobin guidance after the survey was conducted; the survey definition was retained to preserve comparability with the official national estimates.[14]

### Socioeconomic and explanatory variables

Household socioeconomic position was measured using the DHS wealth index. Wealth quintiles were used for descriptive and regression analyses. The continuous wealth score was used to rank women from poorest to richest for concentration-index analysis.

Prespecified covariates were age group, educational attainment, urban or rural residence, administrative region, current pregnancy status, parity, BMI category, current employment and marital status. BMI was categorized as underweight (<18.5 kg/m²), normal weight (18.5–24.9 kg/m²), overweight (25.0–29.9 kg/m²) and obesity (≥30.0 kg/m²). Covariates were selected on substantive grounds rather than through stepwise significance testing.

### Complex-survey analysis

Population-level analyses incorporated the DHS individual sampling weight, primary sampling unit and sampling stratum. The individual weight was calculated as `v005/1,000,000`. Survey-weighted proportions and 95% confidence intervals were estimated overall and within demographic, socioeconomic, reproductive, nutritional and geographic subgroups.

### Socioeconomic inequality

Women were ranked from poorest to richest using the continuous wealth score. We first calculated the standard concentration index and plotted the concentration curve. Because anaemia is a bounded binary outcome, the Erreygers-corrected concentration index was used as the primary inequality measure.[11] A negative value indicates that anaemia is concentrated disproportionately among poorer women.

Uncertainty for the corrected index was assessed using stratified primary-sampling-unit bootstrap resampling within DHS strata.

### Decomposition analysis

The Erreygers index was decomposed using a survey-weighted linear probability model based on established concentration-index decomposition methods.[12] The decomposition model included age, years of education, residence, pregnancy status, parity, BMI, employment and marital status. Wealth itself was not entered as a determinant because it defined the socioeconomic ranking. The reproducible specification used DHS five-year age-group indicators and modelled BMI with linear and quadratic terms.

For each domain, the contribution reflected the combination of its association with anaemia and its socioeconomic distribution. Bootstrap resampling was used to assess uncertainty. Because decomposition is model dependent, all contributions were interpreted as statistical rather than causal.

### Adjusted regression

Survey-weighted logistic regression was used to estimate adjusted associations with anaemia. The full model included age group, education, wealth quintile, residence, pregnancy status, parity, BMI category, employment, marital status and region. Adjusted odds ratios (aORs) and 95% confidence intervals were reported. Overall Wald tests were used for categorical variables.

### Community-level heterogeneity

Two-level random-intercept logistic models were fitted with women nested within DHS clusters. A null model quantified baseline clustering, and an adjusted model included the same covariates as the primary regression model. Cluster heterogeneity was summarized using the latent-variable intraclass correlation coefficient (ICC) and median odds ratio (MOR), as recommended for multilevel logistic analyses.[13] The proportional change in variance quantified the reduction in between-cluster variance after adjustment.

The multilevel models used variational Bayes with normally distributed fixed-effect priors (standard deviation 2) and a normal prior on log cluster standard deviation (standard deviation 1). These models were not survey-weighted and were complementary contextual analyses; national prevalence and inequality estimates remained based on the complex survey design. The optimizer emitted a convergence warning in the recorded validation, so the variance-component estimates require cautious interpretation; matching stored values does not establish numerical convergence.

### Sensitivity and missing-data analyses

Recorded exploratory checks examined alternative BMI specifications, pregnancy-stratified patterns and regional prevalence. Continuous haemoglobin and alternative severity analyses were planned, but corresponding executable results are not available in this repository and are not presented as completed sensitivity analyses. Most prespecified socioeconomic and reproductive covariates were complete in the analytic sample. Only seven women were excluded from BMI-dependent models because of unavailable or flagged BMI values.

## Results

### Study population and prevalence

Among 7,557 women with valid anaemia measurements, the survey-weighted prevalence of anaemia was **41.1% (95% CI 39.6–42.6%)**.

A socioeconomic gradient was evident. Anaemia prevalence was **46.6% (95% CI 43.5–49.7%)** among women in the poorest wealth quintile and **38.8% (95% CI 35.2–42.5%)** among those in the richest quintile. Prevalence also declined across educational categories, from **45.4%** among women with no formal education to **36.8%** among those with higher education.

Rural women had higher prevalence than urban women (**43.4% vs 39.4%**). Currently pregnant women had substantially higher prevalence than women who were not pregnant or were unsure (**51.4% vs 40.4%**). Nutritional differences were also marked: prevalence was **49.3%** among underweight women, **44.6%** among women of normal weight, **37.6%** among overweight women and **33.9%** among women with obesity (Table I).

### Wealth-related inequality

The standard concentration index was **-0.0358**, while the Erreygers-corrected concentration index was **-0.0589**. The stratified PSU bootstrap 95% confidence interval for the Erreygers index was **-0.0914 to -0.0212**, excluding zero. The concentration curve lay predominantly above the line of equality, indicating that poorer women accounted for a disproportionate share of anaemia (Figure 1).

### Decomposition of inequality

BMI/nutritional status made the largest measured contribution to wealth-related inequality, accounting for approximately **77.7%** of the observed Erreygers index. Education contributed **15.6%**, residence **6.8%**, parity **4.9%** and pregnancy status **3.8%**. Age, employment and marital/union status made small offsetting contributions, and the residual also offset part of the pro-poor inequality.

The BMI-domain contribution remained consistently negative in the 200-replicate bootstrap (**-0.0457**, 95% bootstrap interval **-0.0617 to -0.0300**). Bootstrap intervals for the smaller domains included zero, so their individual contributions should be interpreted cautiously.

### Adjusted associations with anaemia

Pregnancy status, BMI category and region showed the strongest overall evidence of association with anaemia in the fully adjusted survey-weighted model (Table II).

Currently pregnant women had higher adjusted odds of anaemia than women who were not pregnant or were unsure (aOR **1.77**, 95% CI **1.43–2.21**). Compared with normal-weight women, overweight women had lower adjusted odds (aOR **0.73**, 95% CI **0.62–0.87**) and women with obesity had lower adjusted odds (aOR **0.60**, 95% CI **0.49–0.72**). Underweight women had higher estimated odds, but the confidence interval included the null (aOR **1.18**, 95% CI **0.96–1.47**).

Regional differences also persisted. Relative to Greater Accra, women in Oti had higher adjusted odds of anaemia (aOR **1.48**, 95% CI **1.11–1.98**), whereas women in Bono had lower adjusted odds (aOR **0.61**, 95% CI **0.41–0.90**). Weighted regional prevalence ranged from approximately **30.1% in Bono** to **51.8% in Oti** (Figure 2).

The overall Wald tests for wealth quintile and education were not statistically significant after adjustment, despite the clear crude socioeconomic gradients. This pattern is compatible with the inequality analysis: socioeconomic position may operate partly through characteristics such as nutrition, reproductive status and geography that are also included in the adjusted model.

### Community-level heterogeneity

The null multilevel model had cluster-level variance **0.150**, corresponding to ICC **4.35%** and MOR **1.45**. After adjustment, cluster variance declined to **0.107**, with ICC **3.14%** and MOR **1.37**. These estimates were reproduced with the variational-Bayes implementation. Measured covariates therefore accounted for approximately **28.8%** of the between-cluster variance, while residual contextual heterogeneity remained.

## Discussion

### Main finding of this study

Anaemia affected about two in five Ghanaian women of reproductive age and was unequally distributed across both socioeconomic and geographic groups. The wealth-related concentration index showed a disproportionate burden among poorer women. Nutritional status accounted for the largest measured component of that inequality, while pregnancy and region remained prominent correlates after multivariable adjustment. Community-level heterogeneity also persisted beyond measured individual characteristics.

### What is already known on this topic

The high national burden is consistent with the 2022 GDHS and recent analysis of anaemia among Ghanaian women.[3,4] Pregnancy is a well-recognized period of increased anaemia vulnerability because iron requirements increase and plasma volume expands. Nutritional status, reproductive history and socioeconomic conditions have also been repeatedly implicated in anaemia risk.[1,4]

The inverse association between higher BMI categories and anaemia has been reported in other cross-sectional work, including Ghanaian analyses.[4] It should not be interpreted as evidence that overweight or obesity prevents anaemia. BMI does not directly measure iron stores, diet quality or micronutrient sufficiency, and excess adiposity carries substantial health risks of its own.

### What this study adds

The principal contribution is to move beyond prevalence and individual determinant models by quantifying how the burden is distributed across the socioeconomic hierarchy. The negative Erreygers index demonstrates that anaemia is not simply common; it is disproportionately concentrated among poorer women.

The decomposition further suggests that this inequality is strongly connected to the unequal socioeconomic distribution of nutritional status. This helps explain why the crude wealth gradient can coexist with weak conditional wealth coefficients after multivariable adjustment. Adjustment for these correlated characteristics can attenuate the conditional wealth coefficient without erasing population-level socioeconomic inequality. This analysis cannot distinguish mediation from confounding or establish temporal ordering.

The geographic findings add a second layer. More than 20 percentage points separated the lowest- and highest-prevalence regions, and residual between-cluster heterogeneity remained after adjustment. Contextual conditions not captured in the individual record—such as food environments, malaria transmission, sanitation, local health-service access, environmental exposures or community-level deprivation—may contribute to this variation.

Ghanaian intervention research includes a prospective cohort evaluation of school-based iron and folic acid supplementation among adolescent girls.[15] That evidence concerns a specific programme and population; our cross-sectional analysis does not estimate intervention effects.

From a public-health perspective, these results argue against relying on national averages alone. Equity-sensitive monitoring can indicate whether reductions in anaemia are reaching poorer women, and geographic surveillance can identify areas where universal strategies may need additional targeted support.

### Limitations of this study

The cross-sectional design prevents causal inference and does not establish temporal ordering. Haemoglobin identifies anaemia but cannot determine its aetiology; the data therefore cannot distinguish iron-deficiency anaemia from anaemia associated with infection, inflammation, inherited haemoglobin disorders, blood loss or other micronutrient deficiencies.

BMI is an imperfect proxy for nutritional status, and the large decomposition contribution should be interpreted as a statistical pattern rather than a recommendation to increase body weight. Decomposition estimates are also sensitive to model specification, although the BMI result was similar under alternative parameterisation.

Selection into the haemoglobin-tested analytic sample could introduce bias if women without valid measurements differed systematically in ways not fully addressed by survey weighting. Measurement error is also possible for self-reported reproductive and socioeconomic variables. Nevertheless, the close reproduction of the official national anaemia estimate provides an important validation of the analytic setup.

The findings are nationally relevant to Ghanaian women aged 15–49 years represented by the survey, but they should not be generalized to men, children, women older than 49 years or populations outside Ghana without additional evidence.

Finally, the analysis used the anaemia classification embedded in the 2022 GDHS. WHO subsequently updated haemoglobin cut-offs and measurement guidance,[14] and future research should evaluate whether newer definitions materially alter prevalence or inequality estimates.

## Conclusion

Anaemia among women of reproductive age in Ghana is both socioeconomically and geographically patterned. Poorer women bear a disproportionate burden, with nutritional status accounting for a large share of the measured inequality. Pregnancy and regional location remain important correlates, and residual community-level heterogeneity persists after adjustment.

Reducing anaemia will therefore require population-wide prevention alongside equity-focused, nutritionally informed and geographically targeted strategies. Monitoring socioeconomic inequality together with national prevalence could help ensure that progress reaches women carrying the greatest burden.

## Acknowledgements

We thank The DHS Program, the Ghana Statistical Service and ICF for making the 2022 Ghana Demographic and Health Survey data available for research.

OpenAI ChatGPT was used to assist with code development, statistical workflow documentation and manuscript drafting and language editing. All analytic decisions, numerical outputs, interpretations and final manuscript text were reviewed and verified by the authors, who take full responsibility for the work.

## Author contributions

Contributor roles and final manuscript approval are pending author confirmation. This working version is not ready for submission; see `submission/author_confirmation.md`.

## Ethics statement

The study used de-identified secondary data from the 2022 Ghana Demographic and Health Survey. Access to the microdata was granted by The DHS Program under its data-use terms. The original survey obtained appropriate ethical approvals and informed consent from participants. No attempt was made to identify individual participants.

## Data availability

The microdata analysed in this study are available from The DHS Program following application and approval. Restricted DHS microdata are not redistributed through the project repository.

## Funding

No external funding was received.

## Conflict of interest

The authors declare no conflict of interest.

## References

1. World Health Organization. Anaemia. Geneva: World Health Organization; 2025.
2. World Health Organization. *WHO global anaemia estimates: key findings, 2025*. Geneva: World Health Organization; 2025. ISBN 978-92-4-011393-0.
3. Ghana Statistical Service (GSS), ICF. *Ghana Demographic and Health Survey 2022*. Accra, Ghana and Rockville, Maryland, USA: GSS and ICF; 2024.
4. Agulu GG, Ahissou NCA, Kamiya Y, Baiden F, Matsui M. Anaemia prevalence and risk factors among nonpregnant and pregnant women of reproductive age in Ghana: an analysis of the Ghana demographic and health survey data. *Trop Med Health*. 2025;53:118. doi:10.1186/s41182-025-00792-8.
5. Mare KU, Aychiluhm SB, Sabo KG, et al. Determinants of anemia level among reproductive-age women in 29 Sub-Saharan African countries: a multilevel mixed-effects modelling with ordered logistic regression analysis. *PLoS One*. 2023;18(11):e0294992. doi:10.1371/journal.pone.0294992.
6. Tirore LL, Areba AS, Habte A, Desalegn M, Kebede AS. Prevalence and associated factors of severity levels of anemia among women of reproductive age in sub-Saharan Africa: a multilevel ordinal logistic regression analysis. *Front Public Health*. 2024;11:1349174. doi:10.3389/fpubh.2023.1349174.
7. Correa-Agudelo E, Kim HY, Musuka GN, et al. The epidemiological landscape of anemia in women of reproductive age in sub-Saharan Africa. *Sci Rep*. 2021;11:11955. doi:10.1038/s41598-021-91198-z.
8. Kibret KT, Chojenta C, D'Arcy E, Loxton D. Spatial distribution and determinant factors of anaemia among women of reproductive age in Ethiopia: a multilevel and spatial analysis. *BMJ Open*. 2019;9:e027276. doi:10.1136/bmjopen-2018-027276.
9. Baye K, Hailu BA, Nanama S, Ntambi J, Laillou A. Subnational mapping of anaemia and aetiologic factors in the West and Central African region. *Public Health Nutr*. 2025;28:e6. doi:10.1017/S1368980024002222.
10. Salifu MG, Da-Costa Vroom FB, Guure C. Anaemia among women of reproductive age in selected sub-Saharan African countries: multivariate decomposition analyses of the demographic and health surveys data 2008–2018. *Front Public Health*. 2024;11:1128214. doi:10.3389/fpubh.2023.1128214.
11. Erreygers G. Correcting the concentration index. *J Health Econ*. 2009;28:504–515. doi:10.1016/j.jhealeco.2008.02.003.
12. Wagstaff A, van Doorslaer E, Watanabe N. On decomposing the causes of health sector inequalities with an application to malnutrition inequalities in Vietnam. *J Econometrics*. 2003;112:207–223. doi:10.1016/S0304-4076(02)00161-6.
13. Merlo J, Chaix B, Ohlsson H, et al. A brief conceptual tutorial of multilevel analysis in social epidemiology: using measures of clustering in multilevel logistic regression to investigate contextual phenomena. *J Epidemiol Community Health*. 2006;60:290–297. doi:10.1136/jech.2004.029454.
14. World Health Organization. *Guideline on haemoglobin cutoffs to define anaemia in individuals and populations*. Geneva: World Health Organization; 2024.
15. Gosdin L, Sharma AJ, Tripp K, et al. A school-based weekly iron and folic acid supplementation program effectively reduces anemia in a prospective cohort of Ghanaian adolescent girls. *J Nutr*. 2021;151:1646–1655. doi:10.1093/jn/nxab024.

## Main displays

**Table I.** Weighted participant characteristics and anaemia prevalence.
Source: `results/table1_weighted_characteristics.md`

**Table II.** Survey-weighted adjusted associations with anaemia.
Source: `results/table2_full_adjusted_model.md`

**Figure 1. Concentration curve for anaemia by household wealth rank.**
The concentration curve plots the cumulative share of anaemia against the cumulative weighted population ranked from poorest to richest. The 45-degree line represents socioeconomic equality. The observed curve lies predominantly above the equality line, consistent with a disproportionate concentration of anaemia among poorer women. The Erreygers-corrected concentration index was -0.0589 (95% bootstrap CI -0.0914 to -0.0212).

**Alt text:** Line graph comparing the anaemia concentration curve with a diagonal equality line. The anaemia curve lies mostly above the equality line, showing that poorer women account for a larger share of anaemia than their population share.

Source: `figures/figure1_concentration_curve.svg`

**Figure 2. Survey-weighted anaemia prevalence by region.**
Survey-weighted anaemia prevalence and 95% confidence intervals are shown for Ghana's 16 regions. The dashed reference line marks the national prevalence of 41.1%. Regional prevalence ranged from approximately 30.1% in Bono to 51.8% in Oti.

**Alt text:** Horizontal point-and-whisker plot of anaemia prevalence across 16 Ghanaian regions. Bono has the lowest estimate at about 30%, Oti the highest at about 52%, and several northern regions are above the national prevalence of 41%.

Source: `figures/figure2_regional_prevalence.svg`
