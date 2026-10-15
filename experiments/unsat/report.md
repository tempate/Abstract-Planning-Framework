# Benchmark report

2026-10-15 09:31 — experiments/unsat/results.csv

168 problems compared over abs-fd, fd

## Verdicts

```
Verdict                                 FDᵅ           FD
--------------------------------------------------------
Unsolvable                       23 (13.7%)   56 (33.3%)
Unknown                          18 (10.7%)     0 (0.0%)
Timeouts                         35 (20.8%)   33 (19.6%)
Out of memory                    35 (20.8%)   79 (47.0%)
Others                           57 (33.9%)     0 (0.0%)
Total problems                          168          168
```

## Head to head, over the problems both solved

```
Metric                                  FDᵅ           FD
--------------------------------------------------------
Proved unsolvable by both                21           21
Faster                           13 (61.9%)    8 (38.1%)
Proved when the other did not             2           35
Median runtime                       6.91 s       5.47 s
Total runtime                      983.65 s   2,585.27 s
```

## Where the timeouts died

```
Killed during                           FDᵅ
-------------------------------------------
Abstract search                   35 (100%)
Total                                    35
```

## Proved unsolvable by domain

```
Domain                        Problems       FDᵅ        FD
----------------------------------------------------------
bag-barman                          13         0         5
bag-gripper                         22         0         3
bag-transport                       29         0         8
cave-diving                         25         5        10
document-transfer                   20         1        12
over-nomystery                      24         8        10
over-rovers                         19         8         7
pegsol-row5                          1         1         1
tetris                              15         0         0
Total                              168        23        56
```
