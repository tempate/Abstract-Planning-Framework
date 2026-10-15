# Benchmark report

2026-10-15 09:35 — experiments/opt/symmetries/results.csv

518 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     128 (24.7%)  126 (24.3%)  173 (33.4%)  221 (42.7%)
Timeouts                        389 (75.1%)  384 (74.1%)  345 (66.6%)  296 (57.1%)
Out of memory                      1 (0.2%)     8 (1.5%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     1 (0.2%)
Total problems                          518          518          518          518
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     115          115          167          167
Faster                           76 (66.1%)   39 (33.9%)   29 (17.4%)  138 (82.6%)
Found when the other did not             13           11            6           54
Median runtime                       7.11 s       8.23 s       8.48 s       3.28 s
Total runtime                   10,436.37 s  10,451.93 s  20,541.46 s   7,256.52 s
Shorter plan                     32 (27.8%)     0 (0.0%)     6 (3.6%)   36 (21.6%)
Same plan length                 83 (72.2%)   83 (72.2%)  125 (74.9%)  125 (74.9%)
Median plan length                       11           13           19           19
Total plan length                     1,699        1,788        4,393        4,261
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   334 (87%)    275 (80%)
Guided concrete search              33 (9%)     53 (15%)
Unguided concrete search            17 (4%)      17 (5%)
Total                                   384          345
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   98 (78%)    133 (77%)
Refined, some actions off          23 (18%)     35 (20%)
Solved above the abstract plan       5 (4%)       5 (3%)
Total                                   126          173
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                               13 (11%)     23 (14%)
1 to 4                             85 (70%)    122 (73%)
5 to 9                               4 (3%)       4 (2%)
10 to 19                           18 (15%)     18 (11%)
20 or more                           1 (1%)       1 (1%)
Total                                   121          168
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
depot                                9         1         1         3         3
driverlog                           13         7         6        10        10
elevators-opt08-strips               4         0         1         2         2
elevators-opt11-strips               2         0         1         2         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        11         9
logistics00                         19         8         9        15        15
logistics98                         31         1         0         4         4
miconic                             11         1         2        11        11
mprime                              21        20        20        16        16
mystery                             16        10        10         8         8
nomystery-opt11-strips              10         4         4         7         8
openstacks-opt08-strips             28         0         1         7        21
openstacks-opt11-strips             20         0         0         5        18
openstacks-opt14-strips             14         0         0         0         2
pipesworld-notankage                34        10         9         9        13
pipesworld-tankage                  47         8         9         8         9
quantum-layout-opt23-strips          7         4         3         3         4
satellite                           34         5         5         8        10
sokoban-opt08-strips                 3         1         1         2         3
sokoban-opt11-strips                 2         1         1         2         2
tpp                                 29         4         4         4         6
transport-opt08-strips               4         3         3         3         3
transport-opt14-strips               4         1         2         2         2
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips             5         0         0         1         1
woodworking-opt11-strips             4         0         0         0         1
zenotravel                          13         4         3         7         7
Total                              518       128       126       173       221
```
