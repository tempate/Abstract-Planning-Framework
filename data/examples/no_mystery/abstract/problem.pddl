(define (problem transport-l5-t1-p4---int100n150-m25---int100c150---s1---e0)
(:domain transport-strips)

(:objects
l0 l1 l2 l3 l4 - location
t0 - truck
p0 p1 p2 p3 - package
abslevel1 abslevel2 - fuellevel
)

(:init
(sum abslevel1 abslevel2 abslevel1)

(connected l0 l1)
(fuelcost abslevel2 l0 l1)
(connected l0 l2)
(fuelcost abslevel2 l0 l2)
(connected l0 l3)
(fuelcost abslevel2 l0 l3)
(connected l0 l4)
(fuelcost abslevel2 l0 l4)
(connected l1 l0)
(fuelcost abslevel2 l1 l0)
(connected l1 l2)
(fuelcost abslevel2 l1 l2)
(connected l2 l0)
(fuelcost abslevel2 l2 l0)
(connected l2 l1)
(fuelcost abslevel2 l2 l1)
(connected l2 l3)
(fuelcost abslevel2 l2 l3)
(connected l2 l4)
(fuelcost abslevel2 l2 l4)
(connected l3 l0)
(fuelcost abslevel2 l3 l0)
(connected l3 l2)
(fuelcost abslevel2 l3 l2)
(connected l4 l0)
(fuelcost abslevel2 l4 l0)
(connected l4 l2)
(fuelcost abslevel2 l4 l2)

(at t0 l3)
(fuel t0 abslevel1)
(= (total-cost) 0)

(at p0 l4)
(at p1 l3)
(at p2 l1)
(at p3 l4)
)

(:goal
(and
(at p0 l2)
(at p1 l1)
(at p2 l2)
(at p3 l3)
)
)
(:metric minimize (total-cost)))
