# Benchmark report

2026-10-27 09:04 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  127 (24.5%)  183 (35.3%)  193 (37.3%)
Timeouts                        389 (75.1%)  383 (73.9%)  335 (64.7%)  324 (62.5%)
Out of memory                      1 (0.2%)     8 (1.5%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     115          115          172          172
Faster                           72 (62.6%)   43 (37.4%)   57 (33.1%)  115 (66.9%)
Found when the other did not             13           12           11           21
Median runtime                       7.11 s       7.20 s       7.50 s       3.67 s
Total runtime                   10,436.37 s   8,982.52 s  17,397.26 s  14,480.17 s
Shorter plan                     33 (28.7%)     0 (0.0%)     0 (0.0%)   43 (25.0%)
Same plan length                 82 (71.3%)   82 (71.3%)  129 (75.0%)  129 (75.0%)
Median plan length                       11           13           21           19
Total plan length                     1,699        1,812        4,565        4,350
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   325 (85%)    266 (79%)
Guided concrete search             41 (11%)     65 (19%)
Unguided concrete search            17 (4%)       4 (1%)
Total                                   383          335
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   99 (78%)    144 (79%)
Refined, some actions off          26 (20%)     38 (21%)
Solved above the abstract plan       2 (2%)       1 (1%)
Total                                   127          183
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (10%)     23 (13%)
1 to 4                             90 (72%)    140 (77%)
5 to 9                             17 (14%)      13 (7%)
10 to 19                             4 (3%)       5 (3%)
20 or more                           1 (1%)       1 (1%)
Total                                   125          182
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
depot                                9         1         1         5         3
driverlog                           13         7         6        10        10
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
pipesworld-notankage                34        10         9         9        13
pipesworld-tankage                  47         8        10        10         9
quantum-layout-opt23-strips          7         4         3         3         4
satellite                           34         5         5        10        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         7         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         2         2         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         1         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         7         7
Total                              518       128       127       183       193
```
