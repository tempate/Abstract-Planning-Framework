"""Read and write ASP programs used for plan mapping and refinement."""

from collections.abc import Iterable, Iterator
from pathlib import Path

from core.execution import get_logger, timed_phase


def read_abstract_actions(path: str | Path) -> Iterator[tuple[str, str]]:
    """Yield ``(action, time_step)`` pairs from abstract occurrence facts."""
    with open(path, "r", encoding="utf-8") as source:
        for line in source:
            line = line.strip()
            if not line.startswith("occurs_abstract("):
                continue
            inner = line[len("occurs_abstract("):].rstrip(").")
            if "," in inner:
                action, time_step = inner.rsplit(",", 1)
                yield action.strip(), time_step.strip()


def write_asp_program(path: str | Path, statements: Iterable[str]) -> None:
    """Write ASP statements separated by newlines."""
    with open(path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(statements))


def write_abstract_occurrences(atoms, output_path):
    """Write abstract occurrence facts for the supplied occurrence atoms."""
    logger = get_logger()
    with timed_phase(logger, "[FILES] abstract occurrence generation"):
        statements = []
        for atom in atoms:
            atom = atom.strip()
            if atom.startswith("occurs("):
                statements.append("occurs_abstract" + atom[len("occurs"):] + ".")
            elif atom.startswith("occurs_abstract("):
                statements.append(atom + ".")

        write_asp_program(output_path, statements)
        logger.info(f"[FILES] wrote {output_path}")


def write_forbidden_actions(abstract_atoms, output_path):
    """Write constraints that forbid the supplied abstract occurrence atoms."""
    logger = get_logger()
    with timed_phase(logger, "[REFINE] forbidden action generation"):
        logger.info("[REFINE] Writing forbidden actions")
        statements = []
        for atom in abstract_atoms:
            concrete_atom = str(atom).replace("occurs_abstract", "occurs")
            logger.info(f"[REFINE] forbid {concrete_atom}")
            statements.append(f":- {concrete_atom}.")

        write_asp_program(output_path, statements)
        logger.info(f"[FILES] wrote {output_path}")
