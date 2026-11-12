"""PDDL Symmetries subprocess integration."""

import ast
import os
import re
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from core.integrations.paths import PDDL_SYMMETRIES_TRANSLATOR
from core.utilities.outcomes import IntegrationError, SymmetryTimeoutError, UnsolvableTaskError, tool_failure

# The exit code Fast Downward's translator, which PDDL Symmetries extends, gives when memory runs out.
_TRANSLATE_OUT_OF_MEMORY = 20


def find_symmetric_object_sets(domain_path, problem_path, time_limit=300, before_grounding=False):
    """Run PDDL Symmetries and return its non-trivial object classes.

    Before grounding, the classes come from the lifted task alone: a task too large
    to ground still gets them, but an unreachable goal is no longer detected.
    """
    if time_limit < 1:
        raise ValueError("PDDL Symmetries time limit must be positive")
    command = _translator_command(domain_path, problem_path, time_limit)
    if before_grounding:
        command.append("--symmetries-before-grounding")
    return _parse_object_sets(_run_translator(command, time_limit))


def _translator_command(domain_path, problem_path, time_limit):
    """Build the translator invocation, checking that every input exists."""
    translator = Path(PDDL_SYMMETRIES_TRANSLATOR).resolve()
    if not translator.is_file():
        raise IntegrationError("PDDL Symmetries is not initialized. Run 'git submodule update --init --recursive'.")
    domain = Path(domain_path).resolve()
    problem = Path(problem_path).resolve()
    for label, path in (("domain", domain), ("problem", problem)):
        if not path.is_file():
            raise IntegrationError(f"PDDL {label} file does not exist: {path}")

    return [
        sys.executable,
        str(translator),
        str(domain),
        str(problem),
        "--compute-symmetries",
        "--only-object-symmetries",
        "--compute-symmetric-object-sets-from-symmetries",
        "--bliss-time-limit",
        str(time_limit),
        "--stop-after-computing-symmetries",
    ]


def _run_translator(command, time_limit):
    """Run the translator in a scratch directory and return its standard output."""
    try:
        with TemporaryDirectory(prefix="pddl-symmetries-") as working_directory:
            # The classes change with the string-hash seed, so a fixed seed makes them repeatable.
            result = subprocess.run(
                command,
                cwd=working_directory,
                env={**os.environ, "PYTHONHASHSEED": "0"},
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=time_limit + 30,
            )
    except subprocess.TimeoutExpired as error:
        raise SymmetryTimeoutError(f"PDDL Symmetries exceeded its {time_limit}-second limit") from error
    except OSError as error:
        raise IntegrationError(f"Could not run PDDL Symmetries: {error}") from error
    if "No relaxed solution" in result.stdout + result.stderr:
        raise UnsolvableTaskError("PDDL Symmetries reports that the task has no relaxed solution")
    if result.returncode != 0:
        raise tool_failure("PDDL Symmetries", result, (_TRANSLATE_OUT_OF_MEMORY,))
    return result.stdout


def _parse_object_sets(stdout):
    """Read the object classes the translator reported."""
    match = re.search(r"^\s*Non-trivial symmetric object sets:\s*(.+)$", stdout, flags=re.MULTILINE)
    if not match:
        raise IntegrationError("PDDL Symmetries did not report symmetric object sets")
    try:
        classes = ast.literal_eval(match.group(1))
    except (SyntaxError, ValueError) as error:
        raise IntegrationError("PDDL Symmetries returned malformed object sets") from error
    if not isinstance(classes, list):
        raise IntegrationError(f"PDDL Symmetries returned object sets that are not a list: {classes!r}")
    for group in classes:
        if not isinstance(group, list) or not all(isinstance(item, str) for item in group):
            raise IntegrationError(f"PDDL Symmetries returned an invalid object set: {group!r}")
    return classes
