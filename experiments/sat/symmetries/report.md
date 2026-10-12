# Benchmark report

2026-10-12 12:18 — experiments/sat/symmetries/results.csv

884 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found                     155 (17.5%)  182 (20.6%)  347 (39.3%)  771 (87.2%)
Timeouts                        716 (81.0%)  667 (75.5%)  377 (42.6%)    71 (8.0%)
Out of memory                     13 (1.5%)    35 (4.0%)  158 (17.9%)    40 (4.5%)
Others                             0 (0.0%)     0 (0.0%)     2 (0.2%)     2 (0.2%)
Total problems                          884          884          884          884
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ          FDᵅ           FD
----------------------------------------------------------------------------------
Plans found by both                     151          151          331          331
Faster                           98 (64.9%)   53 (35.1%)     7 (2.1%)  324 (97.9%)
Found when the other did not              4           31           16          440
Median runtime                       8.44 s       6.78 s      15.11 s       3.33 s
Total runtime                   16,826.71 s   9,797.02 s  34,687.47 s   4,210.38 s
Shorter plan                    108 (71.5%)     0 (0.0%)   67 (20.2%)  191 (57.7%)
Same plan length                 43 (28.5%)   43 (28.5%)   73 (22.1%)   73 (22.1%)
Median plan length                       11           15           38           31
Total plan length                     2,011        2,736       21,538       19,402
```

## Where the timeouts died

```
Killed during                          ASPᵅ          FDᵅ
--------------------------------------------------------
Abstract search                   583 (87%)      11 (3%)
Guided concrete search              41 (6%)    307 (81%)
Unguided concrete search            43 (6%)     59 (16%)
Total                                   667          377
```

## How the successes were solved

```
Solved by                              ASPᵅ          FDᵅ
--------------------------------------------------------
Refined directly                   94 (52%)    190 (55%)
Refined, some actions off          75 (41%)    144 (41%)
Solved above the abstract plan      13 (7%)      13 (4%)
Total                                   182          347
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ          FDᵅ
--------------------------------------------------------
None                                12 (7%)     33 (10%)
1 to 4                            107 (63%)    211 (63%)
5 to 9                              14 (8%)     45 (13%)
10 to 19                           31 (18%)     36 (11%)
20 or more                           5 (3%)       9 (3%)
Total                                   169          334
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ       FDᵅ        FD
------------------------------------------------------------------------------
agricola-sat18-strips               20         0         0         0        12
airport                             42        11        14        18        27
barman-sat11-strips                 20         0         0         0        20
barman-sat14-strips                 20         0         0         0        20
childsnack-sat14-strips             20         0         0         0         6
depot                               22         4         6         8        20
driverlog                           20         9        11        18        20
elevators-sat08-strips              30         1         1        12        30
elevators-sat11-strips              20         0         0         0        20
floortile-sat11-strips              20         0         0        11         7
floortile-sat14-strips              20         0         0        14         2
grid                                 5         2         3         3         5
gripper                             20         3         3         3        20
hiking-sat14-strips                 20         2         6        17        20
logistics00                         28        10        12        15        28
logistics98                         35         3         3         5        35
miconic                             11         1         2        11        11
mprime                              35        34        33        35        35
mystery                             28        19        19        18        19
nomystery-sat11-strips              20         2         2        10        12
openstacks-sat08-strips             29         2         2        23        29
openstacks-sat11-strips             15         0         0         4        15
openstacks-sat14-strips             12         0         0         0        12
pipesworld-notankage                49        12        21        26        42
pipesworld-tankage                  49         9        12        13        42
quantum-layout-sat23-strips          7         4         2         2         7
satellite                           36         6         6        14        36
sokoban-sat08-strips                29         2         2        14        28
sokoban-sat11-strips                19         0         0         9        18
tetris-sat14-strips                 20         0         0         0        16
tpp                                 29         4         6         6        29
transport-sat08-strips              30         5         6         8        30
transport-sat11-strips              20         0         0         0        18
transport-sat14-strips              20         0         0         0        16
woodworking-sat08-strips            27         3         3        17        27
woodworking-sat11-strips            19         0         0         0        19
zenotravel                          18         7         7        13        18
Total                              884       155       182       347       771
```
