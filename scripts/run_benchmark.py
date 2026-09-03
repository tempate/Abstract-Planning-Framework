"""Run one concrete or abstract benchmark."""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from core.planning.outcomes import STATUS_BY_EXIT_CODE
from scripts.utils.arguments import positive_int

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "benchmark-results"
DEFAULT_TIMEOUT = 30 * 60
MANIFEST_NAME = "manifest.json"
NO_SYMMETRIES_MESSAGE = "PDDL Symmetries found no abstractable object classes"
SYMMETRY_TIMEOUT_MESSAGE = "PDDL Symmetries exceeded its"


def main():
    args = _argument_parser().parse_args()
    result = _run_task(args.mode, args.domain_name, args.domain, args.problem, timeout=args.timeout)
    print(f"{args.domain_name}/{args.problem.name}: {_task_status(args.mode, result)}", flush=True)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("concrete", "abstract"), help="Planning pipeline to benchmark")
    parser.add_argument("--domain-name", required=True, help="Benchmark-suite domain name")
    parser.add_argument("--domain", required=True, type=Path, help="Domain PDDL file")
    parser.add_argument("--problem", required=True, type=Path, help="Problem PDDL file")
    parser.add_argument(
        "--timeout", type=positive_int, default=DEFAULT_TIMEOUT, help="Wall-clock limit in seconds for this pipeline"
    )
    return parser


def _run_task(mode, domain_name, domain, problem, results_dir=RESULTS_DIR, timeout=None):
    result_file = Path(results_dir) / domain_name / problem.stem / f"{mode}.json"
    result_file.parent.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()
    initial = {
        "status": "running",
        "return_code": None,
        "timed_out": False,
        "wall_time_seconds": 0.0,
        "output": "",
        "mode": mode,
        "domain": domain_name,
        "problem": problem.name,
        "started_at": started_at,
        "progress": {"last_completed_phase": None, "metrics": {}},
    }
    _write_result(result_file, initial)

    command = _planner_command(domain, problem, mode, result_file)
    result = _run_pipeline(command, timeout)
    progress = _read_progress(result_file)
    result.update(
        {
            "mode": mode,
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


def _run_pipeline(command, timeout):
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
            timeout=timeout,
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
    status = _machine_status(return_code, timed_out, output)
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


def _machine_status(return_code, timed_out, output):
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


def _planner_command(domain, problem, mode, progress_file=None):
    command = [sys.executable, "-m", "scripts.planner", mode, "--problem", str(problem), "--domain", str(domain)]
    if progress_file is not None:
        command.extend(("--progress-file", str(progress_file)))
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
