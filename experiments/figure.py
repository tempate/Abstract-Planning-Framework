"""Draw the paper's figure for one track kind, a PR's base on the left and its branch on the right, as a PNG."""

import argparse
import csv
import io
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from experiments.report import _finished_problems
from experiments.run import ABSTRACTION_PREFIX, PROJECT_ROOT

SOURCES = {"symmetries": "Symmetric objects", "resources": "Resource levels"}
# The unsolvability track collapses symmetric objects only.
KIND_SOURCES = {"sat": tuple(SOURCES), "opt": tuple(SOURCES), "unsat": ("symmetries",)}
# The figure draws a problem a mode leaves unsolved on this border, past the 1800 s limit.
UNSOLVED = 6000.0
TIME_LIMIT = 1800
BASELINES = {"sat": ("lama", r"\LAMA", r"\LAMAa"), "opt": ("lmcut", r"\LMcut", r"\LMcuta")}
# Branches from before #135 still call Fast Downward's modes by their old names.
OLD_NAMES = {
    "sat": {"fd": "lama", "abs-fd": "abs-lama"},
    "opt": {"fd-lmcut": "lmcut", "abs-fd": "abs-lmcut"},
    "unsat": {"fd": "ms", "abs-fd": "abs-ms"},
}
DEFAULT_PAPER = PROJECT_ROOT.parent / "paper" / "planpilot_abstractions" / "icaps27" / "main.tex"


def main():
    args = _argument_parser().parse_args()
    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]
    panel = _unsat_panel if args.kind == "unsat" else _panel
    # A label like #134 would otherwise read as a macro parameter in LaTeX.
    base_label = args.base_label.replace("#", r"\#")
    panels = [
        panel(f"Before ({base_label})", args.kind, _tracks(args.base, args.kind, base_manifests)),
        panel("After", args.kind, _tracks(args.branch, args.kind, manifests)),
    ]
    _render(args.paper, panels, Path(args.out))
    print(f"Wrote {args.out}")


def select(rows, kind, source, manifests):
    """Rename old modes, and keep only the abstract rows this track's manifests submitted, for the modes they submitted."""
    renames = OLD_NAMES[kind]
    submitted = set()
    for manifest in manifests:
        # A manifest speaks for its own track only, which may have run other classes.
        if manifest["track"] != f"{kind}/{source}":
            continue
        for entry in manifest["expected_results"]:
            mode = renames.get(entry["mode"], entry["mode"])
            if mode.startswith(ABSTRACTION_PREFIX):
                submitted.add((mode, entry["domain"], entry["problem"], int(entry["class"] or 0)))
    filtered_modes = {mode for mode, *_ in submitted}

    selected = []
    for row in rows:
        row = row | {"mode": renames.get(row["mode"], row["mode"])}
        key = (row["mode"], row["domain"], row["problem"], int(row["class"] or 0))
        if row["mode"] not in filtered_modes or key in submitted:
            selected.append(row)
    return selected


def extra_actions_class(problem, abstraction, baseline):
    """The colour class of an abstract plan's extra actions over an optimal plan, 4 when there is none to compare."""
    optimum = next((int(problem[m]["plan_length"]) for m in ("asp", baseline) if _solved(problem[m])), None)
    if optimum is None or not _solved(problem[abstraction]):
        return 4
    extra = int(problem[abstraction]["plan_length"]) - optimum
    return 0 if extra <= 0 else 1 if extra <= 2 else 2 if extra <= 5 else 3


