import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.utilities.metrics import COUNTER_LABELS, DURATION_LABELS
from experiments.collect import FIELDS, _preserved_rows, _track_results_file, _values, collect
from experiments.submit import _write_manifest
from experiments.tracks import TRACKS


class CollectTests(unittest.TestCase):
    @staticmethod
    def _write_result(directory, mode, status="success"):
        result = {
            "domain": "example",
            "problem": "p01.pddl",
            "mode": mode,
            "status": status,
            "return_code": 0,
            "timed_out": False,
            "wall_time_seconds": 1.0,
            "output": "Plan found: yes\n",
        }
        path = Path(directory) / "example" / "p01" / f"{mode}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result), encoding="utf-8")

    def test_every_metric_the_planner_reports_is_collected(self):
        metrics = {
            "durations": {name: 0.25 for name in DURATION_LABELS},
            "counters": {name: 3 for name in COUNTER_LABELS},
            "abstraction": {"objects": ["a", "b"], "object_type": "item"},
        }
        result = {"status": "success", "wall_time_seconds": 1.0, "output": "", "progress": {"metrics": metrics}}

        values = _values(result)

        for name in DURATION_LABELS:
            self.assertEqual(values[f"{name}_seconds"], 0.25, name)
        for name in COUNTER_LABELS:
            self.assertEqual(values[name], 3, name)
        self.assertEqual((values["abstracted_object_count"], values["abstracted_object_type"]), (2, "item"))

    def test_every_mode_becomes_its_own_row(self):
        """A mode the collector does not know is filed as an abstract result and
        then dropped, silently, because the real abstract result sorts first."""
        with tempfile.TemporaryDirectory() as directory:
            for mode in ("abs-asp", "asp", "lama"):
                self._write_result(directory, mode)

            rows = collect(directory)

        self.assertEqual({row["mode"] for row in rows}, {"abs-asp", "asp", "lama"})

    def test_collector_ignores_copperbench_metadata_next_to_results(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory) / "run-1"
            run_dir.mkdir()
            (run_dir / "metadata.json").write_text('{"instances": {}, "configs": {}}\n', encoding="utf-8")

            self.assertEqual(collect(directory), [])

    def test_a_gap_filling_run_is_merged_with_the_one_it_completes(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            self._write_result(first, "asp")
            self._write_result(first, "abs-asp", status="timeout")
            _write_manifest([("abs-asp", "example", Path("d.pddl"), Path("p01.pddl"), None)], results_dir=first)
            self._write_result(second, "abs-asp")
            _write_manifest([("lama", "example", Path("d.pddl"), Path("p01.pddl"), None)], results_dir=second)

            rows = collect(first, second)

        by_mode = {row["mode"]: row for row in rows}
        self.assertEqual(set(by_mode), {"abs-asp", "asp", "lama"})
        # the later run owns the result both directories hold
        self.assertEqual(by_mode["abs-asp"]["status"], "success")
        # a mode only the second manifest expected is still accounted for
        self.assertEqual(by_mode["lama"]["status"], "missing")

    def test_the_manifest_marks_every_mode_that_produced_no_result(self):
        expected_statuses = {
            (): ["missing", "missing"],
            ("abs-asp",): ["success", "missing"],
            ("abs-asp", "asp"): ["success", "success"],
        }
        for completed, statuses in expected_statuses.items():
            with self.subTest(completed=completed), tempfile.TemporaryDirectory() as directory:
                problem = Path("p01.pddl")
                tasks = [
                    ("abs-asp", "example", Path("domain.pddl"), problem, None),
                    ("asp", "example", Path("domain.pddl"), problem, None),
                ]
                _write_manifest(tasks, directory)
                for mode in completed:
                    self._write_result(directory, mode)

                rows = collect(directory)

                self.assertEqual([row["mode"] for row in rows], ["abs-asp", "asp"])
                self.assertEqual([row["status"] for row in rows], statuses)

    def test_a_run_is_collected_into_the_results_of_its_track(self):
        task = [("asp", "example", Path("domain.pddl"), Path("p01.pddl"), None)]
        with tempfile.TemporaryDirectory() as sat, tempfile.TemporaryDirectory() as opt:
            _write_manifest(task, sat, track="sat/symmetries")
            _write_manifest(task, opt, track="opt/symmetries")

            self.assertEqual(_track_results_file([opt]), TRACKS["opt/symmetries"].results_file)
            with self.assertRaises(SystemExit):
                _track_results_file([sat, opt])


class CollectedCsvTests(unittest.TestCase):
    @staticmethod
    def _write_csv(directory, rows):
        path = Path(directory) / "results.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            for domain, problem, mode, status in rows:
                writer.writerow({"domain": domain, "problem": problem, "mode": mode, "status": status})
        return path

    @staticmethod
    def _collected(rows):
        collected = []
        for domain, problem, mode, status in rows:
            collected.append({"domain": domain, "problem": problem, "mode": mode, "status": status})
        return collected

    def test_a_collected_result_replaces_the_one_already_in_the_csv_unless_it_never_reported(self):
        rows = [("example", "p01.pddl", "asp", "success")]
        for status, kept in (("timed out", []), ("missing", ["success"])):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as directory:
                csv_file = self._write_csv(directory, rows)
                collected = self._collected([("example", "p01.pddl", "asp", status)])

                preserved = _preserved_rows(collected, csv_file)

                self.assertEqual([row["status"] for row in preserved], kept)

    def test_every_result_the_run_did_not_re_run_is_kept(self):
        """A baseline measured on its own, or a run filling one problem's gap,
        leaves the rest of the CSV as it was."""
        with tempfile.TemporaryDirectory() as directory:
            csv_file = self._write_csv(
                directory,
                [
                    ("example", "p01.pddl", "abs-asp", "success"),
                    ("example", "p02.pddl", "abs-asp", "timed out"),
                    ("example", "p01.pddl", "lama", "timed out"),
                ],
            )
            collected = self._collected([("example", "p02.pddl", "abs-asp", "success")])

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual(
            {(row["problem"], row["mode"]) for row in preserved}, {("p01.pddl", "abs-asp"), ("p01.pddl", "lama")}
        )

    def test_a_new_class_leaves_the_row_of_one_collected_before_classes(self):
        with tempfile.TemporaryDirectory() as directory:
            csv_file = self._write_csv(directory, [("example", "p01.pddl", "abs-asp", "success")])
            collected = self._collected([("example", "p01.pddl", "abs-asp", "timed out")])
            collected[0]["class"] = "item-2-0a1b2c"

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual([(row["mode"], row["class"]) for row in preserved], [("abs-asp", "")])

    def test_re_running_one_class_drops_the_classes_it_skipped(self):
        """A best-class run measures newer code, so the other classes' rows no longer describe it."""
        with tempfile.TemporaryDirectory() as directory:
            csv_file = Path(directory) / "results.csv"
            with csv_file.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                for problem, rank in (("p01.pddl", "0"), ("p01.pddl", "1"), ("p02.pddl", "1")):
                    writer.writerow({"domain": "example", "problem": problem, "mode": "abs-asp", "class": rank})
            collected = self._collected([("example", "p01.pddl", "abs-asp", "success")])
            collected[0]["class"] = "0"

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual([(row["problem"], row["class"]) for row in preserved], [("p02.pddl", "1")])

    def test_a_first_run_has_nothing_to_keep(self):
        with tempfile.TemporaryDirectory() as directory:
            preserved = _preserved_rows(self._collected([]), Path(directory) / "results.csv")

        self.assertEqual(preserved, [])


if __name__ == "__main__":
    unittest.main()
