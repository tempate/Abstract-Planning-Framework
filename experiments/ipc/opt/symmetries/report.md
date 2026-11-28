# Benchmark report

2026-11-28 09:19 — experiments/ipc/opt/symmetries/results.csv

661 problems compared over asp, abs-asp, abs-lmcut, lmcut, lmcut-symmetry-pruning, rnd-g

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut       LMcut+        rnd-g
------------------------------------------------------------------------------------------------------------
Plans found                     168 (25.4%)  170 (25.7%)  239 (36.2%)  291 (44.0%)  333 (50.4%)  213 (32.2%)
Timeouts                        491 (74.3%)  490 (74.1%)  420 (63.5%)  368 (55.7%)  325 (49.2%)  268 (40.5%)
Out of memory                      1 (0.2%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)  171 (25.9%)
Others                             1 (0.2%)     1 (0.2%)     2 (0.3%)     2 (0.3%)     2 (0.3%)     9 (1.4%)
Total problems                          661          661          661          661          661          661
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     163          163          234          234
Faster                          132 (81.0%)   31 (19.0%)    23 (9.8%)  211 (90.2%)
Found when the other did not              5            7            5           57
Median runtime                       5.14 s       6.73 s       5.53 s       2.85 s
Total runtime                   15,181.02 s  14,941.15 s  22,357.86 s  18,395.07 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               163 (100.0%) 163 (100.0%) 234 (100.0%) 234 (100.0%)
Median plan length                       11           11           17           17
Total plan length                     2,533        2,533        9,532        9,532
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   440 (90%)    304 (72%)
Guided concrete search              18 (4%)     94 (22%)
Unguided concrete search            32 (7%)      22 (5%)
Total                                   490          420
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   91 (54%)    153 (64%)
Refined, some actions off          39 (23%)     47 (20%)
Solved above the abstract plan     40 (24%)     39 (16%)
Total                                   170          239
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               51 (39%)    116 (58%)
1 to 4                             40 (31%)     49 (24%)
5 to 9                             19 (15%)      15 (8%)
10 to 19                             8 (6%)       8 (4%)
20 or more                          12 (9%)      12 (6%)
Total                                   130          200
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut    LMcut+     rnd-g
----------------------------------------------------------------------------------------
agricola-opt18-strips (20)           7        10         0         0         0         0
airport (50)                        11        11        27        27        28        17
barman-opt11-strips (20)             0         0         0         4         8         4
barman-opt14-strips (14)             0         0         0         0         3         0
childsnack-opt14-strips (20)         0         0         0         0         6         0
depot (9)                            1         1         3         2         3         1
driverlog (14)                       8         7         8        11        11        11
elevators-opt08-strips (4)           0         0         0         2         2         1
elevators-opt11-strips (2)           0         0         0         2         2         1
gripper (20)                         3         3         3         7        20         7
hiking-opt14-strips (20)            11        14        12         9        13        10
logistics00 (19)                     8         8        12        15        15         8
logistics98 (31)                     1         0         2         4         4         0
miconic (11)                         1         1         1        11        11         5
movie (30)                          30        30        30        30        30        30
mprime (21)                         20        20        16        16        15        11
mystery (17)                        10        10         9         8         8         7
nomystery-opt11-strips (10)          4         2         2         8         5         6
openstacks-opt08-strips (28)         0         0         0         7         8         6
openstacks-opt11-strips (20)         0         0         0         4         5         3
openstacks-opt14-strips (14)         0         0         0         0         0         0
parcprinter-08-strips (10)           2         2         7         7         7         3
parcprinter-opt11-strips (6)         1         1         5         5         5         2
pipesworld-notankage (36)           10        10        12        14        15        12
pipesworld-tankage (47)              8         9         9         9        13        10
quantum-layout-opt23-strips (7)         4         4         4         4         4         0
satellite (34)                       5         5         7        10        11         5
sokoban-opt08-strips (30)            4         4        24        24        28        18
sokoban-opt11-strips (20)            1         1        19        19        20        15
tpp (29)                             4         4         4         6         7         5
transport-opt08-strips (4)           3         3         3         3         3         3
transport-opt14-strips (4)           1         1         1         2         2         2
visitall-opt11-strips (1)            1         1         1         1         1         1
woodworking-opt08-strips (15)         3         3         8         8         7         3
woodworking-opt11-strips (11)         2         2         6         6         6         2
zenotravel (13)                      4         3         4         6         7         4
Total (661)                        168       170       239       291       333       213
```
