"""The benchmark tracks: the problems each one runs, the driver that runs them, and where the results go."""

from dataclasses import dataclass
from pathlib import Path

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
        modes=("abs-asp", "abs-fd", "asp", "fd"),
    ),
    # The same suite, restricted to the problems numeric-fast-downward finds a
    # resource for, and planned from that resource's objects.
    "sat/resources": Track(
        directory=Path(sat.__file__).parent / "resources",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-fd", "asp", "fd"),
        abstract_arguments=("--abstraction-source", "resources"),
    ),
    # The sat symmetries suite, refined to the plan that fills the fewest gaps,
    # with abs-fd searching the abstract task optimally like its fd-lmcut baseline.
    "opt": Track(
        directory=Path(__file__).parent / "opt",
        suite=sat.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abs-asp", "abs-fd", "fd-lmcut"),
        abstract_arguments=("--minimize-gaps", "--lmcut"),
    ),
    "unsat": Track(
        directory=Path(unsat.__file__).parent,
        suite=unsat.SUITE,
        benchmarks_dir=BENCHMARKS / "unsolve-ipc-2016",
        driver="scripts.unsolvability",
        modes=("abs-fd", "fd"),
    ),
}
DEFAULT_TRACK = "sat/symmetries"
