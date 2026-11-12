#!/usr/bin/env python3
"""Build everything the planner needs that pip does not install."""

import hashlib
import io
import os
import platform
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLASP_VERSION = "3.1.1"
PLASP_URL = (
    f"https://github.com/potassco/plasp/releases/download/v{PLASP_VERSION}/plasp-{PLASP_VERSION}-linux-x86_64.tar.gz"
)
PLASP_BINARY_SHA256 = "9a709543070b7fc30090735b02c7084b190af007de32ae4317ba5e432c250dc8"
PLASP_ARCHIVE_MEMBER = f"plasp-{PLASP_VERSION}/plasp"
PLASP_BIN = ROOT / "lib" / "plasp" / "bin" / "plasp"
PYBLISS_DIR = ROOT / "lib" / "pddl-symmetries" / "src" / "translate" / "pybliss-0.73"
PYBLISS_MODULE = PYBLISS_DIR / "pybind11_blissmodule.so"
DOWNWARD_BUILD = ROOT / "lib" / "downward" / "builds" / "release"
STRUCTURAL_SYMMETRIES_BUILD = ROOT / "lib" / "structural-symmetries" / "builds" / "release"
# The fork dates from 2023. CMake 4 refuses its minimum version and GCC 14 its bundled
# optional.hh, and older versions of both ignore these two settings.
STRUCTURAL_SYMMETRIES_BUILD_ENV = {"CMAKE_POLICY_VERSION_MINIMUM": "3.5", "CXXFLAGS": "-Wno-template-body"}
MS_UNSAT_URL = (
    "https://github.com/AI-Planning/unsolve-ipc-2016/raw/"
    "97214352c59130a2d7cfdae0e7d696df6e2ac203/planners/team4v1/source.tar.gz"
)
MS_UNSAT_ARCHIVE_SHA256 = "009566c94327e3959e6c0cfc2b3627377cee351d974932969973c73628bd1356"
MS_UNSAT_ARCHIVE_ROOT = "MS-unsat/src/"
# Only the translator's Python and the two statically linked binaries are
# needed, so the sources the archive also ships are left out.
MS_UNSAT_MEMBERS = ("translate/", "preprocess/preprocess", "search/downward-release")
MS_UNSAT_DIR = ROOT / "lib" / "ms-unsat" / "src"
MS_UNSAT_SEARCH = MS_UNSAT_DIR / "search" / "downward-release"

# Each of these fails silently at run time rather than at setup time: a missing
# pybliss kills every abstract run in symmetry discovery, a missing Fast
# Downward build exits 36, and a missing plasp cannot translate anything.
ARTIFACTS = {
    "pybliss extension": PYBLISS_MODULE,
    "Fast Downward release build": DOWNWARD_BUILD,
    "structural symmetries release build": STRUCTURAL_SYMMETRIES_BUILD,
    "plasp binary": PLASP_BIN,
    "MS-unsat search": MS_UNSAT_SEARCH,
}


def main():
    _initialize_submodules()
    _build_pybliss()
    _build_fast_downward()
    _build_structural_symmetries()
    _install_plasp()
    _install_ms_unsat()
    _verify()


def _initialize_submodules():
    print("== submodules")
    _run(["git", "submodule", "update", "--init", "--recursive"], cwd=ROOT)


def _build_pybliss():
    print("== pybliss extension")
    if PYBLISS_MODULE.exists():
        print(f"already built at {PYBLISS_MODULE}")
        return

    _run(["make", "-C", str(PYBLISS_DIR)], cwd=ROOT)


def _build_fast_downward():
    print("== Fast Downward")
    if DOWNWARD_BUILD.is_dir():
        print(f"already built at {DOWNWARD_BUILD}")
        return

    _run([sys.executable, "build.py", "release"], cwd=ROOT / "lib" / "downward")


def _build_structural_symmetries():
    print("== Fast Downward with structural symmetries")
    if STRUCTURAL_SYMMETRIES_BUILD.is_dir():
        print(f"already built at {STRUCTURAL_SYMMETRIES_BUILD}")
        return

    environment = {**os.environ, **STRUCTURAL_SYMMETRIES_BUILD_ENV}
    _run([sys.executable, "build.py", "release"], cwd=ROOT / "lib" / "structural-symmetries", env=environment)


def _install_plasp():
    """Install the pinned official plasp binary, checking its checksum."""
    print("== plasp")
    if sys.platform != "linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("the pinned plasp binary supports Linux x86-64 only")

    if _plasp_is_installed():
        print(f"plasp {PLASP_VERSION} is already installed at {PLASP_BIN}")
        return

    binary = _extract_plasp(_download_plasp())
    digest = hashlib.sha256(binary).hexdigest()
    if digest != PLASP_BINARY_SHA256:
        raise RuntimeError(f"plasp binary checksum mismatch: expected {PLASP_BINARY_SHA256}, received {digest}")

    PLASP_BIN.parent.mkdir(parents=True, exist_ok=True)
    PLASP_BIN.write_bytes(binary)
    PLASP_BIN.chmod(0o755)
    print(f"installed plasp {PLASP_VERSION} at {PLASP_BIN}")


def _download_plasp():
    with urllib.request.urlopen(PLASP_URL) as response:
        return response.read()


def _extract_plasp(archive):
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
        source = bundle.extractfile(PLASP_ARCHIVE_MEMBER)
        if source is None:
            raise RuntimeError(f"plasp archive member is not a regular file: {PLASP_ARCHIVE_MEMBER}")
        return source.read()


def _plasp_is_installed():
    try:
        return hashlib.sha256(PLASP_BIN.read_bytes()).hexdigest() == PLASP_BINARY_SHA256
    except FileNotFoundError:
        return False


def _install_ms_unsat():
    """Install MS-unsat from the pinned competition archive, checking its checksum."""
    print("== MS-unsat")
    if MS_UNSAT_SEARCH.exists():
        print(f"already installed at {MS_UNSAT_DIR}")
        return

    with urllib.request.urlopen(MS_UNSAT_URL) as response:
        archive = response.read()

    digest = hashlib.sha256(archive).hexdigest()
    if digest != MS_UNSAT_ARCHIVE_SHA256:
        raise RuntimeError(f"MS-unsat archive checksum mismatch: expected {MS_UNSAT_ARCHIVE_SHA256}, received {digest}")

    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
        for member in bundle.getmembers():
            relative = member.name.removeprefix(MS_UNSAT_ARCHIVE_ROOT)
            if member.isfile() and relative.startswith(MS_UNSAT_MEMBERS) and not relative.endswith(".pyc"):
                member.name = relative
                bundle.extract(member, MS_UNSAT_DIR, filter="data")

    # The translator predates Python 3.8, which removed time.clock.
    invariant_finder = MS_UNSAT_DIR / "translate" / "invariant_finder.py"
    invariant_finder.write_text(invariant_finder.read_text().replace("time.clock()", "time.process_time()"))
    print(f"installed MS-unsat at {MS_UNSAT_DIR}")


def _verify():
    print("== checking what the planner needs")
    missing = []
    for name, path in ARTIFACTS.items():
        if path.exists():
            print(f"found {name}")
        else:
            missing.append(f"{name} ({path})")

    if missing:
        raise SystemExit("missing after setup:\n  " + "\n  ".join(missing))

    print("setup complete")


def _run(command, cwd, env=None):
    completed = subprocess.run(command, cwd=cwd, env=env)
    if completed.returncode != 0:
        raise SystemExit(f"{command[0]} failed with exit code {completed.returncode}")


if __name__ == "__main__":
    main()
