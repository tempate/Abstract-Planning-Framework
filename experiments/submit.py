"""Submit the complete benchmark suite to Slurm through CopperBench."""

import argparse
import json
import os
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from experiments.report import best_classes
from experiments.run import ABSTRACTION_PREFIX, DEFAULT_TIMEOUT, MANIFEST_NAME, MODES, PROJECT_ROOT, RESULTS_DIR
from experiments.tracks import DEFAULT_TRACK, TRACKS, find_domain, has_other_status, is_domain_file
from scripts.setup import ARTIFACTS, ROOT as SETUP_ROOT
from scripts.utils.arguments import positive_int

DEFAULT_MEMORY_LIMIT = 8 * 1024
# One CPU generation, so wall-clock times are comparable across a whole run. The
# "any" partition is not: it spans broadwell and sunnycove, and caps a job at one
# hour, which silently bounds --timeout.
DEFAULT_PARTITION = "sunnycove"
DEFAULT_SOURCE = DEFAULT_TRACK.split("/")[1]


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    track_name = _track_name(args, parser)
    track = TRACKS[track_name]
    modes = args.modes or track.modes[:1]
    unknown = sorted(set(modes) - set(track.modes))
    if unknown:
        parser.error(f"{track_name} has no mode {', '.join(unknown)}; it runs {', '.join(track.modes)}")
    tasks = list(
        _benchmark_tasks(
            benchmarks_dir=track.benchmarks_dir,
            suite=track.suite,
            runnable=None if args.all_problems else track.runnable(),
            modes=modes,
            domains=args.domains,
            problems=args.problems,
            class_counts=track.class_counts(),
            from_rank=args.from_rank,
            best=best_classes(track.results_file) if args.classes == "best" else None,
        )
    )
    if args.skip_manifests:
        tasks = _not_submitted(tasks, args.skip_manifests)
    _check_worktree_is_built()
    if not tasks:
        raise SystemExit(
            f"No problems found under {track.benchmarks_dir}. "
            "A worktree made without new-worktree.sh leaves the benchmark submodule empty."
        )
    if not args.dry_run:
        _set_aside_results_dir()
        _write_manifest(tasks, track=track_name)
    with tempfile.TemporaryDirectory(prefix="apf-copperbench-") as definition_dir:
        config_file = _write_copperbench_config(
            tasks,
            definition_dir=definition_dir,
            timeout=args.timeout,
            memory_limit=args.memory_limit,
            max_parallel_jobs=args.max_parallel_jobs,
            partition=args.partition,
            track=track_name,
        )
        if args.dry_run:
            _report_run(tasks, config_file, definition_dir)
            return
        print(f"Submitting {len(tasks)} cluster jobs (one per mode, benchmark problem and class)")
        subprocess.run(["copperbench", str(config_file), "--submit", "bench"], cwd=RESULTS_DIR, check=True)


def _not_submitted(tasks, manifests):
    """The tasks no earlier run's manifest lists, so that a second run adds to the first."""
    submitted = set()
    for manifest in manifests:
        for entry in json.loads(Path(manifest).read_text(encoding="utf-8"))["expected_results"]:
            submitted.add((entry["mode"], entry["domain"], entry["problem"], entry["class"]))
    return [task for task in tasks if (task[0], task[1], task[3].name, task[4]) not in submitted]


def _track_name(args, parser):
    """The track the arguments name: the question it answers and the source it abstracts."""
    track_name = f"{args.track}/{args.abstraction_source or DEFAULT_SOURCE}"
    if track_name not in TRACKS:
        parser.error(f"no track abstracts {args.abstraction_source} to answer {args.track}")
    return track_name


def _report_run(tasks, config_file, definition_dir):
    """Print what a submission would send, so a submit-side change can be checked for free."""
    definition_dir = Path(definition_dir)
    instances = (definition_dir / "instances.txt").read_text(encoding="utf-8").splitlines()
    print(f"Would submit {len(tasks)} cluster jobs (one per mode, benchmark problem and class)")
    print(config_file.read_text(encoding="utf-8").strip())
    print((definition_dir / "configs.txt").read_text(encoding="utf-8").strip())
    for instance in instances[:3]:
        print(f"  {instance}")
    if len(instances) > 3:
        print(f"  ... and {len(instances) - 3} more")


def _check_worktree_is_built(project_root=PROJECT_ROOT):
    """Refuse to submit from a worktree whose shared build artifacts are missing."""
    # A fresh worktree has none of what setup builds until new-worktree.sh links
    # it in, and a job without it dies long after the queue has drained.
    missing = []
    for name, path in ARTIFACTS.items():
        relative = path.relative_to(SETUP_ROOT)
        if not (Path(project_root) / relative).exists():
            missing.append(f"  {name} ({relative})")
    if missing:
        raise SystemExit("Nothing to run with; this worktree is missing:\n" + "\n".join(missing))


