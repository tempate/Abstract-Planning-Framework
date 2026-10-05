# Benchmark report

2026-10-05 09:45 — experiments/unsolvability/symmetries/results.csv

168 problems compared over abs-fd, fd

## Verdicts

```
Verdict                                              Abs + FD                 FD
--------------------------------------------------------------------------------
Unsolvable                                          16 (9.5%)         45 (26.8%)
Unknown                                            36 (21.4%)           0 (0.0%)
Timeouts                                             3 (1.8%)           0 (0.0%)
Out of memory                                     113 (67.3%)        123 (73.2%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            168                168
```

## Head to head

```
Metric                                               Abs + FD                 FD
--------------------------------------------------------------------------------
Proved unsolvable by both                                  13                 13
Faster when both proved it                          5 (38.5%)          8 (61.5%)
Proved it when the other did not                            3                 32
Median runtime when both proved it                     9.88 s             4.71 s
Total runtime across shared proofs                 1,094.01 s         1,763.27 s
```

## Where the timeouts died

```
Killed during                                        Abs + FD
-------------------------------------------------------------
abstract_pddl_writing                                3 (100%)
Total                                                       3
```

## Proved unsolvable by domain

```
Domain                           Problems   Abs + FD         FD
---------------------------------------------------------------
bag-barman                             13          0          5
bag-gripper                            22          0          3
bag-transport                          29          0          8
cave-diving                            25          5          9
document-transfer                      20          1          5
over-nomystery                         24          1          2
over-rovers                            19          8          7
pegsol-row5                             1          1          1
tetris                                 15          0          5
Total                                 168         16         45
```
