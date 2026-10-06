# Benchmark report

2026-10-06 10:01 — experiments/plan/resources/results.csv

330 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found                                        72 (21.8%)         81 (24.5%)        124 (37.6%)        305 (92.4%)
Timeouts                                          258 (78.2%)        249 (75.5%)        176 (53.3%)          22 (6.7%)
Out of memory                                        0 (0.0%)           0 (0.0%)          29 (8.8%)           1 (0.3%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.3%)           2 (0.6%)
Total problems                                            330                330                330                330
```

## Head to head

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found by both                                        70                 70                124                124
Faster when both found a plan                      47 (67.1%)         23 (32.9%)           3 (2.4%)        121 (97.6%)
Plan found when the other did not                           2                 11                  0                181
Median runtime when both found a plan                  7.20 s            10.03 s            14.32 s             3.15 s
Total runtime across shared solves                 5,966.09 s         3,499.96 s         7,995.62 s           769.71 s
```

## Where the timeouts died

```
Killed during                                       Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstraction                                            5 (2%)             5 (3%)
Writing the abstract task                              1 (0%)             0 (0%)
Searching for the abstract plan                     158 (63%)             3 (2%)
Guided concrete search                                 6 (2%)           66 (38%)
Unguided concrete search                             79 (32%)          102 (58%)
Total                                                     249                176
```

## How the successes were solved

```
Solved by                                           Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstract plan refined directly                       61 (75%)           91 (73%)
Refined after switching some actions off             13 (16%)           26 (21%)
Abstract plan discarded, solved above it               7 (9%)             7 (6%)
Total                                                      81                124
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Deletes relaxed                                     Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
None                                                   0 (0%)             0 (0%)
1 to 4                                               59 (80%)           69 (59%)
5 to 9                                                 7 (9%)           15 (13%)
10 to 19                                              8 (11%)           14 (12%)
20 or more                                             0 (0%)           19 (16%)
Total                                                      74                117
```

## Plans found by domain

```
Domain                           Problems        ASP  Abs + ASP   Abs + FD         FD
-------------------------------------------------------------------------------------
data-network-sat18-strips              15          0          1          1         12
elevators-sat08-strips                 30          1          3          7         30
elevators-sat11-strips                 14          0          0          0         14
freecell                               73         10         10         10         72
mprime                                 29         29         29         28         29
mystery                                26         17         15         17         17
nomystery-sat11-strips                 19          2          8         10         12
openstacks-sat08-strips                27          3          3         24         27
openstacks-sat11-strips                 7          0          0          4          7
thoughtful-sat14-strips                20          0          1          5         15
tpp                                    24          5          5          5         24
transport-sat08-strips                 30          5          6         13         30
transport-sat11-strips                 13          0          0          0         13
transport-sat14-strips                  3          0          0          0          3
Total                                 330         72         81        124        305
```
