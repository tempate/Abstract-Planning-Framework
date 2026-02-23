import re
from collections import defaultdict
from dataclasses import dataclass

###############################################################################
# Data structures
###############################################################################

@dataclass
class SymmetryClass:
    obj_type: str
    objects: list
    resource_preds: set
    needs_relaxation: bool
    reason: str


###############################################################################
# Basic PDDL parsing (robust enough for your domain)
###############################################################################

def extract_objects(problem):
    block = re.search(r"\(:objects(.*?)\)", problem, re.S)
    if not block:
        return {}

    block = block.group(1)
    objs = defaultdict(list)

    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith(";"):
            continue
        if "-" not in line:
            continue

        names, typ = line.rsplit("-", 1)
        typ = typ.strip()
        for n in names.split():
            objs[typ].append(n.strip())

    return objs


def extract_init(problem):
    block = re.search(r"\(:init(.*?)\)\s*\(:goal", problem, re.S).group(1)
    return re.findall(r"\([^)]+\)", block)


def extract_goal(problem):
    block = re.search(r"\(:goal\s*\((and.*?)\)\)", problem, re.S).group(1)
    return re.findall(r"\([^)]+\)", block)


def extract_actions(domain):
    return re.findall(r"\(:action.*?\)\s*\)", domain, re.S)


###############################################################################
# Symmetry detection
###############################################################################

def object_signature(obj, init_atoms, actions):
    sig = []
    for a in init_atoms:
        if obj in a:
            sig.append(("init", re.sub(obj, "?", a)))
    for act in actions:
        if obj in act:
            sig.append(("act", re.sub(obj, "?", act)))
    return tuple(sorted(sig))


def detect_symmetry_classes(objects, init_atoms, actions):
    classes = defaultdict(list)
    for typ, objs in objects.items():
        sig_map = defaultdict(list)
        for o in objs:
            sig = object_signature(o, init_atoms, actions)
            sig_map[sig].append(o)
        for group in sig_map.values():
            if len(group) > 1:
                classes[typ].append(group)
    return classes


###############################################################################
# Resource predicate & safety analysis
###############################################################################

def detect_resource_preds(domain, typ):
    """
    Detect predicates of the form:
      (p ?x - typ)
      (not (p ?x))
    """
    preds = set()
    pred_defs = re.findall(r"\((\w+)\s+\?\w+\s+-\s+" + typ + r"\)", domain)
    for p in pred_defs:
        if f"(not ({p} ?" in domain:
            preds.add(p)
    return preds


def class_is_safe(sym_class, domain, goal_atoms):
    typ = sym_class["type"]
    objs = sym_class["objects"]

    # If goal distinguishes objects → unsafe
    for g in goal_atoms:
        if sum(o in g for o in objs) == 1:
            return None, "Objects appear individually in goal"

    resource_preds = detect_resource_preds(domain, typ)

    needs_relax = len(resource_preds) > 0

    return SymmetryClass(
        obj_type=typ,
        objects=objs,
        resource_preds=resource_preds,
        needs_relaxation=needs_relax,
        reason=(
            "exclusive resource predicates detected"
            if needs_relax else
            "purely existential usage"
        )
    ), None


###############################################################################
# Analysis phase (what you asked for)
###############################################################################

def analyze(domain, problem):
    objects = extract_objects(problem)
    init_atoms = extract_init(problem)
    goal_atoms = extract_goal(problem)
    actions = extract_actions(domain)

    raw_sym = detect_symmetry_classes(objects, init_atoms, actions)

    abstractable = []
    rejected = []

    for typ, groups in raw_sym.items():
        for g in groups:
            sc, reason = class_is_safe(
                {"type": typ, "objects": g},
                domain,
                goal_atoms
            )
            if sc:
                abstractable.append(sc)
            else:
                rejected.append((typ, g, reason))

    return abstractable, rejected


###############################################################################
# Rewrite phase
###############################################################################

import re

def rewrite(domain_text, problem_text, chosen_classes):
    """
    Rewrite domain and problem PDDL files for abstraction.

    - Collapse objects of chosen types in the problem.
    - Delete exclusivity constraints `(empty ?var)` and `(not (empty ?var))`
      in all actions for parameters of the abstracted types.
    """

    new_domain = domain_text
    new_problem = problem_text

    for sc in chosen_classes:
        abs_obj = f"{sc.obj_type}abs"

        # -------------------------------
        # 1. Replace concrete objects in problem with abstract object
        # -------------------------------
        for obj in sc.objects:
            new_problem = re.sub(rf"\b{obj}\b", abs_obj, new_problem)

        # -------------------------------
        # 2. Relax resource predicates in domain
        # -------------------------------
        # Remove all "(empty ?var)" or "(not (empty ?var))" in actions
        # for parameters of the abstracted type
        # Match any action
        action_matches = list(re.finditer(r"(\(:action.*?\))", new_domain, re.S))
        new_actions = []

        for match in action_matches:
            act_text = match.group(0)

            # Pattern to remove both (empty ?var) and (not (empty ?var))
            # \?\w+ matches any PDDL variable like ?t, ?h, etc.
            act_text = re.sub(r"\(empty\s+\?\w+\)", "", act_text)
            act_text = re.sub(r"\(not\s+\(empty\s+\?\w+\)\)", "", act_text)

            # Clean up multiple spaces and empty lines
            act_text = re.sub(r"\s+", " ", act_text)
            new_actions.append(act_text)

        # Replace old actions with new relaxed actions
        def repl(_):
            return new_actions.pop(0)

        new_domain = re.sub(r"\(:action.*?\)", repl, new_domain, flags=re.S)

    return new_domain, new_problem



###############################################################################
# CLI
###############################################################################

if __name__ == "__main__":
    import argparse, json

    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--select", nargs="*", help="Types to abstract")
    parser.add_argument("--out-domain", default="abstract_domain.pddl")
    parser.add_argument("--out-problem", default="abstract_problem.pddl")

    args = parser.parse_args()

    with open(args.domain) as f:
        domain = f.read()
    with open(args.problem) as f:
        problem = f.read()

    abstractable, rejected = analyze(domain, problem)

    print("\n=== ABSTRACTABLE SYMMETRY CLASSES ===")
    for i, sc in enumerate(abstractable):
        print(f"[{i}] type={sc.obj_type}")
        print(f"    objects: {sc.objects}")
        print(f"    needs relaxation: {sc.needs_relaxation}")
        print(f"    reason: {sc.reason}")

    print("\n=== REJECTED ===")
    for typ, g, r in rejected:
        print(f"type={typ}, objects={g}, reason={r}")

    if args.select:
        chosen = [sc for sc in abstractable if sc.obj_type in args.select]
        new_domain, new_problem = rewrite(domain, problem, chosen)

        with open(args.out_domain, "w") as f:
            f.write(new_domain)
        with open(args.out_problem, "w") as f:
            f.write(new_problem)

        print("\nAbstraction applied.")
