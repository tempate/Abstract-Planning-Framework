import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from experiments import grounding


class GroundingTests(unittest.TestCase):
    def test_a_driver_crash_on_a_memory_error_counts_as_out_of_memory(self):
        directory = Path(tempfile.mkdtemp())
        (directory / "domain.pddl").touch()
        crash = subprocess.CompletedProcess([], 1, stdout="", stderr='if "MemoryError" not in line:\nTypeError')

        with patch.object(grounding.subprocess, "run", return_value=crash):
            outcome = grounding._ground(directory, "p01.pddl")

        self.assertEqual(outcome, "out of memory")

    def test_only_problems_no_concrete_mode_solves_on_any_sibling_track_are_ground(self):
        directory = Path(tempfile.mkdtemp())
        rows = {
            "sat": "domain,problem,mode,class,status\nd,a.pddl,lama,,success\nd,b.pddl,abs-lama,0,success\n",
            "opt": "domain,problem,mode,class,status\nd,c.pddl,lmcut,,success\n",
        }
        tracks = []
        for name, csv_text in rows.items():
            (directory / name).mkdir()
            (directory / name / "results.csv").write_text(csv_text, encoding="utf-8")
            problems = frozenset(("d", f"{p}.pddl") for p in "abcd")
            tracks.append(SimpleNamespace(results_file=directory / name / "results.csv", runnable=lambda p=problems: p))

        with patch.object(grounding, "_siblings", return_value=tracks):
            unsolved = grounding._unsolved("sat-htg/symmetries")

        self.assertEqual(unsolved, {("d", "b.pddl"), ("d", "d.pddl")})


if __name__ == "__main__":
    unittest.main()
