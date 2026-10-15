# Benchmark report

2026-10-15 09:35 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  116 (20.8%)  270 (48.5%)  507 (91.0%)
Timeouts                        440 (79.0%)  429 (77.0%)  191 (34.3%)    35 (6.3%)
Out of memory                     13 (2.3%)    12 (2.2%)   96 (17.2%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found by both                      99           99          267          267
Faster                           51 (51.5%)   48 (48.5%)    18 (6.7%)  249 (93.3%)
Found when the other did not              5           17            3          240
Median runtime                       9.85 s       6.78 s      12.43 s       3.46 s
Total runtime                    7,315.23 s   6,600.50 s  15,375.87 s   2,145.79 s
Shorter plan                     73 (73.7%)     0 (0.0%)   45 (16.9%)  165 (61.8%)
Same plan length                 26 (26.3%)   26 (26.3%)   57 (21.3%)   57 (21.3%)
Median plan length                       11           17           47           40
Total plan length                     1,407        1,935       19,274       16,034
```

## Where the timeouts died

```
Killed during                          ASPᵅ          FDᵅ
--------------------------------------------------------
Abstract search                   402 (94%)      17 (9%)
Guided concrete search              10 (2%)    157 (82%)
Unguided concrete search            17 (4%)      17 (9%)
Total                                   429          191
```

## How the successes were solved

```
Solved by                              ASPᵅ          FDᵅ
--------------------------------------------------------
Refined directly                   82 (71%)    214 (79%)
Refined, some actions off          29 (25%)     51 (19%)
Solved above the abstract plan       5 (4%)       5 (2%)
Total                                   116          270
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ          FDᵅ
--------------------------------------------------------
None                               12 (11%)     29 (11%)
1 to 4                             68 (61%)    193 (73%)
5 to 9                               7 (6%)      12 (5%)
10 to 19                           22 (20%)     29 (11%)
20 or more                           2 (2%)       2 (1%)
Total                                   111          265
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ       FDᵅ        FD
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             19        11        11        19        19
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         0         0         6
depot                                9         1         1         5         8
driverlog                           13         7         6        12        13
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
pipesworld-notankage                34         9        15        16        27
pipesworld-tankage                  47         8        10        12        40
quantum-layout-sat23-strips          7         4         2         2         7
satellite                           34         5         5        13        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         4         6         9        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         6         8
woodworking-sat11-strips            11         0         0         9        11
zenotravel                          13         4         3        11        13
Total                              557       104       116       270       507
```
