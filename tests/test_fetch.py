import contextlib
import io
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import experiments.fetch
from experiments.fetch import _checkout_holds, _default_remote_dir, _remote_command_path, main


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
            patch.object(experiments.fetch, "_remote_run_name", return_value="run-example"),
            patch.object(experiments.fetch, "_pending_jobs", return_value=pending),
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

    def test_the_branch_names_the_worktree_the_run_is_pulled_from(self):
        self.assertEqual(_default_remote_dir("sas-resource-ladders"), "apf/sas-resource-ladders/runs/")

    def test_a_home_relative_path_survives_being_quoted_for_the_remote_shell(self):
        self.assertEqual(_remote_command_path("~/apf/main/runs/"), "apf/main/runs/")
        self.assertEqual(_remote_command_path("/scratch/runs/"), "/scratch/runs/")

    def test_a_run_from_other_code_is_collected_only_when_forced(self):
        for argv, collected in (([], False), (["--force"], True)):
            with self.subTest(argv=argv):
                _, collect = self._run(["--remote-dir", "/apf/other/runs/", *argv], holds=False)

                self.assertEqual(collect.called, collected)

    def test_this_checkout_holds_its_own_commit_and_not_an_unknown_one(self):
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()

        self.assertTrue(_checkout_holds(head))
        self.assertFalse(_checkout_holds("0" * 40))

    def test_each_pull_gets_a_directory_of_its_own(self):
        pulls = [self._run(["--remote-dir", "/apf/branch/runs/"])[0] for _ in range(2)]

        first, second = (pull.call_args.args[2] for pull in pulls)
        self.assertNotEqual(first, second)

    def test_only_this_runs_jobs_hold_up_its_pull(self):
        with patch.object(experiments.fetch, "subprocess") as subprocesses:
            subprocesses.run.return_value.stdout = "0\n"
            experiments.fetch._pending_jobs("copperhead", "run-example")
            with_name = subprocesses.run.call_args[0][0][-1]
            experiments.fetch._pending_jobs("copperhead")
            without_name = subprocesses.run.call_args[0][0][-1]

        self.assertIn("--name=run-example", with_name)
        self.assertNotIn("--name", without_name)

    def test_an_unfinished_run_is_not_pulled(self):
        pull, _ = self._run(["--remote-dir", "/apf/branch/runs/"], pending=3)

        pull.assert_not_called()

    def test_a_finished_run_on_this_commit_is_pulled_and_collected(self):
        pull, collect = self._run(["--remote-dir", "/apf/branch/runs/"])

        pull.assert_called_once()
        collect.assert_called_once()

    def test_a_dry_run_transfers_nothing_into_the_csv(self):
        _, collect = self._run(["--remote-dir", "/apf/branch/runs/", "--dry-run"])

        collect.assert_not_called()


if __name__ == "__main__":
    unittest.main()
