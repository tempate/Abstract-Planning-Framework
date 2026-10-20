# Benchmark report

2026-10-20 09:04 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, len-asp, abs-fd, len-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ         ASP⁺        LAMAᵅ        LAMA⁺         LAMA
------------------------------------------------------------------------------------------------------------
Plans found                     104 (18.7%)  117 (21.0%)  103 (18.5%)  292 (52.4%)  165 (29.6%)  507 (91.0%)
Timeouts                        440 (79.0%)  433 (77.7%)  447 (80.3%)  161 (28.9%)  313 (56.2%)    35 (6.3%)
Out of memory                     13 (2.3%)     7 (1.3%)     7 (1.3%)  104 (18.7%)   79 (14.2%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA         ASP⁺        LAMA⁺
------------------------------------------------------------------------------------------------------------
Plans found by both                     101           99          287          161          101          161
Faster                           73 (72.3%)   51 (51.5%)    20 (7.0%)  150 (93.2%)   28 (27.7%)    11 (6.8%)
Found when the other did not              3           18            5          346            2            4
Median runtime                      10.02 s       6.31 s      12.08 s       3.26 s      11.34 s      12.96 s
Total runtime                    7,479.04 s   5,017.64 s  18,869.85 s     605.97 s   8,849.98 s  24,332.03 s
Shorter plan                       0 (0.0%)     0 (0.0%)   46 (16.0%)     8 (5.0%)     0 (0.0%)   84 (52.2%)
Same plan length               101 (100.0%)   23 (23.2%)   55 (19.2%)   69 (42.9%) 101 (100.0%)   69 (42.9%)
Median plan length                       11           17           51           22           11           20
Total plan length                     1,487        1,958       21,221        6,957        1,487        6,468
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   401 (93%)       5 (3%)
Guided concrete search              15 (3%)    155 (96%)
Unguided concrete search            17 (4%)       1 (1%)
Total                                   433          161
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

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ      ASP⁺     LAMAᵅ     LAMA⁺      LAMA
--------------------------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0         0         0        12
airport                             19        11        11        11        19        19        19
barman-sat11-strips                 20         0         0         0         0         0        20
barman-sat14-strips                 20         0         0         0         0         0        20
childsnack-sat14-strips             20         0         0         0         8        10         6
depot                                9         1         1         1         5         4         8
driverlog                           13         7         6         6        13         7        13
elevators-sat08-strips              15         0         0         0         5         1        15
elevators-sat11-strips              14         0         0         0         0         0        14
gripper                             20         3         3         3         3         3        20
hiking-sat14-strips                 20         2         6         3        15         3        20
logistics00                         19         8         9         8        19         9        19
logistics98                         31         1         0         0        23         1        31
miconic                             11         1         2         1        11        10        11
mprime                              21        20        20        20        21        21        21
mystery                             16        10        10        10         9         9        10
nomystery-sat11-strips              14         2         3         2        12         2         9
openstacks-sat08-strips             29         2         2         2        23        18        29
openstacks-sat11-strips             15         0         0         0         4         4        15
openstacks-sat14-strips             12         0         0         0         0         0        12
pipesworld-notankage                34         9        15         9        17        12        27
pipesworld-tankage                  47         8        11         9        15         9        40
quantum-layout-sat23-strips          7         4         2         4         2         4         7
satellite                           34         5         5         5        20         8        34
sokoban-sat08-strips                 7         1         1         1         6         1         6
sokoban-sat11-strips                 5         0         0         0         4         0         4
tpp                                 29         4         6         4        10         4        29
transport-sat08-strips               2         1         1         1         1         1         2
transport-sat11-strips               2         0         0         0         0         0         2
woodworking-sat08-strips             8         0         0         0         6         1         8
woodworking-sat11-strips            11         0         0         0         9         0        11
zenotravel                          13         4         3         3        12         4        13
Total                              557       104       117       103       292       165       507
```
