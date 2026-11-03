"""Find the problems of a track that have a class to collapse, or every class they have.

By default, run the track's detection on every problem of its suite and list the
problems with a class in problems.txt, which submit runs. With --classes, rank
every class the problems of problems.txt can collapse, largest first, in
classes.txt, which submit runs each abstract mode once per line of. A run ranks
its classes itself, from the same detection and the same ordering, so the file
records what each rank collapses rather than telling the run.

Every problem is scanned in a child process, which a time and memory limit can
stop, and logged as it finishes, so a stopped scan resumes where it left off.

With --submit, the scan runs on the cluster instead, as one Slurm task per
problem of the suite, each ranking that problem's classes. --collect then writes
both problems.txt and classes.txt from what the tasks found.
"""

import argparse
import json
import resource
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from experiments.run import RESULTS_DIR
from experiments.tracks import TRACKS, find_domain, has_other_status, is_domain_file

WORKERS = 1
# Detection gets 300 seconds; reading and ranking the classes needs the rest.
TIMEOUT = 600
MEMORY_LIMIT = 8 * 1024**3
# A submitted task holds the child under MEMORY_LIMIT and the Python that waits on it.
TASK_MEMORY = "9G"
# A little past TIMEOUT, so that the scan records a timeout before Slurm kills the task.
TASK_MINUTES = 12
# Each takes an equal share of a submitted scan, as one array apiece.
PARTITIONS = ("sunnycove", "broadwell")
PROBLEMS_HEADER = """# Problems with a class to collapse.
# Regenerate with:
#   python -m experiments.scan --track {track}
"""
CLASSES_HEADER = """# Every class each problem can collapse, largest first: problem, rank, type, size, objects.
# Regenerate with:
#   python -m experiments.scan --track {track} --classes
"""

# Both run in the child, so the parent stays small however large the task is.
DISCOVER = """
import sys, tempfile
from core.integrations.numeric_fast_downward import detect_resources
from core.integrations.pddl_symmetries import find_symmetric_object_sets

domain, problem, source = sys.argv[1:4]
if source == "resources":
    with tempfile.TemporaryDirectory() as directory:
        classes = detect_resources(directory, domain, problem).resources
else:
    classes = find_symmetric_object_sets(domain, problem)
print(f"{len(classes)} classes" if classes else "none")
"""
RANK = """
import json, sys
from core.abstraction.collapse import validate_supported_problem
from core.abstraction.factory import AbstractionError, _candidate_classes, _select_abstraction
from core.integrations.unified_planning import read_problem, without_action_costs
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig

domain, problem, source = sys.argv[1:4]
config = AbstractPlanningConfig(domain, problem, abstraction_source=source)
task = without_action_costs(read_problem(domain, problem))
validate_supported_problem(task)
classes = _candidate_classes(config, task, PlanningMetrics())
ranked = []
while True:
    try:
        abstraction = _select_abstraction(task, classes, rank=len(ranked))
    except AbstractionError:
        break
    ranked.append([abstraction.object_type, list(abstraction.objects)])
print(json.dumps(ranked))
"""


def main():
    args = _argument_parser().parse_args()
    track = TRACKS[args.track]
    source = args.track.split("/")[1]
    if args.submit:
        _submit(args.track, track, args.domains)
        return
    if args.task is not None:
        _scan_task(args.track, track, args.task, source, args.timeout)
        return
    if args.collect:
        _collect(args.track, track)
        return

    if args.classes:
        tasks = sorted(track.runnable())
        output, script, write = track.classes_file, RANK, _write_classes
    else:
        tasks = sorted(_suite_problems(track.benchmarks_dir, track.suite))
        output, script, write = track.runnable_file, DISCOVER, _write_problems
    log_file = output.with_suffix(".log")

    scanned = _read_log(log_file)
    pending = [task for task in tasks if _name(task) not in scanned]
    print(f"Scanning {len(pending)} of {len(tasks)} problems; {len(tasks) - len(pending)} already in {log_file}")

    with ThreadPoolExecutor(max_workers=args.workers) as pool, open(log_file, "a", encoding="utf-8") as log:
        scan = lambda task: _scan(track.benchmarks_dir, *task, script, source, args.timeout)
        for name, outcome in pool.map(scan, pending):
            log.write(f"{name}\t{outcome}\n")
            log.flush()
            scanned[name] = outcome
            write(output, scanned, args.track)

    print(f"Wrote what {len(scanned)} scanned problems have to {output}")


