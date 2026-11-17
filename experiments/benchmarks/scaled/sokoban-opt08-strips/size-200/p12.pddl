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
    pos-01-03 pos-01-03-copy1 pos-01-03-copy2 pos-01-03-copy3 pos-01-03-copy4 pos-01-03-copy5 pos-01-03-copy6 pos-01-03-copy7 pos-01-03-copy8 pos-01-03-copy9 pos-01-03-copy10 pos-01-03-copy11 pos-01-03-copy12 pos-01-03-copy13 pos-01-03-copy14 pos-01-03-copy15 pos-01-03-copy16 pos-01-03-copy17 pos-01-03-copy18 pos-01-03-copy19 pos-01-03-copy20 pos-01-03-copy21 pos-01-03-copy22 pos-01-03-copy23 pos-01-03-copy24 pos-01-03-copy25 pos-01-03-copy26 pos-01-03-copy27 pos-01-03-copy28 pos-01-03-copy29 pos-01-03-copy30 pos-01-03-copy31 pos-01-03-copy32 pos-01-03-copy33 pos-01-03-copy34 pos-01-03-copy35 pos-01-03-copy36 pos-01-03-copy37 pos-01-03-copy38 pos-01-03-copy39 pos-01-03-copy40 pos-01-03-copy41 pos-01-03-copy42 pos-01-03-copy43 pos-01-03-copy44 pos-01-03-copy45 pos-01-03-copy46 pos-01-03-copy47 pos-01-03-copy48 pos-01-03-copy49 pos-01-03-copy50 pos-01-03-copy51 pos-01-03-copy52 pos-01-03-copy53 pos-01-03-copy54 pos-01-03-copy55 pos-01-03-copy56 pos-01-03-copy57 pos-01-03-copy58 pos-01-03-copy59 pos-01-03-copy60 pos-01-03-copy61 pos-01-03-copy62 pos-01-03-copy63 pos-01-03-copy64 pos-01-03-copy65 pos-01-03-copy66 pos-01-03-copy67 pos-01-03-copy68 pos-01-03-copy69 pos-01-03-copy70 pos-01-03-copy71 pos-01-03-copy72 pos-01-03-copy73 pos-01-03-copy74 pos-01-03-copy75 pos-01-03-copy76 pos-01-03-copy77 pos-01-03-copy78 pos-01-03-copy79 pos-01-03-copy80 pos-01-03-copy81 pos-01-03-copy82 pos-01-03-copy83 pos-01-03-copy84 pos-01-03-copy85 pos-01-03-copy86 pos-01-03-copy87 pos-01-03-copy88 pos-01-03-copy89 pos-01-03-copy90 pos-01-03-copy91 pos-01-03-copy92 pos-01-03-copy93 pos-01-03-copy94 pos-01-03-copy95 pos-01-03-copy96 pos-01-03-copy97 pos-01-03-copy98 pos-01-03-copy99 pos-01-03-copy100 pos-01-03-copy101 pos-01-03-copy102 pos-01-03-copy103 pos-01-03-copy104 pos-01-03-copy105 pos-01-03-copy106 pos-01-03-copy107 pos-01-03-copy108 pos-01-03-copy109 pos-01-03-copy110 pos-01-03-copy111 pos-01-03-copy112 pos-01-03-copy113 pos-01-03-copy114 pos-01-03-copy115 pos-01-03-copy116 pos-01-03-copy117 pos-01-03-copy118 pos-01-03-copy119 pos-01-03-copy120 pos-01-03-copy121 pos-01-03-copy122 pos-01-03-copy123 pos-01-03-copy124 pos-01-03-copy125 pos-01-03-copy126 pos-01-03-copy127 pos-01-03-copy128 pos-01-03-copy129 pos-01-03-copy130 pos-01-03-copy131 pos-01-03-copy132 pos-01-03-copy133 pos-01-03-copy134 pos-01-03-copy135 pos-01-03-copy136 pos-01-03-copy137 pos-01-03-copy138 pos-01-03-copy139 pos-01-03-copy140 pos-01-03-copy141 pos-01-03-copy142 pos-01-03-copy143 pos-01-03-copy144 pos-01-03-copy145 pos-01-03-copy146 pos-01-03-copy147 pos-01-03-copy148 pos-01-03-copy149 pos-01-03-copy150 pos-01-03-copy151 pos-01-03-copy152 pos-01-03-copy153 pos-01-03-copy154 pos-01-03-copy155 pos-01-03-copy156 pos-01-03-copy157 pos-01-03-copy158 pos-01-03-copy159 pos-01-03-copy160 pos-01-03-copy161 pos-01-03-copy162 pos-01-03-copy163 pos-01-03-copy164 pos-01-03-copy165 pos-01-03-copy166 pos-01-03-copy167 pos-01-03-copy168 pos-01-03-copy169 pos-01-03-copy170 pos-01-03-copy171 pos-01-03-copy172 pos-01-03-copy173 pos-01-03-copy174 pos-01-03-copy175 pos-01-03-copy176 pos-01-03-copy177 pos-01-03-copy178 pos-01-03-copy179 pos-01-03-copy180 pos-01-03-copy181 pos-01-03-copy182 pos-01-03-copy183 pos-01-03-copy184 pos-01-03-copy185 pos-01-03-copy186 pos-01-03-copy187 pos-01-03-copy188 pos-01-03-copy189 pos-01-03-copy190 pos-01-03-copy191 pos-01-03-copy192 pos-01-03-copy193 pos-01-03-copy194 pos-01-03-copy195 pos-01-03-copy196 pos-01-03-copy197 pos-01-03-copy198 - location
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
    (IS-NONGOAL pos-01-03) (IS-NONGOAL pos-01-03-copy1) (IS-NONGOAL pos-01-03-copy2) (IS-NONGOAL pos-01-03-copy3) (IS-NONGOAL pos-01-03-copy4) (IS-NONGOAL pos-01-03-copy5) (IS-NONGOAL pos-01-03-copy6) (IS-NONGOAL pos-01-03-copy7) (IS-NONGOAL pos-01-03-copy8) (IS-NONGOAL pos-01-03-copy9) (IS-NONGOAL pos-01-03-copy10) (IS-NONGOAL pos-01-03-copy11) (IS-NONGOAL pos-01-03-copy12) (IS-NONGOAL pos-01-03-copy13) (IS-NONGOAL pos-01-03-copy14) (IS-NONGOAL pos-01-03-copy15) (IS-NONGOAL pos-01-03-copy16) (IS-NONGOAL pos-01-03-copy17) (IS-NONGOAL pos-01-03-copy18) (IS-NONGOAL pos-01-03-copy19) (IS-NONGOAL pos-01-03-copy20) (IS-NONGOAL pos-01-03-copy21) (IS-NONGOAL pos-01-03-copy22) (IS-NONGOAL pos-01-03-copy23) (IS-NONGOAL pos-01-03-copy24) (IS-NONGOAL pos-01-03-copy25) (IS-NONGOAL pos-01-03-copy26) (IS-NONGOAL pos-01-03-copy27) (IS-NONGOAL pos-01-03-copy28) (IS-NONGOAL pos-01-03-copy29) (IS-NONGOAL pos-01-03-copy30) (IS-NONGOAL pos-01-03-copy31) (IS-NONGOAL pos-01-03-copy32) (IS-NONGOAL pos-01-03-copy33) (IS-NONGOAL pos-01-03-copy34) (IS-NONGOAL pos-01-03-copy35) (IS-NONGOAL pos-01-03-copy36) (IS-NONGOAL pos-01-03-copy37) (IS-NONGOAL pos-01-03-copy38) (IS-NONGOAL pos-01-03-copy39) (IS-NONGOAL pos-01-03-copy40) (IS-NONGOAL pos-01-03-copy41) (IS-NONGOAL pos-01-03-copy42) (IS-NONGOAL pos-01-03-copy43) (IS-NONGOAL pos-01-03-copy44) (IS-NONGOAL pos-01-03-copy45) (IS-NONGOAL pos-01-03-copy46) (IS-NONGOAL pos-01-03-copy47) (IS-NONGOAL pos-01-03-copy48) (IS-NONGOAL pos-01-03-copy49) (IS-NONGOAL pos-01-03-copy50) (IS-NONGOAL pos-01-03-copy51) (IS-NONGOAL pos-01-03-copy52) (IS-NONGOAL pos-01-03-copy53) (IS-NONGOAL pos-01-03-copy54) (IS-NONGOAL pos-01-03-copy55) (IS-NONGOAL pos-01-03-copy56) (IS-NONGOAL pos-01-03-copy57) (IS-NONGOAL pos-01-03-copy58) (IS-NONGOAL pos-01-03-copy59) (IS-NONGOAL pos-01-03-copy60) (IS-NONGOAL pos-01-03-copy61) (IS-NONGOAL pos-01-03-copy62) (IS-NONGOAL pos-01-03-copy63) (IS-NONGOAL pos-01-03-copy64) (IS-NONGOAL pos-01-03-copy65) (IS-NONGOAL pos-01-03-copy66) (IS-NONGOAL pos-01-03-copy67) (IS-NONGOAL pos-01-03-copy68) (IS-NONGOAL pos-01-03-copy69) (IS-NONGOAL pos-01-03-copy70) (IS-NONGOAL pos-01-03-copy71) (IS-NONGOAL pos-01-03-copy72) (IS-NONGOAL pos-01-03-copy73) (IS-NONGOAL pos-01-03-copy74) (IS-NONGOAL pos-01-03-copy75) (IS-NONGOAL pos-01-03-copy76) (IS-NONGOAL pos-01-03-copy77) (IS-NONGOAL pos-01-03-copy78) (IS-NONGOAL pos-01-03-copy79) (IS-NONGOAL pos-01-03-copy80) (IS-NONGOAL pos-01-03-copy81) (IS-NONGOAL pos-01-03-copy82) (IS-NONGOAL pos-01-03-copy83) (IS-NONGOAL pos-01-03-copy84) (IS-NONGOAL pos-01-03-copy85) (IS-NONGOAL pos-01-03-copy86) (IS-NONGOAL pos-01-03-copy87) (IS-NONGOAL pos-01-03-copy88) (IS-NONGOAL pos-01-03-copy89) (IS-NONGOAL pos-01-03-copy90) (IS-NONGOAL pos-01-03-copy91) (IS-NONGOAL pos-01-03-copy92) (IS-NONGOAL pos-01-03-copy93) (IS-NONGOAL pos-01-03-copy94) (IS-NONGOAL pos-01-03-copy95) (IS-NONGOAL pos-01-03-copy96) (IS-NONGOAL pos-01-03-copy97) (IS-NONGOAL pos-01-03-copy98) (IS-NONGOAL pos-01-03-copy99) (IS-NONGOAL pos-01-03-copy100) (IS-NONGOAL pos-01-03-copy101) (IS-NONGOAL pos-01-03-copy102) (IS-NONGOAL pos-01-03-copy103) (IS-NONGOAL pos-01-03-copy104) (IS-NONGOAL pos-01-03-copy105) (IS-NONGOAL pos-01-03-copy106) (IS-NONGOAL pos-01-03-copy107) (IS-NONGOAL pos-01-03-copy108) (IS-NONGOAL pos-01-03-copy109) (IS-NONGOAL pos-01-03-copy110) (IS-NONGOAL pos-01-03-copy111) (IS-NONGOAL pos-01-03-copy112) (IS-NONGOAL pos-01-03-copy113) (IS-NONGOAL pos-01-03-copy114) (IS-NONGOAL pos-01-03-copy115) (IS-NONGOAL pos-01-03-copy116) (IS-NONGOAL pos-01-03-copy117) (IS-NONGOAL pos-01-03-copy118) (IS-NONGOAL pos-01-03-copy119) (IS-NONGOAL pos-01-03-copy120) (IS-NONGOAL pos-01-03-copy121) (IS-NONGOAL pos-01-03-copy122) (IS-NONGOAL pos-01-03-copy123) (IS-NONGOAL pos-01-03-copy124) (IS-NONGOAL pos-01-03-copy125) (IS-NONGOAL pos-01-03-copy126) (IS-NONGOAL pos-01-03-copy127) (IS-NONGOAL pos-01-03-copy128) (IS-NONGOAL pos-01-03-copy129) (IS-NONGOAL pos-01-03-copy130) (IS-NONGOAL pos-01-03-copy131) (IS-NONGOAL pos-01-03-copy132) (IS-NONGOAL pos-01-03-copy133) (IS-NONGOAL pos-01-03-copy134) (IS-NONGOAL pos-01-03-copy135) (IS-NONGOAL pos-01-03-copy136) (IS-NONGOAL pos-01-03-copy137) (IS-NONGOAL pos-01-03-copy138) (IS-NONGOAL pos-01-03-copy139) (IS-NONGOAL pos-01-03-copy140) (IS-NONGOAL pos-01-03-copy141) (IS-NONGOAL pos-01-03-copy142) (IS-NONGOAL pos-01-03-copy143) (IS-NONGOAL pos-01-03-copy144) (IS-NONGOAL pos-01-03-copy145) (IS-NONGOAL pos-01-03-copy146) (IS-NONGOAL pos-01-03-copy147) (IS-NONGOAL pos-01-03-copy148) (IS-NONGOAL pos-01-03-copy149) (IS-NONGOAL pos-01-03-copy150) (IS-NONGOAL pos-01-03-copy151) (IS-NONGOAL pos-01-03-copy152) (IS-NONGOAL pos-01-03-copy153) (IS-NONGOAL pos-01-03-copy154) (IS-NONGOAL pos-01-03-copy155) (IS-NONGOAL pos-01-03-copy156) (IS-NONGOAL pos-01-03-copy157) (IS-NONGOAL pos-01-03-copy158) (IS-NONGOAL pos-01-03-copy159) (IS-NONGOAL pos-01-03-copy160) (IS-NONGOAL pos-01-03-copy161) (IS-NONGOAL pos-01-03-copy162) (IS-NONGOAL pos-01-03-copy163) (IS-NONGOAL pos-01-03-copy164) (IS-NONGOAL pos-01-03-copy165) (IS-NONGOAL pos-01-03-copy166) (IS-NONGOAL pos-01-03-copy167) (IS-NONGOAL pos-01-03-copy168) (IS-NONGOAL pos-01-03-copy169) (IS-NONGOAL pos-01-03-copy170) (IS-NONGOAL pos-01-03-copy171) (IS-NONGOAL pos-01-03-copy172) (IS-NONGOAL pos-01-03-copy173) (IS-NONGOAL pos-01-03-copy174) (IS-NONGOAL pos-01-03-copy175) (IS-NONGOAL pos-01-03-copy176) (IS-NONGOAL pos-01-03-copy177) (IS-NONGOAL pos-01-03-copy178) (IS-NONGOAL pos-01-03-copy179) (IS-NONGOAL pos-01-03-copy180) (IS-NONGOAL pos-01-03-copy181) (IS-NONGOAL pos-01-03-copy182) (IS-NONGOAL pos-01-03-copy183) (IS-NONGOAL pos-01-03-copy184) (IS-NONGOAL pos-01-03-copy185) (IS-NONGOAL pos-01-03-copy186) (IS-NONGOAL pos-01-03-copy187) (IS-NONGOAL pos-01-03-copy188) (IS-NONGOAL pos-01-03-copy189) (IS-NONGOAL pos-01-03-copy190) (IS-NONGOAL pos-01-03-copy191) (IS-NONGOAL pos-01-03-copy192) (IS-NONGOAL pos-01-03-copy193) (IS-NONGOAL pos-01-03-copy194) (IS-NONGOAL pos-01-03-copy195) (IS-NONGOAL pos-01-03-copy196) (IS-NONGOAL pos-01-03-copy197) (IS-NONGOAL pos-01-03-copy198)
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
    (clear pos-01-03) (clear pos-01-03-copy1) (clear pos-01-03-copy2) (clear pos-01-03-copy3) (clear pos-01-03-copy4) (clear pos-01-03-copy5) (clear pos-01-03-copy6) (clear pos-01-03-copy7) (clear pos-01-03-copy8) (clear pos-01-03-copy9) (clear pos-01-03-copy10) (clear pos-01-03-copy11) (clear pos-01-03-copy12) (clear pos-01-03-copy13) (clear pos-01-03-copy14) (clear pos-01-03-copy15) (clear pos-01-03-copy16) (clear pos-01-03-copy17) (clear pos-01-03-copy18) (clear pos-01-03-copy19) (clear pos-01-03-copy20) (clear pos-01-03-copy21) (clear pos-01-03-copy22) (clear pos-01-03-copy23) (clear pos-01-03-copy24) (clear pos-01-03-copy25) (clear pos-01-03-copy26) (clear pos-01-03-copy27) (clear pos-01-03-copy28) (clear pos-01-03-copy29) (clear pos-01-03-copy30) (clear pos-01-03-copy31) (clear pos-01-03-copy32) (clear pos-01-03-copy33) (clear pos-01-03-copy34) (clear pos-01-03-copy35) (clear pos-01-03-copy36) (clear pos-01-03-copy37) (clear pos-01-03-copy38) (clear pos-01-03-copy39) (clear pos-01-03-copy40) (clear pos-01-03-copy41) (clear pos-01-03-copy42) (clear pos-01-03-copy43) (clear pos-01-03-copy44) (clear pos-01-03-copy45) (clear pos-01-03-copy46) (clear pos-01-03-copy47) (clear pos-01-03-copy48) (clear pos-01-03-copy49) (clear pos-01-03-copy50) (clear pos-01-03-copy51) (clear pos-01-03-copy52) (clear pos-01-03-copy53) (clear pos-01-03-copy54) (clear pos-01-03-copy55) (clear pos-01-03-copy56) (clear pos-01-03-copy57) (clear pos-01-03-copy58) (clear pos-01-03-copy59) (clear pos-01-03-copy60) (clear pos-01-03-copy61) (clear pos-01-03-copy62) (clear pos-01-03-copy63) (clear pos-01-03-copy64) (clear pos-01-03-copy65) (clear pos-01-03-copy66) (clear pos-01-03-copy67) (clear pos-01-03-copy68) (clear pos-01-03-copy69) (clear pos-01-03-copy70) (clear pos-01-03-copy71) (clear pos-01-03-copy72) (clear pos-01-03-copy73) (clear pos-01-03-copy74) (clear pos-01-03-copy75) (clear pos-01-03-copy76) (clear pos-01-03-copy77) (clear pos-01-03-copy78) (clear pos-01-03-copy79) (clear pos-01-03-copy80) (clear pos-01-03-copy81) (clear pos-01-03-copy82) (clear pos-01-03-copy83) (clear pos-01-03-copy84) (clear pos-01-03-copy85) (clear pos-01-03-copy86) (clear pos-01-03-copy87) (clear pos-01-03-copy88) (clear pos-01-03-copy89) (clear pos-01-03-copy90) (clear pos-01-03-copy91) (clear pos-01-03-copy92) (clear pos-01-03-copy93) (clear pos-01-03-copy94) (clear pos-01-03-copy95) (clear pos-01-03-copy96) (clear pos-01-03-copy97) (clear pos-01-03-copy98) (clear pos-01-03-copy99) (clear pos-01-03-copy100) (clear pos-01-03-copy101) (clear pos-01-03-copy102) (clear pos-01-03-copy103) (clear pos-01-03-copy104) (clear pos-01-03-copy105) (clear pos-01-03-copy106) (clear pos-01-03-copy107) (clear pos-01-03-copy108) (clear pos-01-03-copy109) (clear pos-01-03-copy110) (clear pos-01-03-copy111) (clear pos-01-03-copy112) (clear pos-01-03-copy113) (clear pos-01-03-copy114) (clear pos-01-03-copy115) (clear pos-01-03-copy116) (clear pos-01-03-copy117) (clear pos-01-03-copy118) (clear pos-01-03-copy119) (clear pos-01-03-copy120) (clear pos-01-03-copy121) (clear pos-01-03-copy122) (clear pos-01-03-copy123) (clear pos-01-03-copy124) (clear pos-01-03-copy125) (clear pos-01-03-copy126) (clear pos-01-03-copy127) (clear pos-01-03-copy128) (clear pos-01-03-copy129) (clear pos-01-03-copy130) (clear pos-01-03-copy131) (clear pos-01-03-copy132) (clear pos-01-03-copy133) (clear pos-01-03-copy134) (clear pos-01-03-copy135) (clear pos-01-03-copy136) (clear pos-01-03-copy137) (clear pos-01-03-copy138) (clear pos-01-03-copy139) (clear pos-01-03-copy140) (clear pos-01-03-copy141) (clear pos-01-03-copy142) (clear pos-01-03-copy143) (clear pos-01-03-copy144) (clear pos-01-03-copy145) (clear pos-01-03-copy146) (clear pos-01-03-copy147) (clear pos-01-03-copy148) (clear pos-01-03-copy149) (clear pos-01-03-copy150) (clear pos-01-03-copy151) (clear pos-01-03-copy152) (clear pos-01-03-copy153) (clear pos-01-03-copy154) (clear pos-01-03-copy155) (clear pos-01-03-copy156) (clear pos-01-03-copy157) (clear pos-01-03-copy158) (clear pos-01-03-copy159) (clear pos-01-03-copy160) (clear pos-01-03-copy161) (clear pos-01-03-copy162) (clear pos-01-03-copy163) (clear pos-01-03-copy164) (clear pos-01-03-copy165) (clear pos-01-03-copy166) (clear pos-01-03-copy167) (clear pos-01-03-copy168) (clear pos-01-03-copy169) (clear pos-01-03-copy170) (clear pos-01-03-copy171) (clear pos-01-03-copy172) (clear pos-01-03-copy173) (clear pos-01-03-copy174) (clear pos-01-03-copy175) (clear pos-01-03-copy176) (clear pos-01-03-copy177) (clear pos-01-03-copy178) (clear pos-01-03-copy179) (clear pos-01-03-copy180) (clear pos-01-03-copy181) (clear pos-01-03-copy182) (clear pos-01-03-copy183) (clear pos-01-03-copy184) (clear pos-01-03-copy185) (clear pos-01-03-copy186) (clear pos-01-03-copy187) (clear pos-01-03-copy188) (clear pos-01-03-copy189) (clear pos-01-03-copy190) (clear pos-01-03-copy191) (clear pos-01-03-copy192) (clear pos-01-03-copy193) (clear pos-01-03-copy194) (clear pos-01-03-copy195) (clear pos-01-03-copy196) (clear pos-01-03-copy197) (clear pos-01-03-copy198)
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
