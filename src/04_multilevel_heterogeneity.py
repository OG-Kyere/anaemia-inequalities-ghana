"""Community-level random-intercept logistic models.

This script uses statsmodels BinomialBayesMixedGLM with one random intercept per
DHS cluster. Variational Bayes (VB) is the reproducibility estimator because it
matches the locked manuscript heterogeneity estimates. Laplace/MAP is retained
only as a diagnostic option; in this dataset it fails to converge and collapses
the cluster variance toward zero.

The final seeded VB run uses BFGS gtol=1e-5. The historical stricter gtol=1e-6
run reported precision loss; retain that diagnostic rather than suppressing it.
Optimizer status and maximum absolute gradient are written with the estimates.

These models are contextual complements to the design-based survey analyses;
they do not replace survey-weighted prevalence or inequality estimates.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM

from common import load_analysis_data, OUTPUT_DIR

OUT = OUTPUT_DIR

ADJUSTED_FORMULA = """
anaemia ~
C(v013, Treatment(reference=1)) +
C(v106, Treatment(reference=0)) +
C(v190, Treatment(reference=1)) +
C(v025, Treatment(reference=1)) +
C(v213, Treatment(reference=0)) +
C(parity_cat, Treatment(reference='0')) +
C(bmi_cat, Treatment(reference='Normal weight')) +
C(v714, Treatment(reference=0)) +
C(v501, Treatment(reference=0)) +
C(v024, Treatment(reference=3))
"""


def icc_from_variance(var: float) -> float:
    return float(var / (var + np.pi**2 / 3.0))


def mor_from_sd(sd: float) -> float:
    return float(np.exp(np.sqrt(2.0) * sd * 0.6744897501960817))


def fit_model(df: pd.DataFrame, formula: str, method: str, gtol=1e-5, seed=20261008):
    np.random.seed(seed)
    model = BinomialBayesMixedGLM.from_formula(
        formula,
        {"cluster": "0 + C(psu)"},
        df,
        vcp_p=1.0,
        fe_p=2.0,
    )

    if method == "map":
        result = model.fit_map(
            method="BFGS",
            minim_opts={"maxiter": 2000, "gtol": gtol},
            scale_fe=True,
        )
    else:
        result = model.fit_vb(
            fit_method="BFGS",
            minim_opts={"maxiter": 2000, "gtol": gtol},
            scale_fe=True,
        )

    log_sd = float(np.asarray(result.vcp_mean).reshape(-1)[0])
    sd = float(np.exp(log_sd))
    var = sd**2

    return result, {
        "cluster_sd": sd,
        "cluster_variance": var,
        "icc": icc_from_variance(var),
        "mor": mor_from_sd(sd),
        "optimizer_success": bool(result.optim_retvals.get('success', False)),
        "optimizer_message": str(result.optim_retvals.get('message', 'unavailable')),
        "max_absolute_gradient": float(np.max(np.abs(result.optim_retvals['jac']))),
        "gradient_tolerance": gtol,
        "seed": seed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method",
        choices=["vb", "map"],
        default="vb",
        help="VB reproduces the locked results; MAP is diagnostic only.",
    )
    parser.add_argument('--gtol',type=float,default=1e-5)
    parser.add_argument('--seed',type=int,default=20261008)
    args = parser.parse_args()
    if not np.isfinite(args.gtol) or args.gtol <= 0:
        parser.error('--gtol must be finite and positive')
    if not 0 <= args.seed < 2**32:
        parser.error('--seed must be between 0 and 2**32 - 1')
    OUT.mkdir(parents=True, exist_ok=True)

    df = load_analysis_data().copy()

    null_df = df.dropna(subset=["anaemia", "psu"]).copy()
    adjusted_df = df.dropna(subset=[
        "anaemia", "psu",
        "v013", "v106", "v190", "v025", "v213",
        "parity_cat", "bmi_cat", "v714", "v501", "v024",
    ]).copy()

    print(f"Fitting null model with n={len(null_df):,} ...")
    _, null = fit_model(null_df, "anaemia ~ 1", args.method,args.gtol,args.seed)

    print(f"Fitting adjusted model with n={len(adjusted_df):,} ...")
    adjusted_result, adjusted = fit_model(
        adjusted_df, ADJUSTED_FORMULA, args.method,args.gtol,args.seed
    )

    pcv = (
        null["cluster_variance"] - adjusted["cluster_variance"]
    ) / null["cluster_variance"]

    summary = pd.DataFrame([
        {"model": "Null", "n": len(null_df), **null, "pcv": np.nan},
        {"model": "Adjusted", "n": len(adjusted_df), **adjusted, "pcv": pcv},
    ])
    summary.to_csv(
        OUT / f"community_heterogeneity_{args.method}.csv",
        index=False,
    )

    fe_names = adjusted_result.model.exog_names
    fe_mean = np.asarray(adjusted_result.fe_mean)
    pd.DataFrame({
        "term": fe_names,
        "estimate": fe_mean,
        "odds_ratio": np.exp(fe_mean),
    }).to_csv(
        OUT / f"multilevel_adjusted_fixed_effects_{args.method}.csv",
        index=False,
    )

    print("\nCommunity heterogeneity")
    print(summary.to_string(index=False))
    if not summary['optimizer_success'].all():
        print('\nWARNING: at least one optimizer reported non-convergence; '
              'matching locked estimates does not establish numerical convergence.')
    print("\nLocked comparison values:")
    print("Null:     SD 0.387 | variance 0.150 | ICC 0.0435 | MOR 1.45")
    print("Adjusted: SD 0.327 | variance 0.107 | ICC 0.0314 | MOR 1.37")
    print("PCV:      0.288")

    if args.method == "map":
        print(
            "\nNote: MAP/Laplace failed to reproduce the locked variance "
            "components in validation and is retained for diagnostics only."
        )
    else:
        print(
            "\nNote: statsmodels may emit a VB convergence warning even when "
            "the reproduced variance components match the locked results. "
            "That warning should be retained in the reproducibility record."
        )


if __name__ == "__main__":
    main()
