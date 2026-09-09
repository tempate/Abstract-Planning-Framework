# Benchmark report

2026-09-09 11:36 — benchmarks/results.csv

376 problems every configuration finished, 5 dropped as unfinished

## Coverage

```
Configuration  Plans found  Timeouts  No plan found  Other  vs baseline
-----------------------------------------------------------------------
concrete        75 (19.9%)       301              0      0     +3 / -11
baseline        83 (22.1%)       291              2      0            —
both            71 (18.9%)       303              2      0     +2 / -14
no-goal         90 (23.9%)       284              2      0      +8 / -1
no-init         83 (22.1%)       291              2      0      +8 / -8
```

## Against the concrete pipeline, runtimes as variant / concrete

```
Variant   Solved by both    Faster  Only the variant  Only concrete       Median                Total
-----------------------------------------------------------------------------------------------------
baseline              72  23 (32%)                11              3  6.6 / 9.0 s  3,942.1 / 6,867.9 s
both                  69  12 (17%)                 2              6  7.1 / 6.6 s  8,294.2 / 3,863.2 s
no-goal               72  22 (31%)                18              3  5.4 / 9.0 s  3,377.3 / 6,867.9 s
no-init               71  22 (31%)                12              4  6.1 / 8.9 s  7,306.7 / 6,838.4 s
```

## How much each variant collapsed

```
Variant   Median objects  Mean  Most  Median classes  Most  Class grew vs baseline
----------------------------------------------------------------------------------
baseline               5  19.4   266               2    32                       —
both                  23  38.9   450               3    33               333 (89%)
no-goal               12  24.6   284               4    34               248 (66%)
no-init               16  32.2   391               4    35               284 (76%)
```

## Where the timeouts died

```
Variant   Abstract search  Guided concrete search  Extended concrete search  Timeouts
-------------------------------------------------------------------------------------
baseline        246 (85%)                28 (10%)                   17 (6%)       291
both             38 (13%)               104 (34%)                 161 (53%)       303
no-goal         223 (79%)                44 (15%)                   17 (6%)       284
no-init         159 (55%)                88 (30%)                  44 (15%)       291
```

## How the successes were solved

```
Variant   Refined directly  Switched actions off  Discarded, solved above  Successes
------------------------------------------------------------------------------------
baseline          52 (63%)              26 (31%)                   5 (6%)         83
both              12 (17%)              19 (27%)                 40 (56%)         71
no-goal           57 (63%)              28 (31%)                   5 (6%)         90
no-init           23 (28%)              43 (52%)                 17 (20%)         83
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Variant       None    1 to 4    5 to 9  10 to 19  20 or more  Median  Most  Problems
------------------------------------------------------------------------------------
baseline  11 (14%)  39 (50%)    5 (6%)  14 (18%)     9 (12%)       2    22        78
both       6 (19%)   4 (13%)   6 (19%)   5 (16%)    10 (32%)       7   399        31
no-goal   11 (13%)  39 (46%)  10 (12%)  15 (18%)    10 (12%)       4    22        85
no-init   11 (17%)  14 (21%)  14 (21%)  14 (21%)    13 (20%)       5   409        66
```
