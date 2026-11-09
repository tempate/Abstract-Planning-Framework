"""Write a PR's results into the paper's per-domain table and Figure 1, after checking its base reproduces them.

Figure 1 lives in figures/results.pdf beside main.tex, rendered from the TikZ source figures/results.tex,
which is where its coordinate sets get replaced.
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from experiments.compare import submitted_tracks
from experiments.figure import BASELINES, DEFAULT_PAPER, cactus, load_tracks, render_pdf, scatter, solved

# Where each track's columns start in tab:results, and the modes they count in order.
TABLE_COLUMNS = {
    "sat": (1, ("asp", "abs-asp", "lama", "abs-lama")),
    "opt": (6, ("asp", "abs-asp", "lmcut", "abs-lmcut")),
    "unsat": (11, ("ms", "abs-ms")),
}
TABLE_SECTIONS = {"symmetries": "Symmetric objects", "resources": "Resource levels"}
# A coordinate set in the figure, whose opt points may still carry a colour tag such as [2].
COORDINATES = re.compile(r"\{(\([\d.]+,[\d.]+\)(?: \[\d\])?(?: \([\d.]+,[\d.]+\)(?: \[\d\])?)*)\}")


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    paper = Path(args.paper)
    figures = paper.parent / "figures"
    if args.render_only:
        for source in sorted(figures.glob("*.tex")):
            render_pdf(paper, source.read_text(), source.with_suffix(".pdf"))
            print(f"Wrote {source.with_suffix('.pdf')}")
        return
    if not args.manifests:
        parser.error("--manifests is required unless --render-only")

    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]
    tex = paper.read_text()
    figure_source = figures / "results.tex"
    figure = figure_source.read_text()
    for track in submitted_tracks(manifests):
        kind, source = track.split("/")
        base = load_tracks(args.base, kind, base_manifests, [source])[source]
        branch = load_tracks(args.branch, kind, manifests, [source])[source]
        if _holds(figure, kind, branch):
            print(f"{track}: the paper already holds the branch's results")
            continue
        tex, changed = update_table(tex, kind, source, domain_counts(base, kind), domain_counts(branch, kind))
        figure, replaced = update_figure(figure, figure_sets(base, kind), figure_sets(branch, kind))
        print(f"{track}: {', '.join(changed) or 'no table row'} changed, {replaced} figure sets replaced")
    paper.write_text(tex)
    if figure != figure_source.read_text():
        figure_source.write_text(figure)
        render_pdf(paper, figure, figure_source.with_suffix(".pdf"))
        print(f"Wrote {figure_source.with_suffix('.pdf')}")


def domain_counts(problems, kind):
    """Each domain's row of the table for one track, problems first, under the name the paper gives it."""
    modes = TABLE_COLUMNS[kind][1]
    rows = defaultdict(lambda: [0] * (len(modes) + 1))
    for problem in problems:
        row = rows[_short(next(iter(problem.values()))["domain"])]
        row[0] += 1
        for index, mode in enumerate(modes, 1):
            row[index] += solved(problem[mode])
    # A domain from a single IPC edition goes without its year, such as agricola.
    editions = Counter(_without_year(name) for name in rows)
    return {(_without_year(name) if editions[_without_year(name)] == 1 else name): row for name, row in rows.items()}


def update_table(tex, kind, source, base, branch):
    """Replace one track's columns of one source's section, once every row matches the base."""
    start = tex.index(rf"\emph{{{TABLE_SECTIONS[source]}}}")
    # The section runs to the next section's heading or the end of the table.
    end = re.compile(r"\\emph\{|\\bottomrule").search(tex, start + 1).start()
    lines = tex[start:end].split("\n")
    first, modes = TABLE_COLUMNS[kind]
    width = len(modes) + 1
    totals = {
        name: [sum(row[i] for row in counts.values()) for i in range(width)]
        for name, counts in (("base", base), ("branch", branch))
    }
    changed = []
    for index, line in enumerate(lines):
        cells = line.rstrip().removesuffix("\\\\").split("&")
        if len(cells) < first + width:
            continue
        name = cells[0].strip()
        plain = [re.sub(r"\\textbf\{(\w+)\}", r"\1", cell.strip()) for cell in cells[first : first + width]]
        if plain[0] == "--":
            continue
        expected = totals["base"] if name == "Total" else base.get(name)
        if expected != [int(cell) for cell in plain]:
            raise SystemExit(
                f"The base does not reproduce the paper's {kind} {source} row {name}: {plain} against {expected}"
            )
        fresh = totals["branch"] if name == "Total" else branch[name]
        written = [str(fresh[0]), *_bold_pairs(fresh[1:], bold=name != "Total")]
        if written != [cell.strip() for cell in cells[first : first + width]]:
            changed.append(name)
        cells[first : first + width] = [f" {cell} " for cell in written]
        lines[index] = "&".join(cells).rstrip() + " \\\\"
    return tex[:start] + "\n".join(lines) + tex[end:], changed


def figure_sets(problems, kind):
    """The coordinate sets this track draws in Figure 1, its curves over time and its runtime plots."""
    if kind == "unsat":
        pairs = [("ms", "abs-ms")]
    else:
        pairs = [(BASELINES[kind][0], f"abs-{BASELINES[kind][0]}"), ("asp", "abs-asp")]
    curves = [cactus(problems, mode) for pair in pairs for mode in pair]
    return curves + [scatter(problems, solver, abstraction) for solver, abstraction in pairs]


def update_figure(figure, base_sets, branch_sets):
    """Replace each of the base's coordinate sets in Figure 1's source with the branch's, ignoring old colour tags."""
    replaced = 0
    for old, new in zip(base_sets, branch_sets):
        matches = [match for match in COORDINATES.finditer(figure) if re.sub(r" \[\d\]", "", match.group(1)) == old]
        if len(matches) != 1:
            raise SystemExit(f"The base's coordinate set appears {len(matches)} times in Figure 1, not once")
        if old != new:
            figure = figure[: matches[0].start()] + "{" + new + "}" + figure[matches[0].end() :]
            replaced += 1
    return figure, replaced


def _holds(figure, kind, branch):
    # Results that went in before the merge leave nothing to write.
    stored = {re.sub(r" \[\d\]", "", match.group(1)) for match in COORDINATES.finditer(figure)}
    return all(points in stored for points in figure_sets(branch, kind))


def _bold_pairs(counts, bold):
    cells = []
    for concrete, abstract in zip(counts[::2], counts[1::2]):
        cells.append(f"\\textbf{{{concrete}}}" if bold and concrete > abstract else str(concrete))
        cells.append(f"\\textbf{{{abstract}}}" if bold and abstract > concrete else str(abstract))
    return cells


def _short(domain):
    return re.sub(r"-(sat|opt)(\d\d)$", r"-\2", domain.removesuffix("-strips"))


def _without_year(name):
    return re.sub(r"-\d\d$", "", name)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main~1", help="Revision whose results the paper holds now")
    parser.add_argument("--branch", default="origin/main", help="Revision whose results go into the paper")
    parser.add_argument("--manifests", nargs="+", help="The branch's run manifests, which name its tracks")
    parser.add_argument(
        "--base-manifests", nargs="*", default=[], help="The base's run manifests, when it is a PR with its own runs"
    )
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, beside its figures/ folder")
    parser.add_argument(
        "--render-only", action="store_true", help="Render every figures/*.tex to its PDF, after editing one by hand"
    )
    return parser


if __name__ == "__main__":
    main()
