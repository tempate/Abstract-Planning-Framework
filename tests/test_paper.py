import unittest

from experiments.paper import update_table

TABLE = r"""\multicolumn{14}{l}{\emph{Resource levels}} \\
nomystery & 19 & \textbf{4} & 2 & \textbf{12} & 10 & 20 & 10 & 12 & 18 & 17 & -- & -- & -- \\
\midrule
Total & 19 & 4 & 2 & 12 & 10 & 20 & 10 & 12 & 18 & 17 & -- & -- & -- \\
\bottomrule
"""


class PaperTableTests(unittest.TestCase):
    def test_a_track_s_columns_take_the_counts_and_bold_the_better_of_each_pair(self):
        tex, changed = update_table(TABLE, "sat", "resources", {"nomystery": [19, 4, 6, 9, 10]})

        self.assertIn(r"nomystery & 19 & 4 & \textbf{6} & 9 & \textbf{10} & 20 & 10 & 12", tex)
        # The total never bolds, and the opt columns stay as they were.
        self.assertIn("Total & 19 & 4 & 6 & 9 & 10 & 20 & 10 & 12", tex)
        self.assertEqual(changed, ["nomystery", "Total"])

    def test_a_row_the_results_lack_stops_the_update(self):
        with self.assertRaises(SystemExit):
            update_table(TABLE, "sat", "resources", {})
