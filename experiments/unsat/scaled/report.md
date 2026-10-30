# Benchmark report

2026-10-30 15:47 — experiments/unsat/scaled/results.csv

210 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                     210 (100.0%)   93 (44.3%)
Unknown                            0 (0.0%)     0 (0.0%)
Timeouts                           0 (0.0%)   42 (20.0%)
Out of memory                      0 (0.0%)   75 (35.7%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          210          210
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                93           93
Faster                           43 (46.2%)   50 (53.8%)
Proved when the other did not           117            0
Median runtime                       9.75 s       5.00 s
Total runtime                    9,131.48 s  17,925.07 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Total                                     0
```

## Proved unsolvable by domain

```
Domain (problems)                 Size      M&Sᵅ       M&S
----------------------------------------------------------
cave-diving (5)                      2         1         1
                                     3         1         1
                                     4         2         2
                                     5         3         3
                                     8         1         0
                                    10         4         1
                                    12         1         1
                                    20         5         3
                                    50         5         1
                                   100         5         0
                                   200         5         0
                                   500         5         0
                                  1000         5         0
document-transfer (1)                3         1         1
                                     5         1         1
                                    10         1         1
                                    20         1         1
                                    50         1         1
                                   100         1         1
                                   200         1         1
                                   500         1         1
                                  1000         1         0
over-nomystery (8)                   2         8         8
                                     3         8         4
                                     5         8         3
                                    10         8         3
                                    20         8         3
                                    50         8         3
                                   100         8         3
                                   200         8         3
                                   500         8         2
                                  1000         8         0
over-rovers (8)                      2         6         5
                                     3         8         7
                                     5         8         7
                                    10         8         3
                                    20         8         3
                                    50         8         3
                                   100         8         3
                                   200         8         3
                                   500         8         3
                                  1000         8         3
Total (210)                                  210        93
```
