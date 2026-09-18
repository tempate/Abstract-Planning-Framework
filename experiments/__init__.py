"""Benchmark tracks: the problems each one runs, and the drivers that run them."""

import json
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


# The symmetry classes of each problem, as "<domain>/<problem>" to the object
# names of every class the collapse accepts, in the canonical order
# ``usable_abstractions`` puts them in. A class is identified by its position
# in that list, so regenerating the file renumbers the results.
CLASS_MANIFEST_COMMENT = "_comment"
CLASS_MANIFEST_REGENERATE = "Regenerate with: python -m experiments.classes --jobs 2"


def read_classes(path):
    """Read a class manifest, or None where a track has none."""
    path = Path(path)
    if not path.is_file():
        return None
    document = json.loads(path.read_text(encoding="utf-8"))
    return {key: value for key, value in document.items() if key != CLASS_MANIFEST_COMMENT}


def write_classes(classes, path):
    document = {CLASS_MANIFEST_COMMENT: CLASS_MANIFEST_REGENERATE, **classes}
    Path(path).write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
