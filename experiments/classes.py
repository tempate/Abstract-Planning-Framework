"""Enumerate the symmetry classes of every benchmark problem.

Discovery is the expensive part of an abstract run and it depends only on the
task, so the sweep resolves it once here and writes it down. Every planning job
then gets its class handed to it and skips discovery entirely.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
from functools import partial

from core.abstraction.factory import usable_abstractions
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import PddlError, read_problem
from core.outcomes import PlanningOutcomeError
from experiments import write_classes
from experiments.submit import _benchmark_problems
from experiments.tracks import DEFAULT_TRACK, TRACKS
from scripts.utils.arguments import positive_int


def enumerate_classes(track, jobs=2, time_limit=300):
    """Find the usable classes of every problem the track submits.

    Processes rather than threads: reading a problem goes through Unified
    Planning's process-global environment, and two readers sharing it parse
    each other's names.
    """
    problems = list(_benchmark_problems(track.suite))
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        found = pool.map(partial(_classes_for, time_limit=time_limit), problems)
    return {key: classes for key, classes in found if classes}


def _classes_for(task, time_limit):
    """Discover one problem's classes, keeping the ones the collapse accepts.

    A class the abstraction would refuse is dropped here rather than submitted
    as a job that can only fail.
    """
    domain_name, domain, problem = task
    key = f"{domain_name}/{problem.name}"
    try:
        discovered = find_symmetric_object_sets(domain, problem, time_limit)
        abstractions, _ = usable_abstractions(read_problem(domain, problem), discovered)
    except (PlanningOutcomeError, PddlError) as error:
        print(f"{key}: {error}", flush=True)
        return key, []

    print(f"{key}: {len(abstractions)} class(es)", flush=True)
    return key, [list(abstraction.objects) for abstraction in abstractions]


def main():
    args = _argument_parser().parse_args()
    track = TRACKS[args.track]
    classes = enumerate_classes(track, jobs=args.jobs, time_limit=args.time_limit)
    write_classes(classes, track.classes_file)
    _report(classes, track.classes_file)


def _report(classes, path):
    counts = sorted(len(value) for value in classes.values())
    jobs = sum(counts)
    print(f"\n{len(classes)} problems with a class, {jobs} jobs")
    if counts:
        print(f"classes per problem: min {counts[0]}, median {counts[len(counts) // 2]}, max {counts[-1]}")
    print(f"Wrote {path}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", choices=sorted(TRACKS), default=DEFAULT_TRACK, help="Benchmark track to enumerate")
    parser.add_argument("--jobs", type=positive_int, default=2, help="Problems to discover in parallel")
    parser.add_argument(
        "--time-limit", type=positive_int, default=300, help="PDDL Symmetries time limit per problem in seconds"
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
