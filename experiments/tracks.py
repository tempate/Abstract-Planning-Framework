"""The benchmark tracks: the problems each one runs, the driver that runs them, and where the results go."""

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from experiments.opt import suite as opt
from experiments.sat import suite as sat
from experiments.unsat import suite as unsat

# The benchmark collections. A track says which of their problems it runs; it
# does not own the PDDL, so that two tracks over one collection cannot drift
# onto different revisions of it.
BENCHMARKS = Path(__file__).parent / "benchmarks"


@dataclass(frozen=True)
class Track:
    directory: Path
    suite: list[str]
    benchmarks_dir: Path
    driver: str
    # The driver's modes, the first of them submitted by default.
    modes: tuple[str, ...]
    # Passed to the modes through an abstraction only; the others have no class to choose.
    abstract_arguments: tuple[str, ...] = ()

    @property
    def results_file(self):
        return self.directory / "results.csv"

    @property
    def runnable_file(self):
        return self.directory / "problems.txt"

    @property
    def classes_file(self):
        return self.directory / "classes.txt"

    def class_counts(self):
        """How many classes each problem can collapse, as classes.txt lists them, or None without one."""
        if not self.classes_file.is_file():
            return None
        counts = Counter()
        for line in self.classes_file.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                domain, _, problem = line.split("\t")[0].partition("/")
                counts[(domain, problem)] += 1
        return counts

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the runnable file lists."""
        problems = set()
        for line in self.runnable_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.partition("/")
                problems.add((domain, problem))
        return frozenset(problems)


# Keyed by the question a track asks, then, for sat, by what it abstracts to answer it.
TRACKS = {
    "sat/symmetries": Track(
        directory=Path(sat.__file__).parent / "symmetries",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-lama", "asp", "lama"),
    ),
    # The same suite, restricted to the problems numeric-fast-downward finds a
    # resource for, and planned from that resource's objects.
    "sat/resources": Track(
        directory=Path(sat.__file__).parent / "resources",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-lama", "asp", "lama"),
        abstract_arguments=("--abstraction-source", "resources"),
    ),
    # The optimal suite, refined to the plan that fills the fewest gaps, with
    # abs-lmcut searching the abstract task optimally like its lmcut baseline.
    "opt/symmetries": Track(
        directory=Path(opt.__file__).parent / "symmetries",
        suite=opt.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-lmcut", "asp", "lmcut"),
        abstract_arguments=("--minimize-gaps",),
    ),
    "opt/resources": Track(
        directory=Path(opt.__file__).parent / "resources",
        suite=opt.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-lmcut", "asp", "lmcut"),
        abstract_arguments=("--minimize-gaps", "--abstraction-source", "resources"),
    ),
    "unsat/symmetries": Track(
        directory=Path(unsat.__file__).parent / "symmetries",
        suite=unsat.SUITE,
        benchmarks_dir=BENCHMARKS / "unsolve-ipc-2016",
        driver="scripts.unsolvability",
        modes=("abs-ms", "ms"),
    ),
}
DEFAULT_TRACK = "sat/symmetries"


def is_domain_file(name):
    """Tell a domain file from a problem file by name.

    downward-benchmarks spells it out in full; unsolve-ipc-2016 shortens it to
    domNN, satdomNN and unknowndomNN, against probNN, satprobNN and unknownprobNN.
    """
    return "domain" in name or re.match(r"(sat|unknown)?dom\d", name) is not None


def has_other_status(name):
    """Tell the problems standing around an unsolvable one from the problem itself.

    unsolve-ipc-2016 names probNN for the instances known to be unsolvable,
    satprobNN for the solvable twin beside it, and unknownprobNN for the ones
    nobody settled. Only the first is what this suite asks about.
    """
    return name.startswith(("satprob", "unknownprob"))


def find_domain(problem):
    """Find the domain file using the naming conventions of the benchmark collections."""
    candidates = [
        "domain.pddl",
        f"{problem.stem}-domain{problem.suffix}",
        f"{problem.name[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    ]
    if "prob" in problem.stem:
        # unsolve-ipc-2016 names the pair after each other: probNN.pddl with
        # domNN.pddl, and likewise satprobNN and unknownprobNN. Guarded, or a
        # problem with no prob in its name would answer as its own domain.
        candidates.append(f"{problem.stem.replace('prob', 'dom', 1)}{problem.suffix}")
        # bag-barman and bag-transport ship no satdomNN, and their satprobNN is
        # probNN with a single symbol changed, so it belongs to the same domNN.
        # Last, or diagnosis and cave-diving would take domNN over their satdomNN.
        candidates.append(f"dom{problem.stem.partition('prob')[2]}{problem.suffix}")
    for name in candidates:
        domain = problem.parent / name
        if domain.is_file():
            return domain
    raise FileNotFoundError(f"No domain file found for {problem}")
