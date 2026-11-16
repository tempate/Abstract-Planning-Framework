(define (problem ZTRAVEL-3-6)
(:domain zeno-travel)
(:objects
	plane1
	plane2
	plane3
	person1
	person2 person2-copy1 person2-copy2 person2-copy3 person2-copy4 person2-copy5 person2-copy6 person2-copy7 person2-copy8 person2-copy9 person2-copy10 person2-copy11 person2-copy12 person2-copy13 person2-copy14 person2-copy15 person2-copy16 person2-copy17 person2-copy18 person2-copy19 person2-copy20 person2-copy21 person2-copy22 person2-copy23 person2-copy24 person2-copy25 person2-copy26 person2-copy27 person2-copy28 person2-copy29 person2-copy30 person2-copy31 person2-copy32 person2-copy33 person2-copy34 person2-copy35 person2-copy36 person2-copy37 person2-copy38 person2-copy39 person2-copy40 person2-copy41 person2-copy42 person2-copy43 person2-copy44 person2-copy45 person2-copy46 person2-copy47 person2-copy48
	person3
	person4
	person5
	person6
	city0
	city1
	city2
	city3
	city4
	fl0
	fl1
	fl2
	fl3
	fl4
	fl5
	fl6
	)
(:init
	(at plane1 city0)
	(aircraft plane1)
	(fuel-level plane1 fl6)
	(at plane2 city3)
	(aircraft plane2)
	(fuel-level plane2 fl0)
	(at plane3 city0)
	(aircraft plane3)
	(fuel-level plane3 fl3)
	(at person1 city1)
	(person person1)
	(at person2 city0) (at person2-copy1 city0) (at person2-copy2 city0) (at person2-copy3 city0) (at person2-copy4 city0) (at person2-copy5 city0) (at person2-copy6 city0) (at person2-copy7 city0) (at person2-copy8 city0) (at person2-copy9 city0) (at person2-copy10 city0) (at person2-copy11 city0) (at person2-copy12 city0) (at person2-copy13 city0) (at person2-copy14 city0) (at person2-copy15 city0) (at person2-copy16 city0) (at person2-copy17 city0) (at person2-copy18 city0) (at person2-copy19 city0) (at person2-copy20 city0) (at person2-copy21 city0) (at person2-copy22 city0) (at person2-copy23 city0) (at person2-copy24 city0) (at person2-copy25 city0) (at person2-copy26 city0) (at person2-copy27 city0) (at person2-copy28 city0) (at person2-copy29 city0) (at person2-copy30 city0) (at person2-copy31 city0) (at person2-copy32 city0) (at person2-copy33 city0) (at person2-copy34 city0) (at person2-copy35 city0) (at person2-copy36 city0) (at person2-copy37 city0) (at person2-copy38 city0) (at person2-copy39 city0) (at person2-copy40 city0) (at person2-copy41 city0) (at person2-copy42 city0) (at person2-copy43 city0) (at person2-copy44 city0) (at person2-copy45 city0) (at person2-copy46 city0) (at person2-copy47 city0) (at person2-copy48 city0)
	(person person2) (person person2-copy1) (person person2-copy2) (person person2-copy3) (person person2-copy4) (person person2-copy5) (person person2-copy6) (person person2-copy7) (person person2-copy8) (person person2-copy9) (person person2-copy10) (person person2-copy11) (person person2-copy12) (person person2-copy13) (person person2-copy14) (person person2-copy15) (person person2-copy16) (person person2-copy17) (person person2-copy18) (person person2-copy19) (person person2-copy20) (person person2-copy21) (person person2-copy22) (person person2-copy23) (person person2-copy24) (person person2-copy25) (person person2-copy26) (person person2-copy27) (person person2-copy28) (person person2-copy29) (person person2-copy30) (person person2-copy31) (person person2-copy32) (person person2-copy33) (person person2-copy34) (person person2-copy35) (person person2-copy36) (person person2-copy37) (person person2-copy38) (person person2-copy39) (person person2-copy40) (person person2-copy41) (person person2-copy42) (person person2-copy43) (person person2-copy44) (person person2-copy45) (person person2-copy46) (person person2-copy47) (person person2-copy48)
	(at person3 city2)
	(person person3)
	(at person4 city0)
	(person person4)
	(at person5 city3)
	(person person5)
	(at person6 city4)
	(person person6)
	(city city0)
	(city city1)
	(city city2)
	(city city3)
	(city city4)
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
	(at plane1 city3)
	(at person1 city0)
	(at person2 city0) (at person2-copy1 city0) (at person2-copy2 city0) (at person2-copy3 city0) (at person2-copy4 city0) (at person2-copy5 city0) (at person2-copy6 city0) (at person2-copy7 city0) (at person2-copy8 city0) (at person2-copy9 city0) (at person2-copy10 city0) (at person2-copy11 city0) (at person2-copy12 city0) (at person2-copy13 city0) (at person2-copy14 city0) (at person2-copy15 city0) (at person2-copy16 city0) (at person2-copy17 city0) (at person2-copy18 city0) (at person2-copy19 city0) (at person2-copy20 city0) (at person2-copy21 city0) (at person2-copy22 city0) (at person2-copy23 city0) (at person2-copy24 city0) (at person2-copy25 city0) (at person2-copy26 city0) (at person2-copy27 city0) (at person2-copy28 city0) (at person2-copy29 city0) (at person2-copy30 city0) (at person2-copy31 city0) (at person2-copy32 city0) (at person2-copy33 city0) (at person2-copy34 city0) (at person2-copy35 city0) (at person2-copy36 city0) (at person2-copy37 city0) (at person2-copy38 city0) (at person2-copy39 city0) (at person2-copy40 city0) (at person2-copy41 city0) (at person2-copy42 city0) (at person2-copy43 city0) (at person2-copy44 city0) (at person2-copy45 city0) (at person2-copy46 city0) (at person2-copy47 city0) (at person2-copy48 city0)
	(at person3 city1)
	(at person4 city0)
	(at person5 city3)
	(at person6 city2)
	))

)
