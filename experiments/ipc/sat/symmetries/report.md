# Benchmark report

2026-11-27 09:10 — experiments/ipc/sat/symmetries/results.csv

599 problems compared over asp, abs-asp, abs-lama, lama, lama-symmetry-pruning, rnd-g; 78 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA        LAMA+        rnd-g
------------------------------------------------------------------------------------------------------------
Plans found                     170 (28.4%)  187 (31.2%)  410 (68.4%)  549 (91.7%)  563 (94.0%)  257 (42.9%)
Timeouts                        410 (68.4%)  396 (66.1%)  123 (20.5%)    35 (5.8%)    33 (5.5%)  184 (30.7%)
Out of memory                     19 (3.2%)    16 (2.7%)   65 (10.9%)    14 (2.3%)     1 (0.2%)  150 (25.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)     2 (0.3%)     8 (1.3%)
Total problems                          599          599          599          599          599          599
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     167          167          406          406
Faster                          125 (74.9%)   42 (25.1%)    22 (5.4%)  384 (94.6%)
Found when the other did not              3           20            4          143
Median runtime                       5.32 s       5.52 s       6.13 s       2.54 s
Total runtime                   14,454.74 s  14,827.69 s  16,187.64 s   7,559.91 s
Shorter plan                     59 (35.3%)   22 (13.2%)   77 (19.0%)  133 (32.8%)
Same plan length                 86 (51.5%)   86 (51.5%)  196 (48.3%)  196 (48.3%)
Median plan length                       16           16           50         45.5
Total plan length                     4,332        4,972       30,735       29,177
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
Refined directly                  158 (84%)    391 (95%)
Refined, some actions off          26 (14%)      13 (3%)
Solved above the abstract plan       3 (2%)       6 (1%)
Total                                   187          410
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               57 (31%)     77 (19%)
1 to 4                             72 (39%)    221 (55%)
5 to 9                             25 (14%)      35 (9%)
10 to 19                            10 (5%)     44 (11%)
20 or more                         20 (11%)      27 (7%)
Total                                   184          404
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA     LAMA+     rnd-g
----------------------------------------------------------------------------------------
agricola-sat18-strips (20)           0         0        12        12        11         5
airport (21)                        16        16        21        21        21        17
barman-sat11-strips (20)             0         0         0        20        20         0
barman-sat14-strips (20)             0         0         0        20        20         0
childsnack-sat14-strips (20)         0         1         8         6        19         0
depot (9)                            2         3         6         8         9         4
driverlog (14)                       8         9        14        14        14        11
elevators-sat08-strips (15)          0         0         8        15        15         5
elevators-sat11-strips (14)          0         0         0        14        14         0
gripper (20)                         4         5         5        20        20        20
hiking-sat14-strips (20)             2         7        15        20        20         2
logistics00 (19)                     9         9        19        19        19        15
logistics98 (31)                     4         6        30        31        31         2
miconic (11)                         2         3        11        11        11        11
movie (30)                          30        30        30        30        30        30
mprime (21)                         21        21        21        21        21        10
mystery (16)                        10        10        10        10        10         5
nomystery-sat11-strips (14)          4         4        10         9         9         6
openstacks-sat08-strips (29)         4         5        23        29        29        29
openstacks-sat11-strips (15)         0         0         4        15        15        14
openstacks-sat14-strips (12)         0         0         0        12        12         8
parcprinter-08-strips (3)            3         3         3         3         3         2
pipesworld-notankage (36)           17        17        20        29        30        12
pipesworld-tankage (47)             10        14        40        40        40        15
quantum-layout-sat23-strips (7)         3         2         7         7         7         0
satellite (34)                       6         5        33        34        34         6
sokoban-sat08-strips (10)            4         4         9         9         9         5
sokoban-sat11-strips (6)             1         1         5         5         5         1
tpp (29)                             5         7        14        29        29        11
transport-sat08-strips (2)           1         1         1         2         2         1
transport-sat11-strips (2)           0         0         0         2         2         0
woodworking-sat08-strips (8)         0         0         7         8         8         2
woodworking-sat11-strips (11)         0         0        11        11        11         0
zenotravel (13)                      4         4        13        13        13         8
Total (599)                        170       187       410       549       563       257
```
