"""Fast Downward integration for translating PDDL tasks to SAS and searching them."""

import os
import subprocess
import sys
from dataclasses import dataclass

from core.integrations.paths import FAST_DOWNWARD_SCRIPT, PARTIAL_GROUNDING_TRANSLATOR
from core.utilities.outcomes import UnsolvableTaskError, tool_failure
from core.utilities.plan import PlanAction

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

    _translate(command, label)
    return sas_path


def partial_pddl_to_sas(base_dir, domain_path, problem_path, actions_path):
    """Translate a PDDL task grounding only the actions a plan file lists, and return its SAS file."""
    sas_path = os.path.join(base_dir, "output.sas")
    # The fork's driver insists on a search build, so call its translator, which needs none.
    command = [
        sys.executable,
        PARTIAL_GROUNDING_TRANSLATOR,
        os.fspath(domain_path),
        os.fspath(problem_path),
        "--sas-file",
        sas_path,
        "--grounding-action-queue-ordering",
        "actionsfromfile",
        "--actions-file",
        os.fspath(actions_path),
    ]

    _translate(command, "partial")
    return sas_path


def _translate(command, label):
    completed = subprocess.run(command, capture_output=True, text=True)

    if completed.returncode == _TRANSLATE_UNSOLVABLE or _UNSOLVABLE_MARKER in completed.stdout:
        raise UnsolvableTaskError(f"Fast Downward ({label}) proved the task unsolvable while translating")

    if completed.returncode != _SUCCESS:
        raise tool_failure(f"Fast Downward ({label})", completed, _OUT_OF_MEMORY)


def find_pddl_plan(base_dir, domain_path, problem_path, label, search):
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
    """Convert the lines of a plan file into chronological plan actions, from step 1."""
    actions = []
    for time_step, line in enumerate(plan, 1):
        name, *args = line.strip().strip("()").split()
        action = PlanAction(name=name, args=tuple(args), time_step=time_step)
        actions.append(action)

    return tuple(actions)


def _find_plan(command, label, plan_path):
    completed = subprocess.run(command, capture_output=True, text=True)

    if completed.returncode in (_TRANSLATE_UNSOLVABLE, _SEARCH_UNSOLVABLE):
        return None
    elif completed.returncode != _SUCCESS:
        raise tool_failure(f"Fast Downward ({label})", completed, _OUT_OF_MEMORY)

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
