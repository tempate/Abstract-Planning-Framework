# Benchmark report

2026-09-24 13:38 — experiments/plan/resources/results.csv

330 problems compared over abstract, concrete, lama

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                        72 (21.8%)         72 (21.8%)        305 (92.4%)
Timeouts                                          199 (60.3%)        258 (78.2%)          22 (6.7%)
Out of memory                                        0 (0.0%)           0 (0.0%)           1 (0.3%)
Others                                             59 (17.9%)           0 (0.0%)           2 (0.6%)
Total problems                                            330                330                330
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                        69                 69
Faster when both found a plan                      25 (36.2%)         44 (63.8%)
Plan found when the other did not                           3                  3
Median runtime when both found a plan                 10.10 s             7.09 s
Total runtime across shared solves                 3,792.14 s         5,261.89 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                        72                 72
Faster when both found a plan                        6 (8.3%)         66 (91.7%)
Plan found when the other did not                           0                233
Median runtime when both found a plan                 10.32 s             2.97 s
Total runtime across shared solves                 6,544.34 s           405.35 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     109 (55%)
Abstract plan discarded                              82 (41%)
Guided concrete search                                 8 (4%)
Total                                                     199
```

## How the successes were solved

```
How the 72 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       51 (71%)
Refined after switching some actions off             14 (19%)
Abstract plan discarded, solved above it              7 (10%)
Total                                                      72
```

## Deletes relaxed, over the 65 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                   0 (0%)
1 to 4                                               53 (82%)
5 to 9                                                 4 (6%)
10 to 19                                              8 (12%)
20 or more                                             0 (0%)
Total                                                      65
```
