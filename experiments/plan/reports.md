# Benchmark report

2026-09-18 11:18 — experiments/plan/results.csv

446 problems compared over abstract, concrete, lama; 1 dropped as unfinished

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                       120 (26.9%)         99 (22.2%)        397 (89.0%)
Timeouts                                          314 (70.4%)        335 (75.1%)          34 (7.6%)
Out of memory                                       12 (2.7%)          12 (2.7%)          14 (3.1%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.2%)
Total problems                                            446                446                446
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                        97                 97
Faster when both found a plan                      36 (37.1%)         61 (62.9%)
Plan found when the other did not                          23                  2
Median runtime when both found a plan                  8.50 s             9.75 s
Total runtime across shared solves                 6,184.68 s         8,720.46 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                       120                120
Faster when both found a plan                        1 (0.8%)        119 (99.2%)
Plan found when the other did not                           0                277
Median runtime when both found a plan                 11.24 s             2.44 s
Total runtime across shared solves                16,788.34 s           499.73 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     260 (83%)
Guided concrete search                               34 (11%)
Extended concrete search                              20 (6%)
Total                                                     314
```

## How the successes were solved

```
How the 120 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (55%)
Refined after switching some actions off             46 (38%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     120
```

## Deletes relaxed, over the 112 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               66 (59%)
5 to 9                                                 8 (7%)
10 to 19                                             22 (20%)
20 or more                                             5 (4%)
Total                                                     112
```
