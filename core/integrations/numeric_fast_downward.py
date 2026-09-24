"""numeric-fast-downward integration for detecting resource variables."""

import os
import re
import signal
import subprocess
import sys
from dataclasses import dataclass

from core.integrations.paths import NUMERIC_FAST_DOWNWARD_BIN, NUMERIC_FAST_DOWNWARD_SCRIPT
from core.outcomes import IntegrationError

BUILD = "release64"
DETECTION_SEARCH = "resource_detection()"
# The budget symmetry discovery gets, so neither source can spend a whole job finding a class.
DETECTION_TIME_LIMIT = 300

# The engine classifies the variables, writes its reformulated task and leaves
# through the no-solution path, so its exit code never reports success. These
# two lines do.
_SUMMARY = re.compile(r"^Found (\d+)/(\d+) resource variables$", re.MULTILINE)
_RESOURCE = re.compile(r"^\d+ (\S+) resource\s*$", re.MULTILINE)


@dataclass(frozen=True)
class ResourceVariable:
    """One SAS variable the detector calls a resource, and the objects it ranges over."""

    name: str
    objects: tuple[str, ...]


def detect_resources(base_dir, domain_path, problem_path, timeout=DETECTION_TIME_LIMIT):
    """Return the resource variables of one PDDL task, widest first."""
    if not os.path.exists(NUMERIC_FAST_DOWNWARD_BIN):
        raise IntegrationError(
            f"numeric-fast-downward binary not found: {NUMERIC_FAST_DOWNWARD_BIN}; "
            "apply lib/numeric-fast-downward.patch and run ./build.py release64 there"
        )

    os.makedirs(base_dir, exist_ok=True)
    # The engine writes output.sas and four PDDL files under fixed names in the
    # working directory, so it gets a directory of its own -- which is why the
    # task has to be named absolutely, the caller's relative paths being
    # meaningless from there.
    command = [
        sys.executable,
        NUMERIC_FAST_DOWNWARD_SCRIPT,
        "--build",
        BUILD,
        os.path.abspath(domain_path),
        os.path.abspath(problem_path),
        "--search",
        DETECTION_SEARCH,
    ]
    # The driver starts translate, preprocess and search as children of its own,
    # so it gets a session of its own, and a timeout or an interrupted caller
    # takes all of them down rather than leaving them holding memory.
    process = subprocess.Popen(
        command, cwd=base_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except BaseException as error:
        _kill_process_group(process)
        if isinstance(error, subprocess.TimeoutExpired):
            raise IntegrationError(f"Resource detection timed out after {timeout}s") from error
        raise

    if _SUMMARY.search(stdout) is None:
        diagnostics = "\n".join(output.strip() for output in (stdout, stderr) if output.strip())
        raise IntegrationError(f"Resource detection reported nothing:\n{diagnostics}")

    values = read_sas_variables(os.path.join(base_dir, "output.sas"))
    return parse_resources(stdout, values)


def _kill_process_group(process):
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        process.kill()
    process.communicate()


def parse_resources(detector_output, values):
    """Read the detector's classification, keeping the variables that carry objects."""
    resources = []
    for name in _RESOURCE.findall(detector_output):
        objects = varying_objects(values.get(name, ()))
        if objects:
            resources.append(ResourceVariable(name, objects))

    # Widest first, so the caller can take the longest ladder without re-sorting.
    resources.sort(key=lambda resource: (-len(resource.objects), resource.name))
    return tuple(resources)


def read_sas_variables(sas_path):
    """Map each SAS variable name to the values it can take."""
    with open(sas_path, encoding="utf-8") as sas_file:
        lines = [line.rstrip("\n") for line in sas_file]

    variables = {}
    index = 0
    while index < len(lines):
        if lines[index] != "begin_variable":
            index += 1
            continue
        name = lines[index + 1]
        count = int(lines[index + 3])
        variables[name] = tuple(lines[index + 4 : index + 4 + count])
        index += 4 + count
    return variables


def varying_objects(values):
    """Return the objects that tell one variable's values apart.

    A resource is one predicate over a fixed subject and a ladder of values, as
    ``fuel(t0, level0) ... fuel(t0, level80)`` is, so the objects wanted are the
    ones in the argument positions that differ.  Anything else -- a variable
    whose values mix predicates, or the ``new-axiom@`` variable the translator
    adds, which has no arguments at all -- yields nothing and is dropped.
    """
    atoms = [fields for fields in (_atom_fields(value) for value in values) if fields is not None]
    if len(atoms) < 2:
        return ()

    predicates = {predicate for predicate, _ in atoms}
    widths = {len(arguments) for _, arguments in atoms}
    if len(predicates) != 1 or len(widths) != 1:
        return ()

    objects = set()
    for position in range(widths.pop()):
        column = {arguments[position] for _, arguments in atoms}
        if len(column) > 1:
            objects |= column
    return tuple(sorted(objects))


def _atom_fields(value):
    """Split ``Atom fuel(t0, level0)`` into its predicate and arguments, or None."""
    if not value.startswith("Atom "):
        return None
    body = value[len("Atom ") :].strip()
    if not body.endswith(")") or "(" not in body:
        return None
    predicate, _, arguments = body[:-1].partition("(")
    return predicate.strip(), tuple(argument.strip() for argument in arguments.split(",") if argument.strip())
