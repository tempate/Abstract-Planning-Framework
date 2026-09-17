#!/usr/bin/env python3
"""Build everything the planner needs that pip does not install."""

import subprocess
import sys
from pathlib import Path

from scripts.install_plasp import PLASP_BIN, install_plasp

ROOT = Path(__file__).resolve().parents[1]
PYBLISS_DIR = ROOT / "lib" / "pddl-symmetries" / "src" / "translate" / "pybliss-0.73"
PYBLISS_MODULE = PYBLISS_DIR / "pybind11_blissmodule.so"
DOWNWARD_BUILD = ROOT / "lib" / "downward" / "builds" / "release"

# Each of these fails silently at run time rather than at setup time: a missing
# pybliss kills every abstract run in symmetry discovery, a missing Fast
# Downward build exits 36, and a missing plasp cannot translate anything.
ARTIFACTS = {
    "pybliss extension": PYBLISS_MODULE,
    "Fast Downward release build": DOWNWARD_BUILD,
    "plasp binary": PLASP_BIN,
}


def main():
    _initialize_submodules()
    _build_pybliss()
    _build_fast_downward()
    install_plasp()
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


def _run(command, cwd):
    completed = subprocess.run(command, cwd=cwd)
    if completed.returncode != 0:
        raise SystemExit(f"{command[0]} failed with exit code {completed.returncode}")


if __name__ == "__main__":
    main()
