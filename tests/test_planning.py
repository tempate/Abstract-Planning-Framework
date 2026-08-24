import argparse
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, call, patch

from core.abstraction.model import Abstraction
from core.integrations.unified_planning import read_problem
from core.planning.abstract import _compute_abstract_plan, _resolve_abstraction, compute_abstract_plan
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


class AbstractPlanningOrchestrationTests(unittest.TestCase):
    def test_top_level_result_describes_the_generated_abstraction(self):
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(abstraction=abstraction, unary_delete_score=2)
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract._resolve_abstraction",
                return_value=(generated, "abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch("core.planning.abstract._compute_abstract_plan", return_value={"success": True}) as compute,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        compute.assert_called_once_with(
            config, abstraction, "run-dir", "run-123", "abstract-domain.pddl", "abstract-problem.pddl"
        )
        self.assertEqual(
            result["abstraction"],
            {
                "abstract_symbol": "item_abs",
                "objects_to_abstract": ["a", "b"],
                "object_type": "item",
                "relaxed_unary_deletes": 2,
            },
        )

    def test_clingo_source_translates_both_tasks_and_receives_abstract_asp(self):
        config = AbstractPlanningConfig(
            "domain.pddl", "problem.pddl", horizon=4, encoding="bounded", time_step=True, plan_source="clingo"
        )
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas", "horizon": 0}
        strategy = Mock()
        strategy.refine.return_value = {"success": True}

        with (
            patch(
                "core.planning.abstract.run_fast_downward", side_effect=[(concrete_task, 1.0), (abstract_task, 2.0)]
            ) as run,
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp") as add_switch,
            patch("core.planning.abstract.get_refinement_strategy", return_value=strategy) as get_strategy,
        ):
            result = _compute_abstract_plan(
                config, abstraction, "run-dir", "run-123", "abstract-domain.pddl", "abstract-problem.pddl"
            )

        self.assertEqual(result, {"success": True})
        self.assertEqual(
            run.call_args_list,
            [
                call("run-dir/concrete", "domain.pddl", "problem.pddl", "concrete", "translate"),
                call("run-dir/abstract", "abstract-domain.pddl", "abstract-problem.pddl", "abstract", "translate"),
            ],
        )
        self.assertEqual(
            sas_to_asp.call_args_list, [call("concrete.sas", "bounded", True), call("abstract.sas", "bounded", True)]
        )
        add_switch.assert_called_once_with("concrete asp", "bounded")
        context = get_strategy.call_args.args[1]
        self.assertEqual(get_strategy.call_args.args[0], "clingo")
        self.assertEqual(context.concrete_asp, "guarded concrete asp")
        self.assertEqual(context.abstract_asp, "abstract asp")
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 4)
        self.assertEqual(context.fd_timings["fd_concrete_time"], 1.0)
        self.assertEqual(context.fd_timings["fd_abstract_time"], 2.0)
        strategy.refine.assert_called_once_with()

    def test_fd_source_uses_its_plan_and_skips_abstract_asp_generation(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", plan_source="fd")
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas", "planFile": "sas_plan", "horizon": 6}
        strategy = Mock()
        strategy.refine.return_value = {"success": True}

        with (
            patch(
                "core.planning.abstract.run_fast_downward", side_effect=[(concrete_task, 1.0), (abstract_task, 2.0)]
            ) as run,
            patch("core.planning.abstract.sas_to_asp", return_value="concrete asp") as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.get_refinement_strategy", return_value=strategy) as get_strategy,
        ):
            result = _compute_abstract_plan(
                config, abstraction, "run-dir", "run-123", "abstract-domain.pddl", "abstract-problem.pddl"
            )

        self.assertEqual(result, {"success": True})
        self.assertEqual(run.call_args_list[1].args[-1], "plan")
        sas_to_asp.assert_called_once_with("concrete.sas", "bounded", False)
        context = get_strategy.call_args.args[1]
        self.assertEqual(get_strategy.call_args.args[0], "fd")
        self.assertIsNone(context.abstract_asp)
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 6)
        strategy.refine.assert_called_once_with()


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
        self.assertEqual(concrete.encoding, "bounded")
        self.assertFalse(concrete.time_step)
        self.assertIsInstance(abstract, PlanningConfig)
        self.assertEqual(abstract.encoding, concrete.encoding)
        self.assertEqual(abstract.plan_source, "clingo")
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

            abstract_problem, abstract_domain, abstract_problem_path = _resolve_abstraction(config, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual(config.abstract_name, "combined")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})

    @patch("core.planning.abstract.prepare_abstraction")
    def test_automatic_selection_is_delegated_to_symmetry_abstraction(self, prepare_abstraction):
        problem = Mock()
        abstraction = Mock(name="item_abs", objects=("a", "b"))
        prepare_abstraction.return_value = Mock(problem=problem, abstraction=abstraction)
        with tempfile.TemporaryDirectory() as directory:
            config = AbstractPlanningConfig("domain.pddl", "problem.pddl", bliss_time_limit=17)
            with patch("core.planning.abstract.write_problem", return_value=Mock(domain="d", problem="p")):
                selected, _, _ = _resolve_abstraction(config, directory)

        prepare_abstraction.assert_called_once_with(
            "domain.pddl", "problem.pddl", objects_to_abstract=None, abstract_name=None, bliss_time_limit=17
        )
        self.assertEqual(selected.abstraction.objects, ("a", "b"))
        self.assertIsNone(config.objects_to_abstract)
        self.assertIsNone(config.abstract_name)


if __name__ == "__main__":
    unittest.main()
