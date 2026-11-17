import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from experiments.run import _planner_command
from experiments.tracks import TRACKS
from scripts import planner
from scripts.utils.arguments import abstract_planning_config, planning_config
from core.pipeline.abstraction.collapse import AbstractionError
from core.utilities.metrics import COUNTER_LABELS, DURATION_LABELS
from core.utilities.outcomes import STATUS_BY_EXIT_CODE, UnsolvableTaskError
from core.utilities.plan import PlanAction
from experiments.collect import _values


class PlannerOutputTests(unittest.TestCase):
    def test_every_metric_the_planner_prints_is_collected(self):
        """The collector reads the printed metrics, so the two must agree on the format."""
        metrics = {
            "durations": {name: 0.25 for name in DURATION_LABELS},
            "counters": {name: 3 for name in COUNTER_LABELS},
            "abstraction": {"objects": ["a", "b"], "object_type": "item"},
        }
        output = StringIO()
        with redirect_stdout(output):
            planner.print_planning_result({"plan": (PlanAction("move", (), 1),), "success": True, "metrics": metrics})

        values = _values({"status": "success", "wall_time_seconds": 1.0, "output": output.getvalue()})

        for name in DURATION_LABELS:
            self.assertEqual(values[f"{name}_seconds"], 0.25, name)
        for name in COUNTER_LABELS:
            self.assertEqual(values[name], 3, name)


class PlannerExitStatusTests(unittest.TestCase):
    """The exit codes are the benchmark runner's status source, so they are a contract."""

    def _main(self, argv):
        with patch.object(sys, "argv", ["planner", *argv]):
            return planner.main()

    def test_a_detected_unsolvable_task_exits_without_a_traceback(self):
        output = StringIO()
        with patch.object(planner, "_compute", side_effect=UnsolvableTaskError("task is unsolvable")):
            with redirect_stdout(output):
                status = self._main(["asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(status, 1)

    def test_a_crash_is_an_error_rather_than_a_task_without_a_plan(self):
        output = StringIO()
        with patch.object(planner, "_compute", side_effect=KeyError("plan")):
            with redirect_stdout(output):
                status = self._main(["asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(STATUS_BY_EXIT_CODE[status], "error")

    def test_an_abstraction_error_exits_through_the_parser(self):
        errors = StringIO()
        with patch.object(planner, "_compute", side_effect=AbstractionError("no abstractable object classes")):
            with redirect_stderr(errors), self.assertRaises(SystemExit) as raised:
                self._main(["abs-asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(raised.exception.code, 2)


class PlannerArgumentTests(unittest.TestCase):
    """What each mode's arguments ask of the pipeline."""

    PROBLEM = "experiments/benchmarks/downward-benchmarks/driverlog/p07.pddl"

    def _config(self, *argv):
        args = planner._argument_parser().parse_args([*argv, "--problem", self.PROBLEM])
        if args.mode.startswith("abs-"):
            return abstract_planning_config(args)
        return planning_config(args)

    def test_the_abstraction_arguments_reach_the_config(self):
        config = self._config("abs-lama", "--objects-to-abstract", "a", "b", "--abstraction-source", "resources")

        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual(config.abstraction_source, "resources")

    def test_the_domain_defaults_to_the_one_beside_the_problem(self):
        self.assertEqual(Path(self._config("asp").domain_path), Path(self.PROBLEM).parent / "domain.pddl")

    def test_only_the_optimal_modes_optimize(self):
        optimizing = {
            ("asp",): False,
            ("asp", "--optimize"): True,
            ("abs-asp",): False,
            ("abs-asp", "--optimize"): True,
            ("abs-lama",): False,
            ("abs-lmcut",): True,
        }
        for argv, optimize in optimizing.items():
            with self.subTest(argv=argv):
                self.assertEqual(self._config(*argv).optimize, optimize)

    def test_the_optimal_tracks_run_every_mode_optimally(self):
        for track in ("opt/symmetries", "opt/resources", "opt-htg/symmetries"):
            for mode in TRACKS[track].modes:
                if mode == "lmcut":
                    continue
                with self.subTest(track=track, mode=mode):
                    argv = _planner_command(Path("domain.pddl"), Path(self.PROBLEM), mode, track, 0)[3:]
                    args = planner._argument_parser().parse_args(argv)
                    config = abstract_planning_config(args) if mode.startswith("abs-") else planning_config(args)

                    self.assertTrue(config.optimize)


if __name__ == "__main__":
    unittest.main()
