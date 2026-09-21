"""The switches that hold the abstract plan in the concrete program."""


def collect_switches(solver):
    """Return the abstract-plan switch symbols ordered by time step."""
    switches = []
    for atom in solver.control.symbolic_atoms:
        if atom.symbol.name == "switch":
            switches.append((atom.symbol.arguments[0].number, atom.symbol))

    switches.sort(key=lambda item: item[0])
    return [symbol for _, symbol in switches]
