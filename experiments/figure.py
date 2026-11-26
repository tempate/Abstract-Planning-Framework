"""Draw the paper's figure for one track kind, a PR's base on the left and its branch on the right, as a PNG."""

import argparse
import csv
import io
import json
import math
import re
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path

from experiments.collect import result_key
from experiments.report import finished_problems, solved
from experiments.run import ABSTRACTION_PREFIX, PROJECT_ROOT
from experiments.tracks import TRACKS

SOURCES = {"symmetries": "Symmetries", "resources": "Resources"}
FIGURES = ("sat", "opt", "htg")
# The figure draws a problem a mode leaves unsolved on this border, past the 1800 s limit.
UNSOLVED = 6000.0
TIME_LIMIT = 1800
TRACK_NAMES = {"sat": "Satisficing", "opt": "Optimal"}
# Each track's solvers with their labels, each drawn against its abstraction, the first with solid lines.
PAIRS = {
    "sat": (("lama", r"\LAMA", r"\LAMAa"), ("asp", r"\ASP", r"\ASPa")),
    "opt": (("lmcut", r"\LMcut", r"\LMcuta"), ("asp", r"\ASP", r"\ASPa")),
}
# The columns of the paper's runtime figures in the order of the tables, each a planner's x label and, on each track,
# the planner and the abstraction drawn against it. The tracks share each column's label, so Fast Downward's planners
# read FD and FD+ as in the tables, and the planners without an abstraction of their own face FD's.
PAPER_COLUMNS = (
    (r"\ASP", {"sat": ("asp", "abs-asp"), "opt": ("asp", "abs-asp")}),
    (r"\HM", {"sat": ("rnd-g", "abs-lama"), "opt": ("rnd-g", "abs-lmcut")}),
    (r"\textsc{FD}", {"sat": ("lama", "abs-lama"), "opt": ("lmcut", "abs-lmcut")}),
    (
        r"\textsc{FD}$^+$",
        {"sat": ("lama-symmetry-pruning", "abs-lama"), "opt": ("lmcut-symmetry-pruning", "abs-lmcut")},
    ),
    (r"\textsc{Powerlifted}", {"sat": ("powerlifted", "abs-powerlifted"), "opt": ("powerlifted", "abs-powerlifted")}),
)
# Powerlifted, which only the hard-to-ground tracks run, against its abstraction.
POWERLIFTED = ("powerlifted", r"\textsc{Powerlifted}", r"\textsc{Powerlifted}\textsuperscript{$\alpha$}")
# The color and mark of each solver's points in a runtime plot, in the order of its track's pairs.
SOLVER_MARKS = (("conc", "*"), ("abst", "triangle*"), ("ext0", "diamond*"))
# Orange means abstract in the other figures, so Powerlifted takes another color.
POWERLIFTED_MARKS = SOLVER_MARKS[2:]
# Lifts a cactus plot's source title over the legend that sits just above the plot.
ABOVE_LEGEND = "title style={yshift=11pt}"
# A plot that carries its own legend, centred above it in rows of two.
CENTRED_LEGEND = "legend columns=2, legend style={overlay, at={(0.5,1.04)}, anchor=south}"
# The HTG figure's plots are drawn at the size they print, as main.tex includes it unscaled, five to the text width.
HTG_PLOT_SIZE = 1.1
# The IPC figures' plots, drawn at the size they print, as main.tex includes them unscaled.
IPC_PLOT_SIZE = 1.05
# The gap between the plots colored by domain, which share the first plot's y axis, in inches.
DOMAIN_PLOT_GAP = 0.2
# The extra space between their rows, whose upper one has no x axis to make room for, in inches.
DOMAIN_ROW_GAP = 0.0
# The IPC figures' legends, in this many lines under the plots.
IPC_LEGEND_LINES = 2
# The HTG figure's ten domains in two rows under its plots.
HTG_LEGEND_COLUMNS = 5
# Each HTG domain's color, the xcolor names in the figures of Horcik et al. (AAAI 2022), which read better than lighter
# palettes at the size of a cross. A domain both papers show keeps its color there, and tpp takes a tenth color.
DOMAIN_COLORS = {
    "agricola": "black",
    "blocksworld": "blue",
    "childsnack": "purple",
    "depots": "olive",
    "logistics": "brown",
    "organic-synthesis": "cyan",
    "pipesworld-tankage": "orange",
    "rovers": "teal",
    "satellite": "violet",
    "tpp": "green!60!black",
}
# IPC domains that are one domain under several names, each by the name the IPC figures give it.
IPC_FAMILIES = {
    "logistics00": "logistics",
    "logistics98": "logistics",
    "mprime": "mystery",
    "pipesworld-notankage": "pipesworld",
    "pipesworld-tankage": "pipesworld",
}
# The Symmetries figure colors the seven IPC domains with the most problems, each with at least 58 to the others'
# 40 or fewer, a domain the HTG figure shows in its color there, and draws the rest in grey.
OTHER_DOMAINS = "other"
SYMMETRIES_DOMAIN_COLORS = {
    "barman": "cyan",
    "logistics": "brown",
    "mystery": "red",
    "openstacks": "blue",
    "pipesworld": "orange",
    "satellite": "violet",
    "tpp": "green!60!black",
    OTHER_DOMAINS: "black!35",
}
# Resources has ten domains, so its figure colors them all, a domain the Symmetries figure colors in the same color.
RESOURCES_DOMAIN_COLORS = {
    "data-network": "olive",
    "elevators": "black",
    "freecell": "teal",
    "mystery": "red",
    "nomystery": "orange",
    "openstacks": "blue",
    "thoughtful": "brown",
    "tpp": "green!60!black",
    "transport": "cyan",
    "visitall": "magenta",
}
IPC_DOMAIN_COLORS = {"symmetries": SYMMETRIES_DOMAIN_COLORS, "resources": RESOURCES_DOMAIN_COLORS}
# HTG names a domain by the collection it comes from; the paper by the domain.
HTG_DOMAINS = {
    "blocksworld-large-simple": "blocksworld",
    "childsnack-contents": "childsnack",
    "logistics-large-simple": "logistics",
    "organic-synthesis-alkene": "organic-synthesis",
    "organic-synthesis-MIT": "organic-synthesis",
    "organic-synthesis-original": "organic-synthesis",
    "pipesworld-tankage-nosplit": "pipesworld-tankage",
    "rovers-large-simple": "rovers",
}
HTG_COLLECTION = "gnad-et-al-aaai19-large-instances"
DEFAULT_PAPER = PROJECT_ROOT.parent / "paper" / "planpilot_abstractions" / "icaps27" / "main.tex"


