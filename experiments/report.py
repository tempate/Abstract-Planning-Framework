"""Summarize a collected benchmark CSV, as plan coverage or as solvability verdicts."""

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path

from experiments.run import ABSTRACTION_PREFIX, MODES, PROJECT_ROOT
from experiments.tracks import DEFAULT_TRACK, TRACKS

DEFAULT_CSV = TRACKS[DEFAULT_TRACK].results_file
MODE_LABELS = {
    "abs-asp": "Abs + ASP",
    "abs-fd": "Abs + FD",
    "asp": "ASP",
    "fd": "FD",
}
UNFINISHED_STATUSES = ("running", "missing")
RELAXED_DELETE_BUCKETS = ("None", "1 to 4", "5 to 9", "10 to 19", "20 or more")
VERDICTS = ("unsolvable", "unknown")
# A killed run reports the phase it completed last, so it died in the next one.
KILLED_IN_PHASE = {
    "concrete_asp": "Searching for the abstract plan",
    "abstract_asp": "Searching for the abstract plan",
    "abstract_solving": "Guided concrete search",
    "abstract_fd_search": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}


def main():
    args = _argument_parser().parse_args()
    modes, problems, dropped = _finished_problems(args.results)
    abstractions = [mode for mode in modes if mode.startswith(ABSTRACTION_PREFIX)]
    # Each abstraction is compared with the solver that plans its abstract task.
    pairs = []
    for mode in abstractions:
        solver = mode.removeprefix(ABSTRACTION_PREFIX)
        if solver in modes:
            pairs.append((mode, solver))

    # A decide run reports no plan, horizon or refinement, so none of the other
    # tables have anything to say about one.
    verdict_run = _is_verdict_run(problems)
    if verdict_run:
        sections = [_verdicts(problems, modes)]
        if pairs:
            sections.append(_verdict_head_to_head(problems, pairs))
    else:
        sections = [_coverage(problems, modes)]
        if pairs:
            sections.append(_head_to_head(problems, pairs))

    # Only a mode through an abstraction has one to report on.
    if abstractions:
        sections.append(_timeout_phases(problems, abstractions))
        if not verdict_run:
            sections += [_refinement_outcomes(problems, abstractions), _relaxed_deletes(problems, abstractions)]
    sections.append(_by_domain(problems, modes, verdict_run))

    summary = _summary(modes, problems, dropped)
    reports_file = Path(args.results).parent / "report.md"
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
    rows = [(verdict.capitalize(), _verdict_counts(problems, modes, verdict)) for verdict in VERDICTS]
    return "Verdicts", _outcome_table(problems, modes, "Verdict", rows)


def _coverage(problems, modes):
    rows = [("Plans found", _status_counts(problems, modes, "success"))]
    return "Coverage", _outcome_table(problems, modes, "Metric", rows)


def _outcome_table(problems, modes, heading, rows):
    """Count each mode's outcomes, ending with the ones the given rows, timeouts and memory leave out."""
    total = len(problems)
    rows = rows + [
        ("Timeouts", _status_counts(problems, modes, "timed out")),
        ("Out of memory", _out_of_memory(problems, modes)),
    ]
    # Whatever the rows leave out, errors among them, so they always add up to
    # the total even when a status nobody has named yet turns up.
    other = {mode: total - sum(counts[mode] for _label, counts in rows) for mode in modes}

    lines = _wide_header(heading, modes)
    for label, counts in (*rows, ("Others", other)):
        lines.append(_wide(label, [_share(counts[mode], total, 1) for mode in modes]))
    lines.append(_wide("Total problems", [total for _ in modes]))
    return lines


def _verdict_counts(problems, modes, verdict):
    counts = {mode: 0 for mode in modes}
    for modes in problems:
        for mode in counts:
            if modes[mode]["verdict"] == verdict:
                counts[mode] += 1
    return counts


PLAN_COMPARISON = {
    "shared": "Plans found by both",
    "faster": "Faster when both found a plan",
    "alone": "Plan found when the other did not",
    "median": "Median runtime when both found a plan",
    "total": "Total runtime across shared solves",
}
VERDICT_COMPARISON = {
    "shared": "Proved unsolvable by both",
    "faster": "Faster when both proved it",
    "alone": "Proved it when the other did not",
    "median": "Median runtime when both proved it",
    "total": "Total runtime across shared proofs",
}


def _head_to_head(problems, pairs):
    return _compare(problems, pairs, lambda row: row["status"] == "success", PLAN_COMPARISON)


def _verdict_head_to_head(problems, pairs):
    return _compare(problems, pairs, lambda row: row["verdict"] == "unsolvable", VERDICT_COMPARISON)


def _compare(problems, pairs, succeeded, labels):
    """Compare each abstraction with its solver, side by side, on what both succeeded at."""
    columns = {}
    for abstraction, solver in pairs:
        columns |= _compare_pair(problems, abstraction, solver, succeeded)

    lines = _wide_header("Metric", columns)
    for key, label in labels.items():
        lines.append(_wide(label, [columns[mode][key] for mode in columns]))
    return "Head to head", lines


