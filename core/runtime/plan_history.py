"""Persist planning runs and plan outcomes as compact JSON histories."""

import hashlib
import json
import os

from core.paths import BASE_JSON_DIR


_HASH_LENGTH = 16


def hash_files(*paths):
    """Return a stable short hash of the contents of all supplied files."""
    digest = hashlib.sha256()
    for path in paths:
        with open(path, "rb") as source_file:
            while chunk := source_file.read(8192):
                digest.update(chunk)
    return digest.hexdigest()[:_HASH_LENGTH]


def hash_plan(abstract_atoms):
    """Return a stable short hash independent of the plan atom order."""
    normalized_plan = "\n".join(sorted(str(atom) for atom in abstract_atoms))
    return hashlib.sha256(normalized_plan.encode()).hexdigest()[:_HASH_LENGTH]


def get_json_path(abstract_problem_path, concrete_problem_path, directory):
    """Return the history path and content hash for a pair of problems."""
    problem_hash = hash_files(abstract_problem_path, concrete_problem_path)
    target_directory = os.path.join(BASE_JSON_DIR, directory)
    os.makedirs(target_directory, exist_ok=True)
    return os.path.join(target_directory, f"{problem_hash}.json"), problem_hash


def load_json(path):
    """Load JSON data, returning an empty plan history for absent or invalid files."""
    if not os.path.exists(path):
        return _empty_plan_history()

    try:
        with open(path, "r", encoding="utf-8") as source_file:
            content = source_file.read().strip()
        return json.loads(content) if content else _empty_plan_history()
    except json.JSONDecodeError:
        print(f"[WARNING] Corrupted JSON file: {path}, resetting.")
        return _empty_plan_history()


def save_json(path, data):
    """Write JSON history data in a human-readable format."""
    with open(path, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=2)


def init_plan_file(
    path,
    problem_hash,
    abstract_problem_path,
    concrete_problem_path,
    abstract_symbol=None,
    concrete_objects=None,
):
    """Create a plan-outcome history with the mapping metadata needed to read it."""
    if os.path.exists(path):
        return

    save_json(
        path,
        {
            "problem_hash": problem_hash,
            "abstract_problem_file": os.path.basename(abstract_problem_path),
            "concrete_problem_file": os.path.basename(concrete_problem_path),
            "abstract_symbol": abstract_symbol,
            "concrete_objects": concrete_objects or [],
            "plans": {},
        },
    )


def update_plan(path, abstract_atoms, success, bad_actions, mode):
    """Record the outcome of one plan for a planner mode."""
    data = load_json(path)
    plan_hash = hash_plan(abstract_atoms)
    plan_entry = data["plans"].setdefault(
        plan_hash,
        {"plan": [str(atom) for atom in abstract_atoms], "modes": {}},
    )
    mode_entry = plan_entry["modes"].setdefault(
        mode,
        {"success_count": 0, "failure_count": 0, "failures": []},
    )

    if success:
        mode_entry["success_count"] += 1
    else:
        mode_entry["failure_count"] += 1
        mode_entry["failures"].append([str(atom) for atom in bad_actions])
    save_json(path, data)


def _empty_plan_history():
    return {"problem_hash": None, "plans": {}}
