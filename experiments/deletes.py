"""Count the deletes each class relaxes, lifted and grounded, and plot how they relate to coverage.

The results only record the lifted deletes the relaxation drops. One lifted delete
can stand for thousands of grounded ones, so `scan` grounds every problem with
Fast Downward's translator and counts, for each class, how many of the task's
grounded deletes it relaxes.
"""

import argparse
import collections
import contextlib
import csv
import io
import json
import os
import statistics
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, _render
from experiments.report import KILLED_IN_PHASE, KILLED_IN_PHASE_DECIDING
from experiments.run import PROJECT_ROOT
from experiments.tracks import TRACKS, find_domain

TRACK_NAMES = ("sat/symmetries", "sat/resources", "opt/symmetries", "opt/resources", "unsat/symmetries")
FIELDS = ("domain", "problem", "class", "lifted", "ground_deletes", "ground_relaxed", "ground_relaxed_on_class")
TRANSLATOR = PROJECT_ROOT / "lib" / "downward" / "src" / "translate"
# The phases a run can die in that count as searching for the abstract plan or refining it.
DIED_IN = {
    "Abstract search": "search",
    "Guided concrete search": "refinement",
    "Extended concrete search": "refinement",
}
# Each abstract mode, with the tracks it runs on.
SERIES = (
    ("abs-lama", ("sat/symmetries", "sat/resources")),
    ("abs-asp", ("sat/symmetries", "sat/resources")),
    ("abs-lmcut", ("opt/symmetries", "opt/resources")),
    ("abs-asp", ("opt/symmetries", "opt/resources")),
    ("abs-ms", ("unsat/symmetries",)),
)


def count(spec):
    """One row per class of the problem the spec names, from a single grounding of it."""
    sys.path.insert(0, str(TRANSLATOR))
    from fast_downward.translate import instantiate, normalize, options, pddl_parser

    from core.abstraction.factory import build_abstract_problem
    from core.planning.config import AbstractPlanningConfig

    domain, problem = spec["domain_file"], spec["problem_file"]
    with contextlib.redirect_stdout(io.StringIO()):
        options.set_options([domain, problem])
        task = pddl_parser.open(domain_filename=domain, problem_filename=problem)
        normalize.normalize(task)
        _reachable, _atoms, actions, *_ = instantiate.explore(task)

    for rank, objects in spec["classes"]:
        config = AbstractPlanningConfig(domain, problem, objects_to_abstract=objects.split())
        with contextlib.redirect_stdout(io.StringIO()):
            abstraction = build_abstract_problem(config)
        relaxed = collections.defaultdict(list)
        for action_name, effect in abstraction.relaxed_deletes:
            args = [arg.parameter().name if arg.is_parameter_exp() else str(arg) for arg in effect.fluent.args]
            relaxed[action_name.lower()].append((effect.fluent.fluent().name.lower(), args))
        parameters = {
            action.name.lower(): [p.name for p in action.parameters] for action in abstraction.problem.actions
        }
        collapsed = {name.lower() for name in objects.split()}

        totals = {"ground_deletes": 0, "ground_relaxed": 0, "ground_relaxed_on_class": 0}
        for action in actions:
            name, *args = action.name.strip("()").split()
            deletes = {(atom.predicate, tuple(atom.args)) for _condition, atom in action.del_effects}
            totals["ground_deletes"] += len(deletes)
            # A ground action names its schema's parameters in order, which grounds each relaxed delete.
            binding = dict(zip(parameters.get(name, []), args))
            for predicate, lifted_args in relaxed.get(name, []):
                atom = (predicate, tuple(binding.get(arg, arg) for arg in lifted_args))
                if atom in deletes:
                    totals["ground_relaxed"] += 1
                    totals["ground_relaxed_on_class"] += any(arg in collapsed for arg in atom[1])
        lifted = sum(len(deletes) for deletes in relaxed.values())
        yield {"domain": spec["domain"], "problem": spec["problem"], "class": rank, "lifted": lifted} | totals


