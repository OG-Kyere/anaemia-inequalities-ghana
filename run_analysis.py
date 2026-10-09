"""Run the reproducible analysis pipeline.

By default this runs the validated core analysis only. Use --extended to add
the inequality decomposition/bootstrap. Use --multilevel to additionally fit
the community random-intercept models.
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


CORE = [
    "src/01_descriptive_and_inequality.py",
    "src/02_adjusted_logistic.py",
]


def run(script, *args):
    print(f"\n=== Running {script} {' '.join(args)} ===")
    subprocess.run([sys.executable, str(ROOT / script), *args], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--multilevel", action="store_true")
    parser.add_argument("--bootstrap-reps", type=int, default=200)
    parser.add_argument("--multilevel-method", choices=["vb", "map"], default="vb")
    args = parser.parse_args()
    if args.bootstrap_reps < 2:
        parser.error('--bootstrap-reps must be at least 2 to estimate intervals')

    for script in CORE:
        if script.endswith('01_descriptive_and_inequality.py'):
            run(script, '--bootstrap-reps', str(args.bootstrap_reps))
        else:
            run(script)

    if args.extended or args.multilevel:
        run(
            "src/03_inequality_decomposition.py",
            "--bootstrap-reps",
            str(args.bootstrap_reps),
        )

    if args.multilevel:
        run(
            "src/04_multilevel_heterogeneity.py",
            "--method",
            args.multilevel_method,
        )

    print("\nRequested pipeline commands finished. Review optimizer diagnostics and "
          "compare the outputs with validation records before interpreting results.")
    print("Outputs are under results/reproduced/.")


if __name__ == "__main__":
    main()
