import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from core.integrations.clingo import collect_plan, create_control, parse_plan_actions, run_clingo
from core.integrations.fast_downward import _get_command, _run_task
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.planning.outcomes import IntegrationError
from core.planning.plan import PlanAction


class ClingoIntegrationTests(unittest.TestCase):
    @patch("core.integrations.clingo.clingo.Control")
    def test_control_always_uses_one_thread(self, control):
        create_control("", horizon=3)

        control.assert_called_once_with(["-c", "horizon=3", "-t", "1", "--warn=none"])

    def test_parse_plan_actions_ignores_other_atoms_and_orders_actions(self):
        atoms = [
            'occurs(action(("unload","p0","t0","l1")),3)',
            "cost(4)",
            'occurs(action(("load","p0","t0","l0")),1)',
            'occurs(action("wait"),2)',
        ]

        self.assertEqual(
            parse_plan_actions(atoms),
            (
                PlanAction("load", ("p0", "t0", "l0"), 1),
                PlanAction("wait", (), 2),
                PlanAction("unload", ("p0", "t0", "l1"), 3),
            ),
        )

    def test_control_receives_the_requested_horizon(self):
        program = "step(1..horizon).\n#show step/1.\n"
        plan = collect_plan(create_control(program, horizon=3))

        self.assertEqual(set(plan), {"step(1)", "step(2)", "step(3)"})

    def test_unsatisfiable_program_has_no_plan(self):
        plan = collect_plan(create_control(":-.\n", horizon=0))

        self.assertIsNone(plan)

    def test_horizon_search_returns_the_first_satisfiable_horizon(self):
        program = """
#const horizon=0.
reached(0..horizon).
#show reached/1.
:- horizon < 2.
"""

        result = run_clingo(program, max_horizon=4)

        self.assertEqual(result.horizon, 2)
        self.assertEqual(result.attempts, 3)
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)"})

    def test_horizon_search_checks_horizon_zero(self):
        program = """
ready.
#show ready/0.
:- not ready.
"""

        result = run_clingo(program, max_horizon=4)

        self.assertEqual(result.plan, ["ready"])
        self.assertEqual(result.horizon, 0)
        self.assertEqual(result.attempts, 1)

    def test_horizon_search_honors_an_inclusive_maximum(self):
        program = """
#const horizon=0.
:- horizon < 2.
"""

        result = run_clingo(program, max_horizon=1)

        self.assertIsNone(result.plan)
        self.assertEqual(result.horizon, 1)
        self.assertEqual(result.attempts, 2)


class FastDownwardHelperTests(unittest.TestCase):
    def test_translation_command_uses_the_active_python_interpreter(self):
        paths = {"domain": "domain.pddl", "problem": "problem.pddl", "sas": "output.sas"}

        command = _get_command(paths)

        self.assertEqual(command[0], sys.executable)
        self.assertIn("--translate", command)
        self.assertNotIn("--plan-file", command)
        self.assertNotIn("--search", command)

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_run_task_surfaces_external_tool_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=20, stdout="translator output", stderr="search failed"
        )

        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "source-domain.pddl")
            problem = Path(directory, "source-problem.pddl")
            with self.assertRaisesRegex(RuntimeError, "translator output"):
                _run_task("concrete", directory, domain, problem, Mock())

            command = run.call_args.args[0]
            self.assertIn(str(domain), command)
            self.assertIn(str(problem), command)
            self.assertFalse(Path(directory, "domain.pddl").exists())
            self.assertFalse(Path(directory, "problem.pddl").exists())


class PlaspPostProcessingTests(unittest.TestCase):
    @patch("core.integrations.plasp.subprocess.run")
    def test_program_combines_selected_encodings_with_translator_output(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="translated.\n", stderr="")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "plasp"
            sas = root / "output.sas"
            bounded = root / "bounded.lp"
            actions = root / "actions.lp"
            for path in (binary, sas):
                path.touch()
            bounded.write_text("bounded.\n", encoding="utf-8")
            actions.write_text("actions.\n", encoding="utf-8")

            with (
                patch("core.integrations.plasp.PLASP_BIN", str(binary)),
                patch("core.integrations.plasp._HORIZON_ENCODINGS", {"bounded": str(bounded)}),
                patch("core.integrations.plasp.ACTION_PER_TIME_STEP_ENCODING", str(actions)),
            ):
                program = sas_to_asp(str(sas))

            self.assertEqual(program, "bounded.\nactions.\ntranslated.\n")

    def test_switch_guard_is_added_for_both_horizon_encodings(self):
        rules = {
            "exact": "1 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0.",
            "bounded": "0 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0.",
        }

        for encoding, rule in rules.items():
            with self.subTest(encoding=encoding):
                result = add_switch_to_asp_rule(f"before.\n{rule}\nafter.\n", encoding)

                self.assertIn("time(T), not switch(T), T > 0.", result)
                self.assertNotIn(rule, result)
                self.assertEqual(result.count("not switch(T)"), 1)
                self.assertIn("before.\n", result)
                self.assertIn("after.\n", result)

    def test_switch_guard_rejects_an_encoding_without_the_occurrence_rule(self):
        with self.assertRaisesRegex(IntegrationError, "No occurrence rule"):
            add_switch_to_asp_rule("before.\nafter.\n")


if __name__ == "__main__":
    unittest.main()
