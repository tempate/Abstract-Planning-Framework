# Benchmark report

2026-10-15 09:36 — experiments/unsat/symmetries/results.csv

111 problems compared over abs-fd, fd

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                       23 (20.7%)   47 (42.3%)
Unknown                          18 (16.2%)     0 (0.0%)
Timeouts                         35 (31.5%)   13 (11.7%)
Out of memory                    35 (31.5%)   51 (45.9%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          111          111
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                21           21
Faster                           13 (61.9%)    8 (38.1%)
Proved when the other did not             2           26
Median runtime                       6.91 s       5.47 s
Total runtime                      983.65 s   2,585.27 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Abstract search                   35 (100%)
Total                                    35
```

## Proved unsolvable by domain

```
Domain                        Problems      M&Sᵅ       M&S
----------------------------------------------------------
bag-barman                          13         0         5
bag-gripper                         11         0         3
cave-diving                         25         5        10
document-transfer                   20         1        12
over-nomystery                      22         8         9
over-rovers                         19         8         7
pegsol-row5                          1         1         1
Total                              111        23        47
```
