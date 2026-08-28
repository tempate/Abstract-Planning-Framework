"""Run abstract and eligible concrete comparisons across the benchmark suite."""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

from benchmarks.suite import BENCHMARKS_DIR, SUITE
from scripts.utils.arguments import positive_int

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "benchmark-results"
DEFAULT_TIMEOUT = 60
NO_SYMMETRIES_MESSAGE = "PDDL Symmetries found no abstractable object classes"


def main():
    args = _argument_parser().parse_args()
    print("Running benchmarks")

    for index, (domain_name, domain, problem) in enumerate(_benchmark_tasks(), 1):
        result = _run_task(domain_name, domain, problem, timeout=args.timeout)
        status = f"abstract {_human_status(result)}"
        if "concrete" in result:
            status += f", concrete {_human_status(result['concrete'])}"
        print(f"[{index}] {domain_name}/{problem.name}: {status}", flush=True)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--timeout", type=positive_int, default=DEFAULT_TIMEOUT, help="Maximum seconds for each benchmark"
    )
    return parser


def _benchmark_tasks(benchmarks_dir=BENCHMARKS_DIR, suite=SUITE, results_dir=RESULTS_DIR):
    for domain_name in reversed(suite):
        directory = Path(benchmarks_dir) / domain_name
        for problem in sorted(directory.glob("*.pddl")):
            result_file = Path(results_dir) / domain_name / f"{problem.stem}.json"
            if "domain" not in problem.name and not result_file.exists():
                yield domain_name, _find_domain(problem), problem


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


def _run_task(domain_name, domain, problem, results_dir=RESULTS_DIR, timeout=None):
    result_file = Path(results_dir) / domain_name / f"{problem.stem}.json"

    command = _planner_command(domain, problem, "abstract")
    result = _run_pipeline(command, timeout)
    result["domain"] = domain_name
    result["problem"] = problem.name

    if NO_SYMMETRIES_MESSAGE not in result["output"]:
        command = _planner_command(domain, problem, "concrete")
        result["concrete"] = _run_pipeline(command, timeout)

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


if __name__ == "__main__":
    raise SystemExit(main())
