"""Pull finished benchmark results off the cluster and collect them into the CSV."""

import argparse
import shlex
import subprocess

from experiments.collect import CSV_FILE, main as collect
from experiments.run import RESULTS_DIR

DEFAULT_HOST = "copperhead"
# One worktree per branch, all under ~/apf on the cluster.
REMOTE_ROOT = "apf"


def main():
    args = _argument_parser().parse_args()
    remote_dir = args.remote_dir or _default_remote_dir(_current_branch())
    remote_head = _remote_head(args.host, remote_dir)
    local_head = _local_head()
    print(f"The run was produced by {remote_head[:9]} on {args.host}")
    if remote_head != local_head and not args.force:
        print(
            f"This checkout is on {local_head[:9]}, so {remote_dir} does not hold this branch's run. "
            "Check out the commit that produced them, or pass --force."
        )
        return
    pending = _pending_jobs(args.host)
    if pending and not args.force:
        print(f"{pending} job(s) still on the queue; the run is unfinished. Pass --force to pull anyway.")
        return
    _pull(args.host, remote_dir, args.into, args.dry_run)
    if not args.dry_run:
        collect(args.into, args.csv)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help="SSH host running the benchmarks")
    parser.add_argument(
        "--remote-dir",
        help="Results directory on that host; defaults to the worktree matching this branch, ~/apf/<branch>/runs/",
    )
    parser.add_argument("--into", default=RESULTS_DIR, help="Local directory to pull the results into")
    parser.add_argument("--csv", default=CSV_FILE, help="CSV file to collect the results into")
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


def _remote_head(host, remote_dir):
    """The commit the checkout that produced a run is standing on.

    An empty queue says a run finished, not which code ran it, and the results
    carry no record of that themselves.
    """
    path = shlex.quote(_remote_command_path(remote_dir))
    command = ["ssh", "-o", "BatchMode=yes", host, f"git -C {path} rev-parse HEAD"]
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(f"Cannot read the checkout holding {host}:{remote_dir}\n{completed.stderr.strip()}")
    return completed.stdout.strip()


def _local_head():
    completed = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
    return completed.stdout.strip()


def _pending_jobs(host):
    """Count the queued and running jobs the cluster still holds for this user."""
    command = ["ssh", "-o", "BatchMode=yes", host, 'squeue -u "$USER" -h | wc -l']
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
