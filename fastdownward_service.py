import os
import subprocess
import uuid
import time


def run_fastdownward_service(
    domain_file,
    problem_file,
    abstract_domain_file=None,
    abstract_problem_file=None,
):
    # Read file contents
    domain_bytes = domain_file.read()
    problem_bytes = problem_file.read()

    # Create a unique temp directory per run
    current_directory = os.path.dirname(os.path.abspath(__file__))
    run_id = str(uuid.uuid4())
    base_dir = os.path.join(current_directory, "temp", run_id)
    os.makedirs(base_dir, exist_ok=True)

    # File paths
    domain_file_path = os.path.join(base_dir, "domain.pddl")
    problem_file_path = os.path.join(base_dir, "problem.pddl")
    sas_file_path = os.path.join(base_dir, "output.sas")
    plan_file_path = os.path.join(base_dir, "sas_plan")

    # Write domain and problem files
    with open(domain_file_path, "wb") as f:
        f.write(domain_bytes)

    with open(problem_file_path, "wb") as f:
        f.write(problem_bytes)

    # Fast Downward script path
    fast_downward_script = os.path.join(
        current_directory, "lib", "downward", "fast-downward.py"
    )

    # Run Fast Downward (concrete)
    command = [
        "python3",
        fast_downward_script,
        "--plan-file",
        plan_file_path,
        "--sas-file",
        sas_file_path,
        "--keep-sas-file",
        domain_file_path,
        problem_file_path,
        "--search",
        "astar(lmcut())",
    ]

    t_concrete_start = time.perf_counter()
    result = subprocess.run(command, capture_output=True, text=True)
    t_concrete_end = time.perf_counter()
    print("Fastdownward concrete: ",  t_concrete_end - t_concrete_start)
    if result.returncode != 0:
        print(result)
        raise RuntimeError(f"Fast Downward failed:\n{result.stderr}")

    horizon = calculate_horizon(plan_file_path)

    concrete_result = {
        "horizon": horizon,
        "sasFile": sas_file_path,
        "planFile": plan_file_path,
    }

    # Optional abstract run
    abstract_result = None
    if abstract_domain_file and abstract_problem_file:
        abstract_dir = os.path.join(base_dir, "abstract")
        os.makedirs(abstract_dir, exist_ok=True)

        abstract_domain_path = os.path.join(abstract_dir, "domain.pddl")
        abstract_problem_path = os.path.join(abstract_dir, "problem.pddl")
        abstract_sas_file = os.path.join(abstract_dir, "output.sas")
        abstract_plan_file = os.path.join(abstract_dir, "sas_plan")

        with open(abstract_domain_path, "wb") as f:
            f.write(abstract_domain_file.read())

        with open(abstract_problem_path, "wb") as f:
            f.write(abstract_problem_file.read())

        cmd = [
            "python3",
            fast_downward_script,
            "--plan-file",
            abstract_plan_file,
            "--sas-file",
            abstract_sas_file,
            "--keep-sas-file",
            abstract_domain_path,
            abstract_problem_path,
            "--search",
            "astar(lmcut())",
        ]

        t_abstract_start = time.perf_counter()
        result = subprocess.run(cmd, capture_output=True, text=True)
        t_abstract_end = time.perf_counter()
        print("Fastdownward abstract: ", t_abstract_end - t_abstract_start)
        if result.returncode != 0:
            raise RuntimeError(f"Fast Downward (abstract) failed:\n{result.stderr}")

        abstract_horizon = calculate_horizon(abstract_plan_file)

        abstract_result = {
            "horizon": abstract_horizon,
            "sasFile": abstract_sas_file,
            "planFile": abstract_plan_file,
        }

    return concrete_result, abstract_result


def calculate_horizon(plan_file_path):
    with open(plan_file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Ignore trailing cost comment
    if lines and lines[-1].startswith(";"):
        return len(lines) - 1
    return len(lines)
