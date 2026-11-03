"""MS-unsat, the merge-and-shrink planner Torralba and Hoffmann entered in the Unsolvability IPC 2016."""

import os
import subprocess
import sys

from core.integrations.paths import MS_UNSAT_PREPROCESSOR, MS_UNSAT_SEARCH, MS_UNSAT_TRANSLATOR
from core.outcomes import IntegrationError, OutOfMemoryError

# The search's exit codes, from utilities.h of its 2016 Fast Downward.
_PLAN_FOUND = 0
_UNSOLVABLE = 4
_OUT_OF_MEMORY = 6
# A step killed by SIGKILL, which on these tasks is the kernel reclaiming the
# memory it asked for.
_KILLED = -9
# The competition's MS-unsat configuration, from its search/downward script.
# Bisimulation is exact and own-label shrinking keeps every goal path, so the
# abstraction has a path to the goal whenever the task has a plan.
_SEARCH_OPTIONS = (
    "--search",
    "astar(merge_and_shrink(shrink_after_merge=true,"
    "merge_strategy=merge_linear_criteria(criteria=[scc(reverse=False,complete_cg=True),goal],var_order=level),"
    "shrink_strategy=shrink_composite(strategies=[shrink_own_labels(goal_shrinking=true),"
    "shrink_bisimulation(max_states=infinity,greedy=false,threshold=1,aggregate_goals=true)]),"
    "cost_type=3))",
)


def has_plan(base_dir, domain_path, problem_path, label):
    """Translate, preprocess and search one PDDL task, reporting only whether it has a plan.

    The translator and the preprocessor prove some tasks unsolvable themselves,
    the preprocessor through h² mutexes. Both then write a trivially unsolvable
    task, so the search's exit code carries every verdict.
    """
    os.makedirs(base_dir, exist_ok=True)
    # Each step reads and writes fixed file names in its working directory.
    translate = [sys.executable, MS_UNSAT_TRANSLATOR, os.path.abspath(domain_path), os.path.abspath(problem_path)]
    _run(translate, base_dir, label, "translator")
    _run([MS_UNSAT_PREPROCESSOR], base_dir, label, "preprocessor", stdin="output.sas")
    completed_process = _run(
        [MS_UNSAT_SEARCH, *_SEARCH_OPTIONS], base_dir, label, "search", stdin="output", check=False
    )

    if completed_process.returncode == _PLAN_FOUND:
        return True
    if completed_process.returncode == _UNSOLVABLE:
        return False
    _raise_failure(completed_process, label, "search")


def _run(command, base_dir, label, step, stdin=os.devnull, check=True):
    with open(os.path.join(base_dir, stdin), encoding="utf-8") as input_file:
        completed_process = subprocess.run(command, cwd=base_dir, stdin=input_file, capture_output=True, text=True)
    if check and completed_process.returncode != 0:
        _raise_failure(completed_process, label, step)
    return completed_process


def _raise_failure(completed_process, label, step):
    """Report what MS-unsat said, as memory when that is what ran out."""
    diagnostics = "\n".join(
        output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
    )
    message = f"MS-unsat {step} ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
    # The translator is Python, so it runs out of memory with a traceback.
    if completed_process.returncode in (_OUT_OF_MEMORY, _KILLED) or "MemoryError" in completed_process.stderr:
        raise OutOfMemoryError(message)
    raise IntegrationError(message)