def scan(args):
    """Ground every problem with a class, smallest first, and add its rows to each track's grounded_deletes.csv."""
    specs = []
    for track_name in args.tracks:
        track = TRACKS[track_name]
        out = track.directory / "grounded_deletes.csv"
        done = {(row["domain"], row["problem"]) for row in _rows(out)}
        problems = {}
        for line in track.classes_file.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            name, rank, _type, _size, objects = line.split("\t")
            domain, _, problem = name.rpartition("/")
            if (domain, problem) in done:
                continue
            problem_file = track.benchmarks_dir / domain / problem
            spec = problems.setdefault(
                (domain, problem),
                {
                    "out": str(out),
                    "domain": domain,
                    "problem": problem,
                    "classes": [],
                    "problem_file": str(problem_file),
                    "domain_file": str(find_domain(problem_file)),
                },
            )
            spec["classes"].append([int(rank), objects])
        specs.extend(problems.values())
    specs.sort(key=lambda spec: Path(spec["problem_file"]).stat().st_size)
    print(f"{len(specs)} problems to ground with {args.workers} workers, {args.memory} GiB and {args.timeout} s each")

    # Numeric libraries otherwise start a thread per core in every worker.
    environment = os.environ | {name: "1" for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")}

    def run(spec):
        command = [
            "nice",
            "-n",
            "19",
            "prlimit",
            f"--as={args.memory * 1024**3}",
            "timeout",
            str(args.timeout),
            sys.executable,
            "-m",
            "experiments.deletes",
            "count",
            json.dumps(spec),
        ]
        result = subprocess.run(command, capture_output=True, text=True, cwd=PROJECT_ROOT, env=environment)
        rows = [json.loads(line) for line in result.stdout.splitlines() if line.startswith("{")]
        if not rows:
            print(f"failed: {spec['domain']}/{spec['problem']}", flush=True)
        return spec["out"], rows

    with ThreadPoolExecutor(args.workers) as pool:
        for out, rows in pool.map(run, specs):
            _append(Path(out), rows)


def _rows(path):
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def _append(path, rows):
    if not rows:
        return
    new = not path.is_file()
    with path.open("a", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\r\n")
        if new:
            writer.writeheader()
        writer.writerows(rows)


def figure(args):
    """Two plots per measure: coverage over every run, and over domains weighted equally."""
    lifted = {"label": "Relaxed deletes", "bins": [str(k) for k in range(14)] + ["14+"]}
    grounded = {"label": r"Grounded deletes relaxed (\%)", "bins": [str(10 * k + 5) for k in range(10)]}
    for measure, out in ((lifted, args.out_lifted), (grounded, args.out_grounded)):
        shares = {}
        if measure is grounded:
            for track_name in TRACK_NAMES:
                for row in _rows(TRACKS[track_name].directory / "grounded_deletes.csv"):
                    if int(row["ground_deletes"]):
                        key = (track_name, row["domain"], row["problem"], row["class"])
                        shares[key] = 100 * int(row["ground_relaxed"]) / int(row["ground_deletes"])

        def bin_of(track_name, row):
            if measure is lifted:
                if not row["relaxed_deletes"].strip():
                    return None
                return min(int(float(row["relaxed_deletes"])), 14)
            share = shares.get((track_name, row["domain"], row["problem"], row["class"] or "0"))
            return None if share is None else min(int(share // 10), 9)

        panels = [_panel(measure, bin_of, by_domain) for by_domain in (False, True)]
        _render(args.paper, panels, Path(out))
        print(f"Wrote {out}")


def _panel(measure, bin_of, by_domain):
    """The share solved, averaged over the modes, against the left axis, and the mean search and
    refinement shares of every run's time, over every mode, against the right axis."""
    solved_by_mode = collections.defaultdict(list)
    times = {"search": collections.defaultdict(list), "refinement": collections.defaultdict(list)}
    for mode, tracks in SERIES:
        runs = collections.defaultdict(lambda: [0, 0])  # (bin, track, domain) -> solved, runs
        for track_name in tracks:
            for row in _rows(TRACKS[track_name].results_file):
                if row["mode"] != mode or row["status"] == "running":
                    continue
                b = bin_of(track_name, row)
                if b is None:
                    continue
                key = (b, track_name, row["domain"])
                solved = row["status"] == "success" and row.get("verdict") != "unknown"
                runs[key][0] += solved
                runs[key][1] += 1
                for phase, share in _phase_shares(row, solved).items():
                    if share is not None:
                        times[phase][key].append(share)
        for b, value in _shares(runs, by_domain).items():
            solved_by_mode[b].append(value)

    def coordinates(values):
        return " ".join(f"({measure['bins'][b]},{value:.2f})" for b, value in sorted(values.items()))

    solved = {b: statistics.mean(values) for b, values in solved_by_mode.items()}
    search, refinement = (_typical_times(times[phase], by_domain) for phase in ("search", "refinement"))

    if measure["bins"][0] == "0":
        x_axis = (
            "symbolic x coords={" + ",".join(measure["bins"]) + "}, xtick={" + ",".join(measure["bins"]) + "},"
            " x tick label style={font=\\scriptsize}"
        )
    else:
        x_axis = "xmin=0, xmax=100, xtick={0,10,...,100}"
    title = "Domains weighted equally" if by_domain else "Every run counted"
    common = (
        "width=3in, height=2.2in, " + x_axis + ", axis line style={black!50}, tick style={black!50},"
        " tick label style={font=\\footnotesize}, label style={font=\\footnotesize}"
    )
    search_style, refinement_style = "abst, thick, mark=none", "conc, thick, dashed, mark=none"
    return (
        "\\begin{tikzpicture}\n"
        f"\\begin{{axis}}[{common}, axis y line*=left, title={{\\small {title}}}, xlabel={{{measure['label']}}},"
        " ylabel={Problems solved (\\%)}, ymin=0, ymax=100, ymajorgrids, grid style={black!10}]\n"
        rf"\addplot[black, very thick, mark=none] coordinates {{{coordinates(solved)}}};"
        "\n\\end{axis}\n"
        f"\\begin{{axis}}[{common}, axis y line*=right, axis x line=none, ymin=0, ymax=100,"
        " ylabel={Share of runtime (\\%)},"
        " legend style={font=\\scriptsize, draw=none, fill=none, at={(0.5,-0.26)}, anchor=north},"
        " legend columns=3]\n"
        "\\addlegendimage{black, very thick}\\addlegendentry{Solved}\n"
        rf"\addplot[{search_style}] coordinates {{{coordinates(search)}}};\addlegendentry{{Search}}"
        "\n"
        rf"\addplot[{refinement_style}] coordinates {{{coordinates(refinement)}}};\addlegendentry{{Refinement}}"
        "\n\\end{axis}\n\\end{tikzpicture}"
    )


def _phase_shares(row, solved):
    """The share of a run's time spent finding the abstract plan and refining it, or None for a phase it never had.

    A run that failed records no time for the phase it died in. Its time beyond the
    phases it completed goes to the phase after the last of them.
    """
    total = float(row["wall_time_seconds"])
    if not total:
        return {"search": None, "refinement": None}

    def recorded(*columns):
        values = [float(row[column]) for column in columns if row.get(column, "").strip()]
        return sum(values) if values else None

    seconds = {
        "search": recorded("abstract_solving_seconds", "abstract_fd_search_seconds"),
        "refinement": recorded("guided_concrete_solving_seconds", "extended_concrete_solving_seconds"),
    }
    if not solved:
        phases = KILLED_IN_PHASE_DECIDING if row["mode"] == "abs-ms" else KILLED_IN_PHASE
        died_in = DIED_IN.get(phases.get(row["last_completed_phase"]))
        if died_in:
            columns = [c for c in row if c.endswith("_seconds") and c not in ("wall_time_seconds", "total_seconds")]
            unrecorded = total - sum(float(row[c]) for c in columns if row[c].strip())
            seconds[died_in] = (seconds[died_in] or 0) + max(unrecorded, 0)
    return {phase: None if value is None else 100 * value / total for phase, value in seconds.items()}


def _typical_times(times, by_domain):
    """Per bin, the mean share over its runs, or the mean of its domains' means when domains weigh equally."""
    values = {}
    for b in sorted({key[0] for key in times}):
        cells = [cell for key, cell in times.items() if key[0] == b and cell]
        if by_domain and len(cells) >= 3:
            values[b] = statistics.mean(statistics.mean(cell) for cell in cells)
        elif not by_domain and sum(len(cell) for cell in cells) >= 10:
            values[b] = statistics.mean(share for cell in cells for share in cell)
    return values


def _shares(runs, by_domain):
    """Per bin, the share of runs solved, with each domain weighing as much as any other when asked."""
    values = {}
    for b in sorted({key[0] for key in runs}):
        cells = [counts for key, counts in runs.items() if key[0] == b]
        if by_domain and len(cells) >= 3:
            values[b] = statistics.mean(100 * solved / total for solved, total in cells)
        elif not by_domain and sum(total for _solved, total in cells) >= 10:
            values[b] = 100 * sum(solved for solved, _total in cells) / sum(total for _solved, total in cells)
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    one = commands.add_parser("count", help="Count one problem's classes, from a JSON spec, as JSON lines")
    one.add_argument("spec")
    every = commands.add_parser("scan", help="Count every problem of the tracks into their grounded_deletes.csv")
    every.add_argument("--tracks", nargs="+", default=list(TRACK_NAMES), choices=TRACK_NAMES)
    every.add_argument("--workers", type=int, default=2)
    every.add_argument("--memory", type=int, default=3, help="GiB per problem")
    every.add_argument("--timeout", type=int, default=600, help="Seconds per problem")
    plot = commands.add_parser("figure", help="Plot coverage against relaxed deletes")
    plot.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, whose preamble the figure uses")
    plot.add_argument("--out-lifted", default="relaxed-deletes.png")
    plot.add_argument("--out-grounded", default="grounded-relaxed-deletes.png")
    args = parser.parse_args()

    if args.command == "count":
        for row in count(json.loads(args.spec)):
            print(json.dumps(row), flush=True)
    elif args.command == "scan":
        scan(args)
    else:
        figure(args)


if __name__ == "__main__":
    main()
