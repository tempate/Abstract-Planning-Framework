"""Print a PR's plans-found and median-runtime tables, base → branch, for its description."""

import argparse
import json
import statistics
from pathlib import Path

from experiments.figure import load_tracks, solve_time, solved

LABELS = {"abs-asp": "ASPᵅ", "abs-lama": "LAMAᵅ", "abs-lmcut": "LMcutᵅ", "abs-ms": "M&Sᵅ"}


def main():
    args = _argument_parser().parse_args()
    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]
    columns = {}
    for track, modes in submitted_tracks(manifests).items():
        kind, source = track.split("/")
        base = load_tracks(args.base, kind, base_manifests, [source])[source]
        branch = load_tracks(args.branch, kind, manifests, [source])[source]
        columns[f"{kind} {source}"] = (base, branch, modes)
    print(tables(columns))


def submitted_tracks(manifests):
    """The abstract modes each track's manifests submitted, by track such as sat/resources."""
    tracks = {}
    for manifest in manifests:
        modes = tracks.setdefault(manifest["track"], set())
        modes.update(entry["mode"] for entry in manifest["expected_results"] if entry["mode"] in LABELS)
    return tracks


def tables(columns):
    """The two tables, one column per track and one row per abstract mode any track submitted."""
    modes = [mode for mode in LABELS if any(mode in submitted for *_, submitted in columns.values())]
    plans, runtimes = [], []
    for mode in modes:
        plan_cells, runtime_cells = [], []
        for base, branch, submitted in columns.values():
            if mode not in submitted:
                plan_cells.append("")
                runtime_cells.append("")
                continue
            plan_cells.append(_plans_cell(base, branch, mode))
            runtime_cells.append(_runtime_cell(base, branch, mode))
        plans.append(_line(LABELS[mode], plan_cells))
        runtimes.append(_line(LABELS[mode], runtime_cells))
    header = list(columns)
    return "\n".join(
        [
            _line("Plans found", header),
            _rule(header),
            *plans,
            "",
            _line("Median runtime", header),
            _rule(header),
            *runtimes,
        ]
    )


def _plans_cell(base, branch, mode):
    before = sum(solved(problem[mode]) for problem in base)
    after = sum(solved(problem[mode]) for problem in branch)
    bold = lambda count, other: f"**{count}**" if count > other else str(count)
    return f"{bold(before, after)} → {bold(after, before)}"


def _runtime_cell(base, branch, mode):
    # Compare the two sides on the problems both solve, so a newly solved hard problem does not skew the median.
    before = {_key(problem): problem[mode] for problem in base if solved(problem[mode])}
    after = {_key(problem): problem[mode] for problem in branch if solved(problem[mode])}
    shared = before.keys() & after.keys()
    if not shared:
        return ""
    median = lambda rows: statistics.median(solve_time(rows[key]) for key in shared)
    return f"{median(before):.1f} → {median(after):.1f} s"


def _key(problem):
    row = next(iter(problem.values()))
    return row["domain"], row["problem"]


def _line(label, cells):
    return "|" + "|".join(f" {cell} " if cell else " " for cell in [label, *cells]) + "|"


def _rule(header):
    return "|" + "---|" * (len(header) + 1)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main", help="Revision whose results.csv files are the before side")
    parser.add_argument("--branch", default="HEAD", help="Revision whose results.csv files are the after side")
    parser.add_argument(
        "--manifests", nargs="+", required=True, help="The branch's run manifests, which name its tracks"
    )
    parser.add_argument(
        "--base-manifests", nargs="*", default=[], help="The base's run manifests, when it is a PR with its own runs"
    )
    return parser


if __name__ == "__main__":
    main()
