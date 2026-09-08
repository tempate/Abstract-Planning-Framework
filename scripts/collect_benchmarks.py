"""Collect benchmark result files into one CSV file."""

import ast
from collections import Counter
import csv
import json
import re
from pathlib import Path

from core.metrics import COUNTER_LABELS, DURATION_LABELS
from scripts.run_benchmark import MANIFEST_NAME, PROJECT_ROOT, RESULTS_DIR, _human_status

# The raw run output stays in the untracked results directory; the collected CSV
# is the artifact that gets committed and reported on.
CSV_FILE = PROJECT_ROOT / "benchmarks" / "results.csv"
DURATION_FIELDS = tuple(f"{name}_seconds" for name in DURATION_LABELS)
FIELDS = (
    "domain",
    "problem",
    "mode",
    "status",
    "wall_time_seconds",
    "last_completed_phase",
    *DURATION_FIELDS,
    "horizon",
    "plan_length",
    *COUNTER_LABELS,
    "abstracted_object_count",
    "abstracted_object_type",
    "abstracted_class_count",
    "error_message",
)


def _value(output, label, convert=str):
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
    progress = result.get("progress", {})
    metrics = _metrics(output, progress)
    durations = metrics.get("durations", {})
    counters = metrics.get("counters", {})
    return {
        "status": _human_status(result),
        "wall_time_seconds": result["wall_time_seconds"],
        "last_completed_phase": progress.get("last_completed_phase", ""),
        **{f"{name}_seconds": durations.get(name, "") for name in DURATION_LABELS},
        "horizon": _value(output, "Horizon", int),
        "plan_length": _plan_length(output),
        **_counter_values(output, counters),
        **_abstraction_values(output, metrics.get("abstraction")),
        "error_message": _error_message(result),
    }


def _counter_values(output, counters):
    """Read the counters, falling back to the two the oldest planner printed on their own line."""
    values = {}
    for name in COUNTER_LABELS:
        if name in counters:
            values[name] = counters[name]
        elif name in ("decrements", "increments"):
            values[name] = _value(output, name.title(), int)
        else:
            values[name] = ""
    return values


def _metrics(output, progress=None):
    # Read the compact JSON emitted by the first structured-metrics version.
    match = re.search(r"^Metrics: (\{.*\})$", output, re.MULTILINE)
    if match is not None:
        try:
            metrics = json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
        else:
            if isinstance(metrics, dict):
                return metrics

    metrics = {
        "durations": _metric_group(output, DURATION_LABELS, float),
        "counters": _metric_group(output, COUNTER_LABELS, int),
    }
    if metrics["durations"] or metrics["counters"]:
        return metrics
    if progress and isinstance(progress.get("metrics"), dict):
        return progress["metrics"]
    return metrics


def _metric_group(output, labels, conversion):
    values = {}
    for name, label in labels.items():
        match = re.search(rf"^    {re.escape(label)}  +(.+)$", output, re.MULTILINE)
        if match is not None:
            values[name] = conversion(match.group(1))
    return values


def _plan_length(output):
    if _value(output, "Plan found") != "yes":
        return ""
    return len(re.findall(r"^[ \t]+occurs\(", output, re.MULTILINE))


def _abstraction_values(output, abstraction=None):
    """Summarize the collapsed classes over every class the run reported."""
    classes = _collapsed_classes(output, abstraction)
    if not classes:
        return {"abstracted_object_count": "", "abstracted_object_type": "", "abstracted_class_count": ""}

    object_count = 0
    object_types = []
    for count, object_type in classes:
        if count == "":
            object_count = ""
        elif object_count != "":
            object_count += count
        if object_type not in object_types:
            object_types.append(object_type)
    return {
        "abstracted_object_count": object_count,
        "abstracted_object_type": "+".join(object_types),
        "abstracted_class_count": len(classes),
    }


def _collapsed_classes(output, abstraction):
    """Return (object count, type) per class, from the metrics snapshot or the printed lines."""
    if abstraction:
        # Runs before classes became plural stored a single class as one dict.
        entries = [abstraction] if isinstance(abstraction, dict) else abstraction
        classes = []
        for entry in entries:
            classes.append((len(entry["objects"]), entry["object_type"]))
        return classes

    classes = []
    for objects, object_type in re.findall(r"^Collapsed (\[.*\]) into \S+ \(type=([^)]+)\)$", output, re.MULTILINE):
        try:
            classes.append((len(ast.literal_eval(objects)), object_type))
        except (SyntaxError, ValueError):
            classes.append(("", object_type))
    return classes


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
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
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
