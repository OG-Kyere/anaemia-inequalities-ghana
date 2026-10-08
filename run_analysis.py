"""Run the reproducible core analysis pipeline."""

import subprocess
import sys


SCRIPTS = [
    "src/01_descriptive_and_inequality.py",
    "src/02_adjusted_logistic.py",
]


def main():
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, script], check=True)

    print("\nCore reproducibility run completed successfully.")
    print("Outputs are under results/reproduced/.")


if __name__ == "__main__":
    main()
