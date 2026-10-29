# Benchmark report

2026-10-29 09:35 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  114 (20.5%)  288 (51.7%)  507 (91.0%)
Timeouts                        440 (79.0%)  436 (78.3%)  166 (29.8%)    35 (6.3%)
Out of memory                     13 (2.3%)     7 (1.3%)  103 (18.5%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      99           99          283          283
Faster                           57 (57.6%)   42 (42.4%)    10 (3.5%)  273 (96.5%)
Found when the other did not              5           15            5          224
Median runtime                       9.85 s       7.11 s      13.26 s       3.43 s
Total runtime                    7,315.23 s   7,523.08 s  16,071.06 s   2,176.03 s
Shorter plan                     76 (76.8%)     0 (0.0%)   46 (16.3%)  181 (64.0%)
Same plan length                 23 (23.2%)   23 (23.2%)   56 (19.8%)   56 (19.8%)
Median plan length                       11           17           51           42
Total plan length                     1,407        1,960       20,897       17,213
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   403 (92%)       5 (3%)
Guided concrete search              16 (4%)    160 (96%)
Unguided concrete search            17 (4%)       1 (1%)
Total                                   436          166
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   83 (73%)    234 (81%)
Refined, some actions off          29 (25%)     53 (18%)
Solved above the abstract plan       2 (2%)       1 (0%)
Total                                   114          288
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (11%)     37 (13%)
1 to 4                             71 (63%)    205 (71%)
5 to 9                               6 (5%)      13 (5%)
10 to 19                           21 (19%)     30 (10%)
20 or more                           2 (2%)       2 (1%)
Total                                   112          287
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
hiking-sat14-strips                 20         2         6        14        20
logistics00                         19         8         9        19        19
logistics98                         31         1         0        23        31
miconic                             11         1         2        11        11
mprime                              21        20        20        21        21
mystery                             16        10        10         9        10
nomystery-sat11-strips              14         2         3        12         9
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                34         9        13        17        27
pipesworld-tankage                  47         8        10        12        40
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
Total                              557       104       114       288       507
```
