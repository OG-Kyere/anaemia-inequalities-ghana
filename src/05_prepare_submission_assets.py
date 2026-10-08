"""Prepare journal-upload assets from repository sources.

Creates:
- editable CSV versions of Tables I and II;
- high-resolution PNG and TIFF versions of Figures 1 and 2.

This Windows-safe version uses Matplotlib directly and does not require Cairo.
Outputs go to submission/generated/.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "submission" / "generated"
OUT.mkdir(parents=True, exist_ok=True)


def extract_markdown_table(source: Path, output: Path, table_index: int = 0) -> None:
    lines = source.read_text(encoding="utf-8").splitlines()
    tables = []
    current = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            current.append(stripped)
        else:
            if current:
                tables.append(current)
                current = []

    if current:
        tables.append(current)

    if table_index >= len(tables):
        raise ValueError(f"No table {table_index} found in {source}")

    rows = []
    for i, line in enumerate(tables[table_index]):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if i == 1 and all(set(c) <= {"-", ":"} for c in cells):
            continue
        rows.append(cells)

    with output.open("w", encoding="utf-8-sig", newline="") as fh:
        csv.writer(fh).writerows(rows)


def save_png_and_tiff(fig, stem: str) -> None:
    png_path = OUT / f"{stem}.png"
    tiff_path = OUT / f"{stem}.tiff"

    fig.savefig(png_path, dpi=600, bbox_inches="tight")
    plt.close(fig)

    with Image.open(png_path) as im:
        im = im.convert("RGB")
        im.save(
            tiff_path,
            format="TIFF",
            compression="tiff_lzw",
            dpi=(600, 600),
        )


def make_concentration_curve() -> None:
    population = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    anaemia = np.array([0.0, 0.116, 0.224, 0.327, 0.435, 0.525, 0.615, 0.714, 0.811, 0.912, 1.0])

    fig, ax = plt.subplots(figsize=(7.6, 6.2))
    ax.plot(population, population, linestyle="--", linewidth=1.5, label="Line of equality")
    ax.plot(population, anaemia, linewidth=2.0, marker="o", markersize=3.5, label="Anaemia concentration curve")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Cumulative population share, poorest to richest")
    ax.set_ylabel("Cumulative share of anaemia")
    ax.set_title("Concentration curve for anaemia")
    ax.grid(True, linewidth=0.5, alpha=0.4)
    ax.text(
        0.03,
        0.95,
        "Erreygers index = -0.0589\n95% CI: -0.0914 to -0.0212",
        transform=ax.transAxes,
        va="top",
    )
    ax.legend(frameon=False, loc="lower right")

    save_png_and_tiff(fig, "Figure_1_concentration_curve")


def make_regional_prevalence() -> None:
    regions = [
        "Bono", "Ahafo", "Western North", "Ashanti", "Eastern", "Greater Accra",
        "Bono East", "Volta", "Savannah", "Central", "North East", "Western",
        "Upper West", "Upper East", "Northern", "Oti",
    ]
    prevalence = np.array([
        30.1, 35.6, 36.3, 37.5, 37.5, 38.8, 40.3, 43.0,
        43.2, 44.4, 45.0, 45.9, 46.3, 47.0, 48.4, 51.8,
    ])
    ci_low = np.array([
        23.3, 31.3, 30.2, 33.4, 31.9, 34.5, 35.0, 37.5,
        38.4, 39.2, 40.3, 40.3, 41.0, 41.0, 44.4, 46.8,
    ])
    ci_high = np.array([
        37.0, 39.9, 42.4, 41.5, 43.1, 43.1, 45.7, 48.5,
        48.0, 49.6, 49.7, 51.4, 51.6, 53.0, 52.3, 56.8,
    ])

    y = np.arange(len(regions))
    xerr = np.vstack([prevalence - ci_low, ci_high - prevalence])

    fig, ax = plt.subplots(figsize=(8.6, 8.0))
    ax.errorbar(
        prevalence,
        y,
        xerr=xerr,
        fmt="o",
        markersize=4,
        capsize=3,
        linewidth=1.2,
    )
    ax.axvline(41.1, linestyle="--", linewidth=1.2)
    ax.set_yticks(y)
    ax.set_yticklabels(regions)
    ax.invert_yaxis()
    ax.set_xlabel("Anaemia prevalence (%)")
    ax.set_title("Survey-weighted anaemia prevalence by region")
    ax.grid(True, axis="x", linewidth=0.5, alpha=0.4)
    ax.text(41.5, -0.6, "National: 41.1%", va="bottom")

    save_png_and_tiff(fig, "Figure_2_regional_prevalence")


def main() -> None:
    extract_markdown_table(
        ROOT / "results" / "table1_weighted_characteristics.md",
        OUT / "Table_I_weighted_characteristics.csv",
    )

    extract_markdown_table(
        ROOT / "results" / "table2_full_adjusted_model.md",
        OUT / "Table_II_adjusted_logistic_regression.csv",
    )

    make_concentration_curve()
    make_regional_prevalence()

    print("Submission assets created in:")
    print(OUT)
    for path in sorted(OUT.iterdir()):
        print(f" - {path.name}")


if __name__ == "__main__":
    main()
