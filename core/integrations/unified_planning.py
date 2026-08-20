"""Unified Planning boundary for parsing and serializing paired PDDL tasks."""

import re
from dataclasses import dataclass
from pathlib import Path

from unified_planning.io import PDDLReader, PDDLWriter
from unified_planning.model import Problem


class PddlError(ValueError):
    """Raised when a paired PDDL task cannot be parsed or serialized."""


@dataclass(frozen=True)
class PddlText:
    """A domain and problem serialized as one matched PDDL pair."""

    domain: str
    problem: str


def read_problem(domain_path, problem_path):
    """Read a PDDL pair from disk into a Unified Planning problem."""
    domain = Path(domain_path).read_text(encoding="utf-8")
    problem = Path(problem_path).read_text(encoding="utf-8")
    return parse_problem(domain, problem)


def parse_problem(domain_text, problem_text):
    """Parse a PDDL pair and validate its domain reference."""
    domain_name = _declaration_name(domain_text, "domain")
    referenced_domain = _problem_domain_name(problem_text)
    if domain_name.casefold() != referenced_domain.casefold():
        raise PddlError(f"Problem references domain {referenced_domain!r}, expected {domain_name!r}")

    try:
        return PDDLReader().parse_problem_string(domain_text, problem_text)
    except Exception as error:
        raise PddlError(f"Could not parse PDDL task: {error}") from error


def write_problem(problem: Problem):
    """Serialize a Unified Planning problem as a matched PDDL pair."""
    try:
        writer = PDDLWriter(problem)
        return PddlText(writer.get_domain(), writer.get_problem())
    except Exception as error:
        raise PddlError(f"Could not serialize PDDL task: {error}") from error


def _without_comments(text):
    return "\n".join(line.split(";", 1)[0] for line in text.splitlines())


def _declaration_name(text, kind):
    match = re.search(rf"\(\s*{kind}\s+([^\s()]+)\s*\)", _without_comments(text), flags=re.IGNORECASE)
    if not match:
        raise PddlError(f"PDDL does not declare a {kind} name")
    return match.group(1)


def _problem_domain_name(text):
    match = re.search(r"\(\s*:domain\s+([^\s()]+)\s*\)", _without_comments(text), flags=re.IGNORECASE)
    if not match:
        raise PddlError("PDDL problem does not reference a domain")
    return match.group(1)
