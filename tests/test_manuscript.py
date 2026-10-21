import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from manuscript_checks import citation_issues, markdown_tables


class ManuscriptTests(unittest.TestCase):
    def test_final_manuscript_citations(self):
        self.assertEqual(citation_issues((ROOT/'submission/jph_main_manuscript.md').read_text(encoding='utf8')), [])

    def test_out_of_order_or_unused_references_are_detected(self):
        issues = citation_issues('Text.[2]\n## References\n1. First\n2. Second\n')
        self.assertTrue(any('first appearance' in x for x in issues))
        self.assertTrue(any('Uncited' in x for x in issues))

    def test_tables_strip_markup_and_preserve_numbers(self):
        rows = markdown_tables('| Factor | Value |\n|---|---:|\n| **BMI** | **77.7%** |')[0]
        self.assertEqual(rows, [['Factor','Value'],['BMI','77.7%']])

    def test_table_column_mismatch_is_rejected(self):
        with self.assertRaises(ValueError):
            markdown_tables('| Factor | Value |\n|---|---|\n| BMI |')

    def test_promoted_decomposition_matches_locked_aggregate_outputs(self):
        import csv
        rows = markdown_tables((ROOT/'results/table3_inequality_and_heterogeneity.md').read_text(encoding='utf8'))[0][1:]
        points = {r['domain']: r for r in csv.DictReader((ROOT/'results/reproduced/inequality_decomposition_point.csv').read_text(encoding='utf8').splitlines())}
        intervals = {r['domain']: r for r in csv.DictReader((ROOT/'results/reproduced/inequality_decomposition_bootstrap_intervals.csv').read_text(encoding='utf8').splitlines())}
        self.assertEqual({r[0] for r in rows}, set(points))
        for domain, absolute, percent, interval in rows:
            self.assertAlmostEqual(float(absolute), float(points[domain]['absolute_contribution']), delta=0.0000005)
            self.assertAlmostEqual(float(percent.rstrip('%')), float(points[domain]['percent_of_observed_E']), delta=0.05)
            lower, upper = map(float, interval.split(' to '))
            self.assertAlmostEqual(lower, float(intervals[domain]['bootstrap_ci_low']), delta=0.0000005)
            self.assertAlmostEqual(upper, float(intervals[domain]['bootstrap_ci_high']), delta=0.0000005)

    def test_promoted_multilevel_table_matches_locked_aggregate_outputs(self):
        import csv
        rows = dict((r[0], r[1:]) for r in markdown_tables((ROOT/'results/table3_inequality_and_heterogeneity.md').read_text(encoding='utf8'))[1][1:])
        models = list(csv.DictReader((ROOT/'results/reproduced/community_heterogeneity_vb.csv').read_text(encoding='utf8').splitlines()))
        for column, model in enumerate(models):
            self.assertEqual(int(rows['Women, n'][column].replace(',', '')), int(model['n']))
            for label, field, tolerance in [('Cluster-level SD','cluster_sd',0.0005), ('Cluster-level variance','cluster_variance',0.0005), ('Median odds ratio','mor',0.005)]:
                self.assertAlmostEqual(float(rows[label][column]), float(model[field]), delta=tolerance)
            self.assertAlmostEqual(float(rows['ICC'][column].rstrip('%')), 100*float(model['icc']), delta=0.005)
        self.assertAlmostEqual(float(rows['Proportional change in variance'][1].rstrip('%')), 100*float(models[1]['pcv']), delta=0.05)

    def test_selected_display_exports_preserve_both_promoted_panels(self):
        import ast
        import csv
        import tempfile
        source = ast.parse((ROOT/'src/05_prepare_submission_assets.py').read_text(encoding='utf8'))
        function = next(n for n in source.body if isinstance(n, ast.FunctionDef) and n.name == 'extract_markdown_table')
        scope = {'Path': Path, 'csv': csv, 'markdown_tables': markdown_tables}
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<table-export>', 'exec'), scope)
        table_source = ROOT/'results/table3_inequality_and_heterogeneity.md'
        with tempfile.TemporaryDirectory() as directory:
            for panel in range(2):
                target = Path(directory)/f'panel_{panel}.csv'
                scope['extract_markdown_table'](table_source, target, panel)
                with target.open(encoding='utf-8-sig', newline='') as stream:
                    exported = list(csv.reader(stream))
                self.assertEqual(exported, markdown_tables(table_source.read_text(encoding='utf8'))[panel])
        main = next(n for n in source.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
        calls = [n for n in ast.walk(main) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'extract_markdown_table']
        panel_calls = [n for n in calls if 'table3_inequality_and_heterogeneity.md' in ast.unparse(n)]
        self.assertEqual(sorted(n.args[2].value for n in panel_calls), [0, 1])

    def test_main_and_supplementary_display_placement(self):
        import re
        main = (ROOT/'submission/jph_main_manuscript.md').read_text(encoding='utf8')
        displays = main.split('## Main displays', 1)[1]
        self.assertEqual(re.findall(r'\*\*(Table [IVX]+|Figure \d+)\.', displays), ['Table I', 'Table II', 'Table III', 'Figure 1'])
        self.assertIn('Source: `figures/figure2_regional_prevalence.svg`', displays)
        supplement = (ROOT/'supplementary/supplementary_material.md').read_text(encoding='utf8')
        self.assertEqual(re.findall(r'^## Supplementary Table (S\d+)\.', supplement, re.M), ['S1'])
        self.assertEqual(re.findall(r'^## Supplementary Figure (S\d+)$', supplement, re.M), ['S1','S2','S3'])
        self.assertIn('Supplementary Figure S1', main.split('## Discussion')[0])
        self.assertNotIn('(Figure 2)', main)


if __name__ == '__main__': unittest.main()
