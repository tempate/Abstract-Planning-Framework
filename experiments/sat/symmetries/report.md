# Benchmark report

2026-10-22 10:04 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     131 (23.5%)  142 (25.5%)  292 (52.4%)  507 (91.0%)
Timeouts                        405 (72.7%)  403 (72.4%)  161 (28.9%)    35 (6.3%)
Out of memory                     21 (3.8%)    12 (2.2%)  104 (18.7%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     124          124          287          287
Faster                           88 (71.0%)   36 (29.0%)    20 (7.0%)  267 (93.0%)
Found when the other did not              7           18            5          220
Median runtime                       6.65 s       7.84 s      12.08 s       3.46 s
Total runtime                   11,759.81 s  11,678.75 s  18,869.85 s   2,221.52 s
Shorter plan                     89 (71.8%)   14 (11.3%)   46 (16.0%)  186 (64.8%)
Same plan length                 21 (16.9%)   21 (16.9%)   55 (19.2%)   55 (19.2%)
Median plan length                       16           26           51           42
Total plan length                     2,610        3,677       21,221       17,396
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   356 (88%)       5 (3%)
Guided concrete search              30 (7%)    155 (96%)
Unguided concrete search            17 (4%)       1 (1%)
Total                                   403          161
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   96 (68%)    235 (80%)
Refined, some actions off          45 (32%)     56 (19%)
Solved above the abstract plan       1 (1%)       1 (0%)
Total                                   142          292
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
gripper                             20         4         3         3        20
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
Total                              557       131       142       292       507
```
