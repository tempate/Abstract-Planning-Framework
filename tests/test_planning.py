import argparse
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from core.integrations.unified_planning import read_problem
from core.planning.abstract import _resolve_abstraction
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import nonnegative_int, positive_int


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.run_clingo")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.run_fast_downward")
    @patch("core.planning.concrete.temp_run_dir")
    def test_pipeline_uses_an_explicit_horizon_and_returns_normalized_timings(
        self, temp_run_dir, run_fast_downward, sas_to_asp, run_clingo
    ):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "domain.pddl")
            problem = Path(directory, "problem.pddl")
            domain.write_bytes(b"domain")
            problem.write_bytes(b"problem")
            temp_run_dir.return_value.__enter__.return_value = (directory, "run-123")
            run_fast_downward.return_value = (
                {
                    "horizon": 8,
                    "sasFile": str(Path(directory, "output.sas")),
                    "planFile": str(Path(directory, "sas_plan")),
                },
                0.1,
            )
            sas_to_asp.return_value = "asp program"
            run_clingo.return_value = ["occurs(action,3)"]

            config = PlanningConfig(
                domain_path=domain, problem_path=problem, horizon=3, encoding="bounded", time_step=True
            )
            result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["timings"]["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertIsNone(result["timings"]["iterations"])
        run_fast_downward.assert_called_once_with(directory, domain, problem, "concrete", "translate")
        sas_to_asp.assert_called_once_with(str(Path(directory, "output.sas")), "bounded", True)
        run_clingo.assert_called_once_with("asp program", 3)


class ArgumentTests(unittest.TestCase):
    def test_nonnegative_integer_accepts_zero(self):
        self.assertEqual(nonnegative_int("0"), 0)
        self.assertEqual(nonnegative_int("12"), 12)

    def test_nonnegative_integer_rejects_negative_values(self):
        with self.assertRaisesRegex(Exception, "must be nonnegative"):
            nonnegative_int("-1")

    def test_positive_integer_rejects_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_int("0")


class PlanningConfigurationTests(unittest.TestCase):
    def test_shared_defaults_are_explicit(self):
        concrete = PlanningConfig("domain.pddl", "problem.pddl")
        abstract = AbstractPlanningConfig("domain.pddl", "problem.pddl")

        self.assertIsNone(concrete.horizon)
        self.assertEqual(concrete.encoding, "exact")
        self.assertFalse(concrete.time_step)
        self.assertIsInstance(abstract, PlanningConfig)
        self.assertEqual(abstract.encoding, concrete.encoding)
        self.assertEqual(abstract.plan_source, "clingo")
        self.assertIsNone(abstract.abstract_name)
        self.assertIsNone(abstract.objects)

    def test_selected_objects_are_stored_immutably(self):
        objects = ["hangar1", "hangar2"]
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", objects=objects)
        objects.append("hangar3")

        self.assertEqual(config.objects, ("hangar1", "hangar2"))


class GeneratedAbstractionTests(unittest.TestCase):
    def test_explicit_objects_create_temporary_planner_inputs_and_mapping(self):
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
            config = AbstractPlanningConfig(domain, problem, objects=["a", "b"], abstract_name="combined")

            abstraction, abstract_domain, abstract_problem = _resolve_abstraction(config, root / "run")
            generated = read_problem(abstract_domain, abstract_problem)

        self.assertEqual(abstraction.abstract_name, "combined")
        self.assertEqual(config.abstract_name, "combined")
        self.assertEqual(config.objects, ("a", "b"))
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})

    @patch("core.planning.abstract.prepare_abstraction")
    def test_automatic_selection_is_delegated_to_symmetry_abstraction(self, prepare_abstraction):
        abstract_problem = Mock()
        abstraction = Mock(problem=abstract_problem, abstract_name="item_abs", objects=("a", "b"))
        prepare_abstraction.return_value = Mock(result=abstraction)
        with tempfile.TemporaryDirectory() as directory:
            config = AbstractPlanningConfig("domain.pddl", "problem.pddl", bliss_time_limit=17)
            with patch("core.planning.abstract.write_problem", return_value=Mock(domain="d", problem="p")):
                selected, _, _ = _resolve_abstraction(config, directory)

        prepare_abstraction.assert_called_once_with(
            "domain.pddl", "problem.pddl", objects=None, abstract_name=None, bliss_time_limit=17
        )
        self.assertEqual(selected.objects, ("a", "b"))
        self.assertIsNone(config.objects)
        self.assertIsNone(config.abstract_name)


if __name__ == "__main__":
    unittest.main()
