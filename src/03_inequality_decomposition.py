"""Decompose the Erreygers concentration index and bootstrap domain contributions.

Primary executable specification selected by diagnostic comparison with the
original locked decomposition:
- DHS five-year age-group indicators
- years of education
- rural residence
- current pregnancy
- continuous parity
- BMI and BMI^2
- current employment
- currently in union vs not

Wealth is used only to rank women and is not entered as a determinant.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

from common import concentration_indices, load_analysis_data, weighted_midrank

OUT = Path("results/reproduced")
OUT.mkdir(parents=True, exist_ok=True)

DOMAIN_TERMS = {
    "Age": ["age_2", "age_3", "age_4", "age_5", "age_6", "age_7"],
    "Education": ["education_years"],
    "Residence": ["rural"],
    "Pregnancy status": ["pregnant"],
    "Parity": ["parity"],
    "BMI / nutritional status": ["bmi", "bmi_sq"],
    "Employment": ["employed"],
    "Marital/union status": ["in_union"],
}


def analysis_frame(df: pd.DataFrame) -> pd.DataFrame:
    x = pd.DataFrame(index=df.index)
    x["anaemia"] = df["anaemia"].astype(float)
    x["weight"] = df["weight"].astype(float)
    x["wealth"] = df["v191"].astype(float)
    x["strata"] = df["strata"]
    x["psu"] = df["psu"]

    for code in range(2, 8):
        x[f"age_{code}"] = (df["v013"] == code).astype(float)
    x["education_years"] = df["v133"].astype(float)
    x["rural"] = (df["v025"] == 2).astype(float)
    x["pregnant"] = (df["v213"] == 1).astype(float)
    x["parity"] = df["v201"].astype(float)
    x["bmi"] = df["bmi"].astype(float)
    x["bmi_sq"] = x["bmi"] ** 2
    x["employed"] = (df["v714"] == 1).astype(float)

    # DHS v501 codes 1 (married) and 2 (living together) as currently in union.
    x["in_union"] = df["v501"].isin([1, 2]).astype(float)

    required = [
        "anaemia", "weight", "wealth", "strata", "psu",
        *[term for terms in DOMAIN_TERMS.values() for term in terms],
    ]
    return x.dropna(subset=required).copy()


def weighted_cov(x: np.ndarray, r: np.ndarray, w: np.ndarray) -> float:
    sw = np.sum(w)
    mx = np.sum(w * x) / sw
    mr = np.sum(w * r) / sw
    return float(np.sum(w * (x - mx) * (r - mr)) / sw)


def decompose(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    terms = [t for group in DOMAIN_TERMS.values() for t in group]

    y = frame["anaemia"].to_numpy(dtype=float)
    w = frame["weight"].to_numpy(dtype=float)
    X = sm.add_constant(frame[terms], has_constant="add")

    model = sm.WLS(y, X, weights=w).fit()

    ranks = weighted_midrank(frame["wealth"], frame["weight"]).to_numpy(dtype=float)

    overall = concentration_indices(
        frame["anaemia"], frame["wealth"], frame["weight"]
    )
    E = overall["erreygers_index"]

    term_contrib = {}
    for term in terms:
        beta = float(model.params[term])
        cov_xr = weighted_cov(
            frame[term].to_numpy(dtype=float),
            ranks,
            w,
        )
        # E decomposition for a linear probability model:
        # 4 * beta * mean(x) * CI_x = 8 * beta * Cov(x, rank).
        term_contrib[term] = 8.0 * beta * cov_xr

    rows = []
    measured_total = 0.0
    for domain, domain_terms in DOMAIN_TERMS.items():
        contribution = float(sum(term_contrib[t] for t in domain_terms))
        measured_total += contribution
        rows.append({
            "domain": domain,
            "absolute_contribution": contribution,
            "percent_of_observed_E": 100.0 * contribution / E,
        })

    residual = float(E - measured_total)
    rows.append({
        "domain": "Residual",
        "absolute_contribution": residual,
        "percent_of_observed_E": 100.0 * residual / E,
    })

    meta = {
        "n": int(len(frame)),
        "erreygers_index": float(E),
        "measured_contribution_sum": float(measured_total),
        "residual": residual,
    }
    return pd.DataFrame(rows), meta


def resample_psus_within_strata(
    frame: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    pieces = []
    for stratum, g in frame.groupby("strata", observed=True):
        psus = pd.unique(g["psu"])
        sampled = rng.choice(psus, size=len(psus), replace=True)

        for draw_id, selected_psu in enumerate(sampled):
            piece = g.loc[g["psu"] == selected_psu].copy()
            # Give repeated copies unique bootstrap cluster identifiers.
            piece["psu_boot"] = f"{stratum}_{draw_id}"
            pieces.append(piece)

    return pd.concat(pieces, ignore_index=True)


def bootstrap(
    frame: pd.DataFrame,
    reps: int,
    seed: int,
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    records = []

    for b in range(reps):
        boot = resample_psus_within_strata(frame, rng)
        table, meta = decompose(boot)
        row = {"replicate": b + 1, "erreygers_index": meta["erreygers_index"]}
        for _, rec in table.iterrows():
            row[rec["domain"]] = rec["absolute_contribution"]
        records.append(row)

        if (b + 1) % 25 == 0 or b + 1 == reps:
            print(f"Bootstrap replicate {b + 1}/{reps}")

    return pd.DataFrame(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-reps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20261008)
    parser.add_argument(
        "--no-bootstrap",
        action="store_true",
        help="Write point decomposition only.",
    )
    args = parser.parse_args()

    frame = analysis_frame(load_analysis_data())

    point, meta = decompose(frame)
    point.to_csv(OUT / "inequality_decomposition_point.csv", index=False)
    pd.DataFrame([meta]).to_csv(
        OUT / "inequality_decomposition_meta.csv", index=False
    )

    print("\nPoint decomposition")
    print(point.to_string(index=False))
    print(f"\nAnalytic n = {meta['n']:,}")
    print(f"Erreygers index = {meta['erreygers_index']:.6f}")

    if args.no_bootstrap:
        return

    boot = bootstrap(frame, args.bootstrap_reps, args.seed)
    boot.to_csv(OUT / "inequality_decomposition_bootstrap.csv", index=False)

    domains = list(DOMAIN_TERMS) + ["Residual"]
    intervals = []
    for domain in domains:
        q = boot[domain].quantile([0.025, 0.975])
        intervals.append({
            "domain": domain,
            "point": float(point.loc[point["domain"] == domain, "absolute_contribution"].iloc[0]),
            "bootstrap_ci_low": float(q.loc[0.025]),
            "bootstrap_ci_high": float(q.loc[0.975]),
        })

    interval_df = pd.DataFrame(intervals)
    interval_df.to_csv(
        OUT / "inequality_decomposition_bootstrap_intervals.csv",
        index=False,
    )

    e_q = boot["erreygers_index"].quantile([0.025, 0.975])
    pd.DataFrame([{
        "point_erreygers": meta["erreygers_index"],
        "bootstrap_ci_low": float(e_q.loc[0.025]),
        "bootstrap_ci_high": float(e_q.loc[0.975]),
        "bootstrap_reps": args.bootstrap_reps,
        "seed": args.seed,
    }]).to_csv(OUT / "erreygers_bootstrap_interval.csv", index=False)

    print("\nBootstrap intervals")
    print(interval_df.to_string(index=False))


if __name__ == "__main__":
    main()
