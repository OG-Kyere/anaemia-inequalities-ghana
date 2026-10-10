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
    weighted_mean,
    concentration_curve,
    bootstrap_concentration_indices,
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

    def test_domain_variance_retains_outside_psus(self):
        domain = pd.Series([True,True,False,False,False,False,False,False])
        estimate,se = survey_domain_proportion(self.y,domain,self.w,self.strata,self.psu)
        self.assertAlmostEqual(estimate,.5)
        self.assertAlmostEqual(se,0.)

    def test_zero_or_negative_weight_totals_raise(self):
        for weights in [pd.Series([0.,0.]), pd.Series([-1.,2.])]:
            with self.assertRaises(ValueError): weighted_mean(pd.Series([0.,1.]),weights)

    def test_all_zero_outcome_has_zero_erreygers_and_undefined_standard_index(self):
        result=concentration_indices(pd.Series([0.,0.]),pd.Series([1.,2.]),pd.Series([1.,1.]))
        self.assertEqual(result['erreygers_index'],0.)
        self.assertTrue(np.isnan(result['concentration_index']))

    def test_missing_weight_does_not_receive_a_fractional_rank(self):
        ranks=weighted_midrank(pd.Series([1.,1.,2.]),pd.Series([1.,np.nan,1.]))
        self.assertTrue(np.isnan(ranks.iloc[1]))

    def test_singleton_psu_variance_is_not_silently_zero(self):
        with self.assertRaisesRegex(ValueError,'singleton'):
            survey_ratio_se(pd.Series([0.,1.]),pd.Series([1.,1.]),pd.Series([1,1]),pd.Series([1,1]))

    def test_curve_aggregates_ties_and_reaches_unit_endpoint(self):
        curve=concentration_curve(pd.Series([1.,0.,1.]),pd.Series([1.,1.,2.]),pd.Series([1.,1.,2.]),points=3)
        np.testing.assert_allclose(curve.to_numpy(),[[0,0],[.5,1/3],[1,1]])

    def test_full_sample_bootstrap_is_deterministic(self):
        frame=pd.DataFrame({'anaemia':self.y,'weight':self.w,'strata':self.strata,'psu':self.psu,'v191':np.arange(8)})
        pd.testing.assert_frame_equal(bootstrap_concentration_indices(frame,4,10),bootstrap_concentration_indices(frame,4,10))


if __name__ == "__main__":
    unittest.main()
