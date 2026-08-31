"""Submit the complete benchmark suite to Slurm through CopperBench."""

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from benchmarks.suite import BENCHMARKS_DIR, SUITE
from scripts.run_benchmark import DEFAULT_TIMEOUT, PROJECT_ROOT, RESULTS_DIR
from scripts.utils.arguments import positive_int

DEFAULT_MEMORY_LIMIT = 8 * 1024


def main():
    args = _argument_parser().parse_args()
    tasks = list(_benchmark_tasks())
    _reset_results_dir()
    with tempfile.TemporaryDirectory(prefix="apf-copperbench-") as definition_dir:
        config_file = _write_copperbench_config(
            tasks,
            definition_dir=definition_dir,
            timeout=args.timeout,
            memory_limit=args.memory_limit,
            max_parallel_jobs=args.max_parallel_jobs,
        )
        print(f"Submitting {len(tasks)} cluster jobs (one per mode and benchmark problem)")
        subprocess.run(["copperbench", str(config_file), "--submit", "bench"], cwd=RESULTS_DIR, check=True)


def _reset_results_dir(results_dir=RESULTS_DIR):
    """Replace the previous benchmark results with an empty directory."""
    results_dir = Path(results_dir)
    if results_dir.is_symlink() or results_dir.is_file():
        results_dir.unlink()
    elif results_dir.exists():
        shutil.rmtree(results_dir)
    results_dir.mkdir(parents=True)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--timeout",
        type=positive_int,
        default=DEFAULT_TIMEOUT,
        help="Wall-clock limit in seconds for each complete problem",
    )
    parser.add_argument(
        "--memory-limit", type=positive_int, default=DEFAULT_MEMORY_LIMIT, help="Memory limit in MiB for each problem"
    )
    parser.add_argument(
        "--max-parallel-jobs",
        type=positive_int,
        help="Maximum number of CopperBench array tasks allowed to run concurrently",
    )
    return parser


def _write_copperbench_config(
    tasks, definition_dir, timeout=DEFAULT_TIMEOUT, memory_limit=DEFAULT_MEMORY_LIMIT, max_parallel_jobs=None
):
    """Write the files CopperBench needs to submit one job per problem."""
    definition_dir = Path(definition_dir)
    run_name = datetime.now().strftime("run-%Y%m%d-%H%M%S-%f")

    configs_file = definition_dir / "configs.txt"
    instances_file = definition_dir / "instances.txt"
    config_file = definition_dir / "copperbench.json"

    worker = [
        sys.executable,
        "-m",
        "scripts.run_benchmark",
        "$1",
        "--domain-name",
        "$2",
        "--domain",
        "$3",
        "--problem",
        "$4",
        "--timeout",
        "$timeout",
    ]
    configs_file.write_text(shlex.join(worker) + "\n", encoding="utf-8")

    instances = []
    for mode, domain_name, domain, problem in tasks:
        instances.append(f"{mode} {domain_name} {domain.resolve()} {problem.resolve()}")
    instances_file.write_text("\n".join(instances) + "\n", encoding="utf-8")

    config = {
        "name": run_name,
        "configs": configs_file.name,
        "instances": instances_file.name,
        "timeout": timeout,
        "mem_limit": memory_limit,
        "request_cpus": 1,
        "working_dir": os.path.relpath(PROJECT_ROOT, definition_dir),
        "instances_are_parameters": True,
        "max_parallel_jobs": max_parallel_jobs,
    }
    config_file.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return config_file


def _benchmark_tasks(benchmarks_dir=BENCHMARKS_DIR, suite=SUITE):
    for domain_name in reversed(suite):
        directory = Path(benchmarks_dir) / domain_name
        for problem in sorted(directory.glob("*.pddl")):
            if "domain" not in problem.name:
                domain = _find_domain(problem)
                for mode in ("abstract", "concrete"):
                    yield mode, domain_name, domain, problem


def _find_domain(problem):
    """Find the domain file using the naming conventions in downward-benchmarks."""
    candidates = (
        "domain.pddl",
        f"{problem.stem}-domain{problem.suffix}",
        f"{problem.name[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    )
    for name in candidates:
        domain = problem.parent / name
        if domain.is_file():
            return domain
    raise FileNotFoundError(f"No domain file found for {problem}")


if __name__ == "__main__":
    raise SystemExit(main())
