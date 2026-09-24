"""Enumerate the symmetry classes of every problem a track submits.

Discovery depends only on the task, so it runs once here and the result is
written down. A run over every class then hands each job its class, and the job
skips discovery.
"""

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from functools import partial

from core.abstraction.factory import usable_abstractions
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import PddlError, read_problem
from core.outcomes import PlanningOutcomeError
from experiments.submit import _benchmark_problems
from experiments.tracks import TRACKS
from scripts.utils.arguments import positive_int

REGENERATE = "python -m experiments.classes --track {track}"


def enumerate_classes(track, jobs=2, time_limit=300):
    """Find the usable classes of every problem the track submits.

    Processes rather than threads: reading a problem goes through Unified
    Planning's process-global environment, and two readers sharing it parse
    each other's names.
    """
    problems = list(_benchmark_problems(track.benchmarks_dir, track.suite, track.runnable()))
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
    document = {"regenerate": REGENERATE.format(track=args.track), "classes": dict(sorted(classes.items()))}
    track.classes_file.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")

    counts = sorted(len(value) for value in classes.values())
    print(f"\n{len(classes)} problems with a class, {sum(counts)} classes")
    if counts:
        print(f"classes per problem: min {counts[0]}, median {counts[len(counts) // 2]}, max {counts[-1]}")
    print(f"Wrote {track.classes_file}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--track",
        required=True,
        choices=sorted(name for name in TRACKS if name.endswith("/symmetries")),
        help="Track whose problems to enumerate",
    )
    parser.add_argument("--jobs", type=positive_int, default=2, help="Problems to discover in parallel")
    parser.add_argument(
        "--time-limit", type=positive_int, default=300, help="PDDL Symmetries time limit per problem in seconds"
    )
    return parser


if __name__ == "__main__":
    main()
