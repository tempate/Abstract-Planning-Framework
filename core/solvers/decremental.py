"""Decremental concrete solving."""

from core.execution import get_logger, timed_phase
from core.integrations.clingo import collect_plan, create_control


def solve_decrementally(asp_files, horizon):
    """Relax plan constraints in reverse until a concrete plan is found."""
    logger = get_logger()
    with timed_phase(logger, "[DEC] Runtime"):
        control = create_control(asp_files, horizon)
        switch_ids = {
            atom.symbol: atom.symbol.arguments[0].number
            for atom in control.symbolic_atoms
            if atom.symbol.name == "switch"
        }
        switches = sorted(switch_ids, key=switch_ids.__getitem__)
        active_switches = set(switches)

        logger.info("[DEC] Starting decremental solve")
        logger.info(f"[DEC] Found switches={len(switches)}")

        plan = collect_plan(
            control,
            [(switch, True) for switch in switches],
        )
        if plan is not None:
            logger.info("[DEC] Full plan SAT")
            return True, plan, 0

        logger.info("[DEC] Full plan UNSAT. Reverse disabling begins.")
        for decrements, switch in enumerate(reversed(switches), start=1):
            switch_id = switch_ids[switch]
            logger.info(f"[DEC] Disabled switch={switch_id}")
            active_switches.remove(switch)
            assumptions = [
                (candidate, candidate in active_switches)
                for candidate in switches
            ]
            plan = collect_plan(control, assumptions)
            if plan is not None:
                logger.info(f"[DEC] SAT after disabling switch={switch_id}")
                return True, plan, decrements

        logger.info("[DEC] No concrete plan found")
        return False, None, len(switches)
