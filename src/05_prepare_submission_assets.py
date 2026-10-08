"""Prepare journal-upload assets from repository sources.

Creates:
- editable CSV versions of Tables I and II;
- high-resolution PNG and TIFF versions of Figures 1 and 2.

Outputs go to submission/generated/.
"""

from __future__ import annotations

import csv
from pathlib import Path

import cairosvg
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


def render_svg(svg_path: Path, stem: str, width_px: int = 3600) -> None:
    png_path = OUT / f"{stem}.png"
    tiff_path = OUT / f"{stem}.tiff"

    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=width_px,
    )

    with Image.open(png_path) as im:
        if im.mode != "RGB":
            if "A" in im.getbands():
                bg = Image.new("RGB", im.size, "white")
                bg.paste(im, mask=im.getchannel("A"))
                im = bg
            else:
                im = im.convert("RGB")

        im.save(
            tiff_path,
            format="TIFF",
            compression="tiff_lzw",
            dpi=(600, 600),
        )


def main() -> None:
    extract_markdown_table(
        ROOT / "results" / "table1_weighted_characteristics.md",
        OUT / "Table_I_weighted_characteristics.csv",
    )

    extract_markdown_table(
        ROOT / "results" / "table2_full_adjusted_model.md",
        OUT / "Table_II_adjusted_logistic_regression.csv",
    )

    render_svg(
        ROOT / "figures" / "figure1_concentration_curve.svg",
        "Figure_1_concentration_curve",
    )

    render_svg(
        ROOT / "figures" / "figure2_regional_prevalence.svg",
        "Figure_2_regional_prevalence",
    )

    print("Submission assets created in:")
    print(OUT)
    for path in sorted(OUT.iterdir()):
        print(f" - {path.name}")


if __name__ == "__main__":
    main()