def main():
    parser = _argument_parser()
    args = parser.parse_args()

    if args.sources and args.kind not in ("sat", "opt"):
        parser.error("--sources applies to the sat and opt figures only")

    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]

    if args.no_base:
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
    """Keep only the abstract rows this track's manifests submitted, for the modes they submitted."""
    submitted = set()
    for manifest in manifests:
        # A manifest speaks for its own track only, which may have run other classes.
        if manifest["track"] != f"{kind}/{source}":
            continue
        for entry in manifest["expected_results"]:
            if entry["mode"].startswith(ABSTRACTION_PREFIX):
                submitted.add(result_key(entry))
    filtered_modes = {mode for _domain, _problem, mode, _class in submitted}

    selected = []
    for row in rows:
        if row["mode"] not in filtered_modes or result_key(row) in submitted:
            selected.append(row)
    return selected


def load_tracks(revision, kind, manifests, sources=None):
    """Each abstraction source's finished problems at a revision, as the report pairs them."""
    if kind == "htg":
        return {track: load_tracks(revision, f"{track}-htg", manifests)["symmetries"] for track in ("sat", "opt")}

    tracks = {}
    for source in sources or _sources(kind):
        rows = csv.DictReader(io.StringIO(_results_at(revision, kind, source)))
        tracks[source] = finished_problems(select(rows, kind, source, manifests))[1]
    return tracks


