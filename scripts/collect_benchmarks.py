"""Collect benchmark result files into one CSV file."""

import ast
import csv
import json
import re
from pathlib import Path

from scripts.run_benchmark import RESULTS_DIR, _human_status

CSV_FILE = RESULTS_DIR / "results.csv"
FIELDS = (
    "domain",
    "problem",
    "mode",
    "status",
    "wall_time_seconds",
    "planner_time_seconds",
    "horizon",
    "plan_length",
    "decrements",
    "abstracted_object_count",
    "abstracted_object_type",
    "error_message",
)


def value(output, label, convert=str):
    match = re.search(rf"^{re.escape(label)}: (.+)$", output, re.MULTILINE)
    return "" if match is None else convert(match.group(1))


def collect(results_dir=RESULTS_DIR):
    results = {}
    for result_file in sorted(Path(results_dir).rglob("*.json")):
        if result_file.name == "metadata.json":
            continue
        result = json.loads(result_file.read_text(encoding="utf-8"))
        if not {"domain", "problem", "output"} <= result.keys():
            continue

        mode = result.get("mode")
        if mode in ("abstract", "concrete"):
            results[(result["domain"], result["problem"], mode)] = result
        else:
            # Results produced before modes became separate jobs stored the
            # concrete comparison inside the abstract result.
            results.setdefault((result["domain"], result["problem"], "abstract"), result)
            if "concrete" in result:
                results.setdefault((result["domain"], result["problem"], "concrete"), result["concrete"])

    return [
        {"domain": domain, "problem": problem, "mode": mode, **_values(result)}
        for (domain, problem, mode), result in sorted(results.items())
    ]


def _values(result):
    output = result["output"]
    return {
        "status": _human_status(result),
        "wall_time_seconds": result["wall_time_seconds"],
        "planner_time_seconds": value(output, "Total time", lambda item: float(item.removesuffix("s"))),
        "horizon": value(output, "Horizon", int),
        "plan_length": _plan_length(output),
        "decrements": value(output, "Decrements", int),
        **_abstraction_values(output),
        "error_message": _error_message(result),
    }


def _plan_length(output):
    if value(output, "Plan found") != "yes":
        return ""
    return len(re.findall(r"^[ \t]+occurs\(", output, re.MULTILINE))


def _abstraction_values(output):
    match = re.search(r"^Collapsed (\[.*\]) into \S+ \(type=([^)]+)\)$", output, re.MULTILINE)
    if match is None:
        return {"abstracted_object_count": "", "abstracted_object_type": ""}

    try:
        object_count = len(ast.literal_eval(match.group(1)))
    except (SyntaxError, ValueError):
        object_count = ""
    return {"abstracted_object_count": object_count, "abstracted_object_type": match.group(2)}


def _error_message(result):
    if not _human_status(result).startswith("error"):
        return ""

    output = result["output"]
    match = re.search(r"^.*error: (.+)$", output, re.MULTILINE)
    if match is not None:
        return match.group(1)

    lines = [line.strip() for line in output.splitlines() if line.strip() and line.strip() != "Starting"]
    return lines[-1] if lines else ""


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
