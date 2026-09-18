import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.clingo import IncrementalSolver, parse_plan_actions, solve
from core.integrations.fast_downward import find_plan, has_plan, pddl_to_sas
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.outcomes import IntegrationError, OutOfMemoryError
from core.plan import PlanAction


class ClingoIntegrationTests(unittest.TestCase):
    @patch("core.integrations.clingo.clingo.Control")
    def test_control_always_uses_one_thread(self, control):
        IncrementalSolver("", horizon=3)

        # Single-threaded solving keeps benchmark runs reproducible.
        arguments = control.call_args.args[0]
        self.assertEqual(arguments[arguments.index("-t") + 1], "1")

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

    def test_control_is_grounded_through_the_requested_horizon(self):
        program = """
#program base.
step(0).
#show step/1.
#program step(t).
step(t).
"""
        plan = IncrementalSolver(program, horizon=3).solve()

        self.assertEqual(set(plan), {"step(0)", "step(1)", "step(2)", "step(3)"})

    def test_unsatisfiable_program_has_no_plan(self):
        plan = IncrementalSolver(":-.\n", horizon=0).solve()

        self.assertIsNone(plan)

    def test_incremental_search_returns_the_first_satisfiable_horizon(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 2.
"""

        result = solve(program)

        self.assertEqual(result.horizon, 2)
        self.assertEqual(result.attempts, 3)
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)"})

    def test_incremental_search_checks_horizon_zero(self):
        program = """
#program base.
ready.
#show ready/0.
#program check(t).
#external query(t).
:- query(t), not ready.
"""

        result = solve(program)

        self.assertEqual(result.plan, ["ready"])
        self.assertEqual(result.horizon, 0)
        self.assertEqual(result.attempts, 1)

    def test_incremental_search_can_start_above_zero_and_report_attempts(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 3.
"""
        attempts = []

        result = solve(program, start_horizon=2, on_attempt=lambda horizon, calls: attempts.append((horizon, calls)))

        self.assertEqual(result.horizon, 3)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(attempts, [(2, 1), (3, 2)])
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)", "reached(3)"})

    def test_extending_raises_the_horizon_on_the_same_control(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 2.
"""
        solver = IncrementalSolver(program, horizon=1)
        control = solver.control

        self.assertIsNone(solver.solve())

        solver.extend()

        self.assertIs(solver.control, control)
        self.assertEqual(solver.horizon, 2)
        self.assertEqual(set(solver.solve()), {"reached(0)", "reached(1)", "reached(2)"})


class FastDownwardHelperTests(unittest.TestCase):
    @patch("core.integrations.fast_downward.subprocess.run")
    def test_fast_downward_runs_under_the_active_interpreter(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="", stderr="")

        with tempfile.TemporaryDirectory() as directory:
            pddl_to_sas(directory, "domain.pddl", "problem.pddl", "concrete")

        self.assertEqual(run.call_args.args[0][0], sys.executable)

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_pddl_to_sas_surfaces_external_tool_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=20, stdout="translator output", stderr="search failed"
        )

        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "source-domain.pddl")
            problem = Path(directory, "source-problem.pddl")
            with self.assertRaisesRegex(RuntimeError, "translator output"):
                pddl_to_sas(directory, domain, problem, "concrete")

            command = run.call_args.args[0]
            self.assertIn(str(domain), command)
            self.assertIn(str(problem), command)
            self.assertFalse(Path(directory, "domain.pddl").exists())
            self.assertFalse(Path(directory, "problem.pddl").exists())

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_the_search_keeps_its_files_inside_the_run_directory(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="", stderr="")

        with tempfile.TemporaryDirectory() as directory:
            has_plan(directory, "domain.pddl", "problem.pddl", "concrete")

            command = run.call_args.args[0]
            written = [command[i + 1] for i, part in enumerate(command) if part in ("--sas-file", "--plan-file")]

        self.assertEqual(len(written), 2)
        for path in written:
            self.assertTrue(path.startswith(directory), f"{path} escapes the run directory")

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_the_baseline_reads_the_actions_of_the_plan_it_wrote(self, run):
        def write_plan(command, **_):
            plan_path = command[command.index("--plan-file") + 1]
            Path(plan_path).write_text("(walk a b)\n(drive b c)\n; cost = 2 (unit cost)\n", encoding="utf-8")
            return subprocess.CompletedProcess(args=command, returncode=0, stdout="", stderr="")

        run.side_effect = write_plan

        with tempfile.TemporaryDirectory() as directory:
            plan = find_plan(directory, "domain.pddl", "problem.pddl", "lama")

        # The trailing cost comment is not an action.
        self.assertEqual(plan, ["(walk a b)", "(drive b c)"])

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_a_goal_that_already_holds_is_solved_rather_than_unsolvable(self, run):
        def write_plan(command, **_):
            plan_path = command[command.index("--plan-file") + 1]
            Path(plan_path).write_text("; cost = 0 (unit cost)\n", encoding="utf-8")
            return subprocess.CompletedProcess(args=command, returncode=0, stdout="", stderr="")

        run.side_effect = write_plan

        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(find_plan(directory, "domain.pddl", "problem.pddl", "lama"), [])

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_the_baseline_reports_no_plan_when_the_task_is_unsolvable(self, run):
        with tempfile.TemporaryDirectory() as directory:
            for exit_code in (10, 11):
                run.return_value = subprocess.CompletedProcess(args=[], returncode=exit_code, stdout="", stderr="")
                self.assertIsNone(find_plan(directory, "domain.pddl", "problem.pddl", "lama"))

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_the_baseline_keeps_its_files_inside_the_run_directory(self, run):
        run.side_effect = lambda command, **_: subprocess.CompletedProcess(
            args=command, returncode=10, stdout="", stderr=""
        )

        with tempfile.TemporaryDirectory() as directory:
            find_plan(directory, "domain.pddl", "problem.pddl", "lama")

            command = run.call_args.args[0]
            written = [command[i + 1] for i, part in enumerate(command) if part in ("--sas-file", "--plan-file")]

        self.assertEqual(len(written), 2)
        for path in written:
            self.assertTrue(path.startswith(directory), f"{path} escapes the run directory")

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_a_search_killed_for_memory_is_told_apart_from_other_failures(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=247, stdout="search exit code: -9", stderr=""
        )

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(OutOfMemoryError):
                has_plan(directory, "domain.pddl", "problem.pddl", "abstract")

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_both_unsolvable_exit_codes_mean_no_plan(self, run):
        for returncode in (10, 11):
            with self.subTest(returncode=returncode):
                run.return_value = subprocess.CompletedProcess(args=[], returncode=returncode, stdout="", stderr="")

                with tempfile.TemporaryDirectory() as directory:
                    self.assertFalse(has_plan(directory, "domain.pddl", "problem.pddl", "concrete"))


class PlaspPostProcessingTests(unittest.TestCase):
    @patch("core.integrations.plasp.subprocess.run")
    def test_program_combines_exact_encoding_with_translator_output(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="translated.\n", stderr="")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "plasp"
            sas = root / "output.sas"
            exact = root / "exact.lp"
            actions = root / "actions.lp"
            for path in (binary, sas):
                path.touch()
            exact.write_text("exact.\n", encoding="utf-8")
            actions.write_text("actions.\n", encoding="utf-8")

            with (
                patch("core.integrations.plasp.PLASP_BIN", str(binary)),
                patch("core.integrations.plasp.EXACT_HORIZON_ENCODING", str(exact)),
                patch("core.integrations.plasp.ACTION_PER_TIME_STEP_ENCODING", str(actions)),
            ):
                program = sas_to_asp(str(sas))

            self.assertEqual(program, "exact.\nactions.\ntranslated.\n")

    def test_switch_guard_is_added_to_exact_occurrence_rule(self):
        rule = "1 {occurs(Action, t) : action(Action)} 1."

        result = add_switch_to_asp_rule(f"before.\n{rule}\nafter.\n")

        self.assertIn("not switch(t), not gap(t).", result)
        self.assertIn("0 {occurs(Action, t) : action(Action)} 1 :- gap(t).", result)
        self.assertNotIn(rule, result)
        self.assertEqual(result.count("not switch(t)"), 1)
        self.assertIn("before.\n", result)
        self.assertIn("after.\n", result)

    def test_switch_guard_rejects_an_encoding_without_the_occurrence_rule(self):
        with self.assertRaisesRegex(IntegrationError, "No occurrence rule"):
            add_switch_to_asp_rule("before.\nafter.\n")


if __name__ == "__main__":
    unittest.main()
