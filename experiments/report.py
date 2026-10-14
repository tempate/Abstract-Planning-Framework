"""Summarize a collected benchmark CSV, as plan coverage or as solvability verdicts."""

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path

from experiments.run import ABSTRACTION_PREFIX, MODES, PROJECT_ROOT, class_rank
from experiments.tracks import DEFAULT_TRACK, TRACKS

DEFAULT_CSV = TRACKS[DEFAULT_TRACK].results_file
SOLVER_LABELS = {
    "asp": "ASP",
    "fd": "LAMA",
    "fd-lmcut": "LMcut",
}
# A verdict run decides solvability with merge-and-shrink, not with LAMA.
VERDICT_LABELS = SOLVER_LABELS | {"fd": "M&S"}
UNFINISHED_STATUSES = ("running", "missing")
RELAXED_DELETE_BUCKETS = ("None", "1 to 4", "5 to 9", "10 to 19", "20 or more")
VERDICTS = ("unsolvable", "unknown")
# A killed run reports the phase it completed last, so it died in the next one.
# In the order the abstraction pipelines run them, which the timeout table keeps.
KILLED_IN_PHASE = {
    "problem_reading": "Finding the object classes",
    "symmetry_discovery": "Abstraction",
    "resource_detection": "Abstraction",
    # Measured on both sides of the PNF translation, so either translation follows it.
    "abstraction": "Translating the task",
    "pnf_translation": "Abstraction",
    "concrete_fd": "Writing the abstract task",
    "abstract_pddl_writing": "Translating the abstract task",
    "abstract_fd": "Translating the task to ASP",
    "concrete_asp": "Abstract search",
    "abstract_asp": "Abstract search",
    "abstract_solving": "Guided concrete search",
    "abstract_fd_search": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}
# The solvability check searches the abstract task straight from its PDDL.
KILLED_IN_PHASE_DECIDING = KILLED_IN_PHASE | {"abstract_pddl_writing": "Abstract search"}


def main():
    args = _argument_parser().parse_args()
    modes, problems, dropped = _finished_problems(args.results)
    abstractions = [mode for mode in modes if mode.startswith(ABSTRACTION_PREFIX)]
    pairs = _pairs(abstractions, modes)

    # A decide run reports no plan, horizon or refinement, so none of the other
    # tables have anything to say about one.
    verdict_run = _is_verdict_run(problems)
    labels = _labels(abstractions, pairs, VERDICT_LABELS if verdict_run else SOLVER_LABELS)
    if verdict_run:
        sections = [_verdicts(problems, modes, labels)]
        if pairs:
            sections.append(_verdict_head_to_head(problems, pairs, labels))
    else:
        sections = [_coverage(problems, modes, labels)]
        if pairs:
            sections.append(_head_to_head(problems, pairs, labels))

    # Only a mode through an abstraction has one to report on.
    if abstractions:
        sections.append(_timeout_phases(problems, abstractions, verdict_run, labels))
        if not verdict_run:
            sections += [
                _refinement_outcomes(problems, abstractions, labels),
                _relaxed_deletes(problems, abstractions, labels),
            ]
            classes = _classes(args.results, abstractions, labels)
            if classes:
                sections.append(classes)
    sections.append(_by_domain(problems, modes, verdict_run, labels))

    summary = _summary(modes, problems, dropped)
    reports_file = Path(args.results).parent / "report.md"
    _print_report(sections)
    _write_report(sections, args.results, reports_file, summary)
    print(f"\n{summary}")
    print(f"Wrote this report to {_relative(reports_file)}")


def _pairs(abstractions, modes):
    """Pair each abstraction with the solver that plans its abstract task, or, when
    the run has no plain one, a configuration of it such as fd-lmcut."""
    pairs = []
    for abstraction in abstractions:
        solver = abstraction.removeprefix(ABSTRACTION_PREFIX)
        candidates = [mode for mode in modes if mode == solver or mode.startswith(f"{solver}-")]
        if candidates:
            pairs.append((abstraction, solver if solver in candidates else candidates[0]))
    return pairs


def _labels(abstractions, pairs, solver_labels=SOLVER_LABELS):
    """Name each abstraction after the solver it is compared with, marked with an alpha."""
    labels = dict(solver_labels)
    solvers = dict(pairs)
    for abstraction in abstractions:
        solver = solvers.get(abstraction, abstraction.removeprefix(ABSTRACTION_PREFIX))
        labels[abstraction] = f"{solver_labels[solver]}ᵅ"
    return labels


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
            # The planner collapses the largest class. The others get a section of their own.
            if class_rank(row["mode"], row.get("class")) in ("", "0"):
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


