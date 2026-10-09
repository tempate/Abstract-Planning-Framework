# Benchmark report

2026-10-09 14:57 — experiments/plan/symmetries-min-gaps/results.csv

667 problems compared over abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                              Abs + ASP           Abs + FD        FD (LM-cut)
---------------------------------------------------------------------------------------------------
Plans found                                       114 (17.1%)        186 (27.9%)        215 (32.2%)
Timeouts                                          540 (81.0%)        392 (58.8%)        451 (67.6%)
Out of memory                                       13 (1.9%)         88 (13.2%)           0 (0.0%)
Others                                               0 (0.0%)           1 (0.1%)           1 (0.1%)
Total problems                                            667                667                667
```

## Where the timeouts died

```
Killed during                                       Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Searching for the abstract plan                     450 (83%)            11 (3%)
Guided concrete search                               56 (10%)          340 (87%)
Unguided concrete search                              34 (6%)           41 (10%)
Total                                                     540                392
```

## How the successes were solved

```
Solved by                                           Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
Abstract plan refined directly                       71 (62%)          129 (69%)
Refined after switching some actions off             34 (30%)           48 (26%)
Abstract plan discarded, solved above it               9 (8%)             9 (5%)
Total                                                     114                186
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Deletes relaxed                                     Abs + ASP           Abs + FD
--------------------------------------------------------------------------------
None                                                 12 (11%)           28 (16%)
1 to 4                                               71 (68%)          125 (71%)
5 to 9                                                 8 (8%)            10 (6%)
10 to 19                                             13 (12%)            13 (7%)
20 or more                                             1 (1%)             1 (1%)
Total                                                     105                177
```

## Plans found by domain

```
Domain                           Problems  Abs + ASP   Abs + FDFD (LM-cut)
--------------------------------------------------------------------------
agricola-sat18-strips                  20          0          0          0
airport                                19         11         11         19
barman-sat11-strips                    20          0          0          0
barman-sat14-strips                    20          0          0          0
childsnack-sat14-strips                20          0          0          0
depot                                   9          1          1          3
driverlog                              13          8          9         10
elevators-sat08-strips                 30          2          4          2
elevators-sat11-strips                 14          0          0          0
floortile-sat11-strips                 20          0          0          6
gripper                                20          3          3          7
hiking-sat14-strips                    20          3          0          2
logistics00                            19         10         10         15
logistics98                            31          1          1          4
miconic                                11          2         11         11
mprime                                 21         20         21         16
mystery                                16         10          9          8
nomystery-sat11-strips                 14          2          5          9
openstacks-sat08-strips                29          2         23         12
openstacks-sat11-strips                15          0          4          0
pipesworld-notankage                   34          8          8         13
pipesworld-tankage                     47          7          7          9
quantum-layout-sat23-strips             7          1          1          4
satellite                              34          5         11         10
sokoban-sat08-strips                   29          2         14         27
sokoban-sat11-strips                    5          0          4          4
tpp                                    29          4          4          6
transport-sat08-strips                 30          6          6          6
transport-sat11-strips                 20          0          0          0
woodworking-sat08-strips               27          2         13          5
woodworking-sat11-strips               11          0          0          0
zenotravel                             13          4          6          7
Total                                 667        114        186        215
```
