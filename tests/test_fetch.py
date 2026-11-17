import contextlib
import io
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import experiments.fetch
from experiments.cluster import remote_path
from experiments.fetch import _checkout_holds, main


class FetchTests(unittest.TestCase):
    def _run(self, argv, holds=True, pending=0):
        # Without --into, a pull makes a directory of its own; keep the tests from leaving them behind.
        created = []
        mkdtemp = tempfile.mkdtemp

        def tracked_mkdtemp(**kwargs):
            created.append(mkdtemp(**kwargs))
            return created[-1]

        with (
            patch.object(experiments.fetch.tempfile, "mkdtemp", side_effect=tracked_mkdtemp),
            patch.object(experiments.fetch, "_manifest_commit", return_value="abc123"),
            patch.object(experiments.fetch, "_checkout_holds", return_value=holds),
            patch.object(experiments.fetch, "run_name", return_value="run-example"),
            patch.object(experiments.fetch, "queued_jobs", return_value=pending),
            patch.object(experiments.fetch, "_pull") as pull,
            patch.object(experiments.fetch, "collect") as collect,
            patch("sys.argv", ["fetch", *argv]),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            try:
                main()
            finally:
                for directory in created:
                    shutil.rmtree(directory)
        return pull, collect

    def test_a_home_relative_path_survives_being_quoted_for_the_remote_shell(self):
        self.assertEqual(remote_path("~/apf/main/runs/"), "apf/main/runs/")
        self.assertEqual(remote_path("/scratch/runs/"), "/scratch/runs/")

    def test_this_checkout_holds_its_own_commit_and_not_an_unknown_one(self):
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()

        self.assertTrue(_checkout_holds(head))
        self.assertFalse(_checkout_holds("0" * 40))

    def test_a_commit_that_only_refreshes_results_still_holds_the_code(self):
        with tempfile.TemporaryDirectory() as directory:
            git = lambda *args: subprocess.run(
                ["git", "-C", directory, *args], check=True, capture_output=True, text=True
            )
            git("init", "-q")
            git("config", "user.email", "test@example.com")
            git("config", "user.name", "Test")
            (Path(directory) / "planner.py").write_text("code\n")
            git("add", "-A")
            git("commit", "-q", "-m", "Code")
            run_commit = git("rev-parse", "HEAD").stdout.strip()
            for name in ("results.csv", "report.md", "best_classes.csv", "runs.md"):
                (Path(directory) / name).write_text("rows\n")
            git("add", "-A")
            git("commit", "-q", "-m", "Update results")

            with contextlib.chdir(directory):
                self.assertTrue(_checkout_holds(run_commit))

    def test_each_pull_gets_a_directory_of_its_own(self):
        pulls = [self._run(["--remote-dir", "/apf/branch/runs/"])[0] for _ in range(2)]

        first, second = (pull.call_args.args[2] for pull in pulls)
        self.assertNotEqual(first, second)

    def test_a_run_is_pulled_only_when_finished_and_collected_only_from_this_code(self):
        cases = (
            # argv, the checkout holds the run's commit, jobs still queued, pulled, collected
            ([], True, 0, True, True),
            ([], True, 3, False, False),
            ([], False, 0, True, False),
            (["--force"], False, 0, True, True),
            (["--dry-run"], True, 0, True, False),
        )
        for argv, holds, pending, pulled, collected in cases:
            with self.subTest(argv=argv, holds=holds, pending=pending):
                pull, collect = self._run(["--remote-dir", "/apf/branch/runs/", *argv], holds=holds, pending=pending)

                self.assertEqual((pull.called, collect.called), (pulled, collected))


if __name__ == "__main__":
    unittest.main()
