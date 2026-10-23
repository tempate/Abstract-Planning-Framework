# Benchmark report

2026-10-23 14:03 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  128 (24.7%)  189 (36.5%)  193 (37.3%)
Timeouts                        389 (75.1%)  381 (73.6%)  328 (63.3%)  324 (62.5%)
Out of memory                      1 (0.2%)     9 (1.7%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.2%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          177          177
Faster                           82 (70.1%)   35 (29.9%)   54 (30.5%)  123 (69.5%)
Found when the other did not             11           11           12           16
Median runtime                       7.86 s       8.65 s       7.35 s       3.83 s
Total runtime                   10,578.35 s   9,222.33 s  17,011.55 s  17,140.23 s
Shorter plan                     26 (22.2%)     0 (0.0%)     0 (0.0%)   35 (19.8%)
Same plan length                 91 (77.8%)   91 (77.8%)  142 (80.2%)  142 (80.2%)
Median plan length                       11           12           20           19
Total plan length                     1,765        1,858        4,661        4,479
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   337 (88%)    262 (80%)
Guided concrete search              27 (7%)     60 (18%)
Unguided concrete search            17 (4%)       6 (2%)
Total                                   381          328
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  106 (83%)    167 (88%)
Refined, some actions off          21 (16%)     21 (11%)
Solved above the abstract plan       1 (1%)       1 (1%)
Total                                   128          189
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (10%)     23 (12%)
1 to 4                             82 (65%)    131 (70%)
5 to 9                             17 (13%)       9 (5%)
10 to 19                             3 (2%)       8 (4%)
20 or more                          12 (9%)      17 (9%)
Total                                   127          188
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
elevators-opt08-strips               4         0         0         3         3
elevators-opt11-strips               2         0         0         2         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        11         9
logistics00                         19         8         9        15        15
logistics98                         31         1         0         4         4
miconic                             11         1         2        11        11
mprime                              21        20        20        16        16
mystery                             16        10        10         9         8
nomystery-opt11-strips              10         4         4         8         8
openstacks-opt08-strips             28         0         1         9         8
openstacks-opt11-strips             20         0         0         5         5
openstacks-opt14-strips             14         0         0         0         0
pipesworld-notankage                34        10        10        11        13
pipesworld-tankage                  47         8        10        10         9
quantum-layout-opt23-strips          7         4         4         3         4
satellite                           34         5         5         9        10
sokoban-opt08-strips                 3         1         1         2         2
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         5         7         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         2         2         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         1         1
woodworking-opt11-strips             4         0         0         1         1
zenotravel                          13         4         3         7         7
Total                              518       128       128       189       193
```
