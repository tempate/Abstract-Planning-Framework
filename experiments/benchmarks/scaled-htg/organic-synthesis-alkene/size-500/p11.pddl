; The variants of the Organic Synthesis domain were created by
; Dr. Russell Viirre, Hadi Qovaizi, and Prof. Mikhail Soutchanski.
;
; This work is licensed under a Creative Commons Attribution,
; NonCommercial, ShareAlike 3.0 Unported License.
;
; For further information, please access the following web page:
; https://www.cs.ryerson.ca/~mes/publications/
(define (problem Alkene_P11) (:domain Chemical)
(:objects
b071 - boron
c001 - carbon
c002 - carbon
c003 - carbon
c004 - carbon
c005 - carbon
c006 - carbon
c032 - carbon
c033 - carbon
c034 - carbon
c035 - carbon
c036 - carbon
c037 - carbon
c038 - carbon
c051 - carbon
c052 - carbon
c053 - carbon
c054 - carbon
c055 - carbon
h058 - hydrogen
h059 - hydrogen
h060 - hydrogen
h133 h133-copy1 h133-copy2 h133-copy3 h133-copy4 h133-copy5 h133-copy6 h133-copy7 h133-copy8 h133-copy9 h133-copy10 h133-copy11 h133-copy12 h133-copy13 h133-copy14 h133-copy15 h133-copy16 h133-copy17 h133-copy18 h133-copy19 h133-copy20 h133-copy21 h133-copy22 h133-copy23 h133-copy24 h133-copy25 h133-copy26 h133-copy27 h133-copy28 h133-copy29 h133-copy30 h133-copy31 h133-copy32 h133-copy33 h133-copy34 h133-copy35 h133-copy36 h133-copy37 h133-copy38 h133-copy39 h133-copy40 h133-copy41 h133-copy42 h133-copy43 h133-copy44 h133-copy45 h133-copy46 h133-copy47 h133-copy48 h133-copy49 h133-copy50 h133-copy51 h133-copy52 h133-copy53 h133-copy54 h133-copy55 h133-copy56 h133-copy57 h133-copy58 h133-copy59 h133-copy60 h133-copy61 h133-copy62 h133-copy63 h133-copy64 h133-copy65 h133-copy66 h133-copy67 h133-copy68 h133-copy69 h133-copy70 h133-copy71 h133-copy72 h133-copy73 h133-copy74 h133-copy75 h133-copy76 h133-copy77 h133-copy78 h133-copy79 h133-copy80 h133-copy81 h133-copy82 h133-copy83 h133-copy84 h133-copy85 h133-copy86 h133-copy87 h133-copy88 h133-copy89 h133-copy90 h133-copy91 h133-copy92 h133-copy93 h133-copy94 h133-copy95 h133-copy96 h133-copy97 h133-copy98 h133-copy99 h133-copy100 h133-copy101 h133-copy102 h133-copy103 h133-copy104 h133-copy105 h133-copy106 h133-copy107 h133-copy108 h133-copy109 h133-copy110 h133-copy111 h133-copy112 h133-copy113 h133-copy114 h133-copy115 h133-copy116 h133-copy117 h133-copy118 h133-copy119 h133-copy120 h133-copy121 h133-copy122 h133-copy123 h133-copy124 h133-copy125 h133-copy126 h133-copy127 h133-copy128 h133-copy129 h133-copy130 h133-copy131 h133-copy132 h133-copy133 h133-copy134 h133-copy135 h133-copy136 h133-copy137 h133-copy138 h133-copy139 h133-copy140 h133-copy141 h133-copy142 h133-copy143 h133-copy144 h133-copy145 h133-copy146 h133-copy147 h133-copy148 h133-copy149 h133-copy150 h133-copy151 h133-copy152 h133-copy153 h133-copy154 h133-copy155 h133-copy156 h133-copy157 h133-copy158 h133-copy159 h133-copy160 h133-copy161 h133-copy162 h133-copy163 h133-copy164 h133-copy165 h133-copy166 h133-copy167 h133-copy168 h133-copy169 h133-copy170 h133-copy171 h133-copy172 h133-copy173 h133-copy174 h133-copy175 h133-copy176 h133-copy177 h133-copy178 h133-copy179 h133-copy180 h133-copy181 h133-copy182 h133-copy183 h133-copy184 h133-copy185 h133-copy186 h133-copy187 h133-copy188 h133-copy189 h133-copy190 h133-copy191 h133-copy192 h133-copy193 h133-copy194 h133-copy195 h133-copy196 h133-copy197 h133-copy198 h133-copy199 h133-copy200 h133-copy201 h133-copy202 h133-copy203 h133-copy204 h133-copy205 h133-copy206 h133-copy207 h133-copy208 h133-copy209 h133-copy210 h133-copy211 h133-copy212 h133-copy213 h133-copy214 h133-copy215 h133-copy216 h133-copy217 h133-copy218 h133-copy219 h133-copy220 h133-copy221 h133-copy222 h133-copy223 h133-copy224 h133-copy225 h133-copy226 h133-copy227 h133-copy228 h133-copy229 h133-copy230 h133-copy231 h133-copy232 h133-copy233 h133-copy234 h133-copy235 h133-copy236 h133-copy237 h133-copy238 h133-copy239 h133-copy240 h133-copy241 h133-copy242 h133-copy243 h133-copy244 h133-copy245 h133-copy246 h133-copy247 h133-copy248 h133-copy249 h133-copy250 h133-copy251 h133-copy252 h133-copy253 h133-copy254 h133-copy255 h133-copy256 h133-copy257 h133-copy258 h133-copy259 h133-copy260 h133-copy261 h133-copy262 h133-copy263 h133-copy264 h133-copy265 h133-copy266 h133-copy267 h133-copy268 h133-copy269 h133-copy270 h133-copy271 h133-copy272 h133-copy273 h133-copy274 h133-copy275 h133-copy276 h133-copy277 h133-copy278 h133-copy279 h133-copy280 h133-copy281 h133-copy282 h133-copy283 h133-copy284 h133-copy285 h133-copy286 h133-copy287 h133-copy288 h133-copy289 h133-copy290 h133-copy291 h133-copy292 h133-copy293 h133-copy294 h133-copy295 h133-copy296 h133-copy297 h133-copy298 h133-copy299 h133-copy300 h133-copy301 h133-copy302 h133-copy303 h133-copy304 h133-copy305 h133-copy306 h133-copy307 h133-copy308 h133-copy309 h133-copy310 h133-copy311 h133-copy312 h133-copy313 h133-copy314 h133-copy315 h133-copy316 h133-copy317 h133-copy318 h133-copy319 h133-copy320 h133-copy321 h133-copy322 h133-copy323 h133-copy324 h133-copy325 h133-copy326 h133-copy327 h133-copy328 h133-copy329 h133-copy330 h133-copy331 h133-copy332 h133-copy333 h133-copy334 h133-copy335 h133-copy336 h133-copy337 h133-copy338 h133-copy339 h133-copy340 h133-copy341 h133-copy342 h133-copy343 h133-copy344 h133-copy345 h133-copy346 h133-copy347 h133-copy348 h133-copy349 h133-copy350 h133-copy351 h133-copy352 h133-copy353 h133-copy354 h133-copy355 h133-copy356 h133-copy357 h133-copy358 h133-copy359 h133-copy360 h133-copy361 h133-copy362 h133-copy363 h133-copy364 h133-copy365 h133-copy366 h133-copy367 h133-copy368 h133-copy369 h133-copy370 h133-copy371 h133-copy372 h133-copy373 h133-copy374 h133-copy375 h133-copy376 h133-copy377 h133-copy378 h133-copy379 h133-copy380 h133-copy381 h133-copy382 h133-copy383 h133-copy384 h133-copy385 h133-copy386 h133-copy387 h133-copy388 h133-copy389 h133-copy390 h133-copy391 h133-copy392 h133-copy393 h133-copy394 h133-copy395 h133-copy396 h133-copy397 h133-copy398 h133-copy399 h133-copy400 h133-copy401 h133-copy402 h133-copy403 h133-copy404 h133-copy405 h133-copy406 h133-copy407 h133-copy408 h133-copy409 h133-copy410 h133-copy411 h133-copy412 h133-copy413 h133-copy414 h133-copy415 h133-copy416 h133-copy417 h133-copy418 h133-copy419 h133-copy420 h133-copy421 h133-copy422 h133-copy423 h133-copy424 h133-copy425 h133-copy426 h133-copy427 h133-copy428 h133-copy429 h133-copy430 h133-copy431 h133-copy432 h133-copy433 h133-copy434 h133-copy435 h133-copy436 h133-copy437 h133-copy438 h133-copy439 h133-copy440 h133-copy441 h133-copy442 h133-copy443 h133-copy444 h133-copy445 h133-copy446 h133-copy447 h133-copy448 h133-copy449 h133-copy450 h133-copy451 h133-copy452 h133-copy453 h133-copy454 h133-copy455 h133-copy456 h133-copy457 h133-copy458 h133-copy459 h133-copy460 h133-copy461 h133-copy462 h133-copy463 h133-copy464 h133-copy465 h133-copy466 h133-copy467 h133-copy468 h133-copy469 h133-copy470 h133-copy471 h133-copy472 h133-copy473 h133-copy474 h133-copy475 h133-copy476 h133-copy477 h133-copy478 h133-copy479 h133-copy480 h133-copy481 h133-copy482 h133-copy483 h133-copy484 h133-copy485 h133-copy486 h133-copy487 h133-copy488 h133-copy489 h133-copy490 h133-copy491 h133-copy492 h133-copy493 h133-copy494 h133-copy495 h133-copy496 h133-copy497 h133-copy498 - hydrogen
h134 - hydrogen
h135 - hydrogen
h136 - hydrogen
h137 - hydrogen
h138 - hydrogen
h139 - hydrogen
h140 - hydrogen
h141 - hydrogen
h142 - hydrogen
h143 - hydrogen
h144 - hydrogen
h166 - hydrogen
h167 - hydrogen
h168 - hydrogen
h169 - hydrogen
h170 - hydrogen
h171 - hydrogen
h172 - hydrogen
h173 - hydrogen
h174 - hydrogen
h175 - hydrogen
h179 - hydrogen
h180 - hydrogen
h183 - hydrogen
h184 - hydrogen
o064 - oxygen
o065 - oxygen
o177 - oxygen
o178 - oxygen
o181 - oxygen
o182 - oxygen
)
(:init
(bond b071 c051)
(bond c051 b071)

(bond b071 c005)
(bond c005 b071)

(bond b071 c002)
(bond c002 b071)

(bond c001 c002)
(bond c002 c001)

(bond c002 c003)
(bond c003 c002)

(bond c004 c005)
(bond c005 c004)

(bond c005 c006)
(bond c006 c005)

(doublebond c032 c033)
(doublebond c033 c032)

(bond c032 h134)
(bond h134 c032)

(bond c032 h133) (bond c032 h133-copy1) (bond c032 h133-copy2) (bond c032 h133-copy3) (bond c032 h133-copy4) (bond c032 h133-copy5) (bond c032 h133-copy6) (bond c032 h133-copy7) (bond c032 h133-copy8) (bond c032 h133-copy9) (bond c032 h133-copy10) (bond c032 h133-copy11) (bond c032 h133-copy12) (bond c032 h133-copy13) (bond c032 h133-copy14) (bond c032 h133-copy15) (bond c032 h133-copy16) (bond c032 h133-copy17) (bond c032 h133-copy18) (bond c032 h133-copy19) (bond c032 h133-copy20) (bond c032 h133-copy21) (bond c032 h133-copy22) (bond c032 h133-copy23) (bond c032 h133-copy24) (bond c032 h133-copy25) (bond c032 h133-copy26) (bond c032 h133-copy27) (bond c032 h133-copy28) (bond c032 h133-copy29) (bond c032 h133-copy30) (bond c032 h133-copy31) (bond c032 h133-copy32) (bond c032 h133-copy33) (bond c032 h133-copy34) (bond c032 h133-copy35) (bond c032 h133-copy36) (bond c032 h133-copy37) (bond c032 h133-copy38) (bond c032 h133-copy39) (bond c032 h133-copy40) (bond c032 h133-copy41) (bond c032 h133-copy42) (bond c032 h133-copy43) (bond c032 h133-copy44) (bond c032 h133-copy45) (bond c032 h133-copy46) (bond c032 h133-copy47) (bond c032 h133-copy48) (bond c032 h133-copy49) (bond c032 h133-copy50) (bond c032 h133-copy51) (bond c032 h133-copy52) (bond c032 h133-copy53) (bond c032 h133-copy54) (bond c032 h133-copy55) (bond c032 h133-copy56) (bond c032 h133-copy57) (bond c032 h133-copy58) (bond c032 h133-copy59) (bond c032 h133-copy60) (bond c032 h133-copy61) (bond c032 h133-copy62) (bond c032 h133-copy63) (bond c032 h133-copy64) (bond c032 h133-copy65) (bond c032 h133-copy66) (bond c032 h133-copy67) (bond c032 h133-copy68) (bond c032 h133-copy69) (bond c032 h133-copy70) (bond c032 h133-copy71) (bond c032 h133-copy72) (bond c032 h133-copy73) (bond c032 h133-copy74) (bond c032 h133-copy75) (bond c032 h133-copy76) (bond c032 h133-copy77) (bond c032 h133-copy78) (bond c032 h133-copy79) (bond c032 h133-copy80) (bond c032 h133-copy81) (bond c032 h133-copy82) (bond c032 h133-copy83) (bond c032 h133-copy84) (bond c032 h133-copy85) (bond c032 h133-copy86) (bond c032 h133-copy87) (bond c032 h133-copy88) (bond c032 h133-copy89) (bond c032 h133-copy90) (bond c032 h133-copy91) (bond c032 h133-copy92) (bond c032 h133-copy93) (bond c032 h133-copy94) (bond c032 h133-copy95) (bond c032 h133-copy96) (bond c032 h133-copy97) (bond c032 h133-copy98) (bond c032 h133-copy99) (bond c032 h133-copy100) (bond c032 h133-copy101) (bond c032 h133-copy102) (bond c032 h133-copy103) (bond c032 h133-copy104) (bond c032 h133-copy105) (bond c032 h133-copy106) (bond c032 h133-copy107) (bond c032 h133-copy108) (bond c032 h133-copy109) (bond c032 h133-copy110) (bond c032 h133-copy111) (bond c032 h133-copy112) (bond c032 h133-copy113) (bond c032 h133-copy114) (bond c032 h133-copy115) (bond c032 h133-copy116) (bond c032 h133-copy117) (bond c032 h133-copy118) (bond c032 h133-copy119) (bond c032 h133-copy120) (bond c032 h133-copy121) (bond c032 h133-copy122) (bond c032 h133-copy123) (bond c032 h133-copy124) (bond c032 h133-copy125) (bond c032 h133-copy126) (bond c032 h133-copy127) (bond c032 h133-copy128) (bond c032 h133-copy129) (bond c032 h133-copy130) (bond c032 h133-copy131) (bond c032 h133-copy132) (bond c032 h133-copy133) (bond c032 h133-copy134) (bond c032 h133-copy135) (bond c032 h133-copy136) (bond c032 h133-copy137) (bond c032 h133-copy138) (bond c032 h133-copy139) (bond c032 h133-copy140) (bond c032 h133-copy141) (bond c032 h133-copy142) (bond c032 h133-copy143) (bond c032 h133-copy144) (bond c032 h133-copy145) (bond c032 h133-copy146) (bond c032 h133-copy147) (bond c032 h133-copy148) (bond c032 h133-copy149) (bond c032 h133-copy150) (bond c032 h133-copy151) (bond c032 h133-copy152) (bond c032 h133-copy153) (bond c032 h133-copy154) (bond c032 h133-copy155) (bond c032 h133-copy156) (bond c032 h133-copy157) (bond c032 h133-copy158) (bond c032 h133-copy159) (bond c032 h133-copy160) (bond c032 h133-copy161) (bond c032 h133-copy162) (bond c032 h133-copy163) (bond c032 h133-copy164) (bond c032 h133-copy165) (bond c032 h133-copy166) (bond c032 h133-copy167) (bond c032 h133-copy168) (bond c032 h133-copy169) (bond c032 h133-copy170) (bond c032 h133-copy171) (bond c032 h133-copy172) (bond c032 h133-copy173) (bond c032 h133-copy174) (bond c032 h133-copy175) (bond c032 h133-copy176) (bond c032 h133-copy177) (bond c032 h133-copy178) (bond c032 h133-copy179) (bond c032 h133-copy180) (bond c032 h133-copy181) (bond c032 h133-copy182) (bond c032 h133-copy183) (bond c032 h133-copy184) (bond c032 h133-copy185) (bond c032 h133-copy186) (bond c032 h133-copy187) (bond c032 h133-copy188) (bond c032 h133-copy189) (bond c032 h133-copy190) (bond c032 h133-copy191) (bond c032 h133-copy192) (bond c032 h133-copy193) (bond c032 h133-copy194) (bond c032 h133-copy195) (bond c032 h133-copy196) (bond c032 h133-copy197) (bond c032 h133-copy198) (bond c032 h133-copy199) (bond c032 h133-copy200) (bond c032 h133-copy201) (bond c032 h133-copy202) (bond c032 h133-copy203) (bond c032 h133-copy204) (bond c032 h133-copy205) (bond c032 h133-copy206) (bond c032 h133-copy207) (bond c032 h133-copy208) (bond c032 h133-copy209) (bond c032 h133-copy210) (bond c032 h133-copy211) (bond c032 h133-copy212) (bond c032 h133-copy213) (bond c032 h133-copy214) (bond c032 h133-copy215) (bond c032 h133-copy216) (bond c032 h133-copy217) (bond c032 h133-copy218) (bond c032 h133-copy219) (bond c032 h133-copy220) (bond c032 h133-copy221) (bond c032 h133-copy222) (bond c032 h133-copy223) (bond c032 h133-copy224) (bond c032 h133-copy225) (bond c032 h133-copy226) (bond c032 h133-copy227) (bond c032 h133-copy228) (bond c032 h133-copy229) (bond c032 h133-copy230) (bond c032 h133-copy231) (bond c032 h133-copy232) (bond c032 h133-copy233) (bond c032 h133-copy234) (bond c032 h133-copy235) (bond c032 h133-copy236) (bond c032 h133-copy237) (bond c032 h133-copy238) (bond c032 h133-copy239) (bond c032 h133-copy240) (bond c032 h133-copy241) (bond c032 h133-copy242) (bond c032 h133-copy243) (bond c032 h133-copy244) (bond c032 h133-copy245) (bond c032 h133-copy246) (bond c032 h133-copy247) (bond c032 h133-copy248) (bond c032 h133-copy249) (bond c032 h133-copy250) (bond c032 h133-copy251) (bond c032 h133-copy252) (bond c032 h133-copy253) (bond c032 h133-copy254) (bond c032 h133-copy255) (bond c032 h133-copy256) (bond c032 h133-copy257) (bond c032 h133-copy258) (bond c032 h133-copy259) (bond c032 h133-copy260) (bond c032 h133-copy261) (bond c032 h133-copy262) (bond c032 h133-copy263) (bond c032 h133-copy264) (bond c032 h133-copy265) (bond c032 h133-copy266) (bond c032 h133-copy267) (bond c032 h133-copy268) (bond c032 h133-copy269) (bond c032 h133-copy270) (bond c032 h133-copy271) (bond c032 h133-copy272) (bond c032 h133-copy273) (bond c032 h133-copy274) (bond c032 h133-copy275) (bond c032 h133-copy276) (bond c032 h133-copy277) (bond c032 h133-copy278) (bond c032 h133-copy279) (bond c032 h133-copy280) (bond c032 h133-copy281) (bond c032 h133-copy282) (bond c032 h133-copy283) (bond c032 h133-copy284) (bond c032 h133-copy285) (bond c032 h133-copy286) (bond c032 h133-copy287) (bond c032 h133-copy288) (bond c032 h133-copy289) (bond c032 h133-copy290) (bond c032 h133-copy291) (bond c032 h133-copy292) (bond c032 h133-copy293) (bond c032 h133-copy294) (bond c032 h133-copy295) (bond c032 h133-copy296) (bond c032 h133-copy297) (bond c032 h133-copy298) (bond c032 h133-copy299) (bond c032 h133-copy300) (bond c032 h133-copy301) (bond c032 h133-copy302) (bond c032 h133-copy303) (bond c032 h133-copy304) (bond c032 h133-copy305) (bond c032 h133-copy306) (bond c032 h133-copy307) (bond c032 h133-copy308) (bond c032 h133-copy309) (bond c032 h133-copy310) (bond c032 h133-copy311) (bond c032 h133-copy312) (bond c032 h133-copy313) (bond c032 h133-copy314) (bond c032 h133-copy315) (bond c032 h133-copy316) (bond c032 h133-copy317) (bond c032 h133-copy318) (bond c032 h133-copy319) (bond c032 h133-copy320) (bond c032 h133-copy321) (bond c032 h133-copy322) (bond c032 h133-copy323) (bond c032 h133-copy324) (bond c032 h133-copy325) (bond c032 h133-copy326) (bond c032 h133-copy327) (bond c032 h133-copy328) (bond c032 h133-copy329) (bond c032 h133-copy330) (bond c032 h133-copy331) (bond c032 h133-copy332) (bond c032 h133-copy333) (bond c032 h133-copy334) (bond c032 h133-copy335) (bond c032 h133-copy336) (bond c032 h133-copy337) (bond c032 h133-copy338) (bond c032 h133-copy339) (bond c032 h133-copy340) (bond c032 h133-copy341) (bond c032 h133-copy342) (bond c032 h133-copy343) (bond c032 h133-copy344) (bond c032 h133-copy345) (bond c032 h133-copy346) (bond c032 h133-copy347) (bond c032 h133-copy348) (bond c032 h133-copy349) (bond c032 h133-copy350) (bond c032 h133-copy351) (bond c032 h133-copy352) (bond c032 h133-copy353) (bond c032 h133-copy354) (bond c032 h133-copy355) (bond c032 h133-copy356) (bond c032 h133-copy357) (bond c032 h133-copy358) (bond c032 h133-copy359) (bond c032 h133-copy360) (bond c032 h133-copy361) (bond c032 h133-copy362) (bond c032 h133-copy363) (bond c032 h133-copy364) (bond c032 h133-copy365) (bond c032 h133-copy366) (bond c032 h133-copy367) (bond c032 h133-copy368) (bond c032 h133-copy369) (bond c032 h133-copy370) (bond c032 h133-copy371) (bond c032 h133-copy372) (bond c032 h133-copy373) (bond c032 h133-copy374) (bond c032 h133-copy375) (bond c032 h133-copy376) (bond c032 h133-copy377) (bond c032 h133-copy378) (bond c032 h133-copy379) (bond c032 h133-copy380) (bond c032 h133-copy381) (bond c032 h133-copy382) (bond c032 h133-copy383) (bond c032 h133-copy384) (bond c032 h133-copy385) (bond c032 h133-copy386) (bond c032 h133-copy387) (bond c032 h133-copy388) (bond c032 h133-copy389) (bond c032 h133-copy390) (bond c032 h133-copy391) (bond c032 h133-copy392) (bond c032 h133-copy393) (bond c032 h133-copy394) (bond c032 h133-copy395) (bond c032 h133-copy396) (bond c032 h133-copy397) (bond c032 h133-copy398) (bond c032 h133-copy399) (bond c032 h133-copy400) (bond c032 h133-copy401) (bond c032 h133-copy402) (bond c032 h133-copy403) (bond c032 h133-copy404) (bond c032 h133-copy405) (bond c032 h133-copy406) (bond c032 h133-copy407) (bond c032 h133-copy408) (bond c032 h133-copy409) (bond c032 h133-copy410) (bond c032 h133-copy411) (bond c032 h133-copy412) (bond c032 h133-copy413) (bond c032 h133-copy414) (bond c032 h133-copy415) (bond c032 h133-copy416) (bond c032 h133-copy417) (bond c032 h133-copy418) (bond c032 h133-copy419) (bond c032 h133-copy420) (bond c032 h133-copy421) (bond c032 h133-copy422) (bond c032 h133-copy423) (bond c032 h133-copy424) (bond c032 h133-copy425) (bond c032 h133-copy426) (bond c032 h133-copy427) (bond c032 h133-copy428) (bond c032 h133-copy429) (bond c032 h133-copy430) (bond c032 h133-copy431) (bond c032 h133-copy432) (bond c032 h133-copy433) (bond c032 h133-copy434) (bond c032 h133-copy435) (bond c032 h133-copy436) (bond c032 h133-copy437) (bond c032 h133-copy438) (bond c032 h133-copy439) (bond c032 h133-copy440) (bond c032 h133-copy441) (bond c032 h133-copy442) (bond c032 h133-copy443) (bond c032 h133-copy444) (bond c032 h133-copy445) (bond c032 h133-copy446) (bond c032 h133-copy447) (bond c032 h133-copy448) (bond c032 h133-copy449) (bond c032 h133-copy450) (bond c032 h133-copy451) (bond c032 h133-copy452) (bond c032 h133-copy453) (bond c032 h133-copy454) (bond c032 h133-copy455) (bond c032 h133-copy456) (bond c032 h133-copy457) (bond c032 h133-copy458) (bond c032 h133-copy459) (bond c032 h133-copy460) (bond c032 h133-copy461) (bond c032 h133-copy462) (bond c032 h133-copy463) (bond c032 h133-copy464) (bond c032 h133-copy465) (bond c032 h133-copy466) (bond c032 h133-copy467) (bond c032 h133-copy468) (bond c032 h133-copy469) (bond c032 h133-copy470) (bond c032 h133-copy471) (bond c032 h133-copy472) (bond c032 h133-copy473) (bond c032 h133-copy474) (bond c032 h133-copy475) (bond c032 h133-copy476) (bond c032 h133-copy477) (bond c032 h133-copy478) (bond c032 h133-copy479) (bond c032 h133-copy480) (bond c032 h133-copy481) (bond c032 h133-copy482) (bond c032 h133-copy483) (bond c032 h133-copy484) (bond c032 h133-copy485) (bond c032 h133-copy486) (bond c032 h133-copy487) (bond c032 h133-copy488) (bond c032 h133-copy489) (bond c032 h133-copy490) (bond c032 h133-copy491) (bond c032 h133-copy492) (bond c032 h133-copy493) (bond c032 h133-copy494) (bond c032 h133-copy495) (bond c032 h133-copy496) (bond c032 h133-copy497) (bond c032 h133-copy498)
(bond h133 c032) (bond h133-copy1 c032) (bond h133-copy2 c032) (bond h133-copy3 c032) (bond h133-copy4 c032) (bond h133-copy5 c032) (bond h133-copy6 c032) (bond h133-copy7 c032) (bond h133-copy8 c032) (bond h133-copy9 c032) (bond h133-copy10 c032) (bond h133-copy11 c032) (bond h133-copy12 c032) (bond h133-copy13 c032) (bond h133-copy14 c032) (bond h133-copy15 c032) (bond h133-copy16 c032) (bond h133-copy17 c032) (bond h133-copy18 c032) (bond h133-copy19 c032) (bond h133-copy20 c032) (bond h133-copy21 c032) (bond h133-copy22 c032) (bond h133-copy23 c032) (bond h133-copy24 c032) (bond h133-copy25 c032) (bond h133-copy26 c032) (bond h133-copy27 c032) (bond h133-copy28 c032) (bond h133-copy29 c032) (bond h133-copy30 c032) (bond h133-copy31 c032) (bond h133-copy32 c032) (bond h133-copy33 c032) (bond h133-copy34 c032) (bond h133-copy35 c032) (bond h133-copy36 c032) (bond h133-copy37 c032) (bond h133-copy38 c032) (bond h133-copy39 c032) (bond h133-copy40 c032) (bond h133-copy41 c032) (bond h133-copy42 c032) (bond h133-copy43 c032) (bond h133-copy44 c032) (bond h133-copy45 c032) (bond h133-copy46 c032) (bond h133-copy47 c032) (bond h133-copy48 c032) (bond h133-copy49 c032) (bond h133-copy50 c032) (bond h133-copy51 c032) (bond h133-copy52 c032) (bond h133-copy53 c032) (bond h133-copy54 c032) (bond h133-copy55 c032) (bond h133-copy56 c032) (bond h133-copy57 c032) (bond h133-copy58 c032) (bond h133-copy59 c032) (bond h133-copy60 c032) (bond h133-copy61 c032) (bond h133-copy62 c032) (bond h133-copy63 c032) (bond h133-copy64 c032) (bond h133-copy65 c032) (bond h133-copy66 c032) (bond h133-copy67 c032) (bond h133-copy68 c032) (bond h133-copy69 c032) (bond h133-copy70 c032) (bond h133-copy71 c032) (bond h133-copy72 c032) (bond h133-copy73 c032) (bond h133-copy74 c032) (bond h133-copy75 c032) (bond h133-copy76 c032) (bond h133-copy77 c032) (bond h133-copy78 c032) (bond h133-copy79 c032) (bond h133-copy80 c032) (bond h133-copy81 c032) (bond h133-copy82 c032) (bond h133-copy83 c032) (bond h133-copy84 c032) (bond h133-copy85 c032) (bond h133-copy86 c032) (bond h133-copy87 c032) (bond h133-copy88 c032) (bond h133-copy89 c032) (bond h133-copy90 c032) (bond h133-copy91 c032) (bond h133-copy92 c032) (bond h133-copy93 c032) (bond h133-copy94 c032) (bond h133-copy95 c032) (bond h133-copy96 c032) (bond h133-copy97 c032) (bond h133-copy98 c032) (bond h133-copy99 c032) (bond h133-copy100 c032) (bond h133-copy101 c032) (bond h133-copy102 c032) (bond h133-copy103 c032) (bond h133-copy104 c032) (bond h133-copy105 c032) (bond h133-copy106 c032) (bond h133-copy107 c032) (bond h133-copy108 c032) (bond h133-copy109 c032) (bond h133-copy110 c032) (bond h133-copy111 c032) (bond h133-copy112 c032) (bond h133-copy113 c032) (bond h133-copy114 c032) (bond h133-copy115 c032) (bond h133-copy116 c032) (bond h133-copy117 c032) (bond h133-copy118 c032) (bond h133-copy119 c032) (bond h133-copy120 c032) (bond h133-copy121 c032) (bond h133-copy122 c032) (bond h133-copy123 c032) (bond h133-copy124 c032) (bond h133-copy125 c032) (bond h133-copy126 c032) (bond h133-copy127 c032) (bond h133-copy128 c032) (bond h133-copy129 c032) (bond h133-copy130 c032) (bond h133-copy131 c032) (bond h133-copy132 c032) (bond h133-copy133 c032) (bond h133-copy134 c032) (bond h133-copy135 c032) (bond h133-copy136 c032) (bond h133-copy137 c032) (bond h133-copy138 c032) (bond h133-copy139 c032) (bond h133-copy140 c032) (bond h133-copy141 c032) (bond h133-copy142 c032) (bond h133-copy143 c032) (bond h133-copy144 c032) (bond h133-copy145 c032) (bond h133-copy146 c032) (bond h133-copy147 c032) (bond h133-copy148 c032) (bond h133-copy149 c032) (bond h133-copy150 c032) (bond h133-copy151 c032) (bond h133-copy152 c032) (bond h133-copy153 c032) (bond h133-copy154 c032) (bond h133-copy155 c032) (bond h133-copy156 c032) (bond h133-copy157 c032) (bond h133-copy158 c032) (bond h133-copy159 c032) (bond h133-copy160 c032) (bond h133-copy161 c032) (bond h133-copy162 c032) (bond h133-copy163 c032) (bond h133-copy164 c032) (bond h133-copy165 c032) (bond h133-copy166 c032) (bond h133-copy167 c032) (bond h133-copy168 c032) (bond h133-copy169 c032) (bond h133-copy170 c032) (bond h133-copy171 c032) (bond h133-copy172 c032) (bond h133-copy173 c032) (bond h133-copy174 c032) (bond h133-copy175 c032) (bond h133-copy176 c032) (bond h133-copy177 c032) (bond h133-copy178 c032) (bond h133-copy179 c032) (bond h133-copy180 c032) (bond h133-copy181 c032) (bond h133-copy182 c032) (bond h133-copy183 c032) (bond h133-copy184 c032) (bond h133-copy185 c032) (bond h133-copy186 c032) (bond h133-copy187 c032) (bond h133-copy188 c032) (bond h133-copy189 c032) (bond h133-copy190 c032) (bond h133-copy191 c032) (bond h133-copy192 c032) (bond h133-copy193 c032) (bond h133-copy194 c032) (bond h133-copy195 c032) (bond h133-copy196 c032) (bond h133-copy197 c032) (bond h133-copy198 c032) (bond h133-copy199 c032) (bond h133-copy200 c032) (bond h133-copy201 c032) (bond h133-copy202 c032) (bond h133-copy203 c032) (bond h133-copy204 c032) (bond h133-copy205 c032) (bond h133-copy206 c032) (bond h133-copy207 c032) (bond h133-copy208 c032) (bond h133-copy209 c032) (bond h133-copy210 c032) (bond h133-copy211 c032) (bond h133-copy212 c032) (bond h133-copy213 c032) (bond h133-copy214 c032) (bond h133-copy215 c032) (bond h133-copy216 c032) (bond h133-copy217 c032) (bond h133-copy218 c032) (bond h133-copy219 c032) (bond h133-copy220 c032) (bond h133-copy221 c032) (bond h133-copy222 c032) (bond h133-copy223 c032) (bond h133-copy224 c032) (bond h133-copy225 c032) (bond h133-copy226 c032) (bond h133-copy227 c032) (bond h133-copy228 c032) (bond h133-copy229 c032) (bond h133-copy230 c032) (bond h133-copy231 c032) (bond h133-copy232 c032) (bond h133-copy233 c032) (bond h133-copy234 c032) (bond h133-copy235 c032) (bond h133-copy236 c032) (bond h133-copy237 c032) (bond h133-copy238 c032) (bond h133-copy239 c032) (bond h133-copy240 c032) (bond h133-copy241 c032) (bond h133-copy242 c032) (bond h133-copy243 c032) (bond h133-copy244 c032) (bond h133-copy245 c032) (bond h133-copy246 c032) (bond h133-copy247 c032) (bond h133-copy248 c032) (bond h133-copy249 c032) (bond h133-copy250 c032) (bond h133-copy251 c032) (bond h133-copy252 c032) (bond h133-copy253 c032) (bond h133-copy254 c032) (bond h133-copy255 c032) (bond h133-copy256 c032) (bond h133-copy257 c032) (bond h133-copy258 c032) (bond h133-copy259 c032) (bond h133-copy260 c032) (bond h133-copy261 c032) (bond h133-copy262 c032) (bond h133-copy263 c032) (bond h133-copy264 c032) (bond h133-copy265 c032) (bond h133-copy266 c032) (bond h133-copy267 c032) (bond h133-copy268 c032) (bond h133-copy269 c032) (bond h133-copy270 c032) (bond h133-copy271 c032) (bond h133-copy272 c032) (bond h133-copy273 c032) (bond h133-copy274 c032) (bond h133-copy275 c032) (bond h133-copy276 c032) (bond h133-copy277 c032) (bond h133-copy278 c032) (bond h133-copy279 c032) (bond h133-copy280 c032) (bond h133-copy281 c032) (bond h133-copy282 c032) (bond h133-copy283 c032) (bond h133-copy284 c032) (bond h133-copy285 c032) (bond h133-copy286 c032) (bond h133-copy287 c032) (bond h133-copy288 c032) (bond h133-copy289 c032) (bond h133-copy290 c032) (bond h133-copy291 c032) (bond h133-copy292 c032) (bond h133-copy293 c032) (bond h133-copy294 c032) (bond h133-copy295 c032) (bond h133-copy296 c032) (bond h133-copy297 c032) (bond h133-copy298 c032) (bond h133-copy299 c032) (bond h133-copy300 c032) (bond h133-copy301 c032) (bond h133-copy302 c032) (bond h133-copy303 c032) (bond h133-copy304 c032) (bond h133-copy305 c032) (bond h133-copy306 c032) (bond h133-copy307 c032) (bond h133-copy308 c032) (bond h133-copy309 c032) (bond h133-copy310 c032) (bond h133-copy311 c032) (bond h133-copy312 c032) (bond h133-copy313 c032) (bond h133-copy314 c032) (bond h133-copy315 c032) (bond h133-copy316 c032) (bond h133-copy317 c032) (bond h133-copy318 c032) (bond h133-copy319 c032) (bond h133-copy320 c032) (bond h133-copy321 c032) (bond h133-copy322 c032) (bond h133-copy323 c032) (bond h133-copy324 c032) (bond h133-copy325 c032) (bond h133-copy326 c032) (bond h133-copy327 c032) (bond h133-copy328 c032) (bond h133-copy329 c032) (bond h133-copy330 c032) (bond h133-copy331 c032) (bond h133-copy332 c032) (bond h133-copy333 c032) (bond h133-copy334 c032) (bond h133-copy335 c032) (bond h133-copy336 c032) (bond h133-copy337 c032) (bond h133-copy338 c032) (bond h133-copy339 c032) (bond h133-copy340 c032) (bond h133-copy341 c032) (bond h133-copy342 c032) (bond h133-copy343 c032) (bond h133-copy344 c032) (bond h133-copy345 c032) (bond h133-copy346 c032) (bond h133-copy347 c032) (bond h133-copy348 c032) (bond h133-copy349 c032) (bond h133-copy350 c032) (bond h133-copy351 c032) (bond h133-copy352 c032) (bond h133-copy353 c032) (bond h133-copy354 c032) (bond h133-copy355 c032) (bond h133-copy356 c032) (bond h133-copy357 c032) (bond h133-copy358 c032) (bond h133-copy359 c032) (bond h133-copy360 c032) (bond h133-copy361 c032) (bond h133-copy362 c032) (bond h133-copy363 c032) (bond h133-copy364 c032) (bond h133-copy365 c032) (bond h133-copy366 c032) (bond h133-copy367 c032) (bond h133-copy368 c032) (bond h133-copy369 c032) (bond h133-copy370 c032) (bond h133-copy371 c032) (bond h133-copy372 c032) (bond h133-copy373 c032) (bond h133-copy374 c032) (bond h133-copy375 c032) (bond h133-copy376 c032) (bond h133-copy377 c032) (bond h133-copy378 c032) (bond h133-copy379 c032) (bond h133-copy380 c032) (bond h133-copy381 c032) (bond h133-copy382 c032) (bond h133-copy383 c032) (bond h133-copy384 c032) (bond h133-copy385 c032) (bond h133-copy386 c032) (bond h133-copy387 c032) (bond h133-copy388 c032) (bond h133-copy389 c032) (bond h133-copy390 c032) (bond h133-copy391 c032) (bond h133-copy392 c032) (bond h133-copy393 c032) (bond h133-copy394 c032) (bond h133-copy395 c032) (bond h133-copy396 c032) (bond h133-copy397 c032) (bond h133-copy398 c032) (bond h133-copy399 c032) (bond h133-copy400 c032) (bond h133-copy401 c032) (bond h133-copy402 c032) (bond h133-copy403 c032) (bond h133-copy404 c032) (bond h133-copy405 c032) (bond h133-copy406 c032) (bond h133-copy407 c032) (bond h133-copy408 c032) (bond h133-copy409 c032) (bond h133-copy410 c032) (bond h133-copy411 c032) (bond h133-copy412 c032) (bond h133-copy413 c032) (bond h133-copy414 c032) (bond h133-copy415 c032) (bond h133-copy416 c032) (bond h133-copy417 c032) (bond h133-copy418 c032) (bond h133-copy419 c032) (bond h133-copy420 c032) (bond h133-copy421 c032) (bond h133-copy422 c032) (bond h133-copy423 c032) (bond h133-copy424 c032) (bond h133-copy425 c032) (bond h133-copy426 c032) (bond h133-copy427 c032) (bond h133-copy428 c032) (bond h133-copy429 c032) (bond h133-copy430 c032) (bond h133-copy431 c032) (bond h133-copy432 c032) (bond h133-copy433 c032) (bond h133-copy434 c032) (bond h133-copy435 c032) (bond h133-copy436 c032) (bond h133-copy437 c032) (bond h133-copy438 c032) (bond h133-copy439 c032) (bond h133-copy440 c032) (bond h133-copy441 c032) (bond h133-copy442 c032) (bond h133-copy443 c032) (bond h133-copy444 c032) (bond h133-copy445 c032) (bond h133-copy446 c032) (bond h133-copy447 c032) (bond h133-copy448 c032) (bond h133-copy449 c032) (bond h133-copy450 c032) (bond h133-copy451 c032) (bond h133-copy452 c032) (bond h133-copy453 c032) (bond h133-copy454 c032) (bond h133-copy455 c032) (bond h133-copy456 c032) (bond h133-copy457 c032) (bond h133-copy458 c032) (bond h133-copy459 c032) (bond h133-copy460 c032) (bond h133-copy461 c032) (bond h133-copy462 c032) (bond h133-copy463 c032) (bond h133-copy464 c032) (bond h133-copy465 c032) (bond h133-copy466 c032) (bond h133-copy467 c032) (bond h133-copy468 c032) (bond h133-copy469 c032) (bond h133-copy470 c032) (bond h133-copy471 c032) (bond h133-copy472 c032) (bond h133-copy473 c032) (bond h133-copy474 c032) (bond h133-copy475 c032) (bond h133-copy476 c032) (bond h133-copy477 c032) (bond h133-copy478 c032) (bond h133-copy479 c032) (bond h133-copy480 c032) (bond h133-copy481 c032) (bond h133-copy482 c032) (bond h133-copy483 c032) (bond h133-copy484 c032) (bond h133-copy485 c032) (bond h133-copy486 c032) (bond h133-copy487 c032) (bond h133-copy488 c032) (bond h133-copy489 c032) (bond h133-copy490 c032) (bond h133-copy491 c032) (bond h133-copy492 c032) (bond h133-copy493 c032) (bond h133-copy494 c032) (bond h133-copy495 c032) (bond h133-copy496 c032) (bond h133-copy497 c032) (bond h133-copy498 c032)

(bond c033 c034)
(bond c034 c033)

(bond c033 c038)
(bond c038 c033)

(bond c034 h136)
(bond h136 c034)

(bond c034 h135)
(bond h135 c034)

(bond c034 c035)
(bond c035 c034)

(bond c035 c036)
(bond c036 c035)

(bond c035 h138)
(bond h138 c035)

(bond c035 h137)
(bond h137 c035)

(bond c036 h140)
(bond h140 c036)

(bond c036 h139)
(bond h139 c036)

(bond c036 c037)
(bond c037 c036)

(bond c037 h142)
(bond h142 c037)

(bond c037 h141)
(bond h141 c037)

(bond c037 c038)
(bond c038 c037)

(bond c038 h144)
(bond h144 c038)

(bond c038 h143)
(bond h143 c038)

(bond c051 h166)
(bond h166 c051)

(bond c051 h167)
(bond h167 c051)

(bond c051 c052)
(bond c052 c051)

(bond c052 c053)
(bond c053 c052)

(bond c052 h060)
(bond h060 c052)

(bond c052 h168)
(bond h168 c052)

(bond c053 h170)
(bond h170 c053)

(bond c053 h169)
(bond h169 c053)

(bond c053 c054)
(bond c054 c053)

(bond c054 h172)
(bond h172 c054)

(bond c054 h171)
(bond h171 c054)

(bond c054 c055)
(bond c055 c054)

(bond c055 h175)
(bond h175 c055)

(bond c055 h174)
(bond h174 c055)

(bond c055 h173)
(bond h173 c055)

(bond h058 o064)
(bond o064 h058)

(bond h059 o065)
(bond o065 h059)

(bond h179 o177)
(bond o177 h179)

(bond h180 o178)
(bond o178 h180)

(bond h183 o181)
(bond o181 h183)

(bond h184 o182)
(bond o182 h184)

(bond o064 o065)
(bond o065 o064)

(bond o177 o178)
(bond o178 o177)

(bond o181 o182)
(bond o182 o181)
)
(:goal
(and
(bond c032 c033)
(bond c033 c032)

(bond c032 h059)
(bond h059 c032)

(bond c032 h134)
(bond h134 c032)

(bond c032 h133) (bond c032 h133-copy1) (bond c032 h133-copy2) (bond c032 h133-copy3) (bond c032 h133-copy4) (bond c032 h133-copy5) (bond c032 h133-copy6) (bond c032 h133-copy7) (bond c032 h133-copy8) (bond c032 h133-copy9) (bond c032 h133-copy10) (bond c032 h133-copy11) (bond c032 h133-copy12) (bond c032 h133-copy13) (bond c032 h133-copy14) (bond c032 h133-copy15) (bond c032 h133-copy16) (bond c032 h133-copy17) (bond c032 h133-copy18) (bond c032 h133-copy19) (bond c032 h133-copy20) (bond c032 h133-copy21) (bond c032 h133-copy22) (bond c032 h133-copy23) (bond c032 h133-copy24) (bond c032 h133-copy25) (bond c032 h133-copy26) (bond c032 h133-copy27) (bond c032 h133-copy28) (bond c032 h133-copy29) (bond c032 h133-copy30) (bond c032 h133-copy31) (bond c032 h133-copy32) (bond c032 h133-copy33) (bond c032 h133-copy34) (bond c032 h133-copy35) (bond c032 h133-copy36) (bond c032 h133-copy37) (bond c032 h133-copy38) (bond c032 h133-copy39) (bond c032 h133-copy40) (bond c032 h133-copy41) (bond c032 h133-copy42) (bond c032 h133-copy43) (bond c032 h133-copy44) (bond c032 h133-copy45) (bond c032 h133-copy46) (bond c032 h133-copy47) (bond c032 h133-copy48) (bond c032 h133-copy49) (bond c032 h133-copy50) (bond c032 h133-copy51) (bond c032 h133-copy52) (bond c032 h133-copy53) (bond c032 h133-copy54) (bond c032 h133-copy55) (bond c032 h133-copy56) (bond c032 h133-copy57) (bond c032 h133-copy58) (bond c032 h133-copy59) (bond c032 h133-copy60) (bond c032 h133-copy61) (bond c032 h133-copy62) (bond c032 h133-copy63) (bond c032 h133-copy64) (bond c032 h133-copy65) (bond c032 h133-copy66) (bond c032 h133-copy67) (bond c032 h133-copy68) (bond c032 h133-copy69) (bond c032 h133-copy70) (bond c032 h133-copy71) (bond c032 h133-copy72) (bond c032 h133-copy73) (bond c032 h133-copy74) (bond c032 h133-copy75) (bond c032 h133-copy76) (bond c032 h133-copy77) (bond c032 h133-copy78) (bond c032 h133-copy79) (bond c032 h133-copy80) (bond c032 h133-copy81) (bond c032 h133-copy82) (bond c032 h133-copy83) (bond c032 h133-copy84) (bond c032 h133-copy85) (bond c032 h133-copy86) (bond c032 h133-copy87) (bond c032 h133-copy88) (bond c032 h133-copy89) (bond c032 h133-copy90) (bond c032 h133-copy91) (bond c032 h133-copy92) (bond c032 h133-copy93) (bond c032 h133-copy94) (bond c032 h133-copy95) (bond c032 h133-copy96) (bond c032 h133-copy97) (bond c032 h133-copy98) (bond c032 h133-copy99) (bond c032 h133-copy100) (bond c032 h133-copy101) (bond c032 h133-copy102) (bond c032 h133-copy103) (bond c032 h133-copy104) (bond c032 h133-copy105) (bond c032 h133-copy106) (bond c032 h133-copy107) (bond c032 h133-copy108) (bond c032 h133-copy109) (bond c032 h133-copy110) (bond c032 h133-copy111) (bond c032 h133-copy112) (bond c032 h133-copy113) (bond c032 h133-copy114) (bond c032 h133-copy115) (bond c032 h133-copy116) (bond c032 h133-copy117) (bond c032 h133-copy118) (bond c032 h133-copy119) (bond c032 h133-copy120) (bond c032 h133-copy121) (bond c032 h133-copy122) (bond c032 h133-copy123) (bond c032 h133-copy124) (bond c032 h133-copy125) (bond c032 h133-copy126) (bond c032 h133-copy127) (bond c032 h133-copy128) (bond c032 h133-copy129) (bond c032 h133-copy130) (bond c032 h133-copy131) (bond c032 h133-copy132) (bond c032 h133-copy133) (bond c032 h133-copy134) (bond c032 h133-copy135) (bond c032 h133-copy136) (bond c032 h133-copy137) (bond c032 h133-copy138) (bond c032 h133-copy139) (bond c032 h133-copy140) (bond c032 h133-copy141) (bond c032 h133-copy142) (bond c032 h133-copy143) (bond c032 h133-copy144) (bond c032 h133-copy145) (bond c032 h133-copy146) (bond c032 h133-copy147) (bond c032 h133-copy148) (bond c032 h133-copy149) (bond c032 h133-copy150) (bond c032 h133-copy151) (bond c032 h133-copy152) (bond c032 h133-copy153) (bond c032 h133-copy154) (bond c032 h133-copy155) (bond c032 h133-copy156) (bond c032 h133-copy157) (bond c032 h133-copy158) (bond c032 h133-copy159) (bond c032 h133-copy160) (bond c032 h133-copy161) (bond c032 h133-copy162) (bond c032 h133-copy163) (bond c032 h133-copy164) (bond c032 h133-copy165) (bond c032 h133-copy166) (bond c032 h133-copy167) (bond c032 h133-copy168) (bond c032 h133-copy169) (bond c032 h133-copy170) (bond c032 h133-copy171) (bond c032 h133-copy172) (bond c032 h133-copy173) (bond c032 h133-copy174) (bond c032 h133-copy175) (bond c032 h133-copy176) (bond c032 h133-copy177) (bond c032 h133-copy178) (bond c032 h133-copy179) (bond c032 h133-copy180) (bond c032 h133-copy181) (bond c032 h133-copy182) (bond c032 h133-copy183) (bond c032 h133-copy184) (bond c032 h133-copy185) (bond c032 h133-copy186) (bond c032 h133-copy187) (bond c032 h133-copy188) (bond c032 h133-copy189) (bond c032 h133-copy190) (bond c032 h133-copy191) (bond c032 h133-copy192) (bond c032 h133-copy193) (bond c032 h133-copy194) (bond c032 h133-copy195) (bond c032 h133-copy196) (bond c032 h133-copy197) (bond c032 h133-copy198) (bond c032 h133-copy199) (bond c032 h133-copy200) (bond c032 h133-copy201) (bond c032 h133-copy202) (bond c032 h133-copy203) (bond c032 h133-copy204) (bond c032 h133-copy205) (bond c032 h133-copy206) (bond c032 h133-copy207) (bond c032 h133-copy208) (bond c032 h133-copy209) (bond c032 h133-copy210) (bond c032 h133-copy211) (bond c032 h133-copy212) (bond c032 h133-copy213) (bond c032 h133-copy214) (bond c032 h133-copy215) (bond c032 h133-copy216) (bond c032 h133-copy217) (bond c032 h133-copy218) (bond c032 h133-copy219) (bond c032 h133-copy220) (bond c032 h133-copy221) (bond c032 h133-copy222) (bond c032 h133-copy223) (bond c032 h133-copy224) (bond c032 h133-copy225) (bond c032 h133-copy226) (bond c032 h133-copy227) (bond c032 h133-copy228) (bond c032 h133-copy229) (bond c032 h133-copy230) (bond c032 h133-copy231) (bond c032 h133-copy232) (bond c032 h133-copy233) (bond c032 h133-copy234) (bond c032 h133-copy235) (bond c032 h133-copy236) (bond c032 h133-copy237) (bond c032 h133-copy238) (bond c032 h133-copy239) (bond c032 h133-copy240) (bond c032 h133-copy241) (bond c032 h133-copy242) (bond c032 h133-copy243) (bond c032 h133-copy244) (bond c032 h133-copy245) (bond c032 h133-copy246) (bond c032 h133-copy247) (bond c032 h133-copy248) (bond c032 h133-copy249) (bond c032 h133-copy250) (bond c032 h133-copy251) (bond c032 h133-copy252) (bond c032 h133-copy253) (bond c032 h133-copy254) (bond c032 h133-copy255) (bond c032 h133-copy256) (bond c032 h133-copy257) (bond c032 h133-copy258) (bond c032 h133-copy259) (bond c032 h133-copy260) (bond c032 h133-copy261) (bond c032 h133-copy262) (bond c032 h133-copy263) (bond c032 h133-copy264) (bond c032 h133-copy265) (bond c032 h133-copy266) (bond c032 h133-copy267) (bond c032 h133-copy268) (bond c032 h133-copy269) (bond c032 h133-copy270) (bond c032 h133-copy271) (bond c032 h133-copy272) (bond c032 h133-copy273) (bond c032 h133-copy274) (bond c032 h133-copy275) (bond c032 h133-copy276) (bond c032 h133-copy277) (bond c032 h133-copy278) (bond c032 h133-copy279) (bond c032 h133-copy280) (bond c032 h133-copy281) (bond c032 h133-copy282) (bond c032 h133-copy283) (bond c032 h133-copy284) (bond c032 h133-copy285) (bond c032 h133-copy286) (bond c032 h133-copy287) (bond c032 h133-copy288) (bond c032 h133-copy289) (bond c032 h133-copy290) (bond c032 h133-copy291) (bond c032 h133-copy292) (bond c032 h133-copy293) (bond c032 h133-copy294) (bond c032 h133-copy295) (bond c032 h133-copy296) (bond c032 h133-copy297) (bond c032 h133-copy298) (bond c032 h133-copy299) (bond c032 h133-copy300) (bond c032 h133-copy301) (bond c032 h133-copy302) (bond c032 h133-copy303) (bond c032 h133-copy304) (bond c032 h133-copy305) (bond c032 h133-copy306) (bond c032 h133-copy307) (bond c032 h133-copy308) (bond c032 h133-copy309) (bond c032 h133-copy310) (bond c032 h133-copy311) (bond c032 h133-copy312) (bond c032 h133-copy313) (bond c032 h133-copy314) (bond c032 h133-copy315) (bond c032 h133-copy316) (bond c032 h133-copy317) (bond c032 h133-copy318) (bond c032 h133-copy319) (bond c032 h133-copy320) (bond c032 h133-copy321) (bond c032 h133-copy322) (bond c032 h133-copy323) (bond c032 h133-copy324) (bond c032 h133-copy325) (bond c032 h133-copy326) (bond c032 h133-copy327) (bond c032 h133-copy328) (bond c032 h133-copy329) (bond c032 h133-copy330) (bond c032 h133-copy331) (bond c032 h133-copy332) (bond c032 h133-copy333) (bond c032 h133-copy334) (bond c032 h133-copy335) (bond c032 h133-copy336) (bond c032 h133-copy337) (bond c032 h133-copy338) (bond c032 h133-copy339) (bond c032 h133-copy340) (bond c032 h133-copy341) (bond c032 h133-copy342) (bond c032 h133-copy343) (bond c032 h133-copy344) (bond c032 h133-copy345) (bond c032 h133-copy346) (bond c032 h133-copy347) (bond c032 h133-copy348) (bond c032 h133-copy349) (bond c032 h133-copy350) (bond c032 h133-copy351) (bond c032 h133-copy352) (bond c032 h133-copy353) (bond c032 h133-copy354) (bond c032 h133-copy355) (bond c032 h133-copy356) (bond c032 h133-copy357) (bond c032 h133-copy358) (bond c032 h133-copy359) (bond c032 h133-copy360) (bond c032 h133-copy361) (bond c032 h133-copy362) (bond c032 h133-copy363) (bond c032 h133-copy364) (bond c032 h133-copy365) (bond c032 h133-copy366) (bond c032 h133-copy367) (bond c032 h133-copy368) (bond c032 h133-copy369) (bond c032 h133-copy370) (bond c032 h133-copy371) (bond c032 h133-copy372) (bond c032 h133-copy373) (bond c032 h133-copy374) (bond c032 h133-copy375) (bond c032 h133-copy376) (bond c032 h133-copy377) (bond c032 h133-copy378) (bond c032 h133-copy379) (bond c032 h133-copy380) (bond c032 h133-copy381) (bond c032 h133-copy382) (bond c032 h133-copy383) (bond c032 h133-copy384) (bond c032 h133-copy385) (bond c032 h133-copy386) (bond c032 h133-copy387) (bond c032 h133-copy388) (bond c032 h133-copy389) (bond c032 h133-copy390) (bond c032 h133-copy391) (bond c032 h133-copy392) (bond c032 h133-copy393) (bond c032 h133-copy394) (bond c032 h133-copy395) (bond c032 h133-copy396) (bond c032 h133-copy397) (bond c032 h133-copy398) (bond c032 h133-copy399) (bond c032 h133-copy400) (bond c032 h133-copy401) (bond c032 h133-copy402) (bond c032 h133-copy403) (bond c032 h133-copy404) (bond c032 h133-copy405) (bond c032 h133-copy406) (bond c032 h133-copy407) (bond c032 h133-copy408) (bond c032 h133-copy409) (bond c032 h133-copy410) (bond c032 h133-copy411) (bond c032 h133-copy412) (bond c032 h133-copy413) (bond c032 h133-copy414) (bond c032 h133-copy415) (bond c032 h133-copy416) (bond c032 h133-copy417) (bond c032 h133-copy418) (bond c032 h133-copy419) (bond c032 h133-copy420) (bond c032 h133-copy421) (bond c032 h133-copy422) (bond c032 h133-copy423) (bond c032 h133-copy424) (bond c032 h133-copy425) (bond c032 h133-copy426) (bond c032 h133-copy427) (bond c032 h133-copy428) (bond c032 h133-copy429) (bond c032 h133-copy430) (bond c032 h133-copy431) (bond c032 h133-copy432) (bond c032 h133-copy433) (bond c032 h133-copy434) (bond c032 h133-copy435) (bond c032 h133-copy436) (bond c032 h133-copy437) (bond c032 h133-copy438) (bond c032 h133-copy439) (bond c032 h133-copy440) (bond c032 h133-copy441) (bond c032 h133-copy442) (bond c032 h133-copy443) (bond c032 h133-copy444) (bond c032 h133-copy445) (bond c032 h133-copy446) (bond c032 h133-copy447) (bond c032 h133-copy448) (bond c032 h133-copy449) (bond c032 h133-copy450) (bond c032 h133-copy451) (bond c032 h133-copy452) (bond c032 h133-copy453) (bond c032 h133-copy454) (bond c032 h133-copy455) (bond c032 h133-copy456) (bond c032 h133-copy457) (bond c032 h133-copy458) (bond c032 h133-copy459) (bond c032 h133-copy460) (bond c032 h133-copy461) (bond c032 h133-copy462) (bond c032 h133-copy463) (bond c032 h133-copy464) (bond c032 h133-copy465) (bond c032 h133-copy466) (bond c032 h133-copy467) (bond c032 h133-copy468) (bond c032 h133-copy469) (bond c032 h133-copy470) (bond c032 h133-copy471) (bond c032 h133-copy472) (bond c032 h133-copy473) (bond c032 h133-copy474) (bond c032 h133-copy475) (bond c032 h133-copy476) (bond c032 h133-copy477) (bond c032 h133-copy478) (bond c032 h133-copy479) (bond c032 h133-copy480) (bond c032 h133-copy481) (bond c032 h133-copy482) (bond c032 h133-copy483) (bond c032 h133-copy484) (bond c032 h133-copy485) (bond c032 h133-copy486) (bond c032 h133-copy487) (bond c032 h133-copy488) (bond c032 h133-copy489) (bond c032 h133-copy490) (bond c032 h133-copy491) (bond c032 h133-copy492) (bond c032 h133-copy493) (bond c032 h133-copy494) (bond c032 h133-copy495) (bond c032 h133-copy496) (bond c032 h133-copy497) (bond c032 h133-copy498)
(bond h133 c032) (bond h133-copy1 c032) (bond h133-copy2 c032) (bond h133-copy3 c032) (bond h133-copy4 c032) (bond h133-copy5 c032) (bond h133-copy6 c032) (bond h133-copy7 c032) (bond h133-copy8 c032) (bond h133-copy9 c032) (bond h133-copy10 c032) (bond h133-copy11 c032) (bond h133-copy12 c032) (bond h133-copy13 c032) (bond h133-copy14 c032) (bond h133-copy15 c032) (bond h133-copy16 c032) (bond h133-copy17 c032) (bond h133-copy18 c032) (bond h133-copy19 c032) (bond h133-copy20 c032) (bond h133-copy21 c032) (bond h133-copy22 c032) (bond h133-copy23 c032) (bond h133-copy24 c032) (bond h133-copy25 c032) (bond h133-copy26 c032) (bond h133-copy27 c032) (bond h133-copy28 c032) (bond h133-copy29 c032) (bond h133-copy30 c032) (bond h133-copy31 c032) (bond h133-copy32 c032) (bond h133-copy33 c032) (bond h133-copy34 c032) (bond h133-copy35 c032) (bond h133-copy36 c032) (bond h133-copy37 c032) (bond h133-copy38 c032) (bond h133-copy39 c032) (bond h133-copy40 c032) (bond h133-copy41 c032) (bond h133-copy42 c032) (bond h133-copy43 c032) (bond h133-copy44 c032) (bond h133-copy45 c032) (bond h133-copy46 c032) (bond h133-copy47 c032) (bond h133-copy48 c032) (bond h133-copy49 c032) (bond h133-copy50 c032) (bond h133-copy51 c032) (bond h133-copy52 c032) (bond h133-copy53 c032) (bond h133-copy54 c032) (bond h133-copy55 c032) (bond h133-copy56 c032) (bond h133-copy57 c032) (bond h133-copy58 c032) (bond h133-copy59 c032) (bond h133-copy60 c032) (bond h133-copy61 c032) (bond h133-copy62 c032) (bond h133-copy63 c032) (bond h133-copy64 c032) (bond h133-copy65 c032) (bond h133-copy66 c032) (bond h133-copy67 c032) (bond h133-copy68 c032) (bond h133-copy69 c032) (bond h133-copy70 c032) (bond h133-copy71 c032) (bond h133-copy72 c032) (bond h133-copy73 c032) (bond h133-copy74 c032) (bond h133-copy75 c032) (bond h133-copy76 c032) (bond h133-copy77 c032) (bond h133-copy78 c032) (bond h133-copy79 c032) (bond h133-copy80 c032) (bond h133-copy81 c032) (bond h133-copy82 c032) (bond h133-copy83 c032) (bond h133-copy84 c032) (bond h133-copy85 c032) (bond h133-copy86 c032) (bond h133-copy87 c032) (bond h133-copy88 c032) (bond h133-copy89 c032) (bond h133-copy90 c032) (bond h133-copy91 c032) (bond h133-copy92 c032) (bond h133-copy93 c032) (bond h133-copy94 c032) (bond h133-copy95 c032) (bond h133-copy96 c032) (bond h133-copy97 c032) (bond h133-copy98 c032) (bond h133-copy99 c032) (bond h133-copy100 c032) (bond h133-copy101 c032) (bond h133-copy102 c032) (bond h133-copy103 c032) (bond h133-copy104 c032) (bond h133-copy105 c032) (bond h133-copy106 c032) (bond h133-copy107 c032) (bond h133-copy108 c032) (bond h133-copy109 c032) (bond h133-copy110 c032) (bond h133-copy111 c032) (bond h133-copy112 c032) (bond h133-copy113 c032) (bond h133-copy114 c032) (bond h133-copy115 c032) (bond h133-copy116 c032) (bond h133-copy117 c032) (bond h133-copy118 c032) (bond h133-copy119 c032) (bond h133-copy120 c032) (bond h133-copy121 c032) (bond h133-copy122 c032) (bond h133-copy123 c032) (bond h133-copy124 c032) (bond h133-copy125 c032) (bond h133-copy126 c032) (bond h133-copy127 c032) (bond h133-copy128 c032) (bond h133-copy129 c032) (bond h133-copy130 c032) (bond h133-copy131 c032) (bond h133-copy132 c032) (bond h133-copy133 c032) (bond h133-copy134 c032) (bond h133-copy135 c032) (bond h133-copy136 c032) (bond h133-copy137 c032) (bond h133-copy138 c032) (bond h133-copy139 c032) (bond h133-copy140 c032) (bond h133-copy141 c032) (bond h133-copy142 c032) (bond h133-copy143 c032) (bond h133-copy144 c032) (bond h133-copy145 c032) (bond h133-copy146 c032) (bond h133-copy147 c032) (bond h133-copy148 c032) (bond h133-copy149 c032) (bond h133-copy150 c032) (bond h133-copy151 c032) (bond h133-copy152 c032) (bond h133-copy153 c032) (bond h133-copy154 c032) (bond h133-copy155 c032) (bond h133-copy156 c032) (bond h133-copy157 c032) (bond h133-copy158 c032) (bond h133-copy159 c032) (bond h133-copy160 c032) (bond h133-copy161 c032) (bond h133-copy162 c032) (bond h133-copy163 c032) (bond h133-copy164 c032) (bond h133-copy165 c032) (bond h133-copy166 c032) (bond h133-copy167 c032) (bond h133-copy168 c032) (bond h133-copy169 c032) (bond h133-copy170 c032) (bond h133-copy171 c032) (bond h133-copy172 c032) (bond h133-copy173 c032) (bond h133-copy174 c032) (bond h133-copy175 c032) (bond h133-copy176 c032) (bond h133-copy177 c032) (bond h133-copy178 c032) (bond h133-copy179 c032) (bond h133-copy180 c032) (bond h133-copy181 c032) (bond h133-copy182 c032) (bond h133-copy183 c032) (bond h133-copy184 c032) (bond h133-copy185 c032) (bond h133-copy186 c032) (bond h133-copy187 c032) (bond h133-copy188 c032) (bond h133-copy189 c032) (bond h133-copy190 c032) (bond h133-copy191 c032) (bond h133-copy192 c032) (bond h133-copy193 c032) (bond h133-copy194 c032) (bond h133-copy195 c032) (bond h133-copy196 c032) (bond h133-copy197 c032) (bond h133-copy198 c032) (bond h133-copy199 c032) (bond h133-copy200 c032) (bond h133-copy201 c032) (bond h133-copy202 c032) (bond h133-copy203 c032) (bond h133-copy204 c032) (bond h133-copy205 c032) (bond h133-copy206 c032) (bond h133-copy207 c032) (bond h133-copy208 c032) (bond h133-copy209 c032) (bond h133-copy210 c032) (bond h133-copy211 c032) (bond h133-copy212 c032) (bond h133-copy213 c032) (bond h133-copy214 c032) (bond h133-copy215 c032) (bond h133-copy216 c032) (bond h133-copy217 c032) (bond h133-copy218 c032) (bond h133-copy219 c032) (bond h133-copy220 c032) (bond h133-copy221 c032) (bond h133-copy222 c032) (bond h133-copy223 c032) (bond h133-copy224 c032) (bond h133-copy225 c032) (bond h133-copy226 c032) (bond h133-copy227 c032) (bond h133-copy228 c032) (bond h133-copy229 c032) (bond h133-copy230 c032) (bond h133-copy231 c032) (bond h133-copy232 c032) (bond h133-copy233 c032) (bond h133-copy234 c032) (bond h133-copy235 c032) (bond h133-copy236 c032) (bond h133-copy237 c032) (bond h133-copy238 c032) (bond h133-copy239 c032) (bond h133-copy240 c032) (bond h133-copy241 c032) (bond h133-copy242 c032) (bond h133-copy243 c032) (bond h133-copy244 c032) (bond h133-copy245 c032) (bond h133-copy246 c032) (bond h133-copy247 c032) (bond h133-copy248 c032) (bond h133-copy249 c032) (bond h133-copy250 c032) (bond h133-copy251 c032) (bond h133-copy252 c032) (bond h133-copy253 c032) (bond h133-copy254 c032) (bond h133-copy255 c032) (bond h133-copy256 c032) (bond h133-copy257 c032) (bond h133-copy258 c032) (bond h133-copy259 c032) (bond h133-copy260 c032) (bond h133-copy261 c032) (bond h133-copy262 c032) (bond h133-copy263 c032) (bond h133-copy264 c032) (bond h133-copy265 c032) (bond h133-copy266 c032) (bond h133-copy267 c032) (bond h133-copy268 c032) (bond h133-copy269 c032) (bond h133-copy270 c032) (bond h133-copy271 c032) (bond h133-copy272 c032) (bond h133-copy273 c032) (bond h133-copy274 c032) (bond h133-copy275 c032) (bond h133-copy276 c032) (bond h133-copy277 c032) (bond h133-copy278 c032) (bond h133-copy279 c032) (bond h133-copy280 c032) (bond h133-copy281 c032) (bond h133-copy282 c032) (bond h133-copy283 c032) (bond h133-copy284 c032) (bond h133-copy285 c032) (bond h133-copy286 c032) (bond h133-copy287 c032) (bond h133-copy288 c032) (bond h133-copy289 c032) (bond h133-copy290 c032) (bond h133-copy291 c032) (bond h133-copy292 c032) (bond h133-copy293 c032) (bond h133-copy294 c032) (bond h133-copy295 c032) (bond h133-copy296 c032) (bond h133-copy297 c032) (bond h133-copy298 c032) (bond h133-copy299 c032) (bond h133-copy300 c032) (bond h133-copy301 c032) (bond h133-copy302 c032) (bond h133-copy303 c032) (bond h133-copy304 c032) (bond h133-copy305 c032) (bond h133-copy306 c032) (bond h133-copy307 c032) (bond h133-copy308 c032) (bond h133-copy309 c032) (bond h133-copy310 c032) (bond h133-copy311 c032) (bond h133-copy312 c032) (bond h133-copy313 c032) (bond h133-copy314 c032) (bond h133-copy315 c032) (bond h133-copy316 c032) (bond h133-copy317 c032) (bond h133-copy318 c032) (bond h133-copy319 c032) (bond h133-copy320 c032) (bond h133-copy321 c032) (bond h133-copy322 c032) (bond h133-copy323 c032) (bond h133-copy324 c032) (bond h133-copy325 c032) (bond h133-copy326 c032) (bond h133-copy327 c032) (bond h133-copy328 c032) (bond h133-copy329 c032) (bond h133-copy330 c032) (bond h133-copy331 c032) (bond h133-copy332 c032) (bond h133-copy333 c032) (bond h133-copy334 c032) (bond h133-copy335 c032) (bond h133-copy336 c032) (bond h133-copy337 c032) (bond h133-copy338 c032) (bond h133-copy339 c032) (bond h133-copy340 c032) (bond h133-copy341 c032) (bond h133-copy342 c032) (bond h133-copy343 c032) (bond h133-copy344 c032) (bond h133-copy345 c032) (bond h133-copy346 c032) (bond h133-copy347 c032) (bond h133-copy348 c032) (bond h133-copy349 c032) (bond h133-copy350 c032) (bond h133-copy351 c032) (bond h133-copy352 c032) (bond h133-copy353 c032) (bond h133-copy354 c032) (bond h133-copy355 c032) (bond h133-copy356 c032) (bond h133-copy357 c032) (bond h133-copy358 c032) (bond h133-copy359 c032) (bond h133-copy360 c032) (bond h133-copy361 c032) (bond h133-copy362 c032) (bond h133-copy363 c032) (bond h133-copy364 c032) (bond h133-copy365 c032) (bond h133-copy366 c032) (bond h133-copy367 c032) (bond h133-copy368 c032) (bond h133-copy369 c032) (bond h133-copy370 c032) (bond h133-copy371 c032) (bond h133-copy372 c032) (bond h133-copy373 c032) (bond h133-copy374 c032) (bond h133-copy375 c032) (bond h133-copy376 c032) (bond h133-copy377 c032) (bond h133-copy378 c032) (bond h133-copy379 c032) (bond h133-copy380 c032) (bond h133-copy381 c032) (bond h133-copy382 c032) (bond h133-copy383 c032) (bond h133-copy384 c032) (bond h133-copy385 c032) (bond h133-copy386 c032) (bond h133-copy387 c032) (bond h133-copy388 c032) (bond h133-copy389 c032) (bond h133-copy390 c032) (bond h133-copy391 c032) (bond h133-copy392 c032) (bond h133-copy393 c032) (bond h133-copy394 c032) (bond h133-copy395 c032) (bond h133-copy396 c032) (bond h133-copy397 c032) (bond h133-copy398 c032) (bond h133-copy399 c032) (bond h133-copy400 c032) (bond h133-copy401 c032) (bond h133-copy402 c032) (bond h133-copy403 c032) (bond h133-copy404 c032) (bond h133-copy405 c032) (bond h133-copy406 c032) (bond h133-copy407 c032) (bond h133-copy408 c032) (bond h133-copy409 c032) (bond h133-copy410 c032) (bond h133-copy411 c032) (bond h133-copy412 c032) (bond h133-copy413 c032) (bond h133-copy414 c032) (bond h133-copy415 c032) (bond h133-copy416 c032) (bond h133-copy417 c032) (bond h133-copy418 c032) (bond h133-copy419 c032) (bond h133-copy420 c032) (bond h133-copy421 c032) (bond h133-copy422 c032) (bond h133-copy423 c032) (bond h133-copy424 c032) (bond h133-copy425 c032) (bond h133-copy426 c032) (bond h133-copy427 c032) (bond h133-copy428 c032) (bond h133-copy429 c032) (bond h133-copy430 c032) (bond h133-copy431 c032) (bond h133-copy432 c032) (bond h133-copy433 c032) (bond h133-copy434 c032) (bond h133-copy435 c032) (bond h133-copy436 c032) (bond h133-copy437 c032) (bond h133-copy438 c032) (bond h133-copy439 c032) (bond h133-copy440 c032) (bond h133-copy441 c032) (bond h133-copy442 c032) (bond h133-copy443 c032) (bond h133-copy444 c032) (bond h133-copy445 c032) (bond h133-copy446 c032) (bond h133-copy447 c032) (bond h133-copy448 c032) (bond h133-copy449 c032) (bond h133-copy450 c032) (bond h133-copy451 c032) (bond h133-copy452 c032) (bond h133-copy453 c032) (bond h133-copy454 c032) (bond h133-copy455 c032) (bond h133-copy456 c032) (bond h133-copy457 c032) (bond h133-copy458 c032) (bond h133-copy459 c032) (bond h133-copy460 c032) (bond h133-copy461 c032) (bond h133-copy462 c032) (bond h133-copy463 c032) (bond h133-copy464 c032) (bond h133-copy465 c032) (bond h133-copy466 c032) (bond h133-copy467 c032) (bond h133-copy468 c032) (bond h133-copy469 c032) (bond h133-copy470 c032) (bond h133-copy471 c032) (bond h133-copy472 c032) (bond h133-copy473 c032) (bond h133-copy474 c032) (bond h133-copy475 c032) (bond h133-copy476 c032) (bond h133-copy477 c032) (bond h133-copy478 c032) (bond h133-copy479 c032) (bond h133-copy480 c032) (bond h133-copy481 c032) (bond h133-copy482 c032) (bond h133-copy483 c032) (bond h133-copy484 c032) (bond h133-copy485 c032) (bond h133-copy486 c032) (bond h133-copy487 c032) (bond h133-copy488 c032) (bond h133-copy489 c032) (bond h133-copy490 c032) (bond h133-copy491 c032) (bond h133-copy492 c032) (bond h133-copy493 c032) (bond h133-copy494 c032) (bond h133-copy495 c032) (bond h133-copy496 c032) (bond h133-copy497 c032) (bond h133-copy498 c032)

(bond c033 c034)
(bond c034 c033)

(bond c033 c038)
(bond c038 c033)

(bond c033 o065)
(bond o065 c033)

(bond c034 c035)
(bond c035 c034)

(bond c034 h136)
(bond h136 c034)

(bond c034 h135)
(bond h135 c034)

(bond c035 c036)
(bond c036 c035)

(bond c035 h137)
(bond h137 c035)

(bond c035 h138)
(bond h138 c035)

(bond c036 c037)
(bond c037 c036)

(bond c036 h139)
(bond h139 c036)

(bond c036 h140)
(bond h140 c036)

(bond c037 c038)
(bond c038 c037)

(bond c037 h141)
(bond h141 c037)

(bond c037 h142)
(bond h142 c037)

(bond c038 h143)
(bond h143 c038)

(bond c038 h144)
(bond h144 c038)

(bond c051 o065)
(bond o065 c051)

(bond c051 c052)
(bond c052 c051)

(bond c051 h167)
(bond h167 c051)

(bond c051 h166)
(bond h166 c051)

(bond c052 c053)
(bond c053 c052)

(bond c052 h060)
(bond h060 c052)

(bond c052 h168)
(bond h168 c052)

(bond c053 c054)
(bond c054 c053)

(bond c053 h169)
(bond h169 c053)

(bond c053 h170)
(bond h170 c053)

(bond c054 c055)
(bond c055 c054)

(bond c054 h171)
(bond h171 c054)

(bond c054 h172)
(bond h172 c054)

(bond c055 h174)
(bond h174 c055)

(bond c055 h173)
(bond h173 c055)

(bond c055 h175)
(bond h175 c055)
)
)
)