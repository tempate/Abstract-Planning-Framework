"""Collect benchmark result files into one CSV file."""

import csv
import json
import re
from pathlib import Path

from scripts.run_benchmarks import RESULTS_DIR, _human_status

CSV_FILE = RESULTS_DIR / "results.csv"
FIELDS = (
    "domain",
    "problem",
    "status",
    "return_code",
    "timed_out",
    "wall_time_seconds",
    "horizon",
    "plan_found",
    "refinement_iterations",
    "decrements",
    "planner_time_seconds",
    "concrete_status",
    "concrete_return_code",
    "concrete_timed_out",
    "concrete_wall_time_seconds",
    "concrete_horizon",
    "concrete_plan_found",
    "concrete_planner_time_seconds",
)


def value(output, label, convert=str):
    match = re.search(rf"^{re.escape(label)}: (.+)$", output, re.MULTILINE)
    return "" if match is None else convert(match.group(1))


def collect(results_dir=RESULTS_DIR):
    rows = []
    for result_file in sorted(Path(results_dir).glob("*/*.json")):
        result = json.loads(result_file.read_text(encoding="utf-8"))
        output = result["output"]
        row = {
            "domain": result["domain"],
            "problem": result["problem"],
            "status": _human_status(result),
            "return_code": result["return_code"],
            "timed_out": result.get("timed_out", False),
            "wall_time_seconds": result["wall_time_seconds"],
            "horizon": value(output, "Horizon", int),
            "plan_found": value(output, "Plan found"),
            "refinement_iterations": value(output, "Refinement iterations", int),
            "decrements": value(output, "Decrements", int),
            "planner_time_seconds": value(output, "Total time", lambda item: float(item.removesuffix("s"))),
            **_concrete_values(result.get("concrete")),
        }
        rows.append(row)
    return rows


def _concrete_values(result):
    if result is None:
        return {field: "" for field in FIELDS if field.startswith("concrete_")}

    output = result["output"]
    return {
        "concrete_status": _human_status(result),
        "concrete_return_code": result["return_code"],
        "concrete_timed_out": result.get("timed_out", False),
        "concrete_wall_time_seconds": result["wall_time_seconds"],
        "concrete_horizon": value(output, "Horizon", int),
        "concrete_plan_found": value(output, "Plan found"),
        "concrete_planner_time_seconds": value(output, "Total time", lambda item: float(item.removesuffix("s"))),
    }


def main():
    rows = collect()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_FILE.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Collected {len(rows)} results in {CSV_FILE}")


if __name__ == "__main__":
    main()
