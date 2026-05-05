import os
import json
import hashlib

current_directory = os.path.dirname(os.path.abspath(__file__))
BASE_JSON_DIR = os.path.join(current_directory, "temp", "jsonFiles")

# --------------------------------------------------
# SETUP
# --------------------------------------------------

def ensure_json_dir():
    os.makedirs(BASE_JSON_DIR, exist_ok=True)


# --------------------------------------------------
# HASHING (CONTENT-BASED)
# --------------------------------------------------

def hash_files(*paths):
    h = hashlib.sha256()
    for path in paths:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    return h.hexdigest()[:16]


def get_json_path(abstract_problem_path, concrete_problem_path):
    ensure_json_dir()
    run_hash = hash_files(abstract_problem_path, concrete_problem_path)
    return os.path.join(BASE_JSON_DIR, f"{run_hash}.json")


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
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


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