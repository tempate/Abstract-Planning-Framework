#!/usr/bin/env python3
"""Install the pinned official plasp binary used by the planning pipeline."""

import hashlib
import io
import platform
import sys
import tarfile
import urllib.request
from pathlib import Path

PLASP_VERSION = "3.1.1"
PLASP_URL = (
    f"https://github.com/potassco/plasp/releases/download/v{PLASP_VERSION}/plasp-{PLASP_VERSION}-linux-x86_64.tar.gz"
)
PLASP_BINARY_SHA256 = "9a709543070b7fc30090735b02c7084b190af007de32ae4317ba5e432c250dc8"
PLASP_ARCHIVE_MEMBER = f"plasp-{PLASP_VERSION}/plasp"
PLASP_BIN = Path(__file__).resolve().parents[1] / "lib" / "plasp" / "bin" / "plasp"


def _download_archive():
    with urllib.request.urlopen(PLASP_URL) as response:
        return response.read()


def _extract_binary(archive):
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
        source = bundle.extractfile(PLASP_ARCHIVE_MEMBER)
        if source is None:
            raise RuntimeError(f"plasp archive member is not a regular file: {PLASP_ARCHIVE_MEMBER}")
        return source.read()


def _is_installed():
    """Check whether the pinned binary is already in place."""
    try:
        return hashlib.sha256(PLASP_BIN.read_bytes()).hexdigest() == PLASP_BINARY_SHA256
    except FileNotFoundError:
        return False


def install_plasp():
    if sys.platform != "linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("the pinned plasp binary supports Linux x86-64 only")

    if _is_installed():
        print(f"plasp {PLASP_VERSION} is already installed at {PLASP_BIN}")
        return

    binary = _extract_binary(_download_archive())
    digest = hashlib.sha256(binary).hexdigest()
    if digest != PLASP_BINARY_SHA256:
        raise RuntimeError(f"plasp binary checksum mismatch: expected {PLASP_BINARY_SHA256}, received {digest}")

    PLASP_BIN.parent.mkdir(parents=True, exist_ok=True)
    PLASP_BIN.write_bytes(binary)
    PLASP_BIN.chmod(0o755)

    print(f"installed plasp {PLASP_VERSION} at {PLASP_BIN}")


if __name__ == "__main__":
    install_plasp()
