# Benchmark report

2026-09-09 10:09 — benchmarks/results.csv

376 problems every configuration finished, 5 dropped as unfinished

## Coverage

```
Configuration  Plans found  Timeouts  No plan found  vs baseline
----------------------------------------------------------------
concrete        75 (19.9%)       301              0     +3 / -11
baseline        83 (22.1%)       291              2            —
both            77 (20.5%)       297              2     +5 / -11
no-goal         85 (22.6%)       289              2      +5 / -3
no-init         90 (23.9%)       284              2     +10 / -3
```

## Against the concrete pipeline, runtimes as variant / concrete

```
Variant   Solved by both    Faster  Only the variant  Only concrete       Median                Total
-----------------------------------------------------------------------------------------------------
baseline              72  17 (24%)                11              3  7.5 / 9.0 s  5,332.5 / 6,815.3 s
both                  72  15 (21%)                 5              3  6.7 / 9.0 s  8,544.3 / 8,715.5 s
no-goal               71  17 (24%)                14              4  6.1 / 8.8 s  5,237.4 / 6,781.8 s
no-init               75  29 (39%)                15              0  6.8 / 9.6 s  4,331.6 / 9,445.5 s
```

## How many objects each variant collapsed

```
Variant   Median objects  Mean  Largest  Class grew vs baseline
---------------------------------------------------------------
baseline               2   5.5       60                       —
both                  10  17.2      201               305 (82%)
no-goal                3   8.7      196               135 (36%)
no-init                5  10.6      106               237 (63%)
```

## Where the timeouts died

```
Variant   Abstract search  Guided concrete search  Extended concrete search  Timeouts
-------------------------------------------------------------------------------------
baseline        267 (92%)                  7 (2%)                   17 (6%)       291
both            123 (41%)                89 (30%)                  85 (29%)       297
no-goal         256 (89%)                 16 (6%)                   17 (6%)       289
no-init         234 (82%)                30 (11%)                   20 (7%)       284
```

## How the successes were solved

```
Variant   Refined directly  Switched actions off  Discarded, solved above  Successes
------------------------------------------------------------------------------------
baseline          56 (67%)              22 (27%)                   5 (6%)         83
both              19 (25%)              26 (34%)                 32 (42%)         77
no-goal           56 (66%)              24 (28%)                   5 (6%)         85
no-init           48 (53%)              35 (39%)                   7 (8%)         90
```

## Deletes relaxed, over the successes whose abstract plan was used

```
Variant       None    1 to 4    5 to 9  10 to 19  20 or more  Median  Most  Problems
------------------------------------------------------------------------------------
baseline  11 (14%)  39 (50%)  13 (17%)  15 (19%)      0 (0%)       2    14        78
both       9 (20%)  13 (29%)    2 (4%)  19 (42%)      2 (4%)       6   327        45
no-goal   11 (14%)  41 (51%)  10 (12%)  18 (22%)      0 (0%)       3    14        80
no-init   11 (13%)  43 (52%)   8 (10%)  19 (23%)      2 (2%)       2   409        83
```
