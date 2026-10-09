"""Shared data-loading and survey-analysis helpers.

Raw DHS microdata are never committed to the repository. Point DHS_IR_PATH to the
authorized Ghana 2022 Individual Recode Stata file before running the scripts.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = ROOT / "data/raw/GHIR8CFL.DTA"
OUTPUT_DIR = ROOT / "results/reproduced"

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


def _check_weights(w: pd.Series) -> None:
    if (w < 0).any() or not np.isfinite(w).all() or float(w.sum()) <= 0:
        raise ValueError('Weights must be finite, nonnegative and have a positive total.')


def weighted_mean(x: pd.Series, w: pd.Series) -> float:
    mask = x.notna() & w.notna() & np.isfinite(x) & np.isfinite(w)
    x = x.loc[mask].astype(float)
    w = w.loc[mask].astype(float)
    _check_weights(w)
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
            raise ValueError('Survey variance requires at least two PSUs per stratum; '
                             'a singleton-PSU policy must be specified explicitly.')
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
    _check_weights(w)
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
    _check_weights(w)
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
    _check_weights(x['weight'])
    if not np.isfinite(x['value']).all():
        raise ValueError('Ranking values must be finite.')
    grouped = (
        x.groupby("value", sort=True, observed=True)["weight"]
        .sum()
        .reset_index()
    )
    grouped["cum_before"] = grouped["weight"].cumsum() - grouped["weight"]
    total = grouped["weight"].sum()
    grouped["rank"] = (grouped["cum_before"] + grouped["weight"] / 2.0) / total
    mapping = grouped.set_index("value")["rank"]
    result = pd.Series(np.nan, index=values.index, dtype=float)
    result.loc[x.index] = x['value'].map(mapping)
    return result


def concentration_indices(
    y: pd.Series,
    rank_variable: pd.Series,
    weights: pd.Series,
) -> dict[str, float]:
    mask = (y.notna() & rank_variable.notna() & weights.notna()
            & np.isfinite(y) & np.isfinite(rank_variable) & np.isfinite(weights))
    yy = y.loc[mask].astype(float)
    xx = rank_variable.loc[mask].astype(float)
    ww = weights.loc[mask].astype(float)
    _check_weights(ww)
    if not yy.between(0, 1).all():
        raise ValueError('Erreygers correction here is defined for outcomes in [0, 1].')

    ranks = weighted_midrank(xx, ww)
    mu = weighted_mean(yy, ww)
    mean_r = weighted_mean(ranks, ww)
    cov = weighted_mean((yy - mu) * (ranks - mean_r), ww)

    ci = 2.0 * cov / mu if mu > 0 else float('nan')
    erreygers = 8.0 * cov
    return {
        "mean_outcome": mu,
        "concentration_index": float(ci),
        "erreygers_index": float(erreygers),
    }


def concentration_curve(y, rank_variable, weights, points=101) -> pd.DataFrame:
    """Interpolate empirical tied-wealth totals on a fixed population-share grid.

    Exporting only this grid avoids a record-by-record cumulative output.
    """
    if points < 2:
        raise ValueError('A concentration curve needs at least two grid points.')
    frame = pd.DataFrame({'outcome': y, 'wealth': rank_variable, 'weight': weights}).dropna()
    _check_weights(frame['weight'])
    if not np.isfinite(frame[['outcome', 'wealth']]).all().all():
        raise ValueError('Curve values must be finite.')
    if not frame['outcome'].between(0,1).all():
        raise ValueError('Curve outcomes must be in [0, 1].')
    frame['weighted_cases'] = frame['outcome'] * frame['weight']
    grouped = frame.groupby('wealth', sort=True)[['weight', 'weighted_cases']].sum()
    cases = grouped['weighted_cases'].sum()
    if cases <= 0:
        raise ValueError('A concentration curve requires at least one weighted case.')
    curve = pd.DataFrame({'population_share': grouped['weight'].cumsum()/grouped['weight'].sum(),
                          'anaemia_share': grouped['weighted_cases'].cumsum()/cases})
    empirical=pd.concat([pd.DataFrame({'population_share':[0.], 'anaemia_share':[0.]}),
                         curve.reset_index(drop=True)], ignore_index=True)
    grid=np.linspace(0.,1.,points)
    return pd.DataFrame({'population_share':grid,
        'anaemia_share':np.interp(grid,empirical['population_share'],empirical['anaemia_share'])})


def resample_psus_within_strata(frame, rng):
    pieces = []
    for stratum, group in frame.groupby('strata', observed=True):
        psus = pd.unique(group['psu'])
        for draw_id, selected in enumerate(rng.choice(psus, size=len(psus), replace=True)):
            piece = group.loc[group['psu'] == selected].copy()
            piece['psu_boot'] = f'{stratum}_{draw_id}'
            pieces.append(piece)
    if not pieces:
        raise ValueError('Cannot resample an empty survey frame.')
    return pd.concat(pieces, ignore_index=True)


def bootstrap_concentration_indices(frame, reps=200, seed=20261008):
    if reps < 2:
        raise ValueError('At least two bootstrap replicates are required.')
    rng = np.random.default_rng(seed)
    records = []
    for replicate in range(1, reps+1):
        sample = resample_psus_within_strata(frame, rng)
        result = concentration_indices(sample['anaemia'], sample['v191'], sample['weight'])
        records.append({'replicate':replicate, **result})
    return pd.DataFrame(records)
