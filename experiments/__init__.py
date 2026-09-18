"""Benchmark tracks: the problems each one runs, and the drivers that run them."""

from pathlib import Path

# The benchmark collections. A track says which of their problems it runs; it
# does not own the PDDL, so that two tracks over one collection cannot drift
# onto different revisions of it.
_BENCHMARKS = Path(__file__).parent / "benchmarks"
DOWNWARD_BENCHMARKS_DIR = _BENCHMARKS / "downward-benchmarks"
UNSOLVE_IPC_DIR = _BENCHMARKS / "unsolve-ipc-2016"


def read_problems(path):
    """Read a symmetries file into the (domain, problem) pairs worth submitting."""
    problems = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domain, _, problem = line.partition("/")
            problems.add((domain, problem))
    return frozenset(problems)
