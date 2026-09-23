"""Pull finished benchmark results off the cluster and collect them into the CSV."""

import argparse
import json
import shlex
import subprocess
import tempfile
from pathlib import Path

from experiments.collect import main as collect
from experiments.run import MANIFEST_NAME

DEFAULT_HOST = "copperhead"
# One worktree per branch, all under ~/apf on the cluster.
REMOTE_ROOT = "apf"


def main():
    args = _argument_parser().parse_args()
    remote_dir = args.remote_dir or _default_remote_dir(_current_branch())
    run_name = _remote_run_name(args.host, remote_dir)
    pending = _pending_jobs(args.host, run_name)
    if pending and not args.force:
        whose = run_name or "this user"
        print(f"{pending} job(s) of {whose} still on the queue; the run is unfinished. Pass --force to pull anyway.")
        return
    # A fresh directory each time, since rsync merges into whatever a previous
    # pull left there and collect would read that too.
    into = args.into or tempfile.mkdtemp(prefix="apf-results-")
    _pull(args.host, remote_dir, into, args.dry_run)
    if args.dry_run:
        return
    commit = _manifest_commit(into) or _remote_head(args.host, remote_dir)
    print(f"The run was produced by {commit[:9]} on {args.host}, pulled into {into}")
    if not _checkout_holds(commit) and not args.force:
        print(
            f"This checkout differs from {commit[:9]} in more than results, so it does not hold the code "
            "that produced them. Check out that commit, or pass --force."
        )
        return
    collect(into, args.csv)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help="SSH host running the benchmarks")
    parser.add_argument(
        "--remote-dir",
        help="Results directory on that host; defaults to the worktree matching this branch, ~/apf/<branch>/runs/",
    )
    parser.add_argument("--into", help="Local directory to pull the results into; defaults to a fresh temporary one")
    parser.add_argument("--csv", help="CSV file to collect the results into; defaults to the run's track's")
    parser.add_argument(
        "--force", action="store_true", help="Pull even while jobs are queued, or from a checkout on another commit"
    )
    parser.add_argument("--dry-run", action="store_true", help="Report what rsync would transfer")
    return parser


def _current_branch():
    completed = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, check=True)
    return completed.stdout.strip()


def _default_remote_dir(branch):
    return f"{REMOTE_ROOT}/{branch}/runs/"


def _remote_command_path(remote_dir):
    """Drop a ~/ prefix, which quoting would stop the remote shell expanding.

    ssh runs the command from the home directory, so what is left resolves to
    the same place.
    """
    return remote_dir[2:] if remote_dir.startswith("~/") else remote_dir


def _manifest_commit(results_dir):
    """The commit the run was submitted from, as its manifest records it."""
    manifest = Path(results_dir) / MANIFEST_NAME
    return json.loads(manifest.read_text(encoding="utf-8")).get("commit") if manifest.is_file() else None


def _remote_head(host, remote_dir):
    """The commit the checkout that produced a run stands on, for a manifest that does not record it."""
    path = shlex.quote(_remote_command_path(remote_dir))
    command = ["ssh", "-o", "BatchMode=yes", host, f"git -C {path} rev-parse HEAD"]
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(f"Cannot read the checkout holding {host}:{remote_dir}\n{completed.stderr.strip()}")
    return completed.stdout.strip()


def _checkout_holds(commit):
    """Whether this checkout runs the code of that commit, results committed since aside."""
    completed = subprocess.run(["git", "diff", "--name-only", commit, "HEAD"], capture_output=True, text=True)
    if completed.returncode != 0:
        # A commit this clone does not have.
        return False
    return all(Path(name).name in ("results.csv", "reports.md") for name in completed.stdout.splitlines())


def _remote_run_name(host, remote_dir):
    """The Slurm job name of the run in that directory.

    CopperBench names its own directory and every array task after the run, so
    the name is there to be read even though the results do not carry it. An
    empty answer means a directory CopperBench did not write.
    """
    path = shlex.quote(_remote_command_path(remote_dir))
    command = ["ssh", "-o", "BatchMode=yes", host, f"ls -1dt {path}/run-*/ 2>/dev/null | head -1"]
    completed = subprocess.run(command, capture_output=True, text=True)
    return Path(completed.stdout.strip()).name


def _pending_jobs(host, run_name=None, states=None):
    """Count the jobs the cluster still holds for this run, or for the user without one."""
    selector = f" --name={shlex.quote(run_name)}" if run_name else ""
    if states:
        selector += f" --states={states}"
    command = ["ssh", "-o", "BatchMode=yes", host, f'squeue -u "$USER"{selector} -h | wc -l']
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    return int(completed.stdout.strip())


def _pull(host, remote_dir, into, dry_run):
    command = ["rsync", "-az", "--info=stats1"]
    if dry_run:
        command.append("--dry-run")
    command.append(f"{host}:{remote_dir}")
    command.append(f"{into}/")
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
