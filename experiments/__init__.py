"""Benchmark tracks: the problems each one runs, and the drivers that run them."""

from pathlib import Path


def read_problems(path):
    """Read a symmetries file into the (domain, problem) pairs worth submitting."""
    problems = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domain, _, problem = line.partition("/")
            problems.add((domain, problem))
    return frozenset(problems)
