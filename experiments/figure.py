"""Draw the paper's figure for one track kind, a PR's base on the left and its branch on the right, as a PNG."""

import argparse
import csv
import io
import json
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path

from experiments.report import finished_problems
from experiments.run import ABSTRACTION_PREFIX, PROJECT_ROOT

SOURCES = {"symmetries": "Symmetries", "resources": "Resources"}
# The unsolvability track collapses symmetric objects only.
# The hard-to-ground tracks collapse symmetric objects only, and the htg figure draws both of them.
KIND_SOURCES = {
    "sat": tuple(SOURCES),
    "opt": tuple(SOURCES),
    "unsat": ("symmetries",),
    "sat-htg": ("symmetries",),
    "opt-htg": ("symmetries",),
    # The unsat track's grown problems, which the scaled figure draws for the branch alone.
    "scaled": ("symmetries",),
}
FIGURES = ("sat", "opt", "unsat", "htg", "scaled")
# The figure draws a problem a mode leaves unsolved on this border, past the 1800 s limit.
UNSOLVED = 6000.0
TIME_LIMIT = 1800
TRACK_NAMES = {"sat": "Satisficing", "opt": "Optimal", "unsat": "Unsolvability"}
# Each track's solvers with their labels, each drawn against its abstraction, the first with solid lines.
PAIRS = {
    "sat": (("lama", r"\LAMA", r"\LAMAa"), ("asp", r"\ASP", r"\ASPa")),
    "opt": (("lmcut", r"\LMcut", r"\LMcuta"), ("asp", r"\ASP", r"\ASPa")),
    "unsat": (("ms", r"\MS", r"\MSa"),),
}
# Lifts a cactus plot's source title over the legend that sits just above the plot.
ABOVE_LEGEND = "title style={yshift=11pt}"
# A plot that carries its own legend, centred above it in rows of two.
CENTRED_LEGEND = "legend columns=2, legend style={overlay, at={(0.5,1.04)}, anchor=south}"
# Branches from before #135 still call Fast Downward's modes by their old names.
OLD_NAMES = {
    "sat": {"fd": "lama", "abs-fd": "abs-lama"},
    "opt": {"fd-lmcut": "lmcut", "abs-fd": "abs-lmcut"},
    "unsat": {"fd": "ms", "abs-fd": "abs-ms"},
}
DEFAULT_PAPER = PROJECT_ROOT.parent / "paper" / "planpilot_abstractions" / "icaps27" / "main.tex"


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    if args.sources and args.kind not in ("sat", "opt"):
        parser.error("--sources applies to the sat and opt figures only")
    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]
    if args.kind == "scaled":
        panels = [_scaled_plot(load_tracks(args.branch, args.kind, manifests)["symmetries"])]
    elif args.no_base:
        panels = [_panel("", args.kind, load_tracks(args.branch, args.kind, manifests, args.sources))]
    else:
        # A label like #134 would otherwise read as a macro parameter in LaTeX.
        base_label = args.base_label.replace("#", r"\#")
        panels = [
            _panel(
                f"Before ({base_label})", args.kind, load_tracks(args.base, args.kind, base_manifests, args.sources)
            ),
            _panel("After", args.kind, load_tracks(args.branch, args.kind, manifests, args.sources)),
        ]
    _render(args.paper, panels, Path(args.out))
    print(f"Wrote {args.out}")


def select(rows, kind, source, manifests):
    """Rename old modes, and keep only the abstract rows this track's manifests submitted, for the modes they submitted."""
    # The HTG tracks came after #135, so they never used the old names.
    renames = OLD_NAMES.get(kind, {})
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


def load_tracks(revision, kind, manifests, sources=None):
    """Each abstraction source's finished problems at a revision, as the report pairs them."""
    if kind == "htg":
        return {track: load_tracks(revision, f"{track}-htg", manifests)["symmetries"] for track in ("sat", "opt")}
    tracks = {}
    for source in sources or KIND_SOURCES[kind]:
        rows = csv.DictReader(io.StringIO(_results_at(revision, kind, source)))
        tracks[source] = finished_problems(select(rows, kind, source, manifests))[1]
    return tracks


