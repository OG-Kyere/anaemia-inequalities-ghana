> Synchronized working manuscript. Canonical submission source: `submission/jph_main_manuscript.md`.

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

The 2022 Ghana Demographic and Health Survey (GDHS) reported anaemia in about two in five women of reproductive age.[3] A recent analysis of the same survey found higher prevalence among pregnant women and associations with nutritional status, parity, wealth and geographic location.[4] Such prevalence comparisons and regression models describe group differences and adjusted associations. They do not directly quantify inequality across the socioeconomic ranking.

Multicountry analyses have examined anaemia severity using multilevel models,[5,6] while spatial studies have described geographic variation in anaemia among women across sub-Saharan Africa and within Ethiopia.[7,8] Subnational mapping in West and Central Africa provides a further geographic perspective.[9] Salifu and colleagues used multivariate decomposition to examine changes in anaemia prevalence between survey periods in selected countries, including Ghana.[10] That temporal decomposition separates changes associated with population characteristics and model coefficients; it does not estimate each characteristic's contribution to wealth-ranked inequality within the 2022 GDHS.

Together, these studies establish that socioeconomic and geographic differences in anaemia are already recognised. The remaining question addressed here is how anaemia is distributed across the wealth ranking in Ghana in 2022, which measured characteristics statistically contribute to that distribution, and whether community-level variation remains after adjustment. This is a focused extension of the cited evidence, rather than a claim that socioeconomic determinants, spatial variation or decomposition have not previously been studied.

National prevalence can decline while disadvantaged groups continue to carry a greater burden. A non-significant adjusted wealth coefficient also does not establish the absence of population-level inequality. Socioeconomic position is related to nutritional, educational, reproductive and geographic characteristics, which may themselves be associated with anaemia. Health-inequality measures describe the distribution of anaemia across the population, complementing the conditional associations estimated by regression.

Concentration curves and indices summarise how a health outcome is distributed across the socioeconomic ranking. The Erreygers correction normalises the index for bounded outcomes such as binary anaemia status.[11] Decomposition estimates the statistical contributions of measured characteristics to this inequality.[12] Multilevel models quantify variation between communities after accounting for individual characteristics.[13]

We examined socioeconomic and geographic inequalities in anaemia among women aged 15–49 years in Ghana. We estimated prevalence across population groups, quantified wealth-related inequality and its measured contributors, and assessed adjusted associations with anaemia. We also examined whether community-level heterogeneity persisted after adjustment. Combining these complementary analyses distinguishes the national burden, wealth-related inequality, conditional associations and residual clustering, while retaining a non-causal interpretation.

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

Population-level analyses incorporated the DHS individual sampling weight, primary sampling unit and sampling stratum. For woman $i$, let $y_i=1$ indicate mild, moderate or severe anaemia and $y_i=0$ indicate no anaemia. The sampling weight and weighted prevalence were

$$
w_i=\frac{v005_i}{10^6},\qquad
\widehat{\mu}=\frac{\sum_i w_i y_i}{\sum_i w_i}.
\tag{1}
$$

Primary sampling units and strata were identified by $\texttt{v021}$ and $\texttt{v022}$, respectively. Survey-weighted proportions and 95% confidence intervals were estimated overall and within demographic, socioeconomic, reproductive, nutritional and geographic subgroups. Standard errors used Taylor linearisation with PSU totals centred within strata; subgroup estimates retained the full analytic sample's design structure through domain indicators. Prevalence intervals used the normal approximation $\widehat{\mu}\pm1.96\,SE(\widehat{\mu})$.

### Socioeconomic inequality

Women were ranked from poorest to richest using the continuous wealth score. We first calculated the standard concentration index and plotted the concentration curve. Because anaemia is a bounded binary outcome, the Erreygers-corrected concentration index was used as the primary inequality measure.[11] Let $s_i$ denote the continuous wealth score and $W=\sum_i w_i$. Weighted fractional midranks assigned the same rank to women with tied wealth scores:

$$
R_i=\frac{\sum_{j:s_j<s_i}w_j+\tfrac12\sum_{j:s_j=s_i}w_j}{W}.
\tag{2}
$$

Writing $\overline R_w=\sum_i w_iR_i/W$ and
$\operatorname{Cov}_w(y,R)=\sum_i w_i(y_i-\widehat{\mu})(R_i-\overline R_w)/W$, the standard index and its correction were

