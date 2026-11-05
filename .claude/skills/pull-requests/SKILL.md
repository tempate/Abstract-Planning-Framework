---
name: pull-requests
description: Open, describe, stack, merge and clean up pull requests in this repo. Use when asked to open or update a PR, write or rewrite its description or results, add its before/after figures, stack a branch on another, wait for CI and merge, rebase a branch whose base has merged, or tidy up branches after a merge.
---

# Pull requests

The repo **squash-merges**. A branch's commits never reach `main`. `main` gets one
new commit with a different SHA and a `(#N)` suffix, and everything below follows
from that.

## Opening a PR

The title names the change in a few plain words, as an imperative, such as "Relax
groundings instead of schemas". It describes what the code now does, not how.

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

Once the results are pushed and the PR is ready, the `## Results` section holds two
small tables and nothing else, as #146 and #147 do:

1. **Plans found.** One row per abstract mode the run submitted and one column per track
   it touched, such as `sat symmetries` or `opt resources`. Each cell reads `base → PR`,
   with the larger number in bold. A mode that does not run on a track leaves its cell empty.
2. **Median runtime.** The same rows and columns. Each cell reads `base → PR` in seconds
   with one decimal, the median over the problems both sides solve.

```markdown
| Plans found | sat resources | opt resources |
|---|---|---|
| ASPᵅ | 90 → **92** | **126** → 119 |
| LAMAᵅ | **125** → 121 | |
| LMcutᵅ | | **138** → 131 |

| Median runtime | sat resources | opt resources |
|---|---|---|
| ASPᵅ | 15.4 → 15.2 s | 15.3 → 17.3 s |
| LAMAᵅ | 17.7 → 17.3 s | |
| LMcutᵅ | | 10.7 → 12.7 s |
```

Leave out figures, baseline rows, sentences about the numbers and tables of runs.

"Before" is the PR's base, which is `main` or, for a stacked PR, the PR below it. Compare the
same problems and classes on both sides. For a best-class run, keep only the
abstract rows the run's manifest lists, as the `cluster-benchmarks` skill explains.
For a run over a subset of problems, report on the problems the subset was meant to
cover, not on whatever extra the submission swept in.

Descriptions carry no figure unless Daniel asks for one. `experiments.figure` draws
the paper's sat, opt or unsat figure, problems solved or proved over time and runtime
per problem with every mode, for the base and the branch side by side:

```bash
python -m experiments.figure opt --base origin/main --branch HEAD \
  --manifests /tmp/apf-results-<a>/manifest.json /tmp/apf-results-<b>/manifest.json \
  --out 130-opt-before-after.png
```

`--manifests` limits the branch's abstract modes to the classes its runs submitted.
For a stacked PR, pass `--base <the base branch> --base-label '#<n>'` and the base's
own manifests as `--base-manifests`. The script needs the paper checked out next to
the repository, or `--paper`, plus `pdflatex`, `pdfcrop` and `pdftoppm`. After
changing it, check that the base half reproduces the coordinates in the paper's
`main.tex` from the `main` commit the paper's figure came from.

When he asks for a figure, he uploads it by dragging it into the description, so
leave an HTML comment where it goes:

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
git branch -D <branch>                                         # if gh did not delete it, -d refuses
git branch -vv                                                 # stale branches pile up
```

Leave branches whose PR is still open. `gh pr list --head <branch> --state all`
says whether a branch merged, and `git branch --merged main` cannot. A branch a
worktree has checked out cannot be deleted. `git worktree list` shows which, and
`git worktree prune` clears the entries whose directories are gone.

Then clean the cluster. Remove every checkout the PR ran from, the branch's own and
its `<branch>-<track>` copies, together with their branches in the bare repo. Their
results are in `main` by now, so only the raw run directories go with them. Check
first that none of their jobs is queued and that none has local changes:

```bash
ssh -o BatchMode=yes copperhead 'squeue -u dquilez -h | wc -l; git -C ~/apf/.bare worktree list'
ssh -o BatchMode=yes copperhead 'for b in <branch> <branch>-<track>; do
  git -C ~/apf/.bare worktree remove --force ~/apf/$b && git -C ~/apf/.bare branch -D $b; done'
```

Leave the checkouts of PRs that are still open, and `~/apf/main`.
