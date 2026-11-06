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

from experiments.report import _finished_problems
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
}
# The scaled figure draws the coverage of the unsat track's grown problems, for the branch alone.
TRACKS = {"scaled": "unsat"}
FIGURES = ("sat", "opt", "unsat", "htg", "scaled")
# The figure draws a problem a mode leaves unsolved on this border, past the 1800 s limit.
UNSOLVED = 6000.0
TIME_LIMIT = 1800
TRACK_NAMES = {"sat": "Satisficing", "opt": "Optimal", "unsat": "Unsolvability"}
# Lifts a cactus plot's source title over the legend that sits just above the plot.
ABOVE_LEGEND = "title style={yshift=11pt}"
BASELINES = {"sat": ("lama", r"\LAMA", r"\LAMAa"), "opt": ("lmcut", r"\LMcut", r"\LMcuta")}
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
        _render(args.paper, [_scaled_panel(load_tracks(args.branch, args.kind, manifests)["scaled"])], Path(args.out))
        print(f"Wrote {args.out}")
        return
    panel = {"unsat": _unsat_panel, "htg": _htg_panel}.get(args.kind, _panel)
    # A label like #134 would otherwise read as a macro parameter in LaTeX.
    base_label = args.base_label.replace("#", r"\#")
    if args.no_base:
        panels = [panel("", args.kind, load_tracks(args.branch, args.kind, manifests, args.sources))]
    else:
        panels = [
            panel(f"Before ({base_label})", args.kind, load_tracks(args.base, args.kind, base_manifests, args.sources)),
            panel("After", args.kind, load_tracks(args.branch, args.kind, manifests, args.sources)),
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
    track = TRACKS.get(kind, kind)
    if kind == "scaled":
        sources = ("scaled",)
    elif not sources:
        sources = KIND_SOURCES[kind]
    tracks = {}
    for source in sources:
        text = _results_at(revision, track, source)
        rows = select(list(csv.DictReader(io.StringIO(text))), track, source, manifests)
        with tempfile.NamedTemporaryFile("w", suffix=".csv", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
            stream.flush()
            tracks[source] = _finished_problems(stream.name)[1]
    return tracks


def _results_at(revision, kind, source):
    if kind.endswith("-htg"):
        directories = (f"experiments/htg/{kind.removesuffix('-htg')}",)
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


def _panel(title, kind, tracks):
    """One track's half of the paper's results figure, under a title."""
    baseline, label, abstract_label = BASELINES[kind]
    curves = (
        (baseline, "conc, solid", label),
        (f"abs-{baseline}", "abst, solid", abstract_label),
        ("asp", "conc, dashed", r"\ASP"),
        ("abs-asp", "abst, dashed", r"\ASPa"),
    )
    cactus_plots = []
    last = list(tracks)[-1]
    for source, problems in tracks.items():
        lines = []
        for mode, style, name in curves:
            lines.append(rf"\addplot[{style}, thick, const plot, mark=none] coordinates {{{cactus(problems, mode)}}};")
            # One legend above the plots, carried by the right one.
            if source == last:
                lines.append(rf"\addlegendentry{{{name}}}")
        options = f"{ABOVE_LEGEND}, ylabel={{Problems solved}}"
        if len(tracks) == 1:
            # Alone, the plot is too narrow for one row, so the baselines sit above ASP.
            options += ", legend columns=2, legend style={overlay, at={(0.5,1.04)}, anchor=south}"
        elif source == last:
            options = f"{ABOVE_LEGEND}, ylabel={{}}, legend style={{overlay, at={{(-0.16,1.04)}}, anchor=south}}"
        cactus_plots.append(_cactus_plot(SOURCES[source], options, lines))

    runtime_rows = []
    for solver, solver_label, abstraction_label in ((baseline, label, abstract_label), ("asp", r"\ASP", r"\ASPa")):
        plots = []
        for index, (source, problems) in enumerate(tracks.items()):
            # The cactus plots above name the sources, and only the left plot labels its y axis.
            option = rf"ylabel={{{abstraction_label}{{}} time (s)}}" if index == 0 else "yticklabels={}"
            points = scatter(problems, solver, f"abs-{solver}")
            plots.append(rf"\runtimeplot[{option}]{{{solver_label}}}{{{points}}}")
        runtime_rows.append(_row(plots))

    return _titled(
        title,
        _track_header(TRACK_NAMES[kind], len(tracks))
        + _row(cactus_plots)
        + "\n\n\\medskip\n"
        + "\n\n\\smallskip\n".join(runtime_rows),
        len(tracks),
    )


def _unsat_panel(title, _kind, tracks):
    problems = tracks["symmetries"]
    lines = [
        rf"\addplot[conc, solid, thick, const plot, mark=none] coordinates {{{cactus(problems, 'ms')}}};",
        r"\addlegendentry{\MS}",
        rf"\addplot[abst, solid, thick, const plot, mark=none] coordinates {{{cactus(problems, 'abs-ms')}}};",
        r"\addlegendentry{\MSa}",
    ]
    options = f"{ABOVE_LEGEND}, ylabel={{Problems proved}}, legend style={{overlay, at={{(0.5,1.04)}}, anchor=south}}"
    runtime = rf"\runtimeplot[ylabel={{\MSa{{}} time (s)}}]{{\MS}}{{{scatter(problems, 'ms', 'abs-ms')}}}"
    return _titled(
        title,
        _track_header(TRACK_NAMES["unsat"], 1)
        + _row([_cactus_plot(SOURCES["symmetries"], options, lines)])
        + "\n\n\\medskip\n"
        + _row([runtime]),
        1,
    )


def _cactus_plot(source_title, options, lines):
    return (
        "\\begin{tikzpicture}[trim axis left, trim axis right]\n"
        + rf"\begin{{semilogxaxis}}[cactusplot, title={{\small {source_title}}}, {options}]"
        + "\n"
        + "\n".join(lines)
        + "\n\\end{semilogxaxis}\n\\end{tikzpicture}"
    )


# Both htg plots label their own y axis, so they need more room between them than the paper's rows.
HTG_GAP = "0.75in"


def _htg_panel(title, _kind, tracks):
    cactus_plots, runtimes = [], []
    for track in ("sat", "opt"):
        name = TRACK_NAMES[track]
        baseline, label, abstract_label = BASELINES[track]
        problems = tracks[track]
        lines = [
            rf"\addplot[conc, solid, thick, const plot, mark=none] coordinates {{{cactus(problems, baseline)}}};",
            rf"\addlegendentry{{{label}}}",
            rf"\addplot[abst, solid, thick, const plot, mark=none] coordinates {{{cactus(problems, 'abs-' + baseline)}}};",
            rf"\addlegendentry{{{abstract_label}}}",
        ]
        # Each track has its own baseline, so each plot carries its own legend.
        options = "ylabel={Problems solved}, legend columns=1, legend style={at={(0.03,0.97)}, anchor=north west}"
        cactus_plots.append(_cactus_plot(name, options, lines))
        points = scatter(problems, baseline, f"abs-{baseline}")
        runtimes.append(rf"\runtimeplot[ylabel={{{abstract_label}{{}} time (s)}}]{{{label}}}{{{points}}}")
    return _titled(title, _row(cactus_plots, HTG_GAP) + "\n\n\\medskip\n" + _row(runtimes, HTG_GAP), 2)


def _track_header(name, columns):
    # The track's name over its plots and the gaps between them, ruled like a table's cmidrule.
    width = f"\\dimexpr{columns}\\plotsize+{0.3 * (columns - 1):.1f}in\\relax"
    return (
        "\\noindent\\makebox[\\linewidth][c]{%\n\\hspace*{0.42in}%\n"
        + rf"\parbox[b]{{{width}}}{{\centering\small {name}\\[-2pt]\rule{{\linewidth}}{{0.4pt}}}}}}"
        + "\n\n\\vspace{0.4em}\n"
    )


def _row(plots, gap="0.3in"):
    # The paper's spacing: room for the y label on the left, then a gap between the plots.
    return "\\noindent\\makebox[\\linewidth][c]{%\n\\hspace*{0.42in}%\n" + f"%\n\\hspace{{{gap}}}%\n".join(plots) + "}"


def _titled(title, body, columns):
    # A single column of plots gets a narrow panel, so the two halves sit close together.
    width = "\\columnwidth" if columns > 1 else "2in"
    return (
        f"\\begin{{minipage}}[t]{{{width}}}\n\\centering\n"
        + f"{{\\large\\bfseries\\strut {title}}}\\par\\vspace{{2.4em}}\n"
        + body
        + "\n\\end{minipage}"
    )


SCALED_MODES = (("ms", "conc", "*", r"\MS"), ("abs-ms", "abst", "square*", r"\MSa"))


def scaled_coverage(problems, mode):
    """The share of each class size's problems a mode proves unsolvable, in percent."""
    by_size = defaultdict(list)
    for problem in problems:
        by_size[int(problem[mode]["domain"].rsplit("/size-", 1)[1])].append(solved(problem[mode]))
    return [(size, 100 * sum(proved) / len(proved)) for size, proved in sorted(by_size.items())]


def _scaled_panel(problems):
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
    preamble = Path(paper).read_text().split(r"\title{")[0]
    document = (
        preamble
        + "\\pagestyle{empty}\n\\begin{document}\n\\noindent\\mbox{"
        + r"\hspace{2em}".join(panels)
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
