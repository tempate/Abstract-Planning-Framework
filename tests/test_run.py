import contextlib
import json
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from experiments.collect import collect
from experiments.run import PROJECT_ROOT, _human_status, _run_pipeline, _run_task
from scripts.utils.reporting import update_result_progress


class _FakeProcess:
    """One recorded outcome, shaped like the Popen the worker waits on."""

    def __init__(self, command, outcome):
        self.args = command
        # Never a real group: the worker signals this pid on a timeout.
        self.pid = -1
        self.returncode = None
        self._outcome = outcome

    def communicate(self, timeout=None):
        outcome = self._outcome
        if isinstance(outcome, BaseException):
            # The worker kills the group and reads what the process had left.
            left = getattr(outcome, "output", "") or ""
            if isinstance(left, bytes):
                left = left.decode()
            self._outcome = subprocess.CompletedProcess(self.args, None, stdout=left)
            raise outcome
        self.returncode = outcome.returncode
        return outcome.stdout, None

    def kill(self):
        pass


@contextlib.contextmanager
def _fake_planner(outcomes):
    """Replace the planner subprocess with recorded outcomes.

    `outcomes` is one CompletedProcess, a sequence of them, or a callable taking
    the command and the spawn arguments. os.killpg goes too, so that the fake
    pid cannot reach a group this test may signal.
    """
    pending = iter(outcomes if isinstance(outcomes, (list, tuple)) else [outcomes])

    def spawn(command, **kwargs):
        try:
            outcome = outcomes(command, **kwargs) if callable(outcomes) else next(pending)
        except BaseException as error:  # noqa: BLE001 - replayed where the worker expects it
            outcome = error
        return _FakeProcess(command, outcome)

    with patch("experiments.run.subprocess.Popen", side_effect=spawn) as popen, patch("experiments.run.os.killpg"):
        yield popen


