; Transport two-cities-sequential-2nodes-1000size-2degree-100mindistance-2trucks-2packages-2008seed

(define (problem transport-two-cities-sequential-2nodes-1000size-2degree-100mindistance-2trucks-2packages-2008seed)
 (:domain transport)
 (:objects
  city-1-loc-1 - location
  city-2-loc-1 - location
  city-1-loc-2 - location
  city-2-loc-2 - location
  truck-1 truck-1-copy1 truck-1-copy2 truck-1-copy3 truck-1-copy4 truck-1-copy5 truck-1-copy6 truck-1-copy7 truck-1-copy8 truck-1-copy9 truck-1-copy10 truck-1-copy11 truck-1-copy12 truck-1-copy13 truck-1-copy14 truck-1-copy15 truck-1-copy16 truck-1-copy17 truck-1-copy18 - vehicle
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
  (at truck-1 city-2-loc-2) (at truck-1-copy1 city-2-loc-2) (at truck-1-copy2 city-2-loc-2) (at truck-1-copy3 city-2-loc-2) (at truck-1-copy4 city-2-loc-2) (at truck-1-copy5 city-2-loc-2) (at truck-1-copy6 city-2-loc-2) (at truck-1-copy7 city-2-loc-2) (at truck-1-copy8 city-2-loc-2) (at truck-1-copy9 city-2-loc-2) (at truck-1-copy10 city-2-loc-2) (at truck-1-copy11 city-2-loc-2) (at truck-1-copy12 city-2-loc-2) (at truck-1-copy13 city-2-loc-2) (at truck-1-copy14 city-2-loc-2) (at truck-1-copy15 city-2-loc-2) (at truck-1-copy16 city-2-loc-2) (at truck-1-copy17 city-2-loc-2) (at truck-1-copy18 city-2-loc-2)
  (capacity truck-1 capacity-3) (capacity truck-1-copy1 capacity-3) (capacity truck-1-copy2 capacity-3) (capacity truck-1-copy3 capacity-3) (capacity truck-1-copy4 capacity-3) (capacity truck-1-copy5 capacity-3) (capacity truck-1-copy6 capacity-3) (capacity truck-1-copy7 capacity-3) (capacity truck-1-copy8 capacity-3) (capacity truck-1-copy9 capacity-3) (capacity truck-1-copy10 capacity-3) (capacity truck-1-copy11 capacity-3) (capacity truck-1-copy12 capacity-3) (capacity truck-1-copy13 capacity-3) (capacity truck-1-copy14 capacity-3) (capacity truck-1-copy15 capacity-3) (capacity truck-1-copy16 capacity-3) (capacity truck-1-copy17 capacity-3) (capacity truck-1-copy18 capacity-3)
  (at truck-2 city-2-loc-2)
  (capacity truck-2 capacity-3)
 )
 (:goal (and
  (at package-1 city-2-loc-1)
  (at package-2 city-2-loc-2)
 ))
 (:metric minimize (total-cost))
)