def _sources(kind):
    """What the tracks of a kind abstract, such as symmetries and resources for sat."""
    sources = []
    for track in TRACKS.values():
        if track.kind == kind:
            sources.append(track.source)
    return sources


def _results_at(revision, kind, source):
    results_file = TRACKS[f"{kind}/{source}"].results_file.relative_to(PROJECT_ROOT)

    shown = subprocess.run(
        ["git", "-C", PROJECT_ROOT, "show", f"{revision}:{results_file}"], capture_output=True, text=True
    )

    if shown.returncode != 0:
        raise SystemExit(f"No {kind}/{source} results.csv at {revision}")
    return shown.stdout


def paper_figures(revision):
    """The paper's figures at a revision, by the file name main.tex includes, each the body of a PDF."""
    return {
        "runtimes-htg": _minipage(
            r"\textwidth", f"\\setlength{{\\plotsize}}{{{HTG_PLOT_SIZE}in}}\n" + _htg_runtime_figure(revision)
        ),
        **{
            f"runtimes-ipc-{source}": _minipage(
                r"\textwidth",
                f"\\setlength{{\\plotsize}}{{{IPC_PLOT_SIZE}in}}\n"
                + _ipc_runtime_figure(problems, IPC_DOMAIN_COLORS[source]),
            )
            for source, problems in _ipc_sources(revision).items()
        },
    }


def _htg_runtime_figure(revision):
    """The paper's HTG runtime figure, a row per track, a plot per planner, and a domain legend."""
    htg = load_tracks(revision, "htg", [])
    domains = sorted({_htg_problem_domain(problem) for problems in htg.values() for problem in problems})

    plot_table = _plot_rows(htg, _htg_problem_domain, DOMAIN_COLORS)

    # The domains in rows under the plots.
    entries = [_legend_entry(DOMAIN_COLORS[domain], domain) for domain in domains]
    return _with_legend_below(plot_table, entries, HTG_LEGEND_COLUMNS)


def _ipc_sources(revision):
    """Each IPC abstraction source's finished problems, by track."""
    tracks = {kind: load_tracks(revision, kind, []) for kind in TRACK_NAMES}
    return {source: {kind: tracks[kind][source] for kind in TRACK_NAMES} for source in SOURCES}


def _ipc_runtime_figure(tracks, colors):
    """One IPC source's runtime figure, a row per track, a plot per planner, and a domain legend."""

    def domain_of(problem):
        return _ipc_problem_domain(problem, colors)

    plot_table = _plot_rows(tracks, domain_of, colors)

    # The domains this source has under the plots, the grey of the other domains last.
    present = {domain_of(problem) for problems in tracks.values() for problem in problems}
    entries = [_legend_entry(color, domain) for domain, color in colors.items() if domain in present]
    return _with_legend_below(plot_table, entries, math.ceil(len(entries) / IPC_LEGEND_LINES))


def _plot_rows(tracks, domain_of, colors):
    """A row of runtime plots per track, sharing their axes: a column per planner every track ran.

    Only the first plot of a row numbers its y axis and only the bottom row its
    x axes, so a planner one track lacks has no column at all. The last plot of
    a row names its track on the right.
    """
    columns = [
        (label, modes)
        for label, modes in PAPER_COLUMNS
        if all(tracks[kind] and modes[kind][0] in tracks[kind][0] for kind in TRACK_NAMES)
    ]
    lines = []
    for row, (kind, name) in enumerate(TRACK_NAMES.items()):
        plots = [
            _domain_runtime_plot(
                tracks[kind],
                *modes[kind],
                label,
                domain_of,
                colors,
                left=index == 0,
                bottom=row == len(TRACK_NAMES) - 1,
                track=name if index == len(columns) - 1 else None,
            )
            for index, (label, modes) in enumerate(columns)
        ]
        # Room on the left for the y label, so the plots stay centred.
        lines.append("\\hspace*{0.42in}" + _joined(plots, f"{DOMAIN_PLOT_GAP}in"))
    return "\\begin{tabular}[c]{@{}c@{}}\n" + f" \\\\[{DOMAIN_ROW_GAP}in]\n".join(lines) + "\n\\end{tabular}"