class WorkerTests(unittest.TestCase):
    def test_the_project_root_is_the_repository_root(self):
        """Guards the parents[N] depth, which moving the runner has broken twice."""
        self.assertTrue((PROJECT_ROOT / "pyproject.toml").is_file(), f"{PROJECT_ROOT} is not the repository root")

    def test_worker_preserves_phase_progress_in_the_result(self):
        metrics = {"durations": {"concrete_fd": 2.5}, "counters": {}}

        def complete(command, **_kwargs):
            result_file = Path(_kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            running = json.loads(result_file.read_text(encoding="utf-8"))
            self.assertEqual(running["status"], "running")
            self.assertIsNone(running["progress"]["last_completed_phase"])
            update_result_progress(result_file, {"kind": "phase_completed", "phase": "concrete_fd"}, metrics)
            return subprocess.CompletedProcess(command, 2, stdout="planner failed before final metrics\n")

        with tempfile.TemporaryDirectory() as directory, _fake_planner(complete):
            result = _run_task("asp", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(result["progress"]["last_completed_phase"], "concrete_fd")
        self.assertEqual(result["progress"]["last_update"]["kind"], "phase_completed")
        self.assertEqual(rows[0]["concrete_fd_seconds"], 2.5)
        self.assertEqual(rows[0]["last_completed_phase"], "concrete_fd")

    def test_a_run_the_memory_limit_interrupts_is_recorded_with_its_phase(self):
        metrics = {"durations": {"symmetry_discovery": 1.5}, "counters": {}}

        def interrupt(command, **_kwargs):
            result_file = Path(_kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            update_result_progress(result_file, {"kind": "phase_completed", "phase": "symmetry_discovery"}, metrics)
            # runsolver sends SIGINT when the job outgrows its memory limit.
            raise KeyboardInterrupt

        with tempfile.TemporaryDirectory() as directory, _fake_planner(interrupt):
            result = _run_task("abs-asp", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(result["status"], "interrupted")
        self.assertEqual(rows[0]["last_completed_phase"], "symmetry_discovery")
        self.assertNotEqual(rows[0]["status"], "running")

    def test_timed_out_run_still_records_the_collapsed_class(self):
        metrics = {
            "durations": {},
            "counters": {},
            "abstraction": {"objects": ["ball1", "ball2", "ball3"], "object_type": "ball"},
        }

        def selected_then_killed(command, **kwargs):
            result_file = Path(kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            update_result_progress(result_file, {"kind": "abstraction_selected"}, metrics)
            raise subprocess.TimeoutExpired(command, 10, output="Starting\n")

        with tempfile.TemporaryDirectory() as directory, _fake_planner(selected_then_killed):
            _run_task("abs-asp", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=10)
            rows = collect(directory)

        # Nothing the killed run printed reaches the collector, so the class can
        # only come from the result file.
        self.assertEqual(rows[0]["status"], "timed out")
        self.assertEqual(rows[0]["abstracted_object_count"], 3)
        self.assertEqual(rows[0]["abstracted_object_type"], "ball")

    def test_the_collector_keeps_the_line_that_says_what_failed(self):
        outputs = {
            "usage: planner.py [-h]\nplanner.py: error: Unsupported quality metric\nStarting\n": (
                "Unsupported quality metric"
            ),
            # Fast Downward capitalizes its error, then keeps printing.
            (
                "Starting\n"
                "Error: Fast Downward (abstract) failed with exit code 31\n"
                "Driver aborting after translate\n"
                "INFO     Planner time: 0.14s\n"
            ): "Fast Downward (abstract) failed with exit code 31",
        }
        for output, message in outputs.items():
            with self.subTest(message=message):
                failed = subprocess.CompletedProcess([], 2, stdout=output)
                with tempfile.TemporaryDirectory() as directory, _fake_planner(failed):
                    _run_task("abs-asp", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
                    rows = collect(directory)

                self.assertEqual(rows[0]["status"], "error (exit code 2)")
                self.assertEqual(rows[0]["error_message"], message)

    def test_a_timeout_takes_down_what_the_pipeline_spawned(self):
        # No mocks: what outlives a timeout is the planner's own children, and
        # only a real process tree shows whether they were reaped.
        with tempfile.TemporaryDirectory() as directory:
            survivor = Path(directory) / "survivor.txt"
            outlives_its_parent = f"import time; time.sleep(1.5); open({str(survivor)!r}, 'w').write('alive')"
            spawns_it = (
                f"import subprocess, sys, time;"
                f" subprocess.Popen([sys.executable, '-c', {outlives_its_parent!r}]);"
                f" time.sleep(1.5)"
            )

            result = _run_pipeline([sys.executable, "-c", spawns_it], timeout=0.5)

            self.assertTrue(result["timed_out"])
            time.sleep(2)
            self.assertFalse(survivor.exists(), "a grandchild outlived the timeout")

    def test_benchmark_status_is_human_readable(self):
        self.assertEqual(_human_status({"status": "success"}), "success")
        self.assertEqual(_human_status({"status": "no_plan"}), "no plan found")
        self.assertEqual(_human_status({"status": "error", "return_code": 2}), "error (exit code 2)")
        self.assertEqual(_human_status({"status": "out_of_memory"}), "out of memory")
        self.assertEqual(_human_status({"status": "timed_out"}), "timed out")
        self.assertEqual(_human_status({"status": "symmetry_timeout"}), "symmetry timeout")
        self.assertEqual(_human_status({"status": "killed", "signal": 9}), "killed (signal 9)")
        self.assertEqual(_human_status({"status": "running"}), "running")

    def test_pipeline_records_every_machine_readable_outcome(self):
        completed = [
            subprocess.CompletedProcess([], 0, stdout=""),
            subprocess.CompletedProcess([], 1, stdout=""),
            subprocess.CompletedProcess([], 4, stdout=""),
            subprocess.CompletedProcess([], 3, stdout=""),
            subprocess.CompletedProcess([], 5, stdout=""),
            subprocess.CompletedProcess([], 6, stdout=""),
            subprocess.CompletedProcess([], 7, stdout=""),
            subprocess.CompletedProcess([], -9, stdout=""),
            subprocess.CompletedProcess([], 2, stdout=""),
            subprocess.TimeoutExpired([], 10, output="partial output"),
        ]
        with _fake_planner(completed):
            results = [_run_pipeline([], 10) for _ in completed]

        self.assertEqual(
            [result["status"] for result in results],
            [
                "success",
                "no_plan",
                "no_symmetries",
                "symmetry_timeout",
                "out_of_memory",
                "no_resources",
                "resource_timeout",
                "killed",
                "error",
                "timed_out",
            ],
        )
        self.assertEqual(results[7]["signal"], 9)
        self.assertNotIn("signal", results[8])


if __name__ == "__main__":
    unittest.main()
