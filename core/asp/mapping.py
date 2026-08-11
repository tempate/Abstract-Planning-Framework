"""Shared parsing and file-writing helpers for ASP mapping programs."""

from collections.abc import Iterable, Iterator
from pathlib import Path


def read_abstract_actions(path: str | Path) -> Iterator[tuple[str, str]]:
    """Yield ``(action, time_step)`` pairs from ``occurs_abstract`` facts."""
    with open(path, "r", encoding="utf-8") as source:
        for line in source:
            line = line.strip()
            if not line.startswith("occurs_abstract("):
                continue
            inner = line[len("occurs_abstract("):].rstrip(").")
            if "," in inner:
                yield tuple(part.strip() for part in inner.rsplit(",", 1))


def write_lp_lines(path: str | Path, lines: Iterable[str]) -> None:
    """Write LP statements separated by newlines."""
    with open(path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(lines))
