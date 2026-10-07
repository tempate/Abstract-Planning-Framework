# Benchmark report

2026-10-07 09:25 — experiments/unsolvability/symmetries/results.csv

168 problems compared over abs-fd, fd

## Verdicts

```
Verdict                                              Abs + FD                 FD
--------------------------------------------------------------------------------
Unsolvable                                         26 (15.5%)         56 (33.3%)
Unknown                                            41 (24.4%)           0 (0.0%)
Timeouts                                           40 (23.8%)         33 (19.6%)
Out of memory                                      61 (36.3%)         79 (47.0%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            168                168
```

## Head to head

```
Metric                                               Abs + FD                 FD
--------------------------------------------------------------------------------
Proved unsolvable by both                                  24                 24
Faster when both proved it                         14 (58.3%)         10 (41.7%)
Proved it when the other did not                            2                 32
Median runtime when both proved it                    11.12 s             5.78 s
Total runtime across shared proofs                 1,526.28 s         2,755.60 s
```

## Where the timeouts died

```
Killed during                                        Abs + FD
-------------------------------------------------------------
Searching for the abstract plan                     40 (100%)
Total                                                      40
```

## Proved unsolvable by domain

```
Domain                           Problems   Abs + FD         FD
---------------------------------------------------------------
bag-barman                             13          0          5
bag-gripper                            22          0          3
bag-transport                          29          0          8
cave-diving                            25          5         10
document-transfer                      20          3         12
over-nomystery                         24          9         10
over-rovers                            19          8          7
pegsol-row5                             1          1          1
tetris                                 15          0          0
Total                                 168         26         56
```