$$
C=\frac{2\,\operatorname{Cov}_w(y,R)}{\widehat{\mu}},
\qquad
E=\frac{4\widehat{\mu}}{b-a}C
 =4\widehat{\mu}C
 =8\,\operatorname{Cov}_w(y,R),
\tag{3}
$$

where $a=0$ and $b=1$ are the outcome bounds.[11] A negative value indicates that anaemia is concentrated disproportionately among poorer women.

We estimated a percentile 95% confidence interval for the corrected index using 5,000 bootstrap replicates, resampling primary sampling units within DHS strata (seed 20261008). The decomposition used a separate 200-replicate bootstrap. Wealth ranks were recomputed in each resampled dataset, and decomposition models were refitted in each replicate.

### Decomposition analysis

The Erreygers index was decomposed using a survey-weighted linear probability model based on established concentration-index decomposition methods.[12] The decomposition model included age, years of education, residence, pregnancy status, parity, BMI, employment and marital status. Wealth itself was not entered as a determinant because it defined the socioeconomic ranking. The reproducible specification used DHS five-year age-group indicators and modelled BMI with linear and quadratic terms.

The weighted least-squares model was

$$
y_i=\alpha+\sum_k\beta_k x_{ki}+\varepsilon_i.
\tag{4}
$$

Using the same sample, weights and wealth ranks for all terms, its additive decomposition was

$$
E=\sum_k8\widehat{\beta}_k\operatorname{Cov}_w(x_k,R)
  +8\operatorname{Cov}_w(\widehat{\varepsilon},R).
\tag{5}
$$

For a term with non-zero weighted mean $\overline{x}_{k,w}$, its contribution can equivalently be written as $4\widehat{\beta}_k\overline{x}_{k,w}C_k$, where $C_k=2\operatorname{Cov}_w(x_k,R)/\overline{x}_{k,w}$.[11,12] The covariance form avoids division by a covariate mean. Domain contributions summed all relevant terms, including both BMI terms and all age indicators. A domain's percentage contribution was $100$ times its absolute contribution divided by the observed $E$ in the complete-case decomposition sample; the residual was $E$ minus the sum of measured contributions. Thus, the denominator was the observed index, not the sum of measured contributions, and offsetting contributions can produce percentages below zero or above 100%.

We used bootstrap resampling to assess uncertainty. Contributions depend on the model specification and describe statistical patterns, not causal effects.

### Adjusted regression

Survey-weighted logistic regression was used to estimate adjusted associations with anaemia. The full model included age group, education, wealth quintile, residence, pregnancy status, parity, BMI category, employment, marital status and region. For the covariate vector $\mathbf X_i$, the model was

$$
\log\left(\frac{p_i}{1-p_i}\right)
 =\gamma_0+\mathbf X_i^\mathsf{T}\boldsymbol{\gamma},
\qquad p_i=\Pr(y_i=1\mid\mathbf X_i).
\tag{6}
$$

Coefficients were estimated using sampling weights, with a design-based sandwich covariance accounting for stratification and PSU clustering. Adjusted odds ratios were $\exp(\widehat{\gamma}_k)$, with 95% confidence limits $\exp\{\widehat{\gamma}_k\pm1.96\,SE_{\mathrm{design}}(\widehat{\gamma}_k)\}$. Overall Wald tests were used for categorical variables.

### Community-level heterogeneity

Two-level random-intercept logistic models were fitted with women nested within DHS clusters. A null model quantified baseline clustering, and an adjusted model included the same covariates as the primary regression model. We summarised cluster heterogeneity using the latent-variable intraclass correlation coefficient (ICC) and median odds ratio (MOR).[13] For woman $i$ in cluster $j$, the conditional model was

$$
\log\left(\frac{p_{ij}}{1-p_{ij}}\right)
 =\delta_0+\mathbf X_{ij}^\mathsf{T}\boldsymbol{\delta}+u_j,
\qquad u_j\sim N(0,\sigma_u^2),
\tag{7}
$$

where $p_{ij}=\Pr(y_{ij}=1\mid\mathbf X_{ij},u_j)$; the null model omitted the covariates. Heterogeneity summaries were

$$
ICC=\frac{\sigma_u^2}{\sigma_u^2+\pi^2/3},
\qquad
MOR=\exp\left\{\Phi^{-1}(0.75)\sqrt{2\sigma_u^2}\right\},
\qquad
PCV=\frac{\sigma_{u,0}^2-\sigma_{u,A}^2}{\sigma_{u,0}^2}.
\tag{8}
$$

