# Benchmark report

2026-11-09 09:01 — experiments/ipc/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     126 (24.3%)  126 (24.3%)  135 (26.1%)  193 (37.3%)
Timeouts                        391 (75.5%)  391 (75.5%)  382 (73.7%)  324 (62.5%)
Out of memory                      1 (0.2%)     1 (0.2%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          129          129
Faster                           98 (81.0%)   23 (19.0%)    12 (9.3%)  117 (90.7%)
Found when the other did not              5            5            6           64
Median runtime                       9.64 s      11.25 s       7.76 s       2.74 s
Total runtime                   15,289.75 s  16,931.62 s  11,224.77 s   5,549.83 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               121 (100.0%) 121 (100.0%) 129 (100.0%) 129 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,138        2,138        2,766        2,766
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   343 (88%)    297 (78%)
Guided concrete search              16 (4%)     74 (19%)
Unguided concrete search            32 (8%)      11 (3%)
Total                                   391          382
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   79 (63%)     89 (66%)
Refined, some actions off            5 (4%)       6 (4%)
Solved above the abstract plan     42 (33%)     40 (30%)
Total                                   126          135
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (15%)     23 (24%)
1 to 4                             32 (38%)     35 (37%)
5 to 9                             20 (24%)     15 (16%)
10 to 19                             6 (7%)       8 (8%)
20 or more                         13 (15%)     14 (15%)
Total                                    84           95
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
logistics98 (31)                     1         0         2         4
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
Total (518)                        126       126       135       193
```
