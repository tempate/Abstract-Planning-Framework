import os
import tempfile
import unittest
from pathlib import Path

from core.integrations.fast_downward import pddl_to_sas
from core.planners.symmetry_pruning import SasTask, class_generators

GRIPPER = Path(__file__).resolve().parents[1] / "experiments" / "benchmarks" / "downward-benchmarks" / "gripper"


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1", "set RUN_PLANNER_INTEGRATION=1 to run Fast Downward"
)
class ClassGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as directory:
            sas_path = pddl_to_sas(directory, GRIPPER / "domain.pddl", GRIPPER / "prob01.pddl", "concrete")
            cls.task = SasTask.read(sas_path)

    def test_interchangeable_objects_give_generators(self):
        self.assertTrue(class_generators(self.task, ("ball1", "ball2", "ball3", "ball4")))

    def test_objects_the_goal_tells_apart_give_none(self):
        self.assertEqual(class_generators(self.task, ("rooma", "roomb")), [])


if __name__ == "__main__":
    unittest.main()
