"""The benchmark tracks: the problems each one runs, the driver that runs them, and where the results go."""

from dataclasses import dataclass
from pathlib import Path

import experiments.resources as resources
from experiments.symmetries import suite as symmetries
from experiments.unsolvability import suite as unsolvability

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
    # Where the problems worth submitting are listed, beside the results.
    runnable_name: str = "symmetries.txt"
    # Passed to the driver's abstract mode only; concrete has no class to choose.
    abstract_arguments: tuple[str, ...] = ()

    @property
    def results_file(self):
        return self.directory / "results.csv"

    @property
    def runnable_file(self):
        return self.directory / self.runnable_name

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the runnable file lists."""
        problems = set()
        for line in self.runnable_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.partition("/")
                problems.add((domain, problem))
        return frozenset(problems)


TRACKS = {
    "symmetries": Track(
        directory=Path(symmetries.__file__).parent,
        suite=symmetries.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
    ),
    # The symmetry track's problems, restricted to the ones numeric-fast-downward
    # finds a resource for, and planned from that resource's objects.
    "resources": Track(
        directory=Path(resources.__file__).parent,
        suite=symmetries.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        runnable_name="resources.txt",
        abstract_arguments=("--abstraction-source", "resources"),
    ),
    "unsolvability": Track(
        directory=Path(unsolvability.__file__).parent,
        suite=unsolvability.SUITE,
        benchmarks_dir=BENCHMARKS / "unsolve-ipc-2016",
        driver="scripts.unsolvability",
    ),
}
DEFAULT_TRACK = "symmetries"
