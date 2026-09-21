"""Fast Downward integration for translating PDDL tasks to SAS and searching them."""

import os
import subprocess
import sys

from core.integrations.paths import FAST_DOWNWARD_SCRIPT
from core.outcomes import IntegrationError, OutOfMemoryError, UnsolvableTaskError
from core.plan import PlanAction

# Fast Downward's exit codes, documented at
# https://www.fast-downward.org/latest/documentation/exit-codes/.
_SUCCESS = 0
_TRANSLATE_UNSOLVABLE = 10
_SEARCH_UNSOLVABLE = 11
# The translator and the search report running out of memory themselves. The
# driver reports a component killed by a signal as 256 minus the signal, so 247
# is a SIGKILL, which on these tasks is the kernel reclaiming the memory the
# search asked for.
_OUT_OF_MEMORY = (20, 22, 24, 247)
# Reaching an unsolvable task through --translate alone is not a failure to the
# driver, which exits 0 after the translator has written a dummy task in place
# of the real one. The verdict only reaches us through what it printed.
_UNSOLVABLE_MARKER = "Generating unsolvable task"

SEARCH = "astar(blind())"
LAMA_FIRST = "lama-first"


def pddl_to_sas(base_dir, domain_path, problem_path, label):
    """Translate a concrete or abstract PDDL task and return its SAS file."""
    os.makedirs(base_dir, exist_ok=True)
    sas_path = os.path.join(base_dir, "output.sas")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        sas_path,
        "--keep-sas-file",
        "--translate",
        os.fspath(domain_path),
        os.fspath(problem_path),
    ]
    completed_process = subprocess.run(command, capture_output=True, text=True)

    if completed_process.returncode == _TRANSLATE_UNSOLVABLE or _UNSOLVABLE_MARKER in completed_process.stdout:
        raise UnsolvableTaskError(f"Fast Downward ({label}) proved the task unsolvable while translating")

    if completed_process.returncode != _SUCCESS:
        _raise_failure(completed_process, label)

    return sas_path


def has_plan(base_dir, domain_path, problem_path, label):
    """Translate and search one PDDL task, reporting only whether it has a plan."""
    completed_process, _ = _search(base_dir, domain_path, problem_path, label, search=("--search", SEARCH))

    if completed_process.returncode == _SUCCESS:
        return True
    if completed_process.returncode in (_TRANSLATE_UNSOLVABLE, _SEARCH_UNSOLVABLE):
        return False

    _raise_failure(completed_process, label)


def find_plan(base_dir, domain_path, problem_path, label):
    """Search one PDDL task with LAMA-first, returning its plan or None."""
    completed_process, plan_path = _search(base_dir, domain_path, problem_path, label, driver=("--alias", LAMA_FIRST))

    if completed_process.returncode == _SUCCESS:
        return _read_plan(plan_path)
    if completed_process.returncode in (_TRANSLATE_UNSOLVABLE, _SEARCH_UNSOLVABLE):
        return None

    _raise_failure(completed_process, label)


def _search(base_dir, domain_path, problem_path, label, driver=(), search=()):
    """Translate and search one task, returning the process and its plan file.

    The driver reads its own options before the task and passes on whatever
    follows it, so an alias and a search configuration go on opposite sides.
    """
    os.makedirs(base_dir, exist_ok=True)
    plan_path = os.path.join(base_dir, f"{label}.plan")
    # Both paths have to be named. Left to itself the driver writes and reads
    # output.sas in the working directory, which every task of a cluster run
    # shares, so concurrent tasks truncate and delete each other's file.
    sas_path = os.path.join(base_dir, f"{label}.sas")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        sas_path,
        "--plan-file",
        plan_path,
        *driver,
        os.fspath(domain_path),
        os.fspath(problem_path),
        *search,
    ]
    return subprocess.run(command, capture_output=True, text=True), plan_path


def parse_plan_actions(plan):
    """Convert the lines of a plan file into chronological plan actions."""
    actions = []
    for time_step, line in enumerate(plan):
        name, *args = line.strip().strip("()").split()
        actions.append(PlanAction(name=name, args=tuple(args), time_step=time_step))
    return tuple(actions)


def _read_plan(plan_path):
    """Read the actions of a plan file, which ends in a comment naming its cost."""
    with open(plan_path, encoding="utf-8") as plan_file:
        return [line.strip() for line in plan_file if line.strip() and not line.startswith(";")]


def _raise_failure(completed_process, label):
    """Report what Fast Downward said, as memory when that is what ran out."""
    diagnostics = "\n".join(
        output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
    )
    message = f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
    if completed_process.returncode in _OUT_OF_MEMORY:
        raise OutOfMemoryError(message)
    raise IntegrationError(message)
