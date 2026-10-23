# Benchmark report

2026-10-28 11:24 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     131 (23.5%)  144 (25.9%)  292 (52.4%)  507 (91.0%)
Timeouts                        405 (72.7%)  401 (72.0%)  161 (28.9%)    35 (6.3%)
Out of memory                     21 (3.8%)    12 (2.2%)  104 (18.7%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     125          125          287          287
Faster                           88 (70.4%)   37 (29.6%)    19 (6.6%)  268 (93.4%)
Found when the other did not              6           19            5          220
Median runtime                       6.72 s       7.95 s      12.08 s       3.46 s
Total runtime                   11,797.49 s  12,006.98 s  18,870.05 s   2,221.52 s
Shorter plan                     90 (72.0%)   13 (10.4%)   46 (16.0%)  186 (64.8%)
Same plan length                 22 (17.6%)   22 (17.6%)   55 (19.2%)   55 (19.2%)
Median plan length                       16           27           51           42
Total plan length                     2,641        3,718       21,221       17,396
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   356 (89%)       5 (3%)
Guided concrete search              30 (7%)    154 (96%)
Unguided concrete search            15 (4%)       2 (1%)
Total                                   401          161
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   96 (67%)    235 (80%)
Refined, some actions off          45 (31%)     56 (19%)
Solved above the abstract plan       3 (2%)       1 (0%)
Total                                   144          292
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (11%)     37 (13%)
1 to 4                             93 (66%)    206 (71%)
5 to 9                              10 (7%)      16 (5%)
10 to 19                           21 (15%)     30 (10%)
20 or more                           2 (1%)       2 (1%)
Total                                   141          291
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             19        14        14        19        19
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         1         8         6
depot                                9         2         4         5         8
driverlog                           13         7         8        13        13
elevators-sat08-strips              15         0         1         5        15
elevators-sat11-strips              14         0         0         0        14
gripper                             20         4         5         3        20
hiking-sat14-strips                 20         2         8        15        20
logistics00                         19        10         9        19        19
logistics98                         31         4         6        23        31
miconic                             11         2         3        11        11
mprime                              21        21        20        21        21
mystery                             16        10        10         9        10
nomystery-sat11-strips              14         4         4        12         9
openstacks-sat08-strips             29         4         4        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                34        15        15        17        27
pipesworld-tankage                  47        10        10        15        40
quantum-layout-sat23-strips          7         3         2         2         7
satellite                           34         8         7        20        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         5         7        10        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         6         8
woodworking-sat11-strips            11         0         0         9        11
zenotravel                          13         4         4        12        13
Total                              557       131       144       292       507
```
