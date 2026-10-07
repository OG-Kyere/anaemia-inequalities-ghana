# Ghana 2022 DHS Data Audit

## Source file

The audit was performed on the Ghana 2022 DHS **Individual Recode (IR)** Stata file, `GHIR8CFL.DTA`.

The restricted DHS microdata are **not** stored in this repository.

## Dataset dimensions

- Total women in IR file: **15,014**
- Total variables: **5,584**
- Women with a valid anaemia classification (`v457`): **7,557**

The weighted total represented by women with valid anaemia measurements is approximately **7,655**, matching the published DHS denominator after application of `v005`.

## Anaemia outcome check

Unweighted `v457` distribution among women with valid measurements:

| Anaemia level | n |
|---|---:|
| Severe | 68 |
| Moderate | 1,382 |
| Mild | 1,731 |
| Not anaemic | 4,376 |
| **Total** | **7,557** |

Using `v005 / 1,000,000`, the survey-weighted prevalence of any anaemia is:

**41.12%**

This reproduces the published Ghana DHS estimate of approximately 41.1% and serves as the primary validation check for the analytic setup.

The survey-weighted mean adjusted haemoglobin level (`v456 / 10`) is approximately **12.10 g/dL**.

## Survey design variables

- `v005`: woman's sampling weight
- `v021`: primary sampling unit (cluster)
- `v022`: sampling stratum
- `v023`: stratification used in the sample design

In this file, `v022` and `v023` are identical for all records. The primary survey setup will therefore use `v022`.

## Geographic validation

The IR file contains all 16 Ghana regions in `v024`.

Selected weighted anaemia prevalence estimates reproduced during the audit include:

- Bono: approximately **30.1%**
- Oti: approximately **51.8%**
- Urban: approximately **39.4%**
- Rural: approximately **43.4%**

These patterns are consistent with the Ghana DHS report.

## Wealth gradient validation

Weighted anaemia prevalence by `v190`:

| Wealth quintile | Weighted prevalence |
|---|---:|
| Poorest | 46.6% |
| Poorer | 41.8% |
| Middle | 40.8% |
| Richer | 39.3% |
| Richest | 38.8% |

This confirms a measurable socioeconomic gradient suitable for concentration-index analysis.

## Core-variable completeness among the 7,557 women with valid anaemia data

The following planned variables have no ordinary missing observations in the anaemia-analysis subset:

- age (`v012`, `v013`)
- region (`v024`)
- residence (`v025`)
- education (`v106`, `v133`)
- wealth (`v190`, `v191`)
- marital status (`v501`)
- current employment (`v714`)
- children ever born (`v201`)
- pregnancy status (`v213`)
- number of living children (`v218`)
- contraceptive use (`v312`, `v313`)
- household size (`v136`)

## Anthropometric cleaning

DHS anthropometric variables contain special numeric codes that must not be treated as observed measurements.

- `v437` weight: code `9996` = other/no valid measurement
- `v438` height: code `9996` = other/no valid measurement
- `v445` BMI: code `9998` = flagged case

Within the anaemia subset:

- 5 women have `v437 = 9996`
- 5 women have `v438 = 9996`
- 2 women have `v445 = 9998`
- 5 women have system-missing `v445`

These values will be recoded to missing before deriving BMI categories.

## Preliminary conclusion

The dataset supports the planned study without major data-availability problems. The anaemia outcome, socioeconomic ranking variables, regional identifiers, reproductive variables, anthropometry, and survey-design variables are all present.

The next step is to freeze the analytic variable dictionary and implement the reproducible cleaning pipeline.