def _verdicts(problems, modes, labels):
    rows = [(verdict.capitalize(), _verdict_counts(problems, modes, verdict)) for verdict in VERDICTS]
    return "Verdicts", _outcome_table(problems, modes, "Verdict", rows, labels)


def _coverage(problems, modes, labels):
    rows = [("Plans found", _status_counts(problems, modes, "success"))]
    return "Coverage", _outcome_table(problems, modes, "Metric", rows, labels)


def _outcome_table(problems, modes, heading, rows, labels):
    """Count each mode's outcomes, ending with the ones the given rows, timeouts and memory leave out."""
    total = len(problems)
    rows = rows + [
        ("Timeouts", _status_counts(problems, modes, "timed out")),
        ("Out of memory", _out_of_memory(problems, modes)),
    ]
    # Whatever the rows leave out, errors among them, so they always add up to
    # the total even when a status nobody has named yet turns up.
    other = {mode: total - sum(counts[mode] for _label, counts in rows) for mode in modes}

    lines = _wide_header(heading, modes, labels)
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
    "faster": "Faster",
    "alone": "Found when the other did not",
    "median": "Median runtime",
    "total": "Total runtime",
    "shorter": "Shorter plan",
    "equal": "Same plan length",
    "median_length": "Median plan length",
    "total_length": "Total plan length",
}
VERDICT_COMPARISON = {
    "shared": "Proved unsolvable by both",
    "faster": "Faster",
    "alone": "Proved when the other did not",
    "median": "Median runtime",
    "total": "Total runtime",
}


def _head_to_head(problems, pairs, labels):
    return _compare(problems, pairs, lambda row: row["status"] == "success", PLAN_COMPARISON, labels)


def _verdict_head_to_head(problems, pairs, labels):
    return _compare(problems, pairs, lambda row: row["verdict"] == "unsolvable", VERDICT_COMPARISON, labels)


def _compare(problems, pairs, succeeded, metrics, labels):
    """Compare each abstraction with its solver, side by side, on what both succeeded at."""
    columns = {}
    for abstraction, solver in pairs:
        columns |= _compare_pair(problems, abstraction, solver, succeeded)

    lines = _wide_header("Metric", columns, labels)
    for key, label in metrics.items():
        lines.append(_wide(label, [columns[mode][key] for mode in columns]))
    return "Head to head, over the problems both solved", lines


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

    # A verdict run reports no plan, so only the problems with both lengths compare.
    measured = [problem for problem in both if all(_plan_length(problem[mode]) is not None for mode in pair)]
    shorter = {mode: 0 for mode in pair}
    for problem in measured:
        lengths = {mode: _plan_length(problem[mode]) for mode in pair}
        if lengths[abstraction] != lengths[solver]:
            shorter[min(pair, key=lengths.get)] += 1
    equal = len(measured) - sum(shorter.values())

    columns = {}
    for mode in sorted(pair, key=MODES.index):
        times = [_runtime(problem[mode]) for problem in both]
        lengths = [_plan_length(problem[mode]) for problem in measured]
        columns[mode] = {
            "shared": shared,
            "faster": _share(faster[mode], shared, 1),
            "alone": sum(succeeded(problem[mode]) for problem in problems) - shared,
            "median": _median(times),
            "total": _seconds(sum(times)),
            "shorter": _share(shorter[mode], len(measured), 1),
            "equal": _share(equal, len(measured), 1),
            "median_length": f"{statistics.median(lengths):g}" if lengths else "n/a",
            "total_length": f"{sum(lengths):,}",
        }
    return columns


def _plan_length(row):
    length = row.get("plan_length", "").strip()
    return int(float(length)) if length else None


def _discarded_the_abstract_plan(row):
    if not row["decrements"].strip():
        return False
    return int(row["decrements"]) == int(row["abstract_plan_length"])


