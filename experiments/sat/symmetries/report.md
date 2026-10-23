# Benchmark report

2026-10-23 14:03 — experiments/sat/symmetries/results.csv

557 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                     104 (18.7%)  113 (20.3%)  319 (57.3%)  507 (91.0%)
Timeouts                        440 (79.0%)  437 (78.5%)  138 (24.8%)    35 (6.3%)
Out of memory                     13 (2.3%)     7 (1.3%)   99 (17.8%)    14 (2.5%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          557          557          557          557
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                     100          100          316          316
Faster                           59 (59.0%)   41 (41.0%)    21 (6.6%)  295 (93.4%)
Found when the other did not              4           13            3          191
Median runtime                       9.93 s       7.82 s      13.44 s       3.63 s
Total runtime                    7,450.05 s   6,263.54 s  18,513.99 s   3,011.70 s
Shorter plan                     73 (73.0%)     0 (0.0%)   45 (14.2%)  209 (66.1%)
Same plan length                 27 (27.0%)   27 (27.0%)   62 (19.6%)   62 (19.6%)
Median plan length                       11         17.5         56.5           43
Total plan length                     1,457        2,054       23,733       19,604
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                   409 (94%)      13 (9%)
Guided concrete search              11 (3%)    122 (88%)
Unguided concrete search            17 (4%)       3 (2%)
Total                                   437          138
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   92 (81%)    294 (92%)
Refined, some actions off          20 (18%)      23 (7%)
Solved above the abstract plan       1 (1%)       2 (1%)
Total                                   113          319
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                               12 (11%)     37 (12%)
1 to 4                             68 (61%)    204 (64%)
5 to 9                             16 (14%)      18 (6%)
10 to 19                             4 (4%)     33 (10%)
20 or more                         12 (11%)      25 (8%)
Total                                   112          317
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
elevators-sat08-strips              15         0         0         8        15
elevators-sat11-strips              14         0         0         1        14
gripper                             20         3         3         3        20
hiking-sat14-strips                 20         2         6        15        20
logistics00                         19         8         9        19        19
logistics98                         31         1         0        23        31
miconic                             11         1         2        11        11
mprime                              21        20        20        21        21
mystery                             16        10        10        10        10
nomystery-sat11-strips              14         2         3        10         9
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                34         9        11        16        27
pipesworld-tankage                  47         8        10        29        40
quantum-layout-sat23-strips          7         4         3         7         7
satellite                           34         5         5        21        34
sokoban-sat08-strips                 7         1         1         6         6
sokoban-sat11-strips                 5         0         0         4         4
tpp                                 29         4         6        12        29
transport-sat08-strips               2         1         1         1         2
transport-sat11-strips               2         0         0         0         2
woodworking-sat08-strips             8         0         0         7         8
woodworking-sat11-strips            11         0         0        11        11
zenotravel                          13         4         3        12        13
Total                              557       104       113       319       507
```
