"""Reading a run's state off the cluster over ssh."""

import shlex
import subprocess
from pathlib import Path

DEFAULT_HOST = "copperhead"
# One worktree per branch, all under ~/apf on the cluster.
REMOTE_ROOT = "apf"


def ssh(host, command, check=False):
    """Run a shell command on the host, never stopping to ask for a password."""
    return subprocess.run(["ssh", "-o", "BatchMode=yes", host, command], capture_output=True, text=True, check=check)


def current_branch():
    completed = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, check=True)
    return completed.stdout.strip()


def default_remote_dir(branch):
    return f"{REMOTE_ROOT}/{branch}/runs/"


def remote_path(remote_dir):
    """Quote a remote directory for the shell, dropping a ~/ prefix that quoting would stop it expanding.

    ssh runs the command from the home directory, so what is left resolves to
    the same place.
    """
    return shlex.quote(remote_dir[2:] if remote_dir.startswith("~/") else remote_dir)


def remote_head(host, remote_dir):
    """The commit the checkout holding a run stands on."""
    completed = ssh(host, f"git -C {remote_path(remote_dir)} rev-parse HEAD")
    if completed.returncode != 0:
        raise SystemExit(f"Cannot read the checkout holding {host}:{remote_dir}\n{completed.stderr.strip()}")
    return completed.stdout.strip()


def run_name(host, remote_dir):
    """The Slurm job name of the run in that directory.

    CopperBench names its own directory and every array task after the run, so
    the name is there to be read even though the results do not carry it. An
    empty answer means a directory CopperBench did not write.
    """
    completed = ssh(host, f"ls -1dt {remote_path(remote_dir)}/run-*/ 2>/dev/null | head -1")
    return Path(completed.stdout.strip()).name


def queued_jobs(host, name=None, states=None):
    """Count the jobs the cluster still holds for this run, or for the user without one."""
    selector = f" --name={shlex.quote(name)}" if name else ""
    if states:
        selector += f" --states={states}"
    return int(ssh(host, f'squeue -u "$USER"{selector} -h | wc -l', check=True).stdout.strip())
