# Socioeconomic and Geographic Inequalities in Anaemia Among Women of Reproductive Age in Ghana

## Abstract

### Background
Anaemia is common among Ghanaian women of reproductive age. We quantified wealth-related inequality, examined its measured contributors and assessed geographic and community-level variation that national estimates may conceal.

### Methods
We analysed nationally representative cross-sectional data for women aged 15–49 years with valid anaemia measurements. Analyses included survey-weighted prevalence and logistic regression, Erreygers-corrected concentration indices, inequality decomposition and multilevel logistic models.

### Results
Among 7,557 women, anaemia prevalence was 41.1% (95% CI 39.6–42.6%), declining from 46.6% in the poorest wealth quintile to 38.8% in the richest. The Erreygers index was -0.0589 (95% bootstrap CI -0.0924 to -0.0249), indicating concentration among poorer women. BMI/nutritional status contributed 77.7% of measured inequality. Pregnancy was associated with higher adjusted odds of anaemia (aOR 1.77, 95% CI 1.43–2.21). Regional and residual community-level heterogeneity persisted after adjustment.

### Conclusions
The findings support monitoring socioeconomic and geographic differences in anaemia and considering these differences in prevention strategies that address nutritional needs.

Keywords: anaemia; women of reproductive age; socioeconomic inequality; concentration index; Ghana

## Introduction

Anaemia is a common haematological and nutritional public-health problem among women of reproductive age. The World Health Organization (WHO) estimates that roughly three in ten women aged 15–49 years worldwide are anaemic. The burden is particularly high among pregnant women and in low- and middle-income countries.[1,2] Anaemia has several causes, including iron and other micronutrient deficiencies, infection, inflammation, blood loss, gynaecological and obstetric conditions, and inherited disorders. Its distribution reflects biological vulnerability as well as social conditions.

The 2022 Ghana Demographic and Health Survey (GDHS) reported anaemia in about two in five women of reproductive age.[3] Agulu and colleagues subsequently examined anaemia prevalence and associated factors separately among pregnant and nonpregnant Ghanaian women using the 2022 GDHS.[4] This establishes the contemporary burden and identifies conditional associations, but such regression estimates do not by themselves quantify how anaemia is distributed along the full wealth ranking or partition the measured contributions to that inequality.

Multicountry analyses have examined anaemia severity using multilevel models,[5,6] while spatial studies have described geographic variation in anaemia among women across sub-Saharan Africa and within Ethiopia.[7,8] Subnational mapping in West and Central Africa provides a further geographic perspective.[9] Decomposition has also been used to examine changes in anaemia prevalence between survey periods in selected countries, including Ghana,[10] a different question from decomposing wealth-related inequality within one survey.

National prevalence can decline while disadvantaged groups continue to carry a greater burden. A non-significant adjusted wealth coefficient also does not establish the absence of population-level inequality. Socioeconomic position is related to nutritional, educational, reproductive and geographic characteristics, which may themselves be associated with anaemia. Health-inequality measures describe the distribution of anaemia across the population, complementing the conditional associations estimated by regression.

Concentration curves and indices summarise how a health outcome is distributed across the socioeconomic ranking. The Erreygers correction normalises the index for bounded outcomes such as binary anaemia status.[11] Decomposition estimates the statistical contributions of measured characteristics to this inequality.[12] Multilevel models quantify variation between communities after accounting for individual characteristics.[13]

Against that background, we examined socioeconomic and geographic inequalities in anaemia among women aged 15–49 years in Ghana. Specifically, we estimated design-adjusted prevalence across population groups; quantified wealth-related inequality using a bounded-outcome concentration index; decomposed that index into measured statistical contributions; and assessed adjusted individual-level associations and residual between-community heterogeneity. The central contribution is the decomposition of wealth-ranked inequality rather than a claim to be the first analysis of anaemia prevalence or risk factors using the 2022 GDHS.

## Methods

### Study design and data source

We conducted a secondary cross-sectional analysis of the 2022 GDHS, a nationally representative household survey implemented using a stratified multistage sampling design.[3] Enumeration areas served as primary sampling units, and households were selected within clusters. The Individual Recode file contained 15,014 women aged 15–49 years.

