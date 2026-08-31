"""Run one abstract benchmark and its eligible concrete comparison."""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

from scripts.utils.arguments import positive_int

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "benchmark-results"
DEFAULT_TIMEOUT = 30 * 60
NO_SYMMETRIES_MESSAGE = "PDDL Symmetries found no abstractable object classes"


def main():
    args = _argument_parser().parse_args()
    result = _run_task(args.domain_name, args.domain, args.problem, timeout=args.timeout)
    print(f"{args.domain_name}/{args.problem.name}: {_task_status(result)}", flush=True)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain-name", required=True, help="Benchmark-suite domain name")
    parser.add_argument("--domain", required=True, type=Path, help="Domain PDDL file")
    parser.add_argument("--problem", required=True, type=Path, help="Problem PDDL file")
    parser.add_argument(
        "--timeout",
        type=positive_int,
        default=DEFAULT_TIMEOUT,
        help="Wall-clock limit in seconds for the complete problem",
    )
    return parser


def _run_task(domain_name, domain, problem, results_dir=RESULTS_DIR, timeout=None):
    result_file = Path(results_dir) / domain_name / f"{problem.stem}.json"
    started = time.perf_counter() if timeout is not None else None

    command = _planner_command(domain, problem, "abstract")
    result = _run_pipeline(command, timeout)
    result["domain"] = domain_name
    result["problem"] = problem.name

    if NO_SYMMETRIES_MESSAGE not in result["output"]:
        remaining = None if timeout is None else timeout - (time.perf_counter() - started)
        if remaining is not None and remaining <= 0:
            result["concrete"] = _exhausted_timeout_result()
        else:
            command = _planner_command(domain, problem, "concrete")
            result["concrete"] = _run_pipeline(command, remaining)

    result_file.parent.mkdir(parents=True, exist_ok=True)
    temporary = result_file.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(result_file)
    return result


def _exhausted_timeout_result():
    return {
        "return_code": None,
        "timed_out": True,
        "wall_time_seconds": 0.0,
        "output": "Problem time limit exhausted before the concrete comparison\n",
    }


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
        output = completed.stdout
        timed_out = False
    except subprocess.TimeoutExpired as error:
        return_code = None
        output = error.stdout or ""
        if isinstance(output, bytes):
            output = output.decode(errors="replace")
        timed_out = True
    return {
        "return_code": return_code,
        "timed_out": timed_out,
        "wall_time_seconds": time.perf_counter() - started,
        "output": output,
    }


def _planner_command(domain, problem, mode):
    return [sys.executable, "-m", "scripts.planner", mode, "--problem", str(problem), "--domain", str(domain)]


def _human_status(result):
    if result["timed_out"]:
        return "timed out"
    if NO_SYMMETRIES_MESSAGE in result["output"]:
        return "no symmetries"
    if result["return_code"] == 0:
        return "success"
    if result["return_code"] == 1:
        return "no plan found"
    return f"error (exit code {result['return_code']})"


def _task_status(result):
    status = f"abstract {_human_status(result)}"
    if "concrete" in result:
        status += f", concrete {_human_status(result['concrete'])}"
    return status


if __name__ == "__main__":
    raise SystemExit(main())
