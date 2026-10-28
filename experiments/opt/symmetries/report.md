# Benchmark report

2026-10-28 05:22 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  124 (23.9%)  127 (24.5%)  193 (37.3%)
Timeouts                        389 (75.1%)  391 (75.5%)  391 (75.5%)  324 (62.5%)
Out of memory                      1 (0.2%)     3 (0.6%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     122          122          123          123
Faster                           99 (81.1%)   23 (18.9%)   18 (14.6%)  105 (85.4%)
Found when the other did not              6            2            4           70
Median runtime                       8.72 s      13.12 s       6.57 s       2.67 s
Total runtime                   14,631.66 s  16,091.35 s   9,639.66 s   2,855.40 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               122 (100.0%) 122 (100.0%) 123 (100.0%) 123 (100.0%)
Median plan length                       12           12           14           14
Total plan length                     2,114        2,114        2,608        2,608
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   325 (83%)    267 (68%)
Guided concrete search              28 (7%)    100 (26%)
Unguided concrete search           38 (10%)      24 (6%)
Total                                   391          391
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   56 (45%)     60 (47%)
Refined, some actions off           11 (9%)     17 (13%)
Solved above the abstract plan     57 (46%)     50 (39%)
Total                                   124          127
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (19%)     23 (30%)
1 to 4                             45 (67%)     42 (55%)
5 to 9                               5 (7%)       6 (8%)
10 to 19                             2 (3%)       4 (5%)
20 or more                           2 (3%)       2 (3%)
Total                                    67           77
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         8         0         0
airport                             19        11        11        19        19
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                                9         1         1         2         3
driverlog                           13         7         6         7        10
elevators-opt08-strips               4         0         0         0         3
elevators-opt11-strips               2         0         0         0         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        13         9
logistics00                         19         8         8        12        15
logistics98                         31         1         0         1         4
miconic                             11         1         1         1        11
mprime                              21        20        20        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         2         2         8
openstacks-opt08-strips             28         0         0         0         8
openstacks-opt11-strips             20         0         0         0         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10        10         9        13
pipesworld-tankage                  47         8         8         8         9
quantum-layout-opt23-strips          7         4         4         4         4
satellite                           34         5         5         5        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         4         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         1         1         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         0         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         4         7
Total                              518       128       124       127       193
```
