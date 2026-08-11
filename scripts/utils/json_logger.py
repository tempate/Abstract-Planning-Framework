import os
import json
import hashlib
from core.repo import BASE_JSON_DIR

# --------------------------------------------------
# SETUP
# --------------------------------------------------

def ensure_json_dir():
    os.makedirs(BASE_JSON_DIR, exist_ok=True)


# --------------------------------------------------
# HASHING
# --------------------------------------------------

def hash_files(*paths):
    h = hashlib.sha256()
    for path in paths:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    return h.hexdigest()[:16]

def hash_plan(abstract_atoms):
    normalized = sorted(str(a) for a in abstract_atoms)
    joined = "\n".join(normalized)
    return hashlib.sha256(joined.encode()).hexdigest()[:16]

def get_json_path(abstract_problem_path, concrete_problem_path, dir):
    problem_hash = hash_files(abstract_problem_path, concrete_problem_path)

    target_dir = os.path.join(BASE_JSON_DIR, dir)
    os.makedirs(target_dir, exist_ok=True)

    return os.path.join(target_dir, f"{problem_hash}.json"), problem_hash

def get_json_path_more(abstract_problem_path, concrete_problem_path, abstract_symbol, concrete_objects):
    ensure_json_dir()

    problem_hash = hashlib.sha256(
        (
            abstract_problem_path +
            concrete_problem_path +
            abstract_symbol +
            ",".join(sorted(concrete_objects or []))
        ).encode()
    ).hexdigest()[:16]

    return os.path.join(BASE_JSON_DIR, f"{problem_hash}.json"), problem_hash

# --------------------------------------------------
# FILE HANDLING
# --------------------------------------------------

def init_json_file(path, problem_hash):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({
                "problem_hash": problem_hash,
                "runs": []
            }, f, indent=2)

def load_json(path):
    if not os.path.exists(path):
        return {"problem_hash": None, "plans": {}}

    try:
        with open(path, "r") as f:
            content = f.read().strip()

            if not content:
                # empty file → reset
                return {"problem_hash": None, "plans": {}}

            return json.loads(content)

    except json.JSONDecodeError:
        # corrupted file → reset (or back it up)
        print(f"[WARNING] Corrupted JSON file: {path}, resetting.")
        return {"problem_hash": None, "plans": {}}


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def init_plan_file(path, problem_hash, abstract_problem_path, concrete_problem_path,
                   abstract_symbol=None, concrete_objects=None):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({
                "problem_hash": problem_hash,

                # NEW METADATA
                "abstract_problem_file": os.path.basename(abstract_problem_path),
                "concrete_problem_file": os.path.basename(concrete_problem_path),

                "abstract_symbol": abstract_symbol,
                "concrete_objects": concrete_objects or [],

                "plans": {}
            }, f, indent=2)

# --------------------------------------------------
# RUN HANDLING
# --------------------------------------------------

def start_new_run(path, mode):
    data = load_json(path)

    run_entry = {
        "mode": mode,
        "steps": []
    }

    data["runs"].append(run_entry)
    save_json(path, data)


def append_step(path, abstract_atoms, success, bad_actions=None):
    data = load_json(path)

    if not data["runs"]:
        raise RuntimeError("No run initialized. Call start_new_run() first.")

    entry = {
        "abstract_plan": [str(a) for a in abstract_atoms],
        "success": success,
        "bad_actions": [str(a) for a in bad_actions] if bad_actions else []
    }

    data["runs"][-1]["steps"].append(entry)

    save_json(path, data)

def update_plan(path, abstract_atoms, success, bad_actions, mode):
    data = load_json(path)

    plan_hash = hash_plan(abstract_atoms)

    if plan_hash not in data["plans"]:
        data["plans"][plan_hash] = {
            "plan": [str(a) for a in abstract_atoms],
            "modes": {}
        }

    plan_entry = data["plans"][plan_hash]

    if mode not in plan_entry["modes"]:
        plan_entry["modes"][mode] = {
            "success_count": 0,
            "failure_count": 0,
            "failures": []
        }

    mode_entry = plan_entry["modes"][mode]

    if success:
        mode_entry["success_count"] += 1
    else:
        mode_entry["failure_count"] += 1
        mode_entry["failures"].append([str(a) for a in bad_actions])

    save_json(path, data)
