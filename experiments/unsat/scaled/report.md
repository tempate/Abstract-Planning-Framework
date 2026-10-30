# Benchmark report

2026-10-30 11:54 — experiments/unsat/scaled/results.csv

80 problems compared over abs-ms, ms

## Verdicts

```
Verdict                                M&Sᵅ          M&S
--------------------------------------------------------
Unsolvable                      80 (100.0%)   32 (40.0%)
Unknown                            0 (0.0%)     0 (0.0%)
Timeouts                           0 (0.0%)   14 (17.5%)
Out of memory                      0 (0.0%)   34 (42.5%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                           80           80
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both                32           32
Faster                           10 (31.2%)   22 (68.8%)
Proved when the other did not            48            0
Median runtime                      16.00 s       2.56 s
Total runtime                      748.18 s   3,115.15 s
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
Total (80)                                    80        32
```
