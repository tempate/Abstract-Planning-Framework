# Benchmark report

2026-11-12 10:38 — experiments/ipc/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     128 (23.0%)  144 (25.9%)  353 (63.4%)  507 (91.0%)
Timeouts                        410 (73.6%)  396 (71.1%)  128 (23.0%)    35 (6.3%)
Out of memory                     19 (3.4%)    17 (3.1%)   75 (13.5%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     124          124          350          350
Faster                           88 (71.0%)   36 (29.0%)    14 (4.0%)  336 (96.0%)
Found when the other did not              4           20            3          157
Median runtime                       8.24 s       9.27 s      12.41 s       3.81 s
Total runtime                   13,707.47 s  13,916.69 s  22,676.23 s   6,120.23 s
Shorter plan                     51 (41.1%)   16 (12.9%)   64 (18.3%)  159 (45.4%)
Same plan length                 57 (46.0%)   57 (46.0%)  127 (36.3%)  127 (36.3%)
Median plan length                       16         18.5         56.5         48.5
Total plan length                     2,589        3,229       27,636       25,140
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   357 (90%)     13 (10%)
Guided concrete search              24 (6%)    110 (86%)
Unguided concrete search            15 (4%)       5 (4%)
Total                                   396          128
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                  118 (82%)    330 (93%)
Refined, some actions off          25 (17%)      17 (5%)
Solved above the abstract plan       1 (1%)       6 (2%)
Total                                   144          353
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (10%)     37 (11%)
1 to 4                             73 (51%)    203 (59%)
5 to 9                             25 (17%)     37 (11%)
10 to 19                            10 (7%)     43 (12%)
20 or more                         20 (14%)      27 (8%)
Total                                   143          347
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
quantum-layout-sat23-strips (7)         3         1         2         7
satellite (34)                       6         5        28        34
sokoban-sat08-strips (7)             1         1         6         6
sokoban-sat11-strips (5)             0         0         4         4
tpp (29)                             5         7        14        29
transport-sat08-strips (2)           1         1         1         2
transport-sat11-strips (2)           0         0         0         2
woodworking-sat08-strips (8)         0         0         7         8
woodworking-sat11-strips (11)         0         0        11        11
zenotravel (13)                      4         4        13        13
Total (557)                        128       144       353       507
```
