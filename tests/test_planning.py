import argparse
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, call, patch

from core.abstraction.factory import Abstraction, AbstractionError, build_abstract_problem
from core.integrations.unified_planning import read_problem
from core.planning.abstract import _write_abstract_problem, compute_abstract_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import nonnegative_int, positive_int


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.run_clingo")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.run_fast_downward")
    @patch("core.planning.concrete.temp_run_dir")
    def test_pipeline_uses_an_explicit_horizon_and_returns_normalized_result(
        self, temp_run_dir, run_fast_downward, sas_to_asp, run_clingo
    ):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "domain.pddl")
            problem = Path(directory, "problem.pddl")
            domain.write_bytes(b"domain")
            problem.write_bytes(b"problem")
            temp_run_dir.return_value.__enter__.return_value = (directory, "run-123")
            run_fast_downward.return_value = {
                "horizon": 8,
                "sasFile": str(Path(directory, "output.sas")),
                "planFile": str(Path(directory, "sas_plan")),
            }
            sas_to_asp.return_value = "asp program"
            run_clingo.return_value = ["occurs(action,3)"]

            config = PlanningConfig(
                domain_path=domain, problem_path=problem, horizon=3, encoding="bounded", time_step=True
            )
            result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertIsNone(result["iterations"])
        run_fast_downward.assert_called_once_with(directory, domain, problem, "concrete", "translate")
        sas_to_asp.assert_called_once_with(str(Path(directory, "output.sas")), "bounded", True)
        run_clingo.assert_called_once_with("asp program", 3)


class AbstractPlanningOrchestrationTests(unittest.TestCase):
    def test_top_level_passes_the_generated_abstraction_to_refinement(self):
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        abstract_problem = Mock()
        generated = SimpleNamespace(
            problem=abstract_problem, abstraction=abstraction, relaxed_deletes=(object(), object())
        )
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas", "horizon": 2}

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated) as build,
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ) as write,
            patch("core.planning.abstract.run_fast_downward", side_effect=[concrete_task, abstract_task]),
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]),
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        build.assert_called_once_with(config)
        write.assert_called_once_with(abstract_problem, "run-dir")
        context = refine.call_args.args[0]
        self.assertIs(context.abstraction, abstraction)
        self.assertIs(context.relaxed_deletes, generated.relaxed_deletes)
        self.assertEqual(result, {"success": True})

    def test_exits_abstract_pipeline_when_no_symmetry_class_exists(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", horizon=4, encoding="exact", time_step=True)

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract.build_abstract_problem",
                side_effect=AbstractionError("PDDL Symmetries found no abstractable object classes"),
            ),
            patch("core.planning.abstract.run_fast_downward") as run_fast_downward,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            with self.assertRaisesRegex(AbstractionError, "found no abstractable object classes"):
                compute_abstract_plan(config)

        run_fast_downward.assert_not_called()

    def test_propagates_other_abstraction_errors_before_planning(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", objects_to_abstract=("a", "b"))

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract.build_abstract_problem",
                side_effect=AbstractionError("Selected objects must have the same declared type"),
            ),
            patch("core.planning.abstract.run_fast_downward") as run_fast_downward,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            with self.assertRaisesRegex(AbstractionError, "same declared type"):
                compute_abstract_plan(config)

        run_fast_downward.assert_not_called()

    def test_clingo_source_translates_both_tasks_and_receives_abstract_asp(self):
        config = AbstractPlanningConfig(
            "domain.pddl", "problem.pddl", horizon=4, encoding="bounded", time_step=True, plan_source="clingo"
        )
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(problem=Mock(), abstraction=abstraction, relaxed_deletes=())
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas", "horizon": 0}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch("core.planning.abstract.run_fast_downward", side_effect=[concrete_task, abstract_task]) as run,
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp") as add_switch,
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

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
        context = refine.call_args.args[0]
        self.assertEqual(context.concrete_asp, "guarded concrete asp")
        self.assertEqual(context.abstract_asp, "abstract asp")
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 4)
        refine.assert_called_once_with(context)

    def test_fd_source_uses_its_plan_and_skips_abstract_asp_generation(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", plan_source="fd")
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(problem=Mock(), abstraction=abstraction, relaxed_deletes=())
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas", "planFile": "sas_plan", "horizon": 6}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch("core.planning.abstract.run_fast_downward", side_effect=[concrete_task, abstract_task]) as run,
            patch("core.planning.abstract.sas_to_asp", return_value="concrete asp") as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        self.assertEqual(result, {"success": True})
        self.assertEqual(run.call_args_list[1].args[-1], "plan")
        sas_to_asp.assert_called_once_with("concrete.sas", "bounded", False)
        context = refine.call_args.args[0]
        self.assertIsNone(context.abstract_asp)
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 6)
        refine.assert_called_once_with(context)


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

            abstract_problem = build_abstract_problem(config)
            abstract_domain, abstract_problem_path = _write_abstract_problem(abstract_problem.problem, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual(config.abstract_name, "combined")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})

    @patch("core.planning.abstract.build_abstract_problem")
    def test_automatic_selection_is_delegated_to_symmetry_abstraction(self, build_abstract_problem):
        problem = Mock()
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        build_abstract_problem.return_value = Mock(problem=problem, abstraction=abstraction, relaxed_deletes=())
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", symmetry_time_limit=17)
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch(
                "core.planning.abstract.run_fast_downward",
                side_effect=[{"sasFile": "concrete.sas"}, {"sasFile": "abstract.sas", "horizon": 0}],
            ),
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]),
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}),
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            compute_abstract_plan(config)

        build_abstract_problem.assert_called_once_with(config)
        self.assertEqual(build_abstract_problem.return_value.abstraction.objects, ("a", "b"))
        self.assertIsNone(config.objects_to_abstract)
        self.assertIsNone(config.abstract_name)


if __name__ == "__main__":
    unittest.main()
