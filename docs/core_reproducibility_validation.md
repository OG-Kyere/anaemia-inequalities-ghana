# Core Reproducibility Validation

Date validated: **2026-10-08**

The executable core pipeline was rerun locally against an authorized copy of the 2022 Ghana DHS Individual Recode file.

Command:

```bash
python run_analysis.py
```

The regenerated outputs matched the locked manuscript results.

## Validation results

| Quantity | Reproduced value | Locked manuscript value | Status |
|---|---:|---:|---|
| Valid anaemia sample | 7,557 | 7,557 | PASS |
| Weighted denominator | 7,655.051315 | 7,655.051315 | PASS |
| Anaemia prevalence | 0.411225 | 0.411225 | PASS |
| 95% CI | 0.396050–0.426399 | 0.3960–0.4264 | PASS |
| Standard concentration index | -0.035831 | -0.035831 | PASS |
| Erreygers index | -0.058938 | -0.058938 | PASS |
| Adjusted-model sample | 7,550 | 7,550 | PASS |
| Pregnancy aOR | 1.7746 | 1.77 | PASS |
| Overweight aOR | 0.7337 | 0.73 | PASS |
| Obesity aOR | 0.5972 | 0.60 | PASS |
| Bono aOR | 0.6105 | 0.61 | PASS |
| Oti aOR | 1.4808 | 1.48 | PASS |

## Conclusion

The core descriptive, socioeconomic-inequality, and adjusted-regression workflow is reproducible from the authorized DHS IR file using the repository code and listed dependencies.

The remaining analyses to convert into fully executable scripts are:

- stratified PSU bootstrap for the Erreygers index and decomposition;
- inequality decomposition;
- multilevel random-intercept logistic models;
- automated regeneration of publication tables and figures from reproduced outputs.