The primary analytic sample included women with a valid haemoglobin-based anaemia classification. Of the 15,014 women in the Individual Recode file, 7,557 met this criterion. Models requiring BMI excluded seven women whose BMI values were unavailable or flagged.

### Outcome

The primary outcome was any anaemia, derived from the DHS anaemia classification variable. Women classified as having mild, moderate or severe anaemia were coded as anaemic, and women classified as not anaemic were coded as non-anaemic. The classification was based on the haemoglobin definition embedded in the 2022 GDHS. WHO published updated haemoglobin guidance after the survey was conducted; the survey definition was retained to preserve comparability with the official national estimates.[14]

### Socioeconomic and explanatory variables

Household socioeconomic position was measured using the DHS wealth index. Wealth quintiles were used for descriptive and regression analyses. The continuous wealth score was used to rank women from poorest to richest for concentration-index analysis.

Prespecified covariates were age group, educational attainment, urban or rural residence, administrative region, current pregnancy status, parity, BMI category, current employment and marital status. BMI was categorised as underweight (<18.5 kg/m²), normal weight (18.5–24.9 kg/m²), overweight (25.0–29.9 kg/m²) and obesity (≥30.0 kg/m²). Covariate selection was based on substantive considerations, without stepwise significance testing.

### Complex-survey analysis

Population-level analyses incorporated the DHS individual sampling weight, primary sampling unit (PSU) and sampling stratum. The individual weight was calculated as `v005/1,000,000`. For binary anaemia status $Y_i$, weighted prevalence was estimated as

$\widehat P=\frac{\sum_{i=1}^n w_iY_i}{\sum_{i=1}^n w_i},$

where $w_i$ denotes the sampling weight. For Taylor linearisation, observation $i$ contributed $z_i=w_i(Y_i-\widehat P)/\sum_iw_i$. Writing $Z_{hj}=\sum_{i\in(h,j)}z_i$ for the sum within PSU $j$ in stratum $h$, the implemented design variance was

$\widehat{\operatorname{Var}}(\widehat P)=\sum_{h=1}^H\frac{m_h}{m_h-1}\sum_{j=1}^{m_h}(Z_{hj}-\overline Z_h)^2,$

where $m_h$ is the number of sampled PSUs in stratum $h$. The code used normal-reference 95% confidence intervals, $\widehat P\pm1.96\sqrt{\widehat{\operatorname{Var}}(\widehat P)}$. For subgroup estimates, the full available survey design was retained and out-of-domain observations contributed zero to the linearised variable.

### Socioeconomic inequality

Women were ranked from poorest to richest using the continuous wealth score. Ties were assigned survey-weighted fractional midranks $R_i$. Let $\mu=\sum_iw_iY_i/\sum_iw_i$ and let $\operatorname{Cov}_w$ denote a covariance calculated with normalised sampling weights. The standard concentration index and its Erreygers correction for the binary outcome bounded by zero and one were, respectively,[11]

$C_Y=\frac{2}{\mu}\operatorname{Cov}_w(Y,R),\qquad E_Y=4\mu C_Y=8\operatorname{Cov}_w(Y,R).$

The concentration curve displays cumulative weighted anaemia against cumulative weighted population share ordered by wealth. A negative index indicates a disproportionate concentration of anaemia among poorer women. The Erreygers index was the primary measure because anaemia is binary. A percentile 95% confidence interval for the full-sample corrected index was calculated from 5,000 bootstrap replicates resampling PSUs within DHS strata (seed 20261008); the decomposition used a separate 200-replicate bootstrap.

### Decomposition analysis

The Erreygers index was decomposed using a survey-weighted linear probability model based on established concentration-index decomposition methods.[12] The decomposition model included age, years of education, residence, pregnancy status, parity, BMI, employment and marital status. Wealth itself was not entered as a determinant because it defined the socioeconomic ranking. The reproducible specification used DHS five-year age-group indicators and modelled BMI with linear and quadratic terms.

Writing the weighted linear probability model as $Y_i=\alpha+\sum_{k=1}^K\beta_kX_{ki}+\varepsilon_i$, the implemented absolute contribution for term $k$ was

$D_k=8\widehat\beta_k\operatorname{Cov}_w(X_k,R),\qquad E_Y=\sum_{k=1}^KD_k+E_{\mathrm{res}},$

