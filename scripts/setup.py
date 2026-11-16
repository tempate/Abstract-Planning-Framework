#!/usr/bin/env python3
"""Build everything the planner needs that pip does not install."""

import hashlib
import io
import os
import platform
import shutil
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
NUMERIC_DOWNWARD = ROOT / "lib" / "numeric-fast-downward"
NUMERIC_DOWNWARD_PATCH = ROOT / "lib" / "numeric-fast-downward.patch"
NUMERIC_DOWNWARD_BUILD = NUMERIC_DOWNWARD / "builds" / "release64"
POWERLIFTED_SEARCH = ROOT / "lib" / "powerlifted" / "builds" / "release" / "search" / "search"
CPDDL_DIR = ROOT / "lib" / "cpddl"
CPDDL_BIN = CPDDL_DIR / "bin" / "pddl-tool"

# Each of these fails silently at run time rather than at setup time: a missing
# pybliss kills every abstract run in symmetry discovery, a missing Fast
# Downward build exits 36, a missing plasp cannot translate anything, and a
# missing numeric Fast Downward kills every resources-track job in detection.
ARTIFACTS = {
    "pybliss extension": PYBLISS_MODULE,
    "Fast Downward release build": DOWNWARD_BUILD,
    "plasp binary": PLASP_BIN,
    "numeric Fast Downward release64 build": NUMERIC_DOWNWARD_BUILD,
    "Powerlifted release build": POWERLIFTED_SEARCH,
    "cpddl binary": CPDDL_BIN,
}


def main():
    _initialize_submodules()
    _build_pybliss()
    _build_fast_downward()
    _build_numeric_fast_downward()
    _build_powerlifted()
    _install_plasp()
    _build_cpddl()
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


def _build_numeric_fast_downward():
    """Build numeric Fast Downward for resource detection, with the patch that lets it use Clp instead of CPLEX."""
    print("== numeric Fast Downward")
    if NUMERIC_DOWNWARD_BUILD.is_dir():
        print(f"already built at {NUMERIC_DOWNWARD_BUILD}")
        return

    patch_is_applied = subprocess.run(
        ["git", "apply", "--reverse", "--check", str(NUMERIC_DOWNWARD_PATCH)], cwd=NUMERIC_DOWNWARD
    )
    if patch_is_applied.returncode != 0:
        _run(["git", "apply", str(NUMERIC_DOWNWARD_PATCH)], cwd=NUMERIC_DOWNWARD)
    _run([sys.executable, "build.py", "release64"], cwd=NUMERIC_DOWNWARD)


def _build_powerlifted():
    print("== Powerlifted")
    if POWERLIFTED_SEARCH.exists():
        print(f"already built at {POWERLIFTED_SEARCH}")
        return

    # Compilers that default to C++20 lack the allocator rebind Powerlifted uses, and
    # GCC 16 reports a spurious overflow in it that Powerlifted's -Werror makes fatal.
    flags = {**os.environ, "CXXFLAGS": "-std=c++17 -Wno-error=stringop-overflow"}
    _run([sys.executable, "build.py"], cwd=ROOT / "lib" / "powerlifted", env=flags)


def _build_cpddl():
    print("== cpddl")
    if CPDDL_BIN.exists():
        print(f"already built at {CPDDL_BIN}")
        return

    # The template's defaults build without the optional LP solvers, which rnd-g does not need.
    shutil.copyfile(CPDDL_DIR / "Makefile.config.tpl", CPDDL_DIR / "Makefile.config")
    _run(["make", "bin"], cwd=CPDDL_DIR)


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
