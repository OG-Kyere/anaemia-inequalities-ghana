"""Run the reproducible analysis pipeline.

By default this runs the validated core analysis only. Use --extended to add
the inequality decomposition/bootstrap. Use --multilevel to additionally fit
the community random-intercept models.
"""

import argparse
import subprocess
import sys


CORE = [
    "src/01_descriptive_and_inequality.py",
    "src/02_adjusted_logistic.py",
]


def run(script, *args):
    print(f"\n=== Running {script} {' '.join(args)} ===")
    subprocess.run([sys.executable, script, *args], check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--multilevel", action="store_true")
    parser.add_argument("--bootstrap-reps", type=int, default=200)
    parser.add_argument("--multilevel-method", choices=["vb", "map"], default="vb")
    args = parser.parse_args()

    for script in CORE:
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

    print("\nRequested reproducibility run completed successfully.")
    print("Outputs are under results/reproduced/.")


if __name__ == "__main__":
    main()
