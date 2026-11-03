# Benchmark report

2026-11-03 10:45 — experiments/ipc/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   90 (27.3%)  128 (38.8%)  305 (92.4%)
Timeouts                        240 (72.7%)  240 (72.7%)  174 (52.7%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    28 (8.5%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      82           82          128          128
Faster                           59 (72.0%)   23 (28.0%)     4 (3.1%)  124 (96.9%)
Found when the other did not              7            8            0          177
Median runtime                       6.27 s      12.79 s      15.20 s       3.15 s
Total runtime                    3,374.27 s   3,886.98 s  13,083.56 s     785.69 s
Shorter plan                     68 (82.9%)     3 (3.7%)     4 (3.1%)  112 (87.5%)
Same plan length                 11 (13.4%)   11 (13.4%)    12 (9.4%)    12 (9.4%)
Median plan length                        8           16         27.5         18.5
Total plan length                     1,156        1,701        6,664        5,178
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       4 (2%)
Writing the abstract task            2 (1%)       0 (0%)
Abstract search                   133 (55%)       3 (2%)
Guided concrete search             35 (15%)     62 (36%)
Unguided concrete search           67 (28%)    105 (60%)
Total                                   240          174
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   63 (70%)    100 (78%)
Refined, some actions off          20 (22%)     20 (16%)
Solved above the abstract plan       7 (8%)       8 (6%)
Total                                    90          128
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             25 (30%)     39 (32%)
5 to 9                             37 (45%)     39 (32%)
10 to 19                             7 (8%)     14 (12%)
20 or more                         14 (17%)     28 (23%)
Total                                    83          120
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
data-network-sat18-strips (15)         0         1         1        12
elevators-sat08-strips (30)          2         6         9        30
elevators-sat11-strips (14)          0         0         0        14
freecell (73)                       16        13        10        72
mprime (29)                         28        28        29        29
mystery (26)                        17        17        17        17
nomystery-sat11-strips (19)          4         2        10        12
openstacks-sat08-strips (27)         5         6        24        27
openstacks-sat11-strips (7)          0         0         4         7
thoughtful-sat14-strips (20)         5         5         5        15
tpp (24)                             6         6         6        24
transport-sat08-strips (30)          6         6        13        30
transport-sat11-strips (13)          0         0         0        13
transport-sat14-strips (3)           0         0         0         3
Total (330)                         89        90       128       305
```
