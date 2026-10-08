"""Shared data-loading and survey-analysis helpers.

Raw DHS microdata are never committed to the repository. Point DHS_IR_PATH to the
authorized Ghana 2022 Individual Recode Stata file before running the scripts.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd


DEFAULT_DATA_PATH = Path("data/raw/GHIR8CFL.DTA")

CORE_COLUMNS = [
    "v005", "v021", "v022", "v024", "v025",
    "v012", "v013", "v106", "v133", "v190", "v191",
    "v201", "v213", "v445", "v501", "v714",
    "v456", "v457",
]


def data_path() -> Path:
    path = Path(os.environ.get("DHS_IR_PATH", DEFAULT_DATA_PATH))
    if not path.exists():
        raise FileNotFoundError(
            f"DHS file not found at {path}. Set DHS_IR_PATH to the authorized "
            "Ghana 2022 Individual Recode .DTA file."
        )
    return path


def load_analysis_data() -> pd.DataFrame:
    df = pd.read_stata(
        data_path(),
        columns=CORE_COLUMNS,
        convert_categoricals=False,
    ).copy()

    # Survey design
    df["weight"] = df["v005"] / 1_000_000.0
    df["psu"] = df["v021"]
    df["strata"] = df["v022"]

    # Primary binary outcome: mild/moderate/severe anaemia vs no anaemia.
    # DHS v457 coding: 1 severe, 2 moderate, 3 mild, 4 not anaemic.
    valid_anaemia = df["v457"].isin([1, 2, 3, 4])
    df = df.loc[valid_anaemia].copy()
    df["anaemia"] = (df["v457"] < 4).astype(int)

    # BMI: DHS v445 is BMI x100. Codes >=9990 are special/missing.
    bmi = df["v445"].where(df["v445"] < 9990) / 100.0
    df["bmi"] = bmi
    df["bmi_cat"] = pd.cut(
        bmi,
        bins=[-np.inf, 18.5, 25.0, 30.0, np.inf],
        labels=["Underweight", "Normal weight", "Overweight", "Obesity"],
        right=False,
    )

    # Parity categories: 0, 1-2, 3-5, 6+
    parity = pd.Series(pd.NA, index=df.index, dtype="object")
    parity.loc[df["v201"] == 0] = "0"
    parity.loc[df["v201"].between(1, 2)] = "1–2"
    parity.loc[df["v201"].between(3, 5)] = "3–5"
    parity.loc[df["v201"] >= 6] = "6+"
    df["parity_cat"] = pd.Categorical(
        parity,
        categories=["0", "1–2", "3–5", "6+"],
        ordered=True,
    )

    return df


def weighted_mean(x: pd.Series, w: pd.Series) -> float:
    mask = x.notna() & w.notna() & np.isfinite(x) & np.isfinite(w)
    x = x.loc[mask].astype(float)
    w = w.loc[mask].astype(float)
    return float(np.sum(w * x) / np.sum(w))


def _linearized_variance(
    linearized: pd.Series,
    strata: pd.Series,
    psu: pd.Series,
) -> float:
    """Variance of a Taylor-linearized estimator under stratified PSU sampling."""
    tmp = pd.DataFrame({
        "strata": strata.to_numpy(),
        "psu": psu.to_numpy(),
        "lin": linearized.to_numpy(dtype=float),
    })
    cluster_scores = (
        tmp.groupby(["strata", "psu"], observed=True)["lin"]
        .sum()
        .reset_index()
    )

    variance = 0.0
    for _, g in cluster_scores.groupby("strata", observed=True):
        m = len(g)
        if m <= 1:
            continue
        u = g["lin"].to_numpy(dtype=float)
        variance += (m / (m - 1.0)) * np.sum((u - u.mean()) ** 2)
    return float(variance)


def survey_ratio_se(
    y: pd.Series,
    w: pd.Series,
    strata: pd.Series,
    psu: pd.Series,
) -> tuple[float, float]:
    """Taylor-linearized SE for a weighted mean/proportion in the full sample."""
    mask = (
        y.notna() & w.notna() & strata.notna() & psu.notna()
        & np.isfinite(y) & np.isfinite(w)
    )
    y = y.loc[mask].astype(float)
    w = w.loc[mask].astype(float)
    strata = strata.loc[mask]
    psu = psu.loc[mask]

    total_w = float(w.sum())
    estimate = float(np.sum(w * y) / total_w)
    lin = w * (y - estimate) / total_w
    variance = _linearized_variance(lin, strata, psu)

    return estimate, float(np.sqrt(variance))


def survey_domain_proportion(
    y: pd.Series,
    domain: pd.Series,
    w: pd.Series,
    strata: pd.Series,
    psu: pd.Series,
) -> tuple[float, float]:
    """Survey-domain prevalence with Taylor-linearized SE.

    The entire survey sample is retained when estimating the variance. Units outside
    the requested domain contribute zero to the linearized variable, which preserves
    the original PSU and stratum structure.
    """
    mask = (
        y.notna() & domain.notna() & w.notna() & strata.notna() & psu.notna()
        & np.isfinite(y) & np.isfinite(w)
    )
    y = y.loc[mask].astype(float)
    d = domain.loc[mask].astype(bool)
    w = w.loc[mask].astype(float)
    strata = strata.loc[mask]
    psu = psu.loc[mask]

    denominator = float(np.sum(w * d.astype(float)))
    if denominator <= 0:
        raise ValueError("Domain has zero weighted observations.")

    estimate = float(np.sum(w * d.astype(float) * y) / denominator)
    lin = w * d.astype(float) * (y - estimate) / denominator
    variance = _linearized_variance(lin, strata, psu)

    return estimate, float(np.sqrt(variance))


def ci95(estimate: float, se: float) -> tuple[float, float]:
    return estimate - 1.96 * se, estimate + 1.96 * se


def weighted_midrank(values: pd.Series, weights: pd.Series) -> pd.Series:
    """Weighted fractional midrank in [0,1], preserving ties."""
    x = pd.DataFrame({"value": values, "weight": weights}).dropna().copy()
    grouped = (
        x.groupby("value", sort=True, observed=True)["weight"]
        .sum()
        .reset_index()
    )
    grouped["cum_before"] = grouped["weight"].cumsum() - grouped["weight"]
    total = grouped["weight"].sum()
    grouped["rank"] = (grouped["cum_before"] + grouped["weight"] / 2.0) / total
    mapping = grouped.set_index("value")["rank"]
    return values.map(mapping)


def concentration_indices(
    y: pd.Series,
    rank_variable: pd.Series,
    weights: pd.Series,
) -> dict[str, float]:
    mask = y.notna() & rank_variable.notna() & weights.notna()
    yy = y.loc[mask].astype(float)
    xx = rank_variable.loc[mask].astype(float)
    ww = weights.loc[mask].astype(float)

    ranks = weighted_midrank(xx, ww)
    mu = weighted_mean(yy, ww)
    mean_r = weighted_mean(ranks, ww)
    cov = weighted_mean((yy - mu) * (ranks - mean_r), ww)

    ci = 2.0 * cov / mu
    erreygers = 4.0 * mu * ci
    return {
        "mean_outcome": mu,
        "concentration_index": float(ci),
        "erreygers_index": float(erreygers),
    }
