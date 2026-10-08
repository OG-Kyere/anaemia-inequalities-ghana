# Reproducible Decomposition Validation

Date validated: **2026-10-08**

The inequality decomposition was rerun with a fully executable specification and a
200-replicate stratified PSU bootstrap.

## Executable specification

The specification selected after comparing plausible DHS codings against the original
locked decomposition used:

- DHS five-year age-group indicators;
- years of schooling (`v133`);
- rural residence;
- current pregnancy;
- continuous parity;
- BMI and BMI squared;
- current employment;
- currently in union versus not currently in union.

Wealth (`v191`) was used to rank women and was not included as an explanatory
determinant.

Analytic sample: **7,550**.

Erreygers index in the complete-case decomposition sample: **-0.058853**.

## Reproduced point contributions and 200-replicate intervals

| Domain | Point contribution | 95% bootstrap interval |
|---|---:|---:|
| Age | +0.000570 | -0.003250 to +0.004169 |
| Education | -0.009184 | -0.025104 to +0.006950 |
| Residence | -0.004023 | -0.023362 to +0.013460 |
| Pregnancy status | -0.002221 | -0.005493 to +0.000020 |
| Parity | -0.002892 | -0.014688 to +0.009773 |
| BMI / nutritional status | **-0.045731** | **-0.061716 to -0.030045** |
| Employment | +0.000021 | -0.000592 to +0.000687 |
| Marital/union status | +0.001203 | -0.002581 to +0.005772 |
| Residual | +0.003405 | -0.017297 to +0.025089 |

## Comparison with the earlier locked table

The dominant BMI contribution is essentially unchanged from the earlier stored result
(-0.0458), and its uncertainty interval remains entirely below zero. Residence,
pregnancy, parity, employment, and marital/union contributions are also similar in
magnitude.

The smaller differences for age, education, parity, marital/union status, and the
residual reflect covariate-coding differences between the original stored calculation
and the now fully executable specification. The original repository did not preserve
the exact calculation code that generated the earlier decomposition table.

For reproducibility, future reruns should use the executable specification documented
here. The manuscript should not mix point estimates from one coding specification with
bootstrap intervals from another.

## Interpretation

The reproducible analysis supports the same substantive conclusion: measured
wealth-related anaemia inequality is dominated by the socioeconomic patterning of BMI /
nutritional status. Contributions from the other measured domains are smaller and have
bootstrap intervals spanning zero.

These are statistical decomposition contributions, not causal effects.
