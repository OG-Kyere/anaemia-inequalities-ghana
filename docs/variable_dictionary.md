# Frozen Core Variable Dictionary

This dictionary is based on an audit of the actual Ghana 2022 DHS Individual Recode file.

## Outcome

| Construct | DHS variable | Coding / derivation |
|---|---|---|
| Anaemia level | `v457` | 1 severe, 2 moderate, 3 mild, 4 not anaemic |
| Any anaemia | derived from `v457` | 1 if `v457 < 4`, 0 if `v457 = 4` |
| Adjusted haemoglobin | `v456` | divide by 10 for g/dL |
| Measured haemoglobin | `v453` | divide by 10 for g/dL |
| Haemoglobin measurement result | `v455` | 0 = measured |

## Survey design

| Construct | DHS variable | Derivation |
|---|---|---|
| Sampling weight | `v005` | divide by 1,000,000 |
| Primary sampling unit | `v021` | cluster ID |
| Sampling stratum | `v022` | region-residence stratum |

## Socioeconomic and demographic variables

| Construct | DHS variable | Planned form |
|---|---|---|
| Age | `v012` | continuous and/or groups |
| Age group | `v013` | 5-year groups |
| Education | `v106` | none, primary, secondary, higher |
| Years of education | `v133` | continuous sensitivity variable |
| Wealth quintile | `v190` | poorest to richest |
| Wealth score | `v191` | continuous rank variable |
| Marital status | `v501` | categorical |
| Current employment | `v714` | no / yes |
| Residence | `v025` | urban / rural |
| Region | `v024` | 16 regions |

## Reproductive variables

| Construct | DHS variable | Planned form |
|---|---|---|
| Children ever born | `v201` | parity categories and/or continuous |
| Currently pregnant | `v213` | no/unsure vs yes |
| Living children | `v218` | secondary |
| Current contraceptive method | `v312` | detailed method if needed |
| Contraceptive method type | `v313` | none, folkloric, traditional, modern |
| Currently amenorrhoeic | `v405` | no / yes |
| Menstruated in last six weeks | `v216` | no / yes |

## Anthropometry

| Construct | DHS variable | Cleaning |
|---|---|---|
| Weight | `v437` | divide by 10; special codes 9994-9996 -> missing |
| Height | `v438` | divide by 10; special codes 9994-9996 -> missing |
| BMI | `v445` | divide by 100; code 9998 -> missing |
| BMI category | derived | <18.5, 18.5-24.9, 25.0-29.9, >=30 kg/m2 |

## Household/contextual candidates

| Construct | DHS variable |
|---|---|
| Household size | `v136` |
| Drinking-water source | `v113` |
| Toilet facility | `v116` |
| Electricity | `v119` |
| Sex of household head | `v151` |
| Cooking fuel | `v161` |
| Slept under mosquito net | `v461` |

## Selection principle

Variables will not be selected solely from bivariate p-values. Primary adjustment sets will be prespecified from substantive knowledge and a conceptual framework.

Pregnancy-specific iron supplementation and malaria prophylaxis variables will not be used as universal covariates because they apply only to recent pregnancies.

## Primary analytic population

Women aged 15-49 years with a valid `v457` value.

Observed audit sample: **n = 7,557**.