"""Write the results at a revision into the paper: its summary and per-domain tables, and its figures as the PDFs main.tex includes."""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

from experiments.figure import DEFAULT_PAPER, SOURCES, TRACK_NAMES, htg_domain, load_tracks, paper_figures, render_pdf
from experiments.report import solved
from experiments.run import ABSTRACTION_PREFIX

# The modes each track counts, each planner before its symmetry pruning and its abstraction, and rnd-g after Fast
# Downward's. A set without a mode's results shows --.
MODES = {
    "sat": ("asp", "abs-asp", "lama", "lama-symmetry-pruning", "abs-lama", "rnd-g", "powerlifted", "abs-powerlifted"),
    "opt": (
        "asp",
        "abs-asp",
        "lmcut",
        "lmcut-symmetry-pruning",
        "abs-lmcut",
        "rnd-g",
        "powerlifted",
        "abs-powerlifted",
    ),
}
# The group of the tables' FD columns, LAMA-first or LM-cut by track, which rnd-g joins.
FAST_DOWNWARD = "fd"
# The IPC per-domain table, a section of rows per benchmark set and a block of columns per track.
DOMAIN_TABLE = "tab:ipc-domains"
# The modes the per-domain table shows, in the order of MODES. Powerlifted does not run on IPC.
DOMAIN_MODES = {
    "sat": ("asp", "abs-asp", "lama", "lama-symmetry-pruning", "abs-lama", "rnd-g"),
    "opt": ("asp", "abs-asp", "lmcut", "lmcut-symmetry-pruning", "abs-lmcut", "rnd-g"),
}
# Each summary table, by its label, with the benchmark set each of its sections shows, by the section's title.
SUMMARY_TABLES = {"tab:ipc-summary": {"Symmetries": "IPC Symmetries", "Resources": "IPC Resources"}}
# The HTG table, a row per domain and a total, and a block of columns per track.
HTG_TABLE = "tab:htg"


def main():
    args = _argument_parser().parse_args()
    paper = Path(args.paper)
    tex = paper.read_text()

    totals = {}
    for section, tracks in benchmark_sets(args.revision).items():
        htg = section.startswith("HTG")
        counts = {kind: domain_counts(problems, kind, htg=htg) for kind, problems in tracks.items()}
        if htg:
            tex = update_htg_table(tex, counts)
            continue

        tex, changed = update_table(tex, section, counts)
        for kind, track in counts.items():
            totals[section, kind] = _total(track)
        print(f"{section}: {', '.join(changed) or 'no domain row'} changed")
    for label, sections in SUMMARY_TABLES.items():
        sets = {title: {kind: totals[section, kind] for kind in MODES} for title, section in sections.items()}
        tex = update_summary(tex, label, sets)
    paper.write_text(tex)

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
        row = rows[htg_domain(domain) if htg else _short(domain)]
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


def update_table(tex, section, counts):
    """Write one section of the per-domain table, a block of columns per track, the best of each
    planner's group in bold."""
    start, end = _section(tex, DOMAIN_TABLE, section)
    lines = tex[start:end].split("\n")

    width = sum(len(DOMAIN_MODES[kind]) + 1 for kind in counts)
    domains = {name for track in counts.values() for name in track}
    changed = []
    written = set()
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.rstrip().removesuffix("\\\\").split("&")]
        if len(cells) < width + 1:
            continue

        name = cells[0]
        if name not in domains:
            raise SystemExit(f"No {section} results for the paper's row {name}")

        row = []
        for kind, track in counts.items():
            # A domain only the other track has reads -- here.
            if name not in track:
                row += ["--"] * (len(DOMAIN_MODES[kind]) + 1)
                continue
            count, *solved = track[name]
            shown = [solved[MODES[kind].index(mode)] for mode in DOMAIN_MODES[kind]]
            row += [str(count), *_bold_groups(DOMAIN_MODES[kind], shown)]
        if row != cells[1:]:
            changed.append(name)

        lines[index] = " & ".join([name, *row]) + " \\\\"
        written.add(name)

    missing = sorted(domains - written)
    if missing:
        raise SystemExit(f"The paper's {section} section has no row for {', '.join(missing)}")

    return tex[:start] + "\n".join(lines) + tex[end:], changed


