"""The benchmark tracks: the problems each one runs, and where the results go."""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from experiments.htg.opt import suite as htg_opt
from experiments.htg.sat import suite as htg
from experiments.ipc.opt import suite as opt
from experiments.ipc.sat import suite as sat

# The benchmark collections. A track says which of their problems it runs; it
# does not own the PDDL, so that two tracks over one collection cannot drift
# onto different revisions of it.
EXPERIMENTS = Path(__file__).parent
BENCHMARKS = EXPERIMENTS / "benchmarks"
# PDDL Symmetries grounds the task before it searches for symmetries, and the
# hard-to-ground problems run out of memory there, so they skip the grounding.
HTG_ARGUMENTS = ("--symmetries-before-grounding",)


@dataclass(frozen=True)
class Track:
    directory: Path
    suite: list[str]
    benchmarks_dir: Path
    # The modes, the first of them submitted by default.
    modes: tuple[str, ...]
    # Passed to the modes through an abstraction only; the others have no class to choose.
    abstract_arguments: tuple[str, ...] = ()
    # Passed to the modes that can find a shortest plan.
    optimizing_arguments: tuple[str, ...] = ()

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
                domain, _, problem = line.split("\t")[0].rpartition("/")
                counts[(domain, problem)] += 1

        return counts

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the runnable file lists."""
        problems = set()
        for line in self.runnable_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.rpartition("/")
                problems.add((domain, problem))

        return frozenset(problems)


# Keyed by the question a track asks, then, for sat, by what it abstracts to answer it.
TRACKS = {
    "sat/symmetries": Track(
        directory=EXPERIMENTS / "ipc" / "sat" / "symmetries",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        modes=("abs-asp", "abs-lama", "asp", "lama"),
    ),
    # The same suite, restricted to the problems numeric-fast-downward finds a
    # resource for, and planned from that resource's objects.
    "sat/resources": Track(
        directory=EXPERIMENTS / "ipc" / "sat" / "resources",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        modes=("abs-asp", "abs-lama", "asp", "lama"),
        abstract_arguments=("--abstraction-source", "resources"),
    ),
    # The hard-to-ground benchmarks, refined with the full grounding like sat/symmetries.
    "sat-htg/symmetries": Track(
        directory=EXPERIMENTS / "htg" / "sat",
        suite=htg.SUITE,
        benchmarks_dir=BENCHMARKS / "htg-domains",
        modes=("abs-asp", "abs-lama", "asp", "lama"),
        abstract_arguments=HTG_ARGUMENTS,
    ),
    # The hard-to-ground benchmarks, refined without gaps like opt/symmetries.
    "opt-htg/symmetries": Track(
        directory=EXPERIMENTS / "htg" / "opt",
        suite=htg_opt.SUITE,
        benchmarks_dir=BENCHMARKS / "htg-domains",
        modes=("abs-asp", "abs-lmcut", "asp", "lmcut"),
        abstract_arguments=HTG_ARGUMENTS,
        optimizing_arguments=("--optimize",),
    ),
    # The optimal suite, refined without gaps so that every plan is optimal, with
    # abs-lmcut searching the abstract task optimally like its lmcut baseline.
    "opt/symmetries": Track(
        directory=EXPERIMENTS / "ipc" / "opt" / "symmetries",
        suite=opt.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        modes=("abs-asp", "abs-lmcut", "asp", "lmcut"),
        optimizing_arguments=("--optimize",),
    ),
    "opt/resources": Track(
        directory=EXPERIMENTS / "ipc" / "opt" / "resources",
        suite=opt.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        modes=("abs-asp", "abs-lmcut", "asp", "lmcut"),
        abstract_arguments=("--abstraction-source", "resources"),
        optimizing_arguments=("--optimize",),
    ),
}
DEFAULT_TRACK = "sat/symmetries"


def is_domain_file(name):
    """Tell a domain file from a problem file by name."""
    return "domain" in name


def find_domain(problem):
    """Find the domain file using the naming conventions of the benchmark collections."""
    candidates = [
        "domain.pddl",
        f"{problem.stem}-domain{problem.suffix}",
        f"{problem.name[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    ]

    for name in candidates:
        domain = problem.parent / name
        if domain.is_file():
            return domain

    raise FileNotFoundError(f"No domain file found for {problem}")
