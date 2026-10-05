# Benchmark report

2026-10-05 09:16 — experiments/plan/symmetries/results.csv

667 problems compared over abstraction-asp, abstraction-fd, asp, fd

## Coverage

```
Metric                                      Abstraction + ASP   Abstraction + FD                ASP                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found                                       135 (20.2%)        266 (39.9%)        113 (16.9%)        602 (90.3%)
Timeouts                                          519 (77.8%)        311 (46.6%)        541 (81.1%)          42 (6.3%)
Out of memory                                       13 (1.9%)         89 (13.3%)          13 (1.9%)          22 (3.3%)
Others                                               0 (0.0%)           1 (0.1%)           0 (0.0%)           1 (0.1%)
Total problems                                            667                667                667                667
```

## Head to head: Abstraction + ASP vs ASP

```
Metric                                      Abstraction + ASP                ASP
--------------------------------------------------------------------------------
Plans found by both                                       111                111
Faster when both found a plan                      43 (38.7%)         68 (61.3%)
Plan found when the other did not                          24                  2
Median runtime when both found a plan                  8.09 s            10.35 s
Total runtime across shared solves                 8,268.69 s        12,840.20 s
```

## Head to head: Abstraction + ASP vs FD

```
Metric                                      Abstraction + ASP                 FD
--------------------------------------------------------------------------------
Plans found by both                                       135                135
Faster when both found a plan                        4 (3.0%)        131 (97.0%)
Plan found when the other did not                           0                467
Median runtime when both found a plan                 11.07 s             3.11 s
Total runtime across shared solves                21,616.50 s           626.21 s
```

## Head to head: Abstraction + FD vs ASP

```
Metric                                       Abstraction + FD                ASP
--------------------------------------------------------------------------------
Plans found by both                                       110                110
Faster when both found a plan                      51 (46.4%)         59 (53.6%)
Plan found when the other did not                         156                  3
Median runtime when both found a plan                  5.69 s            10.48 s
Total runtime across shared solves                 2,797.37 s        12,835.88 s
```

## Head to head: Abstraction + FD vs FD

```
Metric                                       Abstraction + FD                 FD
--------------------------------------------------------------------------------
Plans found by both                                       261                261
Faster when both found a plan                        9 (3.4%)        252 (96.6%)
Plan found when the other did not                           5                341
Median runtime when both found a plan                 15.11 s             3.49 s
Total runtime across shared solves                26,836.01 s         3,923.05 s
```

## Where the timeouts of Abstraction + ASP died

```
Where Abstraction + ASP was killed                   Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     454 (87%)
Abstract plan discarded                               33 (6%)
Guided concrete search                                32 (6%)
Total                                                     519
```

## How the successes of Abstraction + ASP were solved

```
How the 135 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       72 (53%)
Refined after switching some actions off             54 (40%)
Abstract plan discarded, solved above it               9 (7%)
Total                                                     135
```

## Deletes relaxed by Abstraction + ASP, over the 126 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 12 (10%)
1 to 4                                               77 (61%)
5 to 9                                                 9 (7%)
10 to 19                                             23 (18%)
20 or more                                             5 (4%)
Total                                                     126
```

## Where the timeouts of Abstraction + FD died

```
Where Abstraction + FD was killed                    Timeouts
-------------------------------------------------------------
Guided concrete search                              264 (85%)
Abstract plan discarded                              36 (12%)
concrete_asp                                          11 (4%)
Total                                                     311
```

## How the successes of Abstraction + FD were solved

```
How the 266 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                      159 (60%)
Refined after switching some actions off             98 (37%)
Abstract plan discarded, solved above it               9 (3%)
Total                                                     266
```

## Deletes relaxed by Abstraction + FD, over the 257 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 28 (11%)
1 to 4                                              170 (66%)
5 to 9                                               27 (11%)
10 to 19                                              24 (9%)
20 or more                                             8 (3%)
Total                                                     257
```
