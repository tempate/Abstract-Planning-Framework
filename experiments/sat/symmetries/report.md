# Benchmark report

2026-10-23 09:53 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  115 (20.6%)  303 (54.4%)  507 (91.0%)
Timeouts                        440 (79.0%)  435 (78.1%)  149 (26.8%)    35 (6.3%)
Out of memory                     13 (2.3%)     7 (1.3%)  105 (18.9%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      99           99          293          293
Faster                           48 (48.5%)   51 (51.5%)    21 (7.2%)  272 (92.8%)
Found when the other did not              5           16           10          214
Median runtime                       9.85 s       6.34 s      12.03 s       3.38 s
Total runtime                    7,315.23 s   4,630.15 s  18,920.28 s   2,197.92 s
Shorter plan                     77 (77.8%)     0 (0.0%)   43 (14.7%)  194 (66.2%)
Same plan length                 22 (22.2%)   22 (22.2%)   56 (19.1%)   56 (19.1%)
Median plan length                       11           17           53           42
Total plan length                     1,407        1,992       21,898       18,074
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   400 (92%)       5 (3%)
Guided concrete search               2 (0%)     45 (30%)
Unguided concrete search            33 (8%)     99 (66%)
Total                                   435          149
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   85 (74%)    235 (78%)
Refined, some actions off          29 (25%)     67 (22%)
Solved above the abstract plan       1 (1%)       1 (0%)
Total                                   115          303
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (11%)     42 (14%)
1 to 4                             72 (63%)    216 (72%)
5 to 9                               9 (8%)      17 (6%)
10 to 19                           19 (17%)      25 (8%)
20 or more                           2 (2%)       2 (1%)
Total                                   114          302
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             19        11        11        19        19
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         0        13         6
depot                                9         1         1         5         8
driverlog                           13         7         6        13        13
elevators-sat08-strips              15         0         0         5        15
elevators-sat11-strips              14         0         0         0        14
gripper                             20         3         3        15        20
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
pipesworld-notankage                34         9        13        16        27
pipesworld-tankage                  47         8        11        14        40
quantum-layout-sat23-strips          7         4         2         2         7
satellite                           34         5         5        20        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         4         6        10        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         4         8
woodworking-sat11-strips            11         0         0         8        11
zenotravel                          13         4         3        11        13
Total                              557       104       115       303       507
```
