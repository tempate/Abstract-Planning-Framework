(define (problem ZTRAVEL-2-4)
(:domain zeno-travel)
(:objects
	plane1
	plane2
	person1
	person2 person2-copy1 person2-copy2 person2-copy3 person2-copy4 person2-copy5 person2-copy6 person2-copy7 person2-copy8 person2-copy9 person2-copy10 person2-copy11 person2-copy12 person2-copy13 person2-copy14 person2-copy15 person2-copy16 person2-copy17 person2-copy18
	person3
	person4
	city0
	city1
	city2
	city3
	fl0
	fl1
	fl2
	fl3
	fl4
	fl5
	fl6
	)
(:init
	(at plane1 city1)
	(aircraft plane1)
	(fuel-level plane1 fl6)
	(at plane2 city2)
	(aircraft plane2)
	(fuel-level plane2 fl0)
	(at person1 city3)
	(person person1)
	(at person2 city0) (at person2-copy1 city0) (at person2-copy2 city0) (at person2-copy3 city0) (at person2-copy4 city0) (at person2-copy5 city0) (at person2-copy6 city0) (at person2-copy7 city0) (at person2-copy8 city0) (at person2-copy9 city0) (at person2-copy10 city0) (at person2-copy11 city0) (at person2-copy12 city0) (at person2-copy13 city0) (at person2-copy14 city0) (at person2-copy15 city0) (at person2-copy16 city0) (at person2-copy17 city0) (at person2-copy18 city0)
	(person person2) (person person2-copy1) (person person2-copy2) (person person2-copy3) (person person2-copy4) (person person2-copy5) (person person2-copy6) (person person2-copy7) (person person2-copy8) (person person2-copy9) (person person2-copy10) (person person2-copy11) (person person2-copy12) (person person2-copy13) (person person2-copy14) (person person2-copy15) (person person2-copy16) (person person2-copy17) (person person2-copy18)
	(at person3 city0)
	(person person3)
	(at person4 city1)
	(person person4)
	(city city0)
	(city city1)
	(city city2)
	(city city3)
	(next fl0 fl1)
	(next fl1 fl2)
	(next fl2 fl3)
	(next fl3 fl4)
	(next fl4 fl5)
	(next fl5 fl6)
	(flevel fl0)
	(flevel fl1)
	(flevel fl2)
	(flevel fl3)
	(flevel fl4)
	(flevel fl5)
	(flevel fl6)
)
(:goal (and
	(at person1 city2)
	(at person2 city3) (at person2-copy1 city3) (at person2-copy2 city3) (at person2-copy3 city3) (at person2-copy4 city3) (at person2-copy5 city3) (at person2-copy6 city3) (at person2-copy7 city3) (at person2-copy8 city3) (at person2-copy9 city3) (at person2-copy10 city3) (at person2-copy11 city3) (at person2-copy12 city3) (at person2-copy13 city3) (at person2-copy14 city3) (at person2-copy15 city3) (at person2-copy16 city3) (at person2-copy17 city3) (at person2-copy18 city3)
	(at person3 city3)
	(at person4 city3)
	))

)
