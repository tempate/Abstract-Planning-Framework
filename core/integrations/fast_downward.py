"""Fast Downward integration for translating PDDL tasks to SAS and searching them."""

import os
import subprocess
import sys
from dataclasses import dataclass

from core.integrations.paths import FAST_DOWNWARD_SCRIPT
from core.outcomes import IntegrationError, OutOfMemoryError, UnsolvableTaskError
from core.plan import PlanAction

# Fast Downward's exit codes, documented at
# https://www.fast-downward.org/latest/documentation/exit-codes/.
_SUCCESS = 0
_TRANSLATE_UNSOLVABLE = 10
_SEARCH_UNSOLVABLE = 11
_OUT_OF_MEMORY = (20, 22, 24, 247)
_UNSOLVABLE_MARKER = "Generating unsolvable task"


@dataclass(frozen=True)
class Search:
    """A Fast Downward search, as the options the driver reads before the task and after it."""

    driver: tuple[str, ...] = ()
    options: tuple[str, ...] = ()


# Satisficing
LAMA = Search(driver=("--alias", "lama-first"))
# Optimal
LMCUT = Search(options=("--search", "astar(eval_modify_costs(lmcut(),cost_type=one),cost_type=one)"))


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


def find_plan(base_dir, domain_path, problem_path, label, search):
    """Translate and search one PDDL task, returning its plan or None."""
    os.makedirs(base_dir, exist_ok=True)
    plan_path = os.path.join(base_dir, f"{label}.plan")
    sas_path = os.path.join(base_dir, f"{label}.sas")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        sas_path,
        "--plan-file",
        plan_path,
        *search.driver,
        os.fspath(domain_path),
        os.fspath(problem_path),
        *search.options,
    ]
    return _find_plan(command, label, plan_path)


def find_sas_plan(base_dir, sas_path, label, search):
    """Search an already translated task, returning its plan or None."""
    plan_path = os.path.join(base_dir, f"{label}.plan")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--plan-file",
        plan_path,
        *search.driver,
        sas_path,
        *search.options,
    ]
    return _find_plan(command, label, plan_path)


def parse_plan_actions(plan):
    """Convert the lines of a plan file into chronological plan actions."""
    actions = []
    for time_step, line in enumerate(plan):
        name, *args = line.strip().strip("()").split()
        action = PlanAction(name=name, args=tuple(args), time_step=time_step)
        actions.append(action)
    return tuple(actions)


def _find_plan(command, label, plan_path):
    out = subprocess.run(command, capture_output=True, text=True)

    if out.returncode in (_TRANSLATE_UNSOLVABLE, _SEARCH_UNSOLVABLE):
        return None
    elif out.returncode != _SUCCESS:
        _raise_failure(out, label)

    return _read_plan(plan_path)


def _read_plan(plan_path):
    """Read the actions of a plan file, which ends in a comment naming its cost."""
    with open(plan_path, encoding="utf-8") as plan_file:
        plan = []
        for line in plan_file:
            line = line.strip()
            if line and not line.startswith(";"):
                plan.append(line)
        return plan


def _raise_failure(out, label):
    """Report what Fast Downward said, as memory when that is what ran out."""
    message = f"Fast Downward ({label}) failed with exit code {out.returncode}"
    if out.stdout.strip():
        message += "\n" + out.stdout.strip()
    if out.stderr.strip():
        message += "\n" + out.stderr.strip()

    if out.returncode in _OUT_OF_MEMORY:
        raise OutOfMemoryError(message)
    else:
        raise IntegrationError(message)
