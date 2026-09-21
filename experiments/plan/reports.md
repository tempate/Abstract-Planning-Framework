# Benchmark report

2026-09-21 09:14 — experiments/plan/results.csv

446 problems compared over abstract, concrete, lama; 1 dropped as unfinished

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                       121 (27.1%)         99 (22.2%)        397 (89.0%)
Timeouts                                          313 (70.2%)        335 (75.1%)          34 (7.6%)
Out of memory                                       12 (2.7%)          12 (2.7%)          14 (3.1%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.2%)
Total problems                                            446                446                446
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                        97                 97
Faster when both found a plan                      31 (32.0%)         66 (68.0%)
Plan found when the other did not                          24                  2
Median runtime when both found a plan                  7.92 s             9.75 s
Total runtime across shared solves                 7,084.61 s         8,720.46 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                       121                121
Faster when both found a plan                        1 (0.8%)        120 (99.2%)
Plan found when the other did not                           0                276
Median runtime when both found a plan                 11.89 s             2.44 s
Total runtime across shared solves                19,377.56 s           502.21 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     262 (84%)
Guided concrete search                               31 (10%)
Abstract plan discarded                               20 (6%)
Total                                                     313
```

## How the successes were solved

```
How the 121 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (55%)
Refined after switching some actions off             47 (39%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     121
```

## Deletes relaxed, over the 113 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               66 (58%)
5 to 9                                                 8 (7%)
10 to 19                                             23 (20%)
20 or more                                             5 (4%)
Total                                                     113
```
