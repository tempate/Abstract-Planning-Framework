# Benchmark report

2026-10-19 10:02 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, len-asp, abs-fd, len-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ         ASP⁺       LMcutᵅ       LMcut⁺        LMcut
------------------------------------------------------------------------------------------------------------
Plans found                     128 (24.7%)  127 (24.5%)  121 (23.4%)  183 (35.3%)  124 (23.9%)  193 (37.3%)
Timeouts                        389 (75.1%)  383 (73.9%)  394 (76.1%)  335 (64.7%)  394 (76.1%)  324 (62.5%)
Out of memory                      1 (0.2%)     8 (1.5%)     3 (0.6%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut         ASP⁺       LMcut⁺
------------------------------------------------------------------------------------------------------------
Plans found by both                     120          115          172          120          120          120
Faster                          101 (84.2%)   45 (39.1%)   56 (32.6%)  103 (85.8%)   19 (15.8%)   17 (14.2%)
Found when the other did not              8           12           11           73            1            4
Median runtime                       8.19 s       7.20 s       7.50 s       2.67 s      10.82 s       7.77 s
Total runtime                   11,671.15 s   9,063.92 s  19,283.72 s   2,737.94 s  15,229.01 s  12,012.31 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               120 (100.0%)   82 (71.3%)  129 (75.0%) 120 (100.0%) 120 (100.0%) 120 (100.0%)
Median plan length                       12           13           21           13           12           13
Total plan length                     1,948        1,804        4,566        2,326        1,948        2,326
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
1 to 4                             88 (70%)    134 (74%)
5 to 9                               6 (5%)       9 (5%)
10 to 19                           17 (14%)      15 (8%)
20 or more                           1 (1%)       1 (1%)
Total                                   125          182
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ      ASP⁺    LMcutᵅ    LMcut⁺     LMcut
--------------------------------------------------------------------------------------------------
agricola-opt18-strips               20         8         3         5         0         0         0
airport                             19        11        11        11        19        19        19
barman-opt11-strips                 20         0         0         0         0         0         4
barman-opt14-strips                 14         0         0         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0         0         0
depot                                9         1         1         1         5         2         3
driverlog                           13         7         6         6        10         7        10
elevators-opt08-strips               4         0         1         0         2         0         3
elevators-opt11-strips               2         0         1         0         2         0         2
gripper                             20         3         3         3         3         3         7
hiking-opt14-strips                 20        12        13        13        11        13         9
logistics00                         19         8         9         8        15         9        15
logistics98                         31         1         0         0         4         1         4
miconic                             11         1         2         1        11         1        11
mprime                              21        20        20        20        16        16        16
mystery                             16        10        10        10         8         8         8
nomystery-opt11-strips              10         4         4         3         7         3         8
openstacks-opt08-strips             28         0         1         0         8         0         8
openstacks-opt11-strips             20         0         0         0         5         0         5
openstacks-opt14-strips             14         0         0         0         0         0         0
pipesworld-notankage                34        10         9         9         9         9        13
pipesworld-tankage                  47         8        10         8        10         8         9
quantum-layout-opt23-strips          7         4         3         4         3         4         4
satellite                           34         5         5         5        10         6        10
sokoban-opt08-strips                 3         1         1         1         2         1         2
sokoban-opt11-strips                 2         1         1         1         2         1         2
tpp                                 29         4         4         4         7         4         6
transport-opt08-strips               4         3         3         3         3         3         3
transport-opt14-strips               4         1         2         1         2         1         2
visitall-opt11-strips                1         1         1         1         1         1         1
woodworking-opt08-strips             5         0         0         0         1         0         1
woodworking-opt11-strips             4         0         0         0         0         0         1
zenotravel                          13         4         3         3         7         4         7
Total                              518       128       127       121       183       124       193
```