def _compare_pair(problems, abstraction, solver, succeeded):
    """Pairwise rather than over every mode at once: intersecting all of them would
    drop the problems one solver missed out of the other pair's comparison, moving
    numbers for a reason that has nothing to do with either of them."""
    pair = (abstraction, solver)
    both = [problem for problem in problems if all(succeeded(problem[mode]) for mode in pair)]
    shared = len(both)

    faster = {mode: 0 for mode in pair}
    for problem in both:
        winner = abstraction if _runtime(problem[abstraction]) < _runtime(problem[solver]) else solver
        faster[winner] += 1

    columns = {}
    for mode in sorted(pair, key=MODES.index):
        times = [_runtime(problem[mode]) for problem in both]
        columns[mode] = {
            "shared": shared,
            "faster": _share(faster[mode], shared, 1),
            "alone": sum(succeeded(problem[mode]) for problem in problems) - shared,
            "median": _median(times),
            "total": _seconds(sum(times)),
        }
    return columns


def _discarded_the_abstract_plan(row):
    if not row["decrements"].strip():
        return False
    return int(row["decrements"]) == int(row["abstract_plan_length"])


def _timeout_phases(problems, abstractions):
    counts = {mode: {} for mode in abstractions}
    totals = {}
    for mode in abstractions:
        timeouts = [modes[mode] for modes in problems if modes[mode]["status"] == "timed out"]
        totals[mode] = len(timeouts)
        for row in timeouts:
            phase = KILLED_IN_PHASE.get(row["last_completed_phase"], row["last_completed_phase"])
            # The extended search is no longer a phase of its own. A guided search that
            # has switched off every abstract action is what used to enter it.
            if phase == "Guided concrete search" and _discarded_the_abstract_plan(row):
                phase = "Unguided concrete search"
            counts[mode][phase] = counts[mode].get(phase, 0) + 1

    phases = {phase for mode in abstractions for phase in counts[mode]}
    lines = _wide_header("Killed during", abstractions)
    for phase in sorted(phases, key=lambda phase: -sum(counts[mode].get(phase, 0) for mode in abstractions)):
        lines.append(_wide(phase, [_share(counts[mode].get(phase, 0), totals[mode], 0) for mode in abstractions]))
    lines.append(_wide("Total", [totals[mode] for mode in abstractions]))
    return "Where the timeouts died", lines


def _refinement_outcomes(problems, abstractions):
    counts = {mode: {"refined": 0, "switched": 0, "discarded": 0} for mode in abstractions}
    totals = {}
    for mode in abstractions:
        successes = [modes[mode] for modes in problems if modes[mode]["status"] == "success"]
        totals[mode] = len(successes)
        for row in successes:
            if int(row["increments"]) > 0:
                counts[mode]["discarded"] += 1
            elif int(row["decrements"]) > 0:
                counts[mode]["switched"] += 1
            else:
                counts[mode]["refined"] += 1

    outcomes = (
        ("refined", "Abstract plan refined directly"),
        ("switched", "Refined after switching some actions off"),
        ("discarded", "Abstract plan discarded, solved above it"),
    )
    lines = _wide_header("Solved by", abstractions)
    for key, label in outcomes:
        lines.append(_wide(label, [_share(counts[mode][key], totals[mode], 0) for mode in abstractions]))
    lines.append(_wide("Total", [totals[mode] for mode in abstractions]))
    return "How the successes were solved", lines


def _relaxed_deletes(problems, abstractions):
    title = "Deletes relaxed, over the successes whose abstract plan was used"
    used = {}
    for mode in abstractions:
        successes = [modes[mode] for modes in problems if modes[mode]["status"] == "success"]
        used[mode] = [row for row in successes if int(row["increments"]) == 0 and row.get("relaxed_deletes")]

    if not any(used.values()):
        successes = [modes[mode] for modes in problems for mode in abstractions if modes[mode]["status"] == "success"]
        if successes and not any(row.get("relaxed_deletes") for row in successes):
            return title, ["This CSV predates the relaxed-deletes counter"]
        return title, ["No success was solved with its abstract plan"]

    counts = {mode: {bucket: 0 for bucket in RELAXED_DELETE_BUCKETS} for mode in abstractions}
    for mode in abstractions:
        for row in used[mode]:
            counts[mode][_relaxed_delete_bucket(int(row["relaxed_deletes"]))] += 1

    lines = _wide_header("Deletes relaxed", abstractions)
    for bucket in RELAXED_DELETE_BUCKETS:
        lines.append(_wide(bucket, [_share(counts[mode][bucket], len(used[mode]), 0) for mode in abstractions]))
    lines.append(_wide("Total", [len(used[mode]) for mode in abstractions]))
    return title, lines


def _by_domain(problems, modes, verdict_run):
    if verdict_run:
        title, succeeded = "Proved unsolvable by domain", lambda row: row["verdict"] == "unsolvable"
    else:
        title, succeeded = "Plans found by domain", lambda row: row["status"] == "success"

    domains = {}
    for problem in problems:
        domain = next(iter(problem.values()))["domain"]
        counts = domains.setdefault(domain, {"problems": 0} | {mode: 0 for mode in modes})
        counts["problems"] += 1
        for mode in modes:
            counts[mode] += succeeded(problem[mode])

    header = _compact("Domain", ["Problems", *(MODE_LABELS[mode] for mode in modes)])
    lines = [header, "-" * len(header)]
    for domain in sorted(domains):
        counts = domains[domain]
        lines.append(_compact(domain, [counts["problems"], *(counts[mode] for mode in modes)]))
    totals = [sum(counts[key] for counts in domains.values()) for key in ("problems", *modes)]
    lines.append(_compact("Total", totals))
    return title, lines


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


def _compact(label, values):
    return f"{label:<30}" + "".join(f"{value:>11}" for value in values)


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
