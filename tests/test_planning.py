import argparse
import subprocess
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
from core.planning import abstraction, asp, fd
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from scripts.utils.arguments import positive_int


def _generated_abstraction():
    return SimpleNamespace(
        problem=Mock(),
        abstraction=Abstraction("item_abs", ("a", "b"), "item"),
        relaxed_deletes=(),
        relaxed_inequalities=(),
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
        patch("core.planning.abstraction.write_abstract_problem", return_value=("domain.pddl", "problem.pddl", {})),
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
            abstract_domain, abstract_problem_path, _ = write_abstract_problem(abstract_problem.problem, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})


class ArgumentTests(unittest.TestCase):
    def test_positive_integer_rejects_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_int("0")


# A counter that three actions advance from 0 to 3, in the facts plasp would emit.
COUNTER_TASK = """
#show occurs/2.
variable(variable(x)).
contains(variable(x), value(x, 0..3)).
initialState(variable(x), value(x, 0)).
goal(variable(x), value(x, 3)).
action(action(("advance", "s1"))). action(action(("advance", "s2"))). action(action(("advance", "s3"))).
precondition(action(("advance", "s1")), variable(x), value(x, 0)).
precondition(action(("advance", "s2")), variable(x), value(x, 1)).
precondition(action(("advance", "s3")), variable(x), value(x, 2)).
postcondition(action(("advance", "s1")), effect(unconditional), variable(x), value(x, 1)).
postcondition(action(("advance", "s2")), effect(unconditional), variable(x), value(x, 2)).
postcondition(action(("advance", "s3")), effect(unconditional), variable(x), value(x, 3)).
"""


class AspHorizonSearchTests(unittest.TestCase):
    def test_exponential_search_finds_a_plan_shorter_than_its_horizon_and_closes_the_empty_steps(self):
        plasp = subprocess.CompletedProcess([], 0, stdout=COUNTER_TASK, stderr="")

        def stop_past_the_plan(_event, metrics):
            # Without empty steps no horizon past 3 holds a plan, and the search would never end.
            if metrics["counters"].get("abstract_plan_length", 0) > 4:
                raise AssertionError("the search passed the first horizon holding the plan")

        with (
            patch("core.integrations.plasp.os.path.exists", return_value=True),
            patch("core.integrations.plasp.subprocess.run", return_value=plasp),
        ):
            actions, horizon = asp.find_abstract_plan(
                None, "abstract.sas", PlanningMetrics(on_update=stop_past_the_plan), True
            )

        self.assertEqual([action.args for action in actions], [("s1",), ("s2",), ("s3",)])
        self.assertEqual([action.time_step for action in actions], [1, 2, 3])
        self.assertEqual(horizon, 3)


if __name__ == "__main__":
    unittest.main()
