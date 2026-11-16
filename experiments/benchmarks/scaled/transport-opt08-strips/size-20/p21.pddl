; Transport three-cities-sequential-1nodes-1000size-0degree-100mindistance-2trucks-2packages-2008seed

(define (problem transport-three-cities-sequential-1nodes-1000size-0degree-100mindistance-2trucks-2packages-2008seed)
 (:domain transport)
 (:objects
  city-1-loc-1 - location
  city-2-loc-1 - location
  city-3-loc-1 - location
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
  ; 890,543 <-> 2384,50
  (road city-1-loc-1 city-2-loc-1)
  (= (road-length city-1-loc-1 city-2-loc-1) 158)
  (road city-2-loc-1 city-1-loc-1)
  (= (road-length city-2-loc-1 city-1-loc-1) 158)
  (road city-1-loc-1 city-3-loc-1)
  (= (road-length city-1-loc-1 city-3-loc-1) 158)
  (road city-3-loc-1 city-1-loc-1)
  (= (road-length city-3-loc-1 city-1-loc-1) 158)
  (road city-2-loc-1 city-3-loc-1)
  (= (road-length city-2-loc-1 city-3-loc-1) 158)
  (road city-3-loc-1 city-2-loc-1)
  (= (road-length city-3-loc-1 city-2-loc-1) 158)
  (at package-1 city-3-loc-1)
  (at package-2 city-3-loc-1)
  (at truck-1 city-2-loc-1) (at truck-1-copy1 city-2-loc-1) (at truck-1-copy2 city-2-loc-1) (at truck-1-copy3 city-2-loc-1) (at truck-1-copy4 city-2-loc-1) (at truck-1-copy5 city-2-loc-1) (at truck-1-copy6 city-2-loc-1) (at truck-1-copy7 city-2-loc-1) (at truck-1-copy8 city-2-loc-1) (at truck-1-copy9 city-2-loc-1) (at truck-1-copy10 city-2-loc-1) (at truck-1-copy11 city-2-loc-1) (at truck-1-copy12 city-2-loc-1) (at truck-1-copy13 city-2-loc-1) (at truck-1-copy14 city-2-loc-1) (at truck-1-copy15 city-2-loc-1) (at truck-1-copy16 city-2-loc-1) (at truck-1-copy17 city-2-loc-1) (at truck-1-copy18 city-2-loc-1)
  (capacity truck-1 capacity-4) (capacity truck-1-copy1 capacity-4) (capacity truck-1-copy2 capacity-4) (capacity truck-1-copy3 capacity-4) (capacity truck-1-copy4 capacity-4) (capacity truck-1-copy5 capacity-4) (capacity truck-1-copy6 capacity-4) (capacity truck-1-copy7 capacity-4) (capacity truck-1-copy8 capacity-4) (capacity truck-1-copy9 capacity-4) (capacity truck-1-copy10 capacity-4) (capacity truck-1-copy11 capacity-4) (capacity truck-1-copy12 capacity-4) (capacity truck-1-copy13 capacity-4) (capacity truck-1-copy14 capacity-4) (capacity truck-1-copy15 capacity-4) (capacity truck-1-copy16 capacity-4) (capacity truck-1-copy17 capacity-4) (capacity truck-1-copy18 capacity-4)
  (at truck-2 city-2-loc-1)
  (capacity truck-2 capacity-4)
 )
 (:goal (and
  (at package-1 city-1-loc-1)
  (at package-2 city-2-loc-1)
 ))
 (:metric minimize (total-cost))
)
