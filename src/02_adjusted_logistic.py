"""Survey-weighted logistic regression with design-based PSU sandwich SEs."""

from pathlib import Path

import numpy as np
import pandas as pd
import patsy
import scipy.stats as st
import statsmodels.api as sm

from common import load_analysis_data

OUT = Path("results/reproduced")
OUT.mkdir(parents=True, exist_ok=True)


FORMULA = """
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


def design_covariance(X, y, p, w, strata, psu):
    x = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    p = np.asarray(p, dtype=float).reshape(-1)
    w = np.asarray(w, dtype=float).reshape(-1)

    bread = x.T @ ((w * p * (1.0 - p))[:, None] * x)
    bread_inv = np.linalg.pinv(bread)

    scores = (w * (y - p))[:, None] * x
    score_df = pd.DataFrame(scores)
    score_df["strata"] = np.asarray(strata)
    score_df["psu"] = np.asarray(psu)

    cols = list(range(x.shape[1]))
    cluster = (
        score_df.groupby(["strata", "psu"], observed=True)[cols]
        .sum()
        .reset_index()
    )

    meat = np.zeros((x.shape[1], x.shape[1]), dtype=float)
    for _, g in cluster.groupby("strata", observed=True):
        m = len(g)
        if m <= 1:
            continue
        u = g[cols].to_numpy(dtype=float)
        centered = u - u.mean(axis=0, keepdims=True)
        meat += (m / (m - 1.0)) * centered.T @ centered

    return bread_inv @ meat @ bread_inv


def main():
    df = load_analysis_data().copy()

    model_df = df.dropna(subset=[
        "anaemia", "v013", "v106", "v190", "v025", "v213",
        "parity_cat", "bmi_cat", "v714", "v501", "v024",
        "weight", "strata", "psu",
    ]).copy()

    y, X = patsy.dmatrices(
        FORMULA,
        model_df,
        return_type="dataframe",
        NA_action="raise",
    )

    glm = sm.GLM(
        y,
        X,
        family=sm.families.Binomial(),
        freq_weights=model_df.loc[X.index, "weight"],
    ).fit()

    p = glm.predict(X)
    cov = design_covariance(
        X,
        y.iloc[:, 0],
        p,
        model_df.loc[X.index, "weight"],
        model_df.loc[X.index, "strata"],
        model_df.loc[X.index, "psu"],
    )
    se = np.sqrt(np.diag(cov))
    beta = glm.params.to_numpy()

    z = beta / se
    pval = 2.0 * st.norm.sf(np.abs(z))
    low = beta - 1.96 * se
    high = beta + 1.96 * se

    result = pd.DataFrame({
        "term": X.columns,
        "beta": beta,
        "se_design": se,
        "aOR": np.exp(beta),
        "ci_low": np.exp(low),
        "ci_high": np.exp(high),
        "p_value": pval,
    })

    result.to_csv(OUT / "adjusted_logistic_model.csv", index=False)
    print(f"Analytic n = {len(model_df):,}")
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
