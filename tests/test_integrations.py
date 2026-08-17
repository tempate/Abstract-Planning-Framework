import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from core.integrations.clingo import collect_plan, create_control
from core.integrations.fast_downward import _get_command, _run_task, calc_horizon
from core.integrations.plasp import add_switch_to_asp_rule, append_pddl_facts_to_asp


class ClingoIntegrationTests(unittest.TestCase):
    def test_control_receives_the_requested_horizon(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "horizon.lp")
            path.write_text("step(1..horizon).\n#show step/1.\n", encoding="utf-8")

            plan = collect_plan(create_control([str(path)], horizon=3))

        self.assertEqual(set(plan), {"step(1)", "step(2)", "step(3)"})

    def test_unsatisfiable_program_has_no_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "unsat.lp")
            path.write_text(":-.\n", encoding="utf-8")

            plan = collect_plan(create_control([str(path)], horizon=0))

        self.assertIsNone(plan)


class FastDownwardHelperTests(unittest.TestCase):
    def test_calc_horizon_counts_only_actions(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "sas_plan")
            path.write_text("; cost = 2\n\n(move a b)\n  ; planner note\n(load p t l)\n", encoding="utf-8")

            self.assertEqual(calc_horizon(path), 2)

    def test_plan_command_uses_the_active_python_interpreter(self):
        paths = {"domain": "domain.pddl", "problem": "problem.pddl", "sas": "output.sas", "plan": "sas_plan"}

        command = _get_command(paths, "plan")

        self.assertEqual(command[0], sys.executable)
        self.assertIn("--plan-file", command)
        self.assertIn("astar(lmcut())", command)

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_run_task_surfaces_external_tool_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=20, stdout="translator output", stderr="search failed"
        )

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, "translator output"):
                _run_task("concrete", directory, b"domain", b"problem", "translate", Mock())

    @patch("core.integrations.fast_downward.subprocess.run")
    def test_run_task_classifies_unsolvable_problems(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=11, stdout="", stderr="")

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, "problem is unsolvable"):
                _run_task("abstract", directory, b"domain", b"problem", "translate", Mock())


class PlaspPostProcessingTests(unittest.TestCase):
    def test_append_pddl_facts_converts_supported_fuel_relations(self):
        pddl = """
(connected l0 l1)
(fuelcost level2 l0 l1)
(sum level0 level2 level2)
"""
        with tempfile.TemporaryDirectory() as directory:
            pddl_path = Path(directory, "problem.pddl")
            asp_path = Path(directory, "problem.lp")
            pddl_path.write_text(pddl, encoding="utf-8")
            asp_path.write_text("base.\n", encoding="utf-8")

            append_pddl_facts_to_asp(pddl_path, asp_path)
            result = asp_path.read_text(encoding="utf-8")

        self.assertIn('fuelcost("level2","l0","l1").', result)
        self.assertIn('sum("level0","level2","level2").', result)
        self.assertNotIn("connected", result)

    def test_switch_guard_is_added_for_both_horizon_encodings(self):
        rules = {
            "exact": "1 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0.",
            "bounded": "0 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0.",
        }

        for encoding, rule in rules.items():
            with self.subTest(encoding=encoding):
                with tempfile.TemporaryDirectory() as directory:
                    path = Path(directory, "problem.lp")
                    path.write_text(f"before.\n{rule}\nafter.\n", encoding="utf-8")

                    add_switch_to_asp_rule(path, encoding)
                    result = path.read_text(encoding="utf-8")

                self.assertIn("time(T), not switch(T), T > 0.", result)
                self.assertIn("before.\n", result)
                self.assertIn("after.\n", result)


if __name__ == "__main__":
    unittest.main()
