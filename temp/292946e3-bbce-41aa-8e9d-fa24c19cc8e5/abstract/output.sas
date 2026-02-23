begin_version
3
end_version
begin_metric
1
end_metric
24
begin_variable
var0
-1
2
Atom size(jig0001, n18)
Atom size(jig0001, n25)
end_variable
begin_variable
var1
-1
2
Atom size(jig0002, n09)
Atom size(jig0002, n18)
end_variable
begin_variable
var2
-1
2
Atom empty(hangar1)
NegatedAtom empty(hangar1)
end_variable
begin_variable
var3
-1
2
Atom empty(hangar2)
NegatedAtom empty(hangar2)
end_variable
begin_variable
var4
-1
2
Atom to_deliver(dummy-jig, pl0)
Atom to_deliver(jig0002, pl0)
end_variable
begin_variable
var5
-1
2
Atom to_deliver(dummy-jig, pl1)
Atom to_deliver(jig0001, pl1)
end_variable
begin_variable
var6
-1
2
Atom empty(hangar3)
NegatedAtom empty(hangar3)
end_variable
begin_variable
var7
-1
2
Atom empty(rack00)
NegatedAtom empty(rack00)
end_variable
begin_variable
var8
-1
3
Atom free-space(rack00, n04)
Atom free-space(rack00, n13)
Atom free-space(rack00, n22)
end_variable
begin_variable
var9
-1
2
Atom next-to(jig0001, jig0002, fside)
NegatedAtom next-to(jig0001, jig0002, fside)
end_variable
begin_variable
var10
-1
2
Atom next-to(jig0002, jig0001, bside)
NegatedAtom next-to(jig0002, jig0001, bside)
end_variable
begin_variable
var11
-1
2
Atom clear(jig0001, bside)
NegatedAtom clear(jig0001, bside)
end_variable
begin_variable
var12
-1
8
Atom in(jig0001, beluga_abs_trailer)
Atom in(jig0001, factory_trailer_1)
Atom in(jig0001, factory_trailer_2)
Atom in(jig0001, hangar1)
Atom in(jig0001, hangar2)
Atom in(jig0001, hangar3)
Atom in(jig0001, rack00)
Atom in(jig0001, rack01)
end_variable
begin_variable
var13
-1
2
Atom next-to(jig0001, jig0002, bside)
NegatedAtom next-to(jig0001, jig0002, bside)
end_variable
begin_variable
var14
-1
2
Atom next-to(jig0002, jig0001, fside)
NegatedAtom next-to(jig0002, jig0001, fside)
end_variable
begin_variable
var15
-1
2
Atom clear(jig0001, fside)
NegatedAtom clear(jig0001, fside)
end_variable
begin_variable
var16
-1
2
Atom empty(rack01)
NegatedAtom empty(rack01)
end_variable
begin_variable
var17
-1
2
Atom clear(jig0002, bside)
NegatedAtom clear(jig0002, bside)
end_variable
begin_variable
var18
-1
9
Atom in(jig0002, beluga1)
Atom in(jig0002, beluga_abs_trailer)
Atom in(jig0002, factory_trailer_1)
Atom in(jig0002, factory_trailer_2)
Atom in(jig0002, hangar1)
Atom in(jig0002, hangar2)
Atom in(jig0002, hangar3)
Atom in(jig0002, rack00)
Atom in(jig0002, rack01)
end_variable
begin_variable
var19
-1
7
Atom free-space(rack01, n04)
Atom free-space(rack01, n06)
Atom free-space(rack01, n13)
Atom free-space(rack01, n15)
Atom free-space(rack01, n22)
Atom free-space(rack01, n31)
Atom free-space(rack01, n40)
end_variable
begin_variable
var20
-1
2
Atom clear(jig0002, fside)
NegatedAtom clear(jig0002, fside)
end_variable
begin_variable
var21
-1
2
Atom to_unload(dummy-jig, beluga1)
Atom to_unload(jig0002, beluga1)
end_variable
begin_variable
var22
-1
2
Atom empty(jig0002)
NegatedAtom empty(jig0002)
end_variable
begin_variable
var23
-1
2
Atom empty(jig0001)
NegatedAtom empty(jig0001)
end_variable
0
begin_state
1
1
0
0
1
1
0
0
2
1
1
0
7
1
1
0
1
1
0
3
1
1
1
1
end_state
begin_goal
3
21 0
22 0
23 0
end_goal
241
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar1 pl1 n18 n18
1
0 0
4
0 2 0 1
0 23 -1 0
0 12 1 3
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar1 pl1 n25 n18
0
5
0 2 0 1
0 23 -1 0
0 12 1 3
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar2 pl1 n18 n18
1
0 0
4
0 3 0 1
0 23 -1 0
0 12 1 4
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar2 pl1 n25 n18
0
5
0 3 0 1
0 23 -1 0
0 12 1 4
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar3 pl1 n18 n18
1
0 0
4
0 6 0 1
0 23 -1 0
0 12 1 5
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_1 hangar3 pl1 n25 n18
0
5
0 6 0 1
0 23 -1 0
0 12 1 5
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar1 pl1 n18 n18
1
0 0
4
0 2 0 1
0 23 -1 0
0 12 2 3
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar1 pl1 n25 n18
0
5
0 2 0 1
0 23 -1 0
0 12 2 3
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar2 pl1 n18 n18
1
0 0
4
0 3 0 1
0 23 -1 0
0 12 2 4
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar2 pl1 n25 n18
0
5
0 3 0 1
0 23 -1 0
0 12 2 4
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar3 pl1 n18 n18
1
0 0
4
0 6 0 1
0 23 -1 0
0 12 2 5
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0001 dummy-jig factory_trailer_2 hangar3 pl1 n25 n18
0
5
0 6 0 1
0 23 -1 0
0 12 2 5
0 0 1 0
0 5 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar1 pl0 n09 n09
1
1 0
4
0 2 0 1
0 22 -1 0
0 18 2 4
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar1 pl0 n18 n09
0
5
0 2 0 1
0 22 -1 0
0 18 2 4
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar2 pl0 n09 n09
1
1 0
4
0 3 0 1
0 22 -1 0
0 18 2 5
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar2 pl0 n18 n09
0
5
0 3 0 1
0 22 -1 0
0 18 2 5
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar3 pl0 n09 n09
1
1 0
4
0 6 0 1
0 22 -1 0
0 18 2 6
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_1 hangar3 pl0 n18 n09
0
5
0 6 0 1
0 22 -1 0
0 18 2 6
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar1 pl0 n09 n09
1
1 0
4
0 2 0 1
0 22 -1 0
0 18 3 4
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar1 pl0 n18 n09
0
5
0 2 0 1
0 22 -1 0
0 18 3 4
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar2 pl0 n09 n09
1
1 0
4
0 3 0 1
0 22 -1 0
0 18 3 5
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar2 pl0 n18 n09
0
5
0 3 0 1
0 22 -1 0
0 18 3 5
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar3 pl0 n09 n09
1
1 0
4
0 6 0 1
0 22 -1 0
0 18 3 6
0 4 1 0
1
end_operator
begin_operator
deliver-to-hangar jig0002 dummy-jig factory_trailer_2 hangar3 pl0 n18 n09
0
5
0 6 0 1
0 22 -1 0
0 18 3 6
0 1 1 0
0 4 1 0
1
end_operator
begin_operator
get-from-hangar jig0001 hangar1 factory_trailer_1
0
2
0 2 -1 0
0 12 3 1
1
end_operator
begin_operator
get-from-hangar jig0001 hangar1 factory_trailer_2
0
2
0 2 -1 0
0 12 3 2
1
end_operator
begin_operator
get-from-hangar jig0001 hangar2 factory_trailer_1
0
2
0 3 -1 0
0 12 4 1
1
end_operator
begin_operator
get-from-hangar jig0001 hangar2 factory_trailer_2
0
2
0 3 -1 0
0 12 4 2
1
end_operator
begin_operator
get-from-hangar jig0001 hangar3 factory_trailer_1
0
2
0 6 -1 0
0 12 5 1
1
end_operator
begin_operator
get-from-hangar jig0001 hangar3 factory_trailer_2
0
2
0 6 -1 0
0 12 5 2
1
end_operator
begin_operator
get-from-hangar jig0002 hangar1 factory_trailer_1
0
2
0 2 -1 0
0 18 4 2
1
end_operator
begin_operator
get-from-hangar jig0002 hangar1 factory_trailer_2
0
2
0 2 -1 0
0 18 4 3
1
end_operator
begin_operator
get-from-hangar jig0002 hangar2 factory_trailer_1
0
2
0 3 -1 0
0 18 5 2
1
end_operator
begin_operator
get-from-hangar jig0002 hangar2 factory_trailer_2
0
2
0 3 -1 0
0 18 5 3
1
end_operator
begin_operator
get-from-hangar jig0002 hangar3 factory_trailer_1
0
2
0 6 -1 0
0 18 6 2
1
end_operator
begin_operator
get-from-hangar jig0002 hangar3 factory_trailer_2
0
2
0 6 -1 0
0 18 6 3
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack00 bside fside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 7 -1 0
0 8 0 2
0 12 6 0
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack01 bside fside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 0 4
0 12 7 0
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack01 bside fside n18 n13 n31
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 2 5
0 12 7 0
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack01 bside fside n18 n22 n40
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 4 6
0 12 7 0
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack01 bside fside n25 n06 n31
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 1 5
0 12 7 0
1
end_operator
begin_operator
pick-up-rack jig0001 beluga_abs_trailer rack01 bside fside n25 n15 n40
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 3 6
0 12 7 0
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack00 fside bside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 7 -1 0
0 8 0 2
0 12 6 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack01 fside bside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 0 4
0 12 7 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack01 fside bside n18 n13 n31
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 2 5
0 12 7 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack01 fside bside n18 n22 n40
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 4 6
0 12 7 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack01 fside bside n25 n06 n31
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 1 5
0 12 7 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_1 rack01 fside bside n25 n15 n40
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 3 6
0 12 7 1
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack00 fside bside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 7 -1 0
0 8 0 2
0 12 6 2
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack01 fside bside n18 n04 n22
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 0 4
0 12 7 2
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack01 fside bside n18 n13 n31
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 2 5
0 12 7 2
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack01 fside bside n18 n22 n40
1
0 0
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 4 6
0 12 7 2
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack01 fside bside n25 n06 n31
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 1 5
0 12 7 2
1
end_operator
begin_operator
pick-up-rack jig0001 factory_trailer_2 rack01 fside bside n25 n15 n40
1
0 1
5
0 11 0 1
0 15 0 1
0 16 -1 0
0 19 3 6
0 12 7 2
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack00 bside fside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 1
0 18 7 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack00 bside fside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 1 2
0 18 7 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack00 bside fside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 2
0 18 7 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 2
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n09 n06 n15
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 1 3
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 4
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n09 n22 n31
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 5
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n09 n31 n40
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 5 6
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 4
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n18 n13 n31
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 5
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 beluga_abs_trailer rack01 bside fside n18 n22 n40
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 6
0 18 8 1
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack00 fside bside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 1
0 18 7 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack00 fside bside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 1 2
0 18 7 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack00 fside bside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 2
0 18 7 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 2
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n09 n06 n15
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 1 3
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 4
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n09 n22 n31
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 5
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n09 n31 n40
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 5 6
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 4
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n18 n13 n31
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 5
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_1 rack01 fside bside n18 n22 n40
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 6
0 18 8 2
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack00 fside bside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 1
0 18 7 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack00 fside bside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 1 2
0 18 7 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack00 fside bside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 7 -1 0
0 8 0 2
0 18 7 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n09 n04 n13
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 2
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n09 n06 n15
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 1 3
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n09 n13 n22
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 4
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n09 n22 n31
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 5
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n09 n31 n40
1
1 0
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 5 6
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n18 n04 n22
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 0 4
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n18 n13 n31
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 2 5
0 18 8 3
1
end_operator
begin_operator
pick-up-rack jig0002 factory_trailer_2 rack01 fside bside n18 n22 n40
1
1 1
5
0 17 0 1
0 20 0 1
0 16 -1 0
0 19 4 6
0 18 8 3
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack00 bside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 7 0 1
0 8 2 0
0 12 0 6
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack01 bside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 4 0
0 12 0 7
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack01 bside n18 n31 n13
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 2
0 12 0 7
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack01 bside n18 n40 n22
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 4
0 12 0 7
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack01 bside n25 n31 n06
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 1
0 12 0 7
1
end_operator
begin_operator
put-down-rack jig0001 beluga_abs_trailer rack01 bside n25 n40 n15
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 3
0 12 0 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack00 fside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 7 0 1
0 8 2 0
0 12 1 6
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack01 fside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 4 0
0 12 1 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack01 fside n18 n31 n13
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 2
0 12 1 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack01 fside n18 n40 n22
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 4
0 12 1 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack01 fside n25 n31 n06
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 1
0 12 1 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_1 rack01 fside n25 n40 n15
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 3
0 12 1 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack00 fside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 7 0 1
0 8 2 0
0 12 2 6
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack01 fside n18 n22 n04
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 4 0
0 12 2 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack01 fside n18 n31 n13
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 2
0 12 2 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack01 fside n18 n40 n22
1
0 0
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 4
0 12 2 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack01 fside n25 n31 n06
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 5 1
0 12 2 7
1
end_operator
begin_operator
put-down-rack jig0001 factory_trailer_2 rack01 fside n25 n40 n15
1
0 1
5
0 11 -1 0
0 15 -1 0
0 16 0 1
0 19 6 3
0 12 2 7
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack00 bside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 1 0
0 18 1 7
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack00 bside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 1
0 18 1 7
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack00 bside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 0
0 18 1 7
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 2 0
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n09 n15 n06
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 3 1
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 2
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n09 n31 n22
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 4
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n09 n40 n31
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 5
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 0
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n18 n31 n13
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 2
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 beluga_abs_trailer rack01 bside n18 n40 n22
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 4
0 18 1 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack00 fside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 1 0
0 18 2 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack00 fside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 1
0 18 2 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack00 fside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 0
0 18 2 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 2 0
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n09 n15 n06
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 3 1
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 2
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n09 n31 n22
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 4
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n09 n40 n31
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 5
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 0
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n18 n31 n13
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 2
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_1 rack01 fside n18 n40 n22
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 4
0 18 2 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack00 fside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 1 0
0 18 3 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack00 fside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 1
0 18 3 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack00 fside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 7 0 1
0 8 2 0
0 18 3 7
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n09 n13 n04
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 2 0
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n09 n15 n06
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 3 1
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n09 n22 n13
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 2
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n09 n31 n22
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 4
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n09 n40 n31
1
1 0
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 5
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n18 n22 n04
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 4 0
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n18 n31 n13
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 5 2
0 18 3 8
1
end_operator
begin_operator
put-down-rack jig0002 factory_trailer_2 rack01 fside n18 n40 n22
1
1 1
5
0 17 -1 0
0 20 -1 0
0 16 0 1
0 19 6 4
0 18 3 8
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack00 bside fside n18 n22 n04
2
18 7
0 0
6
0 11 -1 0
0 17 0 1
0 8 2 0
0 12 0 6
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n22 n04
2
18 8
0 0
6
0 11 -1 0
0 17 0 1
0 19 4 0
0 12 0 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n31 n13
2
18 8
0 0
6
0 11 -1 0
0 17 0 1
0 19 5 2
0 12 0 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n40 n22
2
18 8
0 0
6
0 11 -1 0
0 17 0 1
0 19 6 4
0 12 0 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n25 n31 n06
2
18 8
0 1
6
0 11 -1 0
0 17 0 1
0 19 5 1
0 12 0 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n25 n40 n15
2
18 8
0 1
6
0 11 -1 0
0 17 0 1
0 19 6 3
0 12 0 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack00 fside bside n18 n22 n04
2
18 7
0 0
6
0 15 -1 0
0 20 0 1
0 8 2 0
0 12 1 6
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n22 n04
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 4 0
0 12 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n31 n13
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 5 2
0 12 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n40 n22
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 6 4
0 12 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n31 n06
2
18 8
0 1
6
0 15 -1 0
0 20 0 1
0 19 5 1
0 12 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n40 n15
2
18 8
0 1
6
0 15 -1 0
0 20 0 1
0 19 6 3
0 12 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack00 fside bside n18 n22 n04
2
18 7
0 0
6
0 15 -1 0
0 20 0 1
0 8 2 0
0 12 2 6
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n22 n04
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 4 0
0 12 2 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n31 n13
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 5 2
0 12 2 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n40 n22
2
18 8
0 0
6
0 15 -1 0
0 20 0 1
0 19 6 4
0 12 2 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n31 n06
2
18 8
0 1
6
0 15 -1 0
0 20 0 1
0 19 5 1
0 12 2 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n40 n15
2
18 8
0 1
6
0 15 -1 0
0 20 0 1
0 19 6 3
0 12 2 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n09 n13 n04
2
12 6
1 0
6
0 11 0 1
0 17 -1 0
0 8 1 0
0 18 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n09 n22 n13
2
12 6
1 0
6
0 11 0 1
0 17 -1 0
0 8 2 1
0 18 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n18 n22 n04
2
12 6
1 1
6
0 11 0 1
0 17 -1 0
0 8 2 0
0 18 1 7
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n13 n04
2
12 7
1 0
6
0 11 0 1
0 17 -1 0
0 19 2 0
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n15 n06
2
12 7
1 0
6
0 11 0 1
0 17 -1 0
0 19 3 1
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n22 n13
2
12 7
1 0
6
0 11 0 1
0 17 -1 0
0 19 4 2
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n31 n22
2
12 7
1 0
6
0 11 0 1
0 17 -1 0
0 19 5 4
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n40 n31
2
12 7
1 0
6
0 11 0 1
0 17 -1 0
0 19 6 5
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n22 n04
2
12 7
1 1
6
0 11 0 1
0 17 -1 0
0 19 4 0
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n31 n13
2
12 7
1 1
6
0 11 0 1
0 17 -1 0
0 19 5 2
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n40 n22
2
12 7
1 1
6
0 11 0 1
0 17 -1 0
0 19 6 4
0 18 1 8
0 9 -1 0
0 10 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n13 n04
2
12 6
1 0
6
0 15 0 1
0 20 -1 0
0 8 1 0
0 18 2 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n22 n13
2
12 6
1 0
6
0 15 0 1
0 20 -1 0
0 8 2 1
0 18 2 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n18 n22 n04
2
12 6
1 1
6
0 15 0 1
0 20 -1 0
0 8 2 0
0 18 2 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n13 n04
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 2 0
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n15 n06
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 3 1
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n22 n13
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 4 2
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n31 n22
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 5 4
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n40 n31
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 6 5
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n22 n04
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 4 0
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n31 n13
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 5 2
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n40 n22
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 6 4
0 18 2 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n13 n04
2
12 6
1 0
6
0 15 0 1
0 20 -1 0
0 8 1 0
0 18 3 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n22 n13
2
12 6
1 0
6
0 15 0 1
0 20 -1 0
0 8 2 1
0 18 3 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n18 n22 n04
2
12 6
1 1
6
0 15 0 1
0 20 -1 0
0 8 2 0
0 18 3 7
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n13 n04
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 2 0
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n15 n06
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 3 1
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n22 n13
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 4 2
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n31 n22
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 5 4
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n40 n31
2
12 7
1 0
6
0 15 0 1
0 20 -1 0
0 19 6 5
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n22 n04
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 4 0
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n31 n13
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 5 2
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
stack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n40 n22
2
12 7
1 1
6
0 15 0 1
0 20 -1 0
0 19 6 4
0 18 3 8
0 13 -1 0
0 14 -1 0
1
end_operator
begin_operator
unload-beluga jig0002 dummy-jig beluga_abs_trailer beluga1
0
2
0 18 0 1
0 21 1 0
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack00 bside fside n18 n04 n22
3
11 0
18 7
0 0
5
0 17 -1 0
0 8 0 2
0 12 6 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n04 n22
3
11 0
18 8
0 0
5
0 17 -1 0
0 19 0 4
0 12 7 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n13 n31
3
11 0
18 8
0 0
5
0 17 -1 0
0 19 2 5
0 12 7 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n18 n22 n40
3
11 0
18 8
0 0
5
0 17 -1 0
0 19 4 6
0 12 7 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n25 n06 n31
3
11 0
18 8
0 1
5
0 17 -1 0
0 19 1 5
0 12 7 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 beluga_abs_trailer rack01 bside fside n25 n15 n40
3
11 0
18 8
0 1
5
0 17 -1 0
0 19 3 6
0 12 7 0
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack00 fside bside n18 n04 n22
3
15 0
18 7
0 0
5
0 20 -1 0
0 8 0 2
0 12 6 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n04 n22
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 0 4
0 12 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n13 n31
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 2 5
0 12 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n22 n40
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 4 6
0 12 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n06 n31
3
15 0
18 8
0 1
5
0 20 -1 0
0 19 1 5
0 12 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n15 n40
3
15 0
18 8
0 1
5
0 20 -1 0
0 19 3 6
0 12 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack00 fside bside n18 n04 n22
3
15 0
18 7
0 0
5
0 20 -1 0
0 8 0 2
0 12 6 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n04 n22
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 0 4
0 12 7 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n13 n31
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 2 5
0 12 7 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n22 n40
3
15 0
18 8
0 0
5
0 20 -1 0
0 19 4 6
0 12 7 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n06 n31
3
15 0
18 8
0 1
5
0 20 -1 0
0 19 1 5
0 12 7 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n15 n40
3
15 0
18 8
0 1
5
0 20 -1 0
0 19 3 6
0 12 7 2
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n09 n04 n13
3
17 0
12 6
1 0
5
0 11 -1 0
0 8 0 1
0 18 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n09 n13 n22
3
17 0
12 6
1 0
5
0 11 -1 0
0 8 1 2
0 18 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack00 bside fside n18 n04 n22
3
17 0
12 6
1 1
5
0 11 -1 0
0 8 0 2
0 18 7 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n04 n13
3
17 0
12 7
1 0
5
0 11 -1 0
0 19 0 2
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n06 n15
3
17 0
12 7
1 0
5
0 11 -1 0
0 19 1 3
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n13 n22
3
17 0
12 7
1 0
5
0 11 -1 0
0 19 2 4
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n22 n31
3
17 0
12 7
1 0
5
0 11 -1 0
0 19 4 5
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n09 n31 n40
3
17 0
12 7
1 0
5
0 11 -1 0
0 19 5 6
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n04 n22
3
17 0
12 7
1 1
5
0 11 -1 0
0 19 0 4
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n13 n31
3
17 0
12 7
1 1
5
0 11 -1 0
0 19 2 5
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 beluga_abs_trailer rack01 bside fside n18 n22 n40
3
17 0
12 7
1 1
5
0 11 -1 0
0 19 4 6
0 18 8 1
0 9 0 1
0 10 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n04 n13
3
20 0
12 6
1 0
5
0 15 -1 0
0 8 0 1
0 18 7 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n13 n22
3
20 0
12 6
1 0
5
0 15 -1 0
0 8 1 2
0 18 7 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n18 n04 n22
3
20 0
12 6
1 1
5
0 15 -1 0
0 8 0 2
0 18 7 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n04 n13
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 0 2
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n06 n15
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 1 3
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n13 n22
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 2 4
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n22 n31
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 4 5
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n31 n40
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 5 6
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n04 n22
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 0 4
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n13 n31
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 2 5
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n22 n40
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 4 6
0 18 8 2
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n04 n13
3
20 0
12 6
1 0
5
0 15 -1 0
0 8 0 1
0 18 7 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n13 n22
3
20 0
12 6
1 0
5
0 15 -1 0
0 8 1 2
0 18 7 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n18 n04 n22
3
20 0
12 6
1 1
5
0 15 -1 0
0 8 0 2
0 18 7 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n04 n13
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 0 2
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n06 n15
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 1 3
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n13 n22
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 2 4
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n22 n31
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 4 5
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n31 n40
3
20 0
12 7
1 0
5
0 15 -1 0
0 19 5 6
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n04 n22
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 0 4
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n13 n31
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 2 5
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
begin_operator
unstack-rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n22 n40
3
20 0
12 7
1 1
5
0 15 -1 0
0 19 4 6
0 18 8 3
0 13 0 1
0 14 0 1
1
end_operator
0
