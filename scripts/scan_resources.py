"""Report which suite problems have a resource variable worth collapsing.

Writes the list the resources track submits, the way ``symmetries/problems.txt`` lists
what PDDL Symmetries can abstract.  Detection runs the whole numeric-fast-downward
translate-and-preprocess chain per problem, so this takes a while and is run by
hand rather than as part of a benchmark run.

Every outcome is logged as it arrives, smallest problem first, so a stopped scan
resumes where it left off and the list is current at every point.
"""

import argparse
import signal
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from core.integrations.numeric_fast_downward import detect_resources
from core.outcomes import IntegrationError
from experiments.tracks import TRACKS

# One detection grounds a whole task, and Daniel's machine is what he works on.
WORKERS = 1
DEFAULT_TIMEOUT = 60
TRACK = TRACKS["plan/resources"]
OUTPUT = TRACK.runnable_file
LOG = OUTPUT.with_suffix(".log")
FOUND = "resource"
SUITE = TRACK.suite
HEADER = """# Problems with a resource variable the detector found objects for.
# Regenerate with:
#   python -m scripts.scan_resources
"""


def main():
    args = _argument_parser().parse_args()
    # A plain kill would stop this process and orphan the detector it is waiting
    # on; as an exit, it unwinds through the detector's cleanup instead.
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(1))

    scanned = _read_log(args.log)
    tasks = sorted(_tasks(args.benchmarks), key=lambda task: task[2].stat().st_size)
    pending = [task for task in tasks if _name(task) not in scanned]
    print(f"Scanning {len(pending)} of {len(tasks)} problems; {len(tasks) - len(pending)} already in {args.log}")

    args.log.parent.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool, open(args.log, "a", encoding="utf-8") as log:
        for name, outcome in pool.map(lambda task: _scan(*task, args.timeout), pending):
            log.write(f"{name}\t{outcome}\n")
            log.flush()
            scanned[name] = outcome
            _write_list(args.output, scanned)

    found = sum(outcome.startswith(FOUND) for outcome in scanned.values())
    print(f"{found} of {len(scanned)} scanned problems carry a resource; wrote {args.output}")


def _read_log(path):
    if not path.is_file():
        return {}
    scanned = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        name, _, outcome = line.partition("\t")
        scanned[name] = outcome
    return scanned


def _write_list(path, scanned):
    lines = sorted(name for name, outcome in scanned.items() if outcome.startswith(FOUND))
    path.write_text(HEADER + "".join(f"{line}\n" for line in lines), encoding="utf-8")


def _name(task):
    domain_name, _, problem = task
    return f"{domain_name}/{problem.name}"


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
    name = _name((domain_name, domain, problem))
    try:
        with tempfile.TemporaryDirectory(prefix="apf-scan-") as directory:
            resources = detect_resources(directory, domain, problem, timeout=timeout)
    except (IntegrationError, OSError) as error:
        outcome = f"failed: {str(error).splitlines()[0]}"
    else:
        if resources:
            widest = resources[0]
            outcome = f"{FOUND} {widest.name} over {len(widest.objects)} objects"
        else:
            outcome = "none"
    print(f"  {name}: {outcome}", flush=True)
    return name, outcome


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmarks", type=Path, default=TRACK.benchmarks_dir, help="Benchmark suite directory")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="Problem list to write")
    parser.add_argument("--log", type=Path, default=LOG, help="Every outcome so far, which a rerun resumes from")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Detection limit per problem in seconds")
    parser.add_argument("--workers", type=int, default=WORKERS, help="Problems to scan at a time")
    return parser


if __name__ == "__main__":
    main()
