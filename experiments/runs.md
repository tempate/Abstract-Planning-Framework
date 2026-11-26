# What ran where

`results.csv` records no commit, so each row below goes back to the PR whose merge last changed its status or runtime. State of main at #245 on 2026-11-25.

Latest code means main at #221. The PRs after #181 that change a result are #185 (opt fallback), #203 (fixed PDDL Symmetries seed, so the classes change), #206 (distinct inequalities, rerun on mprime and four HTG domains only) and #209 with #217 (one-shot on a partial grounding). #238 drops the 10 opt resources problems with no class to collapse, so their rows are gone rather than stale. #239 finds symmetries before grounding on every track, which only the HTG rows did before. #223 adds the Powerlifted rows. #225 adds LMcut with symmetry pruning, whose HTG rows on the 177 ungroundable problems are copies of LMcut's. #227 adds LAMA with symmetry pruning, whose HTG rows there are copies of LAMA's. #245 rescans the IPC classes and reruns the IPC baselines on the new lists. The others since then are refactors or touch no track. Fast Downward has not moved since #12, so the LAMA and LMcut rows hold on any commit. Broadwell is the default partition since 2026-11-25, so every row that ran on sunnycove is stale.

| Status | Meaning |
|---|---|
| ✅ **current** | latest relevant code, every class, on broadwell |
| ⚠️ **partly stale** | latest relevant code, but only the best class or partly on sunnycove |
| ❌ **stale** | lacks a result-changing PR on some rows, or ran on sunnycove |

| Classes | Meaning |
|---|---|
| all | every class `classes.txt` lists |
| best | one class per problem, the best of an earlier run |

## HTG

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ❌ **stale** | 3406 | 107 / 243 | #209 | sunnycove | |
| | ASPᵅ | ❌ **stale** | 3406 | best | #212 | sunnycove | #209 |
| | ASP | ❌ **stale** | 443 | | #212 | sunnycove | |
| | LAMA | ⚠️ **partly stale** | 443 | | #157, #196 | broadwell, sunnycove | |
| | LAMA with symmetry pruning | ✅ **current** | 443 | | #227 | broadwell | |
| | Powerliftedᵅ | ✅ **current** | 3406 | all | #223 | broadwell | |
| | Powerlifted | ✅ **current** | 443 | | #223 | broadwell | |
| opt | LMcutᵅ | ❌ **stale** | 3406 | 2 / 239 | #209, #196–#206 | sunnycove | #209 |
| | ASPᵅ | ❌ **stale** | 3406 | best | #212 | sunnycove | #209 |
| | ASP | ❌ **stale** | 443 | | #212 | sunnycove | |
| | LMcut | ❌ **stale** | 443 | | #157, #196 | sunnycove | |
| | LMcut with symmetry pruning | ✅ **current** | 443 | | #225 | broadwell | |
| | Powerliftedᵅ | ✅ **current** | 3406 | all | #223 | broadwell | |
| | Powerlifted | ✅ **current** | 443 | | #223 | broadwell | |

## IPC symmetries

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ❌ **stale** | 2478 | best | #181, #206 | sunnycove | #203, #209, #239, #245 |
| | ASPᵅ | ❌ **stale** | 2478 | best | #181, #206 | sunnycove | #203, #209, #239, #245 |
| | ASP | ❌ **stale** | 677 | | #245 | sunnycove | |
| | LAMA | ❌ **stale** | 677 | | #245 | sunnycove | |
| | LAMA with symmetry pruning | ✅ **current** | 677 | | #227 | broadwell | |
| opt | LMcutᵅ | ❌ **stale** | 2334 | best | #181, #206 | sunnycove | #185, #203, #209, #239, #245 |
| | ASPᵅ | ❌ **stale** | 2334 | best | #181, #206 | sunnycove | #185, #203, #209, #239, #245 |
| | ASP | ❌ **stale** | 661 | | #245 | sunnycove | |
| | LMcut | ❌ **stale** | 661 | | #245 | sunnycove | |
| | LMcut with symmetry pruning | ✅ **current** | 661 | | #225 | broadwell | |

## IPC resources

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ❌ **stale** | 544 | best | #181 | sunnycove | #209, #245 |
| | ASPᵅ | ❌ **stale** | 544 | best | #181 | sunnycove | #209, #245 |
| | ASP | ❌ **stale** | 331 | | #245 | sunnycove | |
| | LAMA | ❌ **stale** | 331 | | #245 | sunnycove | |
| | LAMA with symmetry pruning | ✅ **current** | 331 | | #227 | broadwell | |
| opt | LMcutᵅ | ❌ **stale** | 588 | best | #181 | sunnycove | #185, #209, #245 |
| | ASPᵅ | ❌ **stale** | 588 | best | #181 | sunnycove | #185, #209, #245 |
| | ASP | ❌ **stale** | 383 | | #245 | sunnycove | |
| | LMcut | ❌ **stale** | 383 | | #245 | sunnycove | |
| | LMcut with symmetry pruning | ✅ **current** | 383 | | #225 | broadwell | |
