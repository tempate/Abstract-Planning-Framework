"""Run one concrete or abstract benchmark."""

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
    command = _planner_command(domain, problem, mode)
    result = _run_pipeline(command, timeout)
    result["mode"] = mode
    result["domain"] = domain_name
    result["problem"] = problem.name

    result_file.parent.mkdir(parents=True, exist_ok=True)
    temporary = result_file.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(result_file)
    return result


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


def _task_status(mode, result):
    return f"{mode} {_human_status(result)}"


if __name__ == "__main__":
    raise SystemExit(main())
