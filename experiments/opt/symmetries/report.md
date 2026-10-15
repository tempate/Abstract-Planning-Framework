# Benchmark report

2026-10-15 09:31 — experiments/opt/symmetries/results.csv

866 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     222 (25.6%)  126 (14.5%)  173 (20.0%)  410 (47.3%)
Timeouts                        643 (74.2%)  384 (44.3%)  345 (39.8%)  454 (52.4%)
Out of memory                      1 (0.1%)     8 (0.9%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)  348 (40.2%)  348 (40.2%)     2 (0.2%)
Total problems                          866          866          866          866
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     115          115          167          167
Faster                           76 (66.1%)   39 (33.9%)   29 (17.4%)  138 (82.6%)
Found when the other did not            107           11            6          243
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
airport                             42        11        11        19        22
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                               22         4         1         3         8
driverlog                           20         9         6        10        14
elevators-opt08-strips              20         5         1         2        12
elevators-opt11-strips              13         5         1         2        11
floortile-opt11-strips              20         2         0         0         7
floortile-opt14-strips              20         0         0         0         7
grid                                 5         2         0         0         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        11         9
logistics00                         28        10         9        15        20
logistics98                         35         3         0         4         6
miconic                             11         1         2        11        11
mprime                              35        34        20        16        24
mystery                             28        19        10         8        17
nomystery-opt11-strips              20        10         4         7        18
openstacks-opt08-strips             28         0         1         7        21
openstacks-opt11-strips             20         0         0         5        18
openstacks-opt14-strips             14         0         0         0         2
pipesworld-notankage                49        13         9         9        17
pipesworld-tankage                  49         9         9         8        11
quantum-layout-opt23-strips          7         4         3         3         4
satellite                           36         6         5         8        12
sokoban-opt08-strips                29         4         1         2        29
sokoban-opt11-strips                19         1         1         2        19
tetris-opt14-strips                 16         2         0         0         5
tpp                                 29         4         4         4         6
transport-opt08-strips              30        10         3         3        11
transport-opt11-strips              20         5         0         0         6
transport-opt14-strips              20         3         2         2         6
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips            28         9         0         1        18
woodworking-opt11-strips            20         6         0         0        14
zenotravel                          18         7         3         7        11
Total                              866       222       126       173       410
```
