import hashlib
import io
import stat
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import install_plasp as installer


def _archive_with(binary):
    archive = io.BytesIO()
    with tarfile.open(fileobj=archive, mode="w:gz") as bundle:
        member = tarfile.TarInfo(installer.PLASP_ARCHIVE_MEMBER)
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
                patch.object(installer, "PLASP_BIN", destination),
                patch.object(installer, "PLASP_ARCHIVE_SHA256", hashlib.sha256(archive).hexdigest()),
                patch.object(installer, "PLASP_BINARY_SHA256", hashlib.sha256(binary).hexdigest()),
                patch.object(installer, "_download_archive", download),
                patch.object(installer.platform, "machine", return_value="x86_64"),
                patch.object(installer.sys, "platform", "linux"),
            ):
                installer.install_plasp()

            self.assertEqual(destination.read_bytes(), binary)
            self.assertTrue(destination.stat().st_mode & stat.S_IXUSR)
            download.assert_called_once_with()

    def test_rejects_an_archive_with_the_wrong_checksum(self):
        archive = _archive_with(b"unexpected")

        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory, "bin", "plasp")
            with (
                patch.object(installer, "PLASP_BIN", destination),
                patch.object(installer, "PLASP_ARCHIVE_SHA256", "0" * 64),
                patch.object(installer, "_download_archive", return_value=archive),
                patch.object(installer.platform, "machine", return_value="x86_64"),
                patch.object(installer.sys, "platform", "linux"),
            ):
                with self.assertRaisesRegex(RuntimeError, "archive checksum mismatch"):
                    installer.install_plasp()

            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
