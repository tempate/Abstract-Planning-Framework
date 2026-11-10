# Benchmark report

2026-11-10 14:53 — experiments/ipc/unsat/symmetries/results.csv

111 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                       45 (40.5%)   66 (59.5%)
Unknown                          14 (12.6%)     0 (0.0%)
Timeouts                         23 (20.7%)    10 (9.0%)
Out of memory                    22 (19.8%)   31 (27.9%)
Others                             7 (6.3%)     4 (3.6%)
Total problems                          111          111
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                40           40
Faster                           11 (27.5%)   29 (72.5%)
Proved when the other did not             5           26
Median runtime                      55.70 s       8.54 s
Total runtime                    9,012.07 s   4,070.54 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Abstract search                   23 (100%)
Total                                    23
```

## Proved unsolvable by domain

```
Domain (problems)                 M&Sᵅ       M&S
------------------------------------------------
bag-barman (13)                      0         0
bag-gripper (11)                     0         7
cave-diving (25)                     6         1
document-transfer (20)               8        19
over-nomystery (22)                 12        20
over-rovers (19)                    18        18
pegsol-row5 (1)                      1         1
Total (111)                         45        66
```
