# Benchmark report

2026-09-24 11:30 — experiments/plan/resources/results.csv

330 problems compared over abstract

## Coverage

```
Metric                                      Abstract pipeline
-------------------------------------------------------------
Plans found                                        72 (21.8%)
Timeouts                                          199 (60.3%)
Out of memory                                        0 (0.0%)
Others                                             59 (17.9%)
Total problems                                            330
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