where $E_{\mathrm{res}}$ was calculated as the observed index minus the sum of measured contributions. Each domain's contribution was the sum of its constituent terms and its percentage share was $100D_{\mathrm{domain}}/E_Y$. In particular, the BMI/nutritional-status domain combined the contributions of BMI and BMI squared, rather than those of categorical BMI indicators. The decomposition was fitted to complete cases with BMI and other specified variables present ($n=7,550$), and its $E_Y$ denominator was recalculated on that same analytic sample; this is distinct from the full-sample inequality estimate ($n=7,557$). PSU-within-stratum bootstrap resampling (200 replicates) assessed contribution uncertainty. Contributions depend on the model specification and describe statistical patterns, not causal effects.

### Adjusted regression

Survey-weighted logistic regression was used to estimate adjusted associations with anaemia:

$\log\frac{p_i}{1-p_i}=\beta_0+\sum_{k=1}^K\beta_kX_{ki},\qquad \mathrm{aOR}_k=\exp(\widehat\beta_k),$

where $p_i=\Pr(Y_i=1\mid X_i)$. The full model included age group, education, wealth quintile, residence, pregnancy status, parity, BMI category, employment, marital status and region. The model was fitted by weighted binomial maximum likelihood. Design-based standard errors were estimated using the stratified PSU-score sandwich covariance $\widehat V=A^{-1}BA^{-1}$, where $A$ is the weighted model information and $B$ sums centred PSU scores within strata with finite-PSU corrections. The implemented coefficients used normal-reference 95% intervals and chi-square Wald tests for categorical terms; these were not finite-design-degrees-of-freedom $t$ or $F$ tests. Odds ratios were not interpreted as prevalence ratios.

### Community-level heterogeneity

Two-level random-intercept logistic models were fitted with women nested within DHS clusters. A null model quantified baseline clustering, and an adjusted model included the same covariates as the primary regression model. Writing $p_{ij}$ for the anaemia probability of woman $i$ in DHS cluster $j$, the supplementary random-intercept specification was

$\operatorname{logit}(p_{ij})=\beta_0+\sum_{k=1}^K\beta_kX_{kij}+u_j,\qquad u_j\sim N(0,\sigma_u^2).$

We summarised cluster heterogeneity using the latent-variable intraclass correlation coefficient (ICC), median odds ratio (MOR), and proportional change in variance (PCV):[13]

$\mathrm{ICC}=\frac{\sigma_u^2}{\sigma_u^2+\pi^2/3},\quad \mathrm{MOR}=\exp\!\left[\sqrt{2\sigma_u^2}\,\Phi^{-1}(0.75)\right],\quad \mathrm{PCV}=\frac{\sigma_{u,0}^2-\sigma_{u,1}^2}{\sigma_{u,0}^2},$

where subscripts 0 and 1 denote null and adjusted models. PCV was expressed as a proportion in code and as a percentage when multiplied by 100 in reporting.

The multilevel models used variational Bayes with normally distributed fixed-effect priors on the scaled design matrix (standard deviation 2) and a normal prior on log cluster standard deviation (standard deviation 1). These models were not survey-weighted and were complementary contextual analyses; national prevalence and inequality estimates remained based on the complex survey design. Both final seeded BFGS fits converged at a gradient tolerance of 1e-5; the earlier stricter-tolerance precision-loss diagnostic is documented in the supplement.

### Sensitivity and missing-data analyses

Exploratory checks examined alternative BMI specifications, pregnancy-stratified patterns and regional prevalence. Planned analyses of continuous haemoglobin and alternative anaemia-severity definitions have no executable results in the repository and are not reported as completed sensitivity analyses. Most prespecified socioeconomic and reproductive covariates were complete in the analytic sample. Models requiring BMI excluded seven women with unavailable or flagged values.

## Results

### Study population and prevalence

Among 7,557 women with valid anaemia measurements, the survey-weighted prevalence of anaemia was 41.1% (95% CI 39.6–42.6%).

Anaemia prevalence was 46.6% (95% CI 43.5–49.7%) among women in the poorest wealth quintile and 38.8% (95% CI 35.2–42.5%) among those in the richest quintile. Prevalence also declined across educational categories, from 45.4% among women with no formal education to 36.8% among those with higher education.

