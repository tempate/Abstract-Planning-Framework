# Benchmark report

2026-10-27 09:04 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  129 (24.9%)  144 (27.8%)  193 (37.3%)
Timeouts                        389 (75.1%)  386 (74.5%)  374 (72.2%)  324 (62.5%)
Out of memory                      1 (0.2%)     3 (0.6%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     122          122          140          140
Faster                           94 (77.0%)   28 (23.0%)   28 (20.0%)  112 (80.0%)
Found when the other did not              6            7            4           53
Median runtime                       8.72 s      10.60 s       6.74 s       2.92 s
Total runtime                   14,631.66 s  15,124.78 s  14,700.69 s   7,916.53 s
Shorter plan                       7 (5.7%)     0 (0.0%)     0 (0.0%)     9 (6.4%)
Same plan length                115 (94.3%)  115 (94.3%)  131 (93.6%)  131 (93.6%)
Median plan length                       12           13           16         15.5
Total plan length                     2,114        2,134        3,262        3,186
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   325 (84%)    267 (71%)
Guided concrete search              30 (8%)     91 (24%)
Unguided concrete search            31 (8%)      16 (4%)
Total                                   386          374
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   64 (50%)     83 (58%)
Refined, some actions off          20 (16%)     18 (12%)
Solved above the abstract plan     45 (35%)     43 (30%)
Total                                   129          144
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (15%)     23 (23%)
1 to 4                             52 (62%)     63 (62%)
5 to 9                             10 (12%)       8 (8%)
10 to 19                             7 (8%)       5 (5%)
20 or more                           2 (2%)       2 (2%)
Total                                    84          101
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         8         0         0
airport                             19        11        11        19        19
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                                9         1         1         2         3
driverlog                           13         7         6         7        10
elevators-opt08-strips               4         0         0         0         3
elevators-opt11-strips               2         0         0         0         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        13         9
logistics00                         19         8         9        12        15
logistics98                         31         1         0         3         4
miconic                             11         1         1         2        11
mprime                              21        20        20        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         2         2         8
openstacks-opt08-strips             28         0         1         6         8
openstacks-opt11-strips             20         0         0         4         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10        11        10        13
pipesworld-tankage                  47         8        10         8         9
quantum-layout-opt23-strips          7         4         4         4         4
satellite                           34         5         5         7        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         4         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         1         1         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         0         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         5         7
Total                              518       128       129       144       193
```