def _set_aside_results_dir(results_dir=RESULTS_DIR):
    """Give the run an empty directory, renaming what the previous one left.

    Until a run is pulled, its results directory is the only copy of it. The
    directory still has to start empty, because collect reads every result
    under it.
    """
    results_dir = Path(results_dir)
    if results_dir.is_symlink() or results_dir.is_file():
        results_dir.unlink()
    elif results_dir.exists():
        if any(results_dir.iterdir()):
            kept = results_dir.with_name(datetime.now().strftime(f"{results_dir.name}-%Y%m%d-%H%M%S"))
            results_dir.rename(kept)
            print(f"Kept the previous results in {kept}")
        else:
            results_dir.rmdir()
    results_dir.mkdir(parents=True)
    return results_dir


def _write_manifest(tasks, results_dir=RESULTS_DIR, track=DEFAULT_TRACK):
    """Record every result expected from a submitted benchmark run, and the code that runs it."""
    expected_results = [
        {"domain": domain_name, "problem": problem.name, "mode": mode, "class": rank}
        for mode, domain_name, _domain, problem, rank in tasks
    ]
    manifest = {"version": 1, "track": track, "commit": _head_commit(), "expected_results": expected_results}
    path = Path(results_dir) / MANIFEST_NAME
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path


def _head_commit():
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, capture_output=True, text=True, check=True
    )
    return completed.stdout.strip()


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
        "--modes",
        nargs="+",
        choices=MODES,
        help="Ways to solve every problem, one cluster job each, by default the track's first mode",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build the run definition and print it without submitting, and without touching the results directory",
    )
    parser.add_argument(
        "--domains", nargs="+", help="Submit only these domains of the track's suite, instead of all of them"
    )
    parser.add_argument(
        "--problems", nargs="+", help="Submit only these problem files, named p01.pddl or p01, within each domain"
    )
    parser.add_argument(
        "--from-rank",
        type=int,
        default=0,
        help="Run abstract modes only on the classes from this rank down, to skip those already collected",
    )
    parser.add_argument(
        "--skip-manifests",
        nargs="+",
        type=Path,
        help="Leave out every mode, problem and class these earlier runs' manifests list",
    )
    parser.add_argument(
        "--classes",
        choices=("all", "best"),
        default="best",
        help="Run abstract modes only on the class each did best with in the track's results, or on every class",
    )
    parser.add_argument(
        "--all-problems",
        action="store_true",
        help="Submit every problem of the suite, not only the ones the track lists as runnable",
    )
    parser.add_argument(
        "--track",
        choices=sorted({name.split("/")[0] for name in TRACKS}),
        default=DEFAULT_TRACK.split("/")[0],
        help="What the run asks of each problem: a plan (sat), an optimal plan (opt), or a proof that none exists (unsat)",
    )
    parser.add_argument(
        "--abstraction-source",
        choices=sorted({name.split("/")[1] for name in TRACKS if "/" in name}),
        help=f"What the modes through an abstraction collapse, for sat only (default: {DEFAULT_SOURCE})",
    )
    return parser


def _write_copperbench_config(
    tasks,
    definition_dir,
    timeout=DEFAULT_TIMEOUT,
    memory_limit=DEFAULT_MEMORY_LIMIT,
    max_parallel_jobs=None,
    partition=DEFAULT_PARTITION,
    track=DEFAULT_TRACK,
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
        "--track",
        track,
        "--class-rank",
        "$5",
    ]
    configs_file.write_text(shlex.join(worker) + "\n", encoding="utf-8")

    instances = []
    for mode, domain_name, domain, problem, rank in tasks:
        instances.append(f"{mode} {domain_name} {domain.resolve()} {problem.resolve()} {rank or 0}")
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


def _benchmark_tasks(
    benchmarks_dir,
    suite,
    runnable,
    modes=("abs-asp",),
    domains=None,
    problems=None,
    class_counts=None,
    from_rank=0,
    best=None,
):
    """One task per concrete mode and problem, and per abstract mode, problem and class rank.

    Without class counts, or for a problem they do not list, an abstract mode
    collapses the largest class only. With the best class of each abstract mode
    and problem, it runs that one class instead, and every class where none is known.
    """
    if domains is not None:
        unknown = sorted(set(domains) - set(suite))
        if unknown:
            raise SystemExit(f"Not in this track's suite: {', '.join(unknown)}")
        suite = [domain_name for domain_name in suite if domain_name in set(domains)]
    for domain_name in reversed(suite):
        directory = Path(benchmarks_dir) / domain_name
        for problem in sorted(directory.glob("*.pddl")):
            if is_domain_file(problem.name) or has_other_status(problem.name):
                continue
            if runnable is not None and (domain_name, problem.name) not in runnable:
                continue
            if problems is not None and not {problem.name, problem.stem} & set(problems):
                continue
            domain = find_domain(problem)
            for mode in modes:
                if not mode.startswith(ABSTRACTION_PREFIX):
                    yield mode, domain_name, domain, problem, None
                    continue
                count = 1 if class_counts is None else class_counts.get((domain_name, problem.name), 1)
                ranks = range(from_rank, count)
                if best is not None and (domain_name, problem.name, mode) in best:
                    ranks = [best[(domain_name, problem.name, mode)]]
                for rank in ranks:
                    yield mode, domain_name, domain, problem, rank


if __name__ == "__main__":
    raise SystemExit(main())
