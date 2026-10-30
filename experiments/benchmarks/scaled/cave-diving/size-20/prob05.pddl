;; Cave Diving STRIPS
;; Authors: Nathan Robinson,
;;          Christian Muise, and
;;          Charles Gretton

(define (problem cave-diving-strips-prob05)
  (:domain cave-diving-strips)
  (:objects
    l0 l1 l2 - location
    t0 dummy - tank
    zero one two three four - quantity
  )

  (:init
    (available d0) (available d0-copy1) (available d0-copy2) (available d0-copy3) (available d0-copy4) (available d0-copy5) (available d0-copy6) (available d0-copy7) (available d0-copy8) (available d0-copy9) (available d0-copy10) (available d0-copy11) (available d0-copy12) (available d0-copy13) (available d0-copy14) (available d0-copy15) (available d0-copy16) (available d0-copy17) (available d0-copy18)
    (available d1)
    (capacity d0 four) (capacity d0-copy1 four) (capacity d0-copy2 four) (capacity d0-copy3 four) (capacity d0-copy4 four) (capacity d0-copy5 four) (capacity d0-copy6 four) (capacity d0-copy7 four) (capacity d0-copy8 four) (capacity d0-copy9 four) (capacity d0-copy10 four) (capacity d0-copy11 four) (capacity d0-copy12 four) (capacity d0-copy13 four) (capacity d0-copy14 four) (capacity d0-copy15 four) (capacity d0-copy16 four) (capacity d0-copy17 four) (capacity d0-copy18 four)
    (capacity d1 four)
    (in-storage t0)
    (next-tank t0 dummy)
    (cave-entrance l0)
    (connected l0 l1)
    (connected l1 l0)
    (connected l1 l2)
    (connected l2 l1)
    (next-quantity zero one)
    (next-quantity one two)
    (next-quantity two three)
    (next-quantity three four)
  )

  (:goal
    (and
      (have-photo l2)
      (decompressing d1)
      (decompressing d0) (decompressing d0-copy1) (decompressing d0-copy2) (decompressing d0-copy3) (decompressing d0-copy4) (decompressing d0-copy5) (decompressing d0-copy6) (decompressing d0-copy7) (decompressing d0-copy8) (decompressing d0-copy9) (decompressing d0-copy10) (decompressing d0-copy11) (decompressing d0-copy12) (decompressing d0-copy13) (decompressing d0-copy14) (decompressing d0-copy15) (decompressing d0-copy16) (decompressing d0-copy17) (decompressing d0-copy18)
    )
  )

)
