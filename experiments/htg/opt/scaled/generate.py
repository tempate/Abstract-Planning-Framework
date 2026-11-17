"""Grow the best class of every base problem of the scaled HTG opt suite by copying one of its objects.

The copies follow experiments.ipc.opt.scaled.generate. The grown class need not
be the largest, so its rank at each size goes to best_classes.csv, which submit
reads until the track has results.
"""

import csv

from experiments.htg.opt.scaled.suite import BASE_PROBLEMS
from experiments.ipc.opt.scaled.generate import scale, scale_domain
from experiments.ipc.opt.scaled.suite import SIZES
from experiments.report import best_classes
from experiments.tracks import TRACKS, find_domain


def grown_rank(classes, best, size):
    """The rank of class `best` once it holds `size` objects, ordered as the planner orders its candidates."""
    # Classes are disjoint, so their first objects decide the name order, and a
    # copy of the first object sorts after it.
    sizes = [size if rank == best else len(members) for rank, members in enumerate(classes)]
    order = sorted(range(len(classes)), key=lambda rank: classes[rank])
    order.sort(key=lambda rank: -sizes[rank])
    return order.index(best)


def main():
    source = TRACKS["opt-htg/symmetries"]
    scaled = TRACKS["opt-htg-scaled/symmetries"]
    best = best_classes(source.results_file)

    # Each problem's classes in rank order, each one's objects sorted as the planner sorts them.
    classes = {}
    for line in source.classes_file.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            problem, _rank, _type, _size, objects = line.split("\t")
            classes.setdefault(problem, []).append(sorted(objects.split()))

    runnable = []
    ranks = []
    for name in BASE_PROBLEMS:
        domain_name, _, problem_name = name.rpartition("/")
        rank = best[(domain_name, problem_name, "abs-lmcut")]
        members = classes[name][rank]
        problem = source.benchmarks_dir / name
        base = problem.read_text()
        base_domain = find_domain(problem).read_text()

        for size in [len(members)] + [size for size in SIZES if size > len(members)]:
            domain = f"{domain_name}/size-{size}"
            directory = scaled.benchmarks_dir / domain
            directory.mkdir(parents=True, exist_ok=True)

            # A domain file of its own, since problems of one directory may copy different constants.
            copies = size - len(members)
            (directory / f"{problem.stem}-domain.pddl").write_text(scale_domain(base_domain, members[0], copies))
            (directory / problem_name).write_text(scale(base, members[0], copies))
            runnable.append(f"{domain}/{problem_name}")
            ranks.append((domain, problem_name, "abs-lmcut", grown_rank(classes[name], rank, size)))

    header = "# Every problem of the suite. Regenerate with:\n#   python -m experiments.htg.opt.scaled.generate\n"
    scaled.runnable_file.write_text(header + "\n".join(sorted(runnable)) + "\n", encoding="utf-8")

    with (scaled.directory / "best_classes.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\r\n")
        writer.writerow(("domain", "problem", "mode", "class"))
        writer.writerows(sorted(ranks))


if __name__ == "__main__":
    main()
