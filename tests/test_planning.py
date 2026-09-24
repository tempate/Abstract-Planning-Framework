import argparse
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.abstraction.factory import Abstraction, build_abstract_problem
from core.integrations.unified_planning import read_problem
from core.outcomes import UnsolvableTaskError
from core.abstraction.factory import write_abstract_problem
from core.metrics import PlanningMetrics
from core.planning import abstraction, fd
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from scripts.utils.arguments import positive_int


def _generated_abstraction():
    return SimpleNamespace(
        problem=Mock(),
        abstraction=Abstraction("item_abs", ("a", "b"), "item"),
        relaxed_deletes=(),
        relaxed_inequalities=(),
        statistics={"counters": {}, "ratios": {}},
    )


class BaselinePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.fd.find_plan")
    def test_the_plan_length_is_reported_rather_than_counted_from_the_output(self, find_plan):
        find_plan.return_value = ["(walk a b)", "(drive b c)"]
        config = PlanningConfig("domain.pddl", "problem.pddl")

        result = fd.solve(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["configuration"], config.as_dict())
        # The plan carries no occurs/2 atoms for the collector to count.
        self.assertEqual(result["metrics"]["counters"]["plan_length"], 2)

    @patch("core.planning.fd.find_sas_plan", return_value=None)
    def test_an_abstract_task_without_a_plan_proves_the_concrete_one_unsolvable(self, _find_sas_plan):
        with self.assertRaises(UnsolvableTaskError):
            fd.find_abstract_plan("run-dir", "abstract.sas", PlanningMetrics())

    @patch("core.planning.fd.find_plan")
    def test_an_unsolvable_task_is_not_a_plan(self, find_plan):
        find_plan.return_value = None

        result = fd.solve(PlanningConfig("domain.pddl", "problem.pddl"))

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertNotIn("plan_length", result["metrics"]["counters"])


@contextmanager
def _stubbed_decision(found):
    """Run the abstract decision pipeline against stubbed integrations."""
    with (
        patch("core.planning.abstraction.temp_run_dir") as temp_run_dir,
        patch(
            "core.planning.abstraction.build_abstract_problem", return_value=_generated_abstraction()
        ) as build_abstract_problem,
        patch("core.planning.abstraction.write_abstract_problem", return_value=("domain.pddl", "problem.pddl")),
        patch("core.planning.abstraction.has_plan", return_value=found),
    ):
        temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
        yield SimpleNamespace(build_abstract_problem=build_abstract_problem)


class DecisionTests(unittest.TestCase):
    @patch("core.planning.fd.has_plan")
    def test_searching_the_task_itself_settles_it(self, has_plan):
        for found, verdict in ((True, "solvable"), (False, "unsolvable")):
            with self.subTest(found=found):
                has_plan.return_value = found

                result = fd.check_solvability(PlanningConfig("domain.pddl", "problem.pddl"))

                self.assertEqual(result["verdict"], verdict)

    def test_an_abstract_plan_settles_nothing(self):
        with _stubbed_decision(found=True):
            result = abstraction.check_solvability(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unknown")

    def test_an_abstraction_with_no_plan_proves_the_task_unsolvable(self):
        with _stubbed_decision(found=False):
            result = abstraction.check_solvability(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unsolvable")

    def test_an_integration_proving_the_task_unsolvable_settles_it(self):
        with _stubbed_decision(found=True) as stubs:
            stubs.build_abstract_problem.side_effect = UnsolvableTaskError("no relaxed solution")

            result = abstraction.check_solvability(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unsolvable")


class PlanningConfigurationTests(unittest.TestCase):
    def test_selected_objects_are_stored_immutably(self):
        objects_to_abstract = ["hangar1", "hangar2"]
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", objects_to_abstract=objects_to_abstract)
        objects_to_abstract.append("hangar3")

        self.assertEqual(config.objects_to_abstract, ("hangar1", "hangar2"))


class GeneratedAbstractionTests(unittest.TestCase):
    def test_explicit_objects_create_temporary_planner_inputs(self):
        domain_text = "(define (domain d) (:types item) (:predicates (ready ?x - item)))"
        problem_text = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init (ready a) (ready b)) (:goal (and)))
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            domain = root / "domain.pddl"
            problem = root / "problem.pddl"
            domain.write_text(domain_text, encoding="utf-8")
            problem.write_text(problem_text, encoding="utf-8")
            config = AbstractPlanningConfig(domain, problem, objects_to_abstract=["a", "b"], abstract_name="combined")

            abstract_problem = build_abstract_problem(config)
            abstract_domain, abstract_problem_path = write_abstract_problem(abstract_problem.problem, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})


class ArgumentTests(unittest.TestCase):
    def test_positive_integer_rejects_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_int("0")


if __name__ == "__main__":
    unittest.main()