def _timeout_phases(problems, abstractions, verdict_run, labels):
    killed_in = KILLED_IN_PHASE_DECIDING if verdict_run else KILLED_IN_PHASE
    pipeline = list(KILLED_IN_PHASE)
    counts = {mode: {} for mode in abstractions}
    totals = {}
    positions = {}
    for mode in abstractions:
        timeouts = [modes[mode] for modes in problems if modes[mode]["status"] == "timed out"]
        totals[mode] = len(timeouts)
        for row in timeouts:
            completed = row["last_completed_phase"]
            phase = killed_in.get(completed, completed)
            # The extended search is no longer a phase of its own. A guided search that
            # has switched off every abstract action is what used to enter it.
            unguided = phase == "Guided concrete search" and _discarded_the_abstract_plan(row)
            if unguided:
                phase = "Unguided concrete search"
            counts[mode][phase] = counts[mode].get(phase, 0) + 1

            # A phase nobody has placed yet goes last rather than failing the report.
            index = pipeline.index(completed) if completed in pipeline else len(pipeline)
            positions[phase] = min(positions.get(phase, (index, unguided)), (index, unguided))

    lines = _wide_header("Killed during", abstractions, labels)
    for phase in sorted(positions, key=positions.get):
        lines.append(_wide(phase, [_share(counts[mode].get(phase, 0), totals[mode], 0) for mode in abstractions]))
    lines.append(_wide("Total", [totals[mode] for mode in abstractions]))
    return "Where the timeouts died", lines


def _classes(results_file, abstractions, labels):
    """Compare the largest class with the best of all, over the problems with several finished classes."""
    ranks = {}
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row["mode"] in abstractions:
                problem = ranks.setdefault((row["domain"], row["problem"], row["mode"]), {})
                problem[class_rank(row["mode"], row.get("class"))] = row

    compared = {mode: [] for mode in abstractions}
    for (_domain, _problem, mode), rows in ranks.items():
        if len(rows) > 1 and "0" in rows and all(row["status"] not in UNFINISHED_STATUSES for row in rows.values()):
            compared[mode].append(rows)
    if not any(compared.values()):
        return None

    values = {key: [] for key in ("problems", "largest", "any", "fastest", "ratio")}
    for mode in abstractions:
        largest_solved = any_solved = largest_fastest = 0
        ratios = []
        for rows in compared[mode]:
            solved = {rank: _runtime(row) for rank, row in rows.items() if row["status"] == "success"}
            largest_solved += "0" in solved
            any_solved += bool(solved)
            if solved:
                best = min(solved.values())
                largest_fastest += solved.get("0") == best
                if "0" in solved:
                    ratios.append(solved["0"] / best)
        values["problems"].append(len(compared[mode]))
        values["largest"].append(largest_solved)
        values["any"].append(any_solved)
        values["fastest"].append(_share(largest_fastest, any_solved, 0))
        values["ratio"].append(f"{statistics.median(ratios):.2f}x" if ratios else "n/a")

    lines = _wide_header("Over problems with 2+ classes", abstractions, labels)
    lines.append(_wide("Problems", values["problems"]))
    lines.append(_wide("Solved by the largest class", values["largest"]))
    lines.append(_wide("Solved by some class", values["any"]))
    lines.append(_wide("Largest class is fastest", values["fastest"]))
    lines.append(_wide("Median time, largest / best", values["ratio"]))
    return "Every class against the largest", lines


def _refinement_outcomes(problems, abstractions, labels):
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
        ("refined", "Refined directly"),
        ("switched", "Refined, some actions off"),
        ("discarded", "Solved above the abstract plan"),
    )
    lines = _wide_header("Solved by", abstractions, labels)
    for key, label in outcomes:
        lines.append(_wide(label, [_share(counts[mode][key], totals[mode], 0) for mode in abstractions]))
    lines.append(_wide("Total", [totals[mode] for mode in abstractions]))
    return "How the successes were solved", lines


def _relaxed_deletes(problems, abstractions, labels):
    title = "Deletes relaxed by the refined plans"
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

    lines = _wide_header("Deletes relaxed", abstractions, labels)
    for bucket in RELAXED_DELETE_BUCKETS:
        lines.append(_wide(bucket, [_share(counts[mode][bucket], len(used[mode]), 0) for mode in abstractions]))
    lines.append(_wide("Total", [len(used[mode]) for mode in abstractions]))
    return title, lines


def _by_domain(problems, modes, verdict_run, labels):
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

    header = _compact("Domain", ["Problems", *(labels[mode] for mode in modes)])
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


def _wide_header(label, modes, labels):
    header = _wide(label, [labels[mode] for mode in modes])
    return [header, "-" * len(header)]


def _wide(label, values):
    return f"{label:<30}" + "".join(f"{value:>13}" for value in values)


def _compact(label, values):
    return f"{label:<28}" + "".join(f"{value:>10}" for value in values)


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
