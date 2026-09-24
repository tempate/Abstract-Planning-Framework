"""Run one benchmark mode, for a plan or for a solvability verdict."""

import argparse
import json
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from core.outcomes import STATUS_BY_EXIT_CODE
from experiments.tracks import DEFAULT_TRACK, TRACKS
from scripts.utils.arguments import positive_int

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "runs"
DEFAULT_TIMEOUT = 30 * 60
MANIFEST_NAME = "manifest.json"
# Every way one problem gets solved, in the order a report reads them. A mode
# names the solver that finds the plan, or through an abstraction the abstract
# plan, which ASP then refines.
MODES = ("abstraction-asp", "abstraction-fd", "asp", "fd")
ABSTRACTION_PREFIX = "abstraction-"
# What a job that collapses no given class passes, since the cluster substitutes
# its arguments positionally and cannot leave one out.
NO_CLASS = "-"


def main():
    args = _argument_parser().parse_args()
    result = _run_task(
        args.mode,
        args.domain_name,
        args.domain,
        args.problem,
        timeout=args.timeout,
        track=args.track,
        symmetry_class=args.symmetry_class,
    )
    print(f"{args.domain_name}/{args.problem.name}: {args.mode} {_human_status(result)}", flush=True)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=MODES, help="How to solve the task")
    parser.add_argument("--domain-name", required=True, help="Benchmark-suite domain name")
    parser.add_argument("--domain", required=True, type=Path, help="Domain PDDL file")
    parser.add_argument("--problem", required=True, type=Path, help="Problem PDDL file")
    parser.add_argument(
        "--timeout", type=positive_int, default=DEFAULT_TIMEOUT, help="Wall-clock limit in seconds for this pipeline"
    )
    parser.add_argument(
        "--track",
        choices=sorted(TRACKS),
        default=DEFAULT_TRACK,
        help="Track the problem belongs to, which names the driver that runs it",
    )
    parser.add_argument(
        "--symmetry-class",
        type=_optional_index,
        default=None,
        help=f"Position of the class to collapse in the track's classes.json, or {NO_CLASS} to let the driver choose",
    )
    return parser


def _optional_index(value):
    return None if value == NO_CLASS else int(value)


def _run_task(
    mode, domain_name, domain, problem, results_dir=RESULTS_DIR, timeout=None, track=DEFAULT_TRACK, symmetry_class=None
):
    # One file per class, or two classes of one problem overwrite each other.
    stem = mode if symmetry_class is None else f"{mode}-{symmetry_class}"
    result_file = Path(results_dir) / domain_name / problem.stem / f"{stem}.json"
    result_file.parent.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()
    initial = {
        "status": "running",
        "return_code": None,
        "timed_out": False,
        "wall_time_seconds": 0.0,
        "output": "",
        "mode": mode,
        "symmetry_class": symmetry_class,
        "track": track,
        "domain": domain_name,
        "problem": problem.name,
        "started_at": started_at,
        "progress": {"last_completed_phase": None, "last_update": None, "metrics": {}},
    }
    _write_result(result_file, initial)

    environment = os.environ.copy()
    environment["APF_BENCHMARK_RESULT_FILE"] = str(result_file)
    objects = None if symmetry_class is None else _class_objects(track, domain_name, problem, symmetry_class)
    command = _planner_command(domain, problem, mode, track, objects)
    result = _run_pipeline(command, timeout, environment)
    progress = _read_progress(result_file)
    result.update(
        {
            "mode": mode,
            "symmetry_class": symmetry_class,
            "track": track,
            "domain": domain_name,
            "problem": problem.name,
            "started_at": started_at,
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "progress": progress,
        }
    )

    _write_result(result_file, result)
    return result


def _write_result(result_file, result):
    temporary = result_file.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(result_file)


def _read_progress(result_file):
    try:
        return json.loads(result_file.read_text(encoding="utf-8")).get("progress", {})
    except (OSError, json.JSONDecodeError):
        return {}


def _run_pipeline(command, timeout, environment=None):
    started = time.perf_counter()
    interrupted = False
    # Its own session, so that the timeout can take down everything the planner
    # spawned. Killing the process we started leaves Fast Downward, its
    # translator, plasp and symmetry discovery holding the CPU they were given.
    process = subprocess.Popen(
        command,
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=environment,
        start_new_session=True,
    )
    try:
        output = process.communicate(timeout=timeout)[0] or ""
        return_code = process.returncode
        timed_out = False
    except subprocess.TimeoutExpired:
        return_code = None
        output = _kill_process_group(process)
        timed_out = True
    except KeyboardInterrupt:
        # runsolver enforces its memory limit by sending SIGINT. Uncaught it
        # escapes before the result is written, leaving the "running" stub while
        # Slurm still records the job COMPLETED.
        output = _kill_process_group(process)
        return_code = None
        timed_out = False
        interrupted = True
    status = _machine_status(return_code, timed_out, interrupted)
    result = {
        "status": status,
        "return_code": return_code,
        "timed_out": timed_out,
        "wall_time_seconds": time.perf_counter() - started,
        "output": output,
    }
    if status == "killed":
        result["signal"] = -return_code
    return result


def _kill_process_group(process):
    """Kill everything the pipeline spawned, and read what it had written."""
    try:
        # start_new_session made the process its own leader, so its pid is the
        # group every descendant inherited.
        os.killpg(process.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        process.kill()
    return process.communicate()[0] or ""


def _machine_status(return_code, timed_out, interrupted=False):
    if interrupted:
        return "interrupted"
    if timed_out:
        return "timed_out"
    if return_code is not None and return_code < 0:
        return "killed"
    return STATUS_BY_EXIT_CODE.get(return_code, "error")


def _class_objects(track, domain_name, problem, symmetry_class):
    """Name the objects of one class, looked up because CopperBench splits an instance parameter on commas."""
    key = f"{domain_name}/{problem.name}"
    try:
        return tuple(TRACKS[track].classes()[key][symmetry_class])
    except (TypeError, KeyError, IndexError):
        raise SystemExit(f"{key} has no symmetry class {symmetry_class} in {TRACKS[track].classes_file}") from None


def _planner_command(domain, problem, mode, track=DEFAULT_TRACK, objects=None):
    command = [sys.executable, "-m", TRACKS[track].driver, mode, "--problem", str(problem), "--domain", str(domain)]
    if mode.startswith(ABSTRACTION_PREFIX):
        command.extend(TRACKS[track].abstract_arguments)
    if objects:
        command.extend(["--objects-to-abstract", *objects])
    return command


def _human_status(result):
    status = result["status"]
    labels = {
        "success": "success",
        "no_plan": "no plan found",
        "no_symmetries": "no symmetries",
        "no_resources": "no resources",
        "symmetry_timeout": "symmetry timeout",
        "timed_out": "timed out",
        "running": "running",
        "missing": "missing",
        "interrupted": "interrupted",
        "out_of_memory": "out of memory",
    }
    if status in labels:
        return labels[status]
    if status == "killed":
        return f"killed (signal {result['signal']})"
    return f"error (exit code {result.get('return_code')})"


if __name__ == "__main__":
    raise SystemExit(main())
