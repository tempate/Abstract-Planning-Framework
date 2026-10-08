# Benchmark report

2026-10-07 09:20 — experiments/plan/symmetries/results.csv

667 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found                                       113 (16.9%)        133 (19.9%)        274 (41.1%)        602 (90.3%)
Timeouts                                          541 (81.1%)        521 (78.1%)        302 (45.3%)          42 (6.3%)
Out of memory                                       13 (1.9%)          13 (1.9%)         90 (13.5%)          22 (3.3%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.1%)           1 (0.1%)
Total problems                                            667                667                667                667
```

## Head to head

```
Metric                                                    ASP          Abs + ASP           Abs + FD                 FD
----------------------------------------------------------------------------------------------------------------------
Plans found by both                                       110                110                272                272
Faster when both found a plan                      67 (60.9%)         43 (39.1%)          13 (4.8%)        259 (95.2%)
Plan found when the other did not                           3                 23                  2                330
Median runtime when both found a plan                 10.48 s             9.11 s            16.56 s             3.52 s
Total runtime across shared solves                12,819.18 s         7,151.68 s        29,694.29 s         4,055.50 s
```

## Where the timeouts died

```
Killed during                                       Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Searching for the abstract plan                     453 (87%)            11 (4%)
Guided concrete search                                35 (7%)          258 (85%)
Unguided concrete search                              33 (6%)           33 (11%)
Total                                                     521                302
```

## How the successes were solved

```
Solved by                                           Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstract plan refined directly                       72 (54%)          160 (58%)
Refined after switching some actions off             52 (39%)          105 (38%)
Abstract plan discarded, solved above it               9 (7%)             9 (3%)
Total                                                     133                274
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Deletes relaxed                                     Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
None                                                 12 (10%)           28 (11%)
1 to 4                                               80 (65%)          191 (72%)
5 to 9                                                 9 (7%)            25 (9%)
10 to 19                                             18 (15%)            15 (6%)
20 or more                                             5 (4%)             6 (2%)
Total                                                     124                265
```

## Plans found by domain

```
Domain                           Problems        ASP  Abs + ASP   Abs + FD         FD
-------------------------------------------------------------------------------------
agricola-sat18-strips                  20          0          0          0         12
airport                                19         11         14         17         19
barman-sat11-strips                    20          0          0          3         20
barman-sat14-strips                    20          0          0          1         20
childsnack-sat14-strips                20          0          0          0          6
depot                                   9          1          3          4          8
driverlog                              13          7          8         12         13
elevators-sat08-strips                 30          1          1         13         30
elevators-sat11-strips                 14          0          0          0         14
floortile-sat11-strips                 20          0          0          9          7
gripper                                20          3          3          3         20
hiking-sat14-strips                    20          2          6         18         20
logistics00                            19          8         10         13         19
logistics98                            31          1          2          4         31
miconic                                11          1          2         11         11
mprime                                 21         20         20         21         21
mystery                                16         10         10          9         10
nomystery-sat11-strips                 14          2          4          8          9
openstacks-sat08-strips                29          2          2         23         29
openstacks-sat11-strips                15          0          0          4         15
pipesworld-notankage                   34          9         10          9         27
pipesworld-tankage                     47          8         10          9         40
quantum-layout-sat23-strips             7          4          2          0          7
satellite                              34          5          5         14         34
sokoban-sat08-strips                   29          2          2         14         28
sokoban-sat11-strips                    5          0          0          4          4
tpp                                    29          4          6          6         29
transport-sat08-strips                 30          5          6          7         30
transport-sat11-strips                 20          0          0          0         18
woodworking-sat08-strips               27          3          3         18         27
woodworking-sat11-strips               11          0          0          8         11
zenotravel                             13          4          4         12         13
Total                                 667        113        133        274        602
```
