# Benchmark report

2026-11-26 05:58 — experiments/ipc/opt/resources/results.csv

363 problems compared over asp, abs-asp, abs-lmcut, lmcut, lmcut-symmetry-pruning, rnd-g; 20 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut       LMcut+        rnd-g
------------------------------------------------------------------------------------------------------------
Plans found                     122 (33.6%)  120 (33.1%)  132 (36.4%)  206 (56.7%)  176 (48.5%)  153 (42.1%)
Timeouts                        241 (66.4%)  243 (66.9%)  231 (63.6%)  155 (42.7%)  185 (51.0%)  105 (28.9%)
Out of memory                      0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)  104 (28.7%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)     2 (0.6%)     1 (0.3%)
Total problems                          363          363          363          363          363          363
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          125          125
Faster                           92 (78.6%)   25 (21.4%)   23 (18.4%)  102 (81.6%)
Found when the other did not              5            3            7           81
Median runtime                       7.15 s      12.71 s       7.79 s       2.94 s
Total runtime                    9,460.61 s   9,810.49 s  11,626.07 s   7,260.11 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               117 (100.0%) 117 (100.0%) 125 (100.0%) 125 (100.0%)
Median plan length                        9            9           11           11
Total plan length                     1,240        1,240        1,569        1,569
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   130 (53%)     31 (13%)
Guided concrete search               8 (3%)     35 (15%)
Unguided concrete search          105 (43%)    165 (71%)
Total                                   243          231
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   64 (53%)     72 (55%)
Refined, some actions off          15 (12%)     20 (15%)
Solved above the abstract plan     41 (34%)     40 (30%)
Total                                   120          132
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             47 (59%)     60 (65%)
5 to 9                             32 (41%)     30 (33%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    79           92
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut    LMcut+     rnd-g
----------------------------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20        20        14
elevators-opt08-strips (30)          9         8         9        26        20        13
elevators-opt11-strips (20)          7         6         7        20        17        11
freecell (73)                       10        10         9        27        15        15
mprime (29)                         29        29        24        23        22        18
mystery (26)                        17        17        17        16        16        15
nomystery-opt11-strips (20)         10         8        12        18        15        16
openstacks-opt08-strips (30)         2         2         2        10        10         8
openstacks-opt11-strips (20)         0         0         0         5         5         3
tpp (24)                             5         5         5         7         8         6
transport-opt08-strips (30)          9        10        15        14        12        14
transport-opt11-strips (20)          4         5         9        10         8        11
transport-opt14-strips (20)          3         4         7         9         7         8
visitall-opt11-strips (1)            1         1         1         1         1         1
Total (363)                        122       120       132       206       176       153
```
