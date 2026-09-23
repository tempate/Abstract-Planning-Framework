"""Pull finished benchmark results off the cluster and collect them into the CSV."""

import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from experiments.cluster import DEFAULT_HOST, current_branch, default_remote_dir, queued_jobs, remote_head, run_name
from experiments.collect import main as collect
from experiments.run import MANIFEST_NAME


def main():
    args = _argument_parser().parse_args()
    remote_dir = args.remote_dir or default_remote_dir(current_branch())
    name = run_name(args.host, remote_dir)
    pending = queued_jobs(args.host, name)
    if pending and not args.force:
        whose = name or "this user"
        print(f"{pending} job(s) of {whose} still on the queue; the run is unfinished. Pass --force to pull anyway.")
        return
    # A fresh directory each time, since rsync merges into whatever a previous
    # pull left there and collect would read that too.
    into = args.into or tempfile.mkdtemp(prefix="apf-results-")
    _pull(args.host, remote_dir, into, args.dry_run)
    if args.dry_run:
        return
    # A manifest written before it recorded the commit leaves only the remote checkout to ask.
    commit = _manifest_commit(into) or remote_head(args.host, remote_dir)
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


def _manifest_commit(results_dir):
    """The commit the run was submitted from, as its manifest records it."""
    manifest = Path(results_dir) / MANIFEST_NAME
    return json.loads(manifest.read_text(encoding="utf-8")).get("commit") if manifest.is_file() else None


def _checkout_holds(commit):
    """Whether this checkout runs the code of that commit, results committed since aside."""
    completed = subprocess.run(["git", "diff", "--name-only", commit, "HEAD"], capture_output=True, text=True)
    if completed.returncode != 0:
        # A commit this clone does not have.
        return False
    return all(Path(name).name in ("results.csv", "reports.md") for name in completed.stdout.splitlines())


def _pull(host, remote_dir, into, dry_run):
    command = ["rsync", "-az", "--info=stats1"]
    if dry_run:
        command.append("--dry-run")
    command.append(f"{host}:{remote_dir}")
    command.append(f"{into}/")
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
