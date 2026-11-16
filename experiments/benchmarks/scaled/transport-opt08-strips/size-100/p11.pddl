; Transport two-cities-sequential-2nodes-1000size-2degree-100mindistance-2trucks-2packages-2008seed

(define (problem transport-two-cities-sequential-2nodes-1000size-2degree-100mindistance-2trucks-2packages-2008seed)
 (:domain transport)
 (:objects
  city-1-loc-1 - location
  city-2-loc-1 - location
  city-1-loc-2 - location
  city-2-loc-2 - location
  truck-1 truck-1-copy1 truck-1-copy2 truck-1-copy3 truck-1-copy4 truck-1-copy5 truck-1-copy6 truck-1-copy7 truck-1-copy8 truck-1-copy9 truck-1-copy10 truck-1-copy11 truck-1-copy12 truck-1-copy13 truck-1-copy14 truck-1-copy15 truck-1-copy16 truck-1-copy17 truck-1-copy18 truck-1-copy19 truck-1-copy20 truck-1-copy21 truck-1-copy22 truck-1-copy23 truck-1-copy24 truck-1-copy25 truck-1-copy26 truck-1-copy27 truck-1-copy28 truck-1-copy29 truck-1-copy30 truck-1-copy31 truck-1-copy32 truck-1-copy33 truck-1-copy34 truck-1-copy35 truck-1-copy36 truck-1-copy37 truck-1-copy38 truck-1-copy39 truck-1-copy40 truck-1-copy41 truck-1-copy42 truck-1-copy43 truck-1-copy44 truck-1-copy45 truck-1-copy46 truck-1-copy47 truck-1-copy48 truck-1-copy49 truck-1-copy50 truck-1-copy51 truck-1-copy52 truck-1-copy53 truck-1-copy54 truck-1-copy55 truck-1-copy56 truck-1-copy57 truck-1-copy58 truck-1-copy59 truck-1-copy60 truck-1-copy61 truck-1-copy62 truck-1-copy63 truck-1-copy64 truck-1-copy65 truck-1-copy66 truck-1-copy67 truck-1-copy68 truck-1-copy69 truck-1-copy70 truck-1-copy71 truck-1-copy72 truck-1-copy73 truck-1-copy74 truck-1-copy75 truck-1-copy76 truck-1-copy77 truck-1-copy78 truck-1-copy79 truck-1-copy80 truck-1-copy81 truck-1-copy82 truck-1-copy83 truck-1-copy84 truck-1-copy85 truck-1-copy86 truck-1-copy87 truck-1-copy88 truck-1-copy89 truck-1-copy90 truck-1-copy91 truck-1-copy92 truck-1-copy93 truck-1-copy94 truck-1-copy95 truck-1-copy96 truck-1-copy97 truck-1-copy98 - vehicle
  truck-2 - vehicle
  package-1 - package
  package-2 - package
  capacity-0 - capacity-number
  capacity-1 - capacity-number
  capacity-2 - capacity-number
  capacity-3 - capacity-number
  capacity-4 - capacity-number
 )
 (:init
  (= (total-cost) 0)
  (capacity-predecessor capacity-0 capacity-1)
  (capacity-predecessor capacity-1 capacity-2)
  (capacity-predecessor capacity-2 capacity-3)
  (capacity-predecessor capacity-3 capacity-4)
  ; 912,799 -> 748,385
  (road city-1-loc-2 city-1-loc-1)
  (= (road-length city-1-loc-2 city-1-loc-1) 45)
  ; 748,385 -> 912,799
  (road city-1-loc-1 city-1-loc-2)
  (= (road-length city-1-loc-1 city-1-loc-2) 45)
  ; 2564,783 -> 2742,542
  (road city-2-loc-2 city-2-loc-1)
  (= (road-length city-2-loc-2 city-2-loc-1) 30)
  ; 2742,542 -> 2564,783
  (road city-2-loc-1 city-2-loc-2)
  (= (road-length city-2-loc-1 city-2-loc-2) 30)
  ; 912,799 <-> 2564,783
  (road city-1-loc-2 city-2-loc-2)
  (= (road-length city-1-loc-2 city-2-loc-2) 166)
  (road city-2-loc-2 city-1-loc-2)
  (= (road-length city-2-loc-2 city-1-loc-2) 166)
  (at package-1 city-1-loc-1)
  (at package-2 city-1-loc-1)
  (at truck-1 city-2-loc-2) (at truck-1-copy1 city-2-loc-2) (at truck-1-copy2 city-2-loc-2) (at truck-1-copy3 city-2-loc-2) (at truck-1-copy4 city-2-loc-2) (at truck-1-copy5 city-2-loc-2) (at truck-1-copy6 city-2-loc-2) (at truck-1-copy7 city-2-loc-2) (at truck-1-copy8 city-2-loc-2) (at truck-1-copy9 city-2-loc-2) (at truck-1-copy10 city-2-loc-2) (at truck-1-copy11 city-2-loc-2) (at truck-1-copy12 city-2-loc-2) (at truck-1-copy13 city-2-loc-2) (at truck-1-copy14 city-2-loc-2) (at truck-1-copy15 city-2-loc-2) (at truck-1-copy16 city-2-loc-2) (at truck-1-copy17 city-2-loc-2) (at truck-1-copy18 city-2-loc-2) (at truck-1-copy19 city-2-loc-2) (at truck-1-copy20 city-2-loc-2) (at truck-1-copy21 city-2-loc-2) (at truck-1-copy22 city-2-loc-2) (at truck-1-copy23 city-2-loc-2) (at truck-1-copy24 city-2-loc-2) (at truck-1-copy25 city-2-loc-2) (at truck-1-copy26 city-2-loc-2) (at truck-1-copy27 city-2-loc-2) (at truck-1-copy28 city-2-loc-2) (at truck-1-copy29 city-2-loc-2) (at truck-1-copy30 city-2-loc-2) (at truck-1-copy31 city-2-loc-2) (at truck-1-copy32 city-2-loc-2) (at truck-1-copy33 city-2-loc-2) (at truck-1-copy34 city-2-loc-2) (at truck-1-copy35 city-2-loc-2) (at truck-1-copy36 city-2-loc-2) (at truck-1-copy37 city-2-loc-2) (at truck-1-copy38 city-2-loc-2) (at truck-1-copy39 city-2-loc-2) (at truck-1-copy40 city-2-loc-2) (at truck-1-copy41 city-2-loc-2) (at truck-1-copy42 city-2-loc-2) (at truck-1-copy43 city-2-loc-2) (at truck-1-copy44 city-2-loc-2) (at truck-1-copy45 city-2-loc-2) (at truck-1-copy46 city-2-loc-2) (at truck-1-copy47 city-2-loc-2) (at truck-1-copy48 city-2-loc-2) (at truck-1-copy49 city-2-loc-2) (at truck-1-copy50 city-2-loc-2) (at truck-1-copy51 city-2-loc-2) (at truck-1-copy52 city-2-loc-2) (at truck-1-copy53 city-2-loc-2) (at truck-1-copy54 city-2-loc-2) (at truck-1-copy55 city-2-loc-2) (at truck-1-copy56 city-2-loc-2) (at truck-1-copy57 city-2-loc-2) (at truck-1-copy58 city-2-loc-2) (at truck-1-copy59 city-2-loc-2) (at truck-1-copy60 city-2-loc-2) (at truck-1-copy61 city-2-loc-2) (at truck-1-copy62 city-2-loc-2) (at truck-1-copy63 city-2-loc-2) (at truck-1-copy64 city-2-loc-2) (at truck-1-copy65 city-2-loc-2) (at truck-1-copy66 city-2-loc-2) (at truck-1-copy67 city-2-loc-2) (at truck-1-copy68 city-2-loc-2) (at truck-1-copy69 city-2-loc-2) (at truck-1-copy70 city-2-loc-2) (at truck-1-copy71 city-2-loc-2) (at truck-1-copy72 city-2-loc-2) (at truck-1-copy73 city-2-loc-2) (at truck-1-copy74 city-2-loc-2) (at truck-1-copy75 city-2-loc-2) (at truck-1-copy76 city-2-loc-2) (at truck-1-copy77 city-2-loc-2) (at truck-1-copy78 city-2-loc-2) (at truck-1-copy79 city-2-loc-2) (at truck-1-copy80 city-2-loc-2) (at truck-1-copy81 city-2-loc-2) (at truck-1-copy82 city-2-loc-2) (at truck-1-copy83 city-2-loc-2) (at truck-1-copy84 city-2-loc-2) (at truck-1-copy85 city-2-loc-2) (at truck-1-copy86 city-2-loc-2) (at truck-1-copy87 city-2-loc-2) (at truck-1-copy88 city-2-loc-2) (at truck-1-copy89 city-2-loc-2) (at truck-1-copy90 city-2-loc-2) (at truck-1-copy91 city-2-loc-2) (at truck-1-copy92 city-2-loc-2) (at truck-1-copy93 city-2-loc-2) (at truck-1-copy94 city-2-loc-2) (at truck-1-copy95 city-2-loc-2) (at truck-1-copy96 city-2-loc-2) (at truck-1-copy97 city-2-loc-2) (at truck-1-copy98 city-2-loc-2)
  (capacity truck-1 capacity-3) (capacity truck-1-copy1 capacity-3) (capacity truck-1-copy2 capacity-3) (capacity truck-1-copy3 capacity-3) (capacity truck-1-copy4 capacity-3) (capacity truck-1-copy5 capacity-3) (capacity truck-1-copy6 capacity-3) (capacity truck-1-copy7 capacity-3) (capacity truck-1-copy8 capacity-3) (capacity truck-1-copy9 capacity-3) (capacity truck-1-copy10 capacity-3) (capacity truck-1-copy11 capacity-3) (capacity truck-1-copy12 capacity-3) (capacity truck-1-copy13 capacity-3) (capacity truck-1-copy14 capacity-3) (capacity truck-1-copy15 capacity-3) (capacity truck-1-copy16 capacity-3) (capacity truck-1-copy17 capacity-3) (capacity truck-1-copy18 capacity-3) (capacity truck-1-copy19 capacity-3) (capacity truck-1-copy20 capacity-3) (capacity truck-1-copy21 capacity-3) (capacity truck-1-copy22 capacity-3) (capacity truck-1-copy23 capacity-3) (capacity truck-1-copy24 capacity-3) (capacity truck-1-copy25 capacity-3) (capacity truck-1-copy26 capacity-3) (capacity truck-1-copy27 capacity-3) (capacity truck-1-copy28 capacity-3) (capacity truck-1-copy29 capacity-3) (capacity truck-1-copy30 capacity-3) (capacity truck-1-copy31 capacity-3) (capacity truck-1-copy32 capacity-3) (capacity truck-1-copy33 capacity-3) (capacity truck-1-copy34 capacity-3) (capacity truck-1-copy35 capacity-3) (capacity truck-1-copy36 capacity-3) (capacity truck-1-copy37 capacity-3) (capacity truck-1-copy38 capacity-3) (capacity truck-1-copy39 capacity-3) (capacity truck-1-copy40 capacity-3) (capacity truck-1-copy41 capacity-3) (capacity truck-1-copy42 capacity-3) (capacity truck-1-copy43 capacity-3) (capacity truck-1-copy44 capacity-3) (capacity truck-1-copy45 capacity-3) (capacity truck-1-copy46 capacity-3) (capacity truck-1-copy47 capacity-3) (capacity truck-1-copy48 capacity-3) (capacity truck-1-copy49 capacity-3) (capacity truck-1-copy50 capacity-3) (capacity truck-1-copy51 capacity-3) (capacity truck-1-copy52 capacity-3) (capacity truck-1-copy53 capacity-3) (capacity truck-1-copy54 capacity-3) (capacity truck-1-copy55 capacity-3) (capacity truck-1-copy56 capacity-3) (capacity truck-1-copy57 capacity-3) (capacity truck-1-copy58 capacity-3) (capacity truck-1-copy59 capacity-3) (capacity truck-1-copy60 capacity-3) (capacity truck-1-copy61 capacity-3) (capacity truck-1-copy62 capacity-3) (capacity truck-1-copy63 capacity-3) (capacity truck-1-copy64 capacity-3) (capacity truck-1-copy65 capacity-3) (capacity truck-1-copy66 capacity-3) (capacity truck-1-copy67 capacity-3) (capacity truck-1-copy68 capacity-3) (capacity truck-1-copy69 capacity-3) (capacity truck-1-copy70 capacity-3) (capacity truck-1-copy71 capacity-3) (capacity truck-1-copy72 capacity-3) (capacity truck-1-copy73 capacity-3) (capacity truck-1-copy74 capacity-3) (capacity truck-1-copy75 capacity-3) (capacity truck-1-copy76 capacity-3) (capacity truck-1-copy77 capacity-3) (capacity truck-1-copy78 capacity-3) (capacity truck-1-copy79 capacity-3) (capacity truck-1-copy80 capacity-3) (capacity truck-1-copy81 capacity-3) (capacity truck-1-copy82 capacity-3) (capacity truck-1-copy83 capacity-3) (capacity truck-1-copy84 capacity-3) (capacity truck-1-copy85 capacity-3) (capacity truck-1-copy86 capacity-3) (capacity truck-1-copy87 capacity-3) (capacity truck-1-copy88 capacity-3) (capacity truck-1-copy89 capacity-3) (capacity truck-1-copy90 capacity-3) (capacity truck-1-copy91 capacity-3) (capacity truck-1-copy92 capacity-3) (capacity truck-1-copy93 capacity-3) (capacity truck-1-copy94 capacity-3) (capacity truck-1-copy95 capacity-3) (capacity truck-1-copy96 capacity-3) (capacity truck-1-copy97 capacity-3) (capacity truck-1-copy98 capacity-3)
  (at truck-2 city-2-loc-2)
  (capacity truck-2 capacity-3)
 )
 (:goal (and
  (at package-1 city-2-loc-1)
  (at package-2 city-2-loc-2)
 ))
 (:metric minimize (total-cost))
)