def _results_at(revision, kind, source):
    if kind.endswith("-htg"):
        directories = (f"experiments/htg/{kind.removesuffix('-htg')}",)
    elif kind == "scaled":
        # The scaled problems keep their results inside the unsat track's directory.
        directories = ("experiments/ipc/unsat/scaled", "experiments/unsat/scaled")
    else:
        # Revisions from before experiments/ipc/ keep the IPC tracks one level higher.
        directories = (f"experiments/ipc/{kind}/{source}", f"experiments/{kind}/{source}")
    for directory in directories:
        shown = subprocess.run(
            ["git", "-C", PROJECT_ROOT, "show", f"{revision}:{directory}/results.csv"], capture_output=True, text=True
        )
        if shown.returncode == 0:
            return shown.stdout
    raise SystemExit(f"No {kind}/{source} results.csv at {revision}")


def paper_figures(revision):
    """The paper's figures at a revision, by the file name main.tex includes, each the body of a PDF."""
    tracks = {kind: load_tracks(revision, kind, []) for kind in TRACK_NAMES}
    htg = load_tracks(revision, "htg", [])
    # Each PDF is as wide as the float main.tex includes it in, so it keeps the paper's sizes.
    return {
        "ipc": _minipage(r"\textwidth", _ipc_figure(tracks)),
        "scaled": _minipage(r"\columnwidth", _scaled_plot(load_tracks(revision, "scaled", [])["symmetries"])),
        "htg": _minipage(r"\columnwidth", _htg_figure(htg, PAPER_ROW_GAP)),
    }


# The paper sets its runtime plots a little further below the cactus plots than a PR's figure does.
PAPER_ROW_GAP = "\n\n\\smallskip\n\n\\medskip\n"


def _ipc_figure(tracks):
    """Figure 1, every track's plots side by side, so each row joins the tracks' own rows."""
    track_gap = "%\n\\hspace{0.1in}%\n\\hspace*{0.42in}%\n"
    header = "%\n\\hspace{0.52in}%\n".join(_track_title(TRACK_NAMES[kind], len(tracks[kind])) for kind in tracks)
    cactus_row = track_gap.join(_joined(_cactus_plots(kind, problems)) for kind, problems in tracks.items())
    runtime_rows = []
    for index in range(2):
        groups = []
        for kind, problems in tracks.items():
            rows = _runtime_rows(kind, problems)
            # The unsolvability track has no ASP row, so its place stays empty.
            groups.append(_joined(rows[index]) if index < len(rows) else "\\hspace{\\plotsize}")
        runtime_rows.append(_in_row(track_gap.join(groups)))
    return (
        _in_row(header)
        + "\n\n\\vspace{0.4em}\n"
        + _in_row(cactus_row)
        + PAPER_ROW_GAP
        + "\n\n\\smallskip\n".join(runtime_rows)
    )


def _panel(title, kind, tracks):
    """One track's half of a PR's figure, under a title."""
    if kind == "htg":
        return _titled(title, _htg_figure(tracks, "\n\n\\medskip\n"), 2)
    body = (
        _in_row(_track_title(TRACK_NAMES[kind], len(tracks)))
        + "\n\n\\vspace{0.4em}\n"
        + _in_row(_joined(_cactus_plots(kind, tracks)))
        + "\n\n\\medskip\n"
        + "\n\n\\smallskip\n".join(_in_row(_joined(plots)) for plots in _runtime_rows(kind, tracks))
    )
    return _titled(title, body, len(tracks))


def _htg_figure(tracks, row_gap):
    """Both hard-to-ground tracks, each with its baseline alone and its own legend."""
    # Both plots label their own y axis, so they need more room between them than the paper's rows.
    gap = "0.75in"
    cactus_plots, runtimes = [], []
    for track, problems in tracks.items():
        baseline = PAIRS[track][0]
        options = f"ylabel={{Problems solved}}, {CENTRED_LEGEND}"
        cactus_plots.append(_cactus_plot(TRACK_NAMES[track], problems, (baseline,), options, legend=True))
        runtimes.append(_runtime_plot(problems, baseline, labelled=True))
    return _in_row(_joined(cactus_plots, gap)) + row_gap + _in_row(_joined(runtimes, gap))


