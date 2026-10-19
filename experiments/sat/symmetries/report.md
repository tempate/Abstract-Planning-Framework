# Benchmark report

2026-10-19 09:05 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  114 (20.5%)  277 (49.7%)  507 (91.0%)
Timeouts                        440 (79.0%)  431 (77.4%)  182 (32.7%)    35 (6.3%)
Out of memory                     13 (2.3%)    12 (2.2%)   98 (17.6%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      99           99          274          274
Faster                           49 (49.5%)   50 (50.5%)    18 (6.6%)  256 (93.4%)
Found when the other did not              5           15            3          233
Median runtime                       9.85 s       6.86 s      12.25 s       3.40 s
Total runtime                    7,315.23 s   6,842.55 s  19,712.32 s   2,136.90 s
Shorter plan                     82 (82.8%)     0 (0.0%)   38 (13.9%)  187 (68.2%)
Same plan length                 17 (17.2%)   17 (17.2%)   49 (17.9%)   49 (17.9%)
Median plan length                       11           21         51.5           41
Total plan length                     1,407        2,308       20,469       16,299
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   401 (93%)      17 (9%)
Guided concrete search              13 (3%)    148 (81%)
Unguided concrete search            17 (4%)      17 (9%)
Total                                   431          182
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   89 (78%)    225 (81%)
Refined, some actions off          23 (20%)     50 (18%)
Solved above the abstract plan       2 (2%)       2 (1%)
Total                                   114          277
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (11%)     29 (11%)
1 to 4                             69 (62%)    198 (72%)
5 to 9                              10 (9%)      15 (5%)
10 to 19                           19 (17%)     30 (11%)
20 or more                           2 (2%)       3 (1%)
Total                                   112          275
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
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
hiking-sat14-strips                 20         2         6        14        20
logistics00                         19         8         9        19        19
logistics98                         31         1         0        22        31
miconic                             11         1         2        11        11
mprime                              21        20        20        21        21
mystery                             16        10        10         9        10
nomystery-sat11-strips              14         2         3        12         9
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                34         9        13        17        27
pipesworld-tankage                  47         8         9        12        40
quantum-layout-sat23-strips          7         4         2         3         7
satellite                           34         5         5        18        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         4         7        11        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         6         8
woodworking-sat11-strips            11         0         0         9        11
zenotravel                          13         4         3        11        13
Total                              557       104       114       277       507
```