Rural women had higher prevalence than urban women (43.4% vs 39.4%). Currently pregnant women had higher prevalence than women who were not pregnant or were unsure (51.4% vs 40.4%). Prevalence also differed by BMI category: 49.3% among underweight women, 44.6% among women of normal weight, 37.6% among overweight women and 33.9% among women with obesity (Table I).

### Wealth-related inequality

The standard concentration index was -0.0358, while the Erreygers-corrected concentration index was -0.0589. The stratified PSU bootstrap 95% confidence interval for the Erreygers index was -0.0924 to -0.0249, excluding zero. The concentration curve lay predominantly above the line of equality, indicating that poorer women accounted for a disproportionate share of anaemia (Figure 1).

### Decomposition of inequality

BMI/nutritional status made the largest measured contribution to wealth-related inequality, accounting for approximately 77.7% of the observed Erreygers index. Education contributed 15.6%, residence 6.8%, parity 4.9% and pregnancy status 3.8%. Age, employment and marital/union status made small offsetting contributions, and the residual also offset part of the pro-poor inequality.

The BMI-domain contribution remained consistently negative in the 200-replicate bootstrap (-0.0457, 95% bootstrap interval -0.0617 to -0.0300). Bootstrap intervals for the smaller domains included zero, so their individual contributions should be interpreted cautiously.

### Adjusted associations with anaemia

Overall Wald tests provided the strongest evidence of association for pregnancy status, BMI category and region in the fully adjusted survey-weighted model (Table II).

Currently pregnant women had higher adjusted odds of anaemia than women who were not pregnant or were unsure (aOR 1.77, 95% CI 1.43–2.21). Compared with normal-weight women, overweight women had lower adjusted odds (aOR 0.73, 95% CI 0.62–0.87) and women with obesity had lower adjusted odds (aOR 0.60, 95% CI 0.49–0.72). Underweight women had higher estimated odds, but the confidence interval included the null (aOR 1.18, 95% CI 0.96–1.47).

Regional differences also persisted. Relative to Greater Accra, women in Oti had higher adjusted odds of anaemia (aOR 1.48, 95% CI 1.11–1.98), whereas women in Bono had lower adjusted odds (aOR 0.61, 95% CI 0.41–0.90). Weighted regional prevalence ranged from approximately 30.1% in Bono to 51.8% in Oti (Figure 2).

The overall Wald tests for wealth quintile and education were not statistically significant after adjustment, although prevalence differed across these groups. These conditional associations and the population-level inequality index describe different quantities. Including correlated characteristics, such as nutrition, reproductive status and geography, can attenuate adjusted wealth coefficients; this cross-sectional analysis cannot establish a causal pathway.

### Community-level heterogeneity

The null multilevel model had cluster-level variance 0.150, corresponding to ICC 4.35% and MOR 1.45. After adjustment, cluster variance declined to 0.107, with ICC 3.14% and MOR 1.37. The variational-Bayes models reproduced these estimates. Between-cluster variance was approximately 28.8% lower after adjustment, with residual contextual heterogeneity remaining.

## Discussion

### Main finding of this study

Anaemia affected about two in five Ghanaian women of reproductive age. Poorer women carried a disproportionate burden, and prevalence varied across regions. Nutritional status had the largest measured contribution to wealth-related inequality. Pregnancy and region remained associated with anaemia after multivariable adjustment, and measured individual characteristics did not fully account for community-level heterogeneity.

### What is already known on this topic

The high national burden is consistent with the 2022 GDHS and recent analysis of anaemia among Ghanaian women.[3,4] During pregnancy, increased iron requirements and plasma-volume expansion increase vulnerability to anaemia. Previous work has also reported associations with nutritional status, reproductive history and socioeconomic conditions.[1,4]

The inverse association between higher BMI categories and anaemia has been reported in other cross-sectional work, including Ghanaian analyses.[4] It should not be interpreted as evidence that overweight or obesity prevents anaemia. BMI does not directly measure iron stores, diet quality or micronutrient sufficiency, and excess adiposity carries substantial health risks of its own.

### What this study adds

This study quantifies wealth-related inequality across the socioeconomic ranking, extending previous prevalence and regression analyses. The negative Erreygers index indicates a disproportionate concentration of anaemia among poorer women.