def _cactus_plots(kind, tracks):
    """One track's problems solved over time, a plot per abstraction source, the right one carrying the legend."""
    ylabel = "Problems proved" if kind == "unsat" else "Problems solved"
    plots = []
    for index, (source, problems) in enumerate(tracks.items()):
        if len(tracks) == 1:
            options, legend = f"ylabel={{{ylabel}}}, {CENTRED_LEGEND}", True
        elif index == 0:
            options, legend = f"ylabel={{{ylabel}}}", False
        else:
            options, legend = "ylabel={}, legend style={overlay, at={(-0.16,1.04)}, anchor=south}", True
        plots.append(_cactus_plot(SOURCES[source], problems, PAIRS[kind], options, legend))
    return plots


def _cactus_plot(title, problems, pairs, options, legend):
    lines = []
    for (solver, label, abstract_label), dash in zip(pairs, ("solid", "dashed")):
        for mode, color, name in ((solver, "conc", label), (f"abs-{solver}", "abst", abstract_label)):
            lines.append(
                rf"\addplot[{color}, {dash}, thick, const plot, mark=none] coordinates {{{cactus(problems, mode)}}};"
            )
            if legend:
                lines.append(rf"\addlegendentry{{{name}}}")
    return (
        "\\begin{tikzpicture}[trim axis left, trim axis right]\n"
        + rf"\begin{{semilogxaxis}}[cactusplot, title={{\small {title}}}, {ABOVE_LEGEND}, {options}]"
        + "\n"
        + "\n".join(lines)
        + "\n\\end{semilogxaxis}\n\\end{tikzpicture}"
    )


def _runtime_rows(kind, tracks):
    """One track's runtime per problem, a row per solver and a plot per abstraction source in each."""
    # The cactus plots above name the sources, so only the left plot labels its y axis.
    return [
        [_runtime_plot(problems, pair, labelled=index == 0) for index, problems in enumerate(tracks.values())]
        for pair in PAIRS[kind]
    ]


def _runtime_plot(problems, pair, labelled):
    solver, label, abstract_label = pair
    option = rf"ylabel={{{abstract_label}{{}} time (s)}}" if labelled else "yticklabels={}"
    return rf"\runtimeplot[{option}]{{{label}}}{{{scatter(problems, solver, f'abs-{solver}')}}}"


def _track_title(name, columns):
    # The track's name over its plots and the gaps between them, ruled like a table's cmidrule.
    width = f"\\dimexpr{columns}\\plotsize+{0.3 * (columns - 1):.1f}in\\relax"
    return rf"\parbox[b]{{{width}}}{{\centering\small {name}\\[-2pt]\rule{{\linewidth}}{{0.4pt}}}}"


def _joined(plots, gap="0.3in"):
    return f"%\n\\hspace{{{gap}}}%\n".join(plots)


def _in_row(content):
    # The paper's spacing: room for the y label on the left of the row.
    return "\\noindent\\makebox[\\linewidth][c]{%\n\\hspace*{0.42in}%\n" + content + "}"


def _titled(title, body, columns):
    # A single column of plots gets a narrow panel, so the two halves sit close together.
    width = "\\columnwidth" if columns > 1 else "2in"
    return (
        f"\\begin{{minipage}}[t]{{{width}}}\n\\centering\n"
        + f"{{\\large\\bfseries\\strut {title}}}\\par\\vspace{{2.4em}}\n"
        + body
        + "\n\\end{minipage}"
    )


def _minipage(width, body):
    return f"\\noindent\\begin{{minipage}}{{{width}}}\\centering\n{body}\n\\end{{minipage}}"


SCALED_MODES = (("ms", "conc", "*", r"\MS"), ("abs-ms", "abst", "square*", r"\MSa"))


def scaled_coverage(problems, mode):
    """The share of each class size's problems a mode proves unsolvable, in percent."""
    by_size = defaultdict(list)
    for problem in problems:
        by_size[int(problem[mode]["domain"].rsplit("/size-", 1)[1])].append(solved(problem[mode]))
    return [(size, 100 * sum(proved) / len(proved)) for size, proved in sorted(by_size.items())]


