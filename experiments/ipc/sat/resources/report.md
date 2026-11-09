# Benchmark report

2026-11-09 09:01 — experiments/ipc/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      88 (26.7%)   92 (27.9%)  122 (37.0%)  305 (92.4%)
Timeouts                        242 (73.3%)  238 (72.1%)  181 (54.8%)    22 (6.7%)
Out of memory                      0 (0.0%)     0 (0.0%)    27 (8.2%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      85           85          122          122
Faster                           51 (60.0%)   34 (40.0%)     4 (3.3%)  118 (96.7%)
Found when the other did not              3            7            0          183
Median runtime                       8.89 s      10.04 s      10.49 s       3.10 s
Total runtime                    6,673.30 s   3,546.61 s   7,008.55 s     651.79 s
Shorter plan                     31 (36.5%)   12 (14.1%)   17 (13.9%)   68 (55.7%)
Same plan length                 42 (49.4%)   42 (49.4%)   37 (30.3%)   37 (30.3%)
Median plan length                        8           11           20           18
Total plan length                     1,238        1,490        5,719        4,910
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          4 (2%)       4 (2%)
Abstract search                   135 (57%)       3 (2%)
Guided concrete search             28 (12%)     63 (35%)
Unguided concrete search           71 (30%)    111 (61%)
Total                                   238          181
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   61 (66%)     94 (77%)
Refined, some actions off          24 (26%)     20 (16%)
Solved above the abstract plan       7 (8%)       8 (7%)
Total                                    92          122
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             28 (33%)     36 (32%)
5 to 9                             36 (42%)     38 (33%)
10 to 19                             7 (8%)     12 (11%)
20 or more                         14 (16%)     28 (25%)
Total                                    85          114
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
data-network-sat18-strips (15)         0         1         1        12
elevators-sat08-strips (30)          2         6         7        30
elevators-sat11-strips (14)          0         0         0        14
freecell (73)                       15        13        10        72
mprime (29)                         28        28        29        29
mystery (26)                        17        17        17        17
nomystery-sat11-strips (19)          4         4         6        12
openstacks-sat08-strips (27)         5         6        24        27
openstacks-sat11-strips (7)          0         0         4         7
thoughtful-sat14-strips (20)         5         5         5        15
tpp (24)                             6         6         6        24
transport-sat08-strips (30)          6         6        13        30
transport-sat11-strips (13)          0         0         0        13
transport-sat14-strips (3)           0         0         0         3
Total (330)                         88        92       122       305
```
