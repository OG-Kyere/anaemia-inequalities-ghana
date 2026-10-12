"""Prepare journal-upload assets from repository sources.

Creates:
- editable CSV versions of Tables I and II;
- high-resolution PNG and TIFF versions of Figures 1 and 2.

This Windows-safe version uses Matplotlib directly and does not require Cairo.
Outputs go to submission/generated/.
"""

from __future__ import annotations

import csv
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "submission" / "generated"
from manuscript_checks import markdown_tables


def extract_markdown_table(source: Path, output: Path, table_index: int = 0) -> None:
    tables = markdown_tables(source.read_text(encoding='utf-8'))

    if table_index >= len(tables):
        raise ValueError(f"No table {table_index} found in {source}")

    rows = tables[table_index]

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


def make_concentration_curve(require_reproduced=False) -> str:
    source = ROOT/'results/reproduced/concentration_curve.csv'
    if source.exists():
        curve = pd.read_csv(source)
        population = curve['population_share'].to_numpy()
        anaemia = curve['anaemia_share'].to_numpy()
        provenance = 'Aggregate curve regenerated from analysis output'
        indices=pd.read_csv(ROOT/'results/reproduced/concentration_indices.csv').iloc[0]
        intervals=pd.read_csv(ROOT/'results/reproduced/full_sample_erreygers_bootstrap_interval.csv').iloc[0]
        annotation=(f"Erreygers index = {indices['erreygers_index']:.4f}\n"
                    f"95% CI: {intervals['bootstrap_ci_low']:.4f} to {intervals['bootstrap_ci_high']:.4f}")
    else:
        if require_reproduced:
            raise FileNotFoundError('Run the authorized-data core pipeline to regenerate concentration_curve.csv before submission.')
        svg = ET.parse(ROOT/'figures/figure1_concentration_curve.svg')
        line = next(element for element in svg.iter() if element.tag.endswith('polyline') and element.get('class')=='line')
        xy=np.array([[float(value) for value in pair.split(',')] for pair in line.get('points').split()])
        population=(xy[:,0]-90)/640
        anaemia=(540-xy[:,1])/480
        provenance = 'Preview using stored SVG curve points; empirical curve not independently reproduced'
        annotation='Erreygers index = -0.0589\n95% CI: -0.0924 to -0.0249'

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
        annotation,
        transform=ax.transAxes,
        va="top",
    )
    ax.legend(frameon=False, loc="lower right")
    if not source.exists():
        fig.text(.5, .01, 'PREVIEW: stored curve points; regenerate from authorized data before submission.',
                 ha='center', fontsize=8)

    save_png_and_tiff(fig, "Figure_1_concentration_curve")
    return provenance


def make_regional_prevalence() -> None:
    import re
    rows=markdown_tables((ROOT/'results/sensitivity_and_geographic_checks.md').read_text(encoding='utf8'))[0][1:]
    regions=[row[0] for row in rows]
    prevalence=np.array([float(row[2].rstrip('%')) for row in rows])
    intervals=np.array([[float(v) for v in re.findall(r'\d+\.\d+',row[3])] for row in rows])
    ci_low,ci_high=intervals[:,0],intervals[:,1]

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
    ax.text(.98, .98, 'National: 41.1%', transform=ax.transAxes,
            ha='right',va='top',fontsize=10,
            bbox={'facecolor':'white','edgecolor':'none','alpha':.9})

    save_png_and_tiff(fig, "Figure_2_regional_prevalence")


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--require-reproduced',action='store_true',help='Require an empirical concentration curve from the authorized-data pipeline.')
    args=parser.parse_args()
    if args.require_reproduced and not (ROOT/'results/reproduced/concentration_curve.csv').exists():
        parser.error('Missing empirical concentration_curve.csv; run the authorized-data core pipeline first.')
    OUT.mkdir(parents=True,exist_ok=True)
    extract_markdown_table(
        ROOT / "results" / "table1_weighted_characteristics.md",
        OUT / "Table_I_weighted_characteristics.csv",
    )

    extract_markdown_table(
        ROOT / "results" / "table2_full_adjusted_model.md",
        OUT / "Table_II_adjusted_logistic_regression.csv",
    )
    extract_markdown_table(ROOT/'results/table2_full_adjusted_model.md',
                           OUT/'Table_S3_overall_Wald_tests.csv',1)

    provenance=make_concentration_curve(args.require_reproduced)
    make_regional_prevalence()
    (OUT/'asset_provenance.json').write_text(json.dumps({'figure1':provenance,
        'tables':'Locked repository aggregate tables; not re-estimated during export',
        'figure2':'Repository regional aggregate table; not re-estimated during export'},indent=2),encoding='utf8')

    print("Submission assets created in:")
    print(OUT)
    for path in sorted(OUT.iterdir()):
        print(f" - {path.name}")


if __name__ == "__main__":
    main()
