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
    pos-1-1 pos-1-1-copy1 pos-1-1-copy2 pos-1-1-copy3 pos-1-1-copy4 pos-1-1-copy5 pos-1-1-copy6 pos-1-1-copy7 pos-1-1-copy8 pos-1-1-copy9 pos-1-1-copy10 pos-1-1-copy11 pos-1-1-copy12 pos-1-1-copy13 pos-1-1-copy14 pos-1-1-copy15 pos-1-1-copy16 pos-1-1-copy17 pos-1-1-copy18 pos-1-1-copy19 pos-1-1-copy20 pos-1-1-copy21 pos-1-1-copy22 pos-1-1-copy23 pos-1-1-copy24 pos-1-1-copy25 pos-1-1-copy26 pos-1-1-copy27 pos-1-1-copy28 pos-1-1-copy29 pos-1-1-copy30 pos-1-1-copy31 pos-1-1-copy32 pos-1-1-copy33 pos-1-1-copy34 pos-1-1-copy35 pos-1-1-copy36 pos-1-1-copy37 pos-1-1-copy38 pos-1-1-copy39 pos-1-1-copy40 pos-1-1-copy41 pos-1-1-copy42 pos-1-1-copy43 pos-1-1-copy44 pos-1-1-copy45 pos-1-1-copy46 pos-1-1-copy47 pos-1-1-copy48 pos-1-1-copy49 pos-1-1-copy50 pos-1-1-copy51 pos-1-1-copy52 pos-1-1-copy53 pos-1-1-copy54 pos-1-1-copy55 pos-1-1-copy56 pos-1-1-copy57 pos-1-1-copy58 pos-1-1-copy59 pos-1-1-copy60 pos-1-1-copy61 pos-1-1-copy62 pos-1-1-copy63 pos-1-1-copy64 pos-1-1-copy65 pos-1-1-copy66 pos-1-1-copy67 pos-1-1-copy68 pos-1-1-copy69 pos-1-1-copy70 pos-1-1-copy71 pos-1-1-copy72 pos-1-1-copy73 pos-1-1-copy74 pos-1-1-copy75 pos-1-1-copy76 pos-1-1-copy77 pos-1-1-copy78 pos-1-1-copy79 pos-1-1-copy80 pos-1-1-copy81 pos-1-1-copy82 pos-1-1-copy83 pos-1-1-copy84 pos-1-1-copy85 pos-1-1-copy86 pos-1-1-copy87 pos-1-1-copy88 pos-1-1-copy89 pos-1-1-copy90 pos-1-1-copy91 pos-1-1-copy92 pos-1-1-copy93 pos-1-1-copy94 pos-1-1-copy95 pos-1-1-copy96 pos-1-1-copy97 pos-1-1-copy98 pos-1-1-copy99 pos-1-1-copy100 pos-1-1-copy101 pos-1-1-copy102 pos-1-1-copy103 pos-1-1-copy104 pos-1-1-copy105 pos-1-1-copy106 pos-1-1-copy107 pos-1-1-copy108 pos-1-1-copy109 pos-1-1-copy110 pos-1-1-copy111 pos-1-1-copy112 pos-1-1-copy113 pos-1-1-copy114 pos-1-1-copy115 pos-1-1-copy116 pos-1-1-copy117 pos-1-1-copy118 pos-1-1-copy119 pos-1-1-copy120 pos-1-1-copy121 pos-1-1-copy122 pos-1-1-copy123 pos-1-1-copy124 pos-1-1-copy125 pos-1-1-copy126 pos-1-1-copy127 pos-1-1-copy128 pos-1-1-copy129 pos-1-1-copy130 pos-1-1-copy131 pos-1-1-copy132 pos-1-1-copy133 pos-1-1-copy134 pos-1-1-copy135 pos-1-1-copy136 pos-1-1-copy137 pos-1-1-copy138 pos-1-1-copy139 pos-1-1-copy140 pos-1-1-copy141 pos-1-1-copy142 pos-1-1-copy143 pos-1-1-copy144 pos-1-1-copy145 pos-1-1-copy146 pos-1-1-copy147 pos-1-1-copy148 pos-1-1-copy149 pos-1-1-copy150 pos-1-1-copy151 pos-1-1-copy152 pos-1-1-copy153 pos-1-1-copy154 pos-1-1-copy155 pos-1-1-copy156 pos-1-1-copy157 pos-1-1-copy158 pos-1-1-copy159 pos-1-1-copy160 pos-1-1-copy161 pos-1-1-copy162 pos-1-1-copy163 pos-1-1-copy164 pos-1-1-copy165 pos-1-1-copy166 pos-1-1-copy167 pos-1-1-copy168 pos-1-1-copy169 pos-1-1-copy170 pos-1-1-copy171 pos-1-1-copy172 pos-1-1-copy173 pos-1-1-copy174 pos-1-1-copy175 pos-1-1-copy176 pos-1-1-copy177 pos-1-1-copy178 pos-1-1-copy179 pos-1-1-copy180 pos-1-1-copy181 pos-1-1-copy182 pos-1-1-copy183 pos-1-1-copy184 pos-1-1-copy185 pos-1-1-copy186 pos-1-1-copy187 pos-1-1-copy188 pos-1-1-copy189 pos-1-1-copy190 pos-1-1-copy191 pos-1-1-copy192 pos-1-1-copy193 pos-1-1-copy194 pos-1-1-copy195 pos-1-1-copy196 pos-1-1-copy197 pos-1-1-copy198 pos-1-1-copy199 pos-1-1-copy200 pos-1-1-copy201 pos-1-1-copy202 pos-1-1-copy203 pos-1-1-copy204 pos-1-1-copy205 pos-1-1-copy206 pos-1-1-copy207 pos-1-1-copy208 pos-1-1-copy209 pos-1-1-copy210 pos-1-1-copy211 pos-1-1-copy212 pos-1-1-copy213 pos-1-1-copy214 pos-1-1-copy215 pos-1-1-copy216 pos-1-1-copy217 pos-1-1-copy218 pos-1-1-copy219 pos-1-1-copy220 pos-1-1-copy221 pos-1-1-copy222 pos-1-1-copy223 pos-1-1-copy224 pos-1-1-copy225 pos-1-1-copy226 pos-1-1-copy227 pos-1-1-copy228 pos-1-1-copy229 pos-1-1-copy230 pos-1-1-copy231 pos-1-1-copy232 pos-1-1-copy233 pos-1-1-copy234 pos-1-1-copy235 pos-1-1-copy236 pos-1-1-copy237 pos-1-1-copy238 pos-1-1-copy239 pos-1-1-copy240 pos-1-1-copy241 pos-1-1-copy242 pos-1-1-copy243 pos-1-1-copy244 pos-1-1-copy245 pos-1-1-copy246 pos-1-1-copy247 pos-1-1-copy248 pos-1-1-copy249 pos-1-1-copy250 pos-1-1-copy251 pos-1-1-copy252 pos-1-1-copy253 pos-1-1-copy254 pos-1-1-copy255 pos-1-1-copy256 pos-1-1-copy257 pos-1-1-copy258 pos-1-1-copy259 pos-1-1-copy260 pos-1-1-copy261 pos-1-1-copy262 pos-1-1-copy263 pos-1-1-copy264 pos-1-1-copy265 pos-1-1-copy266 pos-1-1-copy267 pos-1-1-copy268 pos-1-1-copy269 pos-1-1-copy270 pos-1-1-copy271 pos-1-1-copy272 pos-1-1-copy273 pos-1-1-copy274 pos-1-1-copy275 pos-1-1-copy276 pos-1-1-copy277 pos-1-1-copy278 pos-1-1-copy279 pos-1-1-copy280 pos-1-1-copy281 pos-1-1-copy282 pos-1-1-copy283 pos-1-1-copy284 pos-1-1-copy285 pos-1-1-copy286 pos-1-1-copy287 pos-1-1-copy288 pos-1-1-copy289 pos-1-1-copy290 pos-1-1-copy291 pos-1-1-copy292 pos-1-1-copy293 pos-1-1-copy294 pos-1-1-copy295 pos-1-1-copy296 pos-1-1-copy297 pos-1-1-copy298 pos-1-1-copy299 pos-1-1-copy300 pos-1-1-copy301 pos-1-1-copy302 pos-1-1-copy303 pos-1-1-copy304 pos-1-1-copy305 pos-1-1-copy306 pos-1-1-copy307 pos-1-1-copy308 pos-1-1-copy309 pos-1-1-copy310 pos-1-1-copy311 pos-1-1-copy312 pos-1-1-copy313 pos-1-1-copy314 pos-1-1-copy315 pos-1-1-copy316 pos-1-1-copy317 pos-1-1-copy318 pos-1-1-copy319 pos-1-1-copy320 pos-1-1-copy321 pos-1-1-copy322 pos-1-1-copy323 pos-1-1-copy324 pos-1-1-copy325 pos-1-1-copy326 pos-1-1-copy327 pos-1-1-copy328 pos-1-1-copy329 pos-1-1-copy330 pos-1-1-copy331 pos-1-1-copy332 pos-1-1-copy333 pos-1-1-copy334 pos-1-1-copy335 pos-1-1-copy336 pos-1-1-copy337 pos-1-1-copy338 pos-1-1-copy339 pos-1-1-copy340 pos-1-1-copy341 pos-1-1-copy342 pos-1-1-copy343 pos-1-1-copy344 pos-1-1-copy345 pos-1-1-copy346 pos-1-1-copy347 pos-1-1-copy348 pos-1-1-copy349 pos-1-1-copy350 pos-1-1-copy351 pos-1-1-copy352 pos-1-1-copy353 pos-1-1-copy354 pos-1-1-copy355 pos-1-1-copy356 pos-1-1-copy357 pos-1-1-copy358 pos-1-1-copy359 pos-1-1-copy360 pos-1-1-copy361 pos-1-1-copy362 pos-1-1-copy363 pos-1-1-copy364 pos-1-1-copy365 pos-1-1-copy366 pos-1-1-copy367 pos-1-1-copy368 pos-1-1-copy369 pos-1-1-copy370 pos-1-1-copy371 pos-1-1-copy372 pos-1-1-copy373 pos-1-1-copy374 pos-1-1-copy375 pos-1-1-copy376 pos-1-1-copy377 pos-1-1-copy378 pos-1-1-copy379 pos-1-1-copy380 pos-1-1-copy381 pos-1-1-copy382 pos-1-1-copy383 pos-1-1-copy384 pos-1-1-copy385 pos-1-1-copy386 pos-1-1-copy387 pos-1-1-copy388 pos-1-1-copy389 pos-1-1-copy390 pos-1-1-copy391 pos-1-1-copy392 pos-1-1-copy393 pos-1-1-copy394 pos-1-1-copy395 pos-1-1-copy396 pos-1-1-copy397 pos-1-1-copy398 pos-1-1-copy399 pos-1-1-copy400 pos-1-1-copy401 pos-1-1-copy402 pos-1-1-copy403 pos-1-1-copy404 pos-1-1-copy405 pos-1-1-copy406 pos-1-1-copy407 pos-1-1-copy408 pos-1-1-copy409 pos-1-1-copy410 pos-1-1-copy411 pos-1-1-copy412 pos-1-1-copy413 pos-1-1-copy414 pos-1-1-copy415 pos-1-1-copy416 pos-1-1-copy417 pos-1-1-copy418 pos-1-1-copy419 pos-1-1-copy420 pos-1-1-copy421 pos-1-1-copy422 pos-1-1-copy423 pos-1-1-copy424 pos-1-1-copy425 pos-1-1-copy426 pos-1-1-copy427 pos-1-1-copy428 pos-1-1-copy429 pos-1-1-copy430 pos-1-1-copy431 pos-1-1-copy432 pos-1-1-copy433 pos-1-1-copy434 pos-1-1-copy435 pos-1-1-copy436 pos-1-1-copy437 pos-1-1-copy438 pos-1-1-copy439 pos-1-1-copy440 pos-1-1-copy441 pos-1-1-copy442 pos-1-1-copy443 pos-1-1-copy444 pos-1-1-copy445 pos-1-1-copy446 pos-1-1-copy447 pos-1-1-copy448 pos-1-1-copy449 pos-1-1-copy450 pos-1-1-copy451 pos-1-1-copy452 pos-1-1-copy453 pos-1-1-copy454 pos-1-1-copy455 pos-1-1-copy456 pos-1-1-copy457 pos-1-1-copy458 pos-1-1-copy459 pos-1-1-copy460 pos-1-1-copy461 pos-1-1-copy462 pos-1-1-copy463 pos-1-1-copy464 pos-1-1-copy465 pos-1-1-copy466 pos-1-1-copy467 pos-1-1-copy468 pos-1-1-copy469 pos-1-1-copy470 pos-1-1-copy471 pos-1-1-copy472 pos-1-1-copy473 pos-1-1-copy474 pos-1-1-copy475 pos-1-1-copy476 pos-1-1-copy477 pos-1-1-copy478 pos-1-1-copy479 pos-1-1-copy480 pos-1-1-copy481 pos-1-1-copy482 pos-1-1-copy483 pos-1-1-copy484 pos-1-1-copy485 pos-1-1-copy486 pos-1-1-copy487 pos-1-1-copy488 pos-1-1-copy489 pos-1-1-copy490 pos-1-1-copy491 pos-1-1-copy492 pos-1-1-copy493 pos-1-1-copy494 pos-1-1-copy495 pos-1-1-copy496 pos-1-1-copy497 pos-1-1-copy498 - location
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
    (IS-NONGOAL pos-1-1) (IS-NONGOAL pos-1-1-copy1) (IS-NONGOAL pos-1-1-copy2) (IS-NONGOAL pos-1-1-copy3) (IS-NONGOAL pos-1-1-copy4) (IS-NONGOAL pos-1-1-copy5) (IS-NONGOAL pos-1-1-copy6) (IS-NONGOAL pos-1-1-copy7) (IS-NONGOAL pos-1-1-copy8) (IS-NONGOAL pos-1-1-copy9) (IS-NONGOAL pos-1-1-copy10) (IS-NONGOAL pos-1-1-copy11) (IS-NONGOAL pos-1-1-copy12) (IS-NONGOAL pos-1-1-copy13) (IS-NONGOAL pos-1-1-copy14) (IS-NONGOAL pos-1-1-copy15) (IS-NONGOAL pos-1-1-copy16) (IS-NONGOAL pos-1-1-copy17) (IS-NONGOAL pos-1-1-copy18) (IS-NONGOAL pos-1-1-copy19) (IS-NONGOAL pos-1-1-copy20) (IS-NONGOAL pos-1-1-copy21) (IS-NONGOAL pos-1-1-copy22) (IS-NONGOAL pos-1-1-copy23) (IS-NONGOAL pos-1-1-copy24) (IS-NONGOAL pos-1-1-copy25) (IS-NONGOAL pos-1-1-copy26) (IS-NONGOAL pos-1-1-copy27) (IS-NONGOAL pos-1-1-copy28) (IS-NONGOAL pos-1-1-copy29) (IS-NONGOAL pos-1-1-copy30) (IS-NONGOAL pos-1-1-copy31) (IS-NONGOAL pos-1-1-copy32) (IS-NONGOAL pos-1-1-copy33) (IS-NONGOAL pos-1-1-copy34) (IS-NONGOAL pos-1-1-copy35) (IS-NONGOAL pos-1-1-copy36) (IS-NONGOAL pos-1-1-copy37) (IS-NONGOAL pos-1-1-copy38) (IS-NONGOAL pos-1-1-copy39) (IS-NONGOAL pos-1-1-copy40) (IS-NONGOAL pos-1-1-copy41) (IS-NONGOAL pos-1-1-copy42) (IS-NONGOAL pos-1-1-copy43) (IS-NONGOAL pos-1-1-copy44) (IS-NONGOAL pos-1-1-copy45) (IS-NONGOAL pos-1-1-copy46) (IS-NONGOAL pos-1-1-copy47) (IS-NONGOAL pos-1-1-copy48) (IS-NONGOAL pos-1-1-copy49) (IS-NONGOAL pos-1-1-copy50) (IS-NONGOAL pos-1-1-copy51) (IS-NONGOAL pos-1-1-copy52) (IS-NONGOAL pos-1-1-copy53) (IS-NONGOAL pos-1-1-copy54) (IS-NONGOAL pos-1-1-copy55) (IS-NONGOAL pos-1-1-copy56) (IS-NONGOAL pos-1-1-copy57) (IS-NONGOAL pos-1-1-copy58) (IS-NONGOAL pos-1-1-copy59) (IS-NONGOAL pos-1-1-copy60) (IS-NONGOAL pos-1-1-copy61) (IS-NONGOAL pos-1-1-copy62) (IS-NONGOAL pos-1-1-copy63) (IS-NONGOAL pos-1-1-copy64) (IS-NONGOAL pos-1-1-copy65) (IS-NONGOAL pos-1-1-copy66) (IS-NONGOAL pos-1-1-copy67) (IS-NONGOAL pos-1-1-copy68) (IS-NONGOAL pos-1-1-copy69) (IS-NONGOAL pos-1-1-copy70) (IS-NONGOAL pos-1-1-copy71) (IS-NONGOAL pos-1-1-copy72) (IS-NONGOAL pos-1-1-copy73) (IS-NONGOAL pos-1-1-copy74) (IS-NONGOAL pos-1-1-copy75) (IS-NONGOAL pos-1-1-copy76) (IS-NONGOAL pos-1-1-copy77) (IS-NONGOAL pos-1-1-copy78) (IS-NONGOAL pos-1-1-copy79) (IS-NONGOAL pos-1-1-copy80) (IS-NONGOAL pos-1-1-copy81) (IS-NONGOAL pos-1-1-copy82) (IS-NONGOAL pos-1-1-copy83) (IS-NONGOAL pos-1-1-copy84) (IS-NONGOAL pos-1-1-copy85) (IS-NONGOAL pos-1-1-copy86) (IS-NONGOAL pos-1-1-copy87) (IS-NONGOAL pos-1-1-copy88) (IS-NONGOAL pos-1-1-copy89) (IS-NONGOAL pos-1-1-copy90) (IS-NONGOAL pos-1-1-copy91) (IS-NONGOAL pos-1-1-copy92) (IS-NONGOAL pos-1-1-copy93) (IS-NONGOAL pos-1-1-copy94) (IS-NONGOAL pos-1-1-copy95) (IS-NONGOAL pos-1-1-copy96) (IS-NONGOAL pos-1-1-copy97) (IS-NONGOAL pos-1-1-copy98) (IS-NONGOAL pos-1-1-copy99) (IS-NONGOAL pos-1-1-copy100) (IS-NONGOAL pos-1-1-copy101) (IS-NONGOAL pos-1-1-copy102) (IS-NONGOAL pos-1-1-copy103) (IS-NONGOAL pos-1-1-copy104) (IS-NONGOAL pos-1-1-copy105) (IS-NONGOAL pos-1-1-copy106) (IS-NONGOAL pos-1-1-copy107) (IS-NONGOAL pos-1-1-copy108) (IS-NONGOAL pos-1-1-copy109) (IS-NONGOAL pos-1-1-copy110) (IS-NONGOAL pos-1-1-copy111) (IS-NONGOAL pos-1-1-copy112) (IS-NONGOAL pos-1-1-copy113) (IS-NONGOAL pos-1-1-copy114) (IS-NONGOAL pos-1-1-copy115) (IS-NONGOAL pos-1-1-copy116) (IS-NONGOAL pos-1-1-copy117) (IS-NONGOAL pos-1-1-copy118) (IS-NONGOAL pos-1-1-copy119) (IS-NONGOAL pos-1-1-copy120) (IS-NONGOAL pos-1-1-copy121) (IS-NONGOAL pos-1-1-copy122) (IS-NONGOAL pos-1-1-copy123) (IS-NONGOAL pos-1-1-copy124) (IS-NONGOAL pos-1-1-copy125) (IS-NONGOAL pos-1-1-copy126) (IS-NONGOAL pos-1-1-copy127) (IS-NONGOAL pos-1-1-copy128) (IS-NONGOAL pos-1-1-copy129) (IS-NONGOAL pos-1-1-copy130) (IS-NONGOAL pos-1-1-copy131) (IS-NONGOAL pos-1-1-copy132) (IS-NONGOAL pos-1-1-copy133) (IS-NONGOAL pos-1-1-copy134) (IS-NONGOAL pos-1-1-copy135) (IS-NONGOAL pos-1-1-copy136) (IS-NONGOAL pos-1-1-copy137) (IS-NONGOAL pos-1-1-copy138) (IS-NONGOAL pos-1-1-copy139) (IS-NONGOAL pos-1-1-copy140) (IS-NONGOAL pos-1-1-copy141) (IS-NONGOAL pos-1-1-copy142) (IS-NONGOAL pos-1-1-copy143) (IS-NONGOAL pos-1-1-copy144) (IS-NONGOAL pos-1-1-copy145) (IS-NONGOAL pos-1-1-copy146) (IS-NONGOAL pos-1-1-copy147) (IS-NONGOAL pos-1-1-copy148) (IS-NONGOAL pos-1-1-copy149) (IS-NONGOAL pos-1-1-copy150) (IS-NONGOAL pos-1-1-copy151) (IS-NONGOAL pos-1-1-copy152) (IS-NONGOAL pos-1-1-copy153) (IS-NONGOAL pos-1-1-copy154) (IS-NONGOAL pos-1-1-copy155) (IS-NONGOAL pos-1-1-copy156) (IS-NONGOAL pos-1-1-copy157) (IS-NONGOAL pos-1-1-copy158) (IS-NONGOAL pos-1-1-copy159) (IS-NONGOAL pos-1-1-copy160) (IS-NONGOAL pos-1-1-copy161) (IS-NONGOAL pos-1-1-copy162) (IS-NONGOAL pos-1-1-copy163) (IS-NONGOAL pos-1-1-copy164) (IS-NONGOAL pos-1-1-copy165) (IS-NONGOAL pos-1-1-copy166) (IS-NONGOAL pos-1-1-copy167) (IS-NONGOAL pos-1-1-copy168) (IS-NONGOAL pos-1-1-copy169) (IS-NONGOAL pos-1-1-copy170) (IS-NONGOAL pos-1-1-copy171) (IS-NONGOAL pos-1-1-copy172) (IS-NONGOAL pos-1-1-copy173) (IS-NONGOAL pos-1-1-copy174) (IS-NONGOAL pos-1-1-copy175) (IS-NONGOAL pos-1-1-copy176) (IS-NONGOAL pos-1-1-copy177) (IS-NONGOAL pos-1-1-copy178) (IS-NONGOAL pos-1-1-copy179) (IS-NONGOAL pos-1-1-copy180) (IS-NONGOAL pos-1-1-copy181) (IS-NONGOAL pos-1-1-copy182) (IS-NONGOAL pos-1-1-copy183) (IS-NONGOAL pos-1-1-copy184) (IS-NONGOAL pos-1-1-copy185) (IS-NONGOAL pos-1-1-copy186) (IS-NONGOAL pos-1-1-copy187) (IS-NONGOAL pos-1-1-copy188) (IS-NONGOAL pos-1-1-copy189) (IS-NONGOAL pos-1-1-copy190) (IS-NONGOAL pos-1-1-copy191) (IS-NONGOAL pos-1-1-copy192) (IS-NONGOAL pos-1-1-copy193) (IS-NONGOAL pos-1-1-copy194) (IS-NONGOAL pos-1-1-copy195) (IS-NONGOAL pos-1-1-copy196) (IS-NONGOAL pos-1-1-copy197) (IS-NONGOAL pos-1-1-copy198) (IS-NONGOAL pos-1-1-copy199) (IS-NONGOAL pos-1-1-copy200) (IS-NONGOAL pos-1-1-copy201) (IS-NONGOAL pos-1-1-copy202) (IS-NONGOAL pos-1-1-copy203) (IS-NONGOAL pos-1-1-copy204) (IS-NONGOAL pos-1-1-copy205) (IS-NONGOAL pos-1-1-copy206) (IS-NONGOAL pos-1-1-copy207) (IS-NONGOAL pos-1-1-copy208) (IS-NONGOAL pos-1-1-copy209) (IS-NONGOAL pos-1-1-copy210) (IS-NONGOAL pos-1-1-copy211) (IS-NONGOAL pos-1-1-copy212) (IS-NONGOAL pos-1-1-copy213) (IS-NONGOAL pos-1-1-copy214) (IS-NONGOAL pos-1-1-copy215) (IS-NONGOAL pos-1-1-copy216) (IS-NONGOAL pos-1-1-copy217) (IS-NONGOAL pos-1-1-copy218) (IS-NONGOAL pos-1-1-copy219) (IS-NONGOAL pos-1-1-copy220) (IS-NONGOAL pos-1-1-copy221) (IS-NONGOAL pos-1-1-copy222) (IS-NONGOAL pos-1-1-copy223) (IS-NONGOAL pos-1-1-copy224) (IS-NONGOAL pos-1-1-copy225) (IS-NONGOAL pos-1-1-copy226) (IS-NONGOAL pos-1-1-copy227) (IS-NONGOAL pos-1-1-copy228) (IS-NONGOAL pos-1-1-copy229) (IS-NONGOAL pos-1-1-copy230) (IS-NONGOAL pos-1-1-copy231) (IS-NONGOAL pos-1-1-copy232) (IS-NONGOAL pos-1-1-copy233) (IS-NONGOAL pos-1-1-copy234) (IS-NONGOAL pos-1-1-copy235) (IS-NONGOAL pos-1-1-copy236) (IS-NONGOAL pos-1-1-copy237) (IS-NONGOAL pos-1-1-copy238) (IS-NONGOAL pos-1-1-copy239) (IS-NONGOAL pos-1-1-copy240) (IS-NONGOAL pos-1-1-copy241) (IS-NONGOAL pos-1-1-copy242) (IS-NONGOAL pos-1-1-copy243) (IS-NONGOAL pos-1-1-copy244) (IS-NONGOAL pos-1-1-copy245) (IS-NONGOAL pos-1-1-copy246) (IS-NONGOAL pos-1-1-copy247) (IS-NONGOAL pos-1-1-copy248) (IS-NONGOAL pos-1-1-copy249) (IS-NONGOAL pos-1-1-copy250) (IS-NONGOAL pos-1-1-copy251) (IS-NONGOAL pos-1-1-copy252) (IS-NONGOAL pos-1-1-copy253) (IS-NONGOAL pos-1-1-copy254) (IS-NONGOAL pos-1-1-copy255) (IS-NONGOAL pos-1-1-copy256) (IS-NONGOAL pos-1-1-copy257) (IS-NONGOAL pos-1-1-copy258) (IS-NONGOAL pos-1-1-copy259) (IS-NONGOAL pos-1-1-copy260) (IS-NONGOAL pos-1-1-copy261) (IS-NONGOAL pos-1-1-copy262) (IS-NONGOAL pos-1-1-copy263) (IS-NONGOAL pos-1-1-copy264) (IS-NONGOAL pos-1-1-copy265) (IS-NONGOAL pos-1-1-copy266) (IS-NONGOAL pos-1-1-copy267) (IS-NONGOAL pos-1-1-copy268) (IS-NONGOAL pos-1-1-copy269) (IS-NONGOAL pos-1-1-copy270) (IS-NONGOAL pos-1-1-copy271) (IS-NONGOAL pos-1-1-copy272) (IS-NONGOAL pos-1-1-copy273) (IS-NONGOAL pos-1-1-copy274) (IS-NONGOAL pos-1-1-copy275) (IS-NONGOAL pos-1-1-copy276) (IS-NONGOAL pos-1-1-copy277) (IS-NONGOAL pos-1-1-copy278) (IS-NONGOAL pos-1-1-copy279) (IS-NONGOAL pos-1-1-copy280) (IS-NONGOAL pos-1-1-copy281) (IS-NONGOAL pos-1-1-copy282) (IS-NONGOAL pos-1-1-copy283) (IS-NONGOAL pos-1-1-copy284) (IS-NONGOAL pos-1-1-copy285) (IS-NONGOAL pos-1-1-copy286) (IS-NONGOAL pos-1-1-copy287) (IS-NONGOAL pos-1-1-copy288) (IS-NONGOAL pos-1-1-copy289) (IS-NONGOAL pos-1-1-copy290) (IS-NONGOAL pos-1-1-copy291) (IS-NONGOAL pos-1-1-copy292) (IS-NONGOAL pos-1-1-copy293) (IS-NONGOAL pos-1-1-copy294) (IS-NONGOAL pos-1-1-copy295) (IS-NONGOAL pos-1-1-copy296) (IS-NONGOAL pos-1-1-copy297) (IS-NONGOAL pos-1-1-copy298) (IS-NONGOAL pos-1-1-copy299) (IS-NONGOAL pos-1-1-copy300) (IS-NONGOAL pos-1-1-copy301) (IS-NONGOAL pos-1-1-copy302) (IS-NONGOAL pos-1-1-copy303) (IS-NONGOAL pos-1-1-copy304) (IS-NONGOAL pos-1-1-copy305) (IS-NONGOAL pos-1-1-copy306) (IS-NONGOAL pos-1-1-copy307) (IS-NONGOAL pos-1-1-copy308) (IS-NONGOAL pos-1-1-copy309) (IS-NONGOAL pos-1-1-copy310) (IS-NONGOAL pos-1-1-copy311) (IS-NONGOAL pos-1-1-copy312) (IS-NONGOAL pos-1-1-copy313) (IS-NONGOAL pos-1-1-copy314) (IS-NONGOAL pos-1-1-copy315) (IS-NONGOAL pos-1-1-copy316) (IS-NONGOAL pos-1-1-copy317) (IS-NONGOAL pos-1-1-copy318) (IS-NONGOAL pos-1-1-copy319) (IS-NONGOAL pos-1-1-copy320) (IS-NONGOAL pos-1-1-copy321) (IS-NONGOAL pos-1-1-copy322) (IS-NONGOAL pos-1-1-copy323) (IS-NONGOAL pos-1-1-copy324) (IS-NONGOAL pos-1-1-copy325) (IS-NONGOAL pos-1-1-copy326) (IS-NONGOAL pos-1-1-copy327) (IS-NONGOAL pos-1-1-copy328) (IS-NONGOAL pos-1-1-copy329) (IS-NONGOAL pos-1-1-copy330) (IS-NONGOAL pos-1-1-copy331) (IS-NONGOAL pos-1-1-copy332) (IS-NONGOAL pos-1-1-copy333) (IS-NONGOAL pos-1-1-copy334) (IS-NONGOAL pos-1-1-copy335) (IS-NONGOAL pos-1-1-copy336) (IS-NONGOAL pos-1-1-copy337) (IS-NONGOAL pos-1-1-copy338) (IS-NONGOAL pos-1-1-copy339) (IS-NONGOAL pos-1-1-copy340) (IS-NONGOAL pos-1-1-copy341) (IS-NONGOAL pos-1-1-copy342) (IS-NONGOAL pos-1-1-copy343) (IS-NONGOAL pos-1-1-copy344) (IS-NONGOAL pos-1-1-copy345) (IS-NONGOAL pos-1-1-copy346) (IS-NONGOAL pos-1-1-copy347) (IS-NONGOAL pos-1-1-copy348) (IS-NONGOAL pos-1-1-copy349) (IS-NONGOAL pos-1-1-copy350) (IS-NONGOAL pos-1-1-copy351) (IS-NONGOAL pos-1-1-copy352) (IS-NONGOAL pos-1-1-copy353) (IS-NONGOAL pos-1-1-copy354) (IS-NONGOAL pos-1-1-copy355) (IS-NONGOAL pos-1-1-copy356) (IS-NONGOAL pos-1-1-copy357) (IS-NONGOAL pos-1-1-copy358) (IS-NONGOAL pos-1-1-copy359) (IS-NONGOAL pos-1-1-copy360) (IS-NONGOAL pos-1-1-copy361) (IS-NONGOAL pos-1-1-copy362) (IS-NONGOAL pos-1-1-copy363) (IS-NONGOAL pos-1-1-copy364) (IS-NONGOAL pos-1-1-copy365) (IS-NONGOAL pos-1-1-copy366) (IS-NONGOAL pos-1-1-copy367) (IS-NONGOAL pos-1-1-copy368) (IS-NONGOAL pos-1-1-copy369) (IS-NONGOAL pos-1-1-copy370) (IS-NONGOAL pos-1-1-copy371) (IS-NONGOAL pos-1-1-copy372) (IS-NONGOAL pos-1-1-copy373) (IS-NONGOAL pos-1-1-copy374) (IS-NONGOAL pos-1-1-copy375) (IS-NONGOAL pos-1-1-copy376) (IS-NONGOAL pos-1-1-copy377) (IS-NONGOAL pos-1-1-copy378) (IS-NONGOAL pos-1-1-copy379) (IS-NONGOAL pos-1-1-copy380) (IS-NONGOAL pos-1-1-copy381) (IS-NONGOAL pos-1-1-copy382) (IS-NONGOAL pos-1-1-copy383) (IS-NONGOAL pos-1-1-copy384) (IS-NONGOAL pos-1-1-copy385) (IS-NONGOAL pos-1-1-copy386) (IS-NONGOAL pos-1-1-copy387) (IS-NONGOAL pos-1-1-copy388) (IS-NONGOAL pos-1-1-copy389) (IS-NONGOAL pos-1-1-copy390) (IS-NONGOAL pos-1-1-copy391) (IS-NONGOAL pos-1-1-copy392) (IS-NONGOAL pos-1-1-copy393) (IS-NONGOAL pos-1-1-copy394) (IS-NONGOAL pos-1-1-copy395) (IS-NONGOAL pos-1-1-copy396) (IS-NONGOAL pos-1-1-copy397) (IS-NONGOAL pos-1-1-copy398) (IS-NONGOAL pos-1-1-copy399) (IS-NONGOAL pos-1-1-copy400) (IS-NONGOAL pos-1-1-copy401) (IS-NONGOAL pos-1-1-copy402) (IS-NONGOAL pos-1-1-copy403) (IS-NONGOAL pos-1-1-copy404) (IS-NONGOAL pos-1-1-copy405) (IS-NONGOAL pos-1-1-copy406) (IS-NONGOAL pos-1-1-copy407) (IS-NONGOAL pos-1-1-copy408) (IS-NONGOAL pos-1-1-copy409) (IS-NONGOAL pos-1-1-copy410) (IS-NONGOAL pos-1-1-copy411) (IS-NONGOAL pos-1-1-copy412) (IS-NONGOAL pos-1-1-copy413) (IS-NONGOAL pos-1-1-copy414) (IS-NONGOAL pos-1-1-copy415) (IS-NONGOAL pos-1-1-copy416) (IS-NONGOAL pos-1-1-copy417) (IS-NONGOAL pos-1-1-copy418) (IS-NONGOAL pos-1-1-copy419) (IS-NONGOAL pos-1-1-copy420) (IS-NONGOAL pos-1-1-copy421) (IS-NONGOAL pos-1-1-copy422) (IS-NONGOAL pos-1-1-copy423) (IS-NONGOAL pos-1-1-copy424) (IS-NONGOAL pos-1-1-copy425) (IS-NONGOAL pos-1-1-copy426) (IS-NONGOAL pos-1-1-copy427) (IS-NONGOAL pos-1-1-copy428) (IS-NONGOAL pos-1-1-copy429) (IS-NONGOAL pos-1-1-copy430) (IS-NONGOAL pos-1-1-copy431) (IS-NONGOAL pos-1-1-copy432) (IS-NONGOAL pos-1-1-copy433) (IS-NONGOAL pos-1-1-copy434) (IS-NONGOAL pos-1-1-copy435) (IS-NONGOAL pos-1-1-copy436) (IS-NONGOAL pos-1-1-copy437) (IS-NONGOAL pos-1-1-copy438) (IS-NONGOAL pos-1-1-copy439) (IS-NONGOAL pos-1-1-copy440) (IS-NONGOAL pos-1-1-copy441) (IS-NONGOAL pos-1-1-copy442) (IS-NONGOAL pos-1-1-copy443) (IS-NONGOAL pos-1-1-copy444) (IS-NONGOAL pos-1-1-copy445) (IS-NONGOAL pos-1-1-copy446) (IS-NONGOAL pos-1-1-copy447) (IS-NONGOAL pos-1-1-copy448) (IS-NONGOAL pos-1-1-copy449) (IS-NONGOAL pos-1-1-copy450) (IS-NONGOAL pos-1-1-copy451) (IS-NONGOAL pos-1-1-copy452) (IS-NONGOAL pos-1-1-copy453) (IS-NONGOAL pos-1-1-copy454) (IS-NONGOAL pos-1-1-copy455) (IS-NONGOAL pos-1-1-copy456) (IS-NONGOAL pos-1-1-copy457) (IS-NONGOAL pos-1-1-copy458) (IS-NONGOAL pos-1-1-copy459) (IS-NONGOAL pos-1-1-copy460) (IS-NONGOAL pos-1-1-copy461) (IS-NONGOAL pos-1-1-copy462) (IS-NONGOAL pos-1-1-copy463) (IS-NONGOAL pos-1-1-copy464) (IS-NONGOAL pos-1-1-copy465) (IS-NONGOAL pos-1-1-copy466) (IS-NONGOAL pos-1-1-copy467) (IS-NONGOAL pos-1-1-copy468) (IS-NONGOAL pos-1-1-copy469) (IS-NONGOAL pos-1-1-copy470) (IS-NONGOAL pos-1-1-copy471) (IS-NONGOAL pos-1-1-copy472) (IS-NONGOAL pos-1-1-copy473) (IS-NONGOAL pos-1-1-copy474) (IS-NONGOAL pos-1-1-copy475) (IS-NONGOAL pos-1-1-copy476) (IS-NONGOAL pos-1-1-copy477) (IS-NONGOAL pos-1-1-copy478) (IS-NONGOAL pos-1-1-copy479) (IS-NONGOAL pos-1-1-copy480) (IS-NONGOAL pos-1-1-copy481) (IS-NONGOAL pos-1-1-copy482) (IS-NONGOAL pos-1-1-copy483) (IS-NONGOAL pos-1-1-copy484) (IS-NONGOAL pos-1-1-copy485) (IS-NONGOAL pos-1-1-copy486) (IS-NONGOAL pos-1-1-copy487) (IS-NONGOAL pos-1-1-copy488) (IS-NONGOAL pos-1-1-copy489) (IS-NONGOAL pos-1-1-copy490) (IS-NONGOAL pos-1-1-copy491) (IS-NONGOAL pos-1-1-copy492) (IS-NONGOAL pos-1-1-copy493) (IS-NONGOAL pos-1-1-copy494) (IS-NONGOAL pos-1-1-copy495) (IS-NONGOAL pos-1-1-copy496) (IS-NONGOAL pos-1-1-copy497) (IS-NONGOAL pos-1-1-copy498)
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
    (clear pos-1-1) (clear pos-1-1-copy1) (clear pos-1-1-copy2) (clear pos-1-1-copy3) (clear pos-1-1-copy4) (clear pos-1-1-copy5) (clear pos-1-1-copy6) (clear pos-1-1-copy7) (clear pos-1-1-copy8) (clear pos-1-1-copy9) (clear pos-1-1-copy10) (clear pos-1-1-copy11) (clear pos-1-1-copy12) (clear pos-1-1-copy13) (clear pos-1-1-copy14) (clear pos-1-1-copy15) (clear pos-1-1-copy16) (clear pos-1-1-copy17) (clear pos-1-1-copy18) (clear pos-1-1-copy19) (clear pos-1-1-copy20) (clear pos-1-1-copy21) (clear pos-1-1-copy22) (clear pos-1-1-copy23) (clear pos-1-1-copy24) (clear pos-1-1-copy25) (clear pos-1-1-copy26) (clear pos-1-1-copy27) (clear pos-1-1-copy28) (clear pos-1-1-copy29) (clear pos-1-1-copy30) (clear pos-1-1-copy31) (clear pos-1-1-copy32) (clear pos-1-1-copy33) (clear pos-1-1-copy34) (clear pos-1-1-copy35) (clear pos-1-1-copy36) (clear pos-1-1-copy37) (clear pos-1-1-copy38) (clear pos-1-1-copy39) (clear pos-1-1-copy40) (clear pos-1-1-copy41) (clear pos-1-1-copy42) (clear pos-1-1-copy43) (clear pos-1-1-copy44) (clear pos-1-1-copy45) (clear pos-1-1-copy46) (clear pos-1-1-copy47) (clear pos-1-1-copy48) (clear pos-1-1-copy49) (clear pos-1-1-copy50) (clear pos-1-1-copy51) (clear pos-1-1-copy52) (clear pos-1-1-copy53) (clear pos-1-1-copy54) (clear pos-1-1-copy55) (clear pos-1-1-copy56) (clear pos-1-1-copy57) (clear pos-1-1-copy58) (clear pos-1-1-copy59) (clear pos-1-1-copy60) (clear pos-1-1-copy61) (clear pos-1-1-copy62) (clear pos-1-1-copy63) (clear pos-1-1-copy64) (clear pos-1-1-copy65) (clear pos-1-1-copy66) (clear pos-1-1-copy67) (clear pos-1-1-copy68) (clear pos-1-1-copy69) (clear pos-1-1-copy70) (clear pos-1-1-copy71) (clear pos-1-1-copy72) (clear pos-1-1-copy73) (clear pos-1-1-copy74) (clear pos-1-1-copy75) (clear pos-1-1-copy76) (clear pos-1-1-copy77) (clear pos-1-1-copy78) (clear pos-1-1-copy79) (clear pos-1-1-copy80) (clear pos-1-1-copy81) (clear pos-1-1-copy82) (clear pos-1-1-copy83) (clear pos-1-1-copy84) (clear pos-1-1-copy85) (clear pos-1-1-copy86) (clear pos-1-1-copy87) (clear pos-1-1-copy88) (clear pos-1-1-copy89) (clear pos-1-1-copy90) (clear pos-1-1-copy91) (clear pos-1-1-copy92) (clear pos-1-1-copy93) (clear pos-1-1-copy94) (clear pos-1-1-copy95) (clear pos-1-1-copy96) (clear pos-1-1-copy97) (clear pos-1-1-copy98) (clear pos-1-1-copy99) (clear pos-1-1-copy100) (clear pos-1-1-copy101) (clear pos-1-1-copy102) (clear pos-1-1-copy103) (clear pos-1-1-copy104) (clear pos-1-1-copy105) (clear pos-1-1-copy106) (clear pos-1-1-copy107) (clear pos-1-1-copy108) (clear pos-1-1-copy109) (clear pos-1-1-copy110) (clear pos-1-1-copy111) (clear pos-1-1-copy112) (clear pos-1-1-copy113) (clear pos-1-1-copy114) (clear pos-1-1-copy115) (clear pos-1-1-copy116) (clear pos-1-1-copy117) (clear pos-1-1-copy118) (clear pos-1-1-copy119) (clear pos-1-1-copy120) (clear pos-1-1-copy121) (clear pos-1-1-copy122) (clear pos-1-1-copy123) (clear pos-1-1-copy124) (clear pos-1-1-copy125) (clear pos-1-1-copy126) (clear pos-1-1-copy127) (clear pos-1-1-copy128) (clear pos-1-1-copy129) (clear pos-1-1-copy130) (clear pos-1-1-copy131) (clear pos-1-1-copy132) (clear pos-1-1-copy133) (clear pos-1-1-copy134) (clear pos-1-1-copy135) (clear pos-1-1-copy136) (clear pos-1-1-copy137) (clear pos-1-1-copy138) (clear pos-1-1-copy139) (clear pos-1-1-copy140) (clear pos-1-1-copy141) (clear pos-1-1-copy142) (clear pos-1-1-copy143) (clear pos-1-1-copy144) (clear pos-1-1-copy145) (clear pos-1-1-copy146) (clear pos-1-1-copy147) (clear pos-1-1-copy148) (clear pos-1-1-copy149) (clear pos-1-1-copy150) (clear pos-1-1-copy151) (clear pos-1-1-copy152) (clear pos-1-1-copy153) (clear pos-1-1-copy154) (clear pos-1-1-copy155) (clear pos-1-1-copy156) (clear pos-1-1-copy157) (clear pos-1-1-copy158) (clear pos-1-1-copy159) (clear pos-1-1-copy160) (clear pos-1-1-copy161) (clear pos-1-1-copy162) (clear pos-1-1-copy163) (clear pos-1-1-copy164) (clear pos-1-1-copy165) (clear pos-1-1-copy166) (clear pos-1-1-copy167) (clear pos-1-1-copy168) (clear pos-1-1-copy169) (clear pos-1-1-copy170) (clear pos-1-1-copy171) (clear pos-1-1-copy172) (clear pos-1-1-copy173) (clear pos-1-1-copy174) (clear pos-1-1-copy175) (clear pos-1-1-copy176) (clear pos-1-1-copy177) (clear pos-1-1-copy178) (clear pos-1-1-copy179) (clear pos-1-1-copy180) (clear pos-1-1-copy181) (clear pos-1-1-copy182) (clear pos-1-1-copy183) (clear pos-1-1-copy184) (clear pos-1-1-copy185) (clear pos-1-1-copy186) (clear pos-1-1-copy187) (clear pos-1-1-copy188) (clear pos-1-1-copy189) (clear pos-1-1-copy190) (clear pos-1-1-copy191) (clear pos-1-1-copy192) (clear pos-1-1-copy193) (clear pos-1-1-copy194) (clear pos-1-1-copy195) (clear pos-1-1-copy196) (clear pos-1-1-copy197) (clear pos-1-1-copy198) (clear pos-1-1-copy199) (clear pos-1-1-copy200) (clear pos-1-1-copy201) (clear pos-1-1-copy202) (clear pos-1-1-copy203) (clear pos-1-1-copy204) (clear pos-1-1-copy205) (clear pos-1-1-copy206) (clear pos-1-1-copy207) (clear pos-1-1-copy208) (clear pos-1-1-copy209) (clear pos-1-1-copy210) (clear pos-1-1-copy211) (clear pos-1-1-copy212) (clear pos-1-1-copy213) (clear pos-1-1-copy214) (clear pos-1-1-copy215) (clear pos-1-1-copy216) (clear pos-1-1-copy217) (clear pos-1-1-copy218) (clear pos-1-1-copy219) (clear pos-1-1-copy220) (clear pos-1-1-copy221) (clear pos-1-1-copy222) (clear pos-1-1-copy223) (clear pos-1-1-copy224) (clear pos-1-1-copy225) (clear pos-1-1-copy226) (clear pos-1-1-copy227) (clear pos-1-1-copy228) (clear pos-1-1-copy229) (clear pos-1-1-copy230) (clear pos-1-1-copy231) (clear pos-1-1-copy232) (clear pos-1-1-copy233) (clear pos-1-1-copy234) (clear pos-1-1-copy235) (clear pos-1-1-copy236) (clear pos-1-1-copy237) (clear pos-1-1-copy238) (clear pos-1-1-copy239) (clear pos-1-1-copy240) (clear pos-1-1-copy241) (clear pos-1-1-copy242) (clear pos-1-1-copy243) (clear pos-1-1-copy244) (clear pos-1-1-copy245) (clear pos-1-1-copy246) (clear pos-1-1-copy247) (clear pos-1-1-copy248) (clear pos-1-1-copy249) (clear pos-1-1-copy250) (clear pos-1-1-copy251) (clear pos-1-1-copy252) (clear pos-1-1-copy253) (clear pos-1-1-copy254) (clear pos-1-1-copy255) (clear pos-1-1-copy256) (clear pos-1-1-copy257) (clear pos-1-1-copy258) (clear pos-1-1-copy259) (clear pos-1-1-copy260) (clear pos-1-1-copy261) (clear pos-1-1-copy262) (clear pos-1-1-copy263) (clear pos-1-1-copy264) (clear pos-1-1-copy265) (clear pos-1-1-copy266) (clear pos-1-1-copy267) (clear pos-1-1-copy268) (clear pos-1-1-copy269) (clear pos-1-1-copy270) (clear pos-1-1-copy271) (clear pos-1-1-copy272) (clear pos-1-1-copy273) (clear pos-1-1-copy274) (clear pos-1-1-copy275) (clear pos-1-1-copy276) (clear pos-1-1-copy277) (clear pos-1-1-copy278) (clear pos-1-1-copy279) (clear pos-1-1-copy280) (clear pos-1-1-copy281) (clear pos-1-1-copy282) (clear pos-1-1-copy283) (clear pos-1-1-copy284) (clear pos-1-1-copy285) (clear pos-1-1-copy286) (clear pos-1-1-copy287) (clear pos-1-1-copy288) (clear pos-1-1-copy289) (clear pos-1-1-copy290) (clear pos-1-1-copy291) (clear pos-1-1-copy292) (clear pos-1-1-copy293) (clear pos-1-1-copy294) (clear pos-1-1-copy295) (clear pos-1-1-copy296) (clear pos-1-1-copy297) (clear pos-1-1-copy298) (clear pos-1-1-copy299) (clear pos-1-1-copy300) (clear pos-1-1-copy301) (clear pos-1-1-copy302) (clear pos-1-1-copy303) (clear pos-1-1-copy304) (clear pos-1-1-copy305) (clear pos-1-1-copy306) (clear pos-1-1-copy307) (clear pos-1-1-copy308) (clear pos-1-1-copy309) (clear pos-1-1-copy310) (clear pos-1-1-copy311) (clear pos-1-1-copy312) (clear pos-1-1-copy313) (clear pos-1-1-copy314) (clear pos-1-1-copy315) (clear pos-1-1-copy316) (clear pos-1-1-copy317) (clear pos-1-1-copy318) (clear pos-1-1-copy319) (clear pos-1-1-copy320) (clear pos-1-1-copy321) (clear pos-1-1-copy322) (clear pos-1-1-copy323) (clear pos-1-1-copy324) (clear pos-1-1-copy325) (clear pos-1-1-copy326) (clear pos-1-1-copy327) (clear pos-1-1-copy328) (clear pos-1-1-copy329) (clear pos-1-1-copy330) (clear pos-1-1-copy331) (clear pos-1-1-copy332) (clear pos-1-1-copy333) (clear pos-1-1-copy334) (clear pos-1-1-copy335) (clear pos-1-1-copy336) (clear pos-1-1-copy337) (clear pos-1-1-copy338) (clear pos-1-1-copy339) (clear pos-1-1-copy340) (clear pos-1-1-copy341) (clear pos-1-1-copy342) (clear pos-1-1-copy343) (clear pos-1-1-copy344) (clear pos-1-1-copy345) (clear pos-1-1-copy346) (clear pos-1-1-copy347) (clear pos-1-1-copy348) (clear pos-1-1-copy349) (clear pos-1-1-copy350) (clear pos-1-1-copy351) (clear pos-1-1-copy352) (clear pos-1-1-copy353) (clear pos-1-1-copy354) (clear pos-1-1-copy355) (clear pos-1-1-copy356) (clear pos-1-1-copy357) (clear pos-1-1-copy358) (clear pos-1-1-copy359) (clear pos-1-1-copy360) (clear pos-1-1-copy361) (clear pos-1-1-copy362) (clear pos-1-1-copy363) (clear pos-1-1-copy364) (clear pos-1-1-copy365) (clear pos-1-1-copy366) (clear pos-1-1-copy367) (clear pos-1-1-copy368) (clear pos-1-1-copy369) (clear pos-1-1-copy370) (clear pos-1-1-copy371) (clear pos-1-1-copy372) (clear pos-1-1-copy373) (clear pos-1-1-copy374) (clear pos-1-1-copy375) (clear pos-1-1-copy376) (clear pos-1-1-copy377) (clear pos-1-1-copy378) (clear pos-1-1-copy379) (clear pos-1-1-copy380) (clear pos-1-1-copy381) (clear pos-1-1-copy382) (clear pos-1-1-copy383) (clear pos-1-1-copy384) (clear pos-1-1-copy385) (clear pos-1-1-copy386) (clear pos-1-1-copy387) (clear pos-1-1-copy388) (clear pos-1-1-copy389) (clear pos-1-1-copy390) (clear pos-1-1-copy391) (clear pos-1-1-copy392) (clear pos-1-1-copy393) (clear pos-1-1-copy394) (clear pos-1-1-copy395) (clear pos-1-1-copy396) (clear pos-1-1-copy397) (clear pos-1-1-copy398) (clear pos-1-1-copy399) (clear pos-1-1-copy400) (clear pos-1-1-copy401) (clear pos-1-1-copy402) (clear pos-1-1-copy403) (clear pos-1-1-copy404) (clear pos-1-1-copy405) (clear pos-1-1-copy406) (clear pos-1-1-copy407) (clear pos-1-1-copy408) (clear pos-1-1-copy409) (clear pos-1-1-copy410) (clear pos-1-1-copy411) (clear pos-1-1-copy412) (clear pos-1-1-copy413) (clear pos-1-1-copy414) (clear pos-1-1-copy415) (clear pos-1-1-copy416) (clear pos-1-1-copy417) (clear pos-1-1-copy418) (clear pos-1-1-copy419) (clear pos-1-1-copy420) (clear pos-1-1-copy421) (clear pos-1-1-copy422) (clear pos-1-1-copy423) (clear pos-1-1-copy424) (clear pos-1-1-copy425) (clear pos-1-1-copy426) (clear pos-1-1-copy427) (clear pos-1-1-copy428) (clear pos-1-1-copy429) (clear pos-1-1-copy430) (clear pos-1-1-copy431) (clear pos-1-1-copy432) (clear pos-1-1-copy433) (clear pos-1-1-copy434) (clear pos-1-1-copy435) (clear pos-1-1-copy436) (clear pos-1-1-copy437) (clear pos-1-1-copy438) (clear pos-1-1-copy439) (clear pos-1-1-copy440) (clear pos-1-1-copy441) (clear pos-1-1-copy442) (clear pos-1-1-copy443) (clear pos-1-1-copy444) (clear pos-1-1-copy445) (clear pos-1-1-copy446) (clear pos-1-1-copy447) (clear pos-1-1-copy448) (clear pos-1-1-copy449) (clear pos-1-1-copy450) (clear pos-1-1-copy451) (clear pos-1-1-copy452) (clear pos-1-1-copy453) (clear pos-1-1-copy454) (clear pos-1-1-copy455) (clear pos-1-1-copy456) (clear pos-1-1-copy457) (clear pos-1-1-copy458) (clear pos-1-1-copy459) (clear pos-1-1-copy460) (clear pos-1-1-copy461) (clear pos-1-1-copy462) (clear pos-1-1-copy463) (clear pos-1-1-copy464) (clear pos-1-1-copy465) (clear pos-1-1-copy466) (clear pos-1-1-copy467) (clear pos-1-1-copy468) (clear pos-1-1-copy469) (clear pos-1-1-copy470) (clear pos-1-1-copy471) (clear pos-1-1-copy472) (clear pos-1-1-copy473) (clear pos-1-1-copy474) (clear pos-1-1-copy475) (clear pos-1-1-copy476) (clear pos-1-1-copy477) (clear pos-1-1-copy478) (clear pos-1-1-copy479) (clear pos-1-1-copy480) (clear pos-1-1-copy481) (clear pos-1-1-copy482) (clear pos-1-1-copy483) (clear pos-1-1-copy484) (clear pos-1-1-copy485) (clear pos-1-1-copy486) (clear pos-1-1-copy487) (clear pos-1-1-copy488) (clear pos-1-1-copy489) (clear pos-1-1-copy490) (clear pos-1-1-copy491) (clear pos-1-1-copy492) (clear pos-1-1-copy493) (clear pos-1-1-copy494) (clear pos-1-1-copy495) (clear pos-1-1-copy496) (clear pos-1-1-copy497) (clear pos-1-1-copy498)
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
