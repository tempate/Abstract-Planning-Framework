#!/usr/bin/env python3
"""Install the pinned official plasp binary used by the planning pipeline."""

import hashlib
import io
import os
import platform
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

PLASP_VERSION = "3.1.1"
PLASP_URL = (
    f"https://github.com/potassco/plasp/releases/download/v{PLASP_VERSION}/plasp-{PLASP_VERSION}-linux-x86_64.tar.gz"
)
PLASP_ARCHIVE_SHA256 = "43f030559ac855d9a694350f44e6aec5a4d20bf34ce6af20fe2b7797267e8569"
PLASP_BINARY_SHA256 = "9a709543070b7fc30090735b02c7084b190af007de32ae4317ba5e432c250dc8"
PLASP_ARCHIVE_MEMBER = f"plasp-{PLASP_VERSION}/plasp"
PLASP_BIN = Path(__file__).resolve().parents[1] / "lib" / "plasp" / "bin" / "plasp"


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _read_binary(path):
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return None


def _download_archive():
    with urllib.request.urlopen(PLASP_URL) as response:
        return response.read()


def _extract_binary(archive):
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
        member = bundle.getmember(PLASP_ARCHIVE_MEMBER)
        source = bundle.extractfile(member)
        if source is None:
            raise RuntimeError(f"plasp archive member is not a regular file: {PLASP_ARCHIVE_MEMBER}")
        return source.read()


def install_plasp():
    if sys.platform != "linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("the pinned plasp binary supports Linux x86-64 only")

    installed = _read_binary(PLASP_BIN)
    if installed is not None and _sha256(installed) == PLASP_BINARY_SHA256:
        print(f"plasp {PLASP_VERSION} is already installed at {PLASP_BIN}")
        return

    archive = _download_archive()
    archive_digest = _sha256(archive)
    if archive_digest != PLASP_ARCHIVE_SHA256:
        raise RuntimeError(
            f"plasp archive checksum mismatch: expected {PLASP_ARCHIVE_SHA256}, received {archive_digest}"
        )

    binary = _extract_binary(archive)
    binary_digest = _sha256(binary)
    if binary_digest != PLASP_BINARY_SHA256:
        raise RuntimeError(f"plasp binary checksum mismatch: expected {PLASP_BINARY_SHA256}, received {binary_digest}")

    PLASP_BIN.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".plasp-", dir=PLASP_BIN.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as destination:
            destination.write(binary)
        temporary_path.chmod(0o755)
        temporary_path.replace(PLASP_BIN)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise

    print(f"installed plasp {PLASP_VERSION} at {PLASP_BIN}")


if __name__ == "__main__":
    install_plasp()