Here $\Phi^{-1}(0.75)\simeq0.67449$, and subscripts $0$ and $A$ denote the null and adjusted models.[13] ICC used the logistic latent-variable approximation; ICC and PCV were multiplied by 100 when expressed as percentages. PCV describes a proportional variance difference between models, not a causal proportion explained.

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

1. World Health Organization. Anaemia. Geneva: World Health Organization; 2025. https://www.who.int/news-room/fact-sheets/detail/anaemia (accessed 21 October 2026).
2. World Health Organization. *WHO global anaemia estimates: key findings, 2025*. Geneva: World Health Organization; 2025. ISBN 978-92-4-011393-0. https://www.who.int/publications/i/item/9789240113930 (accessed 21 October 2026).
3. Ghana Statistical Service (GSS), ICF. *Ghana Demographic and Health Survey 2022*. Accra, Ghana and Rockville, Maryland, USA: GSS and ICF; 2024. https://www.dhsprogram.com/publications/publication-fr387-dhs-final-reports.cfm (accessed 21 October 2026).
4. Agulu GG, Ahissou NCA, Kamiya Y, Baiden F, Matsui M. Anaemia prevalence and risk factors among nonpregnant and pregnant women of reproductive age in Ghana: an analysis of the Ghana demographic and health survey data. *Trop Med Health*. 2025;53:118. doi:10.1186/s41182-025-00792-8.
5. Mare KU, Aychiluhm SB, Sabo KG, et al. Determinants of anemia level among reproductive-age women in 29 Sub-Saharan African countries: a multilevel mixed-effects modelling with ordered logistic regression analysis. *PLoS One*. 2023;18(11):e0294992. doi:10.1371/journal.pone.0294992.
6. Tirore LL, Areba AS, Habte A, Desalegn M, Kebede AS. Prevalence and associated factors of severity levels of anemia among women of reproductive age in sub-Saharan Africa: a multilevel ordinal logistic regression analysis. *Front Public Health*. 2024;11:1349174. doi:10.3389/fpubh.2023.1349174.
7. Correa-Agudelo E, Kim HY, Musuka GN, et al. The epidemiological landscape of anemia in women of reproductive age in sub-Saharan Africa. *Sci Rep*. 2021;11:11955. doi:10.1038/s41598-021-91198-z.
8. Kibret KT, Chojenta C, D'Arcy E, Loxton D. Spatial distribution and determinant factors of anaemia among women of reproductive age in Ethiopia: a multilevel and spatial analysis. *BMJ Open*. 2019;9:e027276. doi:10.1136/bmjopen-2018-027276.
9. Baye K, Hailu BA, Nanama S, Ntambi J, Laillou A. Subnational mapping of anaemia and aetiologic factors in the West and Central African region. *Public Health Nutr*. 2025;28:e6. doi:10.1017/S1368980024002222.
10. Salifu MG, Da-Costa Vroom FB, Guure C. Anaemia among women of reproductive age in selected sub-Saharan African countries: multivariate decomposition analyses of the demographic and health surveys data 2008–2018. *Front Public Health*. 2024;11:1128214. doi:10.3389/fpubh.2023.1128214.
11. Erreygers G. Correcting the concentration index. *J Health Econ*. 2009;28(2):504–515. doi:10.1016/j.jhealeco.2008.02.003.
12. Wagstaff A, van Doorslaer E, Watanabe N. On decomposing the causes of health sector inequalities with an application to malnutrition inequalities in Vietnam. *J Econometrics*. 2003;112(1):207–223. doi:10.1016/S0304-4076(02)00161-6.
13. Merlo J, Chaix B, Ohlsson H, et al. A brief conceptual tutorial of multilevel analysis in social epidemiology: using measures of clustering in multilevel logistic regression to investigate contextual phenomena. *J Epidemiol Community Health*. 2006;60(4):290–297. doi:10.1136/jech.2004.029454.
14. World Health Organization. *Guideline on haemoglobin cutoffs to define anaemia in individuals and populations*. Geneva: World Health Organization; 2024. ISBN 978-92-4-008854-2. https://www.who.int/publications/i/item/9789240088542 (accessed 21 October 2026).
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
