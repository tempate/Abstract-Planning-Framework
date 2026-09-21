"""Collect benchmark result files into one CSV file."""

import argparse
import ast
from collections import Counter
import csv
import json
import re
from pathlib import Path

from core.metrics import COUNTER_LABELS, DURATION_LABELS
from experiments.run import MANIFEST_NAME, MODES, PROJECT_ROOT, RESULTS_DIR, _human_status
from experiments.tracks import DEFAULT_TRACK, TRACKS

# The raw run output stays in the untracked results directory; the collected CSV
# is the artifact that gets committed and reported on.
CSV_FILE = TRACKS[DEFAULT_TRACK].results_file
DURATION_FIELDS = tuple(f"{name}_seconds" for name in DURATION_LABELS)
FIELDS = (
    "domain",
    "problem",
    "mode",
    "status",
    "wall_time_seconds",
    "last_completed_phase",
    *DURATION_FIELDS,
    "verdict",
    "plan_valid",
    *COUNTER_LABELS,
    "abstracted_object_count",
    "abstracted_object_type",
    "error_message",
)


def _value(output, label, convert=str):
    match = re.search(rf"^{re.escape(label)}: (.+)$", output, re.MULTILINE)
    return "" if match is None else convert(match.group(1))


def collect(*results_dirs):
    """Collect one run, or several merged into one set of rows.

    A run that filled another's gaps is collected by naming both: the later
    directory wins where the two hold the same result, and the expected results
    are the union of their manifests.
    """
    results = {}
    keys = set()
    for results_dir in results_dirs or (RESULTS_DIR,):
        results_dir = Path(results_dir)
        for result_file in sorted(results_dir.rglob("*.json")):
            if result_file.name in ("metadata.json", MANIFEST_NAME):
                continue
            result = json.loads(result_file.read_text(encoding="utf-8"))
            if not {"domain", "problem", "output"} <= result.keys():
                continue

            mode = result.get("mode")
            if mode in MODES:
                results[(result["domain"], result["problem"], mode)] = result
            else:
                # Results produced before modes became separate jobs stored the
                # concrete comparison inside the abstract result.
                results.setdefault((result["domain"], result["problem"], "abstract"), result)
                if "concrete" in result:
                    results.setdefault((result["domain"], result["problem"], "concrete"), result["concrete"])

        manifest = results_dir / MANIFEST_NAME
        if manifest.is_file():
            keys.update(_manifest_keys(manifest))

    keys.update(results)

    rows = []
    for domain, problem, mode in sorted(keys):
        result = results.get((domain, problem, mode))
        values = _missing_values() if result is None else _values(result)
        rows.append({"domain": domain, "problem": problem, "mode": mode, **values})
    return rows


def _manifest_keys(manifest):
    entries = json.loads(manifest.read_text(encoding="utf-8"))["expected_results"]
    return {(entry["domain"], entry["problem"], entry["mode"]) for entry in entries if entry["mode"] in MODES}


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
        "verdict": _value(output, "Verdict"),
        "plan_valid": _value(output, "Plan valid"),
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
        elif name == "plan_length":
            # Runs from before this was a counter only printed the plan itself.
            values[name] = _plan_length(output)
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
    """Read the collapsed class, falling back to the line older planners only printed."""
    if abstraction:
        return {
            "abstracted_object_count": len(abstraction["objects"]),
            "abstracted_object_type": abstraction["object_type"],
        }

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
    # Fast Downward capitalizes its Error:, so a case-sensitive match falls
    # through to the last line, which is the planner's timing summary.
    match = re.search(r"^.*error: (.+)$", output, re.MULTILINE | re.IGNORECASE)
    if match is not None:
        return match.group(1)

    lines = [line.strip() for line in output.splitlines() if line.strip() and line.strip() != "Starting"]
    return lines[-1] if lines else ""


def _key(row):
    return (row["domain"], row["problem"], row["mode"])


def _preserved_rows(collected, csv_file=CSV_FILE):
    """Read the results of the modes this run left alone, so it cannot erase them.

    A run submits the modes it is interested in, and the others keep whatever
    the CSV already holds: submitting only a baseline must not drop the
    abstract results, and re-running the abstract pipeline must not leave
    behind rows from the encoding before it.  What a run submitted is what it
    collected, the manifest included, so the modes it did not is the rest.
    """
    csv_file = Path(csv_file)
    if not csv_file.is_file():
        return []

    submitted = {row["mode"] for row in collected}

    preserved = []
    with csv_file.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row["mode"] in submitted:
                continue
            kept = {}
            for field in FIELDS:
                kept[field] = row.get(field, "")
            preserved.append(kept)
    return preserved


def main(results_dirs=RESULTS_DIR, csv_file=CSV_FILE):
    if isinstance(results_dirs, (str, Path)):
        results_dirs = [results_dirs]
    collected = collect(*results_dirs)
    preserved = _preserved_rows(collected, csv_file)
    rows = sorted(collected + preserved, key=_key)
    csv_file = Path(csv_file)
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    with csv_file.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    missing = Counter(row["mode"] for row in collected if row["status"] == "missing")
    if missing:
        details = ", ".join(f"{mode}: {count}" for mode, count in sorted(missing.items()))
        print(f"Incomplete benchmark run: {sum(missing.values())} expected results are missing ({details})")
    if preserved:
        print(f"Kept {len(preserved)} results from modes the run did not submit")
    print(f"Collected {len(rows)} results in {csv_file}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "results_dirs",
        nargs="*",
        type=Path,
        default=[RESULTS_DIR],
        help="Result directories to collect; where two hold the same result, the later one wins",
    )
    parser.add_argument("--csv", default=CSV_FILE, help="CSV file to collect the results into")
    return parser


if __name__ == "__main__":
    args = _argument_parser().parse_args()
    main(args.results_dirs, args.csv)
