# Table III. Wealth-related inequality decomposition and community-level heterogeneity

## Panel A. Decomposition of wealth-related inequality

| Domain | Absolute contribution | % of observed Erreygers index | 95% bootstrap interval |
|---|---:|---:|---:|
| BMI / nutritional status | -0.045731 | 77.7% | -0.061716 to -0.030045 |
| Education | -0.009184 | 15.6% | -0.025104 to 0.006950 |
| Residence | -0.004023 | 6.8% | -0.023362 to 0.013460 |
| Parity | -0.002892 | 4.9% | -0.014688 to 0.009773 |
| Pregnancy status | -0.002221 | 3.8% | -0.005493 to 0.000020 |
| Age | +0.000570 | -1.0% | -0.003250 to 0.004169 |
| Employment | +0.000021 | -0.04% | -0.000592 to 0.000687 |
| Marital/union status | +0.001203 | -2.0% | -0.002581 to 0.005772 |
| Residual | +0.003405 | -5.8% | -0.017297 to 0.025089 |

The decomposition uses 7,550 BMI-complete women and a complete-case Erreygers index of -0.058853. The percentages are relative to that negative index, so positive contributions appear as negative percentages and offset part of the measured pro-poor inequality.


## Panel B. Community-level heterogeneity

| Measure | Null model | Adjusted model |
|---|---:|---:|
| Women, n | 7,557 | 7,550 |
| Cluster-level SD | 0.387 | 0.326 |
| Cluster-level variance | 0.150 | 0.107 |
| ICC | 4.35% | 3.14% |
| Median odds ratio | 1.45 | 1.37 |
| Proportional change in variance | — | 28.8% |


The null model includes 7,557 women and the adjusted model 7,550. Both models use unweighted variational Bayes. PCV compares these models descriptively; the sample difference means it is not solely a measure of covariate adjustment. Approximate uncertainty and estimator diagnostics remain in the supplementary material.

**Notes:** Panel A uses a survey-weighted linear probability model; its intervals are percentile intervals from 200 stratified PSU bootstrap replicates. Positive absolute contributions offset the negative observed index. Contributions are statistical, not causal effects; BMI does not identify anaemia aetiology. Panel B describes residual clustering under a separate model; ICC = intraclass correlation coefficient, SD = standard deviation, PCV = proportional change in variance. Neither panel estimates an intervention effect.

**Aggregate sources:** `results/reproduced/inequality_decomposition_point.csv`, `results/reproduced/inequality_decomposition_bootstrap_intervals.csv`, `results/reproduced/inequality_decomposition_meta.csv` and `results/reproduced/community_heterogeneity_vb.csv`. All numerical estimates are copied from the validated outputs; none were re-estimated.
