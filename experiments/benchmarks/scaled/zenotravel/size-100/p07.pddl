(define (problem ZTRAVEL-2-6)
(:domain zeno-travel)
(:objects
	plane1
	plane2
	person1 person1-copy1 person1-copy2 person1-copy3 person1-copy4 person1-copy5 person1-copy6 person1-copy7 person1-copy8 person1-copy9 person1-copy10 person1-copy11 person1-copy12 person1-copy13 person1-copy14 person1-copy15 person1-copy16 person1-copy17 person1-copy18 person1-copy19 person1-copy20 person1-copy21 person1-copy22 person1-copy23 person1-copy24 person1-copy25 person1-copy26 person1-copy27 person1-copy28 person1-copy29 person1-copy30 person1-copy31 person1-copy32 person1-copy33 person1-copy34 person1-copy35 person1-copy36 person1-copy37 person1-copy38 person1-copy39 person1-copy40 person1-copy41 person1-copy42 person1-copy43 person1-copy44 person1-copy45 person1-copy46 person1-copy47 person1-copy48 person1-copy49 person1-copy50 person1-copy51 person1-copy52 person1-copy53 person1-copy54 person1-copy55 person1-copy56 person1-copy57 person1-copy58 person1-copy59 person1-copy60 person1-copy61 person1-copy62 person1-copy63 person1-copy64 person1-copy65 person1-copy66 person1-copy67 person1-copy68 person1-copy69 person1-copy70 person1-copy71 person1-copy72 person1-copy73 person1-copy74 person1-copy75 person1-copy76 person1-copy77 person1-copy78 person1-copy79 person1-copy80 person1-copy81 person1-copy82 person1-copy83 person1-copy84 person1-copy85 person1-copy86 person1-copy87 person1-copy88 person1-copy89 person1-copy90 person1-copy91 person1-copy92 person1-copy93 person1-copy94 person1-copy95 person1-copy96 person1-copy97 person1-copy98
	person2
	person3
	person4
	person5
	person6
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
	(at plane1 city2)
	(aircraft plane1)
	(fuel-level plane1 fl1)
	(at plane2 city1)
	(aircraft plane2)
	(fuel-level plane2 fl1)
	(at person1 city3) (at person1-copy1 city3) (at person1-copy2 city3) (at person1-copy3 city3) (at person1-copy4 city3) (at person1-copy5 city3) (at person1-copy6 city3) (at person1-copy7 city3) (at person1-copy8 city3) (at person1-copy9 city3) (at person1-copy10 city3) (at person1-copy11 city3) (at person1-copy12 city3) (at person1-copy13 city3) (at person1-copy14 city3) (at person1-copy15 city3) (at person1-copy16 city3) (at person1-copy17 city3) (at person1-copy18 city3) (at person1-copy19 city3) (at person1-copy20 city3) (at person1-copy21 city3) (at person1-copy22 city3) (at person1-copy23 city3) (at person1-copy24 city3) (at person1-copy25 city3) (at person1-copy26 city3) (at person1-copy27 city3) (at person1-copy28 city3) (at person1-copy29 city3) (at person1-copy30 city3) (at person1-copy31 city3) (at person1-copy32 city3) (at person1-copy33 city3) (at person1-copy34 city3) (at person1-copy35 city3) (at person1-copy36 city3) (at person1-copy37 city3) (at person1-copy38 city3) (at person1-copy39 city3) (at person1-copy40 city3) (at person1-copy41 city3) (at person1-copy42 city3) (at person1-copy43 city3) (at person1-copy44 city3) (at person1-copy45 city3) (at person1-copy46 city3) (at person1-copy47 city3) (at person1-copy48 city3) (at person1-copy49 city3) (at person1-copy50 city3) (at person1-copy51 city3) (at person1-copy52 city3) (at person1-copy53 city3) (at person1-copy54 city3) (at person1-copy55 city3) (at person1-copy56 city3) (at person1-copy57 city3) (at person1-copy58 city3) (at person1-copy59 city3) (at person1-copy60 city3) (at person1-copy61 city3) (at person1-copy62 city3) (at person1-copy63 city3) (at person1-copy64 city3) (at person1-copy65 city3) (at person1-copy66 city3) (at person1-copy67 city3) (at person1-copy68 city3) (at person1-copy69 city3) (at person1-copy70 city3) (at person1-copy71 city3) (at person1-copy72 city3) (at person1-copy73 city3) (at person1-copy74 city3) (at person1-copy75 city3) (at person1-copy76 city3) (at person1-copy77 city3) (at person1-copy78 city3) (at person1-copy79 city3) (at person1-copy80 city3) (at person1-copy81 city3) (at person1-copy82 city3) (at person1-copy83 city3) (at person1-copy84 city3) (at person1-copy85 city3) (at person1-copy86 city3) (at person1-copy87 city3) (at person1-copy88 city3) (at person1-copy89 city3) (at person1-copy90 city3) (at person1-copy91 city3) (at person1-copy92 city3) (at person1-copy93 city3) (at person1-copy94 city3) (at person1-copy95 city3) (at person1-copy96 city3) (at person1-copy97 city3) (at person1-copy98 city3)
	(person person1) (person person1-copy1) (person person1-copy2) (person person1-copy3) (person person1-copy4) (person person1-copy5) (person person1-copy6) (person person1-copy7) (person person1-copy8) (person person1-copy9) (person person1-copy10) (person person1-copy11) (person person1-copy12) (person person1-copy13) (person person1-copy14) (person person1-copy15) (person person1-copy16) (person person1-copy17) (person person1-copy18) (person person1-copy19) (person person1-copy20) (person person1-copy21) (person person1-copy22) (person person1-copy23) (person person1-copy24) (person person1-copy25) (person person1-copy26) (person person1-copy27) (person person1-copy28) (person person1-copy29) (person person1-copy30) (person person1-copy31) (person person1-copy32) (person person1-copy33) (person person1-copy34) (person person1-copy35) (person person1-copy36) (person person1-copy37) (person person1-copy38) (person person1-copy39) (person person1-copy40) (person person1-copy41) (person person1-copy42) (person person1-copy43) (person person1-copy44) (person person1-copy45) (person person1-copy46) (person person1-copy47) (person person1-copy48) (person person1-copy49) (person person1-copy50) (person person1-copy51) (person person1-copy52) (person person1-copy53) (person person1-copy54) (person person1-copy55) (person person1-copy56) (person person1-copy57) (person person1-copy58) (person person1-copy59) (person person1-copy60) (person person1-copy61) (person person1-copy62) (person person1-copy63) (person person1-copy64) (person person1-copy65) (person person1-copy66) (person person1-copy67) (person person1-copy68) (person person1-copy69) (person person1-copy70) (person person1-copy71) (person person1-copy72) (person person1-copy73) (person person1-copy74) (person person1-copy75) (person person1-copy76) (person person1-copy77) (person person1-copy78) (person person1-copy79) (person person1-copy80) (person person1-copy81) (person person1-copy82) (person person1-copy83) (person person1-copy84) (person person1-copy85) (person person1-copy86) (person person1-copy87) (person person1-copy88) (person person1-copy89) (person person1-copy90) (person person1-copy91) (person person1-copy92) (person person1-copy93) (person person1-copy94) (person person1-copy95) (person person1-copy96) (person person1-copy97) (person person1-copy98)
	(at person2 city3)
	(person person2)
	(at person3 city3)
	(person person3)
	(at person4 city1)
	(person person4)
	(at person5 city3)
	(person person5)
	(at person6 city0)
	(person person6)
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
	(at plane2 city1)
	(at person1 city2) (at person1-copy1 city2) (at person1-copy2 city2) (at person1-copy3 city2) (at person1-copy4 city2) (at person1-copy5 city2) (at person1-copy6 city2) (at person1-copy7 city2) (at person1-copy8 city2) (at person1-copy9 city2) (at person1-copy10 city2) (at person1-copy11 city2) (at person1-copy12 city2) (at person1-copy13 city2) (at person1-copy14 city2) (at person1-copy15 city2) (at person1-copy16 city2) (at person1-copy17 city2) (at person1-copy18 city2) (at person1-copy19 city2) (at person1-copy20 city2) (at person1-copy21 city2) (at person1-copy22 city2) (at person1-copy23 city2) (at person1-copy24 city2) (at person1-copy25 city2) (at person1-copy26 city2) (at person1-copy27 city2) (at person1-copy28 city2) (at person1-copy29 city2) (at person1-copy30 city2) (at person1-copy31 city2) (at person1-copy32 city2) (at person1-copy33 city2) (at person1-copy34 city2) (at person1-copy35 city2) (at person1-copy36 city2) (at person1-copy37 city2) (at person1-copy38 city2) (at person1-copy39 city2) (at person1-copy40 city2) (at person1-copy41 city2) (at person1-copy42 city2) (at person1-copy43 city2) (at person1-copy44 city2) (at person1-copy45 city2) (at person1-copy46 city2) (at person1-copy47 city2) (at person1-copy48 city2) (at person1-copy49 city2) (at person1-copy50 city2) (at person1-copy51 city2) (at person1-copy52 city2) (at person1-copy53 city2) (at person1-copy54 city2) (at person1-copy55 city2) (at person1-copy56 city2) (at person1-copy57 city2) (at person1-copy58 city2) (at person1-copy59 city2) (at person1-copy60 city2) (at person1-copy61 city2) (at person1-copy62 city2) (at person1-copy63 city2) (at person1-copy64 city2) (at person1-copy65 city2) (at person1-copy66 city2) (at person1-copy67 city2) (at person1-copy68 city2) (at person1-copy69 city2) (at person1-copy70 city2) (at person1-copy71 city2) (at person1-copy72 city2) (at person1-copy73 city2) (at person1-copy74 city2) (at person1-copy75 city2) (at person1-copy76 city2) (at person1-copy77 city2) (at person1-copy78 city2) (at person1-copy79 city2) (at person1-copy80 city2) (at person1-copy81 city2) (at person1-copy82 city2) (at person1-copy83 city2) (at person1-copy84 city2) (at person1-copy85 city2) (at person1-copy86 city2) (at person1-copy87 city2) (at person1-copy88 city2) (at person1-copy89 city2) (at person1-copy90 city2) (at person1-copy91 city2) (at person1-copy92 city2) (at person1-copy93 city2) (at person1-copy94 city2) (at person1-copy95 city2) (at person1-copy96 city2) (at person1-copy97 city2) (at person1-copy98 city2)
	(at person3 city3)
	(at person4 city3)
	(at person5 city2)
	(at person6 city2)
	))

)
