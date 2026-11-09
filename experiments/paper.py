"""Write a PR's results into the paper's per-domain table, after checking its base reproduces them, and draw its figures.

main.tex includes each figure as a PDF from figures/, which this draws again from the branch's results.
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from experiments.compare import submitted_tracks
from experiments.figure import DEFAULT_PAPER, load_tracks, paper_figures, render_pdf, solved

# Where each track's columns start in tab:results, and the modes they count in order.
TABLE_COLUMNS = {
    "sat": (1, ("asp", "abs-asp", "lama", "abs-lama")),
    "opt": (6, ("asp", "abs-asp", "lmcut", "abs-lmcut")),
    "unsat": (11, ("ms", "abs-ms")),
}
TABLE_SECTIONS = {"symmetries": "Symmetric objects", "resources": "Resource levels"}


def main():
    args = _argument_parser().parse_args()
    paper = Path(args.paper)
    if args.manifests:
        _update_table(args, paper)
    for name, body in paper_figures(args.branch).items():
        render_pdf(paper, body, paper.parent / "figures" / f"{name}.pdf")
        print(f"Wrote figures/{name}.pdf")


def _update_table(args, paper):
    manifests = [json.loads(Path(path).read_text()) for path in args.manifests]
    base_manifests = [json.loads(Path(path).read_text()) for path in args.base_manifests]
    tex = paper.read_text()
    for track in submitted_tracks(manifests):
        kind, source = track.split("/")
        base = domain_counts(load_tracks(args.base, kind, base_manifests, [source])[source], kind)
        branch = domain_counts(load_tracks(args.branch, kind, manifests, [source])[source], kind)
        if _holds(tex, kind, source, branch):
            print(f"{track}: the paper already holds the branch's results")
            continue
        tex, changed = update_table(tex, kind, source, base, branch)
        print(f"{track}: {', '.join(changed) or 'no table row'} changed")
    paper.write_text(tex)


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


def _holds(tex, kind, source, branch):
    # Results that went in before the merge leave nothing to write, which is when the branch reproduces the table.
    try:
        update_table(tex, kind, source, branch, branch)
    except SystemExit:
        return False
    return True


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
    parser.add_argument(
        "--manifests", nargs="+", help="The branch's run manifests, which name the tracks whose table columns to update"
    )
    parser.add_argument(
        "--base-manifests", nargs="*", default=[], help="The base's run manifests, when it is a PR with its own runs"
    )
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, beside its figures/ folder")
    return parser


if __name__ == "__main__":
    main()