def _submit(track_name, track, domains):
    """Submit one Slurm task per problem of the suite, each ranking the problem's classes."""
    suite = track.suite
    if domains:
        unknown = sorted(set(domains) - set(suite))
        if unknown:
            raise SystemExit(f"Not in this track's suite: {', '.join(unknown)}")
        suite = [domain_name for domain_name in suite if domain_name in domains]
    tasks = sorted(_suite_problems(track.benchmarks_dir, suite))
    directory = _task_dir(track_name)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "tasks.txt").write_text("".join(f"{_name(task)}\n" for task in tasks), encoding="utf-8")
    task_command = f"{sys.executable} -m experiments.scan --track {track_name} --task $SLURM_ARRAY_TASK_ID"
    share = -(-len(tasks) // len(PARTITIONS))
    for number, partition in enumerate(PARTITIONS):
        first, last = number * share, min(len(tasks), (number + 1) * share) - 1
        if first > last:
            continue
        command = [
            "sbatch",
            f"--array={first}-{last}",
            f"--partition={partition}",
            "--cpus-per-task=1",
            f"--mem={TASK_MEMORY}",
            f"--time={TASK_MINUTES}",
            f"--job-name=scan-{track_name.replace('/', '-')}",
            f"--output={directory}/%a.out",
            f"--wrap={task_command}",
        ]
        subprocess.run(command, cwd=RESULTS_DIR.parent, check=True)
    print(f"Submitted {len(tasks)} problems; collect with python -m experiments.scan --track {track_name} --collect")


def _scan_task(track_name, track, index, source, timeout):
    directory = _task_dir(track_name)
    # Slurm requeues tasks, sometimes after they finished, and the outcome stands.
    if (directory / f"{index}.tsv").is_file():
        return
    name = (directory / "tasks.txt").read_text(encoding="utf-8").splitlines()[index]
    domain_name, _, problem = name.rpartition("/")
    name, outcome = _scan(track.benchmarks_dir, domain_name, problem, RANK, source, timeout)
    (directory / f"{index}.tsv").write_text(f"{name}\t{outcome}\n", encoding="utf-8")


def _collect(track_name, track):
    """Write problems.txt and classes.txt from the outcomes of the submitted tasks."""
    scanned = _task_outcomes(track_name)
    # A problem another track scanned over the same benchmarks has the same classes,
    # so a track whose suite overlaps another's submits only the problems it adds.
    suite = {_name(task) for task in _suite_problems(track.benchmarks_dir, track.suite)}
    source = track_name.split("/")[1]
    for other_name, other in TRACKS.items():
        if other.benchmarks_dir == track.benchmarks_dir and other_name.split("/")[1] == source:
            for name, outcome in _task_outcomes(other_name).items():
                if name in suite:
                    scanned.setdefault(name, outcome)

    # A ranking that found no class lists none, which problems.txt leaves out.
    found = {name: "none" if outcome == "[]" else outcome for name, outcome in scanned.items()}
    _write_problems(track.runnable_file, found, track_name)
    _write_classes(track.classes_file, scanned, track_name)
    log = "".join(f"{name}\t{outcome}\n" for name, outcome in sorted(scanned.items()))
    track.classes_file.with_suffix(".log").write_text(log, encoding="utf-8")
    print(f"Wrote what {len(scanned)} scanned problems have to {track.runnable_file} and {track.classes_file}")


def _task_outcomes(track_name):
    outcomes = {}
    for result in sorted(_task_dir(track_name).glob("*.tsv")):
        name, _, outcome = result.read_text(encoding="utf-8").strip().partition("\t")
        outcomes[name] = outcome
    return outcomes


def _task_dir(track_name):
    return RESULTS_DIR / "scan" / track_name.replace("/", "-")


def _suite_problems(benchmarks_dir, suite):
    for domain_name in suite:
        directory = Path(benchmarks_dir) / domain_name
        for problem in sorted(directory.glob("*.pddl")):
            if not is_domain_file(problem.name) and not has_other_status(problem.name):
                yield domain_name, problem.name


def _read_log(path):
    if not path.is_file():
        return {}
    scanned = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        name, _, outcome = line.partition("\t")
        scanned[name] = outcome
    return scanned


def _name(task):
    domain_name, problem = task
    return f"{domain_name}/{problem}"


def _scan(benchmarks_dir, domain_name, problem, script, source, timeout):
    problem_path = Path(benchmarks_dir) / domain_name / problem
    command = [sys.executable, "-c", script, str(find_domain(problem_path)), str(problem_path), source]
    limit_memory = lambda: resource.setrlimit(resource.RLIMIT_AS, (MEMORY_LIMIT, MEMORY_LIMIT))
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout, preexec_fn=limit_memory, check=False
        )
    except subprocess.TimeoutExpired:
        outcome = f"failed: no answer in {timeout} seconds"
    else:
        lines = completed.stdout.strip().splitlines()
        if completed.returncode == 0 and lines:
            outcome = lines[-1]
        else:
            error = completed.stderr.strip().splitlines() or [f"exit code {completed.returncode}"]
            outcome = f"failed: {error[-1]}"
    name = _name((domain_name, problem))
    print(f"  {name}: {outcome[:120]}", flush=True)
    return name, outcome


def _write_problems(path, scanned, track):
    lines = []
    for name in sorted(scanned):
        if scanned[name] != "none" and not scanned[name].startswith("failed"):
            lines.append(f"{name}\n")
    path.write_text(PROBLEMS_HEADER.format(track=track) + "".join(lines), encoding="utf-8")


def _write_classes(path, scanned, track):
    lines = []
    for name in sorted(scanned):
        if scanned[name].startswith("failed"):
            continue
        for rank, (object_type, objects) in enumerate(json.loads(scanned[name])):
            lines.append(f"{name}\t{rank}\t{object_type}\t{len(objects)}\t{' '.join(objects)}\n")
    path.write_text(CLASSES_HEADER.format(track=track) + "".join(lines), encoding="utf-8")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--track",
        required=True,
        choices=sorted(name for name in TRACKS if name.endswith(("/symmetries", "/resources"))),
        help="Track whose problems to scan",
    )
    parser.add_argument(
        "--classes",
        action="store_true",
        help="Rank every class of the problems in problems.txt into classes.txt, instead of finding those problems",
    )
    parser.add_argument(
        "--submit", action="store_true", help="Scan on the cluster, one Slurm task per problem of the suite"
    )
    parser.add_argument("--domains", nargs="+", help="Submit only these domains of the track's suite")
    parser.add_argument("--task", type=int, help=argparse.SUPPRESS)
    parser.add_argument(
        "--collect", action="store_true", help="Write problems.txt and classes.txt from the submitted tasks"
    )
    parser.add_argument("--timeout", type=int, default=TIMEOUT, help="Limit per problem in seconds")
    parser.add_argument("--workers", type=int, default=WORKERS, help="Problems to scan at a time")
    return parser


if __name__ == "__main__":
    main()
