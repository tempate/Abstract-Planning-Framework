"""Write ASP files used for abstract-plan mapping and refinement."""

import time

from core.asp.mapping import write_lp_lines
from core.runtime.run_artifacts import get_logger, log_phase


def write_occurs_abs_lp(atoms, output_path):
    """Write an abstract occurrence fact for each occurrence atom."""
    logger = get_logger()
    start = time.perf_counter()
    lines = []
    for atom in atoms:
        atom = atom.strip()
        if atom.startswith("occurs("):
            lines.append("occurs_abstract" + atom[len("occurs"):] + ".")
        elif atom.startswith("occurs_abstract("):
            lines.append(atom + ".")

    write_lp_lines(output_path, lines)
    logger.info(f"[FILES] wrote {output_path}")
    log_phase(logger, "[FILES] occurs_abs generation", start)


def write_forbid_abstract_lp(abstract_atoms_to_forbid, output_path):
    """Write constraints that forbid selected abstract occurrence atoms."""
    logger = get_logger()
    start = time.perf_counter()
    logger.info("[REFINE] Writing forbid rules")
    lines = []
    for atom in abstract_atoms_to_forbid:
        concrete_atom = str(atom).replace("occurs_abstract", "occurs")
        logger.info(f"[REFINE] forbid {concrete_atom}")
        lines.append(f":- {concrete_atom}.")

    write_lp_lines(output_path, lines)
    logger.info(f"[FILES] wrote {output_path}")
    log_phase(logger, "[REFINE] forbid file generation", start)
