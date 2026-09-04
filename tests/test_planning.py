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
from core.planning.abstract import _write_abstract_problem, compute_abstract_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import positive_int


@contextmanager
def _stubbed_abstract_pipeline(generated):
    """Run the abstract pipeline against stubbed integrations."""
    with (
        patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
        patch("core.planning.abstract.build_abstract_problem", return_value=generated),
        patch("core.planning.abstract._write_abstract_problem", return_value=("domain.pddl", "problem.pddl")),
        patch("core.planning.abstract.pddl_to_sas", side_effect=["concrete.sas", "abstract.sas"]),
        patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
        patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
        patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
    ):
        temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
        yield SimpleNamespace(sas_to_asp=sas_to_asp, refine=refine)


def _generated_abstraction(relaxed_deletes=()):
    return SimpleNamespace(
        problem=Mock(), abstraction=Abstraction("item_abs", ("a", "b"), "item"), relaxed_deletes=relaxed_deletes
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
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertEqual(result["metrics"]["counters"]["final_horizon"], 3)
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
        self.assertIs(context.relaxed_deletes, generated.relaxed_deletes)
        self.assertEqual(context.concrete_asp, "guarded concrete asp")
        self.assertEqual(context.abstract_asp, "abstract asp")

    def test_time_step_reaches_both_asp_translations(self):
        for time_step in (False, True):
            with self.subTest(time_step=time_step):
                config = AbstractPlanningConfig("domain.pddl", "problem.pddl", time_step=time_step)
                with _stubbed_abstract_pipeline(_generated_abstraction()) as stubs:
                    compute_abstract_plan(config)

                for translation in stubs.sas_to_asp.call_args_list:
                    self.assertEqual(translation.kwargs["abstract_time_steps"], time_step)

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


class PlanningConfigurationTests(unittest.TestCase):
    def test_abstract_configuration_extends_the_shared_one(self):
        abstract = AbstractPlanningConfig("domain.pddl", "problem.pddl")

        self.assertIsInstance(abstract, PlanningConfig)
        self.assertFalse(abstract.time_step)
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
            abstract_domain, abstract_problem_path = _write_abstract_problem(abstract_problem.problem, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})


class ArgumentTests(unittest.TestCase):
    def test_positive_integer_rejects_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_int("0")


if __name__ == "__main__":
    unittest.main()
