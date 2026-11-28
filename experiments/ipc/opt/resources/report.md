# Benchmark report

2026-11-28 09:19 — experiments/ipc/opt/resources/results.csv

363 problems compared over asp, abs-asp, abs-lmcut, lmcut, lmcut-symmetry-pruning, rnd-g; 20 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut       LMcut+        rnd-g
------------------------------------------------------------------------------------------------------------
Plans found                     122 (33.6%)  120 (33.1%)  132 (36.4%)  199 (54.8%)  176 (48.5%)  153 (42.1%)
Timeouts                        241 (66.4%)  243 (66.9%)  231 (63.6%)  162 (44.6%)  185 (51.0%)  105 (28.9%)
Out of memory                      0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)  104 (28.7%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)     2 (0.6%)     1 (0.3%)
Total problems                          363          363          363          363          363          363
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          124          124
Faster                           92 (78.6%)   25 (21.4%)   23 (18.5%)  101 (81.5%)
Found when the other did not              5            3            8           75
Median runtime                       7.13 s      11.51 s       7.21 s       2.77 s
Total runtime                    8,344.08 s   9,154.02 s  10,661.86 s   9,176.80 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               117 (100.0%) 117 (100.0%) 124 (100.0%) 124 (100.0%)
Median plan length                        9            9           11           11
Total plan length                     1,240        1,240        1,539        1,539
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
Refined directly                   65 (54%)     71 (54%)
Refined, some actions off          15 (12%)     22 (17%)
Solved above the abstract plan     40 (33%)     39 (30%)
Total                                   120          132
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             46 (57%)     59 (63%)
5 to 9                             34 (42%)     32 (34%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    80           93
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut    LMcut+     rnd-g
----------------------------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20        20        14
elevators-opt08-strips (30)          9         8         9        25        20        13
elevators-opt11-strips (20)          7         6         7        20        17        11
freecell (73)                       10        10         9        26        15        15
mprime (29)                         29        29        24        23        22        18
mystery (26)                        17        17        17        16        16        15
nomystery-opt11-strips (20)         10         8        12        18        15        16
openstacks-opt08-strips (30)         2         2         2         9        10         8
openstacks-opt11-strips (20)         0         0         0         4         5         3
tpp (24)                             5         5         5         7         8         6
transport-opt08-strips (30)          9        10        15        13        12        14
transport-opt11-strips (20)          4         5         9         9         8        11
transport-opt14-strips (20)          3         4         7         8         7         8
visitall-opt11-strips (1)            1         1         1         1         1         1
Total (363)                        122       120       132       199       176       153
```
