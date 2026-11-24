"""Powerlifted integration for searching a PDDL task without grounding it."""

import os
import subprocess
import sys
from dataclasses import dataclass

from core.integrations.paths import POWERLIFTED_SCRIPT
from core.utilities.outcomes import tool_failure

# Powerlifted's exit codes, from src/search/utils/system.h.
_SUCCESS = 0
_UNSOLVABLE = 11
_UNSOLVED_INCOMPLETE = 12
# 247 is the driver passing on its search killed by SIGKILL, which only the memory limit sends.
_OUT_OF_MEMORY = (22, 247)


@dataclass(frozen=True)
class Search:
    """A Powerlifted search, as its algorithm and the heuristic guiding it."""

    algorithm: str
    heuristic: str


# Satisficing, the configuration Powerlifted's README recommends for coverage.
ALT_BFWS = Search("alt-bfws1", "ff")
# Optimal, since h^max is the only admissible heuristic Powerlifted has beyond blind.
HMAX = Search("astar", "hmax")


def find_plan(base_dir, domain_path, problem_path, search):
    """Search one PDDL task, returning its plan as Fast Downward writes one, or None."""
    os.makedirs(base_dir, exist_ok=True)
    plan_path = os.path.join(base_dir, "powerlifted.plan")
    # Unit costs, like lmcut's cost_type=one, so that hmax finds a shortest plan.
    command = [
        sys.executable,
        POWERLIFTED_SCRIPT,
        "--domain",
        os.fspath(domain_path),
        "--instance",
        os.fspath(problem_path),
        "--search",
        search.algorithm,
        "--evaluator",
        search.heuristic,
        "--generator",
        "yannakakis",
        "--unit-cost",
        "--translator-output-file",
        os.path.join(base_dir, "output.lifted"),
        "--plan-file",
        plan_path,
    ]
    completed = subprocess.run(command, capture_output=True, text=True)

    if completed.returncode in (_UNSOLVABLE, _UNSOLVED_INCOMPLETE):
        return None
    elif completed.returncode != _SUCCESS:
        raise tool_failure("Powerlifted", completed, _OUT_OF_MEMORY)

    return _read_plan(plan_path)


def _read_plan(plan_path):
    """Read a plan file, whose lines read `1: (pick ball1 rooma left ) ;[created objects: ]`."""
    with open(plan_path, encoding="utf-8") as plan_file:
        plan = []
        for line in plan_file:
            action = line.partition(";")[0].strip()
            if action:
                plan.append(action.partition(":")[2].strip())

        return plan
