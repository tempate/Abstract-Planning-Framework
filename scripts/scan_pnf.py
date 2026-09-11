"""Report which suite domains must reach positive normal form before deletes are relaxed.

Relaxing a delete can only change a task when some condition tests the deleted
fluent negatively, so a domain is safe unless it negates a predicate that some
action also deletes.
"""

import argparse
import csv
import re
from pathlib import Path

from benchmarks.suite import BENCHMARKS_DIR, SUITE
from scripts.run_benchmark import PROJECT_ROOT

DEFAULT_CSV = PROJECT_ROOT / "benchmarks" / "results.csv"
NEEDS_PNF = "needs PNF"
INERT = "inert"
POSITIVE = "already positive"
ADL_FORMS = ("when", "forall", "exists", "or", "imply")


def main():
    args = _argument_parser().parse_args()
    collapsed = _collapsed_types(args.results)
    rows = []
    for domain in SUITE:
        directory = Path(args.benchmarks) / domain
        if not directory.is_dir():
            continue
        rows.append(scan(directory, collapsed.get(domain, ())))
    _print_table(rows)
    _print_discards(rows)


def scan(directory, collapsed_types=()):
    """Report the negations of one domain directory and what they mean for relaxation."""
    domains, problems = _classify(directory)

    predicates = {}
    fluents = set()
    deleted = set()
    adl = set()
    for text in domains:
        _read_domain(_parse(text), predicates, fluents, deleted, adl)

    negated_pre = {}
    for text in domains:
        for action in _find_all(_parse(text), ":action"):
            _count_negations(_argument_of(action, ":precondition"), negated_pre)

    negated_goal = {}
    for text in problems:
        for goal in _find_all(_parse(text), ":goal"):
            _count_negations(goal, negated_goal)

    negated = {}
    for source in (negated_pre, negated_goal):
        for name, count in source.items():
            negated[name] = negated.get(name, 0) + count

    reachable = []
    for name in sorted(negated):
        if name in deleted:
            reachable.append(name)

    on_collapsed = []
    for name in reachable:
        for parameter in predicates.get(name, ()):
            if parameter in collapsed_types:
                on_collapsed.append(name)
                break

    return {
        "domain": directory.name,
        "files": len(domains),
        "problems": len(problems),
        "negated_fluent_pre": _total(negated_pre, fluents),
        "negated_fluent_goal": _total(negated_goal, fluents),
        "inequalities": negated_pre.get("=", 0) + negated_goal.get("=", 0),
        "predicates": predicates,
        "deleted": deleted,
        "negated": negated,
        "reachable": reachable,
        "on_collapsed": on_collapsed,
        "collapsed_types": tuple(collapsed_types),
        "adl": sorted(adl),
        "verdict": _verdict(negated, fluents, reachable),
    }


def _verdict(negated, fluents, reachable):
    negated_fluents = False
    for name in negated:
        if name in fluents:
            negated_fluents = True
            break
    if not negated_fluents:
        return POSITIVE
    if not reachable:
        return INERT
    return NEEDS_PNF


def _total(counts, fluents):
    total = 0
    for name, count in counts.items():
        if name in fluents:
            total += count
    return total


def _classify(directory):
    """Split a benchmark directory into domain and problem sources."""
    domains, problems = [], []
    for path in sorted(directory.glob("*.pddl")):
        text = path.read_text(errors="ignore")
        stripped = re.sub(r";[^\n]*", "", text).lower()
        if re.search(r"\(\s*define\s*\(\s*domain", stripped):
            domains.append(text)
        elif re.search(r"\(\s*define\s*\(\s*problem", stripped):
            problems.append(text)
    return domains, problems


def _parse(text):
    """Parse PDDL into nested lists, lowercased and without comments."""
    text = re.sub(r";[^\n]*", "", text).lower()
    tokens = text.replace("(", " ( ").replace(")", " ) ").split()
    stack = [[]]
    for token in tokens:
        if token == "(":
            stack.append([])
        elif token == ")":
            node = stack.pop()
            stack[-1].append(node)
        else:
            stack[-1].append(token)
    return stack[0]


def _find_all(node, head):
    """Yield every list whose first element is head, at any depth."""
    if not isinstance(node, list):
        return
    if node and node[0] == head:
        yield node
    for child in node:
        for found in _find_all(child, head):
            yield found


def _argument_of(node, keyword):
    """Return what follows a keyword inside a list, or None."""
    for index, item in enumerate(node):
        if item == keyword and index + 1 < len(node):
            return node[index + 1]
    return None