def _tracks(revision, kind, manifests):
    """Each abstraction source's finished problems at a revision, as the report pairs them."""
    tracks = {}
    for source in KIND_SOURCES[kind]:
        text = subprocess.check_output(
            ["git", "-C", PROJECT_ROOT, "show", f"{revision}:experiments/{kind}/{source}/results.csv"], text=True
        )
        rows = select(list(csv.DictReader(io.StringIO(text))), kind, source, manifests)
        with tempfile.NamedTemporaryFile("w", suffix=".csv", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
            stream.flush()
            tracks[source] = _finished_problems(stream.name)[1]
    return tracks


def _panel(title, kind, tracks):
    baseline, label, abstract_label = BASELINES[kind]
    plot = r"\borderlengthplot" if kind == "opt" else r"\borderplot"
    curves = (
        ("asp", "conc, solid", r"\ASP"),
        ("abs-asp", "abst, solid", r"\ASPa"),
        (f"abs-{baseline}", "abst, dashed", abstract_label),
        (baseline, "conc, dashed", label),
    )

    cactus_plots = []
    for source, problems in tracks.items():
        lines = []
        for mode, style, name in curves:
            lines.append(rf"\addplot[{style}, thick, const plot, mark=none] coordinates {{{_cactus(problems, mode)}}};")
            # One legend serves both plots, so only the last carries it.
            if source == "resources":
                lines.append(rf"\addlegendentry{{{name}}}")
        cactus_plots.append(
            "\\begin{tikzpicture}\n\\begin{semilogxaxis}[cactusplot, title={\\small "
            + SOURCES[source]
            + "}]\n"
            + "\n".join(lines)
            + "\n\\end{semilogxaxis}\n\\end{tikzpicture}"
        )

    scatter_rows = []
    for source, problems in tracks.items():
        asp = _scatter(problems, "asp", "abs-asp", kind, baseline)
        fd = _scatter(problems, baseline, f"abs-{baseline}", kind, baseline)
        scatter_rows.append(
            rf"{{\small {SOURCES[source]}}}\\[2pt]"
            + "\n"
            + rf"{plot}{{\ASP}}{{\ASPa}}{{{asp}}}\hfill{plot}{{{label}}}{{{abstract_label}}}{{{fd}}}"
        )

    key = ""
    if kind == "opt":
        key = (
            r"{\footnotesize Extra actions over the optimum\\ \outcomekey{ext0} 0\quad \outcomekey{ext1} 1--2\quad "
            r"\outcomekey{ext2} 3--5\quad \outcomekey{ext3} 6 or more\quad \outcomekey{black!40} no plan to compare}"
            "\n\n"
        )
    return (
        "\\begin{minipage}[t]{\\columnwidth}\n\\centering\n"
        + f"{{\\large\\bfseries\\strut {title}}}\\par\\vspace{{2.2em}}\n"
        + "\\hfill".join(cactus_plots)
        + "\n\n{\\small (a) Problems solved over time}\n\n\\bigskip\n"
        + "\n\n".join(scatter_rows)
        + "\n\n"
        + key
        + "{\\small (b) Runtime per problem}\n\\end{minipage}"
    )


def _unsat_panel(title, _kind, tracks):
    problems = tracks["symmetries"]
    cactus = (
        "\\begin{tikzpicture}\n\\begin{semilogxaxis}[cactusplot, ylabel={Problems proved}, legend columns=1, "
        "legend style={at={(0.03,0.97)}, anchor=north west}]\n"
        + rf"\addplot[abst, solid, thick, const plot, mark=none] coordinates {{{_cactus(problems, 'abs-ms')}}};"
        + "\n\\addlegendentry{\\MSa}\n"
        + rf"\addplot[conc, solid, thick, const plot, mark=none] coordinates {{{_cactus(problems, 'ms')}}};"
        + "\n\\addlegendentry{\\MS}\n\\end{semilogxaxis}\n\\end{tikzpicture}"
    )
    scatter = rf"\borderplot{{\MS}}{{\MSa}}{{{_scatter(problems, 'ms', 'abs-ms', 'unsat', None)}}}"
    return (
        "\\begin{minipage}[t]{\\columnwidth}\n\\centering\n"
        + f"{{\\large\\bfseries\\strut {title}}}\\par\\vspace{{1em}}\n"
        + cactus
        + "\\hfill"
        + scatter
        + "\n\n\\makebox[0.48\\columnwidth]{\\small (a) Problems proved}\\hfill"
        + "\\makebox[0.48\\columnwidth]{\\small (b) Runtime per problem}\n\\end{minipage}"
    )


def _cactus(problems, mode):
    times = sorted(float(p[mode]["wall_time_seconds"]) for p in problems if _solved(p[mode]))
    # The curve runs on to the time limit, so a mode that stops solving early shows as flat.
    points = [f"({time:.2f},{count})" for count, time in enumerate(times, 1)]
    return " ".join(["(1,0)", *points, f"({TIME_LIMIT},{len(times)})"])


def _scatter(problems, solver, abstraction, kind, baseline):
    points = []
    for problem in problems:
        x, y = _time(problem[solver]), _time(problem[abstraction])
        if x is None and y is None:
            continue
        point = f"({x or UNSOLVED:.2f},{y or UNSOLVED:.2f})"
        if kind == "opt":
            point += f" [{extra_actions_class(problem, abstraction, baseline)}]"
        points.append(point)
    return " ".join(points)


def _solved(row):
    # An abstraction that finds a plan leaves an unsolvability verdict unknown, which proves nothing.
    return row["status"] == "success" and row.get("verdict") != "unknown"


def _time(row):
    return float(row["wall_time_seconds"]) if _solved(row) else None


def _render(paper, panels, out):
    """Typeset both panels with the paper's preamble, then crop the page to a PNG."""
    preamble = Path(paper).read_text().split(r"\title{")[0]
    document = (
        preamble
        + "\\pagestyle{empty}\n\\begin{document}\n\\noindent\\mbox{"
        + panels[0]
        + r"\hspace{2em}"
        + panels[1]
        + "}\n\\end{document}\n"
    )
    with tempfile.TemporaryDirectory() as directory:
        build = Path(directory)
        # The paper's style file has to sit next to the document that loads it.
        for style in Path(paper).parent.glob("*.sty"):
            shutil.copy(style, build)
        (build / "figure.tex").write_text(document)
        commands = [
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "figure.tex"],
            ["pdfcrop", "--margins", "8", "figure.pdf", "cropped.pdf"],
            ["pdftoppm", "-png", "-r", "250", "-singlefile", "cropped.pdf", "figure"],
        ]
        for command in commands:
            subprocess.run(command, cwd=build, check=True, capture_output=True)
        shutil.copy(build / "figure.png", out)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(KIND_SOURCES), help="Which of the paper's figures to draw")
    parser.add_argument("--base", default="origin/main", help="Revision whose results.csv files go on the left")
    parser.add_argument("--base-label", default="main", help="Name of the base in the left panel's title")
    parser.add_argument("--branch", default="HEAD", help="Revision whose results.csv files go on the right")
    parser.add_argument(
        "--manifests",
        nargs="*",
        default=[],
        help="The branch's run manifests; its abstract modes then show only the classes these runs submitted",
    )
    parser.add_argument(
        "--base-manifests", nargs="*", default=[], help="The same for the base, when it is a PR with its own runs"
    )
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, whose preamble the figure uses")
    parser.add_argument("--out", required=True, help="PNG file to write, named <PR>-<kind>-before-after.png")
    return parser


if __name__ == "__main__":
    main()
