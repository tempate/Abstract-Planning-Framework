"""Decremental concrete solving."""

from core.integrations.clingo import create_control


def solve_decrementally(asp, horizon, on_attempt=None):
    """Relax the switches an unsat core blames until a concrete plan is found."""
    control = create_control(asp, horizon)

    switches = _collect_switches(control)
    symbol_by_step = dict(switches)

    step_by_literal = {}
    enabled = {}
    for step, symbol in switches:
        step_by_literal[control.symbolic_atoms[symbol].literal] = step
        enabled[symbol] = True

    decrements = 0
    while True:
        if on_attempt is not None:
            on_attempt(decrements, decrements + 1)

        plan, core = _solve_with_core(control, enabled)
        if plan is not None:
            return True, plan, decrements

        # Keep switches the core does not blame: they still guide the search.
        # If the core blames no enabled switch, no relaxation can help.
        blamed = []
        for literal in core:
            step = step_by_literal.get(literal)
            if step is not None and enabled[symbol_by_step[step]]:
                blamed.append(step)
        if not blamed:
            return False, None, decrements

        enabled[symbol_by_step[max(blamed)]] = False
        decrements += 1


def _collect_switches(control):
    """Return ``(time_step, symbol)`` switch pairs sorted by time step."""
    switches = []
    for atom in control.symbolic_atoms:
        if atom.symbol.name == "switch":
            switches.append((atom.symbol.arguments[0].number, atom.symbol))
    switches.sort(key=lambda item: item[0])
    return switches


def _solve_with_core(control, enabled):
    """Solve under the enabled switches, returning a plan or an unsat core."""
    assumptions = list(enabled.items())
    with control.solve(yield_=True, assumptions=assumptions) as handle:
        for plan in handle:
            atoms = []
            for atom in plan.symbols(shown=True):
                atoms.append(str(atom))
            return atoms, []
        return None, list(handle.core())
