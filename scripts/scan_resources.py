"""Report which suite problems have a resource variable worth collapsing.

Writes the list the resources track submits, the way ``symmetries.txt`` lists
what PDDL Symmetries can abstract.  Detection runs the whole numeric-fast-downward
translate-and-preprocess chain per problem, so this takes a while and is run by
hand rather than as part of a benchmark run.
"""

import argparse
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from core.integrations.numeric_fast_downward import detect_resources
from core.outcomes import IntegrationError
from experiments import DOWNWARD_BENCHMARKS_DIR
from experiments.symmetries.suite import SUITE

# Daniel's machine runs two of these at a time; more only slows them down.
WORKERS = 2
DEFAULT_TIMEOUT = 60
OUTPUT = Path(__file__).resolve().parents[1] / "experiments" / "resources" / "resources.txt"
HEADER = """# Problems with a resource variable the detector found objects for.
# Regenerate with:
#   python -m scripts.scan_resources
"""


def main():
    args = _argument_parser().parse_args()
    tasks = list(_tasks(args.benchmarks))
    print(f"Scanning {len(tasks)} problems from {len(SUITE)} domains")

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        found = list(pool.map(lambda task: _scan(*task, args.timeout), tasks))

    lines = sorted(name for name in found if name is not None)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(HEADER + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(lines)} of {len(tasks)} problems carry a resource; wrote {args.output}")


def _tasks(benchmarks):
    for domain_name in SUITE:
        directory = Path(benchmarks) / domain_name
        if not directory.is_dir():
            continue
        for problem in sorted(directory.glob("*.pddl")):
            domain = _domain_for(directory, problem)
            if domain is not None:
                yield domain_name, domain, problem


def _domain_for(directory, problem):
    """Find the domain file beside one problem, or None when it is one itself."""
    candidates = (directory / f"{problem.stem}-domain.pddl", directory / "domain.pddl")
    if "domain" in problem.name:
        return None
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def _scan(domain_name, domain, problem, timeout):
    name = f"{domain_name}/{problem.name}"
    try:
        with tempfile.TemporaryDirectory(prefix="apf-scan-") as directory:
            resources = detect_resources(directory, domain, problem, timeout=timeout)
    except (IntegrationError, OSError) as error:
        print(f"  {name}: {str(error).splitlines()[0]}")
        return None

    if not resources:
        return None
    widest = resources[0]
    print(f"  {name}: {widest.name} over {len(widest.objects)} objects")
    return name


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmarks", type=Path, default=DOWNWARD_BENCHMARKS_DIR, help="Benchmark suite directory")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="Problem list to write")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Detection limit per problem in seconds")
    parser.add_argument("--workers", type=int, default=WORKERS, help="Problems to scan at a time")
    return parser


if __name__ == "__main__":
    main()
