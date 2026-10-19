# Benchmark report

2026-10-19 09:05 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  117 (21.0%)  292 (52.4%)  507 (91.0%)
Timeouts                        440 (79.0%)  428 (76.8%)  169 (30.3%)    35 (6.3%)
Out of memory                     13 (2.3%)    12 (2.2%)   96 (17.2%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      99           99          287          287
Faster                           48 (48.5%)   51 (51.5%)    20 (7.0%)  267 (93.0%)
Found when the other did not              5           18            5          220
Median runtime                       9.85 s       6.31 s      12.08 s       3.46 s
Total runtime                    7,315.23 s   5,017.64 s  18,869.85 s   2,221.52 s
Shorter plan                     76 (76.8%)     0 (0.0%)   46 (16.0%)  186 (64.8%)
Same plan length                 23 (23.2%)   23 (23.2%)   55 (19.2%)   55 (19.2%)
Median plan length                       11           17           51           42
Total plan length                     1,407        1,958       21,221       17,396
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   401 (94%)     17 (10%)
Guided concrete search              10 (2%)    135 (80%)
Unguided concrete search            17 (4%)     17 (10%)
Total                                   428          169
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   83 (71%)    235 (80%)
Refined, some actions off          32 (27%)     56 (19%)
Solved above the abstract plan       2 (2%)       1 (0%)
Total                                   117          292
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (10%)     37 (13%)
1 to 4                             71 (62%)    206 (71%)
5 to 9                               6 (5%)      16 (5%)
10 to 19                           24 (21%)     30 (10%)
20 or more                           2 (2%)       2 (1%)
Total                                   115          291
```

## Every class against the largest

```
Over problems with 2+ classes          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Problems                                370          370
Solved by the largest class              58          137
Solved by some class                     59          159
Largest class is fastest           27 (46%)     66 (42%)
Median time, largest / best           1.01x        1.00x
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             19        11        11        19        19
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         0         8         6
depot                                9         1         1         5         8
driverlog                           13         7         6        13        13
elevators-sat08-strips              15         0         0         5        15
elevators-sat11-strips              14         0         0         0        14
gripper                             20         3         3         3        20
hiking-sat14-strips                 20         2         6        15        20
logistics00                         19         8         9        19        19
logistics98                         31         1         0        23        31
miconic                             11         1         2        11        11
mprime                              21        20        20        21        21
mystery                             16        10        10         9        10
nomystery-sat11-strips              14         2         3        12         9
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                34         9        15        17        27
pipesworld-tankage                  47         8        11        15        40
quantum-layout-sat23-strips          7         4         2         2         7
satellite                           34         5         5        20        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         4         6        10        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         6         8
woodworking-sat11-strips            11         0         0         9        11
zenotravel                          13         4         3        12        13
Total                              557       104       117       292       507
```
