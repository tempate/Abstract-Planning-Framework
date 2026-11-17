; Transport city-sequential-5nodes-1000size-2degree-100mindistance-2trucks-4packages-2014seed

(define (problem transport-city-sequential-5nodes-1000size-2degree-100mindistance-2trucks-4packages-2014seed)
 (:domain transport)
 (:objects
  city-loc-1 - location
  city-loc-2 - location
  city-loc-3 - location
  city-loc-4 - location
  city-loc-5 - location
  truck-1 - vehicle
  truck-2 - vehicle
  package-1 package-1-copy1 package-1-copy2 package-1-copy3 package-1-copy4 package-1-copy5 package-1-copy6 package-1-copy7 package-1-copy8 package-1-copy9 package-1-copy10 package-1-copy11 package-1-copy12 package-1-copy13 package-1-copy14 package-1-copy15 package-1-copy16 package-1-copy17 package-1-copy18 package-1-copy19 package-1-copy20 package-1-copy21 package-1-copy22 package-1-copy23 package-1-copy24 package-1-copy25 package-1-copy26 package-1-copy27 package-1-copy28 package-1-copy29 package-1-copy30 package-1-copy31 package-1-copy32 package-1-copy33 package-1-copy34 package-1-copy35 package-1-copy36 package-1-copy37 package-1-copy38 package-1-copy39 package-1-copy40 package-1-copy41 package-1-copy42 package-1-copy43 package-1-copy44 package-1-copy45 package-1-copy46 package-1-copy47 package-1-copy48 - package
  package-2 - package
  package-3 - package
  package-4 - package
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
  ; 688,479 -> 680,79
  (road city-loc-3 city-loc-1)
  (= (road-length city-loc-3 city-loc-1) 40)
  ; 680,79 -> 688,479
  (road city-loc-1 city-loc-3)
  (= (road-length city-loc-1 city-loc-3) 40)
  ; 688,479 -> 753,644
  (road city-loc-3 city-loc-2)
  (= (road-length city-loc-3 city-loc-2) 18)
  ; 753,644 -> 688,479
  (road city-loc-2 city-loc-3)
  (= (road-length city-loc-2 city-loc-3) 18)
  ; 383,275 -> 680,79
  (road city-loc-4 city-loc-1)
  (= (road-length city-loc-4 city-loc-1) 36)
  ; 680,79 -> 383,275
  (road city-loc-1 city-loc-4)
  (= (road-length city-loc-1 city-loc-4) 36)
  ; 383,275 -> 688,479
  (road city-loc-4 city-loc-3)
  (= (road-length city-loc-4 city-loc-3) 37)
  ; 688,479 -> 383,275
  (road city-loc-3 city-loc-4)
  (= (road-length city-loc-3 city-loc-4) 37)
  ; 945,511 -> 753,644
  (road city-loc-5 city-loc-2)
  (= (road-length city-loc-5 city-loc-2) 24)
  ; 753,644 -> 945,511
  (road city-loc-2 city-loc-5)
  (= (road-length city-loc-2 city-loc-5) 24)
  ; 945,511 -> 688,479
  (road city-loc-5 city-loc-3)
  (= (road-length city-loc-5 city-loc-3) 26)
  ; 688,479 -> 945,511
  (road city-loc-3 city-loc-5)
  (= (road-length city-loc-3 city-loc-5) 26)
  (at package-1 city-loc-1) (at package-1-copy1 city-loc-1) (at package-1-copy2 city-loc-1) (at package-1-copy3 city-loc-1) (at package-1-copy4 city-loc-1) (at package-1-copy5 city-loc-1) (at package-1-copy6 city-loc-1) (at package-1-copy7 city-loc-1) (at package-1-copy8 city-loc-1) (at package-1-copy9 city-loc-1) (at package-1-copy10 city-loc-1) (at package-1-copy11 city-loc-1) (at package-1-copy12 city-loc-1) (at package-1-copy13 city-loc-1) (at package-1-copy14 city-loc-1) (at package-1-copy15 city-loc-1) (at package-1-copy16 city-loc-1) (at package-1-copy17 city-loc-1) (at package-1-copy18 city-loc-1) (at package-1-copy19 city-loc-1) (at package-1-copy20 city-loc-1) (at package-1-copy21 city-loc-1) (at package-1-copy22 city-loc-1) (at package-1-copy23 city-loc-1) (at package-1-copy24 city-loc-1) (at package-1-copy25 city-loc-1) (at package-1-copy26 city-loc-1) (at package-1-copy27 city-loc-1) (at package-1-copy28 city-loc-1) (at package-1-copy29 city-loc-1) (at package-1-copy30 city-loc-1) (at package-1-copy31 city-loc-1) (at package-1-copy32 city-loc-1) (at package-1-copy33 city-loc-1) (at package-1-copy34 city-loc-1) (at package-1-copy35 city-loc-1) (at package-1-copy36 city-loc-1) (at package-1-copy37 city-loc-1) (at package-1-copy38 city-loc-1) (at package-1-copy39 city-loc-1) (at package-1-copy40 city-loc-1) (at package-1-copy41 city-loc-1) (at package-1-copy42 city-loc-1) (at package-1-copy43 city-loc-1) (at package-1-copy44 city-loc-1) (at package-1-copy45 city-loc-1) (at package-1-copy46 city-loc-1) (at package-1-copy47 city-loc-1) (at package-1-copy48 city-loc-1)
  (at package-2 city-loc-1)
  (at package-3 city-loc-3)
  (at package-4 city-loc-2)
  (at truck-1 city-loc-2)
  (capacity truck-1 capacity-3)
  (at truck-2 city-loc-1)
  (capacity truck-2 capacity-2)
 )
 (:goal (and
  (at package-1 city-loc-2) (at package-1-copy1 city-loc-2) (at package-1-copy2 city-loc-2) (at package-1-copy3 city-loc-2) (at package-1-copy4 city-loc-2) (at package-1-copy5 city-loc-2) (at package-1-copy6 city-loc-2) (at package-1-copy7 city-loc-2) (at package-1-copy8 city-loc-2) (at package-1-copy9 city-loc-2) (at package-1-copy10 city-loc-2) (at package-1-copy11 city-loc-2) (at package-1-copy12 city-loc-2) (at package-1-copy13 city-loc-2) (at package-1-copy14 city-loc-2) (at package-1-copy15 city-loc-2) (at package-1-copy16 city-loc-2) (at package-1-copy17 city-loc-2) (at package-1-copy18 city-loc-2) (at package-1-copy19 city-loc-2) (at package-1-copy20 city-loc-2) (at package-1-copy21 city-loc-2) (at package-1-copy22 city-loc-2) (at package-1-copy23 city-loc-2) (at package-1-copy24 city-loc-2) (at package-1-copy25 city-loc-2) (at package-1-copy26 city-loc-2) (at package-1-copy27 city-loc-2) (at package-1-copy28 city-loc-2) (at package-1-copy29 city-loc-2) (at package-1-copy30 city-loc-2) (at package-1-copy31 city-loc-2) (at package-1-copy32 city-loc-2) (at package-1-copy33 city-loc-2) (at package-1-copy34 city-loc-2) (at package-1-copy35 city-loc-2) (at package-1-copy36 city-loc-2) (at package-1-copy37 city-loc-2) (at package-1-copy38 city-loc-2) (at package-1-copy39 city-loc-2) (at package-1-copy40 city-loc-2) (at package-1-copy41 city-loc-2) (at package-1-copy42 city-loc-2) (at package-1-copy43 city-loc-2) (at package-1-copy44 city-loc-2) (at package-1-copy45 city-loc-2) (at package-1-copy46 city-loc-2) (at package-1-copy47 city-loc-2) (at package-1-copy48 city-loc-2)
  (at package-2 city-loc-2)
  (at package-3 city-loc-1)
  (at package-4 city-loc-5)
 ))
 (:metric minimize (total-cost))
)