The decomposition attributes the largest statistical contribution to the socioeconomic distribution of nutritional status and its association with anaemia. This pattern helps explain the coexistence of a crude wealth gradient and weak wealth coefficients after multivariable adjustment. Adjusting for correlated characteristics can attenuate these coefficients while population-level inequality remains. The analysis cannot distinguish mediation from confounding or establish temporal ordering.

More than 20 percentage points separated the regions with the lowest and highest prevalence. Between-cluster heterogeneity also remained after adjustment. Unmeasured contextual conditions may contribute to this variation, including food environments, malaria transmission, sanitation, local health-service access, environmental exposures and community-level deprivation.

Ghanaian intervention research includes a prospective cohort evaluation of school-based iron and folic acid supplementation among adolescent girls.[15] That evidence concerns a specific programme and population; our cross-sectional analysis does not estimate intervention effects.

Monitoring socioeconomic differences alongside national prevalence can show whether reductions in anaemia reach poorer women. Geographic surveillance can also identify areas where population-wide strategies may need additional targeted support.

### Limitations of this study

The cross-sectional design prevents causal inference and does not establish temporal ordering. Haemoglobin identifies anaemia but cannot determine its aetiology; the data therefore cannot distinguish iron-deficiency anaemia from anaemia associated with infection, inflammation, inherited haemoglobin disorders, blood loss or other micronutrient deficiencies.

BMI is an imperfect proxy for nutritional status. Its large decomposition contribution describes a statistical pattern and does not justify recommending weight gain. Decomposition estimates depend on model specification, although the BMI result was similar under alternative parameterisation.

Selection into the haemoglobin-tested analytic sample could introduce bias if women without valid measurements differed systematically in ways not fully addressed by survey weighting. Measurement error is also possible for self-reported reproductive and socioeconomic variables. The close agreement with the official national anaemia estimate supports the analytic setup, but does not exclude selection or measurement bias.

The findings apply to Ghanaian women aged 15–49 years represented by the survey. They should not be generalised to men, children, women older than 49 years or populations outside Ghana without additional evidence.

Finally, the analysis used the anaemia classification embedded in the 2022 GDHS. WHO subsequently updated haemoglobin cut-offs and measurement guidance,[14] and future research should evaluate whether newer definitions materially alter prevalence or inequality estimates.

## Conclusion

Anaemia among women of reproductive age in Ghana is concentrated disproportionately among poorer women and varies across regions. Nutritional status has the largest measured contribution to wealth-related inequality. Pregnancy and region remain associated with anaemia after adjustment, alongside residual community-level heterogeneity.

The findings support population-wide prevention that addresses nutritional needs, with additional attention to socioeconomic and geographic differences. Monitoring inequality alongside national prevalence can help assess whether progress reaches women with the greatest burden. This study does not establish which interventions will reduce anaemia.

## Acknowledgements

We thank The DHS Program, the Ghana Statistical Service and ICF for making the 2022 Ghana Demographic and Health Survey data available for research.

OpenAI ChatGPT was used to assist with code development, statistical workflow documentation and manuscript drafting and language editing. All analytic decisions, numerical outputs, interpretations and final manuscript text were reviewed and verified by the authors, who take full responsibility for the work.


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
The curve plots the cumulative share of anaemia against the cumulative weighted population ranked from poorest to richest. The 45-degree line indicates equality. The curve lies predominantly above this line, indicating a disproportionate concentration of anaemia among poorer women. The Erreygers-corrected concentration index was -0.0589 (95% bootstrap CI -0.0924 to -0.0249).

**Alt text:** Line graph comparing the anaemia concentration curve with a diagonal equality line. The anaemia curve lies mostly above the equality line, showing that poorer women account for a larger share of anaemia than their population share.

Source: `figures/figure1_concentration_curve.svg`

**Figure 2. Survey-weighted anaemia prevalence by region.**
Survey-weighted anaemia prevalence and 95% confidence intervals are shown for Ghana's 16 regions. The dashed reference line marks the national prevalence of 41.1%. Regional prevalence ranged from approximately 30.1% in Bono to 51.8% in Oti.

**Alt text:** Horizontal point-and-whisker plot of anaemia prevalence across 16 Ghanaian regions. Bono has the lowest estimate at about 30%, Oti the highest at about 52%, and several northern regions are above the national prevalence of 41%.

Source: `figures/figure2_regional_prevalence.svg`
