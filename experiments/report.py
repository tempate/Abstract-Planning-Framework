"""Summarize a collected benchmark CSV, as plan coverage or as solvability verdicts."""

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path

from experiments.run import PROJECT_ROOT

DEFAULT_CSV = PROJECT_ROOT / "experiments" / "plan" / "results.csv"
REPORTS_FILE = PROJECT_ROOT / "experiments" / "plan" / "reports.md"
UNSOLVABLE_REPORTS_FILE = PROJECT_ROOT / "experiments" / "unsolvability" / "reports.md"
UNFINISHED_STATUSES = ("running", "missing")
RELAXED_DELETE_BUCKETS = ("None", "1 to 4", "5 to 9", "10 to 19", "20 or more")
VERDICTS = ("unsolvable", "unknown", "solvable")
# A killed run reports the phase it completed last, so it died in the next one.
KILLED_IN_PHASE = {
    "abstract_asp": "Searching for the abstract plan",
    "abstract_solving": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}


def main():
    args = _argument_parser().parse_args()
    problems = _finished_problems(args.results)
    if _is_verdict_run(problems):
        # A decide run reports no plan, horizon or refinement, so none of the
        # other tables have anything to say about one. It also gets its own
        # report file, or it would replace the one the plan runs write.
        sections = [_verdicts(problems), _verdict_head_to_head(problems), _timeout_phases(problems)]
        reports_file = UNSOLVABLE_REPORTS_FILE
    else:
        sections = [
            _coverage(problems),
            _head_to_head(problems),
            _timeout_phases(problems),
            _refinement_outcomes(problems),
            _relaxed_deletes(problems),
        ]
        reports_file = REPORTS_FILE
    _print_report(sections)
    _write_report(sections, args.results, reports_file)
    print(f"\nWrote this report to {_relative(reports_file)}")


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


def _is_verdict_run(problems):
    """Tell a run that decided solvability from one that searched for plans."""
    for modes in problems:
        for row in modes.values():
            if row.get("verdict"):
                return True
    return False


def _verdicts(problems):
    total = len(problems)
    lines = _wide_header("Verdict")
    for verdict in VERDICTS:
        counts = _verdict_counts(problems, verdict)
        abstract = _share(counts["abstract"], total, 1)
        concrete = _share(counts["concrete"], total, 1)
        lines.append(_wide(verdict.capitalize(), abstract, concrete))

    # Everything that finished without deciding: no symmetries, or an error.
    missing = _verdict_counts(problems, "")
    lines.append(_wide("No verdict", _share(missing["abstract"], total, 1), _share(missing["concrete"], total, 1)))
    lines.append(_wide("Total problems", total, total))
    return "Verdicts", lines


def _verdict_head_to_head(problems):
    proved = []
    for modes in problems:
        if modes["abstract"]["verdict"] == "unsolvable" and modes["concrete"]["verdict"] == "unsolvable":
            proved.append(modes)

    shared = len(proved)
    faster = {"abstract": 0, "concrete": 0}
    abstract_times = []
    concrete_times = []
    for modes in proved:
        abstract_times.append(_runtime(modes["abstract"]))
        concrete_times.append(_runtime(modes["concrete"]))
        winner = "abstract" if _runtime(modes["abstract"]) < _runtime(modes["concrete"]) else "concrete"
        faster[winner] += 1

    counts = _verdict_counts(problems, "unsolvable")
    lines = _wide_header("Metric")
    lines.append(_wide("Proved unsolvable", counts["abstract"], counts["concrete"]))
    lines.append(_wide("Proved unsolvable by both", shared, shared))
    faster_abstract = _share(faster["abstract"], shared, 1)
    faster_concrete = _share(faster["concrete"], shared, 1)
    lines.append(_wide("Faster when both proved it", faster_abstract, faster_concrete))
    lines.append(_wide("Median runtime when both proved it", _median(abstract_times), _median(concrete_times)))
    lines.append(_wide("Proved it when the other did not", counts["abstract"] - shared, counts["concrete"] - shared))
    return "Head to head", lines


def _verdict_counts(problems, verdict):
    counts = {"abstract": 0, "concrete": 0}
    for modes in problems:
        for mode in counts:
            if modes[mode]["verdict"] == verdict:
                counts[mode] += 1
    return counts


def _coverage(problems):
    total = len(problems)
    found = _status_counts(problems, "success")
    timeouts = _status_counts(problems, "timed out")

    # runsolver interrupts a task that reaches the memory limit, and the kernel
    # kills one that outruns it outright, so both statuses are out of memory.
    interrupted = _status_counts(problems, "interrupted")
    killed = _status_counts(problems, "killed (signal 9)")
    out_of_memory = {}
    for mode in interrupted:
        out_of_memory[mode] = interrupted[mode] + killed[mode]
    no_plan = _status_counts(problems, "no plan found")

    # Whatever the rows above leave out, errors among them, so the rows always
    # add up to the total even when a status nobody has named yet turns up.
    other = {}
    for mode in found:
        other[mode] = total - found[mode] - timeouts[mode] - out_of_memory[mode] - no_plan[mode]

    lines = _wide_header("Metric")
    lines.append(_wide("Plans found", _share(found["abstract"], total, 1), _share(found["concrete"], total, 1)))
    lines.append(_wide("Timeouts", _share(timeouts["abstract"], total, 1), _share(timeouts["concrete"], total, 1)))
    lines.append(
        _wide("Out of memory", _share(out_of_memory["abstract"], total, 1), _share(out_of_memory["concrete"], total, 1))
    )
    lines.append(_wide("No plan found", _share(no_plan["abstract"], total, 1), _share(no_plan["concrete"], total, 1)))
    lines.append(_wide("Others", _share(other["abstract"], total, 1), _share(other["concrete"], total, 1)))
    lines.append(_wide("Total problems", total, total))
    return "Coverage", lines