def _read_domain(tree, predicates, fluents, deleted, adl):
    for block in _find_all(tree, ":predicates"):
        for entry in block[1:]:
            if isinstance(entry, list) and entry:
                predicates[entry[0]] = _parameter_types(entry)
    for block in _find_all(tree, ":derived"):
        adl.add(":derived")
        if len(block) > 1 and isinstance(block[1], list) and block[1]:
            predicates.setdefault(block[1][0], _parameter_types(block[1]))
    for action in _find_all(tree, ":action"):
        effect = _argument_of(action, ":effect")
        if effect is None:
            continue
        _read_effect(effect, fluents, deleted)
        for form in ADL_FORMS:
            for _ in _find_all(effect, form):
                adl.add(form)
                break
        precondition = _argument_of(action, ":precondition")
        for form in ADL_FORMS:
            for _ in _find_all(precondition, form):
                adl.add(form)
                break


def _read_effect(node, fluents, deleted):
    """Collect the predicates an effect adds, and those it deletes."""
    if not isinstance(node, list) or not node:
        return
    head = node[0]
    if head == "not":
        if len(node) > 1 and isinstance(node[1], list) and node[1]:
            name = node[1][0]
            fluents.add(name)
            deleted.add(name)
        return
    if head in ("and", "when", "forall", "exists"):
        for child in node[1:]:
            _read_effect(child, fluents, deleted)
        return
    if isinstance(head, str) and not head.startswith(":"):
        fluents.add(head)


def _count_negations(node, counts):
    """Count each (not (p ...)) by the predicate it negates, equality included."""
    if not isinstance(node, list) or not node:
        return
    if node[0] == "not" and len(node) > 1 and isinstance(node[1], list) and node[1]:
        name = node[1][0]
        counts[name] = counts.get(name, 0) + 1
    for child in node:
        _count_negations(child, counts)


def _parameter_types(entry):
    """Read a predicate's parameter types, marking untyped parameters "?"."""
    types = []
    pending = 0
    expecting = False
    for token in entry[1:]:
        if token == "-":
            expecting = True
        elif expecting:
            for _ in range(pending):
                types.append(token)
            pending = 0
            expecting = False
        elif isinstance(token, str) and token.startswith("?"):
            pending += 1
    for _ in range(pending):
        types.append("?")
    return tuple(types)


def _collapsed_types(results_file):
    """Read the object type each domain actually collapsed, from a collected run."""
    collapsed = {}
    path = Path(results_file)
    if not path.is_file():
        return collapsed
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            object_type = row.get("abstracted_object_type")
            if object_type:
                collapsed.setdefault(row["domain"], set()).add(object_type)
    return collapsed


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmarks", default=BENCHMARKS_DIR, help="Directory holding the benchmark domains")
    parser.add_argument("--results", default=DEFAULT_CSV, help="Collected CSV naming the type each domain collapsed")
    return parser


def _print_table(rows):
    header = f"{'domain':38}{'files':>6}{'¬fluent pre':>12}{'¬fluent goal':>13}{'¬=':>6}  {'collapsed':22}{'verdict'}"
    print(header)
    print("-" * len(header))
    for row in sorted(rows, key=lambda item: (item["verdict"] != NEEDS_PNF, item["verdict"] != INERT, item["domain"])):
        collapsed = ", ".join(sorted(row["collapsed_types"])) or "—"
        print(
            f"{row['domain']:38}{row['files']:>6}{row['negated_fluent_pre']:>12}"
            f"{row['negated_fluent_goal']:>13}{row['inequalities']:>6}  {collapsed[:20]:22}{row['verdict']}"
        )


def _print_discards(rows):
    flagged = []
    for row in rows:
        if row["verdict"] == NEEDS_PNF:
            flagged.append(row)
    print(f"\n{len(flagged)} domain(s) negate a predicate that some action deletes:")
    for row in flagged:
        print(f"\n  {row['domain']}")
        for name in row["reachable"]:
            parameters = row["predicates"].get(name, ())
            if name in row["on_collapsed"]:
                reach = "on the collapsed type"
            elif not parameters:
                reach = "no arguments"
            elif "?" in parameters:
                reach = "untyped, cannot tell"
            else:
                reach = "not a collapsed type here"
            label = ", ".join(parameters) or "no arguments"
            print(f"    {name} ({label}) — negated {row['negated'][name]}x, deleted, {reach}")
    adl = set()
    for row in rows:
        adl.update(row["adl"])
    print(f"\nADL forms anywhere in the suite: {', '.join(sorted(adl)) or 'none'}")


if __name__ == "__main__":
    main()
