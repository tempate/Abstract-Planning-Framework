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
)


def value(output, label, convert=str):
    match = re.search(rf"^{re.escape(label)}: (.+)$", output, re.MULTILINE)
    return "" if match is None else convert(match.group(1))


def collect(results_dir=RESULTS_DIR):
    rows = []
    for result_file in sorted(Path(results_dir).glob("*/*.json")):
        result = json.loads(result_file.read_text(encoding="utf-8"))
        output = result["output"]
        rows.append(
            {
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
            }
        )
    return rows


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
