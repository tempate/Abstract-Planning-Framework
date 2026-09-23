"""Move the PRs stacked on a squash-merged branch onto main, then delete the branch.

Run it after `gh pr merge <n> --squash` without --delete-branch. Every open PR
based on the merged branch is rebased onto main by base, since the squash shares
no commit with the copies its children carry, retargeted to main and
force-pushed with a lease; the PRs stacked on those follow them down the chain.
The merged branch is deleted last, because deleting it first closes its
children for good.
"""

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def main():
    args = _argument_parser().parse_args()
    merged = _gh("pr", "list", "--head", args.branch, "--state", "merged", "--json", "number")
    if not merged:
        raise SystemExit(f"No merged PR has {args.branch} as its head; merge it with --squash first.")

    _git("fetch", "--quiet", "--prune", "origin")
    if not _ref_exists(f"refs/remotes/origin/{args.branch}"):
        raise SystemExit(f"{args.branch} is already gone from origin, and any PR based on it was closed with it.")
    old_tip = _git("rev-parse", f"origin/{args.branch}")
    _restack_children(args.branch, old_tip, "origin/main", retarget=True, dry_run=args.dry_run)

    if args.dry_run:
        print(f"would delete {args.branch}")
        return
    _git("push", "--quiet", "origin", "--delete", args.branch)
    if _local_branch_exists(args.branch):
        _git("branch", "-D", args.branch)
    print(f"deleted {args.branch}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("branch", help="The head branch of the PR just squash-merged")
    parser.add_argument("--dry-run", action="store_true", help="Say what would move, and change nothing")
    return parser


def _restack_children(parent, parent_old_tip, new_base, retarget, dry_run):
    """Rebase each PR based on the parent from its old tip onto the new base, and so on down."""
    children = _gh("pr", "list", "--base", parent, "--state", "open", "--json", "number,headRefName")
    for child in children:
        branch = child["headRefName"]
        old_tip = _git("rev-parse", f"origin/{branch}")
        if dry_run:
            where = "main" if retarget else parent
            print(f"would rebase #{child['number']} ({branch}) onto {where}")
            _restack_children(branch, old_tip, old_tip, retarget=False, dry_run=True)
            continue

        new_tip = _rebased(old_tip, parent_old_tip, new_base, branch)
        # Retarget before pushing, so the PR never shows main's commits as its own.
        if retarget:
            _gh("pr", "edit", str(child["number"]), "--base", "main", parse=False)
        _git("push", "--quiet", f"--force-with-lease={branch}:{old_tip}", "origin", f"{new_tip}:refs/heads/{branch}")
        _move_local_branch(branch, new_tip)
        print(f"moved #{child['number']} ({branch}) to {new_tip[:7]}")

        _restack_children(branch, old_tip, new_tip, retarget=False, dry_run=False)


def _rebased(tip, old_base, new_base, branch):
    """Rebase the commits between old_base and tip onto new_base in a scratch worktree, and return the result."""
    with tempfile.TemporaryDirectory(prefix="apf-restack-") as directory:
        worktree = Path(directory) / "worktree"
        _git("worktree", "add", "--quiet", "--detach", str(worktree), tip)
        try:
            rebase = subprocess.run(
                ["git", "-C", str(worktree), "rebase", "--quiet", "--onto", new_base, old_base],
                capture_output=True,
                text=True,
            )
            if rebase.returncode != 0:
                subprocess.run(["git", "-C", str(worktree), "rebase", "--abort"], capture_output=True)
                raise SystemExit(f"{branch} does not rebase cleanly; nothing of it was pushed.\n{rebase.stdout}")
            return _git("-C", str(worktree), "rev-parse", "HEAD")
        finally:
            _git("worktree", "remove", "--force", str(worktree))


def _move_local_branch(branch, tip):
    """Point a local copy of the branch at its new tip, unless a worktree has it checked out."""
    if not _local_branch_exists(branch):
        return
    moved = subprocess.run(["git", "branch", "--force", branch, tip], capture_output=True, text=True)
    if moved.returncode != 0:
        print(f"  left the local {branch} alone, it is checked out: {moved.stderr.strip()}")


def _local_branch_exists(branch):
    return _ref_exists(f"refs/heads/{branch}")


def _ref_exists(ref):
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref], capture_output=True).returncode == 0


def _git(*arguments):
    return subprocess.run(["git", *arguments], capture_output=True, text=True, check=True).stdout.strip()


def _gh(*arguments, parse=True):
    output = subprocess.run(["gh", *arguments], capture_output=True, text=True, check=True).stdout
    return json.loads(output) if parse else output


if __name__ == "__main__":
    main()
