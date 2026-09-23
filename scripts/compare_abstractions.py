"""Check that the working tree abstracts the benchmarks the same way another commit does.

For the first problem of each plan-track domain, collapse its largest same-type
object set with both versions of the code and compare the abstract task and the
relaxed-delete and inequality counts. It is the check that a change to
core/abstraction preserves behavior, which the tests alone cannot show. A class
chosen this way is not the one PDDL Symmetries would pick, and some are rejected;
a problem both versions reject says nothing either way.
"""

import argparse
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from experiments.submit import _find_domain
from experiments.tracks import TRACKS

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = 120

# Run inside the checkout being described, so it may only use what both
# versions of the code provide.
DESCRIBE = """
import collections, hashlib, json, sys
from core.abstraction.factory import build_abstract_problem
from core.integrations.unified_planning import read_problem, without_action_costs
from core.planning.config import AbstractPlanningConfig

domain, problem = sys.argv[1:3]
objects_by_type = collections.defaultdict(list)
for item in read_problem(domain, problem).all_objects:
    objects_by_type[item.type].append(item.name)
objects = max(objects_by_type.values(), key=len)
try:
    result = build_abstract_problem(AbstractPlanningConfig(domain, problem, objects_to_abstract=objects))
except Exception as error:
    print(json.dumps({"rejected": f"{type(error).__name__}: {error}"}))
    sys.exit()

# What the task holds rather than how it is written: Unified Planning declares
# objects in an order that follows their identity, which differs between runs.
task = without_action_costs(result.problem)
actions = []
for action in task.actions:
    conditions = sorted(str(condition) for condition in action.preconditions)
    effects = sorted(str(effect) for effect in action.effects)
    actions.append(json.dumps([action.name, [str(parameter) for parameter in action.parameters], conditions, effects]))
content = {
    "objects": sorted(f"{item.name} - {item.type}" for item in task.all_objects),
    "fluents": sorted(str(fluent) for fluent in task.fluents),
    "actions": sorted(actions),
    "init": sorted(f"{fluent} = {value}" for fluent, value in task.explicit_initial_values.items()),
    "goals": sorted(str(goal) for goal in task.goals),
}
print(json.dumps({
    "task": hashlib.sha256(json.dumps(content).encode()).hexdigest(),
    "relaxed_deletes": len(result.relaxed_deletes),
    "relaxed_inequalities": len(result.relaxed_inequalities),
}))
"""


def main():
    args = _argument_parser().parse_args()
    problems = _first_problem_of_each_domain(args.domains)
    with tempfile.TemporaryDirectory(prefix="apf-compare-") as directory:
        reference = Path(directory) / "reference"
        subprocess.run(["git", "worktree", "add", "--detach", "-q", str(reference), args.ref], check=True)
        try:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                outcomes = list(pool.map(lambda task: _compare(reference, *task), problems))
        finally:
            subprocess.run(["git", "worktree", "remove", "--force", str(reference)], check=True)

    counts = {}
    for domain, (outcome, detail) in outcomes:
        counts[outcome] = counts.get(outcome, 0) + 1
        if detail:
            print(f"{domain}: {outcome}, {detail}")
    print(", ".join(f"{count} {outcome}" for outcome, count in sorted(counts.items())))
    return 0 if set(counts) <= {"identical", "rejected by both"} else 1


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ref", nargs="?", default="main", help="Commit to compare the working tree against")
    parser.add_argument("--domains", nargs="+", help="Compare only these domains")
    parser.add_argument("--workers", type=int, default=2, help="Problems described at once")
    return parser


def _first_problem_of_each_domain(domains=None):
    track = TRACKS["plan"]
    first = {}
    for domain, problem in sorted(track.runnable()):
        if domains is None or domain in domains:
            first.setdefault(domain, problem)
    tasks = []
    for domain, problem in first.items():
        path = track.benchmarks_dir / domain / problem
        tasks.append((domain, _find_domain(path), path))
    return tasks


def _compare(reference, domain_name, domain, problem):
    before = _describe(reference, domain, problem)
    after = _describe(PROJECT_ROOT, domain, problem)
    if "timeout" in (before, after):
        return domain_name, ("timed out", None)
    if "rejected" in before and "rejected" in after:
        return domain_name, ("rejected by both", None)
    if before == after:
        return domain_name, ("identical", None)
    return domain_name, ("differs", f"before {before}, after {after}")


def _describe(checkout, domain, problem):
    """How the code in that checkout abstracts one problem."""
    command = [sys.executable, "-c", DESCRIBE, str(domain), str(problem)]
    environment = {"PYTHONPATH": str(checkout), "PATH": ""}
    try:
        completed = subprocess.run(
            command, cwd=checkout, env=environment, capture_output=True, text=True, timeout=TIMEOUT
        )
    except subprocess.TimeoutExpired:
        return "timeout"
    lines = completed.stdout.strip().splitlines()
    if completed.returncode != 0 or not lines:
        return {"rejected": completed.stderr.strip().splitlines()[-1:]}
    return json.loads(lines[-1])


if __name__ == "__main__":
    raise SystemExit(main())
