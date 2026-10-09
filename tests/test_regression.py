import importlib.util
import sys,unittest
from pathlib import Path
import numpy as np
import pandas as pd
import patsy
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
spec=importlib.util.spec_from_file_location('regression',ROOT/'src/02_adjusted_logistic.py')
reg=importlib.util.module_from_spec(spec);spec.loader.exec_module(reg)


class RegressionTests(unittest.TestCase):
    def test_joint_wald_uses_full_covariance(self):
        _,design=patsy.dmatrices('y ~ C(group)',pd.DataFrame({'y':[0,1,0,1,0,1],'group':[1,1,2,2,3,3]}),return_type='dataframe')
        covariance=np.array([[1,0,0],[0,2,1],[0,1,2]],dtype=float)
        result=reg.overall_wald_tests(np.array([0,1,2]),covariance,design.design_info)
        self.assertEqual(result.iloc[0]['df'],2)
        self.assertAlmostEqual(result.iloc[0]['wald_chi_square'],2.)

    def test_rank_deficient_wald_is_rejected(self):
        _,design=patsy.dmatrices('y ~ C(group)',pd.DataFrame({'y':[0,1,0],'group':[1,2,3]}),return_type='dataframe')
        with self.assertRaisesRegex(ValueError,'rank deficient'):
            reg.overall_wald_tests(np.zeros(3),np.zeros((3,3)),design.design_info)


if __name__=='__main__':unittest.main()
