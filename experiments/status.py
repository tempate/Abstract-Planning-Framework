"""Report how a cluster run is going, without pulling it."""

import argparse
import json
import shlex

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


def main():
    args = _argument_parser().parse_args()
    remote_dir = args.remote_dir or default_remote_dir(current_branch())
    name = run_name(args.host, remote_dir)
    pending = queued_jobs(args.host, name)
    running = queued_jobs(args.host, name, states="RUNNING")
    summary = _remote_summary(args.host, remote_dir)
    _report(name or remote_dir, pending, running, summary)


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


if __name__ == "__main__":
    main()
