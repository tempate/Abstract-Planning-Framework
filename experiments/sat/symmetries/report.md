# Benchmark report

2026-10-23 10:42 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     131 (23.5%)  145 (26.0%)  303 (54.4%)  507 (91.0%)
Timeouts                        405 (72.7%)  400 (71.8%)  149 (26.8%)    35 (6.3%)
Out of memory                     21 (3.8%)    12 (2.2%)  105 (18.9%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     123          123          293          293
Faster                           89 (72.4%)   34 (27.6%)    21 (7.2%)  272 (92.8%)
Found when the other did not              8           22           10          214
Median runtime                       6.57 s       7.72 s      12.10 s       3.38 s
Total runtime                   10,231.52 s  11,867.81 s  20,209.13 s   2,215.70 s
Shorter plan                     88 (71.5%)    12 (9.8%)   42 (14.3%)  195 (66.6%)
Same plan length                 23 (18.7%)   23 (18.7%)   56 (19.1%)   56 (19.1%)
Median plan length                       16           25           52           42
Total plan length                     2,575        3,577       21,961       18,084
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   357 (89%)       5 (3%)
Guided concrete search               1 (0%)     45 (30%)
Unguided concrete search           42 (10%)     99 (66%)
Total                                   400          149
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   97 (67%)    236 (78%)
Refined, some actions off          45 (31%)     65 (21%)
Solved above the abstract plan       3 (2%)       2 (1%)
Total                                   145          303
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               15 (11%)     42 (14%)
1 to 4                             93 (65%)    216 (72%)
5 to 9                              13 (9%)      16 (5%)
10 to 19                           20 (14%)      25 (8%)
20 or more                           1 (1%)       2 (1%)
Total                                   142          301
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             19        14        14        19        19
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         2        13         6
depot                                9         2         3         5         8
driverlog                           13         7         8        13        13
elevators-sat08-strips              15         0         2         5        15
elevators-sat11-strips              14         0         0         0        14
gripper                             20         4         5        15        20
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
pipesworld-notankage                34        15        13        16        27
pipesworld-tankage                  47        10        13        14        40
quantum-layout-sat23-strips          7         3         1         2         7
satellite                           34         8         7        20        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         5         7        10        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         4         8
woodworking-sat11-strips            11         0         0         8        11
zenotravel                          13         4         4        11        13
Total                              557       131       145       303       507
```