def _scaled_plot(problems):
    lines = []
    for mode, style, mark, name in SCALED_MODES:
        shares = " ".join(f"({size},{share:.2f})" for size, share in scaled_coverage(problems, mode))
        lines.append(rf"\addplot[{style}, very thick, mark={mark}, mark size=1.4pt] coordinates {{{shares}}};")
        lines.append(rf"\addlegendentry{{{name}}}")
    return (
        "\\begin{tikzpicture}\n\\begin{semilogxaxis}[scale only axis, width=0.8\\columnwidth, "
        "height=0.5\\columnwidth, xmin=1.8, xmax=1150, xtick={2,10,100,1000}, xticklabels={2,10,100,1000}, "
        "ymin=0, ymax=105, ytick={0,25,50,75,100}, minor tick length=0pt, xlabel={Size of the symmetric class}, "
        "ylabel={Problems proved (\\%)}, axis line style={black!50}, tick style={black!50}, "
        "xtick pos=bottom, ytick pos=left, tick label style={font=\\footnotesize}, label style={font=\\footnotesize}, "
        "legend style={font=\\footnotesize, draw=none, fill=none, at={(0.5,1.03)}, anchor=south, "
        "/tikz/every even column/.append style={column sep=10pt}}, legend columns=2, legend cell align=left]\n"
        + "\n".join(lines)
        + "\n\\end{semilogxaxis}\n\\end{tikzpicture}"
    )


def cactus(problems, mode):
    times = sorted(float(p[mode]["wall_time_seconds"]) for p in problems if solved(p[mode]))
    # The curve runs on to the time limit, so a mode that stops solving early shows as flat.
    points = [f"({time:.2f},{count})" for count, time in enumerate(times, 1)]
    return " ".join(["(1,0)", *points, f"({TIME_LIMIT},{len(times)})"])


def scatter(problems, solver, abstraction):
    points = []
    for problem in problems:
        x, y = solve_time(problem[solver]), solve_time(problem[abstraction])
        if x is None and y is None:
            continue
        points.append(f"({x or UNSOLVED:.2f},{y or UNSOLVED:.2f})")
    return " ".join(points)


def solved(row):
    # An abstraction that finds a plan leaves an unsolvability verdict unknown, which proves nothing.
    return row["status"] == "success" and row.get("verdict") != "unknown"


def solve_time(row):
    return float(row["wall_time_seconds"]) if solved(row) else None


def _render(paper, panels, out):
    """Typeset the panels side by side with the paper's preamble, then crop the page to a PNG."""
    with tempfile.TemporaryDirectory() as directory:
        render_pdf(paper, "\\noindent\\mbox{" + r"\hspace{2em}".join(panels) + "}", Path(directory, "figure.pdf"), 8)
        command = ["pdftoppm", "-png", "-r", "250", "-singlefile", "figure.pdf", "figure"]
        subprocess.run(command, cwd=directory, check=True, capture_output=True)
        shutil.copy(Path(directory, "figure.png"), out)


def render_pdf(paper, body, out, margins=0):
    """Typeset a body with the paper's preamble, then crop the page to a PDF."""
    preamble = Path(paper).read_text().split(r"\title{")[0]
    document = preamble + "\\pagestyle{empty}\n\\begin{document}\n" + body + "\n\\end{document}\n"
    with tempfile.TemporaryDirectory() as directory:
        # The paper's style file has to sit next to the document that loads it.
        for style in Path(paper).parent.glob("*.sty"):
            shutil.copy(style, directory)
        Path(directory, "figure.tex").write_text(document)
        for command in (
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "figure.tex"],
            ["pdfcrop", "--margins", str(margins), "figure.pdf", "cropped.pdf"],
        ):
            subprocess.run(command, cwd=directory, check=True, capture_output=True)
        shutil.copy(Path(directory, "cropped.pdf"), out)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=FIGURES, help="Which of the paper's figures to draw")
    parser.add_argument("--base", default="origin/main", help="Revision whose results.csv files go on the left")
    parser.add_argument("--base-label", default="main", help="Name of the base in the left panel's title")
    parser.add_argument("--no-base", action="store_true", help="Draw the branch alone, for a track the base lacks")
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
    parser.add_argument(
        "--sources", nargs="+", choices=list(SOURCES), help="Draw only these abstraction sources of a sat or opt figure"
    )
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, whose preamble the figure uses")
    parser.add_argument("--out", required=True, help="PNG file to write, named <PR>-<kind>-before-after.png")
    return parser


if __name__ == "__main__":
    main()
