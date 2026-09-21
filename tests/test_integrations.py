import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.clingo import parse_plan_actions
from core.integrations.fast_downward import find_plan, has_plan, pddl_to_sas
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.outcomes import IntegrationError, OutOfMemoryError, UnsolvableTaskError
from core.plan import PlanAction


class ClingoPlanParsingTests(unittest.TestCase):
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

    def test_an_occurrence_the_parser_cannot_read_is_not_passed_over(self):
        # Dropping it would report a plan a step short of the one Clingo found.
        for atom in ('occurs(action(("load",1)),1)', "occurs(step,1)", 'occurs(action(("load","p0")),first)'):
            with self.subTest(atom=atom), self.assertRaises(IntegrationError):
                parse_plan_actions([atom])


class FastDownwardHelperTests(unittest.TestCase):
    @patch("core.integrations.fast_downward.subprocess.run")
    def test_fast_downward_runs_under_the_active_interpreter(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="", stderr="")

        with tempfile.TemporaryDirectory() as directory:
            pddl_to_sas(directory, "domain.pddl", "problem.pddl", "concrete")

        self.assertEqual(run.call_args.args[0][0], sys.executable)

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_a_translator_that_proved_the_task_unsolvable_stops_the_search(self, run):
        # It says so on stdout and still exits 0, leaving a dummy task the
        # horizon search would raise forever on.
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="No relaxed solution! Generating unsolvable task...", stderr=""
        )

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(UnsolvableTaskError):
                pddl_to_sas(directory, "domain.pddl", "problem.pddl", "concrete")

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
