# Benchmark report

2026-11-05 10:50 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     131 (23.5%)  144 (25.9%)  332 (59.6%)  507 (91.0%)
Timeouts                        405 (72.7%)  397 (71.3%)  123 (22.1%)    35 (6.3%)
Out of memory                     21 (3.8%)    16 (2.9%)  101 (18.1%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     125          125          329          329
Faster                          101 (80.8%)   24 (19.2%)     4 (1.2%)  325 (98.8%)
Found when the other did not              6           19            3          178
Median runtime                       6.72 s      15.21 s      18.51 s       3.65 s
Total runtime                   10,607.39 s  15,598.87 s  21,776.34 s   3,595.67 s
Shorter plan                     91 (72.8%)    12 (9.6%)   52 (15.8%)  213 (64.7%)
Same plan length                 22 (17.6%)   22 (17.6%)   64 (19.5%)   64 (19.5%)
Median plan length                       16           28           54           44
Total plan length                     2,621        3,659       24,255       20,523
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   358 (90%)     13 (11%)
Guided concrete search              24 (6%)    105 (85%)
Unguided concrete search            15 (4%)       5 (4%)
Total                                   397          123
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                  118 (82%)    311 (94%)
Refined, some actions off          25 (17%)      15 (5%)
Solved above the abstract plan       1 (1%)       6 (2%)
Total                                   144          332
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (10%)     37 (11%)
1 to 4                             73 (51%)    183 (56%)
5 to 9                             24 (17%)     33 (10%)
10 to 19                            10 (7%)     41 (13%)
20 or more                         21 (15%)     32 (10%)
Total                                   143          326
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
agricola-sat18-strips (20)           0         0         0        12
airport (19)                        14        14        19        19
barman-sat11-strips (20)             0         0         0        20
barman-sat14-strips (20)             0         0         0        20
childsnack-sat14-strips (20)         0         0         8         6
depot (9)                            2         3         6         8
driverlog (13)                       7         8        13        13
elevators-sat08-strips (15)          0         0         8        15
elevators-sat11-strips (14)          0         0         0        14
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
Total (557)                        131       144       332       507
```
