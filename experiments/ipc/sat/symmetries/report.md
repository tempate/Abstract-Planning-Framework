# Benchmark report

2026-11-11 09:20 — experiments/ipc/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     128 (23.0%)  145 (26.0%)  358 (64.3%)  507 (91.0%)
Timeouts                        410 (73.6%)  396 (71.1%)  123 (22.1%)    35 (6.3%)
Out of memory                     19 (3.4%)    16 (2.9%)   75 (13.5%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     125          125          355          355
Faster                           90 (72.0%)   35 (28.0%)    14 (3.9%)  341 (96.1%)
Found when the other did not              3           20            3          152
Median runtime                       8.35 s       9.42 s      11.97 s       3.84 s
Total runtime                   13,780.32 s  14,023.54 s  21,135.87 s   6,142.87 s
Shorter plan                     53 (42.4%)   15 (12.0%)   68 (19.2%)  160 (45.1%)
Same plan length                 57 (45.6%)   57 (45.6%)  127 (35.8%)  127 (35.8%)
Median plan length                       16           19           56           49
Total plan length                     2,621        3,270       27,943       25,439
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   358 (90%)     13 (11%)
Guided concrete search              23 (6%)    105 (85%)
Unguided concrete search            15 (4%)       5 (4%)
Total                                   396          123
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                  118 (81%)    337 (94%)
Refined, some actions off          26 (18%)      15 (4%)
Solved above the abstract plan       1 (1%)       6 (2%)
Total                                   145          358
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (10%)     37 (11%)
1 to 4                             73 (51%)    201 (57%)
5 to 9                             25 (17%)     39 (11%)
10 to 19                            10 (7%)     43 (12%)
20 or more                         21 (15%)      32 (9%)
Total                                   144          352
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
agricola-sat18-strips (20)           0         0        10        12
airport (19)                        14        14        19        19
barman-sat11-strips (20)             0         0         0        20
barman-sat14-strips (20)             0         0         0        20
childsnack-sat14-strips (20)         0         1         8         6
depot (9)                            2         3         6         8
driverlog (13)                       7         8        13        13
elevators-sat08-strips (15)          0         0         8        15
elevators-sat11-strips (14)          0         0         0        14
gripper (20)                         4         5         5        20
hiking-sat14-strips (20)             2         7        15        20
logistics00 (19)                     9         9        19        19
logistics98 (31)                     4         6        28        31
miconic (11)                         2         3        11        11
mprime (21)                         21        21        21        21
mystery (16)                        10        10        10        10
nomystery-sat11-strips (14)          4         4        10         9
openstacks-sat08-strips (29)         4         5        23        29
openstacks-sat11-strips (15)         0         0         4        15
openstacks-sat14-strips (12)         0         0         0        12
pipesworld-notankage (34)           15        15        18        27
pipesworld-tankage (47)             10        14        39        40
quantum-layout-sat23-strips (7)         3         2         7         7
satellite (34)                       6         5        28        34
sokoban-sat08-strips (7)             1         1         6         6
sokoban-sat11-strips (5)             0         0         4         4
tpp (29)                             5         7        14        29
transport-sat08-strips (2)           1         1         1         2
transport-sat11-strips (2)           0         0         0         2
woodworking-sat08-strips (8)         0         0         7         8
woodworking-sat11-strips (11)         0         0        11        11
zenotravel (13)                      4         4        13        13
Total (557)                        128       145       358       507
```
