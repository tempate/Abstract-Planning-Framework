import unittest

from experiments.paper import _htg_name, update_summary, update_table

TABLE = r"""\begin{table*}
\multicolumn{8}{l}{\emph{IPC Resources}} \\
nomystery & 19 & 1 & 1 & 1 & 1 & 1 & 1 \\
mystery & 26 & 0 & 0 & 0 & 0 & 0 & 0 \\
\bottomrule
\label{tab:sat-domains}
\end{table*}
"""
SUMMARY = r"""\begin{table}
\begin{tabular}{lrr}
 & Sat & Opt \\
\midrule
Problems & 1 & 1 \\
\multicolumn{3}{l}{\emph{Baselines}} \\
\ASP & 1 & 1 \\
\textsc{FD} & 1 & 1 \\
\PL & 1 & 1 \\
\multicolumn{3}{l}{\emph{Our pipeline}} \\
\ASP & 1 & 1 \\
\textsc{FD} & 1 & 1 \\
\PL & 1 & 1 \\
\end{tabular}
\label{tab:summary}
\end{table}
"""


class PaperTableTests(unittest.TestCase):
    def test_a_domain_row_puts_the_baselines_first_and_bolds_its_most_solved(self):
        counts = {"nomystery": [19, 4, 6, 12, 10, None, None], "mystery": [26, 0, 0, 0, 0, None, None]}
        tex, changed = update_table(TABLE, "IPC Resources", "sat", counts)

        # A planner without results reads --, and a row nobody solves anything in bolds nothing.
        self.assertIn(r"nomystery & 19 & 4 & \textbf{12} & -- & 6 & 10 & -- \\", tex)
        self.assertIn(r"mystery & 26 & 0 & 0 & -- & 0 & 0 & -- \\", tex)
        self.assertEqual(changed, ["nomystery", "mystery"])

    def test_a_row_the_results_lack_or_a_domain_the_paper_lacks_stops_the_update(self):
        row = [1, 0, 0, 1, 1, None, None]
        for counts in ({"nomystery": row}, {"nomystery": row, "mystery": row, "tpp": row}):
            with self.subTest(counts=sorted(counts)), self.assertRaises(SystemExit):
                update_table(TABLE, "IPC Resources", "sat", counts)

    def test_the_summary_gives_each_track_a_column_and_bolds_its_most_solved(self):
        # Each column holds the problems, then each planner and its abstraction: ASP, FD and PL.
        tex = update_summary(SUMMARY, [[330, 88, 92, 305, 122, None, None], [363, 122, 120, 207, 132, 35, 86]])

        self.assertIn(r"Problems & 330 & 363 \\", tex)
        self.assertIn(
            "Baselines}} \\\\\n\\ASP & 88 & 122 \\\\\n\\textsc{FD} & \\textbf{305} & \\textbf{207} \\\\\n\\PL & -- & 35",
            tex,
        )
        self.assertIn("Our pipeline}} \\\\\n\\ASP & 92 & 120 \\\\\n\\textsc{FD} & 122 & 132 \\\\\n\\PL & -- & 86", tex)

    def test_a_summary_row_the_paper_lacks_stops_the_update(self):
        with self.assertRaises(SystemExit):
            update_summary(SUMMARY.replace("\\PL & 1 & 1 \\\\\n\\end", "\\end"), [[1] * 7, [1] * 7])

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
