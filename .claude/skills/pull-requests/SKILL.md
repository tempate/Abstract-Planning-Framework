---
name: pull-requests
description: Merge a pull request in this repo, stack PRs with gh stack, and clean up afterwards. Use when asked to merge a PR, stack a branch on another, wait for CI before merging, rebase a branch whose base has merged, or tidy up branches after a merge.
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
one does, the PR is part of a stack: merge it with `gh stack merge` below
instead — deleting a base by hand cannot be undone.

**`--auto` does not wait.** No required status checks are configured on this
repo, so GitHub finds the merge conditions already met and merges at once, while
the run is still in progress. Watch the run yourself, then merge.

`MERGEABLE / UNSTABLE` from `gh pr view <n> --json mergeable,mergeStateStatus`
means the branch merges cleanly but a check ## Stacked branches

Stacks use GitHub's native stacked pull requests (public preview) through the
`gh stack` extension, installed with `gh extension install github/gh-stack`.
Each PR targets the branch below it, and GitHub shows the stack on every PR.

```bash
gh stack link <bottom-pr> <next-pr> ...     # turn open PRs into a stack, bottom first
gh stack checkout <pr>                      # track that stack locally
gh stack add <branch>                       # start a new branch on top of the current one
gh stack submit                             # push every branch, open or update its PR
gh stack view                               # the stack, with each PR's state
```

Merge from the bottom up, and watch CI on every PR you merge first:

```bash
gh stack merge <pr> --squash                # merges every PR up to and including <pr>
gh stack sync                               # fetch, rebase what is left, prune merged branches
```

The PRs above the merged one stay open, retarget to the stack's base and get
rebased by GitHub. That replaces `scripts.restack`, which is only for a stack
made without `gh stack`. The first stacked merge here is still to come, so check
`gh stack view` and the remaining PRs' bases after it.

Rewriting a branch in the middle of a stack leaves the ones above on its old
commits. `gh stack rebase` carries the change up the stack; then `gh stack push`.

A child PR whose base branch was deleted is CLOSED and unrecoverable: `gh pr
reopen` fails with `Could not open the pull request`, and `gh pr edit --base`
with `Cannot change the base branch of a closed pull request`. Never delete a
stacked branch by hand.

en by itself,
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
