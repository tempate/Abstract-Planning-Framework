# Benchmark report

2026-11-03 10:45 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  122 (23.6%)  136 (26.3%)  193 (37.3%)
Timeouts                        389 (75.1%)  392 (75.7%)  381 (73.6%)  324 (62.5%)
Out of memory                      1 (0.2%)     4 (0.8%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          129          129
Faster                          105 (86.8%)   16 (13.2%)    12 (9.3%)  117 (90.7%)
Found when the other did not              7            1            7           64
Median runtime                       8.48 s      18.74 s       9.60 s       2.74 s
Total runtime                   13,260.22 s  16,858.00 s  10,366.36 s   5,549.83 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               121 (100.0%) 121 (100.0%) 129 (100.0%) 129 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,096        2,096        2,766        2,766
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   339 (86%)    260 (68%)
Guided concrete search              21 (5%)    100 (26%)
Unguided concrete search            32 (8%)      21 (6%)
Total                                   392          381
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   75 (61%)     90 (66%)
Refined, some actions off            5 (4%)       6 (4%)
Solved above the abstract plan     42 (34%)     40 (29%)
Total                                   122          136
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (16%)     23 (24%)
1 to 4                             29 (36%)     36 (38%)
5 to 9                             19 (24%)     15 (16%)
10 to 19                             6 (8%)       8 (8%)
20 or more                         13 (16%)     14 (15%)
Total                                    80           96
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
agricola-opt18-strips (20)           8         7         0         0
airport (19)                        11        11        19        19
barman-opt11-strips (20)             0         0         0         4
barman-opt14-strips (14)             0         0         0         0
childsnack-opt14-strips (20)         0         0         0         0
depot (9)                            1         1         4         3
driverlog (13)                       7         6         7        10
elevators-opt08-strips (4)           0         0         0         3
elevators-opt11-strips (2)           0         0         0         2
gripper (20)                         3         3         3         7
hiking-opt14-strips (20)            12        13        13         9
logistics00 (19)                     8         8        12        15
logistics98 (31)                     1         0         2         4
miconic (11)                         1         1         1        11
mprime (21)                         20        20        16        16
mystery (16)                        10        10         9         8
nomystery-opt11-strips (10)          4         2         2         8
openstacks-opt08-strips (28)         0         0         0         8
openstacks-opt11-strips (20)         0         0         0         5
openstacks-opt14-strips (14)         0         0         0         0
pipesworld-notankage (34)           10         9        10        13
pipesworld-tankage (47)              8         8        10         9
quantum-layout-opt23-strips (7)         4         4         4         4
satellite (34)                       5         5         7        10
sokoban-opt08-strips (3)             1         1         2         2
sokoban-opt11-strips (2)             1         1         2         2
tpp (29)                             4         4         4         6
transport-opt08-strips (4)           3         3         3         3
transport-opt14-strips (4)           1         1         1         2
visitall-opt11-strips (1)            1         1         1         1
woodworking-opt08-strips (5)         0         0         0         1
woodworking-opt11-strips (4)         0         0         0         1
zenotravel (13)                      4         3         4         7
Total (518)                        128       122       136       193
```
