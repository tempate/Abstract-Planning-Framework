;; ## ####
;; ####  ####
;;  # $ $.  #
;; ## #  .$ #
;; #   ##.###
;; #  $  . #
;; # @ #   #
;; #  ######
;; ####

(define (problem p127-microban-sequential)
  (:domain sokoban-sequential)
  (:objects
    dir-down - direction
    dir-left - direction
    dir-right - direction
    dir-up - direction
    player-01 - player
    pos-01-01 - location
    pos-01-02 - location
    pos-01-03 pos-01-03-copy1 pos-01-03-copy2 pos-01-03-copy3 pos-01-03-copy4 pos-01-03-copy5 pos-01-03-copy6 pos-01-03-copy7 pos-01-03-copy8 pos-01-03-copy9 pos-01-03-copy10 pos-01-03-copy11 pos-01-03-copy12 pos-01-03-copy13 pos-01-03-copy14 pos-01-03-copy15 pos-01-03-copy16 pos-01-03-copy17 pos-01-03-copy18 pos-01-03-copy19 pos-01-03-copy20 pos-01-03-copy21 pos-01-03-copy22 pos-01-03-copy23 pos-01-03-copy24 pos-01-03-copy25 pos-01-03-copy26 pos-01-03-copy27 pos-01-03-copy28 pos-01-03-copy29 pos-01-03-copy30 pos-01-03-copy31 pos-01-03-copy32 pos-01-03-copy33 pos-01-03-copy34 pos-01-03-copy35 pos-01-03-copy36 pos-01-03-copy37 pos-01-03-copy38 pos-01-03-copy39 pos-01-03-copy40 pos-01-03-copy41 pos-01-03-copy42 pos-01-03-copy43 pos-01-03-copy44 pos-01-03-copy45 pos-01-03-copy46 pos-01-03-copy47 pos-01-03-copy48 - location
    pos-01-04 - location
    pos-01-05 - location
    pos-01-06 - location
    pos-01-07 - location
    pos-01-08 - location
    pos-01-09 - location
    pos-02-01 - location
    pos-02-02 - location
    pos-02-03 - location
    pos-02-04 - location
    pos-02-05 - location
    pos-02-06 - location
    pos-02-07 - location
    pos-02-08 - location
    pos-02-09 - location
    pos-03-01 - location
    pos-03-02 - location
    pos-03-03 - location
    pos-03-04 - location
    pos-03-05 - location
    pos-03-06 - location
    pos-03-07 - location
    pos-03-08 - location
    pos-03-09 - location
    pos-04-01 - location
    pos-04-02 - location
    pos-04-03 - location
    pos-04-04 - location
    pos-04-05 - location
    pos-04-06 - location
    pos-04-07 - location
    pos-04-08 - location
    pos-04-09 - location
    pos-05-01 - location
    pos-05-02 - location
    pos-05-03 - location
    pos-05-04 - location
    pos-05-05 - location
    pos-05-06 - location
    pos-05-07 - location
    pos-05-08 - location
    pos-05-09 - location
    pos-06-01 - location
    pos-06-02 - location
    pos-06-03 - location
    pos-06-04 - location
    pos-06-05 - location
    pos-06-06 - location
    pos-06-07 - location
    pos-06-08 - location
    pos-06-09 - location
    pos-07-01 - location
    pos-07-02 - location
    pos-07-03 - location
    pos-07-04 - location
    pos-07-05 - location
    pos-07-06 - location
    pos-07-07 - location
    pos-07-08 - location
    pos-07-09 - location
    pos-08-01 - location
    pos-08-02 - location
    pos-08-03 - location
    pos-08-04 - location
    pos-08-05 - location
    pos-08-06 - location
    pos-08-07 - location
    pos-08-08 - location
    pos-08-09 - location
    pos-09-01 - location
    pos-09-02 - location
    pos-09-03 - location
    pos-09-04 - location
    pos-09-05 - location
    pos-09-06 - location
    pos-09-07 - location
    pos-09-08 - location
    pos-09-09 - location
    pos-10-01 - location
    pos-10-02 - location
    pos-10-03 - location
    pos-10-04 - location
    pos-10-05 - location
    pos-10-06 - location
    pos-10-07 - location
    pos-10-08 - location
    pos-10-09 - location
    stone-01 - stone
    stone-02 - stone
    stone-03 - stone
    stone-04 - stone
  )
  (:init
    (IS-GOAL pos-07-03)
    (IS-GOAL pos-07-04)
    (IS-GOAL pos-07-05)
    (IS-GOAL pos-07-06)
    (IS-NONGOAL pos-01-01)
    (IS-NONGOAL pos-01-02)
    (IS-NONGOAL pos-01-03) (IS-NONGOAL pos-01-03-copy1) (IS-NONGOAL pos-01-03-copy2) (IS-NONGOAL pos-01-03-copy3) (IS-NONGOAL pos-01-03-copy4) (IS-NONGOAL pos-01-03-copy5) (IS-NONGOAL pos-01-03-copy6) (IS-NONGOAL pos-01-03-copy7) (IS-NONGOAL pos-01-03-copy8) (IS-NONGOAL pos-01-03-copy9) (IS-NONGOAL pos-01-03-copy10) (IS-NONGOAL pos-01-03-copy11) (IS-NONGOAL pos-01-03-copy12) (IS-NONGOAL pos-01-03-copy13) (IS-NONGOAL pos-01-03-copy14) (IS-NONGOAL pos-01-03-copy15) (IS-NONGOAL pos-01-03-copy16) (IS-NONGOAL pos-01-03-copy17) (IS-NONGOAL pos-01-03-copy18) (IS-NONGOAL pos-01-03-copy19) (IS-NONGOAL pos-01-03-copy20) (IS-NONGOAL pos-01-03-copy21) (IS-NONGOAL pos-01-03-copy22) (IS-NONGOAL pos-01-03-copy23) (IS-NONGOAL pos-01-03-copy24) (IS-NONGOAL pos-01-03-copy25) (IS-NONGOAL pos-01-03-copy26) (IS-NONGOAL pos-01-03-copy27) (IS-NONGOAL pos-01-03-copy28) (IS-NONGOAL pos-01-03-copy29) (IS-NONGOAL pos-01-03-copy30) (IS-NONGOAL pos-01-03-copy31) (IS-NONGOAL pos-01-03-copy32) (IS-NONGOAL pos-01-03-copy33) (IS-NONGOAL pos-01-03-copy34) (IS-NONGOAL pos-01-03-copy35) (IS-NONGOAL pos-01-03-copy36) (IS-NONGOAL pos-01-03-copy37) (IS-NONGOAL pos-01-03-copy38) (IS-NONGOAL pos-01-03-copy39) (IS-NONGOAL pos-01-03-copy40) (IS-NONGOAL pos-01-03-copy41) (IS-NONGOAL pos-01-03-copy42) (IS-NONGOAL pos-01-03-copy43) (IS-NONGOAL pos-01-03-copy44) (IS-NONGOAL pos-01-03-copy45) (IS-NONGOAL pos-01-03-copy46) (IS-NONGOAL pos-01-03-copy47) (IS-NONGOAL pos-01-03-copy48)
    (IS-NONGOAL pos-01-04)
    (IS-NONGOAL pos-01-05)
    (IS-NONGOAL pos-01-06)
    (IS-NONGOAL pos-01-07)
    (IS-NONGOAL pos-01-08)
    (IS-NONGOAL pos-01-09)
    (IS-NONGOAL pos-02-01)
    (IS-NONGOAL pos-02-02)
    (IS-NONGOAL pos-02-03)
    (IS-NONGOAL pos-02-04)
    (IS-NONGOAL pos-02-05)
    (IS-NONGOAL pos-02-06)
    (IS-NONGOAL pos-02-07)
    (IS-NONGOAL pos-02-08)
    (IS-NONGOAL pos-02-09)
    (IS-NONGOAL pos-03-01)
    (IS-NONGOAL pos-03-02)
    (IS-NONGOAL pos-03-03)
    (IS-NONGOAL pos-03-04)
    (IS-NONGOAL pos-03-05)
    (IS-NONGOAL pos-03-06)
    (IS-NONGOAL pos-03-07)
    (IS-NONGOAL pos-03-08)
    (IS-NONGOAL pos-03-09)
    (IS-NONGOAL pos-04-01)
    (IS-NONGOAL pos-04-02)
    (IS-NONGOAL pos-04-03)
    (IS-NONGOAL pos-04-04)
    (IS-NONGOAL pos-04-05)
    (IS-NONGOAL pos-04-06)
    (IS-NONGOAL pos-04-07)
    (IS-NONGOAL pos-04-08)
    (IS-NONGOAL pos-04-09)
    (IS-NONGOAL pos-05-01)
    (IS-NONGOAL pos-05-02)
    (IS-NONGOAL pos-05-03)
    (IS-NONGOAL pos-05-04)
    (IS-NONGOAL pos-05-05)
    (IS-NONGOAL pos-05-06)
    (IS-NONGOAL pos-05-07)
    (IS-NONGOAL pos-05-08)
    (IS-NONGOAL pos-05-09)
    (IS-NONGOAL pos-06-01)
    (IS-NONGOAL pos-06-02)
    (IS-NONGOAL pos-06-03)
    (IS-NONGOAL pos-06-04)
    (IS-NONGOAL pos-06-05)
    (IS-NONGOAL pos-06-06)
    (IS-NONGOAL pos-06-07)
    (IS-NONGOAL pos-06-08)
    (IS-NONGOAL pos-06-09)
    (IS-NONGOAL pos-07-01)
    (IS-NONGOAL pos-07-02)
    (IS-NONGOAL pos-07-07)
    (IS-NONGOAL pos-07-08)
    (IS-NONGOAL pos-07-09)
    (IS-NONGOAL pos-08-01)
    (IS-NONGOAL pos-08-02)
    (IS-NONGOAL pos-08-03)
    (IS-NONGOAL pos-08-04)
    (IS-NONGOAL pos-08-05)
    (IS-NONGOAL pos-08-06)
    (IS-NONGOAL pos-08-07)
    (IS-NONGOAL pos-08-08)
    (IS-NONGOAL pos-08-09)
    (IS-NONGOAL pos-09-01)
    (IS-NONGOAL pos-09-02)
    (IS-NONGOAL pos-09-03)
    (IS-NONGOAL pos-09-04)
    (IS-NONGOAL pos-09-05)
    (IS-NONGOAL pos-09-06)
    (IS-NONGOAL pos-09-07)
    (IS-NONGOAL pos-09-08)
    (IS-NONGOAL pos-09-09)
    (IS-NONGOAL pos-10-01)
    (IS-NONGOAL pos-10-02)
    (IS-NONGOAL pos-10-03)
    (IS-NONGOAL pos-10-04)
    (IS-NONGOAL pos-10-05)
    (IS-NONGOAL pos-10-06)
    (IS-NONGOAL pos-10-07)
    (IS-NONGOAL pos-10-08)
    (IS-NONGOAL pos-10-09)
    (MOVE-DIR pos-02-05 pos-02-06 dir-down)
    (MOVE-DIR pos-02-05 pos-03-05 dir-right)
    (MOVE-DIR pos-02-06 pos-02-05 dir-up)
    (MOVE-DIR pos-02-06 pos-02-07 dir-down)
    (MOVE-DIR pos-02-06 pos-03-06 dir-right)
    (MOVE-DIR pos-02-07 pos-02-06 dir-up)
    (MOVE-DIR pos-02-07 pos-02-08 dir-down)
    (MOVE-DIR pos-02-07 pos-03-07 dir-right)
    (MOVE-DIR pos-02-08 pos-02-07 dir-up)
    (MOVE-DIR pos-02-08 pos-03-08 dir-right)
    (MOVE-DIR pos-03-03 pos-03-04 dir-down)
    (MOVE-DIR pos-03-03 pos-04-03 dir-right)
    (MOVE-DIR pos-03-04 pos-03-03 dir-up)
    (MOVE-DIR pos-03-04 pos-03-05 dir-down)
    (MOVE-DIR pos-03-05 pos-02-05 dir-left)
    (MOVE-DIR pos-03-05 pos-03-04 dir-up)
    (MOVE-DIR pos-03-05 pos-03-06 dir-down)
    (MOVE-DIR pos-03-05 pos-04-05 dir-right)
    (MOVE-DIR pos-03-06 pos-02-06 dir-left)
    (MOVE-DIR pos-03-06 pos-03-05 dir-up)
    (MOVE-DIR pos-03-06 pos-03-07 dir-down)
    (MOVE-DIR pos-03-06 pos-04-06 dir-right)
    (MOVE-DIR pos-03-07 pos-02-07 dir-left)
    (MOVE-DIR pos-03-07 pos-03-06 dir-up)
    (MOVE-DIR pos-03-07 pos-03-08 dir-down)
    (MOVE-DIR pos-03-07 pos-04-07 dir-right)
    (MOVE-DIR pos-03-08 pos-02-08 dir-left)
    (MOVE-DIR pos-03-08 pos-03-07 dir-up)
    (MOVE-DIR pos-04-03 pos-03-03 dir-left)
    (MOVE-DIR pos-04-03 pos-05-03 dir-right)
    (MOVE-DIR pos-04-05 pos-03-05 dir-left)
    (MOVE-DIR pos-04-05 pos-04-06 dir-down)
    (MOVE-DIR pos-04-06 pos-03-06 dir-left)
    (MOVE-DIR pos-04-06 pos-04-05 dir-up)
    (MOVE-DIR pos-04-06 pos-04-07 dir-down)
    (MOVE-DIR pos-04-06 pos-05-06 dir-right)
    (MOVE-DIR pos-04-07 pos-03-07 dir-left)
    (MOVE-DIR pos-04-07 pos-04-06 dir-up)
    (MOVE-DIR pos-05-02 pos-05-03 dir-down)
    (MOVE-DIR pos-05-02 pos-06-02 dir-right)
    (MOVE-DIR pos-05-03 pos-04-03 dir-left)
    (MOVE-DIR pos-05-03 pos-05-02 dir-up)
    (MOVE-DIR pos-05-03 pos-05-04 dir-down)
    (MOVE-DIR pos-05-03 pos-06-03 dir-right)
    (MOVE-DIR pos-05-04 pos-05-03 dir-up)
    (MOVE-DIR pos-05-04 pos-06-04 dir-right)
    (MOVE-DIR pos-05-06 pos-04-06 dir-left)
    (MOVE-DIR pos-05-06 pos-06-06 dir-right)
    (MOVE-DIR pos-05-09 pos-06-09 dir-right)
    (MOVE-DIR pos-06-02 pos-05-02 dir-left)
    (MOVE-DIR pos-06-02 pos-06-03 dir-down)
    (MOVE-DIR pos-06-03 pos-05-03 dir-left)
    (MOVE-DIR pos-06-03 pos-06-02 dir-up)
    (MOVE-DIR pos-06-03 pos-06-04 dir-down)
    (MOVE-DIR pos-06-03 pos-07-03 dir-right)
    (MOVE-DIR pos-06-04 pos-05-04 dir-left)
    (MOVE-DIR pos-06-04 pos-06-03 dir-up)
    (MOVE-DIR pos-06-04 pos-07-04 dir-right)
    (MOVE-DIR pos-06-06 pos-05-06 dir-left)
    (MOVE-DIR pos-06-06 pos-06-07 dir-down)
    (MOVE-DIR pos-06-06 pos-07-06 dir-right)
    (MOVE-DIR pos-06-07 pos-06-06 dir-up)
    (MOVE-DIR pos-06-07 pos-07-07 dir-right)
    (MOVE-DIR pos-06-09 pos-05-09 dir-left)
    (MOVE-DIR pos-06-09 pos-07-09 dir-right)
    (MOVE-DIR pos-07-03 pos-06-03 dir-left)
    (MOVE-DIR pos-07-03 pos-07-04 dir-down)
    (MOVE-DIR pos-07-03 pos-08-03 dir-right)
    (MOVE-DIR pos-07-04 pos-06-04 dir-left)
    (MOVE-DIR pos-07-04 pos-07-03 dir-up)
    (MOVE-DIR pos-07-04 pos-07-05 dir-down)
    (MOVE-DIR pos-07-04 pos-08-04 dir-right)
    (MOVE-DIR pos-07-05 pos-07-04 dir-up)
    (MOVE-DIR pos-07-05 pos-07-06 dir-down)
    (MOVE-DIR pos-07-06 pos-06-06 dir-left)
    (MOVE-DIR pos-07-06 pos-07-05 dir-up)
    (MOVE-DIR pos-07-06 pos-07-07 dir-down)
    (MOVE-DIR pos-07-06 pos-08-06 dir-right)
    (MOVE-DIR pos-07-07 pos-06-07 dir-left)
    (MOVE-DIR pos-07-07 pos-07-06 dir-up)
    (MOVE-DIR pos-07-07 pos-08-07 dir-right)
    (MOVE-DIR pos-07-09 pos-06-09 dir-left)
    (MOVE-DIR pos-07-09 pos-08-09 dir-right)
    (MOVE-DIR pos-08-01 pos-09-01 dir-right)
    (MOVE-DIR pos-08-03 pos-07-03 dir-left)
    (MOVE-DIR pos-08-03 pos-08-04 dir-down)
    (MOVE-DIR pos-08-03 pos-09-03 dir-right)
    (MOVE-DIR pos-08-04 pos-07-04 dir-left)
    (MOVE-DIR pos-08-04 pos-08-03 dir-up)
    (MOVE-DIR pos-08-04 pos-09-04 dir-right)
    (MOVE-DIR pos-08-06 pos-07-06 dir-left)
    (MOVE-DIR pos-08-06 pos-08-07 dir-down)
    (MOVE-DIR pos-08-07 pos-07-07 dir-left)
    (MOVE-DIR pos-08-07 pos-08-06 dir-up)
    (MOVE-DIR pos-08-09 pos-07-09 dir-left)
    (MOVE-DIR pos-08-09 pos-09-09 dir-right)
    (MOVE-DIR pos-09-01 pos-08-01 dir-left)
    (MOVE-DIR pos-09-01 pos-10-01 dir-right)
    (MOVE-DIR pos-09-03 pos-08-03 dir-left)
    (MOVE-DIR pos-09-03 pos-09-04 dir-down)
    (MOVE-DIR pos-09-04 pos-08-04 dir-left)
    (MOVE-DIR pos-09-04 pos-09-03 dir-up)
    (MOVE-DIR pos-09-09 pos-08-09 dir-left)
    (MOVE-DIR pos-09-09 pos-10-09 dir-right)
    (MOVE-DIR pos-10-01 pos-09-01 dir-left)
    (MOVE-DIR pos-10-06 pos-10-07 dir-down)
    (MOVE-DIR pos-10-07 pos-10-06 dir-up)
    (MOVE-DIR pos-10-07 pos-10-08 dir-down)
    (MOVE-DIR pos-10-08 pos-10-07 dir-up)
    (MOVE-DIR pos-10-08 pos-10-09 dir-down)
    (MOVE-DIR pos-10-09 pos-09-09 dir-left)
    (MOVE-DIR pos-10-09 pos-10-08 dir-up)
    (at player-01 pos-03-07)
    (at stone-01 pos-04-03)
    (at stone-02 pos-06-03)
    (at stone-03 pos-08-04)
    (at stone-04 pos-04-06)
    (clear pos-01-03) (clear pos-01-03-copy1) (clear pos-01-03-copy2) (clear pos-01-03-copy3) (clear pos-01-03-copy4) (clear pos-01-03-copy5) (clear pos-01-03-copy6) (clear pos-01-03-copy7) (clear pos-01-03-copy8) (clear pos-01-03-copy9) (clear pos-01-03-copy10) (clear pos-01-03-copy11) (clear pos-01-03-copy12) (clear pos-01-03-copy13) (clear pos-01-03-copy14) (clear pos-01-03-copy15) (clear pos-01-03-copy16) (clear pos-01-03-copy17) (clear pos-01-03-copy18) (clear pos-01-03-copy19) (clear pos-01-03-copy20) (clear pos-01-03-copy21) (clear pos-01-03-copy22) (clear pos-01-03-copy23) (clear pos-01-03-copy24) (clear pos-01-03-copy25) (clear pos-01-03-copy26) (clear pos-01-03-copy27) (clear pos-01-03-copy28) (clear pos-01-03-copy29) (clear pos-01-03-copy30) (clear pos-01-03-copy31) (clear pos-01-03-copy32) (clear pos-01-03-copy33) (clear pos-01-03-copy34) (clear pos-01-03-copy35) (clear pos-01-03-copy36) (clear pos-01-03-copy37) (clear pos-01-03-copy38) (clear pos-01-03-copy39) (clear pos-01-03-copy40) (clear pos-01-03-copy41) (clear pos-01-03-copy42) (clear pos-01-03-copy43) (clear pos-01-03-copy44) (clear pos-01-03-copy45) (clear pos-01-03-copy46) (clear pos-01-03-copy47) (clear pos-01-03-copy48)
    (clear pos-02-05)
    (clear pos-02-06)
    (clear pos-02-07)
    (clear pos-02-08)
    (clear pos-03-01)
    (clear pos-03-03)
    (clear pos-03-04)
    (clear pos-03-05)
    (clear pos-03-06)
    (clear pos-03-08)
    (clear pos-04-05)
    (clear pos-04-07)
    (clear pos-05-02)
    (clear pos-05-03)
    (clear pos-05-04)
    (clear pos-05-06)
    (clear pos-05-09)
    (clear pos-06-02)
    (clear pos-06-04)
    (clear pos-06-06)
    (clear pos-06-07)
    (clear pos-06-09)
    (clear pos-07-03)
    (clear pos-07-04)
    (clear pos-07-05)
    (clear pos-07-06)
    (clear pos-07-07)
    (clear pos-07-09)
    (clear pos-08-01)
    (clear pos-08-03)
    (clear pos-08-06)
    (clear pos-08-07)
    (clear pos-08-09)
    (clear pos-09-01)
    (clear pos-09-03)
    (clear pos-09-04)
    (clear pos-09-09)
    (clear pos-10-01)
    (clear pos-10-06)
    (clear pos-10-07)
    (clear pos-10-08)
    (clear pos-10-09)
    (= (total-cost) 0)
  )
  (:goal (and
    (at-goal stone-01)
    (at-goal stone-02)
    (at-goal stone-03)
    (at-goal stone-04)
  ))
  (:metric minimize (total-cost))
)
