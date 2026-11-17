import contextlib
import csv
import io
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import experiments.report
from experiments.collect import FIELDS
from experiments.report import (
    PLAN_COMPARISON,
    _by_domain,
    _finished_problems,
    _head_to_head,
    MODE_LABELS,
    _pairs,
    best_classes,
)


class ReportTests(unittest.TestCase):
    def test_a_missing_result_ranks_below_a_finished_class(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            fields = "domain,problem,mode,class,status,wall_time_seconds,last_completed_phase"
            rows = ["d,p01.pddl,abs-asp,0,timed out,1800,", "d,p01.pddl,abs-asp,1,missing,,"]
            results.write_text("\n".join([fields, *rows]) + "\n")

            self.assertEqual(best_classes(results), {("d", "p01.pddl", "abs-asp"): 0})

    def test_the_report_writes_its_files_beside_the_results(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                for mode, rank, seconds in (("asp", "", "5"), ("abs-asp", "0", "90"), ("abs-asp", "1", "40")):
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": "p01.pddl", "mode": mode, "class": rank}
                        | {"status": "success", "wall_time_seconds": seconds, "switches_off": "0", "increments": "0"}
                    )

            with patch("sys.argv", ["report", str(results)]), contextlib.redirect_stdout(io.StringIO()):
                experiments.report.main()

            self.assertTrue((Path(directory) / "report.md").is_file())
            with (Path(directory) / "best_classes.csv").open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
        self.assertEqual(rows, [{"domain": "example", "problem": "p01.pddl", "mode": "abs-asp", "class": "1"}])

    def test_the_report_survives_a_run_with_no_shared_solves(self):
        problems = [
            {
                "abs-asp": {"status": "timed out", "wall_time_seconds": "1800.0"},
                "asp": {"status": "success", "wall_time_seconds": "12.0"},
            }
        ]

        _title, lines = _head_to_head(problems, [("abs-asp", "asp")], PLAN_COMPARISON, MODE_LABELS)

        median = next(line for line in lines if line.startswith("Median runtime"))
        self.assertNotIn(" s", median)

    def test_the_domains_are_alphabetical_and_their_subdirectories_increase(self):
        names = ["rovers/goal-10", "blocksworld/goal-100", "rovers/goal-2", "blocksworld/goal-3"]
        problems = [{"lama": {"domain": name, "problem": "p01.pddl", "status": "success"}} for name in names]

        _title, lines = _by_domain(problems, ("lama",), MODE_LABELS)

        subdirectories = [line.split()[-2] for line in lines[2:-1]]
        self.assertEqual(subdirectories, ["goal-3", "goal-100", "goal-2", "goal-10"])
        self.assertEqual([line.split()[0] for line in lines[2:-1] if "(" in line], ["blocksworld", "rovers"])

    def test_each_abstraction_is_compared_against_its_solver_alone(self):
        """Intersecting every mode would drop the problems one solver missed out
        of the other pair's comparison, moving numbers for an unrelated reason."""
        success = {"status": "success", "wall_time_seconds": "1.0"}
        timeout = {"status": "timed out", "wall_time_seconds": "1800.0"}
        problems = [
            {"asp": success, "abs-asp": success, "abs-lama": success, "lama": success},
            {"asp": success, "abs-asp": success, "abs-lama": success, "lama": timeout},
        ]

        pairs = [("abs-asp", "asp"), ("abs-lama", "lama")]
        _title, lines = _head_to_head(problems, pairs, PLAN_COMPARISON, MODE_LABELS)

        shared = next(line for line in lines if line.startswith("Plans found by both"))
        self.assertEqual(re.findall(r"\d+", shared), ["2", "2", "1", "1"])

    def test_an_abstraction_is_compared_with_the_solver_of_its_abstract_task(self):
        self.assertEqual(_pairs(["abs-lmcut"], ("abs-lmcut", "lama", "lmcut")), [("abs-lmcut", "lmcut")])

    def test_the_head_to_head_compares_plan_lengths_on_shared_solves(self):
        def solved(length):
            return {"status": "success", "wall_time_seconds": "1.0", "plan_length": str(length)}

        problems = [
            {"abs-asp": solved(10), "asp": solved(8)},
            {"abs-asp": solved(8), "asp": solved(8)},
            {"abs-asp": solved(5), "asp": {"status": "timed out", "wall_time_seconds": "1800.0"}},
        ]

        _title, lines = _head_to_head(problems, [("abs-asp", "asp")], PLAN_COMPARISON, MODE_LABELS)

        shorter = next(line for line in lines if line.startswith("Shorter plan"))
        total = next(line for line in lines if line.startswith("Total plan length"))
        self.assertEqual(re.findall(r"(\d+) \(", shorter), ["1", "0"])
        self.assertEqual(re.findall(r"\d+", total.removeprefix("Total plan length")), ["16", "18"])

    def test_the_report_covers_the_modes_the_results_hold(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                rows = [("p01.pddl", "abs-asp"), ("p01.pddl", "asp"), ("p01.pddl", "lama")]
                # p02 never ran the baseline, so no mode can be compared on it.
                rows += [("p02.pddl", "abs-asp"), ("p02.pddl", "asp")]
                for problem, mode in rows:
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": problem, "mode": mode, "status": "success"}
                    )

            modes, problems, dropped = _finished_problems(results)

        self.assertEqual(set(modes), {"asp", "abs-asp", "lama"})
        self.assertEqual(len(problems), 1)
        self.assertEqual(dropped, 1)

    def test_an_abstract_mode_reports_its_best_class(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                # The largest class times out, a smaller one solves, the smallest solves slower.
                runs = [("asp", "", "success", "5"), ("abs-asp", "0", "timed out", "1800")]
                runs += [("abs-asp", "1", "success", "40"), ("abs-asp", "2", "success", "90")]
                for mode, rank, status, seconds in runs:
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": "p01.pddl", "mode": mode, "class": rank}
                        | {"status": status, "wall_time_seconds": seconds}
                    )

            _modes, problems, _dropped = _finished_problems(results)

        self.assertEqual(problems[0]["abs-asp"]["class"], "1")

    def test_a_class_that_completed_no_phase_got_least_far(self):
        crashed = {"status": "error (exit code 2)", "wall_time_seconds": "1", "last_completed_phase": ""}
        refining = {"status": "timed out", "wall_time_seconds": "1800", "last_completed_phase": "concrete_asp"}

        self.assertLess(experiments.report._performance(crashed), experiments.report._performance(refining))

    def test_an_abstract_mode_no_class_solves_reports_the_class_that_got_furthest(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                # The largest class dies in the abstract search, a smaller one while refining.
                runs = [("asp", "", "concrete_asp"), ("abs-asp", "0", "abstract_asp")]
                runs += [("abs-asp", "1", "concrete_asp")]
                for mode, rank, phase in runs:
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": "p01.pddl", "mode": mode, "class": rank}
                        | {"status": "timed out", "wall_time_seconds": "1800", "last_completed_phase": phase}
                    )

            _modes, problems, _dropped = _finished_problems(results)

        self.assertEqual(problems[0]["abs-asp"]["class"], "1")


if __name__ == "__main__":
    unittest.main()
