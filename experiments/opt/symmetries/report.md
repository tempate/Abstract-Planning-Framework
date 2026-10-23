# Benchmark report

2026-10-23 09:53 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  125 (24.1%)  175 (33.8%)  193 (37.3%)
Timeouts                        389 (75.1%)  385 (74.3%)  343 (66.2%)  324 (62.5%)
Out of memory                      1 (0.2%)     8 (1.5%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     113          113          166          166
Faster                           79 (69.9%)   34 (30.1%)   49 (29.5%)  117 (70.5%)
Found when the other did not             15           12            9           27
Median runtime                       6.84 s       8.23 s       6.96 s       3.62 s
Total runtime                   10,385.40 s   9,462.69 s  16,790.55 s  13,288.95 s
Shorter plan                     20 (17.7%)     0 (0.0%)     0 (0.0%)   26 (15.7%)
Same plan length                 93 (82.3%)   93 (82.3%)  140 (84.3%)  140 (84.3%)
Median plan length                       11           12           20           19
Total plan length                     1,668        1,740        4,404        4,253
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   326 (85%)    266 (78%)
Guided concrete search               8 (2%)      12 (3%)
Unguided concrete search           51 (13%)     65 (19%)
Total                                   385          343
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  104 (83%)    151 (86%)
Refined, some actions off          16 (13%)     20 (11%)
Solved above the abstract plan       5 (4%)       4 (2%)
Total                                   125          175
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (11%)     23 (13%)
1 to 4                             84 (70%)    128 (75%)
5 to 9                              10 (8%)       8 (5%)
10 to 19                           12 (10%)      11 (6%)
20 or more                           1 (1%)       1 (1%)
Total                                   120          171
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         3         0         0
airport                             19        11        11        19        19
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                                9         1         1         4         3
driverlog                           13         7         5        10        10
elevators-opt08-strips               4         0         1         2         3
elevators-opt11-strips               2         0         1         2         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        11         9
logistics00                         19         8         9        15        15
logistics98                         31         1         0         4         4
miconic                             11         1         2        11        11
mprime                              21        20        20        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         4         7         8
openstacks-opt08-strips             28         0         1         8         8
openstacks-opt11-strips             20         0         0         5         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10         8         7        13
pipesworld-tankage                  47         8        10         7         9
quantum-layout-opt23-strips          7         4         3         3         4
satellite                           34         5         5         8        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         7         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         2         2         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         1         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         7         7
Total                              518       128       125       175       193
```
