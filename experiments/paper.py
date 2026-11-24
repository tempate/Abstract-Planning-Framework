"""Write the results at a revision into the paper: its summary and per-domain tables, and its figures as the PDFs main.tex includes."""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, SOURCES, TRACK_NAMES, load_tracks, paper_figures, render_pdf
from experiments.report import solved

# The modes each track counts, in the order of its columns. A set without a mode's results shows -- in its columns.
MODES = {
    "sat": ("asp", "abs-asp", "lama", "abs-lama", "powerlifted", "abs-powerlifted"),
    "opt": ("asp", "abs-asp", "lmcut", "abs-lmcut", "powerlifted", "abs-powerlifted"),
}
# Where each track's columns start in a row of the per-domain table.
DOMAIN_TABLE_COLUMN = {"sat": 1, "opt": 8}
# The summary table's groups of rows, each with where its first mode sits in a track's totals,
# which alternate each planner with its abstraction.
SUMMARY_GROUPS = {"Baselines": 1, "Our pipeline": 2}
# The planner each row of a summary group names, in the order of the track's modes.
SUMMARY_LABELS = (r"\ASP", r"\textsc{FD}", r"\PL")
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


def main():
    args = _argument_parser().parse_args()
    paper = Path(args.paper)
    tex = paper.read_text()

    totals = {}
    for section, tracks in benchmark_sets(args.revision).items():
        for kind, problems in tracks.items():
            counts = domain_counts(problems, kind, htg=section.startswith("HTG"))
            tex, changed = update_table(tex, section, kind, counts)
            totals[section, kind] = [None if None in column else sum(column) for column in zip(*counts.values())]
            print(f"{section}, {TRACK_NAMES[kind]}: {', '.join(changed) or 'no domain row'} changed")
    paper.write_text(update_summary(tex, list(totals.values())))

    for name, body in paper_figures(args.revision).items():
        render_pdf(paper, body, paper.parent / "figures" / f"{name}.pdf")
        print(f"Wrote figures/{name}.pdf")


def benchmark_sets(revision):
    """Each section of the tables, by its title, with the finished problems of its tracks."""
    sets = {"HTG Symmetries": load_tracks(revision, "htg", [])}
    for source, name in SOURCES.items():
        sets[f"IPC {name}"] = {kind: load_tracks(revision, kind, [])[source] for kind in MODES}
    return sets


def domain_counts(problems, kind, htg=False):
    """Each domain's row of the table for one track, problems first, under the name the paper gives it."""
    modes = MODES[kind]
    # A mode the results lack counts None, which the table shows as --.
    ran = set(problems[0]) if problems else set()
    rows = defaultdict(lambda: [0] + [0 if mode in ran else None for mode in modes])

    for problem in problems:
        domain = next(iter(problem.values()))["domain"]
        row = rows[_htg_name(domain) if htg else _short(domain)]
        row[0] += 1
        for index, mode in enumerate(modes, 1):
            if mode in ran:
                row[index] += solved(problem[mode])

    if htg:
        return dict(rows)

    # A domain from a single IPC edition goes without its year, such as agricola.
    editions = Counter(_without_year(name) for name in rows)
    counts = {}
    for name, row in rows.items():
        short = _without_year(name)
        counts[short if editions[short] == 1 else name] = row

    return counts


def update_table(tex, section, kind, counts):
    """Write one track's columns of one section of the per-domain table, bolding the better mode of each pair."""
    first = DOMAIN_TABLE_COLUMN[kind]
    start, end = _section(tex, "tab:ipc", section)
    lines = tex[start:end].split("\n")

    width = len(MODES[kind]) + 1
    changed = []
    written = set()
    for index, line in enumerate(lines):
        cells = line.rstrip().removesuffix("\\\\").split("&")
        if len(cells) < first + width or cells[first].strip() == "--":
            continue

        name = cells[0].strip()
        if name not in counts:
            raise SystemExit(f"No {section} {kind} results for the paper's row {name}")

        row = _cells(counts[name])
        if row != [cell.strip() for cell in cells[first : first + width]]:
            changed.append(name)

        cells[first : first + width] = [f" {cell} " for cell in row]
        lines[index] = "&".join(cells).rstrip() + " \\\\"
        written.add(name)

    missing = sorted(set(counts) - written)
    if missing:
        raise SystemExit(f"The paper's {section} section has no {kind} row for {', '.join(missing)}")

    return tex[:start] + "\n".join(lines) + tex[end:], changed


def update_summary(tex, columns):
    """Write the summary table, a column per benchmark set and track, the most solved of each column in bold."""
    rows = {(None, "Problems"): [str(column[0]) for column in columns]}
    for group, first in SUMMARY_GROUPS.items():
        for pair, label in enumerate(SUMMARY_LABELS):
            rows[group, label] = [_summary_cell(column, first + 2 * pair) for column in columns]

    start = tex.rindex(r"\begin{table", 0, tex.index(r"\label{tab:summary}"))
    end = tex.index(r"\end{tabular}", start)
    lines = tex[start:end].split("\n")

    # The problem counts come before the first group.
    group = None
    for index, line in enumerate(lines):
        for name in SUMMARY_GROUPS:
            if rf"\emph{{{name}}}" in line:
                group = name

        label = line.split("&")[0].strip()
        if (group, label) in rows:
            lines[index] = " & ".join([label, *rows.pop((group, label))]) + " \\\\"

    if rows:
        missing = ", ".join(f"{group or 'top'}: {label}" for group, label in rows)
        raise SystemExit(f"The summary table has no row for {missing}")

    return tex[:start] + "\n".join(lines) + tex[end:]


def _summary_cell(column, index):
    solved = column[index]
    if solved is None:
        return "--"

    best = max(count for count in column[1:] if count is not None)
    return f"\\textbf{{{solved}}}" if solved == best else str(solved)


def _section(tex, label, section):
    """Where one section of a table starts, at its title, and ends, at the next title or the end of the table."""
    table = tex.rindex(r"\begin{table", 0, tex.index(rf"\label{{{label}}}"))
    start = tex.index(rf"\emph{{{section}}}", table)
    end = re.compile(r"\\emph\{|\\bottomrule").search(tex, start + 1).start()
    return start, end


def _cells(row):
    """The problem count, then each mode's count, the better of each concrete and abstract pair in bold."""
    cells = [str(row[0])]
    for concrete, abstract in zip(row[1::2], row[2::2]):
        if concrete is None:
            cells += ["--", "--"]
            continue
        cells.append(f"\\textbf{{{concrete}}}" if concrete > abstract else str(concrete))
        cells.append(f"\\textbf{{{abstract}}}" if abstract > concrete else str(abstract))
    return cells


def _short(domain):
    return re.sub(r"-(sat|opt)(\d\d)$", r"-\2", domain.removesuffix("-strips"))


def _htg_name(domain):
    collection, _, subdirectory = domain.partition("/")
    if collection == HTG_COLLECTION:
        return subdirectory.removesuffix("-large")
    return HTG_DOMAINS[collection]


def _without_year(name):
    return re.sub(r"-\d\d$", "", name)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="origin/main", help="Revision whose results go into the paper")
    parser.add_argument("--paper", default=DEFAULT_PAPER, help="The paper's main.tex, beside its figures/ folder")
    return parser


if __name__ == "__main__":
    main()
