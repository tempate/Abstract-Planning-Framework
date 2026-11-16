;;  ####
;; ##  ###
;; #     #
;; #.**$@#
;; #   ###
;; ##  #
;;  ####

(define (problem p032-microban-sequential)
  (:domain sokoban-sequential)
  (:objects
    dir-down - direction
    dir-left - direction
    dir-right - direction
    dir-up - direction
    player-01 - player
    pos-1-1 pos-1-1-copy1 pos-1-1-copy2 pos-1-1-copy3 pos-1-1-copy4 pos-1-1-copy5 pos-1-1-copy6 pos-1-1-copy7 pos-1-1-copy8 pos-1-1-copy9 pos-1-1-copy10 pos-1-1-copy11 pos-1-1-copy12 pos-1-1-copy13 pos-1-1-copy14 pos-1-1-copy15 pos-1-1-copy16 pos-1-1-copy17 pos-1-1-copy18 pos-1-1-copy19 pos-1-1-copy20 pos-1-1-copy21 pos-1-1-copy22 pos-1-1-copy23 pos-1-1-copy24 pos-1-1-copy25 pos-1-1-copy26 pos-1-1-copy27 pos-1-1-copy28 pos-1-1-copy29 pos-1-1-copy30 pos-1-1-copy31 pos-1-1-copy32 pos-1-1-copy33 pos-1-1-copy34 pos-1-1-copy35 pos-1-1-copy36 pos-1-1-copy37 pos-1-1-copy38 pos-1-1-copy39 pos-1-1-copy40 pos-1-1-copy41 pos-1-1-copy42 pos-1-1-copy43 pos-1-1-copy44 pos-1-1-copy45 pos-1-1-copy46 pos-1-1-copy47 pos-1-1-copy48 - location
    pos-1-2 - location
    pos-1-3 - location
    pos-1-4 - location
    pos-1-5 - location
    pos-1-6 - location
    pos-1-7 - location
    pos-2-1 - location
    pos-2-2 - location
    pos-2-3 - location
    pos-2-4 - location
    pos-2-5 - location
    pos-2-6 - location
    pos-2-7 - location
    pos-3-1 - location
    pos-3-2 - location
    pos-3-3 - location
    pos-3-4 - location
    pos-3-5 - location
    pos-3-6 - location
    pos-3-7 - location
    pos-4-1 - location
    pos-4-2 - location
    pos-4-3 - location
    pos-4-4 - location
    pos-4-5 - location
    pos-4-6 - location
    pos-4-7 - location
    pos-5-1 - location
    pos-5-2 - location
    pos-5-3 - location
    pos-5-4 - location
    pos-5-5 - location
    pos-5-6 - location
    pos-5-7 - location
    pos-6-1 - location
    pos-6-2 - location
    pos-6-3 - location
    pos-6-4 - location
    pos-6-5 - location
    pos-6-6 - location
    pos-6-7 - location
    pos-7-1 - location
    pos-7-2 - location
    pos-7-3 - location
    pos-7-4 - location
    pos-7-5 - location
    pos-7-6 - location
    pos-7-7 - location
    stone-01 - stone
    stone-02 - stone
    stone-03 - stone
  )
  (:init
    (IS-GOAL pos-2-4)
    (IS-GOAL pos-3-4)
    (IS-GOAL pos-4-4)
    (IS-NONGOAL pos-1-1) (IS-NONGOAL pos-1-1-copy1) (IS-NONGOAL pos-1-1-copy2) (IS-NONGOAL pos-1-1-copy3) (IS-NONGOAL pos-1-1-copy4) (IS-NONGOAL pos-1-1-copy5) (IS-NONGOAL pos-1-1-copy6) (IS-NONGOAL pos-1-1-copy7) (IS-NONGOAL pos-1-1-copy8) (IS-NONGOAL pos-1-1-copy9) (IS-NONGOAL pos-1-1-copy10) (IS-NONGOAL pos-1-1-copy11) (IS-NONGOAL pos-1-1-copy12) (IS-NONGOAL pos-1-1-copy13) (IS-NONGOAL pos-1-1-copy14) (IS-NONGOAL pos-1-1-copy15) (IS-NONGOAL pos-1-1-copy16) (IS-NONGOAL pos-1-1-copy17) (IS-NONGOAL pos-1-1-copy18) (IS-NONGOAL pos-1-1-copy19) (IS-NONGOAL pos-1-1-copy20) (IS-NONGOAL pos-1-1-copy21) (IS-NONGOAL pos-1-1-copy22) (IS-NONGOAL pos-1-1-copy23) (IS-NONGOAL pos-1-1-copy24) (IS-NONGOAL pos-1-1-copy25) (IS-NONGOAL pos-1-1-copy26) (IS-NONGOAL pos-1-1-copy27) (IS-NONGOAL pos-1-1-copy28) (IS-NONGOAL pos-1-1-copy29) (IS-NONGOAL pos-1-1-copy30) (IS-NONGOAL pos-1-1-copy31) (IS-NONGOAL pos-1-1-copy32) (IS-NONGOAL pos-1-1-copy33) (IS-NONGOAL pos-1-1-copy34) (IS-NONGOAL pos-1-1-copy35) (IS-NONGOAL pos-1-1-copy36) (IS-NONGOAL pos-1-1-copy37) (IS-NONGOAL pos-1-1-copy38) (IS-NONGOAL pos-1-1-copy39) (IS-NONGOAL pos-1-1-copy40) (IS-NONGOAL pos-1-1-copy41) (IS-NONGOAL pos-1-1-copy42) (IS-NONGOAL pos-1-1-copy43) (IS-NONGOAL pos-1-1-copy44) (IS-NONGOAL pos-1-1-copy45) (IS-NONGOAL pos-1-1-copy46) (IS-NONGOAL pos-1-1-copy47) (IS-NONGOAL pos-1-1-copy48)
    (IS-NONGOAL pos-1-2)
    (IS-NONGOAL pos-1-3)
    (IS-NONGOAL pos-1-4)
    (IS-NONGOAL pos-1-5)
    (IS-NONGOAL pos-1-6)
    (IS-NONGOAL pos-1-7)
    (IS-NONGOAL pos-2-1)
    (IS-NONGOAL pos-2-2)
    (IS-NONGOAL pos-2-3)
    (IS-NONGOAL pos-2-5)
    (IS-NONGOAL pos-2-6)
    (IS-NONGOAL pos-2-7)
    (IS-NONGOAL pos-3-1)
    (IS-NONGOAL pos-3-2)
    (IS-NONGOAL pos-3-3)
    (IS-NONGOAL pos-3-5)
    (IS-NONGOAL pos-3-6)
    (IS-NONGOAL pos-3-7)
    (IS-NONGOAL pos-4-1)
    (IS-NONGOAL pos-4-2)
    (IS-NONGOAL pos-4-3)
    (IS-NONGOAL pos-4-5)
    (IS-NONGOAL pos-4-6)
    (IS-NONGOAL pos-4-7)
    (IS-NONGOAL pos-5-1)
    (IS-NONGOAL pos-5-2)
    (IS-NONGOAL pos-5-3)
    (IS-NONGOAL pos-5-4)
    (IS-NONGOAL pos-5-5)
    (IS-NONGOAL pos-5-6)
    (IS-NONGOAL pos-5-7)
    (IS-NONGOAL pos-6-1)
    (IS-NONGOAL pos-6-2)
    (IS-NONGOAL pos-6-3)
    (IS-NONGOAL pos-6-4)
    (IS-NONGOAL pos-6-5)
    (IS-NONGOAL pos-6-6)
    (IS-NONGOAL pos-6-7)
    (IS-NONGOAL pos-7-1)
    (IS-NONGOAL pos-7-2)
    (IS-NONGOAL pos-7-3)
    (IS-NONGOAL pos-7-4)
    (IS-NONGOAL pos-7-5)
    (IS-NONGOAL pos-7-6)
    (IS-NONGOAL pos-7-7)
    (MOVE-DIR pos-2-3 pos-2-4 dir-down)
    (MOVE-DIR pos-2-3 pos-3-3 dir-right)
    (MOVE-DIR pos-2-4 pos-2-3 dir-up)
    (MOVE-DIR pos-2-4 pos-2-5 dir-down)
    (MOVE-DIR pos-2-4 pos-3-4 dir-right)
    (MOVE-DIR pos-2-5 pos-2-4 dir-up)
    (MOVE-DIR pos-2-5 pos-3-5 dir-right)
    (MOVE-DIR pos-3-2 pos-3-3 dir-down)
    (MOVE-DIR pos-3-2 pos-4-2 dir-right)
    (MOVE-DIR pos-3-3 pos-2-3 dir-left)
    (MOVE-DIR pos-3-3 pos-3-2 dir-up)
    (MOVE-DIR pos-3-3 pos-3-4 dir-down)
    (MOVE-DIR pos-3-3 pos-4-3 dir-right)
    (MOVE-DIR pos-3-4 pos-2-4 dir-left)
    (MOVE-DIR pos-3-4 pos-3-3 dir-up)
    (MOVE-DIR pos-3-4 pos-3-5 dir-down)
    (MOVE-DIR pos-3-4 pos-4-4 dir-right)
    (MOVE-DIR pos-3-5 pos-2-5 dir-left)
    (MOVE-DIR pos-3-5 pos-3-4 dir-up)
    (MOVE-DIR pos-3-5 pos-3-6 dir-down)
    (MOVE-DIR pos-3-5 pos-4-5 dir-right)
    (MOVE-DIR pos-3-6 pos-3-5 dir-up)
    (MOVE-DIR pos-3-6 pos-4-6 dir-right)
    (MOVE-DIR pos-4-2 pos-3-2 dir-left)
    (MOVE-DIR pos-4-2 pos-4-3 dir-down)
    (MOVE-DIR pos-4-3 pos-3-3 dir-left)
    (MOVE-DIR pos-4-3 pos-4-2 dir-up)
    (MOVE-DIR pos-4-3 pos-4-4 dir-down)
    (MOVE-DIR pos-4-3 pos-5-3 dir-right)
    (MOVE-DIR pos-4-4 pos-3-4 dir-left)
    (MOVE-DIR pos-4-4 pos-4-3 dir-up)
    (MOVE-DIR pos-4-4 pos-4-5 dir-down)
    (MOVE-DIR pos-4-4 pos-5-4 dir-right)
    (MOVE-DIR pos-4-5 pos-3-5 dir-left)
    (MOVE-DIR pos-4-5 pos-4-4 dir-up)
    (MOVE-DIR pos-4-5 pos-4-6 dir-down)
    (MOVE-DIR pos-4-6 pos-3-6 dir-left)
    (MOVE-DIR pos-4-6 pos-4-5 dir-up)
    (MOVE-DIR pos-5-3 pos-4-3 dir-left)
    (MOVE-DIR pos-5-3 pos-5-4 dir-down)
    (MOVE-DIR pos-5-3 pos-6-3 dir-right)
    (MOVE-DIR pos-5-4 pos-4-4 dir-left)
    (MOVE-DIR pos-5-4 pos-5-3 dir-up)
    (MOVE-DIR pos-5-4 pos-6-4 dir-right)
    (MOVE-DIR pos-6-1 pos-7-1 dir-right)
    (MOVE-DIR pos-6-3 pos-5-3 dir-left)
    (MOVE-DIR pos-6-3 pos-6-4 dir-down)
    (MOVE-DIR pos-6-4 pos-5-4 dir-left)
    (MOVE-DIR pos-6-4 pos-6-3 dir-up)
    (MOVE-DIR pos-6-6 pos-6-7 dir-down)
    (MOVE-DIR pos-6-6 pos-7-6 dir-right)
    (MOVE-DIR pos-6-7 pos-6-6 dir-up)
    (MOVE-DIR pos-6-7 pos-7-7 dir-right)
    (MOVE-DIR pos-7-1 pos-6-1 dir-left)
    (MOVE-DIR pos-7-6 pos-6-6 dir-left)
    (MOVE-DIR pos-7-6 pos-7-7 dir-down)
    (MOVE-DIR pos-7-7 pos-6-7 dir-left)
    (MOVE-DIR pos-7-7 pos-7-6 dir-up)
    (at player-01 pos-6-4)
    (at stone-01 pos-3-4)
    (at stone-02 pos-4-4)
    (at stone-03 pos-5-4)
    (at-goal stone-01)
    (at-goal stone-02)
    (clear pos-1-1) (clear pos-1-1-copy1) (clear pos-1-1-copy2) (clear pos-1-1-copy3) (clear pos-1-1-copy4) (clear pos-1-1-copy5) (clear pos-1-1-copy6) (clear pos-1-1-copy7) (clear pos-1-1-copy8) (clear pos-1-1-copy9) (clear pos-1-1-copy10) (clear pos-1-1-copy11) (clear pos-1-1-copy12) (clear pos-1-1-copy13) (clear pos-1-1-copy14) (clear pos-1-1-copy15) (clear pos-1-1-copy16) (clear pos-1-1-copy17) (clear pos-1-1-copy18) (clear pos-1-1-copy19) (clear pos-1-1-copy20) (clear pos-1-1-copy21) (clear pos-1-1-copy22) (clear pos-1-1-copy23) (clear pos-1-1-copy24) (clear pos-1-1-copy25) (clear pos-1-1-copy26) (clear pos-1-1-copy27) (clear pos-1-1-copy28) (clear pos-1-1-copy29) (clear pos-1-1-copy30) (clear pos-1-1-copy31) (clear pos-1-1-copy32) (clear pos-1-1-copy33) (clear pos-1-1-copy34) (clear pos-1-1-copy35) (clear pos-1-1-copy36) (clear pos-1-1-copy37) (clear pos-1-1-copy38) (clear pos-1-1-copy39) (clear pos-1-1-copy40) (clear pos-1-1-copy41) (clear pos-1-1-copy42) (clear pos-1-1-copy43) (clear pos-1-1-copy44) (clear pos-1-1-copy45) (clear pos-1-1-copy46) (clear pos-1-1-copy47) (clear pos-1-1-copy48)
    (clear pos-1-7)
    (clear pos-2-3)
    (clear pos-2-4)
    (clear pos-2-5)
    (clear pos-3-2)
    (clear pos-3-3)
    (clear pos-3-5)
    (clear pos-3-6)
    (clear pos-4-2)
    (clear pos-4-3)
    (clear pos-4-5)
    (clear pos-4-6)
    (clear pos-5-3)
    (clear pos-6-1)
    (clear pos-6-3)
    (clear pos-6-6)
    (clear pos-6-7)
    (clear pos-7-1)
    (clear pos-7-6)
    (clear pos-7-7)
    (= (total-cost) 0)
  )
  (:goal (and
    (at-goal stone-01)
    (at-goal stone-02)
    (at-goal stone-03)
  ))
  (:metric minimize (total-cost))
)
