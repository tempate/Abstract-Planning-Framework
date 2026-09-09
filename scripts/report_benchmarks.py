"""Summarize a collected benchmark CSV, one row per pipeline configuration."""

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path

from scripts.run_benchmark import PROJECT_ROOT

DEFAULT_CSV = PROJECT_ROOT / "benchmarks" / "results.csv"
REPORTS_FILE = PROJECT_ROOT / "benchmarks" / "reports.md"
CONCRETE = "concrete"
BASELINE = "baseline"
UNFINISHED_STATUSES = ("running", "missing")
RELAXED_DELETE_BUCKETS = ("None", "1 to 4", "5 to 9", "10 to 19", "20 or more")
# A killed run reports the phase it completed last, so it died in the next one.
KILLED_IN_PHASE = {
    "abstract_asp": "Abstract search",
    "abstract_solving": "Guided concrete search",
    "guided_concrete_solving": "Extended concrete search",
}
TIMEOUT_PHASES = ("Abstract search", "Guided concrete search", "Extended concrete search")


def main():
    args = _argument_parser().parse_args()
    problems, dropped = _finished_problems(args.results)
    if not problems:
        sys.exit("No problem was finished by every configuration")

    configs = _configs(problems)
    sections = [
        _coverage(problems, configs),
        _against_concrete(problems, configs),
        _abstraction_sizes(problems, configs),
        _timeout_phases(problems, configs),
        _refinement_outcomes(problems, configs),
        _relaxed_deletes(problems, configs),
    ]
    preamble = f"{len(problems)} problems every configuration finished, {dropped} dropped as unfinished"
    _print_report(sections, preamble)
    _write_report(sections, preamble, args.results)
    print(f"\nWrote this report to {_relative(REPORTS_FILE)}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", nargs="?", type=Path, default=DEFAULT_CSV, help="Collected benchmark CSV")
    return parser


def _finished_problems(results_file):
    """Group each problem's runs by configuration, dropping problems any of them left unfinished."""
    runs = {}
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            config = CONCRETE if row["mode"] == CONCRETE else _variant(row)
            runs.setdefault((row["domain"], row["problem"]), {})[config] = row

    configs = set()
    for problem in runs.values():
        configs.update(problem)

    problems, dropped = [], 0
    for problem in runs.values():
        unfinished = any(row["status"] in UNFINISHED_STATUSES for row in problem.values())
        if unfinished or problem.keys() != configs:
            dropped += 1
        else:
            problems.append(problem)
    return problems, dropped


def _configs(problems):
    """Every configuration in the CSV: the concrete pipeline first, then the variants."""
    configs = set()
    for problem in problems:
        configs.update(problem)
    return sorted(configs, key=lambda config: (config != CONCRETE, config != BASELINE, config))


def _variant(row):
    return row.get("symmetry_variant") or BASELINE


def _coverage(problems, configs):
    total = len(problems)
    rows = []
    for config in configs:
        counts = _status_counts(problems, config)
        rows.append(
            [
                config,
                _share(counts["success"], total, 1),
                counts["timed out"],
                counts["no plan found"],
                _versus_baseline(problems, configs, config),
            ]
        )
    headers = ["Configuration", "Plans found", "Timeouts", "No plan found", "vs baseline"]
    return "Coverage", _table(headers, rows)


def _versus_baseline(problems, configs, config):
    if config == BASELINE or BASELINE not in configs:
        return "—"
    gained = sum(1 for problem in problems if _solved(problem[config]) and not _solved(problem[BASELINE]))
    lost = sum(1 for problem in problems if not _solved(problem[config]) and _solved(problem[BASELINE]))
    return f"+{gained} / -{lost}"


def _against_concrete(problems, configs):
    if CONCRETE not in configs:
        return "Against the concrete pipeline", ["This CSV holds no concrete run"]

    rows = []
    for config in _variants(configs):
        shared = [problem for problem in problems if _solved(problem[config]) and _solved(problem[CONCRETE])]
        abstract_times = [_runtime(problem[config]) for problem in shared]
        concrete_times = [_runtime(problem[CONCRETE]) for problem in shared]
        faster = sum(1 for problem in shared if _runtime(problem[config]) < _runtime(problem[CONCRETE]))
        only_abstract = sum(1 for problem in problems if _solved(problem[config]) and not _solved(problem[CONCRETE]))
        only_concrete = sum(1 for problem in problems if not _solved(problem[config]) and _solved(problem[CONCRETE]))
        rows.append(
            [
                config,
                len(shared),
                _share(faster, len(shared), 0),
                only_abstract,
                only_concrete,
                _pair(statistics.median(abstract_times), statistics.median(concrete_times)) if shared else "—",
                _pair(sum(abstract_times), sum(concrete_times)) if shared else "—",
            ]
        )
    headers = ["Variant", "Solved by both", "Faster", "Only the variant", "Only concrete", "Median", "Total"]
    return "Against the concrete pipeline, runtimes as variant / concrete", _table(headers, rows)


