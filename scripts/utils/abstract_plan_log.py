"""Persist abstract planning attempts as a compact JSON experiment log."""

import hashlib
import json
import os

from core.paths import BASE_JSON_DIR

_HASH_LENGTH = 16


def _hash_files(*paths):
    """Return a stable short hash of the contents of all supplied files."""
    digest = hashlib.sha256()
    for path in paths:
        with open(path, "rb") as source_file:
            while chunk := source_file.read(8192):
                digest.update(chunk)
    return digest.hexdigest()[:_HASH_LENGTH]


def hash_abstract_plan(abstract_atoms):
    """Return a stable short hash independent of the plan atom order."""
    normalized_plan = "\n".join(sorted(str(atom) for atom in abstract_atoms))
    return hashlib.sha256(normalized_plan.encode()).hexdigest()[:_HASH_LENGTH]


def get_plan_log_path(abstract_problem_path, concrete_problem_path, directory):
    """Return the log path and content hash for a pair of problems."""
    problem_hash = _hash_files(abstract_problem_path, concrete_problem_path)
    target_directory = os.path.join(BASE_JSON_DIR, directory)
    os.makedirs(target_directory, exist_ok=True)
    return os.path.join(target_directory, f"{problem_hash}.json"), problem_hash


def _load_plan_log(path):
    """Load a plan log, returning an empty one for absent or invalid files."""
    if not os.path.exists(path):
        return _empty_plan_log()

    try:
        with open(path, "r", encoding="utf-8") as source_file:
            content = source_file.read().strip()
        return json.loads(content) if content else _empty_plan_log()
    except json.JSONDecodeError:
        print(f"[WARNING] Corrupted JSON file: {path}, resetting.")
        return _empty_plan_log()


def _save_plan_log(path, data):
    """Write plan-log data in a human-readable JSON format."""
    with open(path, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=2)


def initialize_plan_log(
    path, problem_hash, abstract_problem_path, concrete_problem_path, abstract_symbol=None, concrete_objects=None
):
    """Create an abstract-plan log containing its mapping metadata."""
    if os.path.exists(path):
        return

    _save_plan_log(
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


def record_plan_attempt(path, abstract_atoms, success, bad_actions):
    """Record one abstract-plan realization attempt."""
    data = _load_plan_log(path)
    plan_hash = hash_abstract_plan(abstract_atoms)
    plan_entry = data["plans"].setdefault(
        plan_hash,
        {"plan": [str(atom) for atom in abstract_atoms], "success_count": 0, "failure_count": 0, "failures": []},
    )
    plan_entry.setdefault("success_count", 0)
    plan_entry.setdefault("failure_count", 0)
    plan_entry.setdefault("failures", [])

    if success:
        plan_entry["success_count"] += 1
    else:
        plan_entry["failure_count"] += 1
        plan_entry["failures"].append([str(atom) for atom in bad_actions])
    _save_plan_log(path, data)


def _empty_plan_log():
    return {"problem_hash": None, "plans": {}}
