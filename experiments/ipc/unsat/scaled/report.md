# Benchmark report

2026-11-03 13:39 — experiments/ipc/unsat/scaled/results.csv

210 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                     210 (100.0%)  163 (77.6%)
Unknown                            0 (0.0%)     0 (0.0%)
Timeouts                           0 (0.0%)     6 (2.9%)
Out of memory                      0 (0.0%)   41 (19.5%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          210          210
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both               163          163
Faster                           29 (17.8%)  134 (82.2%)
Proved when the other did not            47            0
Median runtime                      14.86 s       4.43 s
Total runtime                    8,491.22 s   9,167.72 s
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
                                     4         2         0
                                     5         3         1
                                     8         1         0
                                    10         4         1
                                    12         1         0
                                    20         5         1
                                    50         5         1
                                   100         5         1
                                   200         5         1
                                   500         5         1
                                  1000         5         1
document-transfer (1)                3         1         1
                                     5         1         1
                                    10         1         1
                                    20         1         1
                                    50         1         1
                                   100         1         1
                                   200         1         1
                                   500         1         1
                                  1000         1         1
over-nomystery (8)                   2         8         8
                                     3         8         8
                                     5         8         8
                                    10         8         8
                                    20         8         8
                                    50         8         8
                                   100         8         8
                                   200         8         8
                                   500         8         2
                                  1000         8         2
over-rovers (8)                      2         6         6
                                     3         8         8
                                     5         8         8
                                    10         8         8
                                    20         8         8
                                    50         8         8
                                   100         8         8
                                   200         8         8
                                   500         8         8
                                  1000         8         6
Total (210)                                  210       163
```
