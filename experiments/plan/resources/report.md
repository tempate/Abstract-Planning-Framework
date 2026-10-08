# Benchmark report

2026-10-08 11:56 — experiments/plan/resources/results.csv

330 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found                                        72 (21.8%)         84 (25.5%)        133 (40.3%)        305 (92.4%)
Timeouts                                          258 (78.2%)        246 (74.5%)        166 (50.3%)          22 (6.7%)
Out of memory                                        0 (0.0%)           0 (0.0%)          30 (9.1%)           1 (0.3%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.3%)           2 (0.6%)
Total problems                                            330                330                330                330
```

## Head to head

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found by both                                        72                 72                132                132
Faster when both found a plan                      46 (63.9%)         26 (36.1%)           5 (3.8%)        127 (96.2%)
Plan found when the other did not                           0                 12                  1                173
Median runtime when both found a plan                  7.39 s             9.66 s            12.25 s             3.16 s
Total runtime across shared solves                 6,180.44 s         4,979.74 s        13,259.46 s           799.98 s
```

## Where the timeouts died

```
Killed during                                       Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstraction                                            5 (2%)             5 (3%)
Searching for the abstract plan                     158 (64%)             3 (2%)
Guided concrete search                                16 (7%)           94 (57%)
Unguided concrete search                             67 (27%)           64 (39%)
Total                                                     246                166
```

## How the successes were solved

```
Solved by                                           Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstract plan refined directly                       61 (73%)           91 (68%)
Refined after switching some actions off             16 (19%)           35 (26%)
Abstract plan discarded, solved above it               7 (8%)             7 (5%)
Total                                                      84                133
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Deletes relaxed                                     Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
None                                                   0 (0%)             0 (0%)
1 to 4                                               61 (79%)           69 (55%)
5 to 9                                                 7 (9%)           24 (19%)
10 to 19                                              9 (12%)           14 (11%)
20 or more                                             0 (0%)           19 (15%)
Total                                                      77                126
```

## Plans found by domain

```
Domain                           Problems        ASP  Abs + ASP   Abs + FD         FD
-------------------------------------------------------------------------------------
data-network-sat18-strips              15          0          1          1         12
elevators-sat08-strips                 30          1          3         13         30
elevators-sat11-strips                 14          0          0          0         14
freecell                               73         10         11         10         72
mprime                                 29         29         29         29         29
mystery                                26         17         17         17         17
nomystery-sat11-strips                 19          2          8          9         12
openstacks-sat08-strips                27          3          3         24         27
openstacks-sat11-strips                 7          0          0          4          7
thoughtful-sat14-strips                20          0          1          8         15
tpp                                    24          5          5          5         24
transport-sat08-strips                 30          5          6         13         30
transport-sat11-strips                 13          0          0          0         13
transport-sat14-strips                  3          0          0          0          3
Total                                 330         72         84        133        305
```
