"""Report resource-ladder candidates: object types a static relation orders or counts."""

import argparse
from pathlib import Path

from benchmarks.suite import BENCHMARKS_DIR, NON_PNF_DOMAINS, SUITE
from core.abstraction.ladders import find_ladders
from core.integrations.unified_planning import PddlError, read_problem
from scripts.run_benchmarks import _find_domain


def main():
    args = _argument_parser().parse_args()
    if args.suite:
        _report_suite()
    else:
        _report_problem(args.domain, args.problem)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", type=Path, help="Concrete domain PDDL")
    parser.add_argument("--problem", type=Path, help="Concrete problem PDDL")
    parser.add_argument(
        "--suite", action="store_true", help="List every suite problem that has a ladder, as 'domain/problem' lines"
    )
    return parser


def _report_problem(domain_path, problem_path):
    problem = read_problem(domain_path, problem_path)
    candidates = find_ladders(problem)
    if not candidates:
        print("No resource-ladder candidate found")
        return

    for candidate in candidates:
        size = len(candidate.objects)
        print(f"{candidate.object_type}: {candidate.relation} is {candidate.shape} over {size} objects")
        print(f"  --objects-to-abstract {' '.join(candidate.objects)}")


def _report_suite():
    """List the suite problems a ladder scan accepts, skipping the non-PNF domains."""
    for domain_name in SUITE:
        if domain_name in NON_PNF_DOMAINS:
            continue
        directory = BENCHMARKS_DIR / domain_name
        for problem_path in sorted(directory.glob("*.pddl")):
            if "domain" in problem_path.name:
                continue
            if _has_ladder(_find_domain(problem_path), problem_path):
                print(f"{domain_name}/{problem_path.name}")


def _has_ladder(domain_path, problem_path):
    try:
        return bool(find_ladders(read_problem(domain_path, problem_path)))
    except PddlError:
        # A task this project cannot even parse is not a task it can abstract.
        return False


if __name__ == "__main__":
    main()
