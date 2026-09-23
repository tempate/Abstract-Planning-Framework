---
name: pull-requests
description: Merge a pull request in this repo, including a stacked one, and clean up afterwards. Use when asked to merge a PR, wait for CI before merging, rebase a branch whose base has merged, or tidy up branches after a merge.
---

# Pull requests

The repo **squash-merges**. A branch's commits never reach `main`: `main` gets
one new commit with a different SHA and a `(#N)` suffix. Everything below
follows from that.

## Merging

```bash
gh pr list --state open --json number,headRefName,baseRefName   # anything stacked on it?
gh pr checks <n> --watch                                        # or: gh run watch <id> --exit-status
gh pr merge <n> --squash --delete-branch                        # --delete-branch only if nothing is
```

`--delete-branch` is safe only when no open PR uses this branch as its base. If
one does, follow **Stacked branches** below instead — that mistake cannot be
undone.

**`--auto` does not wait.** No required status checks are configured on this
repo, so GitHub finds the merge conditions already met and merges at once, while
the run is still in progress. Watch the run yourself, then merge.

`MERGEABLE / UNSTABLE` from `gh pr view <n> --json mergeable,mergeStateStatus`
means the branch merges cleanly but a check is still running. It is not a
go-ahead.

## Stacked branches

Branches here stack (`main → #65 → #68`). Merging the parent closes nothing;
**deleting its branch is what closes the children**, so delete it last:

```bash
gh pr merge <parent> --squash                  # no --delete-branch
python -m scripts.restack <parent branch>      # --dry-run first to see what moves
```

`scripts.restack` rebases every open PR based on the parent onto main in a
scratch worktree, retargets it, force-pushes it with a lease, carries the PRs
stacked on those down the chain, and deletes the parent branch last. It stops,
pushing nothing of that child, if a rebase conflicts: resolve that one by hand.
Watch CI on the moved PRs before merging the next.

Check for stacked PRs before **any force-push** too: a PR based on the branch
you rewrite keeps the old commits, so run `gh pr list --base <branch>` first and
rebase those children onto the new tip.

By hand, rebase the child **by base, not by merge**: the squashed parent shares
no SHA with the copies of its commits sitting on the child, so only
`git rebase --onto main <old parent tip>` drops them. The old tip is
`origin/<parent>` until that ref goes.

A child PR whose base branch was deleted is CLOSED and unrecoverable: `gh pr
reopen` fails with `Could not open the pull request`, and `gh pr edit --base`
with `Cannot change the base branch of a closed pull request`. The number and
its review thread are gone. Recreating the deleted branch on the remote does
reopen the path, but it is three remote writes to undo one avoidable mistake —
ask before doing that, and don't rely on GitHub retargeting children by itself,
because it does not here.

## After a merge

Do this without being asked:

```bash
git checkout main && git pull
git rev-list --left-right --count origin/<branch>...<branch>   # ahead 0, or -D drops commits
git branch -D <branch>                                         # -d refuses: squash-merge hides the merge
git branch -vv                                                 # stale ones accumulate, check the rest
```

Leave branches whose PR is still open. `gh pr list --head <branch> --state all`
is the authority on whether a branch has merged; `git branch --merged main` is
not. A branch a worktree has checked out cannot be deleted — `git worktree list`
says which, and the stale scratch worktrees under `/tmp` hold several.

## Writing the PR

Say what changed and what it did, and stop. If the PR ran an experiment, the
numbers are the description — a table, not paragraphs. No commit-by-commit
walkthrough; the commit log is already there. Keep the body current: numbers
that changed after the last push are worse than no numbers.
