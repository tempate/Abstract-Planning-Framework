"""Summarize a collected benchmark CSV as coverage and refinement tables."""

import argparse
import csv
import statistics
from pathlib import Path

from scripts.run_benchmark import PROJECT_ROOT

DEFAULT_CSV = PROJECT_ROOT / "benchmarks" / "results.csv"
UNFINISHED_STATUSES = ("running", "missing")
# A killed run reports the phase it completed last, so it died in the next one.
KILLED_IN_PHASE = {
    "abstract_asp": "Searching for the abstract plan",
    "abstract_solving": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}


def main():
    args = _argument_parser().parse_args()
    problems = _finished_problems(args.results)
    _print_coverage(problems)
    _print_head_to_head(problems)
    _print_timeout_phases(problems)
    _print_refinement_outcomes(problems)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", nargs="?", type=Path, default=DEFAULT_CSV, help="Collected benchmark CSV")
    return parser


def _finished_problems(results_file):
    """Pair both pipelines per problem, dropping problems either one has not finished."""
    rows = {}
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            rows.setdefault((row["domain"], row["problem"]), {})[row["mode"]] = row

    problems = []
    for modes in rows.values():
        if modes.keys() != {"abstract", "concrete"}:
            continue
        if modes["abstract"]["status"] in UNFINISHED_STATUSES or modes["concrete"]["status"] in UNFINISHED_STATUSES:
            continue
        problems.append(modes)
    return problems


def _print_coverage(problems):
    total = len(problems)
    found = _status_counts(problems, "success")
    timeouts = _status_counts(problems, "timed out")

    _print_wide_header("Table 1 — Coverage", "Metric")
    _print_wide("Plans found", _share(found["abstract"], total, 1), _share(found["concrete"], total, 1))
    _print_wide("Timeouts", _share(timeouts["abstract"], total, 1), _share(timeouts["concrete"], total, 1))
    _print_wide("Total problems", total, total)


def _print_head_to_head(problems):
    solved_by_both = [modes for modes in problems if _solved_by_both(modes)]
    shared = len(solved_by_both)
    faster = {"abstract": 0, "concrete": 0}
    for modes in solved_by_both:
        winner = "abstract" if _runtime(modes["abstract"]) < _runtime(modes["concrete"]) else "concrete"
        faster[winner] += 1

    abstract_times = [_runtime(modes["abstract"]) for modes in solved_by_both]
    concrete_times = [_runtime(modes["concrete"]) for modes in solved_by_both]
    found = _status_counts(problems, "success")

    _print_wide_header("Table 2 — Head to head", "Metric")
    _print_wide("Plans found by both pipelines", shared, shared)
    _print_wide(
        "Faster when both found a plan", _share(faster["abstract"], shared, 1), _share(faster["concrete"], shared, 1)
    )
    _print_wide("Plan found when the other did not", found["abstract"] - shared, found["concrete"] - shared)
    _print_wide(
        "Median runtime when both found a plan",
        _seconds(statistics.median(abstract_times)),
        _seconds(statistics.median(concrete_times)),
    )
    _print_wide("Total runtime across shared solves", _seconds(sum(abstract_times)), _seconds(sum(concrete_times)))


def _print_timeout_phases(problems):
    timeouts = [modes["abstract"] for modes in problems if modes["abstract"]["status"] == "timed out"]
    counts = {}
    for row in timeouts:
        phase = KILLED_IN_PHASE.get(row["last_completed_phase"], row["last_completed_phase"])
        counts[phase] = counts.get(phase, 0) + 1

    _print_narrow_header("Table 3 — Where the timeouts died", "Where the abstract pipeline was killed", "Timeouts")
    for phase, count in sorted(counts.items(), key=lambda item: -item[1]):
        _print_narrow(phase, _share(count, len(timeouts), 0))
    _print_narrow("Total", len(timeouts))


def _print_refinement_outcomes(problems):
    successes = [modes["abstract"] for modes in problems if modes["abstract"]["status"] == "success"]
    counts = {"refined": 0, "switched": 0, "discarded": 0}
    for row in successes:
        if int(row["increments"]) > 0:
            counts["discarded"] += 1
        elif int(row["decrements"]) > 0:
            counts["switched"] += 1
        else:
            counts["refined"] += 1

    total = len(successes)
    title = "Table 4 — How the successes were solved"
    _print_narrow_header(title, f"How the {total} successes were solved", "Problems")
    _print_narrow("Abstract plan refined directly", _share(counts["refined"], total, 0))
    _print_narrow("Refined after switching some actions off", _share(counts["switched"], total, 0))
    _print_narrow("Abstract plan discarded, solved above it", _share(counts["discarded"], total, 0))
    _print_narrow("Total", total)


def _solved_by_both(modes):
    return all(modes[mode]["status"] == "success" for mode in ("abstract", "concrete"))


def _runtime(row):
    return float(row["wall_time_seconds"])


def _status_counts(problems, status):
    counts = {"abstract": 0, "concrete": 0}
    for modes in problems:
        for mode in counts:
            if modes[mode]["status"] == status:
                counts[mode] += 1
    return counts


def _share(count, total, decimals):
    return f"{count} ({count / total:.{decimals}%})" if total else f"{count}"


def _seconds(value):
    return f"{value:,.2f} s"


def _print_wide_header(title, label):
    print(f"\n{title}\n")
    _print_wide(label, "Abstract pipeline", "Concrete pipeline")
    print("-" * 80)


def _print_wide(label, abstract, concrete):
    print(f"{label:<44}{abstract:>17}  {concrete:>17}")


def _print_narrow_header(title, label, value_label):
    print(f"\n{title}\n")
    _print_narrow(label, value_label)
    print("-" * 61)


def _print_narrow(label, value):
    print(f"{label:<45}{value:>16}")


if __name__ == "__main__":
    main()
