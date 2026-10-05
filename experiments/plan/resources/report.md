# Benchmark report

2026-10-05 09:34 — experiments/plan/resources/results.csv

330 problems compared over abs-asp, abs-fd, asp, fd

## Coverage

```
Metric                                      Abstraction + ASP   Abstraction + FD                ASP                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found                                        76 (23.0%)        124 (37.6%)         72 (21.8%)        305 (92.4%)
Timeouts                                          254 (77.0%)        176 (53.3%)        258 (78.2%)          22 (6.7%)
Out of memory                                        0 (0.0%)          29 (8.8%)           0 (0.0%)           1 (0.3%)
Others                                               0 (0.0%)           1 (0.3%)           0 (0.0%)           2 (0.6%)
Total problems                                            330                330                330                330
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

## Head to head: Abstraction + FD vs FD

```
Metric                                       Abstraction + FD                 FD
--------------------------------------------------------------------------------
Plans found by both                                       124                124
Faster when both found a plan                        3 (2.4%)        121 (97.6%)
Plan found when the other did not                           0                181
Median runtime when both found a plan                 14.90 s             3.15 s
Total runtime across shared solves                 7,999.37 s           769.71 s
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

## Where the timeouts of Abstraction + FD died

```
Where Abstraction + FD was killed                    Timeouts
-------------------------------------------------------------
Abstract plan discarded                             102 (58%)
Guided concrete search                               66 (38%)
pnf_translation                                        5 (3%)
concrete_asp                                           3 (2%)
Total                                                     176
```

## How the successes of Abstraction + FD were solved

```
How the 124 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       91 (73%)
Refined after switching some actions off             26 (21%)
Abstract plan discarded, solved above it               7 (6%)
Total                                                     124
```

## Deletes relaxed by Abstraction + FD, over the 117 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                   0 (0%)
1 to 4                                               69 (59%)
5 to 9                                               15 (13%)
10 to 19                                             14 (12%)
20 or more                                           19 (16%)
Total                                                     117
```
