"""Write the results at a revision into the paper: its per-domain table, and its figures as the PDFs main.tex includes."""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, SOURCES, load_tracks, paper_figures, render_pdf
from experiments.report import solved

# Each track's table, where its columns start in it, and the modes they count in order.
TABLE_COLUMNS = {
    "sat": ("tab:ipc", 1, ("asp", "abs-asp", "lama", "abs-lama")),
    "opt": ("tab:ipc", 6, ("asp", "abs-asp", "lmcut", "abs-lmcut")),
    "unsat": ("tab:unsat", 1, ("ms", "abs-ms")),
}


def main():
    args = _argument_parser().parse_args()
    paper = Path(args.paper)
    tex = paper.read_text()
    for kind in TABLE_COLUMNS:
        for source, problems in load_tracks(args.revision, kind, []).items():
            tex, changed = update_table(tex, kind, source, domain_counts(problems, kind))
            print(f"{kind}/{source}: {', '.join(changed) or 'no table row'} changed")
    paper.write_text(tex)
    for name, body in paper_figures(args.revision).items():
        render_pdf(paper, body, paper.parent / "figures" / f"{name}.pdf")
        print(f"Wrote figures/{name}.pdf")


def domain_counts(problems, kind):
    """Each domain's row of the table for one track, problems first, under the name the paper gives it."""
    modes = TABLE_COLUMNS[kind][2]
    rows = defaultdict(lambda: [0] * (len(modes) + 1))
    for problem in problems:
        row = rows[_short(next(iter(problem.values()))["domain"])]
        row[0] += 1
        for index, mode in enumerate(modes, 1):
            row[index] += solved(problem[mode])
    # A domain from a single IPC edition goes without its year, such as agricola.
    editions = Counter(_without_year(name) for name in rows)
    return {(_without_year(name) if editions[_without_year(name)] == 1 else name): row for name, row in rows.items()}


def update_table(tex, kind, source, counts):
    """Write one track's columns of one source's section, bolding the better mode of each pair."""
    label, first, modes = TABLE_COLUMNS[kind]
    table = tex.rindex(r"\begin{table", 0, tex.index(rf"\label{{{label}}}"))
    start = tex.index(rf"\emph{{IPC {SOURCES[source]}}}", table)
    # The section runs to the next section's heading or the end of the table.
    end = re.compile(r"\\emph\{|\\bottomrule").search(tex, start + 1).start()
    lines = tex[start:end].split("\n")
    width = len(modes) + 1
    changed = []
    for index, line in enumerate(lines):
        cells = line.rstrip().removesuffix("\\\\").split("&")
        if len(cells) < first + width or cells[first].strip() == "--":
            continue
        name = cells[0].strip()
        if name not in counts:
            raise SystemExit(f"No {kind} {source} results for the paper's row {name}")
        row = counts[name]
        written = [str(row[0]), *_bold_pairs(row[1:])]
        if written != [cell.strip() for cell in cells[first : first + width]]:
            changed.append(name)
        cells[first : first + width] = [f" {cell} " for cell in written]
        lines[index] = "&".join(cells).rstrip() + " \\\\"
    return tex[:start] + "\n".join(lines) + tex[end:], changed


def _bold_pairs(counts):
    cells = []
    for concrete, abstract in zip(counts[::2], counts[1::2]):
        cells.append(f"\\textbf{{{concrete}}}" if concrete > abstract else str(concrete))
        cells.append(f"\\textbf{{{abstract}}}" if abstract > concrete else str(abstract))
    return cells


def _short(domain):
    return re.sub(r"-(sat|opt)(\d\d)$", r"-\2", domain.removesuffix("-strips"))


def _without_year(name):
    return re.sub(r"-\d\d$", "", name)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="origin/main", help="Revision whose results go into the paper")
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, beside its figures/ folder")
    return parser


if __name__ == "__main__":
    main()
