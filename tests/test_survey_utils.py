import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common import (  # noqa: E402
    concentration_indices,
    survey_domain_proportion,
    survey_ratio_se,
    weighted_midrank,
)


class SurveyUtilityTests(unittest.TestCase):
    def setUp(self):
        # Two strata, two PSUs per stratum, two observations per PSU.
        self.y = pd.Series([0, 1, 0, 1, 1, 1, 0, 0], dtype=float)
        self.w = pd.Series(np.ones(8), dtype=float)
        self.strata = pd.Series([1, 1, 1, 1, 2, 2, 2, 2])
        self.psu = pd.Series([1, 1, 2, 2, 3, 3, 4, 4])

    def test_full_sample_weighted_prevalence(self):
        estimate, se = survey_ratio_se(
            self.y, self.w, self.strata, self.psu
        )
        self.assertAlmostEqual(estimate, 0.5)
        self.assertGreaterEqual(se, 0.0)

    def test_domain_estimate_uses_requested_domain(self):
        domain = pd.Series([True, True, False, False, True, False, False, False])
        estimate, se = survey_domain_proportion(
            self.y, domain, self.w, self.strata, self.psu
        )
        self.assertAlmostEqual(estimate, 2.0 / 3.0)
        self.assertGreaterEqual(se, 0.0)

    def test_weighted_midrank_handles_ties(self):
        values = pd.Series([1.0, 1.0, 2.0, 3.0])
        weights = pd.Series([1.0, 1.0, 1.0, 1.0])
        ranks = weighted_midrank(values, weights)
        self.assertAlmostEqual(ranks.iloc[0], 0.25)
        self.assertAlmostEqual(ranks.iloc[1], 0.25)
        self.assertAlmostEqual(ranks.iloc[2], 0.625)
        self.assertAlmostEqual(ranks.iloc[3], 0.875)

    def test_concentration_index_zero_for_constant_outcome(self):
        y = pd.Series([1.0, 1.0, 1.0, 1.0])
        wealth = pd.Series([1.0, 2.0, 3.0, 4.0])
        weights = pd.Series([1.0, 1.0, 1.0, 1.0])
        result = concentration_indices(y, wealth, weights)
        self.assertAlmostEqual(result["concentration_index"], 0.0)
        self.assertAlmostEqual(result["erreygers_index"], 0.0)


if __name__ == "__main__":
    unittest.main()
