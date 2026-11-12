"""List the problems with a class that Fast Downward cannot ground in 8 GB.

Grounding does not depend on the mode, so every track over the same benchmarks
shares one list, written beside their directories. A problem some concrete mode
of those tracks solves must ground, so only the others are grounded.

--submit runs Fast Downward's translator alone on each of them, one Slurm task
per problem, and --collect writes the list from what the tasks found.
"""

import argparse
import csv
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from core.integrations.paths import FAST_DOWNWARD_SCRIPT
from experiments import slurm
from experiments.run import ABSTRACTION_PREFIX, RESULTS_DIR
from experiments.tracks import TRACKS, find_domain

TIME_LIMIT = "30m"
MEMORY_LIMIT = "8G"
# The translator stays under MEMORY_LIMIT; the driver and the Python that waits on it need the rest.
TASK_MEMORY = "9G"
TASK_MINUTES = 40
# Memory decides whether a problem grounds, so the older CPU generation will do.
PARTITION = "broadwell"
# Fast Downward's exit codes for its translator.
_GROUNDED = (0, 10)
_OUT_OF_MEMORY = 20
_OUT_OF_TIME = 21
HEADER = """# Problems with a class that Fast Downward's translator cannot ground in {memory} and {time}.
# A problem some concrete mode solves grounds, so only the others were grounded.
# Regenerate with:
#   python -m experiments.grounding --track {track} --submit
#   python -m experiments.grounding --track {track} --collect
"""


def main():
    args = _argument_parser().parse_args()
    if args.submit:
        _submit(args.track)
    elif args.task is not None:
        _ground_task(args.track, args.task)
    elif args.collect:
        _collect(args.track)


def _submit(track_name):
    """Submit one Slurm task per problem that no concrete mode solves."""
    tasks = sorted(_unsolved(track_name))
    slurm.submit(
        _task_dir(track_name),
        [f"{domain}/{problem}" for domain, problem in tasks],
        f"{sys.executable} -m experiments.grounding --track {track_name}",
        f"grounding-{track_name.split('/')[0]}",
        PARTITION,
        TASK_MEMORY,
        TASK_MINUTES,
    )

    print(
        f"Submitted {len(tasks)} problems; collect with python -m experiments.grounding --track {track_name} --collect"
    )


def _ground_task(track_name, index):
    def ground(name):
        domain_name, _, problem = name.rpartition("/")
        return _ground(TRACKS[track_name].benchmarks_dir / domain_name, problem)

    slurm.run_task(_task_dir(track_name), index, ground)


def _ground(directory, problem):
    """Run Fast Downward's translator alone on one problem and say how it ended."""
    problem_path = directory / problem
    with tempfile.TemporaryDirectory(prefix="grounding-") as work:
        command = [
            sys.executable,
            FAST_DOWNWARD_SCRIPT,
            "--translate-time-limit",
            TIME_LIMIT,
            "--translate-memory-limit",
            MEMORY_LIMIT,
            "--sas-file",
            str(Path(work) / "output.sas"),
            "--translate",
            str(find_domain(problem_path)),
            str(problem_path),
        ]

        completed = subprocess.run(command, capture_output=True, text=True, check=False)

    output = completed.stdout + completed.stderr
    if completed.returncode in _GROUNDED:
        return "grounded"

    # The driver can crash on its own report of a MemoryError, which leaves exit code 1.
    if completed.returncode == _OUT_OF_MEMORY or "MemoryError" in output:
        return "out of memory"

    if completed.returncode == _OUT_OF_TIME:
        return "out of time"
    return f"failed: exit code {completed.returncode}"


def _collect(track_name):
    """Write the problems that did not ground, from the outcomes of the submitted tasks."""
    outcomes = slurm.outcomes(_task_dir(track_name))
    missing = {f"{domain}/{problem}" for domain, problem in _unsolved(track_name)} - set(outcomes)

    if missing:
        raise SystemExit(f"{len(missing)} problems have no outcome yet, such as {sorted(missing)[0]}")

    failed = sorted(name for name, outcome in outcomes.items() if outcome != "grounded")
    header = HEADER.format(
        memory=MEMORY_LIMIT.replace("G", " GB"), time=TIME_LIMIT.replace("m", " minutes"), track=track_name
    )
    _list_file(track_name).write_text(header + "".join(f"{name}\n" for name in failed), encoding="utf-8")
    print(f"Wrote the {len(failed)} of {len(outcomes)} problems that did not ground to {_list_file(track_name)}")


def _unsolved(track_name):
    """The problems with a class that no concrete mode of the sibling tracks solves."""
    problems, solved = set(), set()
    for track in _siblings(track_name):
        problems |= track.runnable()
        if track.results_file.is_file():
            with open(track.results_file, newline="", encoding="utf-8") as results:
                for row in csv.DictReader(results):
                    if not row["mode"].startswith(ABSTRACTION_PREFIX) and row["status"] == "success":
                        solved.add((row["domain"], row["problem"]))

    return problems - solved


def _siblings(track_name):
    """Every track over the same benchmarks as this one, itself included."""
    benchmarks_dir = TRACKS[track_name].benchmarks_dir
    return [track for track in TRACKS.values() if track.benchmarks_dir == benchmarks_dir]


def ungroundable(track_name):
    """The (domain, problem) pairs the track's list says Fast Downward cannot ground, empty without a list."""
    list_file = _list_file(track_name)
    if not list_file.is_file():
        return frozenset()
    problems = set()
    for line in list_file.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            domain, _, problem = line.strip().rpartition("/")
            problems.add((domain, problem))
    return frozenset(problems)


def _list_file(track_name):
    return Path(os.path.commonpath([track.directory for track in _siblings(track_name)])) / "ungroundable.txt"


def _task_dir(track_name):
    return RESULTS_DIR / "grounding" / TRACKS[track_name].benchmarks_dir.name


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--track", choices=sorted(TRACKS), required=True, help="A track over the benchmarks to ground")
    parser.add_argument(
        "--submit", action="store_true", help="Ground every problem no concrete mode solves on the cluster"
    )
    parser.add_argument("--collect", action="store_true", help="Write the list from the submitted tasks' outcomes")
    parser.add_argument("--task", type=int, help=argparse.SUPPRESS)
    return parser


if __name__ == "__main__":
    main()
