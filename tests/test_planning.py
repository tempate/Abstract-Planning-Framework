import argparse
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, call, patch

from core.abstraction.factory import Abstraction, AbstractionError, build_abstract_problem
from core.integrations.clingo import ClingoSolveResult
from core.integrations.unified_planning import read_problem, write_problem_files
from core.metrics import PlanningMetrics
from core.planning.abstract import compute_abstract_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import positive_int


def _written_paths(problem, directory):
    """Stand in for Unified Planning serialization inside a run directory."""
    return f"{directory}/domain.pddl", f"{directory}/problem.pddl"


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.solve")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.pddl_to_sas")
    @patch("core.planning.concrete.write_problem_files")
    @patch("core.planning.concrete.read_problem")
    @patch("core.planning.concrete.temp_run_dir")
    def test_pipeline_returns_the_discovered_horizon_and_structured_metrics(
        self, temp_run_dir, read_problem, write_problem_files, pddl_to_sas, sas_to_asp, solve
    ):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "domain.pddl")
            problem = Path(directory, "problem.pddl")
            domain.write_bytes(b"domain")
            problem.write_bytes(b"problem")
            parsed = Mock()
            temp_run_dir.return_value.__enter__.return_value = (directory, "run-123")
            read_problem.return_value = parsed
            write_problem_files.return_value = ("written-domain.pddl", "written-problem.pddl")
            pddl_to_sas.return_value = {"sasFile": str(Path(directory, "output.sas"))}
            sas_to_asp.return_value = "asp program"
            solve.return_value = ClingoSolveResult(["occurs(action,3)"], horizon=3, attempts=4)

            config = PlanningConfig(domain_path=domain, problem_path=problem, time_step=True)
            result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertEqual(result["metrics"]["counters"]["final_horizon"], 3)
        self.assertEqual(result["metrics"]["counters"]["concrete_solve_calls"], 4)
        self.assertEqual(
            set(result["metrics"]["durations"]),
            {
                "total",
                "problem_reading",
                "concrete_pddl_writing",
                "concrete_fd",
                "concrete_asp",
                "guided_concrete_solving",
            },
        )
        read_problem.assert_called_once_with(domain, problem)
        write_problem_files.assert_called_once_with(parsed, str(Path(directory, "generated-concrete")))
        pddl_to_sas.assert_called_once_with(directory, "written-domain.pddl", "written-problem.pddl", "concrete")
        sas_to_asp.assert_called_once_with(str(Path(directory, "output.sas")), abstract_time_steps=True)
        solve.assert_called_once()
        self.assertEqual(solve.call_args.args, ("asp program",))
        self.assertIn("on_attempt", solve.call_args.kwargs)


