# Benchmark report

2026-11-26 05:58 — experiments/ipc/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama, lama-symmetry-pruning, rnd-g; 120 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA        LAMA+        rnd-g
------------------------------------------------------------------------------------------------------------
Plans found                     128 (23.0%)  145 (26.0%)  358 (64.3%)  507 (91.0%)  521 (93.5%)  217 (39.0%)
Timeouts                        410 (73.6%)  396 (71.1%)  123 (22.1%)    35 (6.3%)    33 (5.9%)  183 (32.9%)
Out of memory                     19 (3.4%)    16 (2.9%)   75 (13.5%)    14 (2.5%)     1 (0.2%)  149 (26.8%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)     2 (0.4%)     8 (1.4%)
Total problems                          557          557          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     125          125          355          355
Faster                           87 (69.6%)   38 (30.4%)     9 (2.5%)  346 (97.5%)
Found when the other did not              3           20            3          152
Median runtime                       7.45 s       9.42 s      11.97 s       3.50 s
Total runtime                   13,493.23 s  14,023.54 s  21,135.87 s   6,387.69 s
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
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA     LAMA+     rnd-g
----------------------------------------------------------------------------------------
agricola-sat18-strips (20)           0         0        10        12        11         5
airport (19)                        14        14        19        19        19        16
barman-sat11-strips (20)             0         0         0        20        20         0
barman-sat14-strips (20)             0         0         0        20        20         0
childsnack-sat14-strips (20)         0         1         8         6        19         0
depot (9)                            2         3         6         8         9         4
driverlog (13)                       7         8        13        13        13        10
elevators-sat08-strips (15)          0         0         8        15        15         5
elevators-sat11-strips (14)          0         0         0        14        14         0
gripper (20)                         4         5         5        20        20        20
hiking-sat14-strips (20)             2         7        15        20        20         2
logistics00 (19)                     9         9        19        19        19        15
logistics98 (31)                     4         6        28        31        31         2
miconic (11)                         2         3        11        11        11        11
mprime (21)                         21        21        21        21        21        10
mystery (16)                        10        10        10        10        10         5
nomystery-sat11-strips (14)          4         4        10         9         9         6
openstacks-sat08-strips (29)         4         5        23        29        29        29
openstacks-sat11-strips (15)         0         0         4        15        15        14
openstacks-sat14-strips (12)         0         0         0        12        12         8
pipesworld-notankage (34)           15        15        18        27        28        10
pipesworld-tankage (47)             10        14        39        40        40        15
quantum-layout-sat23-strips (7)         3         2         7         7         7         0
satellite (34)                       6         5        28        34        34         6
sokoban-sat08-strips (7)             1         1         6         6         6         2
sokoban-sat11-strips (5)             0         0         4         4         4         0
tpp (29)                             5         7        14        29        29        11
transport-sat08-strips (2)           1         1         1         2         2         1
transport-sat11-strips (2)           0         0         0         2         2         0
woodworking-sat08-strips (8)         0         0         7         8         8         2
woodworking-sat11-strips (11)         0         0        11        11        11         0
zenotravel (13)                      4         4        13        13        13         8
Total (557)                        128       145       358       507       521       217
```
