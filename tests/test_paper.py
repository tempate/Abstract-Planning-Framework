import unittest

from experiments.paper import update_figure, update_table

TABLE = r"""\multicolumn{14}{l}{\emph{Resource levels}} \\
nomystery & 19 & \textbf{4} & 2 & \textbf{12} & 10 & 20 & 10 & 12 & 18 & 17 & -- & -- & -- \\
\midrule
Total & 19 & 4 & 2 & 12 & 10 & 20 & 10 & 12 & 18 & 17 & -- & -- & -- \\
\bottomrule
"""


class PaperTableTests(unittest.TestCase):
    def test_a_track_s_columns_take_the_branch_counts_and_bold_the_better_of_each_pair(self):
        tex, changed = update_table(
            TABLE, "sat", "resources", {"nomystery": [19, 4, 2, 12, 10]}, {"nomystery": [19, 4, 6, 9, 10]}
        )

        self.assertIn(r"nomystery & 19 & 4 & \textbf{6} & 9 & \textbf{10} & 20 & 10 & 12", tex)
        # The total never bolds, and the opt columns stay as they were.
        self.assertIn("Total & 19 & 4 & 6 & 9 & 10 & 20 & 10 & 12", tex)
        self.assertEqual(changed, ["nomystery", "Total"])

    def test_a_base_that_does_not_reproduce_the_table_changes_nothing(self):
        with self.assertRaises(SystemExit):
            update_table(TABLE, "sat", "resources", {"nomystery": [19, 5, 2, 12, 10]}, {"nomystery": [19, 4, 6, 9, 10]})


class PaperFigureTests(unittest.TestCase):
    def test_a_set_matches_without_its_old_colour_tags(self):
        figure = r"\runtimeplot{\LMcut}{(1.00,2.00) [0] (3.00,4.00) [4]}"

        figure, replaced = update_figure(figure, ["(1.00,2.00) (3.00,4.00)"], ["(1.00,5.00)"])

        self.assertIn(r"\runtimeplot{\LMcut}{(1.00,5.00)}", figure)
        self.assertEqual(replaced, 1)
