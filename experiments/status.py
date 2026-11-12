"""Report how a cluster run is going, without pulling it."""

import argparse
import json
import re
import shlex
from collections import Counter, defaultdict

from experiments.cluster import (
    DEFAULT_HOST,
    current_branch,
    default_remote_dir,
    queued_jobs,
    remote_path,
    run_name,
    ssh,
)

# Runs on the cluster's own python3, so it may not import anything this
# repository ships, and the worktree's conda env need not be active.
REMOTE_SUMMARY = """
import collections, json, pathlib, sys

root = pathlib.Path(sys.argv[1])
counts = collections.Counter()
for path in root.rglob("*.json"):
    if path.name in ("metadata.json", "manifest.json"):
        continue
    try:
        result = json.loads(path.read_text())
    except ValueError:
        counts["unreadable"] += 1
        continue
    if "status" in result:
        counts[result["status"]] += 1
manifest = root / "manifest.json"
expected = len(json.loads(manifest.read_text())["expected_results"]) if manifest.is_file() else 0
print(json.dumps({"expected": expected, "counts": counts}))
"""


# The states every recent run is counted in, in the order the summary prints them.
COLUMNS = ("pending", "running", "done", "skipped", "failed", "oom", "timeout", "cancelled")
# What sacct calls the outcomes of jobs that have ended. A job still queued or
# running is counted from squeue instead, since sacct keeps stale records of jobs
# that left the queue long ago.
ENDED = {"COMPLETED": "done", "FAILED": "failed", "OUT_OF_MEMORY": "oom", "TIMEOUT": "timeout"}


def main():
    args = _argument_parser().parse_args()
    if args.all:
        command = (
            "squeue -u \"$USER\" -h -r -o '%j|%T'; echo ---; "
            f'sacct -u "$USER" -S now-{args.days}days -X -n -P -o JobName,State,ExitCode,WorkDir'
        )

        completed = ssh(args.host, command, check=True)
        queue, accounting = completed.stdout.split("---\n", 1)
        _report_runs(summarize_runs(queue, accounting))
        return

    remote_dir = args.remote_dir or default_remote_dir(current_branch())
    name = run_name(args.host, remote_dir)
    pending = queued_jobs(args.host, name)
    running = queued_jobs(args.host, name, states="RUNNING")

    summary = _remote_summary(args.host, remote_dir)
    _report(name or remote_dir, pending, running, summary)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help="SSH host running the benchmarks")
    parser.add_argument("--all", action="store_true", help="Summarise every run of the last days instead of one")
    parser.add_argument("--days", type=int, default=2, help="How far back --all looks")
    parser.add_argument(
        "--remote-dir",
        help="Results directory on that host; defaults to the worktree matching this branch, ~/apf/<branch>/runs/",
    )
    return parser


def _remote_summary(host, remote_dir):
    """Count the results written so far, and what each of them says."""
    completed = ssh(host, f"python3 -c {shlex.quote(REMOTE_SUMMARY)} {remote_path(remote_dir)}")
    if completed.returncode != 0:
        raise SystemExit(f"Cannot read {host}:{remote_dir}\n{completed.stderr.strip()}")
    return json.loads(completed.stdout)


def _report(run, pending, running, summary):
    counts = summary["counts"]
    written = sum(counts.values())
    expected = summary["expected"]

    print(f"{run}: {pending} job(s) on the queue, {written} of {expected or '?'} results written")
    for status, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {status:<24} {count}")

    # A job writes its result only once it starts, so a result still saying
    # running with no running job behind it belongs to a job killed before it
    # could write the outcome. A queued job has no result yet to compare.
    stranded = counts.get("running", 0) - running
    if stranded > 0:
        print(f"{stranded} result(s) left running with no job running; those jobs were killed")


def summarize_runs(queue, accounting):
    """Each run's checkout and its jobs by state, from squeue's and sacct's output."""
    checkouts = {}
    counts = defaultdict(Counter)

    for line in queue.splitlines():
        name, state = line.split("|")
        if state in ("PENDING", "RUNNING"):
            counts[name][state.lower()] += 1

    for line in accounting.splitlines():
        name, state, exit_code, workdir = line.split("|")
        match = re.search(r"/apf/([^/]+)/runs", workdir)
        if match:
            checkouts[name] = match.group(1)
        if state.startswith("CANCELLED"):
            counts[name]["cancelled"] += 1
        elif state == "FAILED" and exit_code == "4:0":
            # CopperBench refuses to start a task twice and exits with 4, leaving the first result intact.
            counts[name]["skipped"] += 1
        elif state in ENDED:
            counts[name][ENDED[state]] += 1

    return {name: (checkouts.get(name, "?"), counts[name]) for name in sorted(counts, reverse=True)}


def _report_runs(runs):
    print(f"{'run':<28} {'checkout':<40} " + " ".join(f"{column:>9}" for column in COLUMNS))
    for name, (checkout, counts) in runs.items():
        print(f"{name:<28} {checkout:<40} " + " ".join(f"{counts[column]:>9}" for column in COLUMNS))


if __name__ == "__main__":
    main()