class AbstractPlanningOrchestrationTests(unittest.TestCase):
    def test_top_level_passes_the_generated_abstraction_to_refinement(self):
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        abstract_problem = Mock()
        concrete_problem = Mock()
        generated = SimpleNamespace(
            problem=abstract_problem,
            concrete_problem=concrete_problem,
            abstraction=abstraction,
            relaxed_deletes=(object(), object()),
        )
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}

        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated) as build,
            patch("core.planning.abstract.write_problem_files", side_effect=_written_paths) as write,
            patch("core.planning.abstract.pddl_to_sas", side_effect=[concrete_task, abstract_task]),
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]),
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        build.assert_called_once()
        self.assertEqual(build.call_args.args[0], config)
        self.assertIsInstance(build.call_args.args[1], PlanningMetrics)
        self.assertEqual(
            write.call_args_list,
            [
                call(concrete_problem, "run-dir/generated-concrete"),
                call(abstract_problem, "run-dir/generated-abstraction"),
            ],
        )
        context = refine.call_args.args[0]
        self.assertIs(context.abstraction, abstraction)
        self.assertIs(context.relaxed_deletes, generated.relaxed_deletes)
        self.assertTrue(result["success"])
        self.assertEqual(
            set(result["metrics"]["durations"]),
            {
                "total",
                "concrete_pddl_writing",
                "abstract_pddl_writing",
                "concrete_fd",
                "abstract_fd",
                "concrete_asp",
                "abstract_asp",
            },
        )

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
        generated = SimpleNamespace(
            problem=Mock(), concrete_problem=Mock(), abstraction=abstraction, relaxed_deletes=()
        )
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch("core.planning.abstract.write_problem_files", side_effect=_written_paths),
            patch("core.planning.abstract.pddl_to_sas", side_effect=[concrete_task, abstract_task]) as run,
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp") as add_switch,
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(
            run.call_args_list,
            [
                call(
                    "run-dir/concrete",
                    "run-dir/generated-concrete/domain.pddl",
                    "run-dir/generated-concrete/problem.pddl",
                    "concrete",
                ),
                call(
                    "run-dir/abstract",
                    "run-dir/generated-abstraction/domain.pddl",
                    "run-dir/generated-abstraction/problem.pddl",
                    "abstract",
                ),
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
        self.assertIsInstance(context.metrics, PlanningMetrics)
        refine.assert_called_once_with(context)

    def test_incremental_search_translates_both_tasks_and_generates_both_programs(self):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        generated = SimpleNamespace(
            problem=Mock(), concrete_problem=Mock(), abstraction=abstraction, relaxed_deletes=()
        )
        concrete_task = {"sasFile": "concrete.sas"}
        abstract_task = {"sasFile": "abstract.sas"}
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.build_abstract_problem", return_value=generated),
            patch("core.planning.abstract.write_problem_files", side_effect=_written_paths),
            patch("core.planning.abstract.pddl_to_sas", side_effect=[concrete_task, abstract_task]) as run,
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]) as sas_to_asp,
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}) as refine,
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            result = compute_abstract_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(
            run.call_args_list,
            [
                call(
                    "run-dir/concrete",
                    "run-dir/generated-concrete/domain.pddl",
                    "run-dir/generated-concrete/problem.pddl",
                    "concrete",
                ),
                call(
                    "run-dir/abstract",
                    "run-dir/generated-abstraction/domain.pddl",
                    "run-dir/generated-abstraction/problem.pddl",
                    "abstract",
                ),
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
            abstract_domain, abstract_problem_path = write_problem_files(abstract_problem.problem, root / "run")
            generated = read_problem(abstract_domain, abstract_problem_path)
            concrete_domain, concrete_problem_path = write_problem_files(
                abstract_problem.concrete_problem, root / "concrete-run"
            )
            regenerated = read_problem(concrete_domain, concrete_problem_path)

        self.assertEqual(abstract_problem.abstraction.name, "combined")
        self.assertEqual(config.abstract_name, "combined")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual({item.name for item in generated.all_objects}, {"combined"})
        self.assertEqual({item.name for item in regenerated.all_objects}, {"a", "b"})

    @patch("core.planning.abstract.build_abstract_problem")
    def test_automatic_selection_is_delegated_to_symmetry_abstraction(self, build_abstract_problem):
        problem = Mock()
        abstraction = Abstraction("item_abs", ("a", "b"), "item")
        build_abstract_problem.return_value = Mock(
            problem=problem, concrete_problem=Mock(), abstraction=abstraction, relaxed_deletes=()
        )
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl", symmetry_time_limit=17)
        with (
            patch("core.planning.abstract.temp_run_dir") as temp_run_dir,
            patch("core.planning.abstract.write_problem_files", side_effect=_written_paths),
            patch(
                "core.planning.abstract.pddl_to_sas",
                side_effect=[{"sasFile": "concrete.sas"}, {"sasFile": "abstract.sas"}],
            ),
            patch("core.planning.abstract.sas_to_asp", side_effect=["concrete asp", "abstract asp"]),
            patch("core.planning.abstract.add_switch_to_asp_rule", return_value="guarded concrete asp"),
            patch("core.planning.abstract.refine", return_value={"success": True}),
        ):
            temp_run_dir.return_value.__enter__.return_value = ("run-dir", "run-123")
            compute_abstract_plan(config)

        build_abstract_problem.assert_called_once()
        self.assertEqual(build_abstract_problem.call_args.args[0], config)
        self.assertIsInstance(build_abstract_problem.call_args.args[1], PlanningMetrics)
        self.assertEqual(build_abstract_problem.return_value.abstraction.objects, ("a", "b"))
        self.assertIsNone(config.objects_to_abstract)
        self.assertIsNone(config.abstract_name)


if __name__ == "__main__":
    unittest.main()
