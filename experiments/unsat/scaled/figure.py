"""Draw the scaled track's median time against class size, over every problem, for the paper and as a PNG."""

import argparse
import collections
import csv
import statistics
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, TIME_LIMIT, UNSOLVED, _render
from experiments.tracks import TRACKS

MODES = (("ms", "conc", "mark=*", r"\MS"), ("abs-ms", "abst", "mark=square*", r"\MSa"))


def series(results_file):
    """Per mode, each base problem's time at each class size, with a failure at UNSOLVED."""
    times = collections.defaultdict(lambda: collections.defaultdict(dict))
    with Path(results_file).open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            domain, _, size = row["domain"].rpartition("/")
            proved = row["status"] == "success" and row["verdict"] == "unsolvable"
            seconds = float(row["wall_time_seconds"]) if proved else UNSOLVED
            times[row["mode"]][(domain, row["problem"])][int(size.removeprefix("size-"))] = seconds
    return times


def figure(results_file):
    times = series(results_file)
    lines = [
        rf"\addplot[black!35, dashed, no marks, forget plot] coordinates {{(1.8,{TIME_LIMIT}) (1150,{TIME_LIMIT})}};",
        rf"\node[font=\scriptsize, text=black!50, anchor=south east] at (axis cs:1150,{TIME_LIMIT}) {{time limit}};",
    ]
    for mode, color, mark, label in MODES:
        # Problems start at their own class size, so some sizes hold only a few of them,
        # and the median skips the sizes that hold fewer than half.
        by_size = collections.defaultdict(list)
        for sizes in times[mode].values():
            for size, seconds in sizes.items():
                by_size[size].append(seconds)
        enough = len(times[mode]) / 2
        median = " ".join(
            f"({size},{statistics.median(v):.2f})" for size, v in sorted(by_size.items()) if len(v) >= enough
        )
        lines.append(rf"\addplot[{color}, very thick, {mark}, mark size=1.4pt] coordinates {{{median}}};")
        lines.append(rf"\addlegendentry{{{label}}}")
    options = (
        r"scale only axis, width=0.8\columnwidth, height=0.5\columnwidth, xmin=1.8, xmax=1150, ymin=1, ymax=9000,"
        " xtick={2,10,100,1000}, xticklabels={2,10,100,1000},"
        f" ytick={{1,10,100,1000,{UNSOLVED:.0f}}}, yticklabels={{1,10,100,1000,fail}}, minor tick length=0pt,"
        " xlabel={Size of the symmetric class}, ylabel={Time (s)},"
        " axis line style={black!50}, tick style={black!50}, xtick pos=bottom, ytick pos=left,"
        r" tick label style={font=\footnotesize}, label style={font=\footnotesize},"
        r" legend style={font=\footnotesize, draw=none, fill=none, at={(0.5,1.03)}, anchor=south,"
        " /tikz/every even column/.append style={column sep=10pt}}, legend columns=2, legend cell align=left"
    )
    body = "\n".join(lines)
    return (
        f"\\begin{{tikzpicture}}\n\\begin{{loglogaxis}}[{options}]\n{body}\n\\end{{loglogaxis}}\n\\end{{tikzpicture}}"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--results", default=TRACKS["scaled/symmetries"].results_file, type=Path)
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, whose preamble the figure uses")
    parser.add_argument("--out", default="scaled.png", help="PNG file to write")
    parser.add_argument("--tex", type=Path, help="Also write the plot as TikZ, for the paper's figure")
    args = parser.parse_args()

    plot = figure(args.results)
    if args.tex:
        args.tex.write_text(plot + "\n")
    # The renderer sets two panels side by side, and this figure has one, a column wide like the paper's.
    _render(args.paper, [r"\begin{minipage}{\columnwidth}\centering " + plot + r"\end{minipage}", ""], Path(args.out))
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
