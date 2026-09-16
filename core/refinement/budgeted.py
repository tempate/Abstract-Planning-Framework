"""Budgeted concrete solving."""


def solve_within_budget(solver, on_attempt=None):
    """Raise the number of abstract actions that may be switched off until a plan is found."""
    budgets = collect_budgets(solver)

    # The solver picks which actions to switch off; the budget only says how many.
    for budget in sorted(budgets):
        if on_attempt is not None:
            on_attempt(budget, budget + 1)
        plan = solver.solve(_budget_assumptions(budgets, budget))
        if plan is not None:
            return True, plan, budget

    return False, None, max(budgets)


def collect_budgets(solver):
    """Return the budget atoms by the number of switches each one allows off."""
    budgets = {}
    for atom in solver.control.symbolic_atoms.by_signature("budget", 1):
        budgets[atom.symbol.arguments[0].number] = atom.symbol
    return budgets


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
    """Return assumptions that turn the whole abstract plan off, budget and all."""
    assumptions = []
    for _, symbol in collect_switches(solver):
        assumptions.append((symbol, False))
    for symbol in collect_budgets(solver).values():
        assumptions.append((symbol, False))
    return assumptions


def _budget_assumptions(budgets, budget):
    """Allow exactly this many switches to be off, and no other count."""
    assumptions = []
    for allowed, symbol in budgets.items():
        assumptions.append((symbol, allowed == budget))
    return assumptions
