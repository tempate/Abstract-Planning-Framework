# Benchmark report

2026-10-12 12:18 — experiments/opt/results.csv

866 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     222 (25.6%)  216 (24.9%)  279 (32.2%)  410 (47.3%)
Timeouts                        643 (74.2%)  628 (72.5%)  567 (65.5%)  454 (52.4%)
Out of memory                      1 (0.1%)    22 (2.5%)    18 (2.1%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     2 (0.2%)     2 (0.2%)
Total problems                          866          866          866          866
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     196          196          261          261
Faster                          127 (64.8%)   69 (35.2%)   40 (15.3%)  221 (84.7%)
Found when the other did not             26           20           18          149
Median runtime                       8.61 s       8.26 s       7.70 s       3.06 s
Total runtime                   27,577.78 s  19,894.05 s  41,860.57 s  14,294.33 s
Shorter plan                     68 (34.7%)     0 (0.0%)   30 (11.5%)   89 (34.1%)
Same plan length                128 (65.3%)  128 (65.3%)  142 (54.4%)  142 (54.4%)
Median plan length                       12           13           18           17
Total plan length                     2,794        3,002        6,710        6,827
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   494 (79%)    347 (61%)
Guided concrete search             80 (13%)    149 (26%)
Unguided concrete search            54 (9%)     71 (13%)
Total                                   628          567
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  120 (56%)    159 (57%)
Refined, some actions off          81 (38%)    105 (38%)
Solved above the abstract plan      15 (7%)      15 (5%)
Total                                   216          279
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                13 (6%)      25 (9%)
1 to 4                            148 (74%)    188 (71%)
5 to 9                             20 (10%)     30 (11%)
10 to 19                            19 (9%)      20 (8%)
20 or more                           1 (0%)       1 (0%)
Total                                   201          264
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
agricola-opt18-strips               20         8         3         0         0
airport                             42        11        11        11        22
barman-opt11-strips                 20         0         0         0         4
barman-opt14-strips                 14         0         0         0         0
childsnack-opt14-strips             20         0         0         0         0
depot                               22         4         2         2         8
driverlog                           20         9        11        12        14
elevators-opt08-strips              20         5         7        12        12
elevators-opt11-strips              13         5         6        11        11
floortile-opt11-strips              20         2         0         2         7
floortile-opt14-strips              20         0         0         0         7
grid                                 5         2         3         2         2
gripper                             20         3         3         3         7
hiking-opt14-strips                 20        12        13        11         9
logistics00                         28        10        12        12        20
logistics98                         35         3         3         2         6
miconic                             11         1         2        11        11
mprime                              35        34        33        27        24
mystery                             28        19        19        19        17
nomystery-opt11-strips              20        10         7        14        18
openstacks-opt08-strips             28         0         2         7        21
openstacks-opt11-strips             20         0         0         5        18
openstacks-opt14-strips             14         0         0         0         2
pipesworld-notankage                49        13        11        13        17
pipesworld-tankage                  49         9         8         7        11
quantum-layout-opt23-strips          7         4         3         3         4
satellite                           36         6         6        10        12
sokoban-opt08-strips                29         4         4        11        29
sokoban-opt11-strips                19         1         1         6        19
tetris-opt14-strips                 16         2         0         0         5
tpp                                 29         4         4         4         6
transport-opt08-strips              30        10        10        12        11
transport-opt11-strips              20         5         5         8         6
transport-opt14-strips              20         3         4         4         6
visitall-opt11-strips                1         1         1         1         1
woodworking-opt08-strips            28         9         9        15        18
woodworking-opt11-strips            20         6         6        11        14
zenotravel                          18         7         7        11        11
Total                              866       222       216       279       410
```
