# Benchmark report

2026-09-24 11:37 — experiments/plan/resources/results.csv

183 problems compared over abstract, concrete, lama; 147 dropped as unfinished

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                        38 (20.8%)         39 (21.3%)        172 (94.0%)
Timeouts                                          106 (57.9%)        144 (78.7%)          10 (5.5%)
Out of memory                                        0 (0.0%)           0 (0.0%)           0 (0.0%)
Others                                             39 (21.3%)           0 (0.0%)           1 (0.5%)
Total problems                                            183                183                183
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                        37                 37
Faster when both found a plan                       8 (21.6%)         29 (78.4%)
Plan found when the other did not                           1                  2
Median runtime when both found a plan                 10.14 s             6.38 s
Total runtime across shared solves                 1,300.08 s         1,344.76 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                        38                 38
Faster when both found a plan                        2 (5.3%)         36 (94.7%)
Plan found when the other did not                           0                134
Median runtime when both found a plan                 10.32 s             2.97 s
Total runtime across shared solves                 1,337.33 s           286.01 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                      78 (74%)
Abstract plan discarded                              26 (25%)
Guided concrete search                                 2 (2%)
Total                                                     106
```

## How the successes were solved

```
How the 38 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       31 (82%)
Refined after switching some actions off               3 (8%)
Abstract plan discarded, solved above it              4 (11%)
Total                                                      38
```

## Deletes relaxed, over the 34 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                   0 (0%)
1 to 4                                               32 (94%)
5 to 9                                                 2 (6%)
10 to 19                                               0 (0%)
20 or more                                             0 (0%)
Total                                                      34
```
