"""Console and spreadsheet reporting shared by planner entry points."""

import os

import pandas as pd

from core.paths import EXCEL_FILE


def print_planning_result(result, logger):
    """Print a result and log its high-level outcome."""
    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plans found: {result['numPlans']}")

    logger.info(f"Success: {result['success']}")
    logger.info(f"Plans found: {result['numPlans']}")

    for index, plan in enumerate(result["plans"], start=1):
        print(f"\nPlan {index}:")
        for atom in sorted(plan, key=_time_step):
            print(" ", atom)


def save_result_summary(problem_path, version, mode, result):
    """Store a normalized result summary, regardless of planner variant."""
    timings = result["timings"]
    _append_result({
        "Problem": os.path.basename(problem_path),
        "Version": version,
        "Mode": mode,
        "horizon": result["horizon"],
        "iterations": timings.get("iterations"),
        "fd_conc": _timing(timings, "fd_conc", "fd_concrete_time"),
        "fd_abs": _timing(timings, "fd_abs", "fd_abstract_time"),
        "fd_total": _timing(timings, "fd_total", "fd_total_time"),
        "lp_concrete_time": timings.get("lp_concrete_time"),
        "lp_abstract_time": timings.get("lp_abstract_time"),
        "lp_total_time": timings.get("lp_total_time"),
        "abstract_solve_time": timings.get("abstract_solve_time"),
        "concrete_solve_time": timings.get("concrete_solve_time"),
        "total": timings.get("total_time"),
        "result": "SAT" if result["success"] else "UNSAT",
        "id": timings.get("run_id"),
    })


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))


def _timing(timings, short_name, long_name):
    return timings.get(short_name, timings.get(long_name))


def _append_result(row):
    """Append one normalized result row to the experiment spreadsheet."""
    data = pd.DataFrame([row])
    if os.path.exists(EXCEL_FILE):
        existing = pd.read_excel(EXCEL_FILE)
        data = pd.concat([existing, data], ignore_index=True)
    data.to_excel(EXCEL_FILE, index=False)