def update_summary(tex, table, sets):
    """Write one summary table, a section per benchmark set with a row per track, the best of each planner's
    group in bold."""
    totals = [total for tracks in sets.values() for total in tracks.values()]
    # A planner that never ran on the table's benchmark sets, such as Powerlifted on IPC, has no columns.
    shown = [any(total[index] is not None for total in totals) for index in range(len(totals[0]))]

    for title, tracks in sets.items():
        rows = {}
        for kind, (count, *solved) in tracks.items():
            cells = [str(count), *_bold_groups(MODES[kind], solved)]
            rows[TRACK_NAMES[kind]] = [cell for cell, show in zip(cells, shown) if show]
        start, end = _section(tex, table, title)
        tex = tex[:start] + _write_rows(tex[start:end], f"{table} {title}", rows) + tex[end:]
    return tex


def update_htg_table(tex, counts):
    """Write the HTG table, a row per domain and a total with a block of columns per track, the best of
    each planner's group in bold."""
    domains = {name for track in counts.values() for name in track}
    for kind, track in counts.items():
        lacking = sorted(domains - set(track))
        if lacking:
            raise SystemExit(f"No {TRACK_NAMES[kind]} HTG results for {', '.join(lacking)}")

    tracks = {kind: {**track, "Total": _total(track)} for kind, track in counts.items()}
    rows = {}
    for name in [*sorted(domains), "Total"]:
        rows[name] = []
        for kind, track in tracks.items():
            count, *solved = track[name]
            rows[name] += [str(count), *_bold_groups(MODES[kind], solved)]

    start = tex.rindex(r"\begin{table", 0, tex.index(rf"\label{{{HTG_TABLE}}}"))
    # The table runs the full text width as a tabular*.
    end = tex.index(r"\end{tabular", start)
    return tex[:start] + _write_rows(tex[start:end], HTG_TABLE, rows) + tex[end:]


def _write_rows(text, table, rows):
    """Replace the cells of each row of a table its label names, and stop on a row either side lacks."""
    lines = text.split("\n")

    for index, line in enumerate(lines):
        label, *cells = [cell.strip() for cell in line.split("&")]
        if label in rows:
            lines[index] = " & ".join([label, *rows.pop(label)]) + " \\\\"
        # A row of numbers opens with its problem count, unlike the table's headers.
        elif cells and cells[0].isdigit():
            raise SystemExit(f"No {table} results for the paper's row {label}")

    if rows:
        raise SystemExit(f"The table {table} has no row for {', '.join(rows)}")

    return "\n".join(lines)


def _total(counts):
    """The column sums of a track's domain rows, None for a mode without results."""
    return [None if None in column else sum(column) for column in zip(*counts.values())]


def _bold_groups(modes, solved_counts):
    """The solved counts of these modes, the best of each planner's group in bold."""
    groups = defaultdict(list)
    for mode, solved in zip(modes, solved_counts):
        groups[_planner(mode)].append(solved)
    return [cell for group in groups.values() for cell in _bold_best(group)]


def _planner(mode):
    """The group whose best count is bold, the planner a mode runs, which its pruning and abstraction share."""
    planner = mode.removeprefix(ABSTRACTION_PREFIX).removesuffix("-symmetry-pruning")
    # rnd-g has no abstraction of its own, so it competes in the group of Fast Downward, which it sits beside.
    return FAST_DOWNWARD if planner in ("lama", "lmcut", "rnd-g") else planner


def _section(tex, label, section):
    """Where one section of a table starts, at its title, and ends, at the next title or the end of the table."""
    table = tex.rindex(r"\begin{table", 0, tex.index(rf"\label{{{label}}}"))
    start = tex.index(rf"\emph{{{section}}}", table)
    end = re.compile(r"\\emph\{|\\bottomrule").search(tex, start + 1).start()
    return start, end


def _bold_best(solved_counts):
    """Each mode's count, -- for a mode without results, and the most solved in bold unless none solves any."""
    best = max((solved for solved in solved_counts if solved is not None), default=0)
    cells = []
    for solved in solved_counts:
        if solved is None:
            cells.append("--")
        elif solved == best and best > 0:
            cells.append(f"\\textbf{{{solved}}}")
        else:
            cells.append(str(solved))
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
