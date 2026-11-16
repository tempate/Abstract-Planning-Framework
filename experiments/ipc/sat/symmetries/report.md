# Benchmark report

2026-11-19 12:26 — experiments/ipc/sat/symmetries/results.csv

677 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     170 (25.1%)  187 (27.6%)  463 (68.4%)  610 (90.1%)
Timeouts                        487 (71.9%)  474 (70.0%)  140 (20.7%)    51 (7.5%)
Out of memory                     19 (2.8%)    15 (2.2%)   72 (10.6%)    14 (2.1%)
Others                             1 (0.1%)     1 (0.1%)     2 (0.3%)     2 (0.3%)
Total problems                          677          677          677          677
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     167          167          459          459
Faster                          112 (67.1%)   55 (32.9%)   53 (11.5%)  406 (88.5%)
Found when the other did not              3           20            4          151
Median runtime                       4.94 s       5.14 s       6.76 s       3.50 s
Total runtime                   16,664.05 s  17,182.89 s  17,251.13 s   8,616.16 s
Shorter plan                     60 (35.9%)   21 (12.6%)   74 (16.1%)  131 (28.5%)
Same plan length                 86 (51.5%)   86 (51.5%)  254 (55.3%)  254 (55.3%)
Median plan length                       16           16           56           53
Total plan length                     4,332        5,006       40,876       39,307
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   436 (92%)     29 (21%)
Guided concrete search              23 (5%)    103 (74%)
Unguided concrete search            15 (3%)       8 (6%)
Total                                   474          140
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                  161 (86%)    443 (96%)
Refined, some actions off          24 (13%)      14 (3%)
Solved above the abstract plan       2 (1%)       6 (1%)
Total                                   187          463
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               58 (31%)    135 (30%)
1 to 4                             71 (38%)    214 (47%)
5 to 9                             26 (14%)      36 (8%)
10 to 19                             9 (5%)     45 (10%)
20 or more                         21 (11%)      27 (6%)
Total                                   185          457
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
agricola-sat18-strips (20)           0         0        12        12
airport (50)                        16        16        34        34
barman-sat11-strips (20)             0         0         0        20
barman-sat14-strips (20)             0         0         0        20
childsnack-sat14-strips (20)         0         1         8         6
depot (9)                            2         3         6         8
driverlog (14)                       8         9        14        14
elevators-sat08-strips (15)          0         0         8        15
elevators-sat11-strips (14)          0         0         0        14
gripper (20)                         4         5         5        20
hiking-sat14-strips (20)             2         7        15        20
logistics00 (19)                     9         9        19        19
logistics98 (31)                     4         6        26        31
miconic (11)                         2         3        11        11
movie (30)                          30        30        30        30
mprime (21)                         21        21        21        21
mystery (17)                        10        10        10        10
nomystery-sat11-strips (14)          4         4        10         9
openstacks-sat08-strips (29)         4         5        23        29
openstacks-sat11-strips (15)         0         0         4        15
openstacks-sat14-strips (12)         0         0         0        12
parcprinter-08-strips (10)           3         3        10        10
parcprinter-sat11-strips (4)         0         0         4         4
pipesworld-notankage (36)           17        17        20        29
pipesworld-tankage (47)             10        14        40        40
quantum-layout-sat23-strips (7)         3         2         7         7
satellite (34)                       6         5        29        34
sokoban-sat08-strips (30)            4         4        29        29
sokoban-sat11-strips (20)            1         1        19        19
tpp (29)                             5         7        14        29
transport-sat08-strips (2)           1         1         1         2
transport-sat11-strips (2)           0         0         0         2
woodworking-sat08-strips (11)         0         0        10        11
woodworking-sat11-strips (11)         0         0        11        11
zenotravel (13)                      4         4        13        13
Total (677)                        170       187       463       610
```
