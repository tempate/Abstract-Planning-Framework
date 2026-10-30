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
    (available d0) (available d0-copy1) (available d0-copy2) (available d0-copy3) (available d0-copy4) (available d0-copy5) (available d0-copy6) (available d0-copy7) (available d0-copy8) (available d0-copy9) (available d0-copy10) (available d0-copy11) (available d0-copy12) (available d0-copy13) (available d0-copy14) (available d0-copy15) (available d0-copy16) (available d0-copy17) (available d0-copy18) (available d0-copy19) (available d0-copy20) (available d0-copy21) (available d0-copy22) (available d0-copy23) (available d0-copy24) (available d0-copy25) (available d0-copy26) (available d0-copy27) (available d0-copy28) (available d0-copy29) (available d0-copy30) (available d0-copy31) (available d0-copy32) (available d0-copy33) (available d0-copy34) (available d0-copy35) (available d0-copy36) (available d0-copy37) (available d0-copy38) (available d0-copy39) (available d0-copy40) (available d0-copy41) (available d0-copy42) (available d0-copy43) (available d0-copy44) (available d0-copy45) (available d0-copy46) (available d0-copy47) (available d0-copy48)
    (available d1)
    (capacity d0 four) (capacity d0-copy1 four) (capacity d0-copy2 four) (capacity d0-copy3 four) (capacity d0-copy4 four) (capacity d0-copy5 four) (capacity d0-copy6 four) (capacity d0-copy7 four) (capacity d0-copy8 four) (capacity d0-copy9 four) (capacity d0-copy10 four) (capacity d0-copy11 four) (capacity d0-copy12 four) (capacity d0-copy13 four) (capacity d0-copy14 four) (capacity d0-copy15 four) (capacity d0-copy16 four) (capacity d0-copy17 four) (capacity d0-copy18 four) (capacity d0-copy19 four) (capacity d0-copy20 four) (capacity d0-copy21 four) (capacity d0-copy22 four) (capacity d0-copy23 four) (capacity d0-copy24 four) (capacity d0-copy25 four) (capacity d0-copy26 four) (capacity d0-copy27 four) (capacity d0-copy28 four) (capacity d0-copy29 four) (capacity d0-copy30 four) (capacity d0-copy31 four) (capacity d0-copy32 four) (capacity d0-copy33 four) (capacity d0-copy34 four) (capacity d0-copy35 four) (capacity d0-copy36 four) (capacity d0-copy37 four) (capacity d0-copy38 four) (capacity d0-copy39 four) (capacity d0-copy40 four) (capacity d0-copy41 four) (capacity d0-copy42 four) (capacity d0-copy43 four) (capacity d0-copy44 four) (capacity d0-copy45 four) (capacity d0-copy46 four) (capacity d0-copy47 four) (capacity d0-copy48 four)
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
      (decompressing d0) (decompressing d0-copy1) (decompressing d0-copy2) (decompressing d0-copy3) (decompressing d0-copy4) (decompressing d0-copy5) (decompressing d0-copy6) (decompressing d0-copy7) (decompressing d0-copy8) (decompressing d0-copy9) (decompressing d0-copy10) (decompressing d0-copy11) (decompressing d0-copy12) (decompressing d0-copy13) (decompressing d0-copy14) (decompressing d0-copy15) (decompressing d0-copy16) (decompressing d0-copy17) (decompressing d0-copy18) (decompressing d0-copy19) (decompressing d0-copy20) (decompressing d0-copy21) (decompressing d0-copy22) (decompressing d0-copy23) (decompressing d0-copy24) (decompressing d0-copy25) (decompressing d0-copy26) (decompressing d0-copy27) (decompressing d0-copy28) (decompressing d0-copy29) (decompressing d0-copy30) (decompressing d0-copy31) (decompressing d0-copy32) (decompressing d0-copy33) (decompressing d0-copy34) (decompressing d0-copy35) (decompressing d0-copy36) (decompressing d0-copy37) (decompressing d0-copy38) (decompressing d0-copy39) (decompressing d0-copy40) (decompressing d0-copy41) (decompressing d0-copy42) (decompressing d0-copy43) (decompressing d0-copy44) (decompressing d0-copy45) (decompressing d0-copy46) (decompressing d0-copy47) (decompressing d0-copy48)
    )
  )

)
