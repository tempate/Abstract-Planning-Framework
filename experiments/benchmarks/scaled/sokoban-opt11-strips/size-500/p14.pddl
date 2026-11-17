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
    pos-01-03 pos-01-03-copy1 pos-01-03-copy2 pos-01-03-copy3 pos-01-03-copy4 pos-01-03-copy5 pos-01-03-copy6 pos-01-03-copy7 pos-01-03-copy8 pos-01-03-copy9 pos-01-03-copy10 pos-01-03-copy11 pos-01-03-copy12 pos-01-03-copy13 pos-01-03-copy14 pos-01-03-copy15 pos-01-03-copy16 pos-01-03-copy17 pos-01-03-copy18 pos-01-03-copy19 pos-01-03-copy20 pos-01-03-copy21 pos-01-03-copy22 pos-01-03-copy23 pos-01-03-copy24 pos-01-03-copy25 pos-01-03-copy26 pos-01-03-copy27 pos-01-03-copy28 pos-01-03-copy29 pos-01-03-copy30 pos-01-03-copy31 pos-01-03-copy32 pos-01-03-copy33 pos-01-03-copy34 pos-01-03-copy35 pos-01-03-copy36 pos-01-03-copy37 pos-01-03-copy38 pos-01-03-copy39 pos-01-03-copy40 pos-01-03-copy41 pos-01-03-copy42 pos-01-03-copy43 pos-01-03-copy44 pos-01-03-copy45 pos-01-03-copy46 pos-01-03-copy47 pos-01-03-copy48 pos-01-03-copy49 pos-01-03-copy50 pos-01-03-copy51 pos-01-03-copy52 pos-01-03-copy53 pos-01-03-copy54 pos-01-03-copy55 pos-01-03-copy56 pos-01-03-copy57 pos-01-03-copy58 pos-01-03-copy59 pos-01-03-copy60 pos-01-03-copy61 pos-01-03-copy62 pos-01-03-copy63 pos-01-03-copy64 pos-01-03-copy65 pos-01-03-copy66 pos-01-03-copy67 pos-01-03-copy68 pos-01-03-copy69 pos-01-03-copy70 pos-01-03-copy71 pos-01-03-copy72 pos-01-03-copy73 pos-01-03-copy74 pos-01-03-copy75 pos-01-03-copy76 pos-01-03-copy77 pos-01-03-copy78 pos-01-03-copy79 pos-01-03-copy80 pos-01-03-copy81 pos-01-03-copy82 pos-01-03-copy83 pos-01-03-copy84 pos-01-03-copy85 pos-01-03-copy86 pos-01-03-copy87 pos-01-03-copy88 pos-01-03-copy89 pos-01-03-copy90 pos-01-03-copy91 pos-01-03-copy92 pos-01-03-copy93 pos-01-03-copy94 pos-01-03-copy95 pos-01-03-copy96 pos-01-03-copy97 pos-01-03-copy98 pos-01-03-copy99 pos-01-03-copy100 pos-01-03-copy101 pos-01-03-copy102 pos-01-03-copy103 pos-01-03-copy104 pos-01-03-copy105 pos-01-03-copy106 pos-01-03-copy107 pos-01-03-copy108 pos-01-03-copy109 pos-01-03-copy110 pos-01-03-copy111 pos-01-03-copy112 pos-01-03-copy113 pos-01-03-copy114 pos-01-03-copy115 pos-01-03-copy116 pos-01-03-copy117 pos-01-03-copy118 pos-01-03-copy119 pos-01-03-copy120 pos-01-03-copy121 pos-01-03-copy122 pos-01-03-copy123 pos-01-03-copy124 pos-01-03-copy125 pos-01-03-copy126 pos-01-03-copy127 pos-01-03-copy128 pos-01-03-copy129 pos-01-03-copy130 pos-01-03-copy131 pos-01-03-copy132 pos-01-03-copy133 pos-01-03-copy134 pos-01-03-copy135 pos-01-03-copy136 pos-01-03-copy137 pos-01-03-copy138 pos-01-03-copy139 pos-01-03-copy140 pos-01-03-copy141 pos-01-03-copy142 pos-01-03-copy143 pos-01-03-copy144 pos-01-03-copy145 pos-01-03-copy146 pos-01-03-copy147 pos-01-03-copy148 pos-01-03-copy149 pos-01-03-copy150 pos-01-03-copy151 pos-01-03-copy152 pos-01-03-copy153 pos-01-03-copy154 pos-01-03-copy155 pos-01-03-copy156 pos-01-03-copy157 pos-01-03-copy158 pos-01-03-copy159 pos-01-03-copy160 pos-01-03-copy161 pos-01-03-copy162 pos-01-03-copy163 pos-01-03-copy164 pos-01-03-copy165 pos-01-03-copy166 pos-01-03-copy167 pos-01-03-copy168 pos-01-03-copy169 pos-01-03-copy170 pos-01-03-copy171 pos-01-03-copy172 pos-01-03-copy173 pos-01-03-copy174 pos-01-03-copy175 pos-01-03-copy176 pos-01-03-copy177 pos-01-03-copy178 pos-01-03-copy179 pos-01-03-copy180 pos-01-03-copy181 pos-01-03-copy182 pos-01-03-copy183 pos-01-03-copy184 pos-01-03-copy185 pos-01-03-copy186 pos-01-03-copy187 pos-01-03-copy188 pos-01-03-copy189 pos-01-03-copy190 pos-01-03-copy191 pos-01-03-copy192 pos-01-03-copy193 pos-01-03-copy194 pos-01-03-copy195 pos-01-03-copy196 pos-01-03-copy197 pos-01-03-copy198 pos-01-03-copy199 pos-01-03-copy200 pos-01-03-copy201 pos-01-03-copy202 pos-01-03-copy203 pos-01-03-copy204 pos-01-03-copy205 pos-01-03-copy206 pos-01-03-copy207 pos-01-03-copy208 pos-01-03-copy209 pos-01-03-copy210 pos-01-03-copy211 pos-01-03-copy212 pos-01-03-copy213 pos-01-03-copy214 pos-01-03-copy215 pos-01-03-copy216 pos-01-03-copy217 pos-01-03-copy218 pos-01-03-copy219 pos-01-03-copy220 pos-01-03-copy221 pos-01-03-copy222 pos-01-03-copy223 pos-01-03-copy224 pos-01-03-copy225 pos-01-03-copy226 pos-01-03-copy227 pos-01-03-copy228 pos-01-03-copy229 pos-01-03-copy230 pos-01-03-copy231 pos-01-03-copy232 pos-01-03-copy233 pos-01-03-copy234 pos-01-03-copy235 pos-01-03-copy236 pos-01-03-copy237 pos-01-03-copy238 pos-01-03-copy239 pos-01-03-copy240 pos-01-03-copy241 pos-01-03-copy242 pos-01-03-copy243 pos-01-03-copy244 pos-01-03-copy245 pos-01-03-copy246 pos-01-03-copy247 pos-01-03-copy248 pos-01-03-copy249 pos-01-03-copy250 pos-01-03-copy251 pos-01-03-copy252 pos-01-03-copy253 pos-01-03-copy254 pos-01-03-copy255 pos-01-03-copy256 pos-01-03-copy257 pos-01-03-copy258 pos-01-03-copy259 pos-01-03-copy260 pos-01-03-copy261 pos-01-03-copy262 pos-01-03-copy263 pos-01-03-copy264 pos-01-03-copy265 pos-01-03-copy266 pos-01-03-copy267 pos-01-03-copy268 pos-01-03-copy269 pos-01-03-copy270 pos-01-03-copy271 pos-01-03-copy272 pos-01-03-copy273 pos-01-03-copy274 pos-01-03-copy275 pos-01-03-copy276 pos-01-03-copy277 pos-01-03-copy278 pos-01-03-copy279 pos-01-03-copy280 pos-01-03-copy281 pos-01-03-copy282 pos-01-03-copy283 pos-01-03-copy284 pos-01-03-copy285 pos-01-03-copy286 pos-01-03-copy287 pos-01-03-copy288 pos-01-03-copy289 pos-01-03-copy290 pos-01-03-copy291 pos-01-03-copy292 pos-01-03-copy293 pos-01-03-copy294 pos-01-03-copy295 pos-01-03-copy296 pos-01-03-copy297 pos-01-03-copy298 pos-01-03-copy299 pos-01-03-copy300 pos-01-03-copy301 pos-01-03-copy302 pos-01-03-copy303 pos-01-03-copy304 pos-01-03-copy305 pos-01-03-copy306 pos-01-03-copy307 pos-01-03-copy308 pos-01-03-copy309 pos-01-03-copy310 pos-01-03-copy311 pos-01-03-copy312 pos-01-03-copy313 pos-01-03-copy314 pos-01-03-copy315 pos-01-03-copy316 pos-01-03-copy317 pos-01-03-copy318 pos-01-03-copy319 pos-01-03-copy320 pos-01-03-copy321 pos-01-03-copy322 pos-01-03-copy323 pos-01-03-copy324 pos-01-03-copy325 pos-01-03-copy326 pos-01-03-copy327 pos-01-03-copy328 pos-01-03-copy329 pos-01-03-copy330 pos-01-03-copy331 pos-01-03-copy332 pos-01-03-copy333 pos-01-03-copy334 pos-01-03-copy335 pos-01-03-copy336 pos-01-03-copy337 pos-01-03-copy338 pos-01-03-copy339 pos-01-03-copy340 pos-01-03-copy341 pos-01-03-copy342 pos-01-03-copy343 pos-01-03-copy344 pos-01-03-copy345 pos-01-03-copy346 pos-01-03-copy347 pos-01-03-copy348 pos-01-03-copy349 pos-01-03-copy350 pos-01-03-copy351 pos-01-03-copy352 pos-01-03-copy353 pos-01-03-copy354 pos-01-03-copy355 pos-01-03-copy356 pos-01-03-copy357 pos-01-03-copy358 pos-01-03-copy359 pos-01-03-copy360 pos-01-03-copy361 pos-01-03-copy362 pos-01-03-copy363 pos-01-03-copy364 pos-01-03-copy365 pos-01-03-copy366 pos-01-03-copy367 pos-01-03-copy368 pos-01-03-copy369 pos-01-03-copy370 pos-01-03-copy371 pos-01-03-copy372 pos-01-03-copy373 pos-01-03-copy374 pos-01-03-copy375 pos-01-03-copy376 pos-01-03-copy377 pos-01-03-copy378 pos-01-03-copy379 pos-01-03-copy380 pos-01-03-copy381 pos-01-03-copy382 pos-01-03-copy383 pos-01-03-copy384 pos-01-03-copy385 pos-01-03-copy386 pos-01-03-copy387 pos-01-03-copy388 pos-01-03-copy389 pos-01-03-copy390 pos-01-03-copy391 pos-01-03-copy392 pos-01-03-copy393 pos-01-03-copy394 pos-01-03-copy395 pos-01-03-copy396 pos-01-03-copy397 pos-01-03-copy398 pos-01-03-copy399 pos-01-03-copy400 pos-01-03-copy401 pos-01-03-copy402 pos-01-03-copy403 pos-01-03-copy404 pos-01-03-copy405 pos-01-03-copy406 pos-01-03-copy407 pos-01-03-copy408 pos-01-03-copy409 pos-01-03-copy410 pos-01-03-copy411 pos-01-03-copy412 pos-01-03-copy413 pos-01-03-copy414 pos-01-03-copy415 pos-01-03-copy416 pos-01-03-copy417 pos-01-03-copy418 pos-01-03-copy419 pos-01-03-copy420 pos-01-03-copy421 pos-01-03-copy422 pos-01-03-copy423 pos-01-03-copy424 pos-01-03-copy425 pos-01-03-copy426 pos-01-03-copy427 pos-01-03-copy428 pos-01-03-copy429 pos-01-03-copy430 pos-01-03-copy431 pos-01-03-copy432 pos-01-03-copy433 pos-01-03-copy434 pos-01-03-copy435 pos-01-03-copy436 pos-01-03-copy437 pos-01-03-copy438 pos-01-03-copy439 pos-01-03-copy440 pos-01-03-copy441 pos-01-03-copy442 pos-01-03-copy443 pos-01-03-copy444 pos-01-03-copy445 pos-01-03-copy446 pos-01-03-copy447 pos-01-03-copy448 pos-01-03-copy449 pos-01-03-copy450 pos-01-03-copy451 pos-01-03-copy452 pos-01-03-copy453 pos-01-03-copy454 pos-01-03-copy455 pos-01-03-copy456 pos-01-03-copy457 pos-01-03-copy458 pos-01-03-copy459 pos-01-03-copy460 pos-01-03-copy461 pos-01-03-copy462 pos-01-03-copy463 pos-01-03-copy464 pos-01-03-copy465 pos-01-03-copy466 pos-01-03-copy467 pos-01-03-copy468 pos-01-03-copy469 pos-01-03-copy470 pos-01-03-copy471 pos-01-03-copy472 pos-01-03-copy473 pos-01-03-copy474 pos-01-03-copy475 pos-01-03-copy476 pos-01-03-copy477 pos-01-03-copy478 pos-01-03-copy479 pos-01-03-copy480 pos-01-03-copy481 pos-01-03-copy482 pos-01-03-copy483 pos-01-03-copy484 pos-01-03-copy485 pos-01-03-copy486 pos-01-03-copy487 pos-01-03-copy488 pos-01-03-copy489 pos-01-03-copy490 pos-01-03-copy491 pos-01-03-copy492 pos-01-03-copy493 pos-01-03-copy494 pos-01-03-copy495 pos-01-03-copy496 pos-01-03-copy497 pos-01-03-copy498 - location
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
    (IS-NONGOAL pos-01-03) (IS-NONGOAL pos-01-03-copy1) (IS-NONGOAL pos-01-03-copy2) (IS-NONGOAL pos-01-03-copy3) (IS-NONGOAL pos-01-03-copy4) (IS-NONGOAL pos-01-03-copy5) (IS-NONGOAL pos-01-03-copy6) (IS-NONGOAL pos-01-03-copy7) (IS-NONGOAL pos-01-03-copy8) (IS-NONGOAL pos-01-03-copy9) (IS-NONGOAL pos-01-03-copy10) (IS-NONGOAL pos-01-03-copy11) (IS-NONGOAL pos-01-03-copy12) (IS-NONGOAL pos-01-03-copy13) (IS-NONGOAL pos-01-03-copy14) (IS-NONGOAL pos-01-03-copy15) (IS-NONGOAL pos-01-03-copy16) (IS-NONGOAL pos-01-03-copy17) (IS-NONGOAL pos-01-03-copy18) (IS-NONGOAL pos-01-03-copy19) (IS-NONGOAL pos-01-03-copy20) (IS-NONGOAL pos-01-03-copy21) (IS-NONGOAL pos-01-03-copy22) (IS-NONGOAL pos-01-03-copy23) (IS-NONGOAL pos-01-03-copy24) (IS-NONGOAL pos-01-03-copy25) (IS-NONGOAL pos-01-03-copy26) (IS-NONGOAL pos-01-03-copy27) (IS-NONGOAL pos-01-03-copy28) (IS-NONGOAL pos-01-03-copy29) (IS-NONGOAL pos-01-03-copy30) (IS-NONGOAL pos-01-03-copy31) (IS-NONGOAL pos-01-03-copy32) (IS-NONGOAL pos-01-03-copy33) (IS-NONGOAL pos-01-03-copy34) (IS-NONGOAL pos-01-03-copy35) (IS-NONGOAL pos-01-03-copy36) (IS-NONGOAL pos-01-03-copy37) (IS-NONGOAL pos-01-03-copy38) (IS-NONGOAL pos-01-03-copy39) (IS-NONGOAL pos-01-03-copy40) (IS-NONGOAL pos-01-03-copy41) (IS-NONGOAL pos-01-03-copy42) (IS-NONGOAL pos-01-03-copy43) (IS-NONGOAL pos-01-03-copy44) (IS-NONGOAL pos-01-03-copy45) (IS-NONGOAL pos-01-03-copy46) (IS-NONGOAL pos-01-03-copy47) (IS-NONGOAL pos-01-03-copy48) (IS-NONGOAL pos-01-03-copy49) (IS-NONGOAL pos-01-03-copy50) (IS-NONGOAL pos-01-03-copy51) (IS-NONGOAL pos-01-03-copy52) (IS-NONGOAL pos-01-03-copy53) (IS-NONGOAL pos-01-03-copy54) (IS-NONGOAL pos-01-03-copy55) (IS-NONGOAL pos-01-03-copy56) (IS-NONGOAL pos-01-03-copy57) (IS-NONGOAL pos-01-03-copy58) (IS-NONGOAL pos-01-03-copy59) (IS-NONGOAL pos-01-03-copy60) (IS-NONGOAL pos-01-03-copy61) (IS-NONGOAL pos-01-03-copy62) (IS-NONGOAL pos-01-03-copy63) (IS-NONGOAL pos-01-03-copy64) (IS-NONGOAL pos-01-03-copy65) (IS-NONGOAL pos-01-03-copy66) (IS-NONGOAL pos-01-03-copy67) (IS-NONGOAL pos-01-03-copy68) (IS-NONGOAL pos-01-03-copy69) (IS-NONGOAL pos-01-03-copy70) (IS-NONGOAL pos-01-03-copy71) (IS-NONGOAL pos-01-03-copy72) (IS-NONGOAL pos-01-03-copy73) (IS-NONGOAL pos-01-03-copy74) (IS-NONGOAL pos-01-03-copy75) (IS-NONGOAL pos-01-03-copy76) (IS-NONGOAL pos-01-03-copy77) (IS-NONGOAL pos-01-03-copy78) (IS-NONGOAL pos-01-03-copy79) (IS-NONGOAL pos-01-03-copy80) (IS-NONGOAL pos-01-03-copy81) (IS-NONGOAL pos-01-03-copy82) (IS-NONGOAL pos-01-03-copy83) (IS-NONGOAL pos-01-03-copy84) (IS-NONGOAL pos-01-03-copy85) (IS-NONGOAL pos-01-03-copy86) (IS-NONGOAL pos-01-03-copy87) (IS-NONGOAL pos-01-03-copy88) (IS-NONGOAL pos-01-03-copy89) (IS-NONGOAL pos-01-03-copy90) (IS-NONGOAL pos-01-03-copy91) (IS-NONGOAL pos-01-03-copy92) (IS-NONGOAL pos-01-03-copy93) (IS-NONGOAL pos-01-03-copy94) (IS-NONGOAL pos-01-03-copy95) (IS-NONGOAL pos-01-03-copy96) (IS-NONGOAL pos-01-03-copy97) (IS-NONGOAL pos-01-03-copy98) (IS-NONGOAL pos-01-03-copy99) (IS-NONGOAL pos-01-03-copy100) (IS-NONGOAL pos-01-03-copy101) (IS-NONGOAL pos-01-03-copy102) (IS-NONGOAL pos-01-03-copy103) (IS-NONGOAL pos-01-03-copy104) (IS-NONGOAL pos-01-03-copy105) (IS-NONGOAL pos-01-03-copy106) (IS-NONGOAL pos-01-03-copy107) (IS-NONGOAL pos-01-03-copy108) (IS-NONGOAL pos-01-03-copy109) (IS-NONGOAL pos-01-03-copy110) (IS-NONGOAL pos-01-03-copy111) (IS-NONGOAL pos-01-03-copy112) (IS-NONGOAL pos-01-03-copy113) (IS-NONGOAL pos-01-03-copy114) (IS-NONGOAL pos-01-03-copy115) (IS-NONGOAL pos-01-03-copy116) (IS-NONGOAL pos-01-03-copy117) (IS-NONGOAL pos-01-03-copy118) (IS-NONGOAL pos-01-03-copy119) (IS-NONGOAL pos-01-03-copy120) (IS-NONGOAL pos-01-03-copy121) (IS-NONGOAL pos-01-03-copy122) (IS-NONGOAL pos-01-03-copy123) (IS-NONGOAL pos-01-03-copy124) (IS-NONGOAL pos-01-03-copy125) (IS-NONGOAL pos-01-03-copy126) (IS-NONGOAL pos-01-03-copy127) (IS-NONGOAL pos-01-03-copy128) (IS-NONGOAL pos-01-03-copy129) (IS-NONGOAL pos-01-03-copy130) (IS-NONGOAL pos-01-03-copy131) (IS-NONGOAL pos-01-03-copy132) (IS-NONGOAL pos-01-03-copy133) (IS-NONGOAL pos-01-03-copy134) (IS-NONGOAL pos-01-03-copy135) (IS-NONGOAL pos-01-03-copy136) (IS-NONGOAL pos-01-03-copy137) (IS-NONGOAL pos-01-03-copy138) (IS-NONGOAL pos-01-03-copy139) (IS-NONGOAL pos-01-03-copy140) (IS-NONGOAL pos-01-03-copy141) (IS-NONGOAL pos-01-03-copy142) (IS-NONGOAL pos-01-03-copy143) (IS-NONGOAL pos-01-03-copy144) (IS-NONGOAL pos-01-03-copy145) (IS-NONGOAL pos-01-03-copy146) (IS-NONGOAL pos-01-03-copy147) (IS-NONGOAL pos-01-03-copy148) (IS-NONGOAL pos-01-03-copy149) (IS-NONGOAL pos-01-03-copy150) (IS-NONGOAL pos-01-03-copy151) (IS-NONGOAL pos-01-03-copy152) (IS-NONGOAL pos-01-03-copy153) (IS-NONGOAL pos-01-03-copy154) (IS-NONGOAL pos-01-03-copy155) (IS-NONGOAL pos-01-03-copy156) (IS-NONGOAL pos-01-03-copy157) (IS-NONGOAL pos-01-03-copy158) (IS-NONGOAL pos-01-03-copy159) (IS-NONGOAL pos-01-03-copy160) (IS-NONGOAL pos-01-03-copy161) (IS-NONGOAL pos-01-03-copy162) (IS-NONGOAL pos-01-03-copy163) (IS-NONGOAL pos-01-03-copy164) (IS-NONGOAL pos-01-03-copy165) (IS-NONGOAL pos-01-03-copy166) (IS-NONGOAL pos-01-03-copy167) (IS-NONGOAL pos-01-03-copy168) (IS-NONGOAL pos-01-03-copy169) (IS-NONGOAL pos-01-03-copy170) (IS-NONGOAL pos-01-03-copy171) (IS-NONGOAL pos-01-03-copy172) (IS-NONGOAL pos-01-03-copy173) (IS-NONGOAL pos-01-03-copy174) (IS-NONGOAL pos-01-03-copy175) (IS-NONGOAL pos-01-03-copy176) (IS-NONGOAL pos-01-03-copy177) (IS-NONGOAL pos-01-03-copy178) (IS-NONGOAL pos-01-03-copy179) (IS-NONGOAL pos-01-03-copy180) (IS-NONGOAL pos-01-03-copy181) (IS-NONGOAL pos-01-03-copy182) (IS-NONGOAL pos-01-03-copy183) (IS-NONGOAL pos-01-03-copy184) (IS-NONGOAL pos-01-03-copy185) (IS-NONGOAL pos-01-03-copy186) (IS-NONGOAL pos-01-03-copy187) (IS-NONGOAL pos-01-03-copy188) (IS-NONGOAL pos-01-03-copy189) (IS-NONGOAL pos-01-03-copy190) (IS-NONGOAL pos-01-03-copy191) (IS-NONGOAL pos-01-03-copy192) (IS-NONGOAL pos-01-03-copy193) (IS-NONGOAL pos-01-03-copy194) (IS-NONGOAL pos-01-03-copy195) (IS-NONGOAL pos-01-03-copy196) (IS-NONGOAL pos-01-03-copy197) (IS-NONGOAL pos-01-03-copy198) (IS-NONGOAL pos-01-03-copy199) (IS-NONGOAL pos-01-03-copy200) (IS-NONGOAL pos-01-03-copy201) (IS-NONGOAL pos-01-03-copy202) (IS-NONGOAL pos-01-03-copy203) (IS-NONGOAL pos-01-03-copy204) (IS-NONGOAL pos-01-03-copy205) (IS-NONGOAL pos-01-03-copy206) (IS-NONGOAL pos-01-03-copy207) (IS-NONGOAL pos-01-03-copy208) (IS-NONGOAL pos-01-03-copy209) (IS-NONGOAL pos-01-03-copy210) (IS-NONGOAL pos-01-03-copy211) (IS-NONGOAL pos-01-03-copy212) (IS-NONGOAL pos-01-03-copy213) (IS-NONGOAL pos-01-03-copy214) (IS-NONGOAL pos-01-03-copy215) (IS-NONGOAL pos-01-03-copy216) (IS-NONGOAL pos-01-03-copy217) (IS-NONGOAL pos-01-03-copy218) (IS-NONGOAL pos-01-03-copy219) (IS-NONGOAL pos-01-03-copy220) (IS-NONGOAL pos-01-03-copy221) (IS-NONGOAL pos-01-03-copy222) (IS-NONGOAL pos-01-03-copy223) (IS-NONGOAL pos-01-03-copy224) (IS-NONGOAL pos-01-03-copy225) (IS-NONGOAL pos-01-03-copy226) (IS-NONGOAL pos-01-03-copy227) (IS-NONGOAL pos-01-03-copy228) (IS-NONGOAL pos-01-03-copy229) (IS-NONGOAL pos-01-03-copy230) (IS-NONGOAL pos-01-03-copy231) (IS-NONGOAL pos-01-03-copy232) (IS-NONGOAL pos-01-03-copy233) (IS-NONGOAL pos-01-03-copy234) (IS-NONGOAL pos-01-03-copy235) (IS-NONGOAL pos-01-03-copy236) (IS-NONGOAL pos-01-03-copy237) (IS-NONGOAL pos-01-03-copy238) (IS-NONGOAL pos-01-03-copy239) (IS-NONGOAL pos-01-03-copy240) (IS-NONGOAL pos-01-03-copy241) (IS-NONGOAL pos-01-03-copy242) (IS-NONGOAL pos-01-03-copy243) (IS-NONGOAL pos-01-03-copy244) (IS-NONGOAL pos-01-03-copy245) (IS-NONGOAL pos-01-03-copy246) (IS-NONGOAL pos-01-03-copy247) (IS-NONGOAL pos-01-03-copy248) (IS-NONGOAL pos-01-03-copy249) (IS-NONGOAL pos-01-03-copy250) (IS-NONGOAL pos-01-03-copy251) (IS-NONGOAL pos-01-03-copy252) (IS-NONGOAL pos-01-03-copy253) (IS-NONGOAL pos-01-03-copy254) (IS-NONGOAL pos-01-03-copy255) (IS-NONGOAL pos-01-03-copy256) (IS-NONGOAL pos-01-03-copy257) (IS-NONGOAL pos-01-03-copy258) (IS-NONGOAL pos-01-03-copy259) (IS-NONGOAL pos-01-03-copy260) (IS-NONGOAL pos-01-03-copy261) (IS-NONGOAL pos-01-03-copy262) (IS-NONGOAL pos-01-03-copy263) (IS-NONGOAL pos-01-03-copy264) (IS-NONGOAL pos-01-03-copy265) (IS-NONGOAL pos-01-03-copy266) (IS-NONGOAL pos-01-03-copy267) (IS-NONGOAL pos-01-03-copy268) (IS-NONGOAL pos-01-03-copy269) (IS-NONGOAL pos-01-03-copy270) (IS-NONGOAL pos-01-03-copy271) (IS-NONGOAL pos-01-03-copy272) (IS-NONGOAL pos-01-03-copy273) (IS-NONGOAL pos-01-03-copy274) (IS-NONGOAL pos-01-03-copy275) (IS-NONGOAL pos-01-03-copy276) (IS-NONGOAL pos-01-03-copy277) (IS-NONGOAL pos-01-03-copy278) (IS-NONGOAL pos-01-03-copy279) (IS-NONGOAL pos-01-03-copy280) (IS-NONGOAL pos-01-03-copy281) (IS-NONGOAL pos-01-03-copy282) (IS-NONGOAL pos-01-03-copy283) (IS-NONGOAL pos-01-03-copy284) (IS-NONGOAL pos-01-03-copy285) (IS-NONGOAL pos-01-03-copy286) (IS-NONGOAL pos-01-03-copy287) (IS-NONGOAL pos-01-03-copy288) (IS-NONGOAL pos-01-03-copy289) (IS-NONGOAL pos-01-03-copy290) (IS-NONGOAL pos-01-03-copy291) (IS-NONGOAL pos-01-03-copy292) (IS-NONGOAL pos-01-03-copy293) (IS-NONGOAL pos-01-03-copy294) (IS-NONGOAL pos-01-03-copy295) (IS-NONGOAL pos-01-03-copy296) (IS-NONGOAL pos-01-03-copy297) (IS-NONGOAL pos-01-03-copy298) (IS-NONGOAL pos-01-03-copy299) (IS-NONGOAL pos-01-03-copy300) (IS-NONGOAL pos-01-03-copy301) (IS-NONGOAL pos-01-03-copy302) (IS-NONGOAL pos-01-03-copy303) (IS-NONGOAL pos-01-03-copy304) (IS-NONGOAL pos-01-03-copy305) (IS-NONGOAL pos-01-03-copy306) (IS-NONGOAL pos-01-03-copy307) (IS-NONGOAL pos-01-03-copy308) (IS-NONGOAL pos-01-03-copy309) (IS-NONGOAL pos-01-03-copy310) (IS-NONGOAL pos-01-03-copy311) (IS-NONGOAL pos-01-03-copy312) (IS-NONGOAL pos-01-03-copy313) (IS-NONGOAL pos-01-03-copy314) (IS-NONGOAL pos-01-03-copy315) (IS-NONGOAL pos-01-03-copy316) (IS-NONGOAL pos-01-03-copy317) (IS-NONGOAL pos-01-03-copy318) (IS-NONGOAL pos-01-03-copy319) (IS-NONGOAL pos-01-03-copy320) (IS-NONGOAL pos-01-03-copy321) (IS-NONGOAL pos-01-03-copy322) (IS-NONGOAL pos-01-03-copy323) (IS-NONGOAL pos-01-03-copy324) (IS-NONGOAL pos-01-03-copy325) (IS-NONGOAL pos-01-03-copy326) (IS-NONGOAL pos-01-03-copy327) (IS-NONGOAL pos-01-03-copy328) (IS-NONGOAL pos-01-03-copy329) (IS-NONGOAL pos-01-03-copy330) (IS-NONGOAL pos-01-03-copy331) (IS-NONGOAL pos-01-03-copy332) (IS-NONGOAL pos-01-03-copy333) (IS-NONGOAL pos-01-03-copy334) (IS-NONGOAL pos-01-03-copy335) (IS-NONGOAL pos-01-03-copy336) (IS-NONGOAL pos-01-03-copy337) (IS-NONGOAL pos-01-03-copy338) (IS-NONGOAL pos-01-03-copy339) (IS-NONGOAL pos-01-03-copy340) (IS-NONGOAL pos-01-03-copy341) (IS-NONGOAL pos-01-03-copy342) (IS-NONGOAL pos-01-03-copy343) (IS-NONGOAL pos-01-03-copy344) (IS-NONGOAL pos-01-03-copy345) (IS-NONGOAL pos-01-03-copy346) (IS-NONGOAL pos-01-03-copy347) (IS-NONGOAL pos-01-03-copy348) (IS-NONGOAL pos-01-03-copy349) (IS-NONGOAL pos-01-03-copy350) (IS-NONGOAL pos-01-03-copy351) (IS-NONGOAL pos-01-03-copy352) (IS-NONGOAL pos-01-03-copy353) (IS-NONGOAL pos-01-03-copy354) (IS-NONGOAL pos-01-03-copy355) (IS-NONGOAL pos-01-03-copy356) (IS-NONGOAL pos-01-03-copy357) (IS-NONGOAL pos-01-03-copy358) (IS-NONGOAL pos-01-03-copy359) (IS-NONGOAL pos-01-03-copy360) (IS-NONGOAL pos-01-03-copy361) (IS-NONGOAL pos-01-03-copy362) (IS-NONGOAL pos-01-03-copy363) (IS-NONGOAL pos-01-03-copy364) (IS-NONGOAL pos-01-03-copy365) (IS-NONGOAL pos-01-03-copy366) (IS-NONGOAL pos-01-03-copy367) (IS-NONGOAL pos-01-03-copy368) (IS-NONGOAL pos-01-03-copy369) (IS-NONGOAL pos-01-03-copy370) (IS-NONGOAL pos-01-03-copy371) (IS-NONGOAL pos-01-03-copy372) (IS-NONGOAL pos-01-03-copy373) (IS-NONGOAL pos-01-03-copy374) (IS-NONGOAL pos-01-03-copy375) (IS-NONGOAL pos-01-03-copy376) (IS-NONGOAL pos-01-03-copy377) (IS-NONGOAL pos-01-03-copy378) (IS-NONGOAL pos-01-03-copy379) (IS-NONGOAL pos-01-03-copy380) (IS-NONGOAL pos-01-03-copy381) (IS-NONGOAL pos-01-03-copy382) (IS-NONGOAL pos-01-03-copy383) (IS-NONGOAL pos-01-03-copy384) (IS-NONGOAL pos-01-03-copy385) (IS-NONGOAL pos-01-03-copy386) (IS-NONGOAL pos-01-03-copy387) (IS-NONGOAL pos-01-03-copy388) (IS-NONGOAL pos-01-03-copy389) (IS-NONGOAL pos-01-03-copy390) (IS-NONGOAL pos-01-03-copy391) (IS-NONGOAL pos-01-03-copy392) (IS-NONGOAL pos-01-03-copy393) (IS-NONGOAL pos-01-03-copy394) (IS-NONGOAL pos-01-03-copy395) (IS-NONGOAL pos-01-03-copy396) (IS-NONGOAL pos-01-03-copy397) (IS-NONGOAL pos-01-03-copy398) (IS-NONGOAL pos-01-03-copy399) (IS-NONGOAL pos-01-03-copy400) (IS-NONGOAL pos-01-03-copy401) (IS-NONGOAL pos-01-03-copy402) (IS-NONGOAL pos-01-03-copy403) (IS-NONGOAL pos-01-03-copy404) (IS-NONGOAL pos-01-03-copy405) (IS-NONGOAL pos-01-03-copy406) (IS-NONGOAL pos-01-03-copy407) (IS-NONGOAL pos-01-03-copy408) (IS-NONGOAL pos-01-03-copy409) (IS-NONGOAL pos-01-03-copy410) (IS-NONGOAL pos-01-03-copy411) (IS-NONGOAL pos-01-03-copy412) (IS-NONGOAL pos-01-03-copy413) (IS-NONGOAL pos-01-03-copy414) (IS-NONGOAL pos-01-03-copy415) (IS-NONGOAL pos-01-03-copy416) (IS-NONGOAL pos-01-03-copy417) (IS-NONGOAL pos-01-03-copy418) (IS-NONGOAL pos-01-03-copy419) (IS-NONGOAL pos-01-03-copy420) (IS-NONGOAL pos-01-03-copy421) (IS-NONGOAL pos-01-03-copy422) (IS-NONGOAL pos-01-03-copy423) (IS-NONGOAL pos-01-03-copy424) (IS-NONGOAL pos-01-03-copy425) (IS-NONGOAL pos-01-03-copy426) (IS-NONGOAL pos-01-03-copy427) (IS-NONGOAL pos-01-03-copy428) (IS-NONGOAL pos-01-03-copy429) (IS-NONGOAL pos-01-03-copy430) (IS-NONGOAL pos-01-03-copy431) (IS-NONGOAL pos-01-03-copy432) (IS-NONGOAL pos-01-03-copy433) (IS-NONGOAL pos-01-03-copy434) (IS-NONGOAL pos-01-03-copy435) (IS-NONGOAL pos-01-03-copy436) (IS-NONGOAL pos-01-03-copy437) (IS-NONGOAL pos-01-03-copy438) (IS-NONGOAL pos-01-03-copy439) (IS-NONGOAL pos-01-03-copy440) (IS-NONGOAL pos-01-03-copy441) (IS-NONGOAL pos-01-03-copy442) (IS-NONGOAL pos-01-03-copy443) (IS-NONGOAL pos-01-03-copy444) (IS-NONGOAL pos-01-03-copy445) (IS-NONGOAL pos-01-03-copy446) (IS-NONGOAL pos-01-03-copy447) (IS-NONGOAL pos-01-03-copy448) (IS-NONGOAL pos-01-03-copy449) (IS-NONGOAL pos-01-03-copy450) (IS-NONGOAL pos-01-03-copy451) (IS-NONGOAL pos-01-03-copy452) (IS-NONGOAL pos-01-03-copy453) (IS-NONGOAL pos-01-03-copy454) (IS-NONGOAL pos-01-03-copy455) (IS-NONGOAL pos-01-03-copy456) (IS-NONGOAL pos-01-03-copy457) (IS-NONGOAL pos-01-03-copy458) (IS-NONGOAL pos-01-03-copy459) (IS-NONGOAL pos-01-03-copy460) (IS-NONGOAL pos-01-03-copy461) (IS-NONGOAL pos-01-03-copy462) (IS-NONGOAL pos-01-03-copy463) (IS-NONGOAL pos-01-03-copy464) (IS-NONGOAL pos-01-03-copy465) (IS-NONGOAL pos-01-03-copy466) (IS-NONGOAL pos-01-03-copy467) (IS-NONGOAL pos-01-03-copy468) (IS-NONGOAL pos-01-03-copy469) (IS-NONGOAL pos-01-03-copy470) (IS-NONGOAL pos-01-03-copy471) (IS-NONGOAL pos-01-03-copy472) (IS-NONGOAL pos-01-03-copy473) (IS-NONGOAL pos-01-03-copy474) (IS-NONGOAL pos-01-03-copy475) (IS-NONGOAL pos-01-03-copy476) (IS-NONGOAL pos-01-03-copy477) (IS-NONGOAL pos-01-03-copy478) (IS-NONGOAL pos-01-03-copy479) (IS-NONGOAL pos-01-03-copy480) (IS-NONGOAL pos-01-03-copy481) (IS-NONGOAL pos-01-03-copy482) (IS-NONGOAL pos-01-03-copy483) (IS-NONGOAL pos-01-03-copy484) (IS-NONGOAL pos-01-03-copy485) (IS-NONGOAL pos-01-03-copy486) (IS-NONGOAL pos-01-03-copy487) (IS-NONGOAL pos-01-03-copy488) (IS-NONGOAL pos-01-03-copy489) (IS-NONGOAL pos-01-03-copy490) (IS-NONGOAL pos-01-03-copy491) (IS-NONGOAL pos-01-03-copy492) (IS-NONGOAL pos-01-03-copy493) (IS-NONGOAL pos-01-03-copy494) (IS-NONGOAL pos-01-03-copy495) (IS-NONGOAL pos-01-03-copy496) (IS-NONGOAL pos-01-03-copy497) (IS-NONGOAL pos-01-03-copy498)
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
    (clear pos-01-03) (clear pos-01-03-copy1) (clear pos-01-03-copy2) (clear pos-01-03-copy3) (clear pos-01-03-copy4) (clear pos-01-03-copy5) (clear pos-01-03-copy6) (clear pos-01-03-copy7) (clear pos-01-03-copy8) (clear pos-01-03-copy9) (clear pos-01-03-copy10) (clear pos-01-03-copy11) (clear pos-01-03-copy12) (clear pos-01-03-copy13) (clear pos-01-03-copy14) (clear pos-01-03-copy15) (clear pos-01-03-copy16) (clear pos-01-03-copy17) (clear pos-01-03-copy18) (clear pos-01-03-copy19) (clear pos-01-03-copy20) (clear pos-01-03-copy21) (clear pos-01-03-copy22) (clear pos-01-03-copy23) (clear pos-01-03-copy24) (clear pos-01-03-copy25) (clear pos-01-03-copy26) (clear pos-01-03-copy27) (clear pos-01-03-copy28) (clear pos-01-03-copy29) (clear pos-01-03-copy30) (clear pos-01-03-copy31) (clear pos-01-03-copy32) (clear pos-01-03-copy33) (clear pos-01-03-copy34) (clear pos-01-03-copy35) (clear pos-01-03-copy36) (clear pos-01-03-copy37) (clear pos-01-03-copy38) (clear pos-01-03-copy39) (clear pos-01-03-copy40) (clear pos-01-03-copy41) (clear pos-01-03-copy42) (clear pos-01-03-copy43) (clear pos-01-03-copy44) (clear pos-01-03-copy45) (clear pos-01-03-copy46) (clear pos-01-03-copy47) (clear pos-01-03-copy48) (clear pos-01-03-copy49) (clear pos-01-03-copy50) (clear pos-01-03-copy51) (clear pos-01-03-copy52) (clear pos-01-03-copy53) (clear pos-01-03-copy54) (clear pos-01-03-copy55) (clear pos-01-03-copy56) (clear pos-01-03-copy57) (clear pos-01-03-copy58) (clear pos-01-03-copy59) (clear pos-01-03-copy60) (clear pos-01-03-copy61) (clear pos-01-03-copy62) (clear pos-01-03-copy63) (clear pos-01-03-copy64) (clear pos-01-03-copy65) (clear pos-01-03-copy66) (clear pos-01-03-copy67) (clear pos-01-03-copy68) (clear pos-01-03-copy69) (clear pos-01-03-copy70) (clear pos-01-03-copy71) (clear pos-01-03-copy72) (clear pos-01-03-copy73) (clear pos-01-03-copy74) (clear pos-01-03-copy75) (clear pos-01-03-copy76) (clear pos-01-03-copy77) (clear pos-01-03-copy78) (clear pos-01-03-copy79) (clear pos-01-03-copy80) (clear pos-01-03-copy81) (clear pos-01-03-copy82) (clear pos-01-03-copy83) (clear pos-01-03-copy84) (clear pos-01-03-copy85) (clear pos-01-03-copy86) (clear pos-01-03-copy87) (clear pos-01-03-copy88) (clear pos-01-03-copy89) (clear pos-01-03-copy90) (clear pos-01-03-copy91) (clear pos-01-03-copy92) (clear pos-01-03-copy93) (clear pos-01-03-copy94) (clear pos-01-03-copy95) (clear pos-01-03-copy96) (clear pos-01-03-copy97) (clear pos-01-03-copy98) (clear pos-01-03-copy99) (clear pos-01-03-copy100) (clear pos-01-03-copy101) (clear pos-01-03-copy102) (clear pos-01-03-copy103) (clear pos-01-03-copy104) (clear pos-01-03-copy105) (clear pos-01-03-copy106) (clear pos-01-03-copy107) (clear pos-01-03-copy108) (clear pos-01-03-copy109) (clear pos-01-03-copy110) (clear pos-01-03-copy111) (clear pos-01-03-copy112) (clear pos-01-03-copy113) (clear pos-01-03-copy114) (clear pos-01-03-copy115) (clear pos-01-03-copy116) (clear pos-01-03-copy117) (clear pos-01-03-copy118) (clear pos-01-03-copy119) (clear pos-01-03-copy120) (clear pos-01-03-copy121) (clear pos-01-03-copy122) (clear pos-01-03-copy123) (clear pos-01-03-copy124) (clear pos-01-03-copy125) (clear pos-01-03-copy126) (clear pos-01-03-copy127) (clear pos-01-03-copy128) (clear pos-01-03-copy129) (clear pos-01-03-copy130) (clear pos-01-03-copy131) (clear pos-01-03-copy132) (clear pos-01-03-copy133) (clear pos-01-03-copy134) (clear pos-01-03-copy135) (clear pos-01-03-copy136) (clear pos-01-03-copy137) (clear pos-01-03-copy138) (clear pos-01-03-copy139) (clear pos-01-03-copy140) (clear pos-01-03-copy141) (clear pos-01-03-copy142) (clear pos-01-03-copy143) (clear pos-01-03-copy144) (clear pos-01-03-copy145) (clear pos-01-03-copy146) (clear pos-01-03-copy147) (clear pos-01-03-copy148) (clear pos-01-03-copy149) (clear pos-01-03-copy150) (clear pos-01-03-copy151) (clear pos-01-03-copy152) (clear pos-01-03-copy153) (clear pos-01-03-copy154) (clear pos-01-03-copy155) (clear pos-01-03-copy156) (clear pos-01-03-copy157) (clear pos-01-03-copy158) (clear pos-01-03-copy159) (clear pos-01-03-copy160) (clear pos-01-03-copy161) (clear pos-01-03-copy162) (clear pos-01-03-copy163) (clear pos-01-03-copy164) (clear pos-01-03-copy165) (clear pos-01-03-copy166) (clear pos-01-03-copy167) (clear pos-01-03-copy168) (clear pos-01-03-copy169) (clear pos-01-03-copy170) (clear pos-01-03-copy171) (clear pos-01-03-copy172) (clear pos-01-03-copy173) (clear pos-01-03-copy174) (clear pos-01-03-copy175) (clear pos-01-03-copy176) (clear pos-01-03-copy177) (clear pos-01-03-copy178) (clear pos-01-03-copy179) (clear pos-01-03-copy180) (clear pos-01-03-copy181) (clear pos-01-03-copy182) (clear pos-01-03-copy183) (clear pos-01-03-copy184) (clear pos-01-03-copy185) (clear pos-01-03-copy186) (clear pos-01-03-copy187) (clear pos-01-03-copy188) (clear pos-01-03-copy189) (clear pos-01-03-copy190) (clear pos-01-03-copy191) (clear pos-01-03-copy192) (clear pos-01-03-copy193) (clear pos-01-03-copy194) (clear pos-01-03-copy195) (clear pos-01-03-copy196) (clear pos-01-03-copy197) (clear pos-01-03-copy198) (clear pos-01-03-copy199) (clear pos-01-03-copy200) (clear pos-01-03-copy201) (clear pos-01-03-copy202) (clear pos-01-03-copy203) (clear pos-01-03-copy204) (clear pos-01-03-copy205) (clear pos-01-03-copy206) (clear pos-01-03-copy207) (clear pos-01-03-copy208) (clear pos-01-03-copy209) (clear pos-01-03-copy210) (clear pos-01-03-copy211) (clear pos-01-03-copy212) (clear pos-01-03-copy213) (clear pos-01-03-copy214) (clear pos-01-03-copy215) (clear pos-01-03-copy216) (clear pos-01-03-copy217) (clear pos-01-03-copy218) (clear pos-01-03-copy219) (clear pos-01-03-copy220) (clear pos-01-03-copy221) (clear pos-01-03-copy222) (clear pos-01-03-copy223) (clear pos-01-03-copy224) (clear pos-01-03-copy225) (clear pos-01-03-copy226) (clear pos-01-03-copy227) (clear pos-01-03-copy228) (clear pos-01-03-copy229) (clear pos-01-03-copy230) (clear pos-01-03-copy231) (clear pos-01-03-copy232) (clear pos-01-03-copy233) (clear pos-01-03-copy234) (clear pos-01-03-copy235) (clear pos-01-03-copy236) (clear pos-01-03-copy237) (clear pos-01-03-copy238) (clear pos-01-03-copy239) (clear pos-01-03-copy240) (clear pos-01-03-copy241) (clear pos-01-03-copy242) (clear pos-01-03-copy243) (clear pos-01-03-copy244) (clear pos-01-03-copy245) (clear pos-01-03-copy246) (clear pos-01-03-copy247) (clear pos-01-03-copy248) (clear pos-01-03-copy249) (clear pos-01-03-copy250) (clear pos-01-03-copy251) (clear pos-01-03-copy252) (clear pos-01-03-copy253) (clear pos-01-03-copy254) (clear pos-01-03-copy255) (clear pos-01-03-copy256) (clear pos-01-03-copy257) (clear pos-01-03-copy258) (clear pos-01-03-copy259) (clear pos-01-03-copy260) (clear pos-01-03-copy261) (clear pos-01-03-copy262) (clear pos-01-03-copy263) (clear pos-01-03-copy264) (clear pos-01-03-copy265) (clear pos-01-03-copy266) (clear pos-01-03-copy267) (clear pos-01-03-copy268) (clear pos-01-03-copy269) (clear pos-01-03-copy270) (clear pos-01-03-copy271) (clear pos-01-03-copy272) (clear pos-01-03-copy273) (clear pos-01-03-copy274) (clear pos-01-03-copy275) (clear pos-01-03-copy276) (clear pos-01-03-copy277) (clear pos-01-03-copy278) (clear pos-01-03-copy279) (clear pos-01-03-copy280) (clear pos-01-03-copy281) (clear pos-01-03-copy282) (clear pos-01-03-copy283) (clear pos-01-03-copy284) (clear pos-01-03-copy285) (clear pos-01-03-copy286) (clear pos-01-03-copy287) (clear pos-01-03-copy288) (clear pos-01-03-copy289) (clear pos-01-03-copy290) (clear pos-01-03-copy291) (clear pos-01-03-copy292) (clear pos-01-03-copy293) (clear pos-01-03-copy294) (clear pos-01-03-copy295) (clear pos-01-03-copy296) (clear pos-01-03-copy297) (clear pos-01-03-copy298) (clear pos-01-03-copy299) (clear pos-01-03-copy300) (clear pos-01-03-copy301) (clear pos-01-03-copy302) (clear pos-01-03-copy303) (clear pos-01-03-copy304) (clear pos-01-03-copy305) (clear pos-01-03-copy306) (clear pos-01-03-copy307) (clear pos-01-03-copy308) (clear pos-01-03-copy309) (clear pos-01-03-copy310) (clear pos-01-03-copy311) (clear pos-01-03-copy312) (clear pos-01-03-copy313) (clear pos-01-03-copy314) (clear pos-01-03-copy315) (clear pos-01-03-copy316) (clear pos-01-03-copy317) (clear pos-01-03-copy318) (clear pos-01-03-copy319) (clear pos-01-03-copy320) (clear pos-01-03-copy321) (clear pos-01-03-copy322) (clear pos-01-03-copy323) (clear pos-01-03-copy324) (clear pos-01-03-copy325) (clear pos-01-03-copy326) (clear pos-01-03-copy327) (clear pos-01-03-copy328) (clear pos-01-03-copy329) (clear pos-01-03-copy330) (clear pos-01-03-copy331) (clear pos-01-03-copy332) (clear pos-01-03-copy333) (clear pos-01-03-copy334) (clear pos-01-03-copy335) (clear pos-01-03-copy336) (clear pos-01-03-copy337) (clear pos-01-03-copy338) (clear pos-01-03-copy339) (clear pos-01-03-copy340) (clear pos-01-03-copy341) (clear pos-01-03-copy342) (clear pos-01-03-copy343) (clear pos-01-03-copy344) (clear pos-01-03-copy345) (clear pos-01-03-copy346) (clear pos-01-03-copy347) (clear pos-01-03-copy348) (clear pos-01-03-copy349) (clear pos-01-03-copy350) (clear pos-01-03-copy351) (clear pos-01-03-copy352) (clear pos-01-03-copy353) (clear pos-01-03-copy354) (clear pos-01-03-copy355) (clear pos-01-03-copy356) (clear pos-01-03-copy357) (clear pos-01-03-copy358) (clear pos-01-03-copy359) (clear pos-01-03-copy360) (clear pos-01-03-copy361) (clear pos-01-03-copy362) (clear pos-01-03-copy363) (clear pos-01-03-copy364) (clear pos-01-03-copy365) (clear pos-01-03-copy366) (clear pos-01-03-copy367) (clear pos-01-03-copy368) (clear pos-01-03-copy369) (clear pos-01-03-copy370) (clear pos-01-03-copy371) (clear pos-01-03-copy372) (clear pos-01-03-copy373) (clear pos-01-03-copy374) (clear pos-01-03-copy375) (clear pos-01-03-copy376) (clear pos-01-03-copy377) (clear pos-01-03-copy378) (clear pos-01-03-copy379) (clear pos-01-03-copy380) (clear pos-01-03-copy381) (clear pos-01-03-copy382) (clear pos-01-03-copy383) (clear pos-01-03-copy384) (clear pos-01-03-copy385) (clear pos-01-03-copy386) (clear pos-01-03-copy387) (clear pos-01-03-copy388) (clear pos-01-03-copy389) (clear pos-01-03-copy390) (clear pos-01-03-copy391) (clear pos-01-03-copy392) (clear pos-01-03-copy393) (clear pos-01-03-copy394) (clear pos-01-03-copy395) (clear pos-01-03-copy396) (clear pos-01-03-copy397) (clear pos-01-03-copy398) (clear pos-01-03-copy399) (clear pos-01-03-copy400) (clear pos-01-03-copy401) (clear pos-01-03-copy402) (clear pos-01-03-copy403) (clear pos-01-03-copy404) (clear pos-01-03-copy405) (clear pos-01-03-copy406) (clear pos-01-03-copy407) (clear pos-01-03-copy408) (clear pos-01-03-copy409) (clear pos-01-03-copy410) (clear pos-01-03-copy411) (clear pos-01-03-copy412) (clear pos-01-03-copy413) (clear pos-01-03-copy414) (clear pos-01-03-copy415) (clear pos-01-03-copy416) (clear pos-01-03-copy417) (clear pos-01-03-copy418) (clear pos-01-03-copy419) (clear pos-01-03-copy420) (clear pos-01-03-copy421) (clear pos-01-03-copy422) (clear pos-01-03-copy423) (clear pos-01-03-copy424) (clear pos-01-03-copy425) (clear pos-01-03-copy426) (clear pos-01-03-copy427) (clear pos-01-03-copy428) (clear pos-01-03-copy429) (clear pos-01-03-copy430) (clear pos-01-03-copy431) (clear pos-01-03-copy432) (clear pos-01-03-copy433) (clear pos-01-03-copy434) (clear pos-01-03-copy435) (clear pos-01-03-copy436) (clear pos-01-03-copy437) (clear pos-01-03-copy438) (clear pos-01-03-copy439) (clear pos-01-03-copy440) (clear pos-01-03-copy441) (clear pos-01-03-copy442) (clear pos-01-03-copy443) (clear pos-01-03-copy444) (clear pos-01-03-copy445) (clear pos-01-03-copy446) (clear pos-01-03-copy447) (clear pos-01-03-copy448) (clear pos-01-03-copy449) (clear pos-01-03-copy450) (clear pos-01-03-copy451) (clear pos-01-03-copy452) (clear pos-01-03-copy453) (clear pos-01-03-copy454) (clear pos-01-03-copy455) (clear pos-01-03-copy456) (clear pos-01-03-copy457) (clear pos-01-03-copy458) (clear pos-01-03-copy459) (clear pos-01-03-copy460) (clear pos-01-03-copy461) (clear pos-01-03-copy462) (clear pos-01-03-copy463) (clear pos-01-03-copy464) (clear pos-01-03-copy465) (clear pos-01-03-copy466) (clear pos-01-03-copy467) (clear pos-01-03-copy468) (clear pos-01-03-copy469) (clear pos-01-03-copy470) (clear pos-01-03-copy471) (clear pos-01-03-copy472) (clear pos-01-03-copy473) (clear pos-01-03-copy474) (clear pos-01-03-copy475) (clear pos-01-03-copy476) (clear pos-01-03-copy477) (clear pos-01-03-copy478) (clear pos-01-03-copy479) (clear pos-01-03-copy480) (clear pos-01-03-copy481) (clear pos-01-03-copy482) (clear pos-01-03-copy483) (clear pos-01-03-copy484) (clear pos-01-03-copy485) (clear pos-01-03-copy486) (clear pos-01-03-copy487) (clear pos-01-03-copy488) (clear pos-01-03-copy489) (clear pos-01-03-copy490) (clear pos-01-03-copy491) (clear pos-01-03-copy492) (clear pos-01-03-copy493) (clear pos-01-03-copy494) (clear pos-01-03-copy495) (clear pos-01-03-copy496) (clear pos-01-03-copy497) (clear pos-01-03-copy498)
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
