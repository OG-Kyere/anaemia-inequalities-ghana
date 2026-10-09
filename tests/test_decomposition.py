import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import importlib.util

spec = importlib.util.spec_from_file_location(
    "decomp", ROOT / "src" / "03_inequality_decomposition.py"
)
decomp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(decomp)


class DecompositionTests(unittest.TestCase):
    def test_weighted_cov_zero_for_constant(self):
        x = np.ones(4)
        r = np.array([0.125, 0.375, 0.625, 0.875])
        w = np.ones(4)
        self.assertAlmostEqual(decomp.weighted_cov(x, r, w), 0.0)

    def test_psu_bootstrap_preserves_stratum_psu_count(self):
        df = pd.DataFrame({
            "strata": [1, 1, 1, 1, 2, 2, 2, 2],
            "psu": [10, 10, 11, 11, 20, 20, 21, 21],
            "anaemia": [0, 1, 0, 1, 1, 0, 1, 0],
            "weight": 1.0,
            "wealth": np.arange(8),
        })
        rng = np.random.default_rng(1)
        boot = decomp.resample_psus_within_strata(df, rng)
        # Two PSU draws per stratum; row count stays the same here because
        # every PSU has two observations.
        self.assertEqual(len(boot), len(df))
        self.assertEqual(
            boot.groupby("strata")["psu_boot"].nunique().to_dict(),
            {1: 2, 2: 2},
        )

    def test_missing_category_is_not_encoded_as_reference(self):
        df=pd.DataFrame({'anaemia':[0,1], 'weight':[1.,1.], 'v191':[1.,2.],
                         'strata':[1,1], 'psu':[1,2], 'v013':[1,2], 'v133':[4,5],
                         'v025':[1,np.nan], 'v213':[0,1], 'v201':[0,1], 'bmi':[20.,21.],
                         'v714':[1,1], 'v501':[0,1]})
        self.assertEqual(decomp.analysis_frame(df).index.tolist(),[0])


if __name__ == "__main__":
    unittest.main()
