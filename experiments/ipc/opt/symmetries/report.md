# Benchmark report

2026-11-12 10:38 — experiments/ipc/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     126 (24.3%)  126 (24.3%)  134 (25.9%)  193 (37.3%)
Timeouts                        391 (75.5%)  391 (75.5%)  383 (73.9%)  324 (62.5%)
Out of memory                      1 (0.2%)     1 (0.2%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          128          128
Faster                           98 (81.0%)   23 (19.0%)   14 (10.9%)  114 (89.1%)
Found when the other did not              5            5            6           65
Median runtime                       9.64 s      11.54 s       7.78 s       2.75 s
Total runtime                   15,289.75 s  16,765.05 s   9,647.37 s   5,547.79 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               121 (100.0%) 121 (100.0%) 128 (100.0%) 128 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,138        2,138        2,744        2,744
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   342 (87%)    296 (77%)
Guided concrete search              17 (4%)     76 (20%)
Unguided concrete search            32 (8%)      11 (3%)
Total                                   391          383
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   76 (60%)     86 (64%)
Refined, some actions off            8 (6%)       8 (6%)
Solved above the abstract plan     42 (33%)     40 (30%)
Total                                   126          134
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (15%)     23 (24%)
1 to 4                             32 (38%)     34 (36%)
5 to 9                             20 (24%)     15 (16%)
10 to 19                             7 (8%)      9 (10%)
20 or more                         12 (14%)     13 (14%)
Total                                    84           94
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
agricola-opt18-strips (20)           8        11         0         0
airport (19)                        11        11        19        19
barman-opt11-strips (20)             0         0         0         4
barman-opt14-strips (14)             0         0         0         0
childsnack-opt14-strips (20)         0         0         0         0
depot (9)                            1         1         4         3
driverlog (13)                       7         6         7        10
elevators-opt08-strips (4)           0         0         0         3
elevators-opt11-strips (2)           0         0         0         2
gripper (20)                         3         3         3         7
hiking-opt14-strips (20)            11        13        13         9
logistics00 (19)                     8         8        12        15
logistics98 (31)                     1         0         1         4
miconic (11)                         1         1         1        11
mprime (21)                         20        20        16        16
mystery (16)                        10        10         8         8
nomystery-opt11-strips (10)          4         2         2         8
openstacks-opt08-strips (28)         0         0         0         8
openstacks-opt11-strips (20)         0         0         0         5
openstacks-opt14-strips (14)         0         0         0         0
pipesworld-notankage (34)            9         9        10        13
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
Total (518)                        126       126       134       193
```
