"""Summarize a collected benchmark CSV, as plan coverage or as solvability verdicts."""

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path

from experiments.run import MODES, PROJECT_ROOT
from experiments.tracks import DEFAULT_TRACK, TRACKS

DEFAULT_CSV = TRACKS[DEFAULT_TRACK].results_file
MODE_LABELS = {"abstract": "Abstract pipeline", "concrete": "Concrete pipeline", "lama": "LAMA-first"}
UNFINISHED_STATUSES = ("running", "missing")
RELAXED_DELETE_BUCKETS = ("None", "1 to 4", "5 to 9", "10 to 19", "20 or more")
VERDICTS = ("unsolvable", "unknown")
# A killed run reports the phase it completed last, so it died in the next one.
KILLED_IN_PHASE = {
    "abstract_asp": "Searching for the abstract plan",
    "abstract_solving": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}


def main():
    args = _argument_parser().parse_args()
    modes, problems, dropped = _finished_problems(args.results)
    baselines = [mode for mode in modes if mode != "abstract"]

    # A decide run reports no plan, horizon or refinement, so none of the other
    # tables have anything to say about one.
    verdict_run = _is_verdict_run(problems)
    if verdict_run:
        sections = [_verdicts(problems, modes)]
        sections += [_verdict_head_to_head(problems, baseline) for baseline in baselines]
    else:
        sections = [_coverage(problems, modes)]
        sections += [_head_to_head(problems, baseline) for baseline in baselines]

    # Only the abstract pipeline has an abstraction to report on.
    if "abstract" in modes:
        sections.append(_timeout_phases(problems))
        if not verdict_run:
            sections += [_refinement_outcomes(problems), _relaxed_deletes(problems)]

    summary = _summary(modes, problems, dropped)
    reports_file = Path(args.results).parent / "reports.md"
    _print_report(sections)
    _write_report(sections, args.results, reports_file, summary)
    print(f"\n{summary}")
    print(f"Wrote this report to {_relative(reports_file)}")


def _summary(modes, problems, dropped):
    """Say what the report covers, so a short one is a fact rather than a mystery.

    A problem counts only where every mode finished it, so one mode missing
    from a run quietly shrinks every table below.
    """
    summary = f"{len(problems)} problems compared over {', '.join(modes)}"
    return f"{summary}; {dropped} dropped as unfinished" if dropped else summary


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", nargs="?", type=Path, default=DEFAULT_CSV, help="Collected benchmark CSV")
    return parser


def _finished_problems(results_file):
    """Pair every mode the run holds, dropping problems any of them left unfinished.

    The modes come from the file rather than from a list here, so that a CSV
    with two of them reports on two.  They are read through MODES so that a
    value nobody recognizes is ignored instead of becoming a requirement no
    problem meets, which would empty the report rather than fail.
    """
    rows = {}
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            rows.setdefault((row["domain"], row["problem"]), {})[row["mode"]] = row

    present = {mode for problem in rows.values() for mode in problem}
    modes = tuple(mode for mode in MODES if mode in present)

    problems = []
    for problem in rows.values():
        if any(mode not in problem or problem[mode]["status"] in UNFINISHED_STATUSES for mode in modes):
            continue
        problems.append(problem)
    return modes, problems, len(rows) - len(problems)


def _is_verdict_run(problems):
    """Tell a run that decided solvability from one that searched for plans."""
    for modes in problems:
        for row in modes.values():
            if row.get("verdict"):
                return True
    return False


def _verdicts(problems, modes):
    total = len(problems)
    decided = {mode: 0 for mode in modes}
    lines = _wide_header("Verdict", modes)
    for verdict in VERDICTS:
        counts = _verdict_counts(problems, modes, verdict)
        for mode in decided:
            decided[mode] += counts[mode]
        lines.append(_wide(verdict.capitalize(), [_share(counts[mode], total, 1) for mode in modes]))

    timeouts = _status_counts(problems, modes, "timed out")
    out_of_memory = _out_of_memory(problems, modes)

    # Whatever the rows above leave out: no symmetries, or an error.
    other = {mode: total - decided[mode] - timeouts[mode] - out_of_memory[mode] for mode in modes}

    for label, counts in (("Timeouts", timeouts), ("Out of memory", out_of_memory), ("Others", other)):
        lines.append(_wide(label, [_share(counts[mode], total, 1) for mode in modes]))
    lines.append(_wide("Total problems", [total for _ in modes]))
    return "Verdicts", lines


