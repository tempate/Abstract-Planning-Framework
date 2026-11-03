# Benchmark report

2026-11-03 10:45 — experiments/opt/resources/results.csv

363 problems compared over asp, abs-asp, abs-lmcut, lmcut; 10 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     126 (34.7%)  126 (34.7%)  138 (38.0%)  207 (57.0%)
Timeouts                        237 (65.3%)  237 (65.3%)  225 (62.0%)  154 (42.4%)
Out of memory                      0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          363          363          363          363
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     119          119          130          130
Faster                           97 (81.5%)   22 (18.5%)   20 (15.4%)  110 (84.6%)
Found when the other did not              7            7            8           77
Median runtime                       6.69 s      15.33 s      10.67 s       2.70 s
Total runtime                    9,985.83 s   8,484.35 s   9,877.15 s   6,983.81 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               119 (100.0%) 119 (100.0%) 130 (100.0%) 130 (100.0%)
Median plan length                       10           10         11.5         11.5
Total plan length                     1,299        1,299        1,694        1,694
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   126 (53%)     31 (14%)
Guided concrete search               8 (3%)     35 (16%)
Unguided concrete search          103 (43%)    159 (71%)
Total                                   237          225
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   77 (61%)     83 (60%)
Refined, some actions off            9 (7%)     14 (10%)
Solved above the abstract plan     40 (32%)     41 (30%)
Total                                   126          138
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             53 (62%)     64 (66%)
5 to 9                             33 (38%)     31 (32%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    86           97
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20
elevators-opt08-strips (30)         10         8         9        26
elevators-opt11-strips (20)          9         6         7        20
freecell (73)                       10         9        10        28
mprime (29)                         29        29        24        23
mystery (26)                        17        17        17        16
nomystery-opt11-strips (20)         10        12        17        18
openstacks-opt08-strips (30)         2         2         2        10
openstacks-opt11-strips (20)         0         0         0         5
tpp (24)                             5         5         5         7
transport-opt08-strips (30)          9        11        15        14
transport-opt11-strips (20)          5         6         9        10
transport-opt14-strips (20)          3         5         7         9
visitall-opt11-strips (1)            1         1         1         1
Total (363)                        126       126       138       207
```
