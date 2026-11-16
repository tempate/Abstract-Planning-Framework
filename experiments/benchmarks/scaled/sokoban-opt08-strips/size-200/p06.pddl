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
    pos-1-1 pos-1-1-copy1 pos-1-1-copy2 pos-1-1-copy3 pos-1-1-copy4 pos-1-1-copy5 pos-1-1-copy6 pos-1-1-copy7 pos-1-1-copy8 pos-1-1-copy9 pos-1-1-copy10 pos-1-1-copy11 pos-1-1-copy12 pos-1-1-copy13 pos-1-1-copy14 pos-1-1-copy15 pos-1-1-copy16 pos-1-1-copy17 pos-1-1-copy18 pos-1-1-copy19 pos-1-1-copy20 pos-1-1-copy21 pos-1-1-copy22 pos-1-1-copy23 pos-1-1-copy24 pos-1-1-copy25 pos-1-1-copy26 pos-1-1-copy27 pos-1-1-copy28 pos-1-1-copy29 pos-1-1-copy30 pos-1-1-copy31 pos-1-1-copy32 pos-1-1-copy33 pos-1-1-copy34 pos-1-1-copy35 pos-1-1-copy36 pos-1-1-copy37 pos-1-1-copy38 pos-1-1-copy39 pos-1-1-copy40 pos-1-1-copy41 pos-1-1-copy42 pos-1-1-copy43 pos-1-1-copy44 pos-1-1-copy45 pos-1-1-copy46 pos-1-1-copy47 pos-1-1-copy48 pos-1-1-copy49 pos-1-1-copy50 pos-1-1-copy51 pos-1-1-copy52 pos-1-1-copy53 pos-1-1-copy54 pos-1-1-copy55 pos-1-1-copy56 pos-1-1-copy57 pos-1-1-copy58 pos-1-1-copy59 pos-1-1-copy60 pos-1-1-copy61 pos-1-1-copy62 pos-1-1-copy63 pos-1-1-copy64 pos-1-1-copy65 pos-1-1-copy66 pos-1-1-copy67 pos-1-1-copy68 pos-1-1-copy69 pos-1-1-copy70 pos-1-1-copy71 pos-1-1-copy72 pos-1-1-copy73 pos-1-1-copy74 pos-1-1-copy75 pos-1-1-copy76 pos-1-1-copy77 pos-1-1-copy78 pos-1-1-copy79 pos-1-1-copy80 pos-1-1-copy81 pos-1-1-copy82 pos-1-1-copy83 pos-1-1-copy84 pos-1-1-copy85 pos-1-1-copy86 pos-1-1-copy87 pos-1-1-copy88 pos-1-1-copy89 pos-1-1-copy90 pos-1-1-copy91 pos-1-1-copy92 pos-1-1-copy93 pos-1-1-copy94 pos-1-1-copy95 pos-1-1-copy96 pos-1-1-copy97 pos-1-1-copy98 pos-1-1-copy99 pos-1-1-copy100 pos-1-1-copy101 pos-1-1-copy102 pos-1-1-copy103 pos-1-1-copy104 pos-1-1-copy105 pos-1-1-copy106 pos-1-1-copy107 pos-1-1-copy108 pos-1-1-copy109 pos-1-1-copy110 pos-1-1-copy111 pos-1-1-copy112 pos-1-1-copy113 pos-1-1-copy114 pos-1-1-copy115 pos-1-1-copy116 pos-1-1-copy117 pos-1-1-copy118 pos-1-1-copy119 pos-1-1-copy120 pos-1-1-copy121 pos-1-1-copy122 pos-1-1-copy123 pos-1-1-copy124 pos-1-1-copy125 pos-1-1-copy126 pos-1-1-copy127 pos-1-1-copy128 pos-1-1-copy129 pos-1-1-copy130 pos-1-1-copy131 pos-1-1-copy132 pos-1-1-copy133 pos-1-1-copy134 pos-1-1-copy135 pos-1-1-copy136 pos-1-1-copy137 pos-1-1-copy138 pos-1-1-copy139 pos-1-1-copy140 pos-1-1-copy141 pos-1-1-copy142 pos-1-1-copy143 pos-1-1-copy144 pos-1-1-copy145 pos-1-1-copy146 pos-1-1-copy147 pos-1-1-copy148 pos-1-1-copy149 pos-1-1-copy150 pos-1-1-copy151 pos-1-1-copy152 pos-1-1-copy153 pos-1-1-copy154 pos-1-1-copy155 pos-1-1-copy156 pos-1-1-copy157 pos-1-1-copy158 pos-1-1-copy159 pos-1-1-copy160 pos-1-1-copy161 pos-1-1-copy162 pos-1-1-copy163 pos-1-1-copy164 pos-1-1-copy165 pos-1-1-copy166 pos-1-1-copy167 pos-1-1-copy168 pos-1-1-copy169 pos-1-1-copy170 pos-1-1-copy171 pos-1-1-copy172 pos-1-1-copy173 pos-1-1-copy174 pos-1-1-copy175 pos-1-1-copy176 pos-1-1-copy177 pos-1-1-copy178 pos-1-1-copy179 pos-1-1-copy180 pos-1-1-copy181 pos-1-1-copy182 pos-1-1-copy183 pos-1-1-copy184 pos-1-1-copy185 pos-1-1-copy186 pos-1-1-copy187 pos-1-1-copy188 pos-1-1-copy189 pos-1-1-copy190 pos-1-1-copy191 pos-1-1-copy192 pos-1-1-copy193 pos-1-1-copy194 pos-1-1-copy195 pos-1-1-copy196 pos-1-1-copy197 pos-1-1-copy198 - location
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
    (IS-NONGOAL pos-1-1) (IS-NONGOAL pos-1-1-copy1) (IS-NONGOAL pos-1-1-copy2) (IS-NONGOAL pos-1-1-copy3) (IS-NONGOAL pos-1-1-copy4) (IS-NONGOAL pos-1-1-copy5) (IS-NONGOAL pos-1-1-copy6) (IS-NONGOAL pos-1-1-copy7) (IS-NONGOAL pos-1-1-copy8) (IS-NONGOAL pos-1-1-copy9) (IS-NONGOAL pos-1-1-copy10) (IS-NONGOAL pos-1-1-copy11) (IS-NONGOAL pos-1-1-copy12) (IS-NONGOAL pos-1-1-copy13) (IS-NONGOAL pos-1-1-copy14) (IS-NONGOAL pos-1-1-copy15) (IS-NONGOAL pos-1-1-copy16) (IS-NONGOAL pos-1-1-copy17) (IS-NONGOAL pos-1-1-copy18) (IS-NONGOAL pos-1-1-copy19) (IS-NONGOAL pos-1-1-copy20) (IS-NONGOAL pos-1-1-copy21) (IS-NONGOAL pos-1-1-copy22) (IS-NONGOAL pos-1-1-copy23) (IS-NONGOAL pos-1-1-copy24) (IS-NONGOAL pos-1-1-copy25) (IS-NONGOAL pos-1-1-copy26) (IS-NONGOAL pos-1-1-copy27) (IS-NONGOAL pos-1-1-copy28) (IS-NONGOAL pos-1-1-copy29) (IS-NONGOAL pos-1-1-copy30) (IS-NONGOAL pos-1-1-copy31) (IS-NONGOAL pos-1-1-copy32) (IS-NONGOAL pos-1-1-copy33) (IS-NONGOAL pos-1-1-copy34) (IS-NONGOAL pos-1-1-copy35) (IS-NONGOAL pos-1-1-copy36) (IS-NONGOAL pos-1-1-copy37) (IS-NONGOAL pos-1-1-copy38) (IS-NONGOAL pos-1-1-copy39) (IS-NONGOAL pos-1-1-copy40) (IS-NONGOAL pos-1-1-copy41) (IS-NONGOAL pos-1-1-copy42) (IS-NONGOAL pos-1-1-copy43) (IS-NONGOAL pos-1-1-copy44) (IS-NONGOAL pos-1-1-copy45) (IS-NONGOAL pos-1-1-copy46) (IS-NONGOAL pos-1-1-copy47) (IS-NONGOAL pos-1-1-copy48) (IS-NONGOAL pos-1-1-copy49) (IS-NONGOAL pos-1-1-copy50) (IS-NONGOAL pos-1-1-copy51) (IS-NONGOAL pos-1-1-copy52) (IS-NONGOAL pos-1-1-copy53) (IS-NONGOAL pos-1-1-copy54) (IS-NONGOAL pos-1-1-copy55) (IS-NONGOAL pos-1-1-copy56) (IS-NONGOAL pos-1-1-copy57) (IS-NONGOAL pos-1-1-copy58) (IS-NONGOAL pos-1-1-copy59) (IS-NONGOAL pos-1-1-copy60) (IS-NONGOAL pos-1-1-copy61) (IS-NONGOAL pos-1-1-copy62) (IS-NONGOAL pos-1-1-copy63) (IS-NONGOAL pos-1-1-copy64) (IS-NONGOAL pos-1-1-copy65) (IS-NONGOAL pos-1-1-copy66) (IS-NONGOAL pos-1-1-copy67) (IS-NONGOAL pos-1-1-copy68) (IS-NONGOAL pos-1-1-copy69) (IS-NONGOAL pos-1-1-copy70) (IS-NONGOAL pos-1-1-copy71) (IS-NONGOAL pos-1-1-copy72) (IS-NONGOAL pos-1-1-copy73) (IS-NONGOAL pos-1-1-copy74) (IS-NONGOAL pos-1-1-copy75) (IS-NONGOAL pos-1-1-copy76) (IS-NONGOAL pos-1-1-copy77) (IS-NONGOAL pos-1-1-copy78) (IS-NONGOAL pos-1-1-copy79) (IS-NONGOAL pos-1-1-copy80) (IS-NONGOAL pos-1-1-copy81) (IS-NONGOAL pos-1-1-copy82) (IS-NONGOAL pos-1-1-copy83) (IS-NONGOAL pos-1-1-copy84) (IS-NONGOAL pos-1-1-copy85) (IS-NONGOAL pos-1-1-copy86) (IS-NONGOAL pos-1-1-copy87) (IS-NONGOAL pos-1-1-copy88) (IS-NONGOAL pos-1-1-copy89) (IS-NONGOAL pos-1-1-copy90) (IS-NONGOAL pos-1-1-copy91) (IS-NONGOAL pos-1-1-copy92) (IS-NONGOAL pos-1-1-copy93) (IS-NONGOAL pos-1-1-copy94) (IS-NONGOAL pos-1-1-copy95) (IS-NONGOAL pos-1-1-copy96) (IS-NONGOAL pos-1-1-copy97) (IS-NONGOAL pos-1-1-copy98) (IS-NONGOAL pos-1-1-copy99) (IS-NONGOAL pos-1-1-copy100) (IS-NONGOAL pos-1-1-copy101) (IS-NONGOAL pos-1-1-copy102) (IS-NONGOAL pos-1-1-copy103) (IS-NONGOAL pos-1-1-copy104) (IS-NONGOAL pos-1-1-copy105) (IS-NONGOAL pos-1-1-copy106) (IS-NONGOAL pos-1-1-copy107) (IS-NONGOAL pos-1-1-copy108) (IS-NONGOAL pos-1-1-copy109) (IS-NONGOAL pos-1-1-copy110) (IS-NONGOAL pos-1-1-copy111) (IS-NONGOAL pos-1-1-copy112) (IS-NONGOAL pos-1-1-copy113) (IS-NONGOAL pos-1-1-copy114) (IS-NONGOAL pos-1-1-copy115) (IS-NONGOAL pos-1-1-copy116) (IS-NONGOAL pos-1-1-copy117) (IS-NONGOAL pos-1-1-copy118) (IS-NONGOAL pos-1-1-copy119) (IS-NONGOAL pos-1-1-copy120) (IS-NONGOAL pos-1-1-copy121) (IS-NONGOAL pos-1-1-copy122) (IS-NONGOAL pos-1-1-copy123) (IS-NONGOAL pos-1-1-copy124) (IS-NONGOAL pos-1-1-copy125) (IS-NONGOAL pos-1-1-copy126) (IS-NONGOAL pos-1-1-copy127) (IS-NONGOAL pos-1-1-copy128) (IS-NONGOAL pos-1-1-copy129) (IS-NONGOAL pos-1-1-copy130) (IS-NONGOAL pos-1-1-copy131) (IS-NONGOAL pos-1-1-copy132) (IS-NONGOAL pos-1-1-copy133) (IS-NONGOAL pos-1-1-copy134) (IS-NONGOAL pos-1-1-copy135) (IS-NONGOAL pos-1-1-copy136) (IS-NONGOAL pos-1-1-copy137) (IS-NONGOAL pos-1-1-copy138) (IS-NONGOAL pos-1-1-copy139) (IS-NONGOAL pos-1-1-copy140) (IS-NONGOAL pos-1-1-copy141) (IS-NONGOAL pos-1-1-copy142) (IS-NONGOAL pos-1-1-copy143) (IS-NONGOAL pos-1-1-copy144) (IS-NONGOAL pos-1-1-copy145) (IS-NONGOAL pos-1-1-copy146) (IS-NONGOAL pos-1-1-copy147) (IS-NONGOAL pos-1-1-copy148) (IS-NONGOAL pos-1-1-copy149) (IS-NONGOAL pos-1-1-copy150) (IS-NONGOAL pos-1-1-copy151) (IS-NONGOAL pos-1-1-copy152) (IS-NONGOAL pos-1-1-copy153) (IS-NONGOAL pos-1-1-copy154) (IS-NONGOAL pos-1-1-copy155) (IS-NONGOAL pos-1-1-copy156) (IS-NONGOAL pos-1-1-copy157) (IS-NONGOAL pos-1-1-copy158) (IS-NONGOAL pos-1-1-copy159) (IS-NONGOAL pos-1-1-copy160) (IS-NONGOAL pos-1-1-copy161) (IS-NONGOAL pos-1-1-copy162) (IS-NONGOAL pos-1-1-copy163) (IS-NONGOAL pos-1-1-copy164) (IS-NONGOAL pos-1-1-copy165) (IS-NONGOAL pos-1-1-copy166) (IS-NONGOAL pos-1-1-copy167) (IS-NONGOAL pos-1-1-copy168) (IS-NONGOAL pos-1-1-copy169) (IS-NONGOAL pos-1-1-copy170) (IS-NONGOAL pos-1-1-copy171) (IS-NONGOAL pos-1-1-copy172) (IS-NONGOAL pos-1-1-copy173) (IS-NONGOAL pos-1-1-copy174) (IS-NONGOAL pos-1-1-copy175) (IS-NONGOAL pos-1-1-copy176) (IS-NONGOAL pos-1-1-copy177) (IS-NONGOAL pos-1-1-copy178) (IS-NONGOAL pos-1-1-copy179) (IS-NONGOAL pos-1-1-copy180) (IS-NONGOAL pos-1-1-copy181) (IS-NONGOAL pos-1-1-copy182) (IS-NONGOAL pos-1-1-copy183) (IS-NONGOAL pos-1-1-copy184) (IS-NONGOAL pos-1-1-copy185) (IS-NONGOAL pos-1-1-copy186) (IS-NONGOAL pos-1-1-copy187) (IS-NONGOAL pos-1-1-copy188) (IS-NONGOAL pos-1-1-copy189) (IS-NONGOAL pos-1-1-copy190) (IS-NONGOAL pos-1-1-copy191) (IS-NONGOAL pos-1-1-copy192) (IS-NONGOAL pos-1-1-copy193) (IS-NONGOAL pos-1-1-copy194) (IS-NONGOAL pos-1-1-copy195) (IS-NONGOAL pos-1-1-copy196) (IS-NONGOAL pos-1-1-copy197) (IS-NONGOAL pos-1-1-copy198)
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
    (clear pos-1-1) (clear pos-1-1-copy1) (clear pos-1-1-copy2) (clear pos-1-1-copy3) (clear pos-1-1-copy4) (clear pos-1-1-copy5) (clear pos-1-1-copy6) (clear pos-1-1-copy7) (clear pos-1-1-copy8) (clear pos-1-1-copy9) (clear pos-1-1-copy10) (clear pos-1-1-copy11) (clear pos-1-1-copy12) (clear pos-1-1-copy13) (clear pos-1-1-copy14) (clear pos-1-1-copy15) (clear pos-1-1-copy16) (clear pos-1-1-copy17) (clear pos-1-1-copy18) (clear pos-1-1-copy19) (clear pos-1-1-copy20) (clear pos-1-1-copy21) (clear pos-1-1-copy22) (clear pos-1-1-copy23) (clear pos-1-1-copy24) (clear pos-1-1-copy25) (clear pos-1-1-copy26) (clear pos-1-1-copy27) (clear pos-1-1-copy28) (clear pos-1-1-copy29) (clear pos-1-1-copy30) (clear pos-1-1-copy31) (clear pos-1-1-copy32) (clear pos-1-1-copy33) (clear pos-1-1-copy34) (clear pos-1-1-copy35) (clear pos-1-1-copy36) (clear pos-1-1-copy37) (clear pos-1-1-copy38) (clear pos-1-1-copy39) (clear pos-1-1-copy40) (clear pos-1-1-copy41) (clear pos-1-1-copy42) (clear pos-1-1-copy43) (clear pos-1-1-copy44) (clear pos-1-1-copy45) (clear pos-1-1-copy46) (clear pos-1-1-copy47) (clear pos-1-1-copy48) (clear pos-1-1-copy49) (clear pos-1-1-copy50) (clear pos-1-1-copy51) (clear pos-1-1-copy52) (clear pos-1-1-copy53) (clear pos-1-1-copy54) (clear pos-1-1-copy55) (clear pos-1-1-copy56) (clear pos-1-1-copy57) (clear pos-1-1-copy58) (clear pos-1-1-copy59) (clear pos-1-1-copy60) (clear pos-1-1-copy61) (clear pos-1-1-copy62) (clear pos-1-1-copy63) (clear pos-1-1-copy64) (clear pos-1-1-copy65) (clear pos-1-1-copy66) (clear pos-1-1-copy67) (clear pos-1-1-copy68) (clear pos-1-1-copy69) (clear pos-1-1-copy70) (clear pos-1-1-copy71) (clear pos-1-1-copy72) (clear pos-1-1-copy73) (clear pos-1-1-copy74) (clear pos-1-1-copy75) (clear pos-1-1-copy76) (clear pos-1-1-copy77) (clear pos-1-1-copy78) (clear pos-1-1-copy79) (clear pos-1-1-copy80) (clear pos-1-1-copy81) (clear pos-1-1-copy82) (clear pos-1-1-copy83) (clear pos-1-1-copy84) (clear pos-1-1-copy85) (clear pos-1-1-copy86) (clear pos-1-1-copy87) (clear pos-1-1-copy88) (clear pos-1-1-copy89) (clear pos-1-1-copy90) (clear pos-1-1-copy91) (clear pos-1-1-copy92) (clear pos-1-1-copy93) (clear pos-1-1-copy94) (clear pos-1-1-copy95) (clear pos-1-1-copy96) (clear pos-1-1-copy97) (clear pos-1-1-copy98) (clear pos-1-1-copy99) (clear pos-1-1-copy100) (clear pos-1-1-copy101) (clear pos-1-1-copy102) (clear pos-1-1-copy103) (clear pos-1-1-copy104) (clear pos-1-1-copy105) (clear pos-1-1-copy106) (clear pos-1-1-copy107) (clear pos-1-1-copy108) (clear pos-1-1-copy109) (clear pos-1-1-copy110) (clear pos-1-1-copy111) (clear pos-1-1-copy112) (clear pos-1-1-copy113) (clear pos-1-1-copy114) (clear pos-1-1-copy115) (clear pos-1-1-copy116) (clear pos-1-1-copy117) (clear pos-1-1-copy118) (clear pos-1-1-copy119) (clear pos-1-1-copy120) (clear pos-1-1-copy121) (clear pos-1-1-copy122) (clear pos-1-1-copy123) (clear pos-1-1-copy124) (clear pos-1-1-copy125) (clear pos-1-1-copy126) (clear pos-1-1-copy127) (clear pos-1-1-copy128) (clear pos-1-1-copy129) (clear pos-1-1-copy130) (clear pos-1-1-copy131) (clear pos-1-1-copy132) (clear pos-1-1-copy133) (clear pos-1-1-copy134) (clear pos-1-1-copy135) (clear pos-1-1-copy136) (clear pos-1-1-copy137) (clear pos-1-1-copy138) (clear pos-1-1-copy139) (clear pos-1-1-copy140) (clear pos-1-1-copy141) (clear pos-1-1-copy142) (clear pos-1-1-copy143) (clear pos-1-1-copy144) (clear pos-1-1-copy145) (clear pos-1-1-copy146) (clear pos-1-1-copy147) (clear pos-1-1-copy148) (clear pos-1-1-copy149) (clear pos-1-1-copy150) (clear pos-1-1-copy151) (clear pos-1-1-copy152) (clear pos-1-1-copy153) (clear pos-1-1-copy154) (clear pos-1-1-copy155) (clear pos-1-1-copy156) (clear pos-1-1-copy157) (clear pos-1-1-copy158) (clear pos-1-1-copy159) (clear pos-1-1-copy160) (clear pos-1-1-copy161) (clear pos-1-1-copy162) (clear pos-1-1-copy163) (clear pos-1-1-copy164) (clear pos-1-1-copy165) (clear pos-1-1-copy166) (clear pos-1-1-copy167) (clear pos-1-1-copy168) (clear pos-1-1-copy169) (clear pos-1-1-copy170) (clear pos-1-1-copy171) (clear pos-1-1-copy172) (clear pos-1-1-copy173) (clear pos-1-1-copy174) (clear pos-1-1-copy175) (clear pos-1-1-copy176) (clear pos-1-1-copy177) (clear pos-1-1-copy178) (clear pos-1-1-copy179) (clear pos-1-1-copy180) (clear pos-1-1-copy181) (clear pos-1-1-copy182) (clear pos-1-1-copy183) (clear pos-1-1-copy184) (clear pos-1-1-copy185) (clear pos-1-1-copy186) (clear pos-1-1-copy187) (clear pos-1-1-copy188) (clear pos-1-1-copy189) (clear pos-1-1-copy190) (clear pos-1-1-copy191) (clear pos-1-1-copy192) (clear pos-1-1-copy193) (clear pos-1-1-copy194) (clear pos-1-1-copy195) (clear pos-1-1-copy196) (clear pos-1-1-copy197) (clear pos-1-1-copy198)
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
