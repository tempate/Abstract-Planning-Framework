"""Decremental concrete solving."""

from core.execution import get_logger, timed_phase
from core.integrations.clingo import collect_plan, create_control


def solve_decrementally(asp, horizon):
    """Relax plan constraints in reverse until a concrete plan is found."""
    logger = get_logger()
    with timed_phase(logger, "[DEC] Runtime"):
        control = create_control(asp, horizon)

        # Collect switches
        switches = []
        for atom in control.symbolic_atoms:
            if atom.symbol.name == "switch":
                switch = (atom.symbol.arguments[0].number, atom.symbol)
                switches.append(switch)
        switches.sort(key=lambda item: item[0])

        # Try the full abstract plan
        assumptions = {symbol: True for _, symbol in switches}
        plan = collect_plan(control, list(assumptions.items()))

        if plan is not None:
            # The plan works. We are done.
            logger.info("[DEC] Full plan SAT")
            return True, plan, 0

        # The plan does not work. We need to decrementally disable switches.
        logger.info("[DEC] Full plan UNSAT. Reverse disabling begins.")
        logger.info("[DEC] Starting decremental solve")
        logger.info(f"[DEC] Found switches={len(switches)}")

        # Decrementally disable switches and check for a concrete plan
        for decs, (id, symbol) in enumerate(reversed(switches), start=1):
            # Disable the last switch
            assumptions[symbol] = False

            # Find a concrete plan with the current assumptions
            plan = collect_plan(control, list(assumptions.items()))
            if plan is not None:
                logger.info(f"[DEC] SAT after disabling switch={id}")
                return True, plan, decs

        logger.info("[DEC] No concrete plan found")
        return False, None, len(switches)