def _head_to_head(problems):
    solved_by_both = [modes for modes in problems if _solved_by_both(modes)]
    shared = len(solved_by_both)
    faster = {"abstract": 0, "concrete": 0}
    for modes in solved_by_both:
        winner = "abstract" if _runtime(modes["abstract"]) < _runtime(modes["concrete"]) else "concrete"
        faster[winner] += 1

    abstract_times = [_runtime(modes["abstract"]) for modes in solved_by_both]
    concrete_times = [_runtime(modes["concrete"]) for modes in solved_by_both]
    found = _status_counts(problems, "success")

    lines = _wide_header("Metric")
    lines.append(_wide("Plans found by both pipelines", shared, shared))
    faster_abstract = _share(faster["abstract"], shared, 1)
    faster_concrete = _share(faster["concrete"], shared, 1)
    lines.append(_wide("Faster when both found a plan", faster_abstract, faster_concrete))
    lines.append(_wide("Plan found when the other did not", found["abstract"] - shared, found["concrete"] - shared))
    lines.append(_wide("Median runtime when both found a plan", _median(abstract_times), _median(concrete_times)))
    total_runtimes = (_seconds(sum(abstract_times)), _seconds(sum(concrete_times)))
    lines.append(_wide("Total runtime across shared solves", *total_runtimes))
    return "Head to head", lines


def _timeout_phases(problems):
    timeouts = [modes["abstract"] for modes in problems if modes["abstract"]["status"] == "timed out"]
    counts = {}
    for row in timeouts:
        phase = KILLED_IN_PHASE.get(row["last_completed_phase"], row["last_completed_phase"])
        counts[phase] = counts.get(phase, 0) + 1

    lines = _narrow_header("Where the abstract pipeline was killed", "Timeouts")
    for phase, count in sorted(counts.items(), key=lambda item: -item[1]):
        lines.append(_narrow(phase, _share(count, len(timeouts), 0)))
    lines.append(_narrow("Total", len(timeouts)))
    return "Where the timeouts died", lines


def _refinement_outcomes(problems):
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
    lines = _narrow_header(f"How the {total} successes were solved", "Problems")
    lines.append(_narrow("Abstract plan refined directly", _share(counts["refined"], total, 0)))
    lines.append(_narrow("Refined after switching some actions off", _share(counts["switched"], total, 0)))
    lines.append(_narrow("Abstract plan discarded, solved above it", _share(counts["discarded"], total, 0)))
    lines.append(_narrow("Total", total))
    return "How the successes were solved", lines


def _relaxed_deletes(problems):
    successes = [modes["abstract"] for modes in problems if modes["abstract"]["status"] == "success"]
    rows = []
    for row in successes:
        if int(row["increments"]) == 0 and row.get("relaxed_deletes"):
            rows.append(row)
    if not rows:
        if successes and not any(row.get("relaxed_deletes") for row in successes):
            return "Deletes relaxed", ["This CSV predates the relaxed-deletes counter"]
        return "Deletes relaxed", ["No success was solved with its abstract plan"]

    counts = {bucket: 0 for bucket in RELAXED_DELETE_BUCKETS}
    for row in rows:
        counts[_relaxed_delete_bucket(int(row["relaxed_deletes"]))] += 1

    total = len(rows)
    lines = _narrow_header("Deletes relaxed", "Problems")
    for bucket in RELAXED_DELETE_BUCKETS:
        lines.append(_narrow(bucket, _share(counts[bucket], total, 0)))
    lines.append(_narrow("Total", total))
    return f"Deletes relaxed, over the {total} successes whose abstract plan was used", lines


def _relaxed_delete_bucket(relaxed_deletes):
    if relaxed_deletes == 0:
        return "None"
    if relaxed_deletes < 5:
        return "1 to 4"
    if relaxed_deletes < 10:
        return "5 to 9"
    if relaxed_deletes < 20:
        return "10 to 19"
    return "20 or more"


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


def _median(times):
    """Report the median, which a run with no shared solves does not have."""
    return _seconds(statistics.median(times)) if times else "n/a"


def _relative(path):
    """Name the file the way the repository does, when it lives inside it."""
    path = Path(path).resolve()
    if path.is_relative_to(PROJECT_ROOT):
        return path.relative_to(PROJECT_ROOT)
    return path


def _bold(text):
    """Bold the text on a terminal, leaving redirected output plain."""
    return f"\033[1m{text}\033[0m" if sys.stdout.isatty() else text


def _wide_header(label):
    return [_wide(label, "Abstract pipeline", "Concrete pipeline"), "-" * 80]


def _wide(label, abstract, concrete):
    return f"{label:<44}{abstract:>17}  {concrete:>17}"


def _narrow_header(label, value_label):
    return [_narrow(label, value_label), "-" * 61]


def _narrow(label, value):
    return f"{label:<45}{value:>16}"


def _print_report(sections):
    for title, lines in sections:
        print(f"\n{_bold(title)}\n")
        print("\n".join(lines))


def _write_report(sections, results_file, reports_file=REPORTS_FILE):
    """Replace the report file with the latest report."""
    report = ["# Benchmark report", "", f"{datetime.now().strftime('%Y-%m-%d %H:%M')} — {_relative(results_file)}", ""]
    for title, lines in sections:
        report += [f"## {title}", "", "```", *lines, "```", ""]
    Path(reports_file).write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
