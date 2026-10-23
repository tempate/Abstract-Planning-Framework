---
name: pull-requests
description: Open, describe, stack, merge and clean up pull requests in this repo. Use when asked to open or update a PR, write or rewrite its description or results, add its before/after figures, stack a branch on another, wait for CI and merge, rebase a branch whose base has merged, or tidy up branches after a merge.
---

# Pull requests

The repo **squash-merges**. A branch's commits never reach `main`. `main` gets one
new commit with a different SHA and a `(#N)` suffix, and everything below follows
from that.

## Opening a PR

An experiment PR, one whose results come from the cluster, opens as a draft and
stays one until its results are pushed:

```bash
gh pr create --draft --base <base> --title "<title>" --body-file <draft>
```

A PR without a cluster run, such as a refactor or a rename, opens ready. Watch CI in
the background, never in the foreground:

```bash
gh pr checks <n> --watch --interval 30
```

## Writing the description

Say what changed and what it did, then stop. A reviewer reads the diff and the
commit log, so leave out commit walkthroughs, implementation notes and anything
the code already says. Prefer a table of numbers over sentences about them, and
never add a paragraph interpreting the numbers.

- No H1, since the title is the heading.
- Write the prose without passive voice, colons or semicolons.
- Name the modes ASP, ASPᵅ, LAMA, LAMAᵅ, LMcut, LMcutᵅ, M&S and M&Sᵅ, as the paper does.
- Keep the `🤖 Generated with [Claude Code](https://claude.com/claude-code)` footer.
- Draft the body in the scratchpad and apply it with `gh pr edit <n> --body-file <draft>`. Never commit it to the repo.
- Daniel edits descriptions too, so fetch the live body with `gh pr view <n> --json body -q .body` before every edit and change only your part.

## Experiment PRs

Until the run is collected, the description is one short paragraph on what the PR
changes, then `## Results` with the word `Pending` and what was submitted.

Once the results are pushed and the PR is ready, the `## Results` section holds, in
this order:

1. The before/after figures, one per track kind. Each mirrors the paper's figure for that track, problems solved over time and runtime per problem, with every mode the run compares. Before (main) on the left, After on the right, at equal height. On the optimal tracks the scatter points take their colour from the extra actions over the optimum, as in the paper.
2. A table of plans found, base → PR, with one row per mode and one column per track.
3. Three to six short bullets. Gains and losses with the domains behind them, runtime and plan length on the problems both versions solve, and anything a reader would otherwise misread.
4. One `**Verification:**` line saying what ran, at which commit, and that nothing was killed.

"Before" is the PR's base, which is `main` or, for a stacked PR, the PR below it. Compare the
same problems and classes on both sides. For a best-class run, keep only the
abstract rows the run's manifest lists, as the `cluster-benchmarks` skill explains,
and say when the base used a different class. For a run over a subset of problems,
report on the problems the subset was meant to cover, not on whatever extra the
submission swept in.

Check a figure's definitions before trusting it, by drawing the "before" half from
the paper's own CSV and comparing it with the coordinates in `main.tex`. Render it
as a standalone PDF from the paper's preamble, crop it, convert it to PNG, and name
it `<n>-<track kind>-before-after.png`. Daniel uploads the image by dragging it into
the description, so leave an HTML comment where each one goes:

```markdown
<!-- 130-sat-before-after.png: before (main) left, after right -->
```

## Merging

```bash
gh pr list --state open --json number,headRefName,baseRefName   # anything stacked on it?
gh pr checks <n> --watch --interval 30                          # in the background
gh pr merge <n> --squash --delete-branch                        # only if nothing is stacked on it
```

`--delete-branch` is safe only when no open PR uses the branch as its base. If one
does, merge with `gh stack merge` below, since deleting a base cannot be undone.
It also deletes the local branch and switches to `main`.

**`--auto` does not wait.** The repo has no required checks, so GitHub merges at
once while CI is still running. Watch the run, then merge.

`MERGEABLE / UNSTABLE` from `gh pr view <n> --json mergeable,mergeStateStatus` means
the branch merges cleanly but a check is failing or still running. Find out which
before merging.

## Stacked branches

Stacks use GitHub's native stacked pull requests through the `gh stack` extension
(`gh extension install github/gh-stack`). Each PR targets the branch below it.

```bash
gh stack link <bottom-pr> <next-pr> ...     # bottom first
gh stack add <branch>                       # a new branch on top of the current one
gh stack submit                             # push every branch, open or update its PR
gh stack view                               # the stack, with each PR's state
gh stack rebase && gh stack push            # carry a rewritten branch up the stack
```

`gh stack link` refuses to drop a PR from an existing stack, merged ones included,
so list every PR the stack already holds. When a merged PR's branch is gone, it
also tries to retarget the next PR onto it and prints a harmless
`HTTP 422 ... PullRequest.base is invalid`. Check the bases afterwards with
`gh pr view <n> --json baseRefName`.

Merge from the bottom up, after CI passes on the PR being merged:

```bash
gh stack merge <pr> --squash                # merges every PR up to and including <pr>
gh stack sync                               # fetch, rebase what is left, prune merged branches
```

After a stacked merge GitHub retargets the next PR to the stack's base. Sometimes
it also rebases that PR onto the squash commit and sometimes it leaves it
conflicting. Fetch before rebasing anything. If `origin/<branch>` already holds the
same tree as a local rebase would, take it with `git reset --hard origin/<branch>`
rather than force-pushing over it. Otherwise rebase the branch's own commits onto
`main` with `git rebase --onto origin/main <old base> <branch>`, and push with
`--force-with-lease=<branch>:<sha you read>`.

A child PR whose base branch was deleted is CLOSED for good. `gh pr reopen` and
`gh pr edit --base` both fail. Never delete a stacked branch by hand.

## After a merge

Do this without being asked:

```bash
git checkout main && git pull
git rev-list --left-right --count origin/<branch>...<branch>   # ahead 0, or -D drops commits
git branch -D <branch>                                         # -d refuses, the squash hides the merge
git branch -vv                                                 # stale branches pile up
```

Leave branches whose PR is still open. `gh pr list --head <branch> --state all`
says whether a branch merged, and `git branch --merged main` cannot. A branch a
worktree has checked out cannot be deleted. `git worktree list` shows which, and
`git worktree prune` clears the entries whose directories are gone.
