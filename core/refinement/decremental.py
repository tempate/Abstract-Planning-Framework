"""Decremental concrete solving."""


def solve_decrementally(solver, on_attempt=None):
    """Relax plan constraints in reverse until a concrete plan is found."""
    switches = collect_switches(solver)

    # Try the full abstract plan
    assumptions = {symbol: True for _, symbol in switches}
    if on_attempt is not None:
        on_attempt(0, 1)
    plan = solver.solve(list(assumptions.items()))

    if plan is not None:
        # The plan works. We are done.
        return True, plan, 0

    # The plan does not work. We need to decrementally disable switches.
    # Decrementally disable switches and check for a concrete plan
    for decs, (id, symbol) in enumerate(reversed(switches), start=1):
        # Disable the last switch
        assumptions[symbol] = False

        # Find a concrete plan with the current assumptions
        if on_attempt is not None:
            on_attempt(decs, decs + 1)
        plan = solver.solve(list(assumptions.items()))
        if plan is not None:
            return True, plan, decs

    return False, None, len(switches)


def collect_switches(solver):
    """Return the abstract-plan switches ordered by time step."""
    switches = []
    for atom in solver.control.symbolic_atoms:
        if atom.symbol.name == "switch":
            switch = (atom.symbol.arguments[0].number, atom.symbol)
            switches.append(switch)
    switches.sort(key=lambda item: item[0])
    return switches


def disabled_switches(solver):
    """Return assumptions that turn the whole abstract plan off."""
    assumptions = []
    for _, symbol in collect_switches(solver):
        assumptions.append((symbol, False))
    return assumptions
