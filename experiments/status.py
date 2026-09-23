"""Report how a cluster run is going, without pulling it."""

import argparse
import json
import shlex
import subprocess

from experiments.fetch import (
    DEFAULT_HOST,
    _current_branch,
    _default_remote_dir,
    _pending_jobs,
    _remote_command_path,
    _remote_run_name,
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


def main():
    args = _argument_parser().parse_args()
    remote_dir = args.remote_dir or _default_remote_dir(_current_branch())
    run_name = _remote_run_name(args.host, remote_dir)
    pending = _pending_jobs(args.host, run_name)
    running = _pending_jobs(args.host, run_name, states="RUNNING")
    summary = _remote_summary(args.host, remote_dir)
    _report(run_name or remote_dir, pending, running, summary)


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=DEFAULT_HOST, help="SSH host running the benchmarks")
    parser.add_argument(
        "--remote-dir",
        help="Results directory on that host; defaults to the worktree matching this branch, ~/apf/<branch>/runs/",
    )
    return parser


def _remote_summary(host, remote_dir):
    """Count the results written so far, and what each of them says."""
    path = shlex.quote(_remote_command_path(remote_dir))
    command = ["ssh", "-o", "BatchMode=yes", host, f"python3 -c {shlex.quote(REMOTE_SUMMARY)} {path}"]
    completed = subprocess.run(command, capture_output=True, text=True)
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


if __name__ == "__main__":
    main()
