import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from experiments.status import REMOTE_SUMMARY, _report


class StatusTests(unittest.TestCase):
    def test_the_remote_summary_counts_what_the_results_say(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for problem, status in (("p01", "success"), ("p02", "timed_out"), ("p03", "success")):
                result = root / "example" / problem / "abstract.json"
                result.parent.mkdir(parents=True)
                result.write_text(json.dumps({"status": status}), encoding="utf-8")
            (root / "metadata.json").write_text('{"instances": {}}', encoding="utf-8")
            expected = [{"domain": "example", "problem": f"p0{n}.pddl", "mode": "abstract"} for n in (1, 2, 3, 4)]
            (root / "manifest.json").write_text(json.dumps({"expected_results": expected}), encoding="utf-8")

            completed = subprocess.run(
                [sys.executable, "-c", REMOTE_SUMMARY, str(root)], capture_output=True, text=True, check=True
            )
            summary = json.loads(completed.stdout)

        self.assertEqual(summary["expected"], 4)
        self.assertEqual(summary["counts"], {"success": 2, "timed_out": 1})

    def test_results_still_running_without_a_job_are_called_out(self):
        summary = {"expected": 4, "counts": {"success": 1, "running": 3}}

        with contextlib.redirect_stdout(io.StringIO()) as gone:
            # Queued jobs have not written anything, so they cannot account for them.
            _report("run-example", pending=5, running=0, summary=summary)
        with contextlib.redirect_stdout(io.StringIO()) as still_running:
            _report("run-example", pending=5, running=3, summary=summary)

        self.assertIn("killed", gone.getvalue())
        self.assertNotIn("killed", still_running.getvalue())


if __name__ == "__main__":
    unittest.main()
