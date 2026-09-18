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

from experiments.run import DEFAULT_TIMEOUT, MANIFEST_NAME, PROJECT_ROOT, RESULTS_DIR
from experiments.tracks import DEFAULT_TRACK, TRACKS
from scripts.utils.arguments import positive_int

DEFAULT_MEMORY_LIMIT = 8 * 1024
# CopperBench defaults to broadwell, so every run so far has gone there without
# this repository saying so, and queued behind it while sunnycove sat idle. Two
# things to know before raising --timeout or reading timings from an "any" run:
# the partition caps a job at one hour, and it spans both CPU generations, so
# wall-clock times are only comparable within one of them.
DEFAULT_PARTITION = "any"


def main():
    args = _argument_parser().parse_args()
    track = TRACKS[args.track]
    tasks = list(
        _benchmark_tasks(
            benchmarks_dir=track.suite.BENCHMARKS_DIR,
            suite=track.suite.SUITE,
            runnable=track.suite.SYMMETRIC_PROBLEMS,
            with_concrete=args.with_concrete,
        )
    )
    pipeline = track.pipeline
    _reset_results_dir()
    _write_manifest(tasks, pipeline=pipeline)
    with tempfile.TemporaryDirectory(prefix="apf-copperbench-") as definition_dir:
        config_file = _write_copperbench_config(
            tasks,
            definition_dir=definition_dir,
            timeout=args.timeout,
            memory_limit=args.memory_limit,
            max_parallel_jobs=args.max_parallel_jobs,
            partition=args.partition,
            pipeline=pipeline,
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


def _write_manifest(tasks, results_dir=RESULTS_DIR, pipeline="plan"):
    """Record every result expected from a submitted benchmark run."""
    expected_results = [
        {"domain": domain_name, "problem": problem.name, "mode": mode} for mode, domain_name, _domain, problem in tasks
    ]
    manifest = {"version": 1, "pipeline": pipeline, "expected_results": expected_results}
    path = Path(results_dir) / MANIFEST_NAME
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path


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
    parser.add_argument(
        "--partition", default=DEFAULT_PARTITION, help="Slurm partition to run every task of this run on"
    )
    parser.add_argument(
        "--with-concrete", action="store_true", help="Also submit the concrete pipeline for every problem"
    )
    parser.add_argument(
        "--track",
        choices=sorted(TRACKS),
        default=DEFAULT_TRACK,
        help="Benchmark track to submit: its problems, and the driver that runs them",
    )
    return parser


def _write_copperbench_config(
    tasks,
    definition_dir,
    timeout=DEFAULT_TIMEOUT,
    memory_limit=DEFAULT_MEMORY_LIMIT,
    max_parallel_jobs=None,
    partition=DEFAULT_PARTITION,
    pipeline="plan",
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
        "experiments.run",
        "$1",
        "--domain-name",
        "$2",
        "--domain",
        "$3",
        "--problem",
        "$4",
        "--timeout",
        "$timeout",
        "--pipeline",
        pipeline,
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
        "partition": partition,
        "request_cpus": 1,
        "working_dir": os.path.relpath(PROJECT_ROOT, definition_dir),
        "instances_are_parameters": True,
        "max_parallel_jobs": max_parallel_jobs,
    }
    config_file.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return config_file


def _benchmark_tasks(benchmarks_dir, suite, runnable, with_concrete=False):
    modes = ("abstract", "concrete") if with_concrete else ("abstract",)
    for domain_name in reversed(suite):
        directory = Path(benchmarks_dir) / domain_name
        for problem in sorted(directory.glob("*.pddl")):
            if _is_domain_file(problem.name) or _has_other_status(problem.name):
                continue
            if runnable is not None and (domain_name, problem.name) not in runnable:
                continue
            domain = _find_domain(problem)
            for mode in modes:
                yield mode, domain_name, domain, problem


def _is_domain_file(name):
    """Tell a domain file from a problem file by name.

    downward-benchmarks spells it out in full; unsolve-ipc-2016 shortens it to
    dom, satdom and unknowndom, against prob, satprob and unknownprob.
    """
    return "dom" in name and "prob" not in name


def _has_other_status(name):
    """Tell the problems standing around an unsolvable one from the problem itself.

    unsolve-ipc-2016 names probNN for the instances known to be unsolvable,
    satprobNN for the solvable twin beside it, and unknownprobNN for the ones
    nobody settled. Only the first is what this suite asks about.
    """
    return name.startswith(("satprob", "unknownprob"))


def _find_domain(problem):
    """Find the domain file using the naming conventions of the benchmark collections."""
    candidates = [
        "domain.pddl",
        f"{problem.stem}-domain{problem.suffix}",
        f"{problem.name[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    ]
    if "prob" in problem.stem:
        # unsolve-ipc-2016 names the pair after each other: probNN.pddl with
        # domNN.pddl, and likewise satprobNN and unknownprobNN. Guarded, or a
        # problem with no prob in its name would answer as its own domain.
        candidates.append(f"{problem.stem.replace('prob', 'dom', 1)}{problem.suffix}")
        # bag-barman and bag-transport ship no satdomNN, and their satprobNN is
        # probNN with a single symbol changed, so it belongs to the same domNN.
        # Last, or diagnosis and cave-diving would take domNN over their satdomNN.
        candidates.append(f"dom{problem.stem.partition('prob')[2]}{problem.suffix}")
    for name in candidates:
        domain = problem.parent / name
        if domain.is_file():
            return domain
    raise FileNotFoundError(f"No domain file found for {problem}")


if __name__ == "__main__":
    raise SystemExit(main())
