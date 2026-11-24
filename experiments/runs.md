# What ran where

`results.csv` records no commit, so each row below goes back to the PR whose merge last changed its status or runtime. State of main at #223 on 2026-11-24.

Latest code means main at #221. The PRs after #181 that change a result are #185 (opt fallback), #203 (fixed PDDL Symmetries seed, so the classes change), #206 (distinct inequalities, rerun on mprime and four HTG domains only) and #209 with #217 (one-shot on a partial grounding). #238 drops the 10 opt resources problems with no class to collapse, so their rows are gone rather than stale. #239 finds symmetries before grounding on every track, which only the HTG rows did before. #223 adds the Powerlifted rows. The others since then are refactors or touch no track. Fast Downward has not moved since #12, so the LAMA and LMcut rows hold on any commit.

| Status | Meaning |
|---|---|
| ✅ **current** | latest relevant code, every class, on sunnycove |
| ⚠️ **partly stale** | latest relevant code, but only the best class or partly on broadwell |
| ❌ **stale** | lacks a result-changing PR on some rows |

| Classes | Meaning |
|---|---|
| all | every class `classes.txt` lists |
| best | one class per problem, the best of an earlier run |

## HTG

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ⚠️ **partly stale** | 3406 | 107 / 243 | #209 | sunnycove | |
| | ASPᵅ | ❌ **stale** | 3406 | best | #212 | sunnycove | #209 |
| | ASP | ✅ **current** | 443 | | #212 | sunnycove | |
| | LAMA | ⚠️ **partly stale** | 443 | | #157, #196 | broadwell, sunnycove | |
| | Powerliftedᵅ | ⚠️ **partly stale** | 3406 | all | #223 | broadwell | |
| | Powerlifted | ⚠️ **partly stale** | 443 | | #223 | broadwell | |
| opt | LMcutᵅ | ❌ **stale** | 3406 | 2 / 239 | #209, #196–#206 | sunnycove | #209 |
| | ASPᵅ | ❌ **stale** | 3406 | best | #212 | sunnycove | #209 |
| | ASP | ✅ **current** | 443 | | #212 | sunnycove | |
| | LMcut | ✅ **current** | 443 | | #157, #196 | sunnycove | |
| | Powerliftedᵅ | ⚠️ **partly stale** | 3406 | all | #223 | broadwell | |
| | Powerlifted | ⚠️ **partly stale** | 443 | | #223 | broadwell | |

## IPC symmetries

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ❌ **stale** | 2478 | best | #181, #206 | sunnycove | #203, #209, #239 |
| | ASPᵅ | ❌ **stale** | 2478 | best | #181, #206 | sunnycove | #203, #209, #239 |
| | ASP | ✅ **current** | 557 | | #181 | sunnycove | |
| | LAMA | ✅ **current** | 557 | | #95 | sunnycove | |
| opt | LMcutᵅ | ❌ **stale** | 2334 | best | #181, #206 | sunnycove | #185, #203, #209, #239 |
| | ASPᵅ | ❌ **stale** | 2334 | best | #181, #206 | sunnycove | #185, #203, #209, #239 |
| | ASP | ✅ **current** | 518 | | #181 | sunnycove | |
| | LMcut | ✅ **current** | 518 | | #124 | sunnycove | |

## IPC resources

| Track | Mode | Status | Jobs | Classes (all / best) | Code | Partition | Lacks |
|---|---|---|---|---|---|---|---|
| sat | LAMAᵅ | ❌ **stale** | 544 | best | #181 | sunnycove | #209 |
| | ASPᵅ | ❌ **stale** | 544 | best | #181 | sunnycove | #209 |
| | ASP | ✅ **current** | 330 | | #181 | sunnycove | |
| | LAMA | ✅ **current** | 330 | | #85 | sunnycove | |
| opt | LMcutᵅ | ❌ **stale** | 588 | best | #181 | sunnycove | #185, #209 |
| | ASPᵅ | ❌ **stale** | 588 | best | #181 | sunnycove | #185, #209 |
| | ASP | ✅ **current** | 363 | | #181 | sunnycove | |
| | LMcut | ✅ **current** | 363 | | #124 | sunnycove | |
