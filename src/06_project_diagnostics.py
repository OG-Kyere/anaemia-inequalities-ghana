"""Project diagnostics for the anaemia inequalities study.

Run from the repository root:

    python src/06_project_diagnostics.py

The script performs:
- Python/import checks;
- syntax compilation of project Python files;
- unit tests;
- repository/submission consistency checks;
- optional DHS-data validation when DHS_IR_PATH is available;
- generated submission-asset checks.

It does not modify data or analysis outputs.
"""

from __future__ import annotations

import importlib
import os
import py_compile
import subprocess
import sys
import json
from manuscript_checks import citation_issues
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_IMPORTS = [
    "numpy",
    "pandas",
    "scipy",
    "statsmodels",
    "patsy",
    "matplotlib",
    "PIL",
    "pyarrow",
]

PYTHON_FILES = [
    ROOT / "run_analysis.py",
    *sorted((ROOT / "src").glob("*.py")),
    *sorted((ROOT / "tests").glob("*.py")),
]

SUBMISSION_FILES = [
    ROOT / "submission" / "jph_main_manuscript.md",
    ROOT / "submission" / "jph_title_page.md",
    ROOT / "submission" / "jph_cover_letter.md",
    ROOT / "supplementary" / "supplementary_material.md",
]

STALE_FINAL_TEXT = {
    "77.8%": "old BMI decomposition percentage",
    "17.3%": "old education decomposition percentage",
    "-0.0592": "old BMI bootstrap lower bound",
    "-0.0318": "old BMI bootstrap upper bound",
}

EXPECTED_PLACEHOLDERS = [
    "[insert email before submission]",
    "[to be confirmed before submission]",
]


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def check_imports() -> int:
    failures = 0
    print("\n== Dependency checks ==")
    for name in REQUIRED_IMPORTS:
        try:
            mod = importlib.import_module(name)
            version = getattr(mod, "__version__", "version unavailable")
            ok(f"{name}: {version}")
        except Exception as exc:
            failures += 1
            fail(f"{name}: {exc}")
    return failures


def check_syntax() -> int:
    failures = 0
    print("\n== Syntax compilation ==")
    for path in PYTHON_FILES:
        try:
            py_compile.compile(str(path), doraise=True)
            ok(str(path.relative_to(ROOT)))
        except Exception as exc:
            failures += 1
            fail(f"{path.relative_to(ROOT)}: {exc}")
    return failures


def run_unit_tests() -> int:
    print("\n== Unit tests ==")
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )
    if proc.returncode == 0:
        ok("unit tests passed")
        return 0
    fail(f"unit tests exited with code {proc.returncode}")
    return 1


