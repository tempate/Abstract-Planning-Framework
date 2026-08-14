import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from core.planning.config import (
    AbstractPlanningConfig,
    ConcretePlanningConfig,
)
from core.planning.concrete import compute_concrete_plan
from scripts.utils.arguments import nonnegative_int


class ConcretePlanningOrchestrationTests(unittest.TestCase):
    @patch("core.planning.concrete.run_clingo")
    @patch("core.planning.concrete.sas_to_asp")
    @patch("core.planning.concrete.run_fast_downward")
    @patch("core.planning.concrete.setup_debug_logger")
    @patch("core.planning.concrete.create_run_dir")
    def test_pipeline_uses_an_explicit_horizon_and_returns_normalized_timings(
        self,
        create_run_dir,
        setup_debug_logger,
        run_fast_downward,
        sas_to_asp,
        run_clingo,
    ):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory, "domain.pddl")
            problem = Path(directory, "problem.pddl")
            domain.write_bytes(b"domain")
            problem.write_bytes(b"problem")
            create_run_dir.return_value = (directory, "run-123")
            setup_debug_logger.return_value = (Mock(), str(Path(directory, "debug")))
            run_fast_downward.return_value = (
                {
                    "horizon": 8,
                    "sasFile": str(Path(directory, "output.sas")),
                    "planFile": str(Path(directory, "sas_plan")),
                },
                0.1,
            )
            run_clingo.return_value = ["occurs(action,3)"]

            config = ConcretePlanningConfig(
                domain_path=domain,
                problem_path=problem,
                horizon=3,
                encoding="bounded",
                time_step=True,
            )
            result = compute_concrete_plan(config)

        self.assertTrue(result["success"])
        self.assertEqual(result["horizon"], 3)
        self.assertEqual(result["plan"], ["occurs(action,3)"])
        self.assertEqual(result["timings"]["run_id"], directory)
        self.assertEqual(result["configuration"], config.as_dict())
        self.assertIsNone(result["timings"]["iterations"])
        run_fast_downward.assert_called_once_with(
            directory,
            b"domain",
            b"problem",
            "concrete",
            "translate",
        )
        sas_to_asp.assert_called_once_with(
            str(Path(directory, "output.sas")),
            str(Path(directory, "output_c.lp")),
            "bounded",
            True,
        )
        run_clingo.assert_called_once_with(
            [str(Path(directory, "output_c.lp"))],
            3,
        )


class ArgumentTests(unittest.TestCase):
    def test_nonnegative_integer_accepts_zero(self):
        self.assertEqual(nonnegative_int("0"), 0)
        self.assertEqual(nonnegative_int("12"), 12)

    def test_nonnegative_integer_rejects_negative_values(self):
        with self.assertRaisesRegex(Exception, "must be nonnegative"):
            nonnegative_int("-1")


class PlanningConfigurationTests(unittest.TestCase):
    def test_shared_defaults_are_explicit(self):
        concrete = ConcretePlanningConfig("domain.pddl", "problem.pddl")
        abstract = AbstractPlanningConfig(
            "abstract-domain.pddl",
            "abstract-problem.pddl",
            "concrete-domain.pddl",
            "concrete-problem.pddl",
        )

        self.assertIsNone(concrete.horizon)
        self.assertEqual(concrete.encoding, "exact")
        self.assertFalse(concrete.time_step)
        self.assertEqual(abstract.plan_source, "clingo")
        self.assertEqual(abstract.profile_name, "beluga")
        self.assertIsNone(abstract.abstract_symbol)
        self.assertIsNone(abstract.concrete_objects)

    def test_concrete_objects_are_stored_immutably(self):
        objects = ["hangar1", "hangar2"]
        config = AbstractPlanningConfig(
            "abstract-domain.pddl",
            "abstract-problem.pddl",
            "concrete-domain.pddl",
            "concrete-problem.pddl",
            concrete_objects=objects,
        )
        objects.append("hangar3")

        self.assertEqual(config.concrete_objects, ("hangar1", "hangar2"))


if __name__ == "__main__":
    unittest.main()
