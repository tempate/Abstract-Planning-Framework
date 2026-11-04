# Benchmark report

2026-11-03 10:45 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     131 (23.5%)  146 (26.2%)  333 (59.8%)  507 (91.0%)
Timeouts                        405 (72.7%)  396 (71.1%)  122 (21.9%)    35 (6.3%)
Out of memory                     21 (3.8%)    15 (2.7%)  101 (18.1%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     125          125          330          330
Faster                           96 (76.8%)   29 (23.2%)    14 (4.2%)  316 (95.8%)
Found when the other did not              6           21            3          177
Median runtime                       6.72 s      12.80 s      16.29 s       3.65 s
Total runtime                   10,607.39 s  14,754.34 s  21,277.29 s   3,624.78 s
Shorter plan                     91 (72.8%)    12 (9.6%)   51 (15.5%)  215 (65.2%)
Same plan length                 22 (17.6%)   22 (17.6%)   64 (19.4%)   64 (19.4%)
Median plan length                       16           28         54.5           44
Total plan length                     2,621        3,675       24,508       20,647
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   358 (90%)     13 (11%)
Guided concrete search              23 (6%)    104 (85%)
Unguided concrete search            15 (4%)       5 (4%)
Total                                   396          122
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                  118 (81%)    312 (94%)
Refined, some actions off          27 (18%)      15 (5%)
Solved above the abstract plan       1 (1%)       6 (2%)
Total                                   146          333
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (10%)     37 (11%)
1 to 4                             74 (51%)    184 (56%)
5 to 9                             25 (17%)     33 (10%)
10 to 19                            10 (7%)     41 (13%)
20 or more                         21 (14%)     32 (10%)
Total                                   145          327
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
agricola-sat18-strips (20)           0         0         0        12
airport (19)                        14        14        19        19
barman-sat11-strips (20)             0         0         0        20
barman-sat14-strips (20)             0         0         0        20
childsnack-sat14-strips (20)         0         2         8         6
depot (9)                            2         3         6         8
driverlog (13)                       7         8        13        13
elevators-sat08-strips (15)          0         0         8        15
elevators-sat11-strips (14)          0         0         1        14
gripper (20)                         4         5         5        20
hiking-sat14-strips (20)             2         7        15        20
logistics00 (19)                    10         9        19        19
logistics98 (31)                     4         6        22        31
miconic (11)                         2         3        11        11
mprime (21)                         21        21        21        21
mystery (16)                        10        10        10        10
nomystery-sat11-strips (14)          4         4        10         9
openstacks-sat08-strips (29)         4         5        23        29
openstacks-sat11-strips (15)         0         0         4        15
openstacks-sat14-strips (12)         0         0         0        12
pipesworld-notankage (34)           15        15        18        27
pipesworld-tankage (47)             10        14        37        40
quantum-layout-sat23-strips (7)         3         2         7         7
satellite (34)                       8         5        21        34
sokoban-sat08-strips (7)             1         1         6         6
sokoban-sat11-strips (5)             0         0         4         4
tpp (29)                             5         7        14        29
transport-sat08-strips (2)           1         1         1         2
transport-sat11-strips (2)           0         0         0         2
woodworking-sat08-strips (8)         0         0         7         8
woodworking-sat11-strips (11)         0         0        11        11
zenotravel (13)                      4         4        12        13
Total (557)                        131       146       333       507
```
