# Benchmark report

2026-11-10 10:16 — experiments/ipc/unsat/scaled/results.csv

334 problems compared over abs-ms, ms, oss

## Verdicts

```
Verdict                                M&Sᵅ          M&S          OSS
---------------------------------------------------------------------
Unsolvable                      330 (98.8%)  276 (82.6%)   51 (15.3%)
Unknown                            0 (0.0%)     0 (0.0%)     0 (0.0%)
Timeouts                           0 (0.0%)     3 (0.9%)  218 (65.3%)
Out of memory                      4 (1.2%)   55 (16.5%)   65 (19.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                          334          334          334
```

## Head to head, over the problems both solved

```
Metric                                 M&Sᵅ          M&S
--------------------------------------------------------
Proved unsolvable by both               276          276
Faster                           92 (33.3%)  184 (66.7%)
Proved when the other did not            54            0
Median runtime                      19.42 s       8.67 s
Total runtime                   31,790.40 s  30,914.68 s
```

## Where the timeouts died

```
Killed during                          M&Sᵅ
-------------------------------------------
Total                                     0
```

## Proved unsolvable by domain

```
Domain (problems)                 Size      M&Sᵅ       M&S       OSS
--------------------------------------------------------------------
cave-diving (1)                      2         1         1         1
                                     3         1         1         1
                                     5         1         1         1
                                    10         1         1         1
                                    20         1         1         1
                                    50         1         1         1
                                   100         1         1         0
                                   200         1         1         0
                                   500         1         1         0
                                  1000         1         1         0
document-transfer (7)                3         2         2         1
                                     4         1         1         0
                                     5         6         6         1
                                     6         1         1         0
                                    10         7         7         1
                                    20         7         7         0
                                    50         7         7         0
                                   100         7         7         0
                                   200         7         7         0
                                   500         7         3         0
                                  1000         7         2         0
over-nomystery (12)                  2        12        12         3
                                     3        12        12         2
                                     5        12        11         2
                                    10        12        11         2
                                    20        12        11         1
                                    50        12        11         0
                                   100        12        11         0
                                   200        12        11         0
                                   500        12         4         0
                                  1000        11         4         0
over-rovers (15)                     2        10        10         4
                                     3        14        14         6
                                     4         1         1         0
                                     5        15        15         6
                                    10        15        14         3
                                    20        15        14         3
                                    50        15        12         2
                                   100        15        10         2
                                   200        15        10         2
                                   500        15        10         2
                                  1000        12         8         2
Total (334)                                  330       276        51
```
