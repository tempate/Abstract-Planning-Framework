import unittest

from experiments.figure import htg_domain
from experiments.paper import update_htg_table, update_summary, update_table

TABLE = r"""\begin{table*}
\multicolumn{11}{l}{\emph{IPC Resources}} \\
nomystery & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
thoughtful & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\bottomrule
\label{tab:ipc-domains}
\end{table*}
"""
SUMMARY = r"""\begin{table}
\begin{tabular}{lrrrrr}
 & \# & \ASP & \ASPa & \textsc{FD} & \textsc{FD}\textsuperscript{$\alpha$} \\
\multicolumn{6}{l}{\emph{Resources}} \\
Satisficing & 1 & 1 & 1 & 1 & 1 \\
Optimal & 1 & 1 & 1 & 1 & 1 \\
\bottomrule
\end{tabular}
\label{tab:ipc-summary}
\end{table}
"""
HTG = r"""\begin{table*}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lrrrrrrrrrrrrrr}
 & \multicolumn{7}{c}{Satisficing} & \multicolumn{7}{c}{Optimal} \\
Domain & \# & \ASP & \ASPa & \textsc{FD} & \textsc{FD}\textsuperscript{$\alpha$} & \PL & \PLa & \# & \ASP & \ASPa & \textsc{FD} & \textsc{FD}\textsuperscript{$\alpha$} & \PL & \PLa \\
blocksworld & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
rovers & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
Total & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{tabular*}
\label{tab:htg}
\end{table*}
"""


class PaperTableTests(unittest.TestCase):
    def test_a_domain_row_pairs_each_planner_with_its_abstraction_on_both_tracks(self):
        counts = {
            "sat": {"nomystery": [19, 4, 6, 12, 10, None, None], "thoughtful": [20, 5, 5, 15, 5, None, None]},
            "opt": {"nomystery": [19, 0, 0, 0, 0, None, None]},
        }
        tex, changed = update_table(TABLE, "IPC Resources", counts)

        # Powerlifted, which IPC does not run, gets no column, ties bold both, and a pair that solves nothing bolds nothing.
        self.assertIn(r"nomystery & 19 & 4 & \textbf{6} & \textbf{12} & 10 & 19 & 0 & 0 & 0 & 0 \\", tex)
        # A domain only one track has reads -- on the other.
        self.assertIn(r"thoughtful & 20 & \textbf{5} & \textbf{5} & \textbf{15} & 5 & -- & -- & -- & -- & -- \\", tex)
        self.assertEqual(changed, ["nomystery", "thoughtful"])

    def test_a_row_the_results_lack_or_a_domain_the_paper_lacks_stops_the_update(self):
        row = [1, 0, 0, 1, 1, None, None]
        for sat in ({"nomystery": row}, {"nomystery": row, "thoughtful": row, "tpp": row}):
            with self.subTest(domains=sorted(sat)), self.assertRaises(SystemExit):
                update_table(TABLE, "IPC Resources", {"sat": sat, "opt": {}})

    def test_the_summary_gives_each_track_a_row_and_bolds_the_better_of_each_pair(self):
        # Each track holds the problems, then each planner and its abstraction: ASP, FD and PL, which IPC never runs.
        tracks = {"sat": [330, 88, 92, 305, 122, None, None], "opt": [363, 122, 120, 207, 132, None, None]}
        tex = update_summary(SUMMARY, "tab:ipc-summary", {"Resources": tracks})

        self.assertIn(r"Satisficing & 330 & 88 & \textbf{92} & \textbf{305} & 122 \\", tex)
        self.assertIn(r"Optimal & 363 & \textbf{122} & 120 & \textbf{207} & 132 \\", tex)

    def test_a_track_the_summary_lacks_or_the_results_lack_stops_the_update(self):
        tracks = {"sat": [1] * 5 + [None] * 2, "opt": [1] * 5 + [None] * 2}
        for summary, results in (
            (SUMMARY.replace("Optimal & 1 & 1 & 1 & 1 & 1 \\\\\n", ""), tracks),
            (SUMMARY, {"sat": tracks["sat"]}),
        ):
            with self.subTest(results=sorted(results)), self.assertRaises(SystemExit):
                update_summary(summary, "tab:ipc-summary", {"Resources": results})

    def test_the_htg_table_gives_each_domain_and_the_total_a_row_with_a_block_per_track(self):
        counts = {
            "sat": {"blocksworld": [40, 11, 19, 12, 40, 20, 40], "rovers": [35, 8, 6, 10, 10, 35, 18]},
            "opt": {"blocksworld": [40, 11, 20, 12, 40, 0, 40], "rovers": [10, 4, 3, 3, 3, 1, 1]},
        }
        tex = update_htg_table(HTG, counts)

        # Each planner and its abstraction form a pair, and ties bold both.
        sat = r"35 & \textbf{8} & 6 & \textbf{10} & \textbf{10} & \textbf{35} & 18"
        opt = r"10 & \textbf{4} & 3 & \textbf{3} & \textbf{3} & \textbf{1} & \textbf{1}"
        self.assertIn(rf"rovers & {sat} & {opt} \\", tex)
        self.assertIn(r"Total & 75 & 19 & \textbf{25} & 22 & \textbf{50} & 55 & \textbf{58} & 50 &", tex)

    def test_an_htg_domain_one_side_lacks_stops_the_update(self):
        row = [1, 0, 0, 0, 0, 0, 0]
        both = {"sat": {"blocksworld": row, "rovers": row}, "opt": {"blocksworld": row, "rovers": row}}
        cases = {
            "the paper": (HTG.replace("rovers &", "tpp &"), both),
            "the results": (HTG, {"sat": {"blocksworld": row}, "opt": {"blocksworld": row}}),
            "one track": (HTG, {"sat": both["sat"], "opt": {"blocksworld": row}}),
        }
        for lacking, (paper, counts) in cases.items():
            with self.subTest(lacking=lacking), self.assertRaises(SystemExit):
                update_htg_table(paper, counts)

    def test_an_htg_problem_is_counted_under_the_domain_the_paper_names(self):
        names = {
            "gnad-et-al-aaai19-large-instances/agricola-large": "agricola",
            "organic-synthesis-MIT": "organic-synthesis",
            "childsnack-contents/parsize1-cham3": "childsnack",
        }
        for domain, name in names.items():
            with self.subTest(domain=domain):
                self.assertEqual(htg_domain(domain), name)


if __name__ == "__main__":
    unittest.main()
