"""cpddl integration for the lifted planner of Horčík, Fišer and Torralba (AAAI 2022)."""

import os
import subprocess
from dataclasses import dataclass

from core.integrations.paths import CPDDL_BIN
from core.utilities.outcomes import OutOfMemoryError, tool_failure

# cpddl panics with exit code 255 on every error, out of memory included.
_OUT_OF_MEMORY_MESSAGE = "Allocation of memory failed"
# A SIGKILL, which only the cluster's memory limit sends, before cpddl notices itself.
_KILLED = (-9,)


@dataclass(frozen=True)
class Search:
    """A lifted search guided by a heuristic on a grounded homomorphic image of the task."""

    algorithm: str
    heuristic: str
    # The share of objects collapsed, the paper's best for each search.
    removed_ratio: float


# The paper's best configurations: rnd-g at 75% for GBFS and h^FF, at 95% for A* and LM-cut.
GBFS_FF = Search("gbfs", "homo-ff", 0.75)
ASTAR_LMCUT = Search("astar", "homo-lmc", 0.95)


def find_plan(base_dir, domain_path, problem_path, search):
    """Search one PDDL task, returning the lines of its plan, or None when it has none."""
    os.makedirs(base_dir, exist_ok=True)
    plan_path = os.path.join(base_dir, "cpddl.plan")
    # rnd-g: random objects of the same type, never a goal object, best of 5 samples by h(I).
    command = [
        CPDDL_BIN,
        "lplan",
        # Unit costs, like lmcut's cost_type=one, so that A* with LM-cut finds a shortest plan.
        "--pddl-unit-cost",
        "--homo-type",
        "rnd-objs",
        "--homo-rm-ratio",
        str(search.removed_ratio),
        "--homo-keep-goal-objs",
        "--homo-samples",
        "5",
        search.algorithm,
        search.heuristic,
        plan_path,
        os.fspath(domain_path),
        os.fspath(problem_path),
    ]
    completed = subprocess.run(command, capture_output=True, text=True)

    if completed.returncode != 0:
        if _OUT_OF_MEMORY_MESSAGE in completed.stdout + completed.stderr:
            raise OutOfMemoryError(f"cpddl ran out of memory\n{completed.stderr.strip()}")
        raise tool_failure("cpddl", completed, _KILLED)

    # cpddl exits 0 on an unsolvable task too, and then writes no plan.
    if not os.path.exists(plan_path):
        return None

    return _read_plan(plan_path)


def _read_plan(plan_path):
    """Read a plan file, whose comment lines start with `;;`."""
    with open(plan_path, encoding="utf-8") as plan_file:
        return [line.strip() for line in plan_file if line.strip() and not line.startswith(";")]
