"""Run one benchmark mode, for a plan or for a solvability verdict."""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from core.outcomes import STATUS_BY_EXIT_CODE
from experiments import read_classes
from scripts.utils.arguments import positive_int

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "runs"
DEFAULT_TIMEOUT = 30 * 60
MANIFEST_NAME = "manifest.json"
# Every way one problem gets solved, in the order a report reads them.
MODES = ("abstract", "concrete", "lama")
PIPELINE_MODULES = {"plan": "scripts.planner", "decide": "scripts.unsolvability"}
# What a job with no class to collapse passes, since the cluster substitutes
# its arguments positionally and cannot leave one out.
NO_CLASS = "-"
NO_SYMMETRIES_MESSAGE = "PDDL Symmetries found no abstractable object classes"
SYMMETRY_TIMEOUT_MESSAGE = "PDDL Symmetries exceeded its"


def main():
    args = _argument_parser().parse_args()
    result = _run_task(
        args.mode,
        args.domain_name,
        args.domain,
        args.problem,
        timeout=args.timeout,
        pipeline=args.pipeline,
        symmetry_class=args.symmetry_class,
        objects_to_abstract=_class_objects(args.classes, args.domain_name, args.problem, args.symmetry_class),
    )
    print(f"{args.domain_name}/{args.problem.name}: {_task_status(args.mode, result)}", flush=True)


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
        "--pipeline",
        choices=tuple(PIPELINE_MODULES),
        default="plan",
        help="plan searches for a plan; decide only reports whether the task is solvable",
    )
    # The cluster substitutes positionally, so a job with no class to collapse
    # still passes NO_CLASS rather than leaving the argument out.
    parser.add_argument(
        "--symmetry-class", type=_optional_index, default=None, help=f"Index of the collapsed class, or {NO_CLASS}"
    )
    # The objects themselves are looked up rather than passed: CopperBench
    # splits an instance parameter on commas, so a class of two objects arrived
    # as two parameters and the second landed on the end of the worker command.
    parser.add_argument("--classes", type=Path, help="Class manifest naming the objects of each class")
    return parser


def _optional_index(value):
    return None if value == NO_CLASS else int(value)


def _class_objects(classes_file, domain_name, problem, symmetry_class):
    """Name the objects of one class, or None where the planner picks its own."""
    if symmetry_class is None or classes_file is None:
        return None
    classes = read_classes(classes_file)
    if classes is None:
        raise SystemExit(f"Class manifest does not exist: {classes_file}")
    key = f"{domain_name}/{problem.name}"
    try:
        return tuple(classes[key][symmetry_class])
    except (KeyError, IndexError):
        raise SystemExit(f"{key} has no symmetry class {symmetry_class} in {classes_file}") from None


def _run_task(
    mode,
    domain_name,
    domain,
    problem,
    results_dir=RESULTS_DIR,
    timeout=None,
    pipeline="plan",
    symmetry_class=None,
    objects_to_abstract=None,
):
    # One class per file, or two classes of one problem overwrite each other.
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
        "pipeline": pipeline,
        "domain": domain_name,
        "problem": problem.name,
        "started_at": started_at,
        "progress": {"last_completed_phase": None, "last_update": None, "metrics": {}},
    }
    _write_result(result_file, initial)

    environment = os.environ.copy()
    environment["APF_BENCHMARK_RESULT_FILE"] = str(result_file)
    command = _planner_command(domain, problem, mode, pipeline, objects_to_abstract)
    result = _run_pipeline(command, timeout, environment)
    progress = _read_progress(result_file)
    result.update(
        {
            "mode": mode,
            "symmetry_class": symmetry_class,
            "pipeline": pipeline,
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
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
            timeout=timeout,
            env=environment,
        )
        return_code = completed.returncode
        output = completed.stdout or ""
        timed_out = False
    except subprocess.TimeoutExpired as error:
        return_code = None
        output = error.stdout or ""
        if isinstance(output, bytes):
            output = output.decode(errors="replace")
        timed_out = True
    except KeyboardInterrupt:
        # runsolver enforces its memory limit by sending SIGINT. Uncaught it
        # escapes before the result is written, leaving the "running" stub while
        # Slurm still records the job COMPLETED.
        return_code = None
        output = ""
        timed_out = False
        interrupted = True
    status = _machine_status(return_code, timed_out, output, interrupted)
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


def _machine_status(return_code, timed_out, output, interrupted=False):
    if interrupted:
        return "interrupted"
    if timed_out:
        return "timed_out"
    if return_code is not None and return_code < 0:
        return "killed"
    # These message checks classify results produced by an older planner CLI
    # during a rolling update of cluster workers.
    if NO_SYMMETRIES_MESSAGE in output:
        return "no_symmetries"
    if SYMMETRY_TIMEOUT_MESSAGE in output:
        return "symmetry_timeout"
    return STATUS_BY_EXIT_CODE.get(return_code, "error")


def _planner_command(domain, problem, mode, pipeline="plan", objects_to_abstract=None):
    module = PIPELINE_MODULES[pipeline]
    command = [sys.executable, "-m", module, mode, "--problem", str(problem), "--domain", str(domain)]
    if objects_to_abstract:
        command += ["--objects-to-abstract", *objects_to_abstract]
    return command


def _human_status(result):
    status = result.get("status") or _machine_status(
        result.get("return_code"), result.get("timed_out", False), result.get("output", "")
    )
    labels = {
        "success": "success",
        "no_plan": "no plan found",
        "no_symmetries": "no symmetries",
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
        signal_number = result.get("signal")
        if signal_number is None and result.get("return_code", 0) < 0:
            signal_number = -result["return_code"]
        return f"killed (signal {signal_number})"
    return f"error (exit code {result.get('return_code')})"


def _task_status(mode, result):
    return f"{mode} {_human_status(result)}"


if __name__ == "__main__":
    raise SystemExit(main())
