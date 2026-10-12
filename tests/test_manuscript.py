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


if __name__ == '__main__': unittest.main()
