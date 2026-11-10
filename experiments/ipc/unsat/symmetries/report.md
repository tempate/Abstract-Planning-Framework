# Benchmark report

2026-11-10 14:45 — experiments/ipc/unsat/symmetries/results.csv

111 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                       42 (37.8%)   49 (44.1%)
Unknown                            0 (0.0%)     0 (0.0%)
Timeouts                         17 (15.3%)     6 (5.4%)
Out of memory                    52 (46.8%)   56 (50.5%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          111          111
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                36           36
Faster                            8 (22.2%)   28 (77.8%)
Proved when the other did not             6           13
Median runtime                      12.76 s       4.39 s
Total runtime                    5,498.08 s   3,135.04 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Abstract search                    13 (76%)
Translating the task                4 (24%)
Total                                    17
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
