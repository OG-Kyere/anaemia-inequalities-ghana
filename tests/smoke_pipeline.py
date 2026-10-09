"""Run every analysis stage on synthetic data, outside the repository directory.

This is a software smoke test, not a scientific validation or DHS-data substitute.
All synthetic data and outputs are held in a temporary directory and removed.
"""
import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix='anaemia-synthetic-') as directory:
        base = Path(directory)
        repo = base/'repo'
        repo.mkdir()
        shutil.copytree(ROOT/'src', repo/'src', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(ROOT/'run_analysis.py', repo/'run_analysis.py')
        rng = np.random.default_rng(713)
        n = 1600
        psu = np.repeat(np.arange(1,65),25)
        region = (psu-1)//4+1
        data = pd.DataFrame({
            'v005':rng.integers(200000,2000000,n),'v021':psu,'v022':region,
            'v024':region,'v025':rng.integers(1,3,n),'v012':rng.integers(15,50,n),
            'v013':rng.integers(1,8,n),'v106':rng.integers(0,4,n),'v133':rng.integers(0,17,n),
            'v190':rng.integers(1,6,n),'v191':rng.normal(0,1,n),'v201':rng.integers(0,9,n),
            'v213':rng.binomial(1,.15,n),'v445':rng.integers(1500,3800,n),
            'v501':rng.integers(0,6,n),'v714':rng.integers(0,2,n),
            'v456':rng.integers(70,160,n),'v457':np.where(rng.random(n)<.4,3,4),
        })
        path = base/'SYNTHETIC_TEST_ONLY.dta'
        data.to_stata(path, write_index=False)
        env = os.environ.copy()
        env['DHS_IR_PATH'] = str(path)
        result = subprocess.run([sys.executable, str(repo/'run_analysis.py'),
            '--extended', '--multilevel', '--bootstrap-reps', '2'], cwd=base,
            env=env, text=True, capture_output=True)
        if result.returncode:
            print(result.stdout)
            print(result.stderr)
            raise SystemExit(result.returncode)
        out = repo/'results/reproduced'
        expected = ['overall_prevalence.csv','subgroup_prevalence.csv',
            'concentration_indices.csv','concentration_curve.csv',
            'full_sample_erreygers_bootstrap_interval.csv','adjusted_logistic_model.csv',
            'adjusted_logistic_wald_tests.csv','inequality_decomposition_bootstrap_intervals.csv',
            'community_heterogeneity_vb.csv']
        assert all((out/name).exists() for name in expected)
        assert len(pd.read_csv(out/'adjusted_logistic_wald_tests.csv')) == 10
        assert len(pd.read_csv(out/'overall_prevalence.csv')) == 1
        assert pd.read_csv(out/'overall_prevalence.csv').iloc[0]['n_unweighted'] == n
        assert 'optimizer_success' in pd.read_csv(out/'community_heterogeneity_vb.csv').columns
        print('All analysis stages passed on isolated synthetic data from outside the repository.')
        print('This does not validate the locked DHS estimates.')


if __name__ == '__main__':
    main()
