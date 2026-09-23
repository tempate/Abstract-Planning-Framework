"""The benchmark tracks: the problems each one runs, the driver that runs them, and where the results go."""

from dataclasses import dataclass
from pathlib import Path

from experiments.plan import suite as plan
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

    @property
    def results_file(self):
        return self.directory / "results.csv"

    @property
    def symmetries_file(self):
        return self.directory / "symmetries.txt"

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the symmetries file records a class for."""
        problems = set()
        for line in self.symmetries_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.partition("/")
                problems.add((domain, problem))
        return frozenset(problems)


TRACKS = {
    "plan": Track(
        directory=Path(plan.__file__).parent,
        suite=plan.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
    ),
    "unsolvability": Track(
        directory=Path(unsolvability.__file__).parent,
        suite=unsolvability.SUITE,
        benchmarks_dir=BENCHMARKS / "unsolve-ipc-2016",
        driver="scripts.unsolvability",
    ),
}
DEFAULT_TRACK = "plan"
