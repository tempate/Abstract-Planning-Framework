# Benchmark report

2026-09-24 14:38 — experiments/plan/resources/results.csv

330 problems compared over abstraction-asp, asp, fd

## Coverage

```
Metric                                      Abstraction + ASP                ASP                 FD
---------------------------------------------------------------------------------------------------
Plans found                                        76 (23.0%)         72 (21.8%)        305 (92.4%)
Timeouts                                          254 (77.0%)        258 (78.2%)          22 (6.7%)
Out of memory                                        0 (0.0%)           0 (0.0%)           1 (0.3%)
Others                                               0 (0.0%)           0 (0.0%)           2 (0.6%)
Total problems                                            330                330                330
```

## Head to head: Abstraction + ASP vs ASP

```
Metric                                      Abstraction + ASP                ASP
--------------------------------------------------------------------------------
Plans found by both                                        70                 70
Faster when both found a plan                      26 (37.1%)         44 (62.9%)
Plan found when the other did not                           6                  2
Median runtime when both found a plan                 10.12 s             7.20 s
Total runtime across shared solves                 3,803.93 s         5,966.09 s
```

## Head to head: Abstraction + ASP vs FD

```
Metric                                      Abstraction + ASP                 FD
--------------------------------------------------------------------------------
Plans found by both                                        76                 76
Faster when both found a plan                        6 (7.9%)         70 (92.1%)
Plan found when the other did not                           0                229
Median runtime when both found a plan                 11.04 s             2.97 s
Total runtime across shared solves                 7,620.39 s           417.07 s
```

## Where the timeouts of Abstraction + ASP died

```
Where Abstraction + ASP was killed                   Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     159 (63%)
Abstract plan discarded                              82 (32%)
Guided concrete search                                 8 (3%)
pnf_translation                                        5 (2%)
Total                                                     254
```

## How the successes of Abstraction + ASP were solved

```
How the 76 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       54 (71%)
Refined after switching some actions off             15 (20%)
Abstract plan discarded, solved above it               7 (9%)
Total                                                      76
```

## Deletes relaxed by Abstraction + ASP, over the 69 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                   0 (0%)
1 to 4                                               54 (78%)
5 to 9                                                7 (10%)
10 to 19                                              8 (12%)
20 or more                                             0 (0%)
Total                                                      69
```
