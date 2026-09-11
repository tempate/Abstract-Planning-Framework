"""Pull finished benchmark results off the cluster and collect them into the CSV."""

import argparse
import subprocess

from scripts.collect_benchmarks import CSV_FILE, main as collect_benchmarks
from scripts.run_benchmark import RESULTS_DIR

DEFAULT_HOST = "copperhead"
DEFAULT_REMOTE_DIR = "/home/guests/dquilez/Abstract-Planning-Framework/benchmark-results/"


def main():
    args = _argument_parser().parse_args()
    pending = _pending_jobs(args.host)
    if pending and not args.force:
        print(f"{pending} job(s) still on the queue; the run is unfinished. Pass --force to pull anyway.")
        return
    _pull(args.host, args.remote_dir, args.into, args.dry_run)
    if not args.dry_run:
        collect_benchmarks(args.into, args.csv)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help="SSH host running the benchmarks")
    parser.add_argument("--remote-dir", default=DEFAULT_REMOTE_DIR, help="Results directory on that host")
    parser.add_argument("--into", default=RESULTS_DIR, help="Local directory to pull the results into")
    parser.add_argument("--csv", default=CSV_FILE, help="CSV file to collect the results into")
    parser.add_argument("--force", action="store_true", help="Pull even while jobs are still queued")
    parser.add_argument("--dry-run", action="store_true", help="Report what rsync would transfer")
    return parser


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
