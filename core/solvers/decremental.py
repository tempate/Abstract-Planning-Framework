"""Decremental concrete solving."""

from core.integrations.clingo import create_control


def solve_decrementally(asp, horizon, on_attempt=None):
    """Relax abstract-plan constraints until a concrete plan is found.

    Rather than disabling switches blindly in reverse order, every failed
    solve yields an unsatisfiable core: the still-enabled switches that
    Clingo blames for the conflict. The latest blamed switch is disabled
    next, so switches that do not take part in any conflict keep guiding the
    concrete search. When a core no longer mentions an enabled switch, no
    further relaxation can help and the search stops.
    """
    control = create_control(asp, horizon)

    switches = _collect_switches(control)
    symbol_by_step = dict(switches)
    step_by_literal = {control.symbolic_atoms[symbol].literal: step for step, symbol in switches}

    enabled = {symbol: True for _, symbol in switches}

    decrements = 0
    while True:
        if on_attempt is not None:
            on_attempt(decrements, decrements + 1)

        plan, core = _solve_with_core(control, enabled)
        if plan is not None:
            return True, plan, decrements

        blamed = [
            step
            for literal in core
            if (step := step_by_literal.get(literal)) is not None and enabled[symbol_by_step[step]]
        ]
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
            return [str(atom) for atom in plan.symbols(shown=True)], []
        return None, list(handle.core())
