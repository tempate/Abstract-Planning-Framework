# Benchmark report

2026-10-06 17:04 — experiments/unsolvability/symmetries/results.csv

168 problems compared over abs-fd, fd

## Verdicts

```
Verdict                                              Abs + FD                 FD
--------------------------------------------------------------------------------
Unsolvable                                         17 (10.1%)         37 (22.0%)
Unknown                                            34 (20.2%)           0 (0.0%)
Timeouts                                           87 (51.8%)        131 (78.0%)
Out of memory                                      30 (17.9%)           0 (0.0%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            168                168
```

## Head to head

```
Metric                                               Abs + FD                 FD
--------------------------------------------------------------------------------
Proved unsolvable by both                                  14                 14
Faster when both proved it                          7 (50.0%)          7 (50.0%)
Proved it when the other did not                            3                 23
Median runtime when both proved it                     5.99 s             4.11 s
Total runtime across shared proofs                   140.55 s           440.73 s
```

## Where the timeouts died

```
Killed during                                        Abs + FD
-------------------------------------------------------------
Searching for the abstract plan                     87 (100%)
Total                                                      87
```

## Proved unsolvable by domain

```
Domain                           Problems   Abs + FD         FD
---------------------------------------------------------------
bag-barman                             13          0          2
bag-gripper                            22          0          0
bag-transport                          29          0          7
cave-diving                            25          5          7
document-transfer                      20          2          7
over-nomystery                         24          2          2
over-rovers                            19          7          6
pegsol-row5                             1          1          1
tetris                                 15          0          5
Total                                 168         17         37
```
