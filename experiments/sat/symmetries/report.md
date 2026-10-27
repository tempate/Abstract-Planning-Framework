# Benchmark report

2026-10-27 09:04 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  117 (21.0%)  297 (53.3%)  507 (91.0%)
Timeouts                        440 (79.0%)  433 (77.7%)  157 (28.2%)    35 (6.3%)
Out of memory                     13 (2.3%)     7 (1.3%)  103 (18.5%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      99           99          292          292
Faster                           51 (51.5%)   48 (48.5%)    19 (6.5%)  273 (93.5%)
Found when the other did not              5           18            5          215
Median runtime                       9.85 s       6.31 s      12.37 s       3.51 s
Total runtime                    7,315.23 s   4,948.61 s  20,340.84 s   2,261.64 s
Shorter plan                     76 (76.8%)     0 (0.0%)   48 (16.4%)  190 (65.1%)
Same plan length                 23 (23.2%)   23 (23.2%)   54 (18.5%)   54 (18.5%)
Median plan length                       11           17         52.5           42
Total plan length                     1,407        1,963       21,606       17,803
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   401 (93%)       5 (3%)
Guided concrete search              15 (3%)    151 (96%)
Unguided concrete search            17 (4%)       1 (1%)
Total                                   433          157
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   84 (72%)    242 (81%)
Refined, some actions off          31 (26%)     54 (18%)
Solved above the abstract plan       2 (2%)       1 (0%)
Total                                   117          297
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (10%)     37 (12%)
1 to 4                             73 (63%)    216 (73%)
5 to 9                             23 (20%)      27 (9%)
10 to 19                             5 (4%)      14 (5%)
20 or more                           2 (2%)       2 (1%)
Total                                   115          296
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
pipesworld-tankage                  47         8        11        20        40
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
Total                              557       104       117       297       507
```
