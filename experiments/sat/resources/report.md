# Benchmark report

2026-11-05 11:33 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   92 (27.9%)  121 (36.7%)  305 (92.4%)
Timeouts                        240 (72.7%)  238 (72.1%)  181 (54.8%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    28 (8.5%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      85           85          121          121
Faster                           61 (71.8%)   24 (28.2%)     4 (3.3%)  117 (96.7%)
Found when the other did not              4            7            0          184
Median runtime                       7.11 s      15.33 s      17.26 s       3.07 s
Total runtime                    4,884.80 s   4,207.55 s   9,007.24 s     648.61 s
Shorter plan                     69 (81.2%)     3 (3.5%)     2 (1.7%)  110 (90.9%)
Same plan length                 13 (15.3%)   13 (15.3%)     9 (7.4%)     9 (7.4%)
Median plan length                        8           16           23           18
Total plan length                     1,238        1,830        6,150        4,835
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          4 (2%)       4 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   134 (56%)       3 (2%)
Guided concrete search             28 (12%)     63 (35%)
Unguided concrete search           71 (30%)    110 (61%)
Total                                   238          181
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   61 (66%)     93 (77%)
Refined, some actions off          24 (26%)     20 (17%)
Solved above the abstract plan       7 (8%)       8 (7%)
Total                                    92          121
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             28 (33%)     35 (31%)
5 to 9                             36 (42%)     38 (34%)
10 to 19                             7 (8%)     12 (11%)
20 or more                         14 (16%)     28 (25%)
Total                                    85          113
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
nomystery-sat11-strips (19)          4         4         6        12
openstacks-sat08-strips (27)         5         6        24        27
openstacks-sat11-strips (7)          0         0         4         7
thoughtful-sat14-strips (20)         5         5         5        15
tpp (24)                             6         6         6        24
transport-sat08-strips (30)          6         6        12        30
transport-sat11-strips (13)          0         0         0        13
transport-sat14-strips (3)           0         0         0         3
Total (330)                         89        92       121       305
```
