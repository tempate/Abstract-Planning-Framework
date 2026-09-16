"""Concrete solving that minimizes how much of the abstract plan is given up."""


def solve_fewest_switches_off(solver, on_attempt=None):
    switches = collect_switches(solver)

    # Publish the one call before making it, so an interrupted run still has a counter.
    if on_attempt is not None:
        on_attempt(0, 1)

    plan, switched_off = _optimize(solver, switches)
    if plan is None:
        return False, None, len(switches)

    return True, plan, switched_off


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


def _optimize(solver, switches):
    # Enumerating improving models is how clingo reports an optimum: the last one
    # it yields is the best. Restore the first-model setting for the search that
    # follows, which has no minimize statement left to improve on.
    solver.control.configuration.solve.models = 0
    best = (None, 0)
    with solver.control.solve(yield_=True) as handle:
        for model in handle:
            switched_off = 0
            for _, symbol in switches:
                if not model.contains(symbol):
                    switched_off += 1
            best = ([str(atom) for atom in model.symbols(shown=True)], switched_off)
    solver.control.configuration.solve.models = 1

    return best