def check_submission_consistency() -> int:
    failures = 0
    print("\n== Submission consistency ==")

    for path in SUBMISSION_FILES:
        if not path.exists():
            failures += 1
            fail(f"missing {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        for token, meaning in STALE_FINAL_TEXT.items():
            if token in text:
                failures += 1
                fail(f"{path.relative_to(ROOT)} contains {meaning}: {token}")
        if any(ord(c) < 32 and c not in '\n\r\t' for c in text):
            failures += 1
            fail(f'{path.relative_to(ROOT)} contains broken equation/control characters')

    manuscript = ROOT / 'submission/jph_main_manuscript.md'
    if manuscript.exists():
        for issue in citation_issues(manuscript.read_text(encoding='utf-8')):
            failures += 1
            fail(issue)
        if not citation_issues(manuscript.read_text(encoding='utf-8')):
            ok('All references are cited and numbered by first appearance')
        text = manuscript.read_text(encoding='utf-8')
        if '## Ethics statement' not in text:
            failures += 1
            fail('Canonical submission manuscript has no ethics statement')
        if 'pending author confirmation' in text.lower():
            warn('Author contributions / final approval still require author confirmation')
        if 'not survey-weighted' not in text:
            failures += 1
            fail('Multilevel weighting limitation must be stated explicitly')

    title = (ROOT / "submission" / "jph_title_page.md").read_text(encoding="utf-8")
    final_authors = [
        "Gideon Ofosu Kyere",
        "Wilhemina Adoma Pels",
        "Prince Apaah",
        "Clement Acheampong",
    ]
    missing_authors = [name for name in final_authors if name not in title]
    if not missing_authors:
        ok("all four confirmed authors appear on title page in the submission package")
    else:
        failures += 1
        fail("title page is missing confirmed author(s): " + ", ".join(missing_authors))

    positions = [title.find(name) for name in final_authors]
    if all(pos >= 0 for pos in positions) and positions == sorted(positions):
        ok("author order is Gideon, Wilhemina, Prince, Clement")
    else:
        failures += 1
        fail("title-page author order does not match the confirmed final order")

    if "Academic supervisor" in title or "## Academic supervisor" in title:
        failures += 1
        fail("title page still treats Wilhemina Adoma Pels as a non-author supervisor")
    else:
        ok("no obsolete supervisor-only title-page section remains")

    unresolved = []
    for path in SUBMISSION_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for token in EXPECTED_PLACEHOLDERS:
            if token in text:
                unresolved.append((path.relative_to(ROOT), token))

    if unresolved:
        for path, token in unresolved:
            warn(f"unresolved administrative placeholder in {path}: {token}")
    else:
        ok("no obsolete email/affiliation placeholders remain")

    return failures


def check_gitignore() -> int:
    print("\n== Data-governance / ignore checks ==")
    path = ROOT / ".gitignore"
    text = path.read_text(encoding="utf-8") if path.exists() else ""

    required = [
        "data/raw/",
        "data/processed/",
        "*.dta",
        "submission/generated/",
    ]
    failures = 0
    for rule in required:
        if rule in text:
            ok(f".gitignore contains {rule}")
        else:
            failures += 1
            fail(f".gitignore missing {rule}")

    if "\\n# Locally generated" in text:
        failures += 1
        fail(".gitignore contains literal escaped newline characters")
    return failures


def check_data_if_available() -> int:
    print("\n== DHS data validation ==")
    configured = os.environ.get("DHS_IR_PATH")
    if not configured:
        warn("DHS_IR_PATH is not set; skipping data-dependent diagnostics")
        return 0

    path = Path(configured)
    if not path.exists():
        fail(f"DHS_IR_PATH does not exist: {path}")
        return 1

    sys.path.insert(0, str(ROOT / "src"))
    try:
        from common import concentration_indices, load_analysis_data
    except Exception as exc:
        fail(f"could not import analysis helpers: {exc}")
        return 1

    try:
        df = load_analysis_data()
        failures = 0

        if len(df) == 7557:
            ok("valid anaemia sample n = 7,557")
        else:
            failures += 1
            fail(f"valid anaemia sample n = {len(df):,}; expected 7,557")

        weighted_n = float(df["weight"].sum())
        if abs(weighted_n - 7655.051315) < 1e-5:
            ok(f"weighted denominator = {weighted_n:.6f}")
        else:
            failures += 1
            fail(
                f"weighted denominator = {weighted_n:.6f}; "
                "expected 7655.051315"
            )

        prev = float((df["weight"] * df["anaemia"]).sum() / df["weight"].sum())
        if abs(prev - 0.411225) < 1e-5:
            ok(f"weighted anaemia prevalence = {prev:.6f}")
        else:
            failures += 1
            fail(f"weighted prevalence = {prev:.6f}; expected about 0.411225")

        ci = concentration_indices(df["anaemia"], df["v191"], df["weight"])
        if abs(ci["concentration_index"] - (-0.0358307533)) < 1e-5:
            ok(f"concentration index = {ci['concentration_index']:.6f}")
        else:
            failures += 1
            fail(f"concentration index = {ci['concentration_index']:.6f}")

        if abs(ci["erreygers_index"] - (-0.0589379693)) < 1e-5:
            ok(f"Erreygers index = {ci['erreygers_index']:.6f}")
        else:
            failures += 1
            fail(f"Erreygers index = {ci['erreygers_index']:.6f}")

        complete_bmi = int(df["bmi"].notna().sum())
        if complete_bmi == 7550:
            ok("BMI-complete analytic sample n = 7,550")
        else:
            failures += 1
            fail(f"BMI-complete n = {complete_bmi:,}; expected 7,550")

        return failures
    except Exception as exc:
        fail(f"data-dependent diagnostic failed: {exc}")
        return 1


def check_submission_assets() -> int:
    print("\n== Submission assets ==")
    generated = ROOT / "submission" / "generated"
    expected = [
        "Table_I_weighted_characteristics.csv",
        "Table_II_adjusted_logistic_regression.csv",
        "Figure_1_concentration_curve.png",
        "Figure_1_concentration_curve.tiff",
        "Figure_2_regional_prevalence.png",
        "Figure_2_regional_prevalence.tiff",
    ]

    if not generated.exists():
        warn(
            "submission/generated/ does not exist yet; run "
            "python src/05_prepare_submission_assets.py"
        )
        return 0

    missing = [name for name in expected if not (generated / name).exists()]
    if missing:
        for name in missing:
            fail(f"missing generated asset: {name}")
        return len(missing)
    else:
        ok("all six journal-upload assets are present")
    provenance=generated/'asset_provenance.json'
    if provenance.exists() and 'Preview' in json.loads(provenance.read_text())['figure1']:
        warn('Figure 1 uses stored preview points; regenerate the empirical curve before submission')
    if not missing:
        from PIL import Image
        for name in expected:
            if name.endswith(('.png','.tiff')):
                with Image.open(generated/name) as image:
                    image.verify()
                with Image.open(generated/name) as image:
                    if min(image.size)<1800 or min(image.info.get('dpi',(0,0)))<599:
                        fail(f'{name} is not a high-resolution 600-dpi export')
                        return 1
        ok('Image exports are readable and have the expected high-resolution dimensions/DPI')
    return 0


def main() -> None:
    print("Anaemia inequalities project diagnostics")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Repository: {ROOT}")

    failures = 0
    failures += check_imports()
    failures += check_syntax()
    failures += run_unit_tests()
    failures += check_submission_consistency()
    failures += check_gitignore()
    failures += check_data_if_available()
    failures += check_submission_assets()

    print("\n== Diagnostic summary ==")
    if failures:
        fail(f"{failures} critical diagnostic check(s) failed")
        raise SystemExit(1)

    ok("no critical diagnostic failures detected")
    print("Warnings may remain for unresolved administrative fields or ungenerated assets.")


if __name__ == "__main__":
    main()
