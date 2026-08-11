"""Clingo-backed plan solving and abstraction-mapping helpers."""

import os
import time

import clingo

from core.mapping import read_abstract_actions, write_lp_lines
from scripts.utils.run_artifacts import get_logger, log_phase


THREADS = os.cpu_count()


def run_clingo(lp_files, horizon):
    logger = get_logger()
    start = time.perf_counter()
    logger.info("[CLINGO] Starting solve")
    logger.info(f"[CLINGO] Horizon={horizon}")
    logger.info(f"[CLINGO] Threads={THREADS}")
    logger.info(f"[CLINGO] Files={lp_files}")

    models = _models(_control(lp_files, horizon))
    log_phase(logger, "[CLINGO] Solve runtime", start)
    logger.info(f"[CLINGO] Models found={len(models)}")
    return models


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


def build_switch_mapping(occurs_abs_path, output_path, abstract_symbol, concrete_objects):
    """Build switch-gated concrete mappings for an abstract plan."""
    logger = get_logger()
    start = time.perf_counter()
    lines = []
    switch_map = {}

    for switch_id, (action, time_step) in enumerate(read_abstract_actions(occurs_abs_path), start=1):
        switch = f"switch({switch_id})"
        lines.append(f"0 {{ {switch} }} 1.")
        is_abstract = bool(abstract_symbol and abstract_symbol in action)

        if is_abstract:
            choices = [
                f"occurs({action.replace(abstract_symbol, obj)}, {time_step})"
                for obj in concrete_objects or []
            ]
            lines.append(
                f"1 {{ {'; '.join(choices)} }} 1 :- "
                f"occurs_abstract({action},{time_step}), {switch}."
            )
        else:
            lines.append(
                f"occurs({action},{time_step}) :- "
                f"occurs_abstract({action},{time_step}), {switch}."
            )

        switch_map[switch_id] = {
            "atom": f"occurs_abstract({action},{time_step})",
            "is_abstract": is_abstract,
        }

    write_lp_lines(output_path, lines)
    logger.info(f"[MAP] Switches created={len(switch_map)}")
    logger.info(f"[FILES] wrote {output_path}")
    logger.info("[MAP] Grounded plan:")
    for line in lines:
        logger.info(f"  {line}")
    log_phase(logger, "[MAP] build_switch_mapping", start)
    return switch_map


def solve_concrete_incremental(lp_files, horizon, switch_map):
    logger = get_logger()
    start = time.perf_counter()
    logger.info("[INC] Starting incremental solve")

    control = _control(lp_files, horizon)
    switches, switch_ids = _switches(control)
    logger.info(f"[INC] Found switches={len(switches)}")

    active_switches = []
    for index, switch in enumerate(switches):
        active_switches.append(switch)
        if index + 1 == len(switches):
            continue

        next_id = switch_ids[switches[index + 1]]
        if not switch_map[next_id]["is_abstract"]:
            continue

        logger.info(f"[INC] Testing before abstract switch={next_id}")
        if control.solve(assumptions=_assumptions(switches, active_switches)).unsatisfiable:
            failing_actions = _abstract_actions_for(switches, switch_ids, switch_map, active_switches)
            logger.info("[INC] UNSAT detected")
            logger.info(f"[INC] Failing abstract actions={failing_actions}")
            log_phase(logger, "[INC] Runtime", start)
            return False, [], failing_actions

    logger.info("[INC] All prefixes SAT. Solving full model.")
    plans = _models(control, [(switch, True) for switch in switches])
    abstract_actions = _abstract_actions_for(switches, switch_ids, switch_map, switches)
    logger.info(f"[INC] Plans found={len(plans)}")
    log_phase(logger, "[INC] Runtime", start)
    return True, plans, abstract_actions


def solve_concrete_decremental(lp_files, horizon, switch_map):
    logger = get_logger()
    start = time.perf_counter()
    logger.info("[DEC] Starting decremental solve")

    control = _control(lp_files, horizon)
    switches, switch_ids = _switches(control)
    logger.info(f"[DEC] Found switches={len(switches)}")

    active_switches = set(switches)
    if control.solve(assumptions=_assumptions(switches, active_switches)).satisfiable:
        logger.info("[DEC] Full model SAT")
        plans = _models(control, [(switch, True) for switch in switches])
        abstract_actions = _abstract_actions_for(switches, switch_ids, switch_map, switches)
        log_phase(logger, "[DEC] Runtime", start)
        return True, plans, abstract_actions

    logger.info("[DEC] Full model UNSAT. Reverse disabling begins.")
    for switch in reversed(switches):
        switch_id = switch_ids[switch]
        logger.info(f"[DEC] Disabled switch={switch_id}")
        active_switches.remove(switch)
        if not switch_map[switch_id]["is_abstract"]:
            continue
        if control.solve(assumptions=_assumptions(switches, active_switches)).satisfiable:
            logger.info(f"[DEC] SAT after disabling switch={switch_id}")
            plans = _models(control, _assumptions(switches, active_switches))
            abstract_actions = _abstract_actions_for(
                switches, switch_ids, switch_map, active_switches
            )
            abstract_actions.append(switch_map[switch_id]["atom"])
            log_phase(logger, "[DEC] Runtime", start)
            return False, plans, list(set(abstract_actions))

    earliest_abstract = next(
        (switch_map[switch_ids[switch]]["atom"] for switch in switches
         if switch_map[switch_ids[switch]]["is_abstract"]),
        None,
    )
    logger.info(f"[DEC] Minimal failing action={earliest_abstract}")
    log_phase(logger, "[DEC] Runtime", start)
    return False, [], [earliest_abstract]


def write_forbid_abstract_lp(abstract_atoms_to_forbid, output_path):
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


def _control(lp_files, horizon):
    control = clingo.Control(["-c", f"horizon={horizon}", "-t", str(THREADS), "--warn=none"])
    for lp_file in lp_files:
        control.load(lp_file)
    control.ground([("base", [])])
    return control


def _models(control, assumptions=None):
    models = []
    with control.solve(yield_=True, assumptions=assumptions or []) as handle:
        for model in handle:
            models.append([str(atom) for atom in model.symbols(shown=True)])
    return models


def _switches(control):
    switch_ids = {
        atom.symbol: atom.symbol.arguments[0].number
        for atom in control.symbolic_atoms
        if atom.symbol.name == "switch"
    }
    switches = sorted(switch_ids, key=switch_ids.__getitem__)
    return switches, switch_ids


def _assumptions(switches, active_switches):
    return [(switch, switch in active_switches) for switch in switches]


def _abstract_actions_for(switches, switch_ids, switch_map, selected_switches):
    return [
        switch_map[switch_ids[switch]]["atom"]
        for switch in switches
        if switch in selected_switches and switch_map[switch_ids[switch]]["is_abstract"]
    ]
