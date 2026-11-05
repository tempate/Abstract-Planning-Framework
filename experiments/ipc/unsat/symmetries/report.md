# Benchmark report

2026-11-03 13:39 — experiments/ipc/unsat/symmetries/results.csv

111 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                       42 (37.8%)   49 (44.1%)
Unknown                          13 (11.7%)     0 (0.0%)
Timeouts                          10 (9.0%)     6 (5.4%)
Out of memory                    46 (41.4%)   56 (50.5%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          111          111
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                36           36
Faster                            9 (25.0%)   27 (75.0%)
Proved when the other did not             6           13
Median runtime                      14.67 s       4.39 s
Total runtime                    6,140.10 s   3,135.04 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Abstract search                   10 (100%)
Total                                    10
```

## Proved unsolvable by domain

```
Domain (problems)                 M&Sᵅ       M&S
------------------------------------------------
bag-barman (13)                      0         0
bag-gripper (11)                     0         7
cave-diving (25)                     6         1
document-transfer (20)               7        10
over-nomystery (22)                 12        15
over-rovers (19)                    16        15
pegsol-row5 (1)                      1         1
Total (111)                         42        49
```
