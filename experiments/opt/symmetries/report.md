# Benchmark report

2026-10-29 09:45 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  122 (23.6%)  128 (24.7%)  193 (37.3%)
Timeouts                        389 (75.1%)  395 (76.3%)  390 (75.3%)  324 (62.5%)
Out of memory                      1 (0.2%)     1 (0.2%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     122          122          124          124
Faster                          107 (87.7%)   15 (12.3%)     8 (6.5%)  116 (93.5%)
Found when the other did not              6            0            4           69
Median runtime                       8.72 s      13.75 s       7.94 s       2.70 s
Total runtime                   14,092.05 s  16,603.21 s   9,286.63 s   2,859.72 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               122 (100.0%) 122 (100.0%) 124 (100.0%) 124 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,115        2,115        2,627        2,627
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   330 (84%)    267 (68%)
Guided concrete search               4 (1%)       0 (0%)
Unguided concrete search           61 (15%)    123 (32%)
Total                                   395          390
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   55 (45%)     60 (47%)
Refined, some actions off           10 (8%)     17 (13%)
Solved above the abstract plan     57 (47%)     51 (40%)
Total                                   122          128
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (20%)     23 (30%)
1 to 4                             43 (66%)     42 (55%)
5 to 9                               5 (8%)       6 (8%)
10 to 19                             2 (3%)       4 (5%)
20 or more                           2 (3%)       2 (3%)
Total                                    65           77
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         7         0         0
airport                             19        11        11        19        19
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                                9         1         1         2         3
driverlog                           13         7         6         7        10
elevators-opt08-strips               4         0         0         0         3
elevators-opt11-strips               2         0         0         0         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        12        13         9
logistics00                         19         8         8        12        15
logistics98                         31         1         0         1         4
miconic                             11         1         1         1        11
mprime                              21        20        20        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         3         3         8
openstacks-opt08-strips             28         0         0         0         8
openstacks-opt11-strips             20         0         0         0         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10         9         9        13
pipesworld-tankage                  47         8         8         8         9
quantum-layout-opt23-strips          7         4         4         4         4
satellite                           34         5         5         5        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         4         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         1         1         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         0         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         4         7
Total                              518       128       122       128       193
```
