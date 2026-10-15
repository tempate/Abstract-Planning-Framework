# Benchmark report

2026-10-15 09:31 — experiments/sat/symmetries/results.csv

884 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found                     155 (17.5%)  116 (13.1%)  270 (30.5%)  771 (87.2%)
Timeouts                        716 (81.0%)  429 (48.5%)  191 (21.6%)    71 (8.0%)
Out of memory                     13 (1.5%)    12 (1.4%)   96 (10.9%)    40 (4.5%)
Others                             0 (0.0%)  327 (37.0%)  327 (37.0%)     2 (0.2%)
Total problems                          884          884          884          884
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found by both                      99           99          267          267
Faster                           51 (51.5%)   48 (48.5%)    18 (6.7%)  249 (93.3%)
Found when the other did not             56           17            3          504
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
airport                             42        11        11        19        27
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         0         0         6
depot                               22         4         1         5        20
driverlog                           20         9         6        12        20
elevators-sat08-strips              30         1         0         5        30
elevators-sat11-strips              20         0         0         0        20
floortile-sat11-strips              20         0         0         0         7
floortile-sat14-strips              20         0         0         0         2
grid                                 5         2         0         0         5
gripper                             20         3         3         3        20
hiking-sat14-strips                 20         2         6        15        20
logistics00                         28        10         9        19        28
logistics98                         35         3         0        23        35
miconic                             11         1         2        11        11
mprime                              35        34        20        21        35
mystery                             28        19        10         9        19
nomystery-sat11-strips              20         2         3        12        12
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                49        12        15        16        42
pipesworld-tankage                  49         9        10        12        42
quantum-layout-sat23-strips          7         4         2         2         7
satellite                           36         6         5        13        36
sokoban-sat08-strips                29         2         1         6        28
sokoban-sat11-strips                19         0         0         4        18
tetris-sat14-strips                 20         0         0         0        16
tpp                                 29         4         6         9        29
transport-sat08-strips              30         5         1         1        30
transport-sat11-strips              20         0         0         0        18
transport-sat14-strips              20         0         0         0        16
woodworking-sat08-strips            27         3         0         6        27
woodworking-sat11-strips            19         0         0         9        19
zenotravel                          18         7         3        11        18
Total                              884       155       116       270       771
```