def _abstraction_sizes(problems, configs):
    rows = []
    for config in _variants(configs):
        sizes = [_objects(problem[config]) for problem in problems if _objects(problem[config])]
        rows.append(
            [
                config,
                f"{statistics.median(sizes):.0f}",
                f"{statistics.mean(sizes):.1f}",
                max(sizes),
                _larger_than_baseline(problems, configs, config),
            ]
        )
    headers = ["Variant", "Median objects", "Mean", "Largest", "Class grew vs baseline"]
    return "How many objects each variant collapsed", _table(headers, rows)


def _larger_than_baseline(problems, configs, config):
    if config == BASELINE or BASELINE not in configs:
        return "—"
    comparable = [problem for problem in problems if _objects(problem[config]) and _objects(problem[BASELINE])]
    grew = sum(1 for problem in comparable if _objects(problem[config]) > _objects(problem[BASELINE]))
    return _share(grew, len(comparable), 0)


def _timeout_phases(problems, configs):
    rows = []
    for config in _variants(configs):
        timeouts = [problem[config] for problem in problems if problem[config]["status"] == "timed out"]
        counts = {phase: 0 for phase in TIMEOUT_PHASES}
        for row in timeouts:
            phase = KILLED_IN_PHASE.get(row["last_completed_phase"], row["last_completed_phase"])
            counts[phase] = counts.get(phase, 0) + 1
        shares = [_share(counts[phase], len(timeouts), 0) for phase in TIMEOUT_PHASES]
        rows.append([config, *shares, len(timeouts)])
    return "Where the timeouts died", _table(["Variant", *TIMEOUT_PHASES, "Timeouts"], rows)


def _refinement_outcomes(problems, configs):
    rows = []
    for config in _variants(configs):
        successes = [problem[config] for problem in problems if _solved(problem[config])]
        discarded = sum(1 for row in successes if int(row["increments"]) > 0)
        switched = sum(1 for row in successes if int(row["increments"]) == 0 and int(row["decrements"]) > 0)
        refined = len(successes) - discarded - switched
        shares = [_share(count, len(successes), 0) for count in (refined, switched, discarded)]
        rows.append([config, *shares, len(successes)])
    headers = ["Variant", "Refined directly", "Switched actions off", "Discarded, solved above", "Successes"]
    return "How the successes were solved", _table(headers, rows)


def _relaxed_deletes(problems, configs):
    rows = []
    for config in _variants(configs):
        relaxed = []
        for problem in problems:
            row = problem[config]
            if _solved(row) and int(row["increments"]) == 0 and row.get("relaxed_deletes"):
                relaxed.append(int(row["relaxed_deletes"]))
        if not relaxed:
            continue

        counts = {bucket: 0 for bucket in RELAXED_DELETE_BUCKETS}
        for value in relaxed:
            counts[_relaxed_delete_bucket(value)] += 1
        shares = [_share(counts[bucket], len(relaxed), 0) for bucket in RELAXED_DELETE_BUCKETS]
        rows.append([config, *shares, f"{statistics.median(relaxed):.0f}", max(relaxed), len(relaxed)])
    if not rows:
        return "Deletes relaxed", ["This CSV predates the relaxed-deletes counter"]

    headers = ["Variant", *RELAXED_DELETE_BUCKETS, "Median", "Most", "Problems"]
    return "Deletes relaxed, over the successes whose abstract plan was used", _table(headers, rows)


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


def _variants(configs):
    return [config for config in configs if config != CONCRETE]


def _solved(row):
    return row["status"] == "success"


def _runtime(row):
    return float(row["wall_time_seconds"])


def _objects(row):
    return int(row["abstracted_object_count"]) if row["abstracted_object_count"] else 0


def _status_counts(problems, config):
    counts = {"success": 0, "timed out": 0, "no plan found": 0}
    for problem in problems:
        status = problem[config]["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def _share(count, total, decimals):
    return f"{count} ({count / total:.{decimals}%})" if total else f"{count}"


def _pair(abstract, concrete):
    return f"{abstract:,.1f} / {concrete:,.1f} s"


def _relative(path):
    """Name the file the way the repository does, when it lives inside it."""
    path = Path(path).resolve()
    if path.is_relative_to(PROJECT_ROOT):
        return path.relative_to(PROJECT_ROOT)
    return path


def _bold(text):
    """Bold the text on a terminal, leaving redirected output plain."""
    return f"\033[1m{text}\033[0m" if sys.stdout.isatty() else text


def _table(headers, rows):
    columns = [[str(cell) for cell in column] for column in zip(headers, *rows)]
    widths = [max(len(cell) for cell in column) for column in columns]
    lines = [_line(headers, widths), "-" * (sum(widths) + 2 * (len(widths) - 1))]
    for row in rows:
        lines.append(_line(row, widths))
    return lines


def _line(cells, widths):
    padded = [str(cells[0]).ljust(widths[0])]
    for cell, width in zip(cells[1:], widths[1:]):
        padded.append(str(cell).rjust(width))
    return "  ".join(padded)


def _print_report(sections, preamble):
    print(f"\n{preamble}")
    for title, lines in sections:
        print(f"\n{_bold(title)}\n")
        print("\n".join(lines))


def _write_report(sections, preamble, results_file):
    """Replace the report file with the latest report."""
    stamp = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} — {_relative(results_file)}"
    report = ["# Benchmark report", "", stamp, "", preamble, ""]
    for title, lines in sections:
        report += [f"## {title}", "", "```", *lines, "```", ""]
    REPORTS_FILE.write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
