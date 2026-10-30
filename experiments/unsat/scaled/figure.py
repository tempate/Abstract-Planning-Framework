"""Draw the scaled track's time against class size, one panel per domain, for the paper and as a PNG."""

import argparse
import collections
import csv
import statistics
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, TIME_LIMIT, UNSOLVED, _render
from experiments.tracks import TRACKS
from experiments.unsat.scaled.suite import DOMAINS

MODES = (("ms", "conc", "mark=*", r"\MS"), ("abs-ms", "abst", "mark=square*", r"\MSa"))


def series(results_file):
    """Per domain and mode, each problem's time at each class size, with a failure at UNSOLVED."""
    times = collections.defaultdict(lambda: collections.defaultdict(dict))
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            domain, _, size = row["domain"].rpartition("/")
            proved = row["status"] == "success" and row["verdict"] == "unsolvable"
            seconds = float(row["wall_time_seconds"]) if proved else UNSOLVED
            times[(domain, row["mode"])][row["problem"]][int(size.removeprefix("size-"))] = seconds
    return times


def panel(domain, times, legend):
    lines = [
        rf"\addplot[black!35, dashed, no marks, forget plot] coordinates {{(1.8,{TIME_LIMIT}) (1150,{TIME_LIMIT})}};",
    ]
    for mode, color, mark, label in MODES:
        problems = times[(domain, mode)]
        for sizes in problems.values():
            points = " ".join(f"({size},{seconds:.2f})" for size, seconds in sorted(sizes.items()))
            lines.append(rf"\addplot[{color}, opacity=0.3, thin, no marks, forget plot] coordinates {{{points}}};")
        # Problems start at their own class size, so a size's median covers the problems that reach it.
        by_size = collections.defaultdict(list)
        for sizes in problems.values():
            for size, seconds in sizes.items():
                by_size[size].append(seconds)
        median = " ".join(f"({size},{statistics.median(v):.2f})" for size, v in sorted(by_size.items()))
        lines.append(rf"\addplot[{color}, very thick, {mark}, mark size=1.2pt] coordinates {{{median}}};")
        if legend:
            lines.append(rf"\addlegendentry{{{label}}}")
    options = (
        "scale only axis, width=1.2in, height=1.1in, xmin=1.8, xmax=1150, ymin=1, ymax=9000,"
        " xtick={2,10,100,1000}, xticklabels={2,10,100,1000},"
        f" ytick={{1,10,100,1000,{UNSOLVED:.0f}}}, yticklabels={{1,10,100,1000,fail}}, minor tick length=0pt,"
        rf" title={{\small {domain} ({len(times[(domain, 'abs-ms')])})}}, xlabel={{Size of the symmetric class}},"
        + (" ylabel={Time (s)}," if legend else " yticklabels={},")
        + " axis line style={black!50}, tick style={black!50}, xtick pos=bottom, ytick pos=left,"
        r" tick label style={font=\footnotesize}, label style={font=\footnotesize}, title style={yshift=-3pt}"
    )
    if legend:
        options += (
            r", legend style={font=\footnotesize, draw=none, fill=none, at={(0,1.2)}, anchor=south west,"
            " /tikz/every even column/.append style={column sep=10pt}}, legend columns=2, legend cell align=left"
        )
    body = "\n".join(lines)
    return (
        f"\\begin{{tikzpicture}}\n\\begin{{loglogaxis}}[{options}]\n{body}\n\\end{{loglogaxis}}\n\\end{{tikzpicture}}"
    )


def figure(results_file):
    times = series(results_file)
    return "\\hfill\n".join(panel(domain, times, index == 0) for index, domain in enumerate(DOMAINS))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--results", default=TRACKS["scaled/symmetries"].results_file, type=Path)
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, whose preamble the figure uses")
    parser.add_argument("--out", default="scaled.png", help="PNG file to write")
    parser.add_argument("--tex", type=Path, help="Also write the panels as TikZ, for the paper's figure")
    args = parser.parse_args()

    panels = figure(args.results)
    if args.tex:
        args.tex.write_text(panels + "\n")
    # The renderer sets two panels side by side, and this figure is one row of them.
    _render(args.paper, [r"\begin{minipage}{6.9in}" + panels + r"\end{minipage}", ""], Path(args.out))
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
