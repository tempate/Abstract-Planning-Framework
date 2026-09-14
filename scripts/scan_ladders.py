"""List the SUITE problems whose translated task holds a resource ladder.

Nothing collects this during a benchmark run, so the list comes from translating
every problem and reading the variables back out of the SAS file.
"""

import argparse
import tempfile
from pathlib import Path

from benchmarks.suite import BENCHMARKS_DIR, SUITE
from core.abstraction.detect_ladders import _find_sas_ladders
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.sas import read_sas
from scripts.run_benchmarks import _find_domain


def main():
    args = _argument_parser().parse_args()
    for domain_name in SUITE:
        directory = Path(args.benchmarks) / domain_name
        if not directory.is_dir():
            continue
        for problem in sorted(directory.glob("*.pddl")):
            if "domain" in problem.name:
                continue
            ladders = _scan(domain_name, problem)
            if ladders is None:
                print(f"# {domain_name}/{problem.name}: translation failed", flush=True)
            elif ladders:
                print(f"{domain_name}/{problem.name}", flush=True)


def _scan(domain_name, problem):
    """Translate one problem and report the ladders its variables hold, or None if it fails."""
    with tempfile.TemporaryDirectory() as base_dir:
        try:
            sas = pddl_to_sas(base_dir, _find_domain(problem), problem, f"{domain_name}/{problem.name}")
        except Exception:
            return None
        return _find_sas_ladders(read_sas(Path(sas).read_text(encoding="utf-8")))


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmarks", default=BENCHMARKS_DIR, help="Directory holding the benchmark domains")
    return parser


if __name__ == "__main__":
    main()
