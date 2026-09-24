import hashlib
import io
import stat
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

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


def _archive_with(binary):
    archive = io.BytesIO()
    with tarfile.open(fileobj=archive, mode="w:gz") as bundle:
        member = tarfile.TarInfo(setup.PLASP_ARCHIVE_MEMBER)
        member.size = len(binary)
        bundle.addfile(member, io.BytesIO(binary))
    return archive.getvalue()


class PlaspInstallerTests(unittest.TestCase):
    def test_installs_a_checksum_verified_executable(self):
        binary = b"official plasp binary"
        archive = _archive_with(binary)
        download = Mock(return_value=archive)

        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory, "bin", "plasp")
            with (
                patch.object(setup, "PLASP_BIN", destination),
                patch.object(setup, "PLASP_BINARY_SHA256", hashlib.sha256(binary).hexdigest()),
                patch.object(setup, "_download_plasp", download),
                patch.object(setup.platform, "machine", return_value="x86_64"),
                patch.object(setup.sys, "platform", "linux"),
            ):
                setup._install_plasp()

            self.assertEqual(destination.read_bytes(), binary)
            self.assertTrue(destination.stat().st_mode & stat.S_IXUSR)

    def test_rejects_a_binary_with_the_wrong_checksum(self):
        archive = _archive_with(b"unexpected")

        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory, "bin", "plasp")
            with (
                patch.object(setup, "PLASP_BIN", destination),
                patch.object(setup, "PLASP_BINARY_SHA256", "0" * 64),
                patch.object(setup, "_download_plasp", return_value=archive),
                patch.object(setup.platform, "machine", return_value="x86_64"),
                patch.object(setup.sys, "platform", "linux"),
            ):
                with self.assertRaisesRegex(RuntimeError, "binary checksum mismatch"):
                    setup._install_plasp()

            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
