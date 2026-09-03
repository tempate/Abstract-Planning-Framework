"""Collect benchmark result files into one CSV file."""

import ast
from collections import Counter
import csv
import json
import re
from pathlib import Path

from core.metrics import COUNTER_NAMES, DURATION_NAMES
from scripts.run_benchmark import MANIFEST_NAME, RESULTS_DIR, _human_status

CSV_FILE = RESULTS_DIR / "results.csv"
DURATION_FIELDS = tuple(f"{name}_seconds" for name in DURATION_NAMES)
FIELDS = (
    "domain",
    "problem",
    "mode",
    "status",
    "wall_time_seconds",
    *DURATION_FIELDS,
    "horizon",
    "plan_length",
    *COUNTER_NAMES,
    "abstracted_object_count",
    "abstracted_object_type",
    "error_message",
)


def value(output, label, convert=str):
    match = re.search(rf"^{re.escape(label)}: (.+)$", output, re.MULTILINE)
    return "" if match is None else convert(match.group(1))


def collect(results_dir=RESULTS_DIR):
    results_dir = Path(results_dir)
    results = {}
    for result_file in sorted(results_dir.rglob("*.json")):
        if result_file.name in ("metadata.json", MANIFEST_NAME):
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

    keys = set(results)
    manifest = results_dir / MANIFEST_NAME
    if manifest.is_file():
        keys.update(_manifest_keys(manifest))

    rows = []
    for domain, problem, mode in sorted(keys):
        result = results.get((domain, problem, mode))
        values = _missing_values() if result is None else _values(result)
        rows.append({"domain": domain, "problem": problem, "mode": mode, **values})
    return rows


def _manifest_keys(manifest):
    entries = json.loads(manifest.read_text(encoding="utf-8"))["expected_results"]
    return {
        (entry["domain"], entry["problem"], entry["mode"])
        for entry in entries
        if entry["mode"] in ("abstract", "concrete")
    }


def _missing_values():
    return {field: "" for field in FIELDS[4:]} | {"status": "missing"}


def _values(result):
    output = result["output"]
    metrics = _metrics(output)
    durations = metrics.get("durations", {})
    counters = metrics.get("counters", {})
    return {
        "status": _human_status(result),
        "wall_time_seconds": result["wall_time_seconds"],
        **{f"{name}_seconds": durations.get(name, "") for name in DURATION_NAMES},
        "horizon": value(output, "Horizon", int),
        "plan_length": _plan_length(output),
        **{
            name: counters.get(name, value(output, name.title(), int) if name in ("decrements", "increments") else "")
            for name in COUNTER_NAMES
        },
        **_abstraction_values(output),
        "error_message": _error_message(result),
    }


def _metrics(output):
    match = re.search(r"^Metrics: (\{.*\})$", output, re.MULTILINE)
    if match is None:
        return {}
    try:
        metrics = json.loads(match.group(1))
    except json.JSONDecodeError:
        return {}
    return metrics if isinstance(metrics, dict) else {}


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
    missing = Counter(row["mode"] for row in rows if row["status"] == "missing")
    if missing:
        details = ", ".join(f"{mode}: {count}" for mode, count in sorted(missing.items()))
        print(f"Incomplete benchmark run: {sum(missing.values())} expected results are missing ({details})")
    print(f"Collected {len(rows)} results in {CSV_FILE}")


if __name__ == "__main__":
    main()
