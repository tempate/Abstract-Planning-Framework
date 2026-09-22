import unittest
from unittest.mock import patch

import experiments.fetch
from experiments.fetch import main


class FetchTests(unittest.TestCase):
    def _run(self, argv, remote_head="abc123", local_head="abc123", pending=0):
        with (
            patch.object(experiments.fetch, "_remote_head", return_value=remote_head),
            patch.object(experiments.fetch, "_local_head", return_value=local_head),
            patch.object(experiments.fetch, "_pending_jobs", return_value=pending),
            patch.object(experiments.fetch, "_pull") as pull,
            patch.object(experiments.fetch, "collect") as collect,
            patch("sys.argv", ["fetch", *argv]),
        ):
            main()
        return pull, collect

    def test_a_run_from_another_commit_is_not_pulled(self):
        pull, _ = self._run(["--remote-dir", "/apf/other/runs/"], remote_head="aaa", local_head="bbb")

        pull.assert_not_called()

    def test_force_pulls_a_run_from_another_commit(self):
        pull, _ = self._run(["--remote-dir", "/apf/other/runs/", "--force"], remote_head="aaa", local_head="bbb")

        pull.assert_called_once()

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
