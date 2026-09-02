import argparse
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, call, patch

from core.abstraction.factory import Abstraction, AbstractionError, build_abstract_problem
from core.integrations.clingo import ClingoSolveResult
from core.integrations.unified_planning import read_problem
from core.planning.abstract import _write_abstract_problem, compute_abstract_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import positive_int


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.solve")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.pddl_to_sas")
    @patch("core.planning.concrete.temp_run_dir")
    def test_pipeline_returns_the_discovered_horizon_and_normalized_timings(
        self, temp_run_dir, pddl_to_sas, sas_to_asp, solve
    ):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "domain.pddl")
            problem = Path(directory, "problem.pddl")
            domain.write_bytes(b"domain")
            problem.write_bytes(b"problem")
            temp_run_dir.return_value.__enter__.return_value = (directory, "run-123")
            pddl_to_sas.return_value = ({"sasFile": str(Path(directory, "output.sas"))}, 0.1)
            sas_to_asp.return_value = "asp program"
            solve.return_value = ClingoSolveResult(["occurs(action,3)"], horizon=3, attempts=4)

            config = PlanningConfig(domain_path=domain, problem_path=problem, time_step=True)
            result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["timings"]["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertIsNone(result["timings"]["iterations"])
        pddl_to_sas.assert_called_once_with(directory, domain, problem, "concrete")
        sas_to_asp.assert_called_once_with(str(Path(directory, "output.sas")), abstract_time_steps=True)
        solve.assert_called_once_with("asp program")


class AbstractPlanningOrchestrationTests(unittest.TestCase):
    def test_top_level_passes_the_generated_abstraction_to_refinement(self):
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        abstract_problem = Mock()
        generated = SimpleNamespace(
            problem=abstract_problem, abstraction=abstraction, relaxed_deletes=(object(), object())
        )
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated) as build,
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ) as write,
            patch("core.planning.abstract.pddl_to_sas", side_effect=[(concrete_task, 1.0), (abstract_task, 2.0)]),
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
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", time_step=True)

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract.build_abstract_problem",
                side_effect=AbstractionError("PDDL Symmetries found no abstractable object classes"),
            ),
            patch("core.planning.abstract.pddl_to_sas") as pddl_to_sas,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            with self.assertRaisesRegex(AbstractionError, "found no abstractable object classes"):
                compute_abstract_plan(config)

        pddl_to_sas.assert_not_called()

    def test_propagates_other_abstraction_errors_before_planning(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", objects_to_abstract=("a", "b"))

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch(
                "core.planning.abstract.build_abstract_problem",
                side_effect=AbstractionError("Selected objects must have the same declared type"),
            ),
            patch("core.planning.abstract.pddl_to_sas") as pddl_to_sas,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            with self.assertRaisesRegex(AbstractionError, "same declared type"):
                compute_abstract_plan(config)

        pddl_to_sas.assert_not_called()

    def test_clingo_source_translates_both_tasks_and_receives_abstract_asp(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", time_step=True)
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(problem=Mock(), abstraction=abstraction, relaxed_deletes=())
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch(
                "core.planning.abstract.pddl_to_sas", side_effect=[(concrete_task, 1.0), (abstract_task, 2.0)]
            ) as run,
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
                call("run-dir/concrete", "domain.pddl", "problem.pddl", "concrete"),
                call("run-dir/abstract", "abstract-domain.pddl", "abstract-problem.pddl", "abstract"),
            ],
        )
        self.assertEqual(
            sas_to_asp.call_args_list,
            [call("concrete.sas", abstract_time_steps=True), call("abstract.sas", abstract_time_steps=True)],
        )
        add_switch.assert_called_once_with("concrete asp")
        context = refine.call_args.args[0]
        self.assertEqual(context.concrete_asp, "guarded concrete asp")
        self.assertEqual(context.abstract_asp, "abstract asp")
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 0)
        self.assertEqual(context.fd_timings["fd_concrete_time"], 1.0)
        self.assertEqual(context.fd_timings["fd_abstract_time"], 2.0)
        refine.assert_called_once_with(context)

    def test_incremental_search_translates_both_tasks_and_generates_both_programs(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(problem=Mock(), abstraction=abstraction, relaxed_deletes=())
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch(
                "core.planning.abstract._write_abstract_problem",
                return_value=("abstract-domain.pddl", "abstract-problem.pddl"),
            ),
            patch(
                "core.planning.abstract.pddl_to_sas", side_effect=[(concrete_task, 1.0), (abstract_task, 2.0)]
            ) as run,
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        self.assertEqual(result, {"success": True})
        self.assertEqual(
            run.call_args_list,
            [
                call("run-dir/concrete", "domain.pddl", "problem.pddl", "concrete"),
                call("run-dir/abstract", "abstract-domain.pddl", "abstract-problem.pddl", "abstract"),
            ],
        )
        self.assertEqual(
            sas_to_asp.call_args_list,
            [call("concrete.sas", abstract_time_steps=False), call("abstract.sas", abstract_time_steps=False)],
        )
        context = refine.call_args.args[0]
        self.assertEqual(context.abstract_asp, "abstract asp")
        self.assertEqual(context.abstract_task, abstract_task)
        self.assertEqual(context.horizon, 0)
        refine.assert_called_once_with(context)


class ArgumentTests(unittest.TestCase):
    def test_positive_integer_rejects_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_int("0")


class PlanningConfigurationTests(unittest.TestCase):
    def test_shared_defaults_are_explicit(self):
        concrete = PlanningConfig("domain.pddl", "problem.pddl")
        abstract = AbstractPlanningConfig("domain.pddl", "problem.pddl")

        self.assertFalse(hasattr(concrete, "horizon"))
        self.assertFalse(hasattr(concrete, "encoding"))
        self.assertFalse(concrete.time_step)
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
                "core.planning.abstract.pddl_to_sas",
                side_effect=[({"sasFile": "concrete.sas"}, 1.0), ({"sasFile": "abstract.sas"}, 2.0)],
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
