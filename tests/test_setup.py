import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import setup


class SetupVerificationTests(unittest.TestCase):
    def test_a_missing_artifact_stops_setup_and_is_named(self):
        with tempfile.TemporaryDirectory() as directory:
            present = Path(directory) / "present"
            present.touch()
            artifacts = {"present thing": present, "absent thing": Path(directory) / "absent"}

            with patch.object(setup, "ARTIFACTS", artifacts):
                with self.assertRaises(SystemExit) as raised:
                    setup._verify()

        self.assertIn("absent thing", str(raised.exception))
        self.assertNotIn("present thing", str(raised.exception))

    def test_setup_passes_when_every_artifact_is_there(self):
        with tempfile.TemporaryDirectory() as directory:
            present = Path(directory) / "present"
            present.touch()

            with patch.object(setup, "ARTIFACTS", {"present thing": present}):
                setup._verify()


if __name__ == "__main__":
    unittest.main()
