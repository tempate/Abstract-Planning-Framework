# Benchmark report

2026-11-05 10:16 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   90 (27.3%)  125 (37.9%)  305 (92.4%)
Timeouts                        240 (72.7%)  240 (72.7%)  177 (53.6%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    28 (8.5%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      82           82          125          125
Faster                           61 (74.4%)   21 (25.6%)     1 (0.8%)  124 (99.2%)
Found when the other did not              7            8            0          180
Median runtime                       6.27 s      14.52 s      18.35 s       3.15 s
Total runtime                    3,374.27 s   3,920.99 s   9,210.96 s     775.32 s
Shorter plan                     66 (80.5%)     3 (3.7%)     4 (3.2%)  109 (87.2%)
Same plan length                 13 (15.9%)   13 (15.9%)    12 (9.6%)    12 (9.6%)
Median plan length                        8           16           24           18
Total plan length                     1,156        1,702        6,263        4,969
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          4 (2%)       4 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   134 (56%)       3 (2%)
Guided concrete search             34 (14%)     64 (36%)
Unguided concrete search           67 (28%)    105 (59%)
Total                                   240          177
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   63 (70%)     98 (78%)
Refined, some actions off          20 (22%)     19 (15%)
Solved above the abstract plan       7 (8%)       8 (6%)
Total                                    90          125
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             25 (30%)     38 (32%)
5 to 9                             37 (45%)     39 (33%)
10 to 19                             7 (8%)     12 (10%)
20 or more                         14 (17%)     28 (24%)
Total                                    83          117
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
data-network-sat18-strips (15)         0         1         1        12
elevators-sat08-strips (30)          2         6         7        30
elevators-sat11-strips (14)          0         0         0        14
freecell (73)                       16        13        10        72
mprime (29)                         28        28        29        29
mystery (26)                        17        17        17        17
nomystery-sat11-strips (19)          4         2        10        12
openstacks-sat08-strips (27)         5         6        24        27
openstacks-sat11-strips (7)          0         0         4         7
thoughtful-sat14-strips (20)         5         5         5        15
tpp (24)                             6         6         6        24
transport-sat08-strips (30)          6         6        12        30
transport-sat11-strips (13)          0         0         0        13
transport-sat14-strips (3)           0         0         0         3
Total (330)                         89        90       125       305
```
