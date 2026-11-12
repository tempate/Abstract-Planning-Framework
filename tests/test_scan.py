import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from experiments import scan, slurm


class ScanTests(unittest.TestCase):
    def test_a_later_submit_scans_the_problems_its_renumbered_tasks_hold(self):
        directory = Path(tempfile.mkdtemp())
        track = SimpleNamespace(benchmarks_dir="benchmarks", abstract_arguments=())

        def fake_scan(_benchmarks, domain_name, problem, *_):
            return f"{domain_name}/{problem}", f"[{problem}]"

        with (
            patch.object(scan, "_task_dir", return_value=directory),
            patch.object(scan, "_scan", side_effect=fake_scan),
        ):
            for problems in (["a/p1.pddl"], ["b/p2.pddl"]):
                (directory / "tasks.txt").write_text("".join(f"{p}\n" for p in problems), encoding="utf-8")
                scan._scan_task("sat-htg/symmetries", track, 0, "symmetries", 600)

            outcomes = slurm.outcomes(directory)

        self.assertEqual(outcomes, {"a/p1.pddl": "[p1.pddl]", "b/p2.pddl": "[p2.pddl]"})


if __name__ == "__main__":
    unittest.main()
