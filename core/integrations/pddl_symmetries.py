"""PDDL Symmetries subprocess integration."""

import ast
import re
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from core.paths import PDDL_SYMMETRIES_TRANSLATOR


class PddlSymmetriesError(RuntimeError):
    """Raised when PDDL Symmetries cannot produce object classes."""


def find_symmetric_object_sets(
    domain_path: str | Path,
    problem_path: str | Path,
    time_limit: int = 300,
    translator_path: str | Path = PDDL_SYMMETRIES_TRANSLATOR,
) -> list[list[str]]:
    """Run PDDL Symmetries and return its non-trivial object classes."""
    if time_limit < 1:
        raise ValueError("PDDL Symmetries time limit must be positive")
    translator = Path(translator_path).resolve()
    if not translator.is_file():
        raise PddlSymmetriesError(
            "PDDL Symmetries is not initialized. Run "
            "'git submodule update --init --recursive'."
        )
    domain = Path(domain_path).resolve()
    problem = Path(problem_path).resolve()
    for label, path in (("domain", domain), ("problem", problem)):
        if not path.is_file():
            raise PddlSymmetriesError(f"PDDL {label} file does not exist: {path}")

    command = [
        sys.executable,
        str(translator),
        str(domain),
        str(problem),
        "--compute-symmetries",
        "--only-object-symmetries",
        "--compute-symmetric-object-sets-from-symmetries",
        "--bliss-time-limit", str(time_limit),
        "--stop-after-computing-symmetries",
    ]
    try:
        with TemporaryDirectory(prefix="pddl-symmetries-") as working_directory:
            result = subprocess.run(
                command,
                cwd=working_directory,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=time_limit + 30,
            )
    except subprocess.TimeoutExpired as error:
        raise PddlSymmetriesError(
            f"PDDL Symmetries exceeded its {time_limit}-second limit"
        ) from error
    except OSError as error:
        raise PddlSymmetriesError(
            f"Could not run PDDL Symmetries: {error}"
        ) from error
    if result.returncode != 0:
        diagnostics = "\n".join(
            value.strip()
            for value in (result.stdout, result.stderr)
            if value.strip()
        )
        suffix = f":\n{diagnostics}" if diagnostics else ""
        raise PddlSymmetriesError(
            f"PDDL Symmetries failed with exit code {result.returncode}{suffix}"
        )

    match = re.search(
        r"^\s*Non-trivial symmetric object sets:\s*(.+)$",
        result.stdout,
        flags=re.MULTILINE,
    )
    if not match:
        raise PddlSymmetriesError(
            "PDDL Symmetries did not report symmetric object sets"
        )
    try:
        classes = ast.literal_eval(match.group(1))
    except (SyntaxError, ValueError) as error:
        raise PddlSymmetriesError(
            "PDDL Symmetries returned malformed object sets"
        ) from error
    if not isinstance(classes, list) or not all(
        isinstance(group, list)
        and all(isinstance(item, str) for item in group)
        for group in classes
    ):
        raise PddlSymmetriesError(
            "PDDL Symmetries returned an invalid object-set value"
        )
    return classes