def _with_legend_below(plot_table, entries, columns):
    """The plots centred, then the legend entries in rows of so many columns under them."""
    lines = [" & ".join(entries[start : start + columns]) for start in range(0, len(entries), columns)]
    legend = rf"{{\small\begin{{tabular}}{{@{{}}{'l' * columns}@{{}}}}" + " \\\\\n".join(lines) + r"\end{tabular}}"
    return "\\noindent\\makebox[\\linewidth][c]{%\n" + plot_table + "}" + "\n\n\\vspace{0.8em}\n" + _in_row(legend)


def _legend_entry(color, domain):
    return rf"\mbox{{\tikz[baseline=-0.5ex, color={color}]\pgfuseplotmark{{x}};~{domain}}}"


def _domain_runtime_plot(problems, solver, abstraction, label, domain_of, colors, left, bottom, track):
    """One planner's runtime per problem against an abstraction's, a cross per problem in its domain's color. A plot
    on the left labels the y axis, one at the bottom the x axis, and one given a track names it on its right."""
    by_domain = defaultdict(list)
    for problem in problems:
        by_domain[domain_of(problem)].append(problem)

    lines = []
    for domain, group in sorted(by_domain.items()):
        points = scatter(group, solver, abstraction)
        # A domain neither mode solves anything in has no point to draw.
        if points:
            style = f"only marks, mark=x, mark size=1.4pt, color={colors[domain]}"
            lines.append(rf"\addplot[{style}] coordinates {{{points}}};")

    # The paper's footnote size for the numbers and a size above it for the labels.
    options = r"label style={font=\small}, tick label style={font=\footnotesize}"
    # A light line at every power of ten, as in Horcik et al. (2022).
    options += r", grid=major, grid style={black!30, thin}"
    options += r", ylabel={X\textsuperscript{$\alpha$} time (s)}" if left else ", yticklabels={}"
    options += rf", xlabel={{{label}{{}} time (s)}}" if bottom else ", xticklabels={}"
    if track is not None:
        options += (
            r", after end axis/.append code={\node[rotate=-90, anchor=south, inner sep=4pt, font=\small] "
            rf"at (rel axis cs:1,0.5) {{{track}}};}}"
        )
    return (
        "\\begin{tikzpicture}[trim axis left, trim axis right]\n"
        + rf"\begin{{loglogaxis}}[bordered, {options}]"
        + "\n\\addplot[forget plot, black!40, no marks, domain=1:9000, samples=2] {x};\n"
        + "\n".join(lines)
        + "\n\\end{loglogaxis}\n\\end{tikzpicture}"
    )


def _htg_problem_domain(problem):
    return htg_domain(next(iter(problem.values()))["domain"])


def _ipc_problem_domain(problem, colors):
    """The domain the IPC figures color a problem by, its name without track or year, or the other domains."""
    name = re.sub(r"-(sat|opt)\d\d-strips$", "", next(iter(problem.values()))["domain"])
    name = IPC_FAMILIES.get(name, name)
    return name if name in colors else OTHER_DOMAINS


def _panel(title, kind, tracks):
    """One track's half of a PR's figure, under a title."""
    if kind == "htg":
        return _titled(title, _htg_figure(tracks), 2)

    body = (
        _in_row(_track_title(TRACK_NAMES[kind], len(tracks)))
        + "\n\n\\vspace{0.4em}\n"
        + _in_row(_joined(_cactus_plots(tracks, PAIRS[kind])))
        + "\n\n\\vspace{1.6em}\n"
        + _in_row(_joined(_runtime_plots(tracks, PAIRS[kind])))
    )

    return _titled(title, body, len(tracks))


