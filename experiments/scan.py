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

from experiments import slurm
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
# One CPU generation, so that every problem gets the same time limit.
PARTITION = "sunnycove"
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

domain, problem, source, before_grounding = sys.argv[1:5]
if source == "resources":
    with tempfile.TemporaryDirectory() as directory:
        classes = detect_resources(directory, domain, problem).resources
else:
    classes = find_symmetric_object_sets(domain, problem, before_grounding=before_grounding == "1")
print(f"{len(classes)} classes" if classes else "none")
"""
RANK = """
import json, sys
from core.abstraction.collapse import validate_supported_problem
from core.abstraction.factory import AbstractionError, _candidate_classes, _select_abstraction
from core.integrations.unified_planning import read_problem, without_action_costs
from core.utilities.metrics import PlanningMetrics
from core.utilities.config import AbstractPlanningConfig

domain, problem, source, before_grounding = sys.argv[1:5]
config = AbstractPlanningConfig(
    domain, problem, abstraction_source=source, symmetries_before_grounding=before_grounding == "1"
)
task = without_action_costs(read_problem(domain, problem))
validate_supported_problem(task)
classes = _candidate_classes(config, PlanningMetrics())
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
        _submit(args.track, track, args.domains, args.keep_classes)
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
        scan = lambda task: _scan(track.benchmarks_dir, *task, script, source, _before_grounding(track), args.timeout)
        for name, outcome in pool.map(scan, pending):
            log.write(f"{name}\t{outcome}\n")
            log.flush()
            scanned[name] = outcome
            write(output, scanned, args.track)

    print(f"Wrote what {len(scanned)} scanned problems have to {output}")


def _submit(track_name, track, domains, keep_classes=False):
    """Submit one Slurm task per problem of the suite, each ranking the problem's classes."""
    suite = track.suite
    if domains:
        unknown = sorted(set(domains) - set(suite))
        if unknown:
            raise SystemExit(f"Not in this track's suite: {', '.join(unknown)}")
        suite = [domain_name for domain_name in suite if domain_name in domains]
    tasks = sorted(_suite_problems(track.benchmarks_dir, suite))
    directory = _task_dir(track_name)
    if keep_classes:
        # The kept classes become outcomes, so collecting writes them with the new ones.
        logged = _read_log(track.classes_file.with_suffix(".log"))
        kept = {name: outcome for name, outcome in logged.items() if outcome.startswith("[[")}
        for name, outcome in kept.items():
            result = directory / "outcomes" / f"{name}.tsv"
            result.parent.mkdir(parents=True, exist_ok=True)
            result.write_text(f"{name}\t{outcome}\n", encoding="utf-8")
        tasks = [task for task in tasks if _name(task) not in kept]
    slurm.submit(
        directory,
        [_name(task) for task in tasks],
        f"{sys.executable} -m experiments.scan --track {track_name}",
        f"scan-{track_name.replace('/', '-')}",
        PARTITION,
        TASK_MEMORY,
        TASK_MINUTES,
    )
    print(f"Submitted {len(tasks)} problems; collect with python -m experiments.scan --track {track_name} --collect")


def _scan_task(track_name, track, index, source, timeout):
    def rank(name):
        domain_name, _, problem = name.rpartition("/")
        _, outcome = _scan(track.benchmarks_dir, domain_name, problem, RANK, source, _before_grounding(track), timeout)
        return outcome

    slurm.run_task(_task_dir(track_name), index, rank)


def _collect(track_name, track):
    """Write problems.txt and classes.txt from the outcomes of the submitted tasks."""
    scanned = slurm.outcomes(_task_dir(track_name))
    # A problem another track scanned over the same benchmarks has the same classes,
    # so a track whose suite overlaps another's submits only the problems it adds.
    suite = {_name(task) for task in _suite_problems(track.benchmarks_dir, track.suite)}
    source = track_name.split("/")[1]
    for other_name, other in TRACKS.items():
        if other.benchmarks_dir == track.benchmarks_dir and other_name.split("/")[1] == source:
            for name, outcome in slurm.outcomes(_task_dir(other_name)).items():
                if name in suite:
                    scanned.setdefault(name, outcome)

    # A ranking that found no class lists none, which problems.txt leaves out.
    found = {name: "none" if outcome == "[]" else outcome for name, outcome in scanned.items()}
    _write_problems(track.runnable_file, found, track_name)
    _write_classes(track.classes_file, scanned, track_name)
    log = "".join(f"{name}\t{outcome}\n" for name, outcome in sorted(scanned.items()))
    track.classes_file.with_suffix(".log").write_text(log, encoding="utf-8")
    print(f"Wrote what {len(scanned)} scanned problems have to {track.runnable_file} and {track.classes_file}")


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


def _before_grounding(track):
    # The scan must find the classes the runs will find, so it follows the track's arguments.
    return "--symmetries-before-grounding" in track.abstract_arguments


def _scan(benchmarks_dir, domain_name, problem, script, source, before_grounding, timeout):
    problem_path = Path(benchmarks_dir) / domain_name / problem
    flag = "1" if before_grounding else "0"
    command = [sys.executable, "-c", script, str(find_domain(problem_path)), str(problem_path), source, flag]
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
        choices=sorted(TRACKS),
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
    parser.add_argument(
        "--keep-classes",
        action="store_true",
        help="Submit only the problems the track's classes.log gives no class, keeping the classes it has",
    )
    parser.add_argument("--task", type=int, help=argparse.SUPPRESS)
    parser.add_argument(
        "--collect", action="store_true", help="Write problems.txt and classes.txt from the submitted tasks"
    )
    parser.add_argument("--timeout", type=int, default=TIMEOUT, help="Limit per problem in seconds")
    parser.add_argument("--workers", type=int, default=WORKERS, help="Problems to scan at a time")
    return parser


if __name__ == "__main__":
    main()
