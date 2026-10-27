# Benchmark report

2026-10-27 12:53 — experiments/scaled/symmetries/results.csv

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
Domain                        Problems      M&Sᵅ       M&S
----------------------------------------------------------
size-10                              8         8         3
size-100                             8         8         3
size-1000                            8         8         0
size-2                               8         8         8
size-20                              8         8         3
size-200                             8         8         3
size-3                               8         8         4
size-5                               8         8         3
size-50                              8         8         3
size-500                             8         8         2
Total                               80        80        32
```
