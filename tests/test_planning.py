import argparse
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.abstraction.factory import Abstraction, AbstractionError, build_abstract_problem
from core.integrations.clingo import ClingoSolveResult
from core.integrations.unified_planning import read_problem
from core.outcomes import UnsolvableTaskError
from core.planning.abstract import write_abstract_problem, compute_abstract_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from core.planning.solvability import compute_abstract_verdict, compute_concrete_verdict
from scripts.utils.arguments import positive_int


@contextmanager
def _stubbed_abstract_pipeline(generated):
    """Run the abstract pipeline against stubbed integrations."""
    with (
        patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
        patch("core.planning.abstract.build_abstract_problem", return_value=generated),
        patch("core.planning.abstract.write_abstract_problem", return_value=("domain.pddl", "problem.pddl")),
        patch("core.planning.abstract.pddl_to_sas", side_effect=["concrete.sas", "abstract.sas"]),
        patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
        patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
        patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
    ):
        temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
        yield SimpleNamespace(sas_to_asp=sas_to_asp, refine=refine)


def _generated_abstraction(relaxed_deletes=(), relaxed_inequalities=()):
    return SimpleNamespace(
        problem=Mock(),
        abstraction=Abstraction("item_abs", ("a", "b"), "item"),
        relaxed_deletes=relaxed_deletes,
        relaxed_inequalities=relaxed_inequalities,
    )


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.solve")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.pddl_to_sas")
    @patch("core.planning.concrete.temp_run_dir")
    def test_the_solver_result_becomes_the_planning_result(self, temp_run_dir, pddl_to_sas, sas_to_asp, solve):
        temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
        pddl_to_sas.return_value = "concrete.sas"
        sas_to_asp.return_value = "asp program"
        solve.return_value = ClingoSolveResult(["occurs(action,3)"], horizon=3, attempts=4)
        config = PlanningConfig("domain.pddl", "problem.pddl")

        result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertEqual(result["metrics"]["counters"]["concrete_solve_calls"], 4)
        self.assertEqual(sas_to_asp.call_args.args[0], "concrete.sas")


class AbstractPlanningOrchestrationTests(unittest.TestCase):
    def test_refinement_receives_the_abstraction_and_both_programs(self):
        generated = _generated_abstraction(relaxed_deletes=(object(),))

        with _stubbed_abstract_pipeline(generated) as stubs:
            result = compute_abstract_plan(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        context = stubs.refine.call_args.args[0]
        self.assertTrue(result["success"])
        self.assertIs(context.abstraction, generated.abstraction)
        self.assertEqual(context.concrete_asp, "guarded concrete asp")
        self.assertEqual(context.abstract_asp, "abstract asp")

    def test_an_abstraction_failure_aborts_before_translation(self):
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", side_effect=AbstractionError("no classes")),
            patch("core.planning.abstract.pddl_to_sas") as pddl_to_sas,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            with self.assertRaises(AbstractionError):
                compute_abstract_plan(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        pddl_to_sas.assert_not_called()


@contextmanager
def _stubbed_decision(found):
    """Run the abstract decision pipeline against stubbed integrations."""
    with (
        patch("core.planning.solvability.temp_run_dir") as temp_run_dir,
        patch(
            "core.planning.solvability.build_abstract_problem", return_value=_generated_abstraction()
        ) as build_abstract_problem,
        patch("core.planning.solvability.write_abstract_problem", return_value=("domain.pddl", "problem.pddl")),
        patch("core.planning.solvability.has_plan", return_value=found),
    ):
        temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
        yield SimpleNamespace(build_abstract_problem=build_abstract_problem)


class DecisionTests(unittest.TestCase):
    @patch("core.planning.solvability.has_plan")
    def test_searching_the_task_itself_settles_it(self, has_plan):
        for found, verdict in ((True, "solvable"), (False, "unsolvable")):
            with self.subTest(found=found):
                has_plan.return_value = found

                result = compute_concrete_verdict(PlanningConfig("domain.pddl", "problem.pddl"))

                self.assertEqual(result["verdict"], verdict)

    def test_an_abstract_plan_settles_nothing(self):
        with _stubbed_decision(found=True):
            result = compute_abstract_verdict(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unknown")

    def test_an_abstraction_with_no_plan_proves_the_task_unsolvable(self):
        with _stubbed_decision(found=False):
            result = compute_abstract_verdict(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unsolvable")

    def test_an_integration_proving_the_task_unsolvable_settles_it(self):
        with _stubbed_decision(found=True) as stubs:
            stubs.build_abstract_problem.side_effect = UnsolvableTaskError("no relaxed solution")

            result = compute_abstract_verdict(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(result["verdict"], "unsolvable")


class PlanningConfigurationTests(unittest.TestCase):
    def test_abstract_configuration_extends_the_shared_one(self):
        abstract = AbstractPlanningConfig("domain.pddl", "problem.pddl")

        self.assertIsInstance(abstract, PlanningConfig)
        self.assertIsNone(abstract.abstract_name)
        self.assertIsNone(abstract.objects_to_abstract)

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