def _verdict_head_to_head(problems, baseline):
    pair = ("abstract", baseline)
    proved = [problem for problem in problems if all(problem[mode]["verdict"] == "unsolvable" for mode in pair)]
    shared = len(proved)

    faster = {mode: 0 for mode in pair}
    for problem in proved:
        winner = "abstract" if _runtime(problem["abstract"]) < _runtime(problem[baseline]) else baseline
        faster[winner] += 1

    times = {mode: [_runtime(problem[mode]) for problem in proved] for mode in pair}
    counts = _verdict_counts(problems, pair, "unsolvable")

    lines = _wide_header("Metric", pair)
    lines.append(_wide("Proved unsolvable by both", [shared for _ in pair]))
    lines.append(_wide("Faster when both proved it", [_share(faster[mode], shared, 1) for mode in pair]))
    lines.append(_wide("Proved it when the other did not", [counts[mode] - shared for mode in pair]))
    lines.append(_wide("Median runtime when both proved it", [_median(times[mode]) for mode in pair]))
    lines.append(_wide("Total runtime across shared proofs", [_seconds(sum(times[mode])) for mode in pair]))
    return f"Head to head: abstract vs {MODE_LABELS[baseline]}", lines


def _verdict_counts(problems, modes, verdict):
    counts = {mode: 0 for mode in modes}
    for modes in problems:
        for mode in counts:
            if modes[mode]["verdict"] == verdict:
                counts[mode] += 1
    return counts


def _coverage(problems, modes):
    total = len(problems)
    found = _status_counts(problems, modes, "success")
    timeouts = _status_counts(problems, modes, "timed out")
    out_of_memory = _out_of_memory(problems, modes)

    # Whatever the rows above leave out, errors among them, so the rows always
    # add up to the total even when a status nobody has named yet turns up.
    other = {mode: total - found[mode] - timeouts[mode] - out_of_memory[mode] for mode in modes}

    lines = _wide_header("Metric", modes)
    for label, counts in (
        ("Plans found", found),
        ("Timeouts", timeouts),
        ("Out of memory", out_of_memory),
        ("Others", other),
    ):
        lines.append(_wide(label, [_share(counts[mode], total, 1) for mode in modes]))
    lines.append(_wide("Total problems", [total for _ in modes]))
    return "Coverage", lines


def _head_to_head(problems, baseline):
    """Compare the abstract pipeline with one baseline.

    Pairwise rather than over every mode at once: intersecting three ways would
    drop the problems one baseline missed out of the others' comparison, moving
    numbers for a reason that has nothing to do with either of them.
    """
    pair = ("abstract", baseline)
    both = [problem for problem in problems if _solved_by_both(problem, pair)]
    shared = len(both)

    faster = {mode: 0 for mode in pair}
    for problem in both:
        winner = "abstract" if _runtime(problem["abstract"]) < _runtime(problem[baseline]) else baseline
        faster[winner] += 1

    times = {mode: [_runtime(problem[mode]) for problem in both] for mode in pair}
    found = _status_counts(problems, pair, "success")

    lines = _wide_header("Metric", pair)
    lines.append(_wide("Plans found by both", [shared for _ in pair]))
    lines.append(_wide("Faster when both found a plan", [_share(faster[mode], shared, 1) for mode in pair]))
    lines.append(_wide("Plan found when the other did not", [found[mode] - shared for mode in pair]))
    lines.append(_wide("Median runtime when both found a plan", [_median(times[mode]) for mode in pair]))
    lines.append(_wide("Total runtime across shared solves", [_seconds(sum(times[mode])) for mode in pair]))
    return f"Head to head: abstract vs {MODE_LABELS[baseline]}", lines


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


def _solved_by_both(problem, pair):
    return all(problem[mode]["status"] == "success" for mode in pair)


def _runtime(row):
    return float(row["wall_time_seconds"])


def _out_of_memory(problems, modes):
    """runsolver interrupts a task that reaches the memory limit, the kernel kills
    one that outruns it outright, and Fast Downward reports its own search being
    killed, so all three statuses are out of memory."""
    interrupted = _status_counts(problems, modes, "interrupted")
    killed = _status_counts(problems, modes, "killed (signal 9)")
    reported = _status_counts(problems, modes, "out of memory")
    counts = {}
    for mode in interrupted:
        counts[mode] = interrupted[mode] + killed[mode] + reported[mode]
    return counts


def _status_counts(problems, modes, status):
    counts = {mode: 0 for mode in modes}
    for problem in problems:
        for mode in counts:
            if problem[mode]["status"] == status:
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


def _wide_header(label, modes):
    header = _wide(label, [MODE_LABELS[mode] for mode in modes])
    return [header, "-" * len(header)]


def _wide(label, values):
    return f"{label:<44}" + "  ".join(f"{value:>17}" for value in values)


def _narrow_header(label, value_label):
    return [_narrow(label, value_label), "-" * 61]


def _narrow(label, value):
    return f"{label:<45}{value:>16}"


def _print_report(sections):
    for title, lines in sections:
        print(f"\n{_bold(title)}\n")
        print("\n".join(lines))


def _write_report(sections, results_file, reports_file, summary):
    """Replace the report file with the latest report."""
    stamp = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} — {_relative(results_file)}"
    report = ["# Benchmark report", "", stamp, "", summary, ""]
    for title, lines in sections:
        report += [f"## {title}", "", "```", *lines, "```", ""]
    Path(reports_file).write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
