"""Report planning progress to a benchmark result file and metrics to the terminal."""

import json
import os
from functools import partial
from pathlib import Path

from core.metrics import COUNTER_LABELS, DURATION_LABELS, RATIO_LABELS


def progress_callback():
    """Return the progress reporter for a benchmarked run, or None outside one."""
    result_file = os.environ.get("APF_BENCHMARK_RESULT_FILE")
    return partial(update_result_progress, result_file) if result_file else None


def update_result_progress(result_file, event, metrics):
    """Atomically store the latest planning progress in a benchmark result."""
    result_file = Path(result_file)
    try:
        result = json.loads(result_file.read_text(encoding="utf-8"))
        progress = result["progress"]
        if event["kind"] == "phase_completed":
            progress["last_completed_phase"] = event["phase"]
        progress["last_update"] = event
        progress["metrics"] = metrics
        temporary = result_file.with_suffix(".tmp")
        temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        temporary.replace(result_file)
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        # Progress reporting must never turn a successful planning run into a
        # failure. The benchmark wrapper will still write the final result.
        return


def print_metrics(metrics):
    """Print the durations, counters and ratios of a finished run."""
    print("\nMetrics:")
    _print_metric_group("Durations (seconds)", metrics["durations"], DURATION_LABELS, lambda value: f"{value:.6f}")
    _print_metric_group("Solver activity", metrics["counters"], COUNTER_LABELS, lambda value: str(int(value)))
    _print_metric_group("Class shape", metrics.get("ratios", {}), RATIO_LABELS, lambda value: f"{value:.6f}")


def _print_metric_group(title, values, labels, format_value):
    present = [(labels[name], format_value(values[name])) for name in labels if name in values]
    if not present:
        return

    width = max(len(label) for label, _ in present)
    print(f"  {title}:")
    for label, value in present:
        print(f"    {label:<{width}}  {value}")
