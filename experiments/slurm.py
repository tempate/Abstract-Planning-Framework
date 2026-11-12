"""One Slurm array task per problem: submitting them, running one, and reading what they found."""

import subprocess

from experiments.run import RESULTS_DIR


def submit(directory, names, task_command, job_name, partition, memory, minutes):
    """Write the problem names and submit one array task per name, which task_command reads by its index."""
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "tasks.txt").write_text("".join(f"{name}\n" for name in names), encoding="utf-8")
    if not names:
        return
    command = [
        "sbatch",
        f"--array=0-{len(names) - 1}",
        f"--partition={partition}",
        "--cpus-per-task=1",
        f"--mem={memory}",
        f"--time={minutes}",
        f"--job-name={job_name}",
        f"--output={directory}/%a.out",
        f"--wrap={task_command} --task $SLURM_ARRAY_TASK_ID",
    ]
    subprocess.run(command, cwd=RESULTS_DIR.parent, check=True)


def run_task(directory, index, find_outcome):
    """Record what find_outcome says of the task's problem, unless an earlier run of the task already did."""
    name = (directory / "tasks.txt").read_text(encoding="utf-8").splitlines()[index]
    # Named after the problem, not the index, since a later submit renumbers the tasks.
    result = directory / "outcomes" / f"{name}.tsv"
    # Slurm requeues tasks, sometimes after they finished, and the outcome stands.
    if result.is_file():
        return
    outcome = find_outcome(name)
    result.parent.mkdir(parents=True, exist_ok=True)
    result.write_text(f"{name}\t{outcome}\n", encoding="utf-8")


def outcomes(directory):
    """Each problem's outcome, by its name."""
    found = {}
    for result in sorted((directory / "outcomes").rglob("*.tsv")):
        name, _, outcome = result.read_text(encoding="utf-8").strip().partition("\t")
        found[name] = outcome
    return found
