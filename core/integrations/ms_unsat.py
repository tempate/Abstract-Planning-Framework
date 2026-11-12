"""MS-unsat integration for deciding whether a PDDL task has a plan."""

import os
import subprocess
import sys

from core.integrations.paths import MS_UNSAT_PREPROCESSOR, MS_UNSAT_SEARCH, MS_UNSAT_TRANSLATOR
from core.utilities.outcomes import tool_failure

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

    translate = [sys.executable, MS_UNSAT_TRANSLATOR, os.path.abspath(domain_path), os.path.abspath(problem_path)]
    _run(translate, base_dir, os.devnull, label)

    _run([MS_UNSAT_PREPROCESSOR], base_dir, os.path.join(base_dir, "output.sas"), label)

    search = [MS_UNSAT_SEARCH, *_SEARCH_OPTIONS]
    completed = _run(search, base_dir, os.path.join(base_dir, "output"), label, accepted=(_SEARCH_UNSOLVABLE,))
    return completed.returncode != _SEARCH_UNSOLVABLE


def _run(command, base_dir, stdin_path, label, accepted=()):
    """Run one stage of MS-unsat, raising unless it succeeds or ends with an accepted exit code."""
    with open(stdin_path, encoding="utf-8") as stdin_file:
        completed = subprocess.run(command, cwd=base_dir, stdin=stdin_file, capture_output=True, text=True)

    if completed.returncode != _SUCCESS and completed.returncode not in accepted:
        raise tool_failure(f"MS-unsat ({label})", completed, _OUT_OF_MEMORY)

    return completed