def _htg_figure(tracks):
    """Both hard-to-ground tracks' runtime per problem, Powerlifted's or else the baseline's against its abstraction."""
    plots = []
    for track, problems in tracks.items():
        pairs, marks = (PAIRS[track][0],), SOLVER_MARKS
        if problems and POWERLIFTED[0] in problems[0]:
            pairs, marks = (POWERLIFTED,), POWERLIFTED_MARKS
        plots.append(_runtime_plot(problems, pairs, labelled=True, legend=True, title=TRACK_NAMES[track], marks=marks))

    # Both plots label their own y axis, so they need more room between them than the paper's rows.
    return _in_row(_joined(plots, "0.75in"))


def _cactus_plots(tracks, pairs):
    """One track's problems solved over time, a plot per abstraction source, the right one carrying the legend."""
    plots = []
    for index, (source, problems) in enumerate(tracks.items()):
        if len(tracks) == 1:
            options, legend = f"ylabel={{Problems solved}}, {CENTRED_LEGEND}", True
        elif index == 0:
            options, legend = "ylabel={Problems solved}", False
        else:
            options, legend = "ylabel={}, legend style={overlay, at={(-0.16,1.04)}, anchor=south}", True
        plots.append(_cactus_plot(SOURCES[source], problems, pairs, options, legend))

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


def _runtime_plots(tracks, pairs):
    """One track's runtime per problem, a plot per abstraction source with every solver in it."""
    # The cactus plots above name the sources, so only the left plot labels its y axis, and only the right
    # one names the solvers, as the cactus plots do.
    last = len(tracks) - 1
    return [
        _runtime_plot(problems, pairs, labelled=index == 0, legend=index == last)
        for index, problems in enumerate(tracks.values())
    ]


def _runtime_plot(problems, pairs, labelled, legend, title="", marks=SOLVER_MARKS):
    """Each solver's runtime per problem against its abstraction's, in the solver's own color and mark."""
    options = r"ylabel={X\textsuperscript{$\alpha$} time (s)}" if labelled else "yticklabels={}"
    if title:
        # Lifted over the legend of its row, so every title of the row sits at the same height.
        options += rf", title={{\small {title}}}, {ABOVE_LEGEND}"
    if legend:
        options += (
            ", legend style={font=\\scriptsize, draw=none, fill=none, /tikz/every even column/.append style={column sep=4pt}}, "
            + CENTRED_LEGEND
            # Every solver in one row, which a third solver would otherwise wrap into the title.
            + f", legend columns={len(pairs)}"
        )

    lines = []
    for (solver, label, _abstract_label), (color, mark) in zip(pairs, marks):
        style = rf"only marks, mark={mark}, mark size=1.2pt, color={color}, fill opacity=0.45, draw opacity=0.6"
        # A solver that ran on another benchmark set only, such as Powerlifted on HTG, still names its mark here.
        if problems and solver not in problems[0]:
            if legend:
                lines += [rf"\addlegendimage{{{style}}}", rf"\addlegendentry{{{label}}}"]
            continue

        points = scatter(problems, solver, f"abs-{solver}")
        lines.append(rf"\addplot[{style}] coordinates {{{points}}};")
        if legend:
            lines.append(rf"\addlegendentry{{{label}}}")

    return (
        "\\begin{tikzpicture}[trim axis left, trim axis right]\n"
        + rf"\begin{{loglogaxis}}[bordered, xlabel={{X time (s)}}, {options}]"
        + "\n\\addplot[forget plot, black!40, no marks, domain=1:9000, samples=2] {x};\n"
        + "\n".join(lines)
        + "\n\\end{loglogaxis}\n\\end{tikzpicture}"
    )


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


def htg_domain(domain):
    """The domain the paper names an HTG problem by, such as organic-synthesis for organic-synthesis-MIT."""
    collection, _, subdirectory = domain.partition("/")
    if collection == HTG_COLLECTION:
        return subdirectory.removesuffix("-large")
    return HTG_DOMAINS[collection]


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
