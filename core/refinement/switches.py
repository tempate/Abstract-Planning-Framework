"""The switches that hold the abstract plan in the concrete program."""


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


def switches_off(solver, plan):
    """Count the abstract actions the solver gave up on."""
    switches = len(collect_switches(solver))
    if plan is None:
        return switches
    return switches - sum(1 for atom in plan if atom.startswith("switch("))
