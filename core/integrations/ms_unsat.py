"""MS-unsat integration for deciding whether a PDDL task has a plan."""

import os
import subprocess
import sys

from core.integrations.paths import MS_UNSAT_PREPROCESSOR, MS_UNSAT_SEARCH, MS_UNSAT_TRANSLATOR
from core.outcomes import IntegrationError, OutOfMemoryError

# MS-unsat's exit codes, from utilities.h of its Fast Downward.
_SUCCESS = 0
_SEARCH_UNSOLVABLE = 4
_OUT_OF_MEMORY = (6, -9)
# The configuration MS-unsat ran in the Unsolvability IPC 2016.
_SEARCH_OPTIONS = (
    "--search",
    "astar(merge_and_shrink(shrink_after_merge=true,"
    "merge_strategy=merge_linear_criteria(criteria=[scc(reverse=False,complete_cg=True),goal],var_order=level),"
    "shrink_strategy=shrink_composite(strategies=[shrink_own_labels(goal_shrinking=true),"
    "shrink_bisimulation(max_states=infinity,greedy=false,threshold=1,aggregate_goals=true)]),"
    "cost_type=3))",
)


def has_plan(base_dir, domain_path, problem_path, label):
    """Translate, preprocess and search one PDDL task, reporting only whether it has a plan."""
    os.makedirs(base_dir, exist_ok=True)

    command = [sys.executable, MS_UNSAT_TRANSLATOR, os.path.abspath(domain_path), os.path.abspath(problem_path)]
    out = _run(command, base_dir)
    if out.returncode != _SUCCESS:
        _raise_failure(out, label)

    out = _run([MS_UNSAT_PREPROCESSOR], base_dir, stdin="output.sas")
    if out.returncode != _SUCCESS:
        _raise_failure(out, label)

    out = _run([MS_UNSAT_SEARCH, *_SEARCH_OPTIONS], base_dir, stdin="output")
    if out.returncode == _SEARCH_UNSOLVABLE:
        return False
    elif out.returncode != _SUCCESS:
        _raise_failure(out, label)

    return True


def _run(command, base_dir, stdin=os.devnull):
    with open(os.path.join(base_dir, stdin), encoding="utf-8") as stdin_file:
        return subprocess.run(command, cwd=base_dir, stdin=stdin_file, capture_output=True, text=True)


def _raise_failure(out, label):
    """Report what MS-unsat said, as memory when that is what ran out."""
    message = f"MS-unsat ({label}) failed with exit code {out.returncode}"
    if out.stdout.strip():
        message += "\n" + out.stdout.strip()
    if out.stderr.strip():
        message += "\n" + out.stderr.strip()

    if out.returncode in _OUT_OF_MEMORY or "MemoryError" in out.stderr:
        raise OutOfMemoryError(message)
    else:
        raise IntegrationError(message)
