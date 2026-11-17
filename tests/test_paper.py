import unittest

from experiments.paper import _htg_name, update_summary, update_table

TABLE = r"""\begin{table*}
\multicolumn{11}{l}{\emph{IPC Resources}} \\
nomystery & 19 & \textbf{4} & 2 & \textbf{12} & 10 & 20 & 10 & 12 & 18 & 17 \\
\bottomrule
\label{tab:ipc}
\end{table*}
"""
SUMMARY = r"""\begin{table}
\multicolumn{6}{l}{\emph{IPC Resources}} \\
Satisficing & 330 & 88 & \textbf{92} & \textbf{305} & 122 \\
Optimal & 373 & \textbf{125} & 120 & \textbf{209} & 132 \\
\bottomrule
\label{tab:summary}
\end{table}
"""


class PaperTableTests(unittest.TestCase):
    def test_a_track_s_columns_take_the_counts_and_bold_the_better_of_each_pair(self):
        tex, changed = update_table(TABLE, "IPC Resources", "sat", {"nomystery": [19, 4, 6, 9, 10]})

        # The opt columns stay as they were.
        self.assertIn(r"nomystery & 19 & 4 & \textbf{6} & 9 & \textbf{10} & 20 & 10 & 12", tex)
        self.assertEqual(changed, ["nomystery"])

    def test_a_row_the_results_lack_or_a_domain_the_paper_lacks_stops_the_update(self):
        for counts in ({}, {"nomystery": [19, 4, 6, 9, 10], "tpp": [1, 0, 0, 1, 1]}):
            with self.subTest(counts=sorted(counts)), self.assertRaises(SystemExit):
                update_table(TABLE, "IPC Resources", "sat", counts)

    def test_the_summary_takes_one_track_s_totals(self):
        tex = update_summary(SUMMARY, "IPC Resources", "opt", [373, 120, 125, 209, 132])

        self.assertIn(r"Optimal & 373 & 120 & \textbf{125} & \textbf{209} & 132 \\", tex)
        self.assertIn(r"Satisficing & 330 & 88 & \textbf{92} & \textbf{305} & 122 \\", tex)

    def test_an_htg_problem_is_counted_under_the_domain_the_paper_names(self):
        names = {
            "gnad-et-al-aaai19-large-instances/agricola-large": "agricola",
            "organic-synthesis-MIT": "organic-synthesis",
            "childsnack-contents/parsize1-cham3": "childsnack",
        }
        for domain, name in names.items():
            with self.subTest(domain=domain):
                self.assertEqual(_htg_name(domain), name)


if __name__ == "__main__":
    unittest.main()
