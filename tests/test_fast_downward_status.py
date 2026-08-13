import logging
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from core.integrations.fast_downward import _run_task


class FastDownwardStatusTests(unittest.TestCase):
    def test_unsolvable_exit_codes_raise_clear_error(self):
        for returncode in (10, 11):
            with self.subTest(returncode=returncode):
                result = SimpleNamespace(
                    returncode=returncode,
                    stdout="Task is unsolvable",
                    stderr="",
                )
                with tempfile.TemporaryDirectory() as directory:
                    with patch(
                        "core.integrations.fast_downward.subprocess.run",
                        return_value=result,
                    ):
                        with self.assertRaisesRegex(
                            RuntimeError,
                            "problem is unsolvable",
                        ):
                            _run_task(
                                "concrete",
                                directory,
                                b"domain",
                                b"problem",
                                "plan",
                                logging.getLogger("fd-status-test"),
                            )

    def test_incomplete_search_includes_diagnostics(self):
        result = SimpleNamespace(
            returncode=12,
            stdout="Search stopped before a conclusion",
            stderr="resource limit reached",
        )
        with tempfile.TemporaryDirectory() as directory:
            with patch(
                "core.integrations.fast_downward.subprocess.run",
                return_value=result,
            ):
                with self.assertRaisesRegex(
                    RuntimeError,
                    "Search stopped before a conclusion",
                ):
                    _run_task(
                        "concrete",
                        directory,
                        b"domain",
                        b"problem",
                        "plan",
                        logging.getLogger("fd-status-test"),
                    )


if __name__ == "__main__":
    unittest.main()
