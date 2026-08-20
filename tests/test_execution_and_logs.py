import json
import logging
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.execution import LOGGER_NAME, PhaseTiming, setup_debug_logger
from scripts.utils.abstract_plan_log import hash_abstract_plan, initialize_plan_log, record_plan_attempt


class ExecutionTests(unittest.TestCase):
    def tearDown(self):
        logger = logging.getLogger(LOGGER_NAME)
        for handler in logger.handlers:
            handler.close()
        logger.handlers.clear()

    def test_logger_is_kept_under_the_run_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            logger, debug_dir = setup_debug_logger(directory)
            logger.info("test message")
            for handler in logger.handlers:
                handler.flush()

            self.assertIn("test message", Path(debug_dir, "planner_debug.log").read_text(encoding="utf-8"))

    def test_reconfiguring_the_logger_closes_the_previous_file(self):
        with tempfile.TemporaryDirectory() as directory:
            first_run = Path(directory, "first")
            second_run = Path(directory, "second")
            logger, _ = setup_debug_logger(first_run)
            previous_handler = logger.handlers[0]

            setup_debug_logger(second_run)

            self.assertIsNone(previous_handler.stream)
            self.assertEqual(len(logger.handlers), 1)

    @patch("core.execution.time.perf_counter", return_value=12.5)
    def test_phase_timing_stops_once(self, perf_counter):
        timing = PhaseTiming(_started_at=10.0)

        timing.stop()
        timing.stop()

        self.assertEqual(timing.elapsed, 2.5)
        self.assertEqual(perf_counter.call_count, 1)


class AbstractPlanLogTests(unittest.TestCase):
    def test_plan_hash_is_independent_of_atom_order(self):
        first = ["occurs(a,1)", "occurs(b,2)"]
        second = list(reversed(first))

        self.assertEqual(hash_abstract_plan(first), hash_abstract_plan(second))

    def test_attempts_are_accumulated_for_the_same_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            abstract_problem = Path(directory, "abstract.pddl")
            concrete_problem = Path(directory, "concrete.pddl")
            path = Path(directory, "attempts.json")
            abstract_problem.write_text("abstract", encoding="utf-8")
            concrete_problem.write_text("concrete", encoding="utf-8")
            initialize_plan_log(
                path,
                "problem-hash",
                abstract_problem,
                concrete_problem,
                abstract_symbol="shared",
                concrete_objects=["one", "two"],
            )
            plan = ["occurs(a,1)"]

            record_plan_attempt(path, plan, True, [])
            record_plan_attempt(path, plan, False, ["occurs(a,1)"])
            data = json.loads(path.read_text(encoding="utf-8"))

        entry = data["plans"][hash_abstract_plan(plan)]
        self.assertEqual(data["abstract_symbol"], "shared")
        self.assertEqual(data["concrete_objects"], ["one", "two"])
        self.assertEqual(entry["success_count"], 1)
        self.assertEqual(entry["failure_count"], 1)
        self.assertEqual(entry["failures"], [["occurs(a,1)"]])

    def test_initialization_does_not_overwrite_an_existing_log(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "attempts.json")
            path.write_text('{"sentinel": true}', encoding="utf-8")

            initialize_plan_log(path, "hash", "abstract", "concrete")

            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"sentinel": True})


if __name__ == "__main__":
    unittest.main()
