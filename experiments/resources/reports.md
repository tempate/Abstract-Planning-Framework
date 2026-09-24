# Benchmark report

2026-09-24 10:54 — experiments/resources/results.csv

1716 problems compared over abstract

## Coverage

```
Metric                                      Abstract pipeline
-------------------------------------------------------------
Plans found                                         72 (4.2%)
Timeouts                                          200 (11.7%)
Out of memory                                     302 (17.6%)
Others                                           1142 (66.6%)
Total problems                                           1716
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     109 (55%)
Abstract plan discarded                              82 (41%)
Guided concrete search                                 8 (4%)
problem_reading                                        1 (0%)
Total                                                     200
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
