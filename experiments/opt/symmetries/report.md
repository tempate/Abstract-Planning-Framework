# Benchmark report

2026-10-20 09:04 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)   91 (17.6%)   92 (17.8%)  193 (37.3%)
Timeouts                        389 (75.1%)  415 (80.1%)  425 (82.0%)  324 (62.5%)
Out of memory                      1 (0.2%)    12 (2.3%)     1 (0.2%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                      91           91           92           92
Faster                           88 (96.7%)     3 (3.3%)     8 (8.7%)   84 (91.3%)
Found when the other did not             37            0            0          101
Median runtime                       4.19 s      12.60 s      13.36 s       2.57 s
Total runtime                    1,835.65 s  13,329.22 s  13,739.59 s   1,288.01 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length                91 (100.0%)  91 (100.0%)  92 (100.0%)  92 (100.0%)
Median plan length                       10           10           11           11
Total plan length                     1,143        1,143        1,248        1,248
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   325 (78%)    266 (63%)
Guided concrete search             90 (22%)    159 (37%)
Total                                   415          425
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   86 (95%)     87 (95%)
Refined, some actions off            0 (0%)       0 (0%)
Solved above the abstract plan       5 (5%)       5 (5%)
Total                                    91           92
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (15%)     14 (16%)
1 to 4                             58 (67%)     57 (66%)
5 to 9                               4 (5%)       7 (8%)
10 to 19                           11 (13%)      9 (10%)
20 or more                           0 (0%)       0 (0%)
Total                                    86           87
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         0         0         0
airport                             19        11        11        12        19
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                                9         1         1         1         3
driverlog                           13         7         4         5        10
elevators-opt08-strips               4         0         0         0         3
elevators-opt11-strips               2         0         0         0         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12         7         7         9
logistics00                         19         8         5         6        15
logistics98                         31         1         0         1         4
miconic                             11         1         0         0        11
mprime                              21        20        19        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         2         2         8
openstacks-opt08-strips             28         0         0         0         8
openstacks-opt11-strips             20         0         0         0         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10         5         6        13
pipesworld-tankage                  47         8         6         6         9
quantum-layout-opt23-strips          7         4         2         2         4
satellite                           34         5         3         3        10
sokoban-opt08-strips                 3         1         1         1         2
sokoban-opt11-strips                 2         1         1         1         2
tpp                                 29         4         4         4         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         1         1         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         0         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         2         3         7
Total                              518       128        91        92       193
```
