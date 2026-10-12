# Benchmark report

2026-10-12 11:45 — experiments/opt/results.csv

1217 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                                    ASP          Abs + ASP           Abs + FD        FD (LM-cut)
----------------------------------------------------------------------------------------------------------------------
Plans found                                       243 (20.0%)        236 (19.4%)        353 (29.0%)        487 (40.0%)
Timeouts                                          961 (79.0%)        947 (77.8%)        786 (64.6%)        728 (59.8%)
Out of memory                                       13 (1.1%)          34 (2.8%)          76 (6.2%)           0 (0.0%)
Others                                               0 (0.0%)           0 (0.0%)           2 (0.2%)           2 (0.2%)
Total problems                                           1217               1217               1217               1217
```

## Head to head

```
Metric                                                    ASP          Abs + ASP           Abs + FD        FD (LM-cut)
----------------------------------------------------------------------------------------------------------------------
Plans found by both                                       211                211                306                306
Faster when both found a plan                     132 (62.6%)         79 (37.4%)         65 (21.2%)        241 (78.8%)
Plan found when the other did not                          32                 25                 47                181
Median runtime when both found a plan                  8.98 s             8.29 s             7.65 s             3.45 s
Total runtime across shared solves                29,838.78 s        23,091.16 s        45,968.44 s        20,262.02 s
Shorter plan when both found one                   75 (35.5%)           0 (0.0%)         32 (10.5%)        125 (40.8%)
Same plan length when both found one              136 (64.5%)        136 (64.5%)        149 (48.7%)        149 (48.7%)
Median plan length when both found one                     12                 13                 20                 18
Total plan length across shared solves                  3,058              3,281             11,830             10,644
```

## Where the timeouts died

```
Killed during                                       Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Searching for the abstract plan                     785 (83%)          358 (46%)
Guided concrete search                               94 (10%)          344 (44%)
Unguided concrete search                              68 (7%)           84 (11%)
Total                                                     947                786
```

## How the successes were solved

```
Solved by                                           Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstract plan refined directly                      129 (55%)          210 (59%)
Refined after switching some actions off             91 (39%)          127 (36%)
Abstract plan discarded, solved above it              16 (7%)            16 (5%)
Total                                                     236                353
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Deletes relaxed                                     Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
None                                                  14 (6%)           42 (12%)
1 to 4                                              163 (74%)          239 (71%)
5 to 9                                               22 (10%)           34 (10%)
10 to 19                                              19 (9%)            20 (6%)
20 or more                                             2 (1%)             2 (1%)
Total                                                     220                337
```

## Plans found by domain

```
Domain                           Problems        ASP  Abs + ASP   Abs + FDFD (LM-cut)
-------------------------------------------------------------------------------------
agricola-opt18-strips                  20          8          3          0          0
agricola-sat18-strips                  20          0          0          0          0
airport                                42         11         11         11         22
barman-opt11-strips                    20          0          0          0          4
barman-opt14-strips                    14          0          0          0          0
barman-sat11-strips                    20          0          0          0          0
barman-sat14-strips                    20          0          0          0          0
childsnack-opt14-strips                20          0          0          0          0
childsnack-sat14-strips                20          0          0          0          0
depot                                  22          4          2          2          8
driverlog                              20          9         11         12         14
elevators-opt08-strips                 20          5          7         12         12
elevators-opt11-strips                 13          5          6         11         11
elevators-sat08-strips                 30          1          2          4          2
elevators-sat11-strips                 14          0          0          0          0
floortile-opt11-strips                 20          2          0          2          7
floortile-opt14-strips                 20          0          0          0          7
floortile-sat11-strips                 20          0          0          0          6
grid                                    5          2          3          2          2
gripper                                20          3          3          3          7
hiking-opt14-strips                    20         12         13         11          9
hiking-sat14-strips                    20          2          3          0          2
logistics00                            28         10         12         12         20
logistics98                            35          3          3          2          6
miconic                                11          1          2         11         11
mprime                                 35         34         33         27         24
mystery                                28         19         19         19         17
nomystery-opt11-strips                 20         10          7         14         18
nomystery-sat11-strips                 14          2          2          5          9
openstacks-opt08-strips                28          0          2          7         21
openstacks-opt11-strips                20          0          0          5         18
openstacks-opt14-strips                14          0          0          0          2
openstacks-sat08-strips                29          2          2         23         12
openstacks-sat11-strips                15          0          0          4          0
pipesworld-notankage                   49         13         11         13         17
pipesworld-tankage                     49          9          8          7         11
quantum-layout-opt23-strips             7          4          3          3          4
quantum-layout-sat23-strips             7          4          1          1          4
satellite                              36          6          6         10         12
sokoban-opt08-strips                   29          4          4         11         29
sokoban-opt11-strips                   19          1          1          6         19
sokoban-sat08-strips                   29          2          2         14         27
sokoban-sat11-strips                    5          0          0          4          4
tetris-opt14-strips                    16          2          0          0          5
tpp                                    29          4          4          4          6
transport-opt08-strips                 30         10         10         12         11
transport-opt11-strips                 20          5          5          8          6
transport-opt14-strips                 20          3          4          4          6
transport-sat08-strips                 30          5          6          6          6
transport-sat11-strips                 20          0          0          0          0
visitall-opt11-strips                   1          1          1          1          1
woodworking-opt08-strips               28          9          9         15         18
woodworking-opt11-strips               20          6          6         11         14
woodworking-sat08-strips               27          3          2         13          5
woodworking-sat11-strips               11          0          0          0          0
zenotravel                             18          7          7         11         11
Total                                1217        243        236        353        487
```
