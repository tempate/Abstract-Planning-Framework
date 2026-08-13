import tempfile
import unittest
from pathlib import Path

from core.integrations.clingo import create_control
from core.paths import (
    BOUNDED_HORIZON_ENCODING,
    EXACT_HORIZON_ENCODING,
    OCCURRENCE_VALIDATION_ENCODING,
)


class OccurrenceValidationTests(unittest.TestCase):
    encodings = (EXACT_HORIZON_ENCODING, BOUNDED_HORIZON_ENCODING)

    def test_grounded_action_occurrence_is_allowed(self):
        for encoding in self.encodings:
            with self.subTest(encoding=encoding):
                self.assertTrue(self._solve(encoding, "known").satisfiable)

    def test_unknown_action_occurrence_is_rejected(self):
        for encoding in self.encodings:
            with self.subTest(encoding=encoding):
                self.assertTrue(self._solve(encoding, "missing").unsatisfiable)

    @staticmethod
    def _solve(encoding, mapped_action):
        with tempfile.TemporaryDirectory() as directory:
            task_path = Path(directory) / "task.lp"
            task_path.write_text('action(action("known")).\n', encoding="utf-8")

            mapping_path = Path(directory) / "mapping.lp"
            mapping_path.write_text(
                f'occurs(action("{mapped_action}"), 1).\n',
                encoding="utf-8",
            )

            control = create_control(
                [
                    encoding,
                    str(task_path),
                    str(mapping_path),
                    OCCURRENCE_VALIDATION_ENCODING,
                ],
                horizon=1,
            )
            return control.solve()


if __name__ == "__main__":
    unittest.main()
