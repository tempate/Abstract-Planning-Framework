# Benchmark report

2026-10-30 16:36 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  122 (23.6%)  130 (25.1%)  193 (37.3%)
Timeouts                        389 (75.1%)  393 (75.9%)  387 (74.7%)  324 (62.5%)
Out of memory                      1 (0.2%)     3 (0.6%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          125          125
Faster                          108 (89.3%)   13 (10.7%)    10 (8.0%)  115 (92.0%)
Found when the other did not              7            1            5           68
Median runtime                       8.48 s      21.31 s       8.97 s       2.72 s
Total runtime                   13,260.22 s  20,296.04 s   8,774.59 s   3,329.37 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               121 (100.0%) 121 (100.0%) 125 (100.0%) 125 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,096        2,096        2,648        2,648
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   344 (88%)    267 (69%)
Guided concrete search              19 (5%)     98 (25%)
Unguided concrete search            30 (8%)      22 (6%)
Total                                   393          387
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   72 (59%)     83 (64%)
Refined, some actions off            5 (4%)       7 (5%)
Solved above the abstract plan     45 (37%)     40 (31%)
Total                                   122          130
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (17%)     23 (26%)
1 to 4                             28 (36%)     31 (34%)
5 to 9                             19 (25%)     14 (16%)
10 to 19                             6 (8%)     10 (11%)
20 or more                         11 (14%)     12 (13%)
Total                                    77           90
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
depot (9)                            1         1         2         3
driverlog (13)                       7         6         7        10
elevators-opt08-strips (4)           0         0         0         3
elevators-opt11-strips (2)           0         0         0         2
gripper (20)                         3         3         3         7
hiking-opt14-strips (20)            12        13        13         9
logistics00 (19)                     8         8        12        15
logistics98 (31)                     1         0         1         4
miconic (11)                         1         1         1        11
mprime (21)                         20        20        16        16
mystery (16)                        10        10         8         8
nomystery-opt11-strips (10)          4         2         2         8
openstacks-opt08-strips (28)         0         0         0         8
openstacks-opt11-strips (20)         0         0         0         5
openstacks-opt14-strips (14)         0         0         0         0
pipesworld-notankage (34)           10         9        10        13
pipesworld-tankage (47)              8         8        10         9
quantum-layout-opt23-strips (7)         4         4         4         4
satellite (34)                       5         5         5        10
sokoban-opt08-strips (3)             1         1         2         2
sokoban-opt11-strips (2)             1         1         2         2
tpp (29)                             4         4         4         6
transport-opt08-strips (4)           3         3         3         3
transport-opt14-strips (4)           1         1         1         2
visitall-opt11-strips (1)            1         1         1         1
woodworking-opt08-strips (5)         0         0         0         1
woodworking-opt11-strips (4)         0         0         0         1
zenotravel (13)                      4         3         4         7
Total (518)                        128       122       130       193
```
