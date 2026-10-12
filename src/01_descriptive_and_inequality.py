"""Reproduce core descriptive and inequality results."""

from pathlib import Path
import argparse

import pandas as pd

from common import (
    ci95,
    concentration_indices,
    concentration_curve,
    OUTPUT_DIR,
    bootstrap_concentration_indices,
    load_analysis_data,
    survey_domain_proportion,
    survey_ratio_se,
)

OUT = OUTPUT_DIR


def subgroup_table(df: pd.DataFrame, variable: str) -> pd.DataFrame:
    rows = []
    levels = [x for x in df[variable].dropna().unique()]
    for level in levels:
        domain = df[variable].eq(level)
        est, se = survey_domain_proportion(
            df["anaemia"],
            domain,
            df["weight"],
            df["strata"],
            df["psu"],
        )
        lo, hi = ci95(est, se)
        rows.append({
            "variable": variable,
            "category": str(level),
            "n_unweighted": int(domain.sum()),
            "weighted_percent": 100.0 * df.loc[domain, 'weight'].sum() / df.loc[df[variable].notna(), 'weight'].sum(),
            "weighted_prevalence": est,
            "ci_low": lo,
            "ci_high": hi,
        })
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bootstrap-reps', type=int, default=200)
    parser.add_argument('--seed', type=int, default=20261008)
    parser.add_argument('--no-bootstrap', action='store_true')
    args = parser.parse_args()
    if not args.no_bootstrap and args.bootstrap_reps < 2:
        parser.error('--bootstrap-reps must be at least 2')
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_analysis_data()

    est, se = survey_ratio_se(
        df["anaemia"], df["weight"], df["strata"], df["psu"]
    )
    lo, hi = ci95(est, se)

    overall = pd.DataFrame([{
        "n_unweighted": len(df),
        "weighted_denominator": df["weight"].sum(),
        "anaemia_prevalence": est,
        "ci_low": lo,
        "ci_high": hi,
    }])
    overall.to_csv(OUT / "overall_prevalence.csv", index=False)

    variables = [
        "v013",   # age group
        "v106",   # education
        "v190",   # wealth quintile
        "v025",   # residence
        "v213",   # pregnancy
        "parity_cat",
        "bmi_cat",
        "v714",   # employment
        "v501",   # marital status
        "v024",   # region
    ]
    tables = [subgroup_table(df, v) for v in variables]
    pd.concat(tables, ignore_index=True).to_csv(
        OUT / "subgroup_prevalence.csv", index=False
    )

    inequality = concentration_indices(
        df["anaemia"], df["v191"], df["weight"]
    )
    pd.DataFrame([inequality]).to_csv(
        OUT / "concentration_indices.csv", index=False
    )
    concentration_curve(df['anaemia'], df['v191'], df['weight']).to_csv(
        OUT / 'concentration_curve.csv', index=False)
    if not args.no_bootstrap:
        boot = bootstrap_concentration_indices(df, args.bootstrap_reps, args.seed)
        boot.to_csv(OUT / 'concentration_indices_bootstrap.csv', index=False)
        pd.DataFrame([{'sample':'Full valid-anaemia sample', 'n':len(df),
                       'point_erreygers':inequality['erreygers_index'],
                       'bootstrap_ci_low':boot['erreygers_index'].quantile(.025),
                       'bootstrap_ci_high':boot['erreygers_index'].quantile(.975),
                       'bootstrap_reps':args.bootstrap_reps,'seed':args.seed}]).to_csv(
            OUT / 'full_sample_erreygers_bootstrap_interval.csv', index=False)

    print(overall.to_string(index=False))
    print("\nConcentration indices")
    print(pd.DataFrame([inequality]).to_string(index=False))


if __name__ == "__main__":
    main()
