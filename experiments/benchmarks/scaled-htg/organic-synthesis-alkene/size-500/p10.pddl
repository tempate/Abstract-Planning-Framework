; The variants of the Organic Synthesis domain were created by
; Dr. Russell Viirre, Hadi Qovaizi, and Prof. Mikhail Soutchanski.
;
; This work is licensed under a Creative Commons Attribution,
; NonCommercial, ShareAlike 3.0 Unported License.
;
; For further information, please access the following web page:
; https://www.cs.ryerson.ca/~mes/publications/
(define (problem Alkene_P10) (:domain Chemical)
(:objects
c019 - carbon
c020 - carbon
c021 - carbon
c022 - carbon
c023 - carbon
c024 - carbon
c039 - carbon
c040 - carbon
c041 - carbon
c042 - carbon
c043 - carbon
c044 - carbon
c045 - carbon
c046 - carbon
c047 - carbon
c048 - carbon
c049 - carbon
c050 - carbon
cl073 - chlorine
h059 - hydrogen
h060 - hydrogen
h145 - hydrogen
h146 - hydrogen
h147 - hydrogen
h148 - hydrogen
h149 - hydrogen
h150 - hydrogen
h151 - hydrogen
h152 - hydrogen
h153 - hydrogen
h154 - hydrogen
h155 - hydrogen
h156 - hydrogen
h157 - hydrogen
h158 - hydrogen
h159 - hydrogen
h160 - hydrogen
h161 - hydrogen
h162 - hydrogen
h163 - hydrogen
h164 - hydrogen
h165 - hydrogen
h176 - hydrogen
o065 - oxygen
o068 o068-copy1 o068-copy2 o068-copy3 o068-copy4 o068-copy5 o068-copy6 o068-copy7 o068-copy8 o068-copy9 o068-copy10 o068-copy11 o068-copy12 o068-copy13 o068-copy14 o068-copy15 o068-copy16 o068-copy17 o068-copy18 o068-copy19 o068-copy20 o068-copy21 o068-copy22 o068-copy23 o068-copy24 o068-copy25 o068-copy26 o068-copy27 o068-copy28 o068-copy29 o068-copy30 o068-copy31 o068-copy32 o068-copy33 o068-copy34 o068-copy35 o068-copy36 o068-copy37 o068-copy38 o068-copy39 o068-copy40 o068-copy41 o068-copy42 o068-copy43 o068-copy44 o068-copy45 o068-copy46 o068-copy47 o068-copy48 o068-copy49 o068-copy50 o068-copy51 o068-copy52 o068-copy53 o068-copy54 o068-copy55 o068-copy56 o068-copy57 o068-copy58 o068-copy59 o068-copy60 o068-copy61 o068-copy62 o068-copy63 o068-copy64 o068-copy65 o068-copy66 o068-copy67 o068-copy68 o068-copy69 o068-copy70 o068-copy71 o068-copy72 o068-copy73 o068-copy74 o068-copy75 o068-copy76 o068-copy77 o068-copy78 o068-copy79 o068-copy80 o068-copy81 o068-copy82 o068-copy83 o068-copy84 o068-copy85 o068-copy86 o068-copy87 o068-copy88 o068-copy89 o068-copy90 o068-copy91 o068-copy92 o068-copy93 o068-copy94 o068-copy95 o068-copy96 o068-copy97 o068-copy98 o068-copy99 o068-copy100 o068-copy101 o068-copy102 o068-copy103 o068-copy104 o068-copy105 o068-copy106 o068-copy107 o068-copy108 o068-copy109 o068-copy110 o068-copy111 o068-copy112 o068-copy113 o068-copy114 o068-copy115 o068-copy116 o068-copy117 o068-copy118 o068-copy119 o068-copy120 o068-copy121 o068-copy122 o068-copy123 o068-copy124 o068-copy125 o068-copy126 o068-copy127 o068-copy128 o068-copy129 o068-copy130 o068-copy131 o068-copy132 o068-copy133 o068-copy134 o068-copy135 o068-copy136 o068-copy137 o068-copy138 o068-copy139 o068-copy140 o068-copy141 o068-copy142 o068-copy143 o068-copy144 o068-copy145 o068-copy146 o068-copy147 o068-copy148 o068-copy149 o068-copy150 o068-copy151 o068-copy152 o068-copy153 o068-copy154 o068-copy155 o068-copy156 o068-copy157 o068-copy158 o068-copy159 o068-copy160 o068-copy161 o068-copy162 o068-copy163 o068-copy164 o068-copy165 o068-copy166 o068-copy167 o068-copy168 o068-copy169 o068-copy170 o068-copy171 o068-copy172 o068-copy173 o068-copy174 o068-copy175 o068-copy176 o068-copy177 o068-copy178 o068-copy179 o068-copy180 o068-copy181 o068-copy182 o068-copy183 o068-copy184 o068-copy185 o068-copy186 o068-copy187 o068-copy188 o068-copy189 o068-copy190 o068-copy191 o068-copy192 o068-copy193 o068-copy194 o068-copy195 o068-copy196 o068-copy197 o068-copy198 o068-copy199 o068-copy200 o068-copy201 o068-copy202 o068-copy203 o068-copy204 o068-copy205 o068-copy206 o068-copy207 o068-copy208 o068-copy209 o068-copy210 o068-copy211 o068-copy212 o068-copy213 o068-copy214 o068-copy215 o068-copy216 o068-copy217 o068-copy218 o068-copy219 o068-copy220 o068-copy221 o068-copy222 o068-copy223 o068-copy224 o068-copy225 o068-copy226 o068-copy227 o068-copy228 o068-copy229 o068-copy230 o068-copy231 o068-copy232 o068-copy233 o068-copy234 o068-copy235 o068-copy236 o068-copy237 o068-copy238 o068-copy239 o068-copy240 o068-copy241 o068-copy242 o068-copy243 o068-copy244 o068-copy245 o068-copy246 o068-copy247 o068-copy248 o068-copy249 o068-copy250 o068-copy251 o068-copy252 o068-copy253 o068-copy254 o068-copy255 o068-copy256 o068-copy257 o068-copy258 o068-copy259 o068-copy260 o068-copy261 o068-copy262 o068-copy263 o068-copy264 o068-copy265 o068-copy266 o068-copy267 o068-copy268 o068-copy269 o068-copy270 o068-copy271 o068-copy272 o068-copy273 o068-copy274 o068-copy275 o068-copy276 o068-copy277 o068-copy278 o068-copy279 o068-copy280 o068-copy281 o068-copy282 o068-copy283 o068-copy284 o068-copy285 o068-copy286 o068-copy287 o068-copy288 o068-copy289 o068-copy290 o068-copy291 o068-copy292 o068-copy293 o068-copy294 o068-copy295 o068-copy296 o068-copy297 o068-copy298 o068-copy299 o068-copy300 o068-copy301 o068-copy302 o068-copy303 o068-copy304 o068-copy305 o068-copy306 o068-copy307 o068-copy308 o068-copy309 o068-copy310 o068-copy311 o068-copy312 o068-copy313 o068-copy314 o068-copy315 o068-copy316 o068-copy317 o068-copy318 o068-copy319 o068-copy320 o068-copy321 o068-copy322 o068-copy323 o068-copy324 o068-copy325 o068-copy326 o068-copy327 o068-copy328 o068-copy329 o068-copy330 o068-copy331 o068-copy332 o068-copy333 o068-copy334 o068-copy335 o068-copy336 o068-copy337 o068-copy338 o068-copy339 o068-copy340 o068-copy341 o068-copy342 o068-copy343 o068-copy344 o068-copy345 o068-copy346 o068-copy347 o068-copy348 o068-copy349 o068-copy350 o068-copy351 o068-copy352 o068-copy353 o068-copy354 o068-copy355 o068-copy356 o068-copy357 o068-copy358 o068-copy359 o068-copy360 o068-copy361 o068-copy362 o068-copy363 o068-copy364 o068-copy365 o068-copy366 o068-copy367 o068-copy368 o068-copy369 o068-copy370 o068-copy371 o068-copy372 o068-copy373 o068-copy374 o068-copy375 o068-copy376 o068-copy377 o068-copy378 o068-copy379 o068-copy380 o068-copy381 o068-copy382 o068-copy383 o068-copy384 o068-copy385 o068-copy386 o068-copy387 o068-copy388 o068-copy389 o068-copy390 o068-copy391 o068-copy392 o068-copy393 o068-copy394 o068-copy395 o068-copy396 o068-copy397 o068-copy398 o068-copy399 o068-copy400 o068-copy401 o068-copy402 o068-copy403 o068-copy404 o068-copy405 o068-copy406 o068-copy407 o068-copy408 o068-copy409 o068-copy410 o068-copy411 o068-copy412 o068-copy413 o068-copy414 o068-copy415 o068-copy416 o068-copy417 o068-copy418 o068-copy419 o068-copy420 o068-copy421 o068-copy422 o068-copy423 o068-copy424 o068-copy425 o068-copy426 o068-copy427 o068-copy428 o068-copy429 o068-copy430 o068-copy431 o068-copy432 o068-copy433 o068-copy434 o068-copy435 o068-copy436 o068-copy437 o068-copy438 o068-copy439 o068-copy440 o068-copy441 o068-copy442 o068-copy443 o068-copy444 o068-copy445 o068-copy446 o068-copy447 o068-copy448 o068-copy449 o068-copy450 o068-copy451 o068-copy452 o068-copy453 o068-copy454 o068-copy455 o068-copy456 o068-copy457 o068-copy458 o068-copy459 o068-copy460 o068-copy461 o068-copy462 o068-copy463 o068-copy464 o068-copy465 o068-copy466 o068-copy467 o068-copy468 o068-copy469 o068-copy470 o068-copy471 o068-copy472 o068-copy473 o068-copy474 o068-copy475 o068-copy476 o068-copy477 o068-copy478 o068-copy479 o068-copy480 o068-copy481 o068-copy482 o068-copy483 o068-copy484 o068-copy485 o068-copy486 o068-copy487 o068-copy488 o068-copy489 o068-copy490 o068-copy491 o068-copy492 o068-copy493 o068-copy494 o068-copy495 o068-copy496 o068-copy497 o068-copy498 - oxygen
o069 - oxygen
o070 - oxygen
s072 - sulfur
)
(:init
(doublebond c019 c024)
(doublebond c024 c019)

(bond c019 c020)
(bond c020 c019)

(doublebond c020 c021)
(doublebond c021 c020)

(bond c021 s072)
(bond s072 c021)

(bond c021 c022)
(bond c022 c021)

(doublebond c022 c023)
(doublebond c023 c022)

(bond c023 c024)
(bond c024 c023)

(bond c039 h147)
(bond h147 c039)

(bond c039 h146)
(bond h146 c039)

(bond c039 h145)
(bond h145 c039)

(bond c039 c040)
(bond c040 c039)

(bond c040 h060)
(bond h060 c040)

(bond c040 c041)
(bond c041 c040)

(bond c040 c045)
(bond c045 c040)

(bond c041 o065)
(bond o065 c041)

(bond c041 h148)
(bond h148 c041)

(bond c041 c042)
(bond c042 c041)

(bond c042 h150)
(bond h150 c042)

(bond c042 h149)
(bond h149 c042)

(bond c042 c043)
(bond c043 c042)

(bond c043 h152)
(bond h152 c043)

(bond c043 h151)
(bond h151 c043)

(bond c043 c044)
(bond c044 c043)

(bond c044 h154)
(bond h154 c044)

(bond c044 h153)
(bond h153 c044)

(bond c044 c045)
(bond c045 c044)

(bond c045 h156)
(bond h156 c045)

(bond c045 h155)
(bond h155 c045)

(doublebond c046 c047)
(doublebond c047 c046)

(bond c046 h158)
(bond h158 c046)

(bond c046 h157)
(bond h157 c046)

(bond c047 h159)
(bond h159 c047)

(bond c047 c048)
(bond c048 c047)

(bond c048 c049)
(bond c049 c048)

(bond c048 h161)
(bond h161 c048)

(bond c048 h160)
(bond h160 c048)

(bond c049 h163)
(bond h163 c049)

(bond c049 h162)
(bond h162 c049)

(bond c049 c050)
(bond c050 c049)

(bond c050 h165)
(bond h165 c050)

(bond c050 h164)
(bond h164 c050)

(bond c050 o070)
(bond o070 c050)

(bond cl073 s072)
(bond s072 cl073)

(bond h059 o065)
(bond o065 h059)

(bond h176 o070)
(bond o070 h176)

(doublebond o068 s072) (doublebond o068-copy1 s072) (doublebond o068-copy2 s072) (doublebond o068-copy3 s072) (doublebond o068-copy4 s072) (doublebond o068-copy5 s072) (doublebond o068-copy6 s072) (doublebond o068-copy7 s072) (doublebond o068-copy8 s072) (doublebond o068-copy9 s072) (doublebond o068-copy10 s072) (doublebond o068-copy11 s072) (doublebond o068-copy12 s072) (doublebond o068-copy13 s072) (doublebond o068-copy14 s072) (doublebond o068-copy15 s072) (doublebond o068-copy16 s072) (doublebond o068-copy17 s072) (doublebond o068-copy18 s072) (doublebond o068-copy19 s072) (doublebond o068-copy20 s072) (doublebond o068-copy21 s072) (doublebond o068-copy22 s072) (doublebond o068-copy23 s072) (doublebond o068-copy24 s072) (doublebond o068-copy25 s072) (doublebond o068-copy26 s072) (doublebond o068-copy27 s072) (doublebond o068-copy28 s072) (doublebond o068-copy29 s072) (doublebond o068-copy30 s072) (doublebond o068-copy31 s072) (doublebond o068-copy32 s072) (doublebond o068-copy33 s072) (doublebond o068-copy34 s072) (doublebond o068-copy35 s072) (doublebond o068-copy36 s072) (doublebond o068-copy37 s072) (doublebond o068-copy38 s072) (doublebond o068-copy39 s072) (doublebond o068-copy40 s072) (doublebond o068-copy41 s072) (doublebond o068-copy42 s072) (doublebond o068-copy43 s072) (doublebond o068-copy44 s072) (doublebond o068-copy45 s072) (doublebond o068-copy46 s072) (doublebond o068-copy47 s072) (doublebond o068-copy48 s072) (doublebond o068-copy49 s072) (doublebond o068-copy50 s072) (doublebond o068-copy51 s072) (doublebond o068-copy52 s072) (doublebond o068-copy53 s072) (doublebond o068-copy54 s072) (doublebond o068-copy55 s072) (doublebond o068-copy56 s072) (doublebond o068-copy57 s072) (doublebond o068-copy58 s072) (doublebond o068-copy59 s072) (doublebond o068-copy60 s072) (doublebond o068-copy61 s072) (doublebond o068-copy62 s072) (doublebond o068-copy63 s072) (doublebond o068-copy64 s072) (doublebond o068-copy65 s072) (doublebond o068-copy66 s072) (doublebond o068-copy67 s072) (doublebond o068-copy68 s072) (doublebond o068-copy69 s072) (doublebond o068-copy70 s072) (doublebond o068-copy71 s072) (doublebond o068-copy72 s072) (doublebond o068-copy73 s072) (doublebond o068-copy74 s072) (doublebond o068-copy75 s072) (doublebond o068-copy76 s072) (doublebond o068-copy77 s072) (doublebond o068-copy78 s072) (doublebond o068-copy79 s072) (doublebond o068-copy80 s072) (doublebond o068-copy81 s072) (doublebond o068-copy82 s072) (doublebond o068-copy83 s072) (doublebond o068-copy84 s072) (doublebond o068-copy85 s072) (doublebond o068-copy86 s072) (doublebond o068-copy87 s072) (doublebond o068-copy88 s072) (doublebond o068-copy89 s072) (doublebond o068-copy90 s072) (doublebond o068-copy91 s072) (doublebond o068-copy92 s072) (doublebond o068-copy93 s072) (doublebond o068-copy94 s072) (doublebond o068-copy95 s072) (doublebond o068-copy96 s072) (doublebond o068-copy97 s072) (doublebond o068-copy98 s072) (doublebond o068-copy99 s072) (doublebond o068-copy100 s072) (doublebond o068-copy101 s072) (doublebond o068-copy102 s072) (doublebond o068-copy103 s072) (doublebond o068-copy104 s072) (doublebond o068-copy105 s072) (doublebond o068-copy106 s072) (doublebond o068-copy107 s072) (doublebond o068-copy108 s072) (doublebond o068-copy109 s072) (doublebond o068-copy110 s072) (doublebond o068-copy111 s072) (doublebond o068-copy112 s072) (doublebond o068-copy113 s072) (doublebond o068-copy114 s072) (doublebond o068-copy115 s072) (doublebond o068-copy116 s072) (doublebond o068-copy117 s072) (doublebond o068-copy118 s072) (doublebond o068-copy119 s072) (doublebond o068-copy120 s072) (doublebond o068-copy121 s072) (doublebond o068-copy122 s072) (doublebond o068-copy123 s072) (doublebond o068-copy124 s072) (doublebond o068-copy125 s072) (doublebond o068-copy126 s072) (doublebond o068-copy127 s072) (doublebond o068-copy128 s072) (doublebond o068-copy129 s072) (doublebond o068-copy130 s072) (doublebond o068-copy131 s072) (doublebond o068-copy132 s072) (doublebond o068-copy133 s072) (doublebond o068-copy134 s072) (doublebond o068-copy135 s072) (doublebond o068-copy136 s072) (doublebond o068-copy137 s072) (doublebond o068-copy138 s072) (doublebond o068-copy139 s072) (doublebond o068-copy140 s072) (doublebond o068-copy141 s072) (doublebond o068-copy142 s072) (doublebond o068-copy143 s072) (doublebond o068-copy144 s072) (doublebond o068-copy145 s072) (doublebond o068-copy146 s072) (doublebond o068-copy147 s072) (doublebond o068-copy148 s072) (doublebond o068-copy149 s072) (doublebond o068-copy150 s072) (doublebond o068-copy151 s072) (doublebond o068-copy152 s072) (doublebond o068-copy153 s072) (doublebond o068-copy154 s072) (doublebond o068-copy155 s072) (doublebond o068-copy156 s072) (doublebond o068-copy157 s072) (doublebond o068-copy158 s072) (doublebond o068-copy159 s072) (doublebond o068-copy160 s072) (doublebond o068-copy161 s072) (doublebond o068-copy162 s072) (doublebond o068-copy163 s072) (doublebond o068-copy164 s072) (doublebond o068-copy165 s072) (doublebond o068-copy166 s072) (doublebond o068-copy167 s072) (doublebond o068-copy168 s072) (doublebond o068-copy169 s072) (doublebond o068-copy170 s072) (doublebond o068-copy171 s072) (doublebond o068-copy172 s072) (doublebond o068-copy173 s072) (doublebond o068-copy174 s072) (doublebond o068-copy175 s072) (doublebond o068-copy176 s072) (doublebond o068-copy177 s072) (doublebond o068-copy178 s072) (doublebond o068-copy179 s072) (doublebond o068-copy180 s072) (doublebond o068-copy181 s072) (doublebond o068-copy182 s072) (doublebond o068-copy183 s072) (doublebond o068-copy184 s072) (doublebond o068-copy185 s072) (doublebond o068-copy186 s072) (doublebond o068-copy187 s072) (doublebond o068-copy188 s072) (doublebond o068-copy189 s072) (doublebond o068-copy190 s072) (doublebond o068-copy191 s072) (doublebond o068-copy192 s072) (doublebond o068-copy193 s072) (doublebond o068-copy194 s072) (doublebond o068-copy195 s072) (doublebond o068-copy196 s072) (doublebond o068-copy197 s072) (doublebond o068-copy198 s072) (doublebond o068-copy199 s072) (doublebond o068-copy200 s072) (doublebond o068-copy201 s072) (doublebond o068-copy202 s072) (doublebond o068-copy203 s072) (doublebond o068-copy204 s072) (doublebond o068-copy205 s072) (doublebond o068-copy206 s072) (doublebond o068-copy207 s072) (doublebond o068-copy208 s072) (doublebond o068-copy209 s072) (doublebond o068-copy210 s072) (doublebond o068-copy211 s072) (doublebond o068-copy212 s072) (doublebond o068-copy213 s072) (doublebond o068-copy214 s072) (doublebond o068-copy215 s072) (doublebond o068-copy216 s072) (doublebond o068-copy217 s072) (doublebond o068-copy218 s072) (doublebond o068-copy219 s072) (doublebond o068-copy220 s072) (doublebond o068-copy221 s072) (doublebond o068-copy222 s072) (doublebond o068-copy223 s072) (doublebond o068-copy224 s072) (doublebond o068-copy225 s072) (doublebond o068-copy226 s072) (doublebond o068-copy227 s072) (doublebond o068-copy228 s072) (doublebond o068-copy229 s072) (doublebond o068-copy230 s072) (doublebond o068-copy231 s072) (doublebond o068-copy232 s072) (doublebond o068-copy233 s072) (doublebond o068-copy234 s072) (doublebond o068-copy235 s072) (doublebond o068-copy236 s072) (doublebond o068-copy237 s072) (doublebond o068-copy238 s072) (doublebond o068-copy239 s072) (doublebond o068-copy240 s072) (doublebond o068-copy241 s072) (doublebond o068-copy242 s072) (doublebond o068-copy243 s072) (doublebond o068-copy244 s072) (doublebond o068-copy245 s072) (doublebond o068-copy246 s072) (doublebond o068-copy247 s072) (doublebond o068-copy248 s072) (doublebond o068-copy249 s072) (doublebond o068-copy250 s072) (doublebond o068-copy251 s072) (doublebond o068-copy252 s072) (doublebond o068-copy253 s072) (doublebond o068-copy254 s072) (doublebond o068-copy255 s072) (doublebond o068-copy256 s072) (doublebond o068-copy257 s072) (doublebond o068-copy258 s072) (doublebond o068-copy259 s072) (doublebond o068-copy260 s072) (doublebond o068-copy261 s072) (doublebond o068-copy262 s072) (doublebond o068-copy263 s072) (doublebond o068-copy264 s072) (doublebond o068-copy265 s072) (doublebond o068-copy266 s072) (doublebond o068-copy267 s072) (doublebond o068-copy268 s072) (doublebond o068-copy269 s072) (doublebond o068-copy270 s072) (doublebond o068-copy271 s072) (doublebond o068-copy272 s072) (doublebond o068-copy273 s072) (doublebond o068-copy274 s072) (doublebond o068-copy275 s072) (doublebond o068-copy276 s072) (doublebond o068-copy277 s072) (doublebond o068-copy278 s072) (doublebond o068-copy279 s072) (doublebond o068-copy280 s072) (doublebond o068-copy281 s072) (doublebond o068-copy282 s072) (doublebond o068-copy283 s072) (doublebond o068-copy284 s072) (doublebond o068-copy285 s072) (doublebond o068-copy286 s072) (doublebond o068-copy287 s072) (doublebond o068-copy288 s072) (doublebond o068-copy289 s072) (doublebond o068-copy290 s072) (doublebond o068-copy291 s072) (doublebond o068-copy292 s072) (doublebond o068-copy293 s072) (doublebond o068-copy294 s072) (doublebond o068-copy295 s072) (doublebond o068-copy296 s072) (doublebond o068-copy297 s072) (doublebond o068-copy298 s072) (doublebond o068-copy299 s072) (doublebond o068-copy300 s072) (doublebond o068-copy301 s072) (doublebond o068-copy302 s072) (doublebond o068-copy303 s072) (doublebond o068-copy304 s072) (doublebond o068-copy305 s072) (doublebond o068-copy306 s072) (doublebond o068-copy307 s072) (doublebond o068-copy308 s072) (doublebond o068-copy309 s072) (doublebond o068-copy310 s072) (doublebond o068-copy311 s072) (doublebond o068-copy312 s072) (doublebond o068-copy313 s072) (doublebond o068-copy314 s072) (doublebond o068-copy315 s072) (doublebond o068-copy316 s072) (doublebond o068-copy317 s072) (doublebond o068-copy318 s072) (doublebond o068-copy319 s072) (doublebond o068-copy320 s072) (doublebond o068-copy321 s072) (doublebond o068-copy322 s072) (doublebond o068-copy323 s072) (doublebond o068-copy324 s072) (doublebond o068-copy325 s072) (doublebond o068-copy326 s072) (doublebond o068-copy327 s072) (doublebond o068-copy328 s072) (doublebond o068-copy329 s072) (doublebond o068-copy330 s072) (doublebond o068-copy331 s072) (doublebond o068-copy332 s072) (doublebond o068-copy333 s072) (doublebond o068-copy334 s072) (doublebond o068-copy335 s072) (doublebond o068-copy336 s072) (doublebond o068-copy337 s072) (doublebond o068-copy338 s072) (doublebond o068-copy339 s072) (doublebond o068-copy340 s072) (doublebond o068-copy341 s072) (doublebond o068-copy342 s072) (doublebond o068-copy343 s072) (doublebond o068-copy344 s072) (doublebond o068-copy345 s072) (doublebond o068-copy346 s072) (doublebond o068-copy347 s072) (doublebond o068-copy348 s072) (doublebond o068-copy349 s072) (doublebond o068-copy350 s072) (doublebond o068-copy351 s072) (doublebond o068-copy352 s072) (doublebond o068-copy353 s072) (doublebond o068-copy354 s072) (doublebond o068-copy355 s072) (doublebond o068-copy356 s072) (doublebond o068-copy357 s072) (doublebond o068-copy358 s072) (doublebond o068-copy359 s072) (doublebond o068-copy360 s072) (doublebond o068-copy361 s072) (doublebond o068-copy362 s072) (doublebond o068-copy363 s072) (doublebond o068-copy364 s072) (doublebond o068-copy365 s072) (doublebond o068-copy366 s072) (doublebond o068-copy367 s072) (doublebond o068-copy368 s072) (doublebond o068-copy369 s072) (doublebond o068-copy370 s072) (doublebond o068-copy371 s072) (doublebond o068-copy372 s072) (doublebond o068-copy373 s072) (doublebond o068-copy374 s072) (doublebond o068-copy375 s072) (doublebond o068-copy376 s072) (doublebond o068-copy377 s072) (doublebond o068-copy378 s072) (doublebond o068-copy379 s072) (doublebond o068-copy380 s072) (doublebond o068-copy381 s072) (doublebond o068-copy382 s072) (doublebond o068-copy383 s072) (doublebond o068-copy384 s072) (doublebond o068-copy385 s072) (doublebond o068-copy386 s072) (doublebond o068-copy387 s072) (doublebond o068-copy388 s072) (doublebond o068-copy389 s072) (doublebond o068-copy390 s072) (doublebond o068-copy391 s072) (doublebond o068-copy392 s072) (doublebond o068-copy393 s072) (doublebond o068-copy394 s072) (doublebond o068-copy395 s072) (doublebond o068-copy396 s072) (doublebond o068-copy397 s072) (doublebond o068-copy398 s072) (doublebond o068-copy399 s072) (doublebond o068-copy400 s072) (doublebond o068-copy401 s072) (doublebond o068-copy402 s072) (doublebond o068-copy403 s072) (doublebond o068-copy404 s072) (doublebond o068-copy405 s072) (doublebond o068-copy406 s072) (doublebond o068-copy407 s072) (doublebond o068-copy408 s072) (doublebond o068-copy409 s072) (doublebond o068-copy410 s072) (doublebond o068-copy411 s072) (doublebond o068-copy412 s072) (doublebond o068-copy413 s072) (doublebond o068-copy414 s072) (doublebond o068-copy415 s072) (doublebond o068-copy416 s072) (doublebond o068-copy417 s072) (doublebond o068-copy418 s072) (doublebond o068-copy419 s072) (doublebond o068-copy420 s072) (doublebond o068-copy421 s072) (doublebond o068-copy422 s072) (doublebond o068-copy423 s072) (doublebond o068-copy424 s072) (doublebond o068-copy425 s072) (doublebond o068-copy426 s072) (doublebond o068-copy427 s072) (doublebond o068-copy428 s072) (doublebond o068-copy429 s072) (doublebond o068-copy430 s072) (doublebond o068-copy431 s072) (doublebond o068-copy432 s072) (doublebond o068-copy433 s072) (doublebond o068-copy434 s072) (doublebond o068-copy435 s072) (doublebond o068-copy436 s072) (doublebond o068-copy437 s072) (doublebond o068-copy438 s072) (doublebond o068-copy439 s072) (doublebond o068-copy440 s072) (doublebond o068-copy441 s072) (doublebond o068-copy442 s072) (doublebond o068-copy443 s072) (doublebond o068-copy444 s072) (doublebond o068-copy445 s072) (doublebond o068-copy446 s072) (doublebond o068-copy447 s072) (doublebond o068-copy448 s072) (doublebond o068-copy449 s072) (doublebond o068-copy450 s072) (doublebond o068-copy451 s072) (doublebond o068-copy452 s072) (doublebond o068-copy453 s072) (doublebond o068-copy454 s072) (doublebond o068-copy455 s072) (doublebond o068-copy456 s072) (doublebond o068-copy457 s072) (doublebond o068-copy458 s072) (doublebond o068-copy459 s072) (doublebond o068-copy460 s072) (doublebond o068-copy461 s072) (doublebond o068-copy462 s072) (doublebond o068-copy463 s072) (doublebond o068-copy464 s072) (doublebond o068-copy465 s072) (doublebond o068-copy466 s072) (doublebond o068-copy467 s072) (doublebond o068-copy468 s072) (doublebond o068-copy469 s072) (doublebond o068-copy470 s072) (doublebond o068-copy471 s072) (doublebond o068-copy472 s072) (doublebond o068-copy473 s072) (doublebond o068-copy474 s072) (doublebond o068-copy475 s072) (doublebond o068-copy476 s072) (doublebond o068-copy477 s072) (doublebond o068-copy478 s072) (doublebond o068-copy479 s072) (doublebond o068-copy480 s072) (doublebond o068-copy481 s072) (doublebond o068-copy482 s072) (doublebond o068-copy483 s072) (doublebond o068-copy484 s072) (doublebond o068-copy485 s072) (doublebond o068-copy486 s072) (doublebond o068-copy487 s072) (doublebond o068-copy488 s072) (doublebond o068-copy489 s072) (doublebond o068-copy490 s072) (doublebond o068-copy491 s072) (doublebond o068-copy492 s072) (doublebond o068-copy493 s072) (doublebond o068-copy494 s072) (doublebond o068-copy495 s072) (doublebond o068-copy496 s072) (doublebond o068-copy497 s072) (doublebond o068-copy498 s072)
(doublebond s072 o068) (doublebond s072 o068-copy1) (doublebond s072 o068-copy2) (doublebond s072 o068-copy3) (doublebond s072 o068-copy4) (doublebond s072 o068-copy5) (doublebond s072 o068-copy6) (doublebond s072 o068-copy7) (doublebond s072 o068-copy8) (doublebond s072 o068-copy9) (doublebond s072 o068-copy10) (doublebond s072 o068-copy11) (doublebond s072 o068-copy12) (doublebond s072 o068-copy13) (doublebond s072 o068-copy14) (doublebond s072 o068-copy15) (doublebond s072 o068-copy16) (doublebond s072 o068-copy17) (doublebond s072 o068-copy18) (doublebond s072 o068-copy19) (doublebond s072 o068-copy20) (doublebond s072 o068-copy21) (doublebond s072 o068-copy22) (doublebond s072 o068-copy23) (doublebond s072 o068-copy24) (doublebond s072 o068-copy25) (doublebond s072 o068-copy26) (doublebond s072 o068-copy27) (doublebond s072 o068-copy28) (doublebond s072 o068-copy29) (doublebond s072 o068-copy30) (doublebond s072 o068-copy31) (doublebond s072 o068-copy32) (doublebond s072 o068-copy33) (doublebond s072 o068-copy34) (doublebond s072 o068-copy35) (doublebond s072 o068-copy36) (doublebond s072 o068-copy37) (doublebond s072 o068-copy38) (doublebond s072 o068-copy39) (doublebond s072 o068-copy40) (doublebond s072 o068-copy41) (doublebond s072 o068-copy42) (doublebond s072 o068-copy43) (doublebond s072 o068-copy44) (doublebond s072 o068-copy45) (doublebond s072 o068-copy46) (doublebond s072 o068-copy47) (doublebond s072 o068-copy48) (doublebond s072 o068-copy49) (doublebond s072 o068-copy50) (doublebond s072 o068-copy51) (doublebond s072 o068-copy52) (doublebond s072 o068-copy53) (doublebond s072 o068-copy54) (doublebond s072 o068-copy55) (doublebond s072 o068-copy56) (doublebond s072 o068-copy57) (doublebond s072 o068-copy58) (doublebond s072 o068-copy59) (doublebond s072 o068-copy60) (doublebond s072 o068-copy61) (doublebond s072 o068-copy62) (doublebond s072 o068-copy63) (doublebond s072 o068-copy64) (doublebond s072 o068-copy65) (doublebond s072 o068-copy66) (doublebond s072 o068-copy67) (doublebond s072 o068-copy68) (doublebond s072 o068-copy69) (doublebond s072 o068-copy70) (doublebond s072 o068-copy71) (doublebond s072 o068-copy72) (doublebond s072 o068-copy73) (doublebond s072 o068-copy74) (doublebond s072 o068-copy75) (doublebond s072 o068-copy76) (doublebond s072 o068-copy77) (doublebond s072 o068-copy78) (doublebond s072 o068-copy79) (doublebond s072 o068-copy80) (doublebond s072 o068-copy81) (doublebond s072 o068-copy82) (doublebond s072 o068-copy83) (doublebond s072 o068-copy84) (doublebond s072 o068-copy85) (doublebond s072 o068-copy86) (doublebond s072 o068-copy87) (doublebond s072 o068-copy88) (doublebond s072 o068-copy89) (doublebond s072 o068-copy90) (doublebond s072 o068-copy91) (doublebond s072 o068-copy92) (doublebond s072 o068-copy93) (doublebond s072 o068-copy94) (doublebond s072 o068-copy95) (doublebond s072 o068-copy96) (doublebond s072 o068-copy97) (doublebond s072 o068-copy98) (doublebond s072 o068-copy99) (doublebond s072 o068-copy100) (doublebond s072 o068-copy101) (doublebond s072 o068-copy102) (doublebond s072 o068-copy103) (doublebond s072 o068-copy104) (doublebond s072 o068-copy105) (doublebond s072 o068-copy106) (doublebond s072 o068-copy107) (doublebond s072 o068-copy108) (doublebond s072 o068-copy109) (doublebond s072 o068-copy110) (doublebond s072 o068-copy111) (doublebond s072 o068-copy112) (doublebond s072 o068-copy113) (doublebond s072 o068-copy114) (doublebond s072 o068-copy115) (doublebond s072 o068-copy116) (doublebond s072 o068-copy117) (doublebond s072 o068-copy118) (doublebond s072 o068-copy119) (doublebond s072 o068-copy120) (doublebond s072 o068-copy121) (doublebond s072 o068-copy122) (doublebond s072 o068-copy123) (doublebond s072 o068-copy124) (doublebond s072 o068-copy125) (doublebond s072 o068-copy126) (doublebond s072 o068-copy127) (doublebond s072 o068-copy128) (doublebond s072 o068-copy129) (doublebond s072 o068-copy130) (doublebond s072 o068-copy131) (doublebond s072 o068-copy132) (doublebond s072 o068-copy133) (doublebond s072 o068-copy134) (doublebond s072 o068-copy135) (doublebond s072 o068-copy136) (doublebond s072 o068-copy137) (doublebond s072 o068-copy138) (doublebond s072 o068-copy139) (doublebond s072 o068-copy140) (doublebond s072 o068-copy141) (doublebond s072 o068-copy142) (doublebond s072 o068-copy143) (doublebond s072 o068-copy144) (doublebond s072 o068-copy145) (doublebond s072 o068-copy146) (doublebond s072 o068-copy147) (doublebond s072 o068-copy148) (doublebond s072 o068-copy149) (doublebond s072 o068-copy150) (doublebond s072 o068-copy151) (doublebond s072 o068-copy152) (doublebond s072 o068-copy153) (doublebond s072 o068-copy154) (doublebond s072 o068-copy155) (doublebond s072 o068-copy156) (doublebond s072 o068-copy157) (doublebond s072 o068-copy158) (doublebond s072 o068-copy159) (doublebond s072 o068-copy160) (doublebond s072 o068-copy161) (doublebond s072 o068-copy162) (doublebond s072 o068-copy163) (doublebond s072 o068-copy164) (doublebond s072 o068-copy165) (doublebond s072 o068-copy166) (doublebond s072 o068-copy167) (doublebond s072 o068-copy168) (doublebond s072 o068-copy169) (doublebond s072 o068-copy170) (doublebond s072 o068-copy171) (doublebond s072 o068-copy172) (doublebond s072 o068-copy173) (doublebond s072 o068-copy174) (doublebond s072 o068-copy175) (doublebond s072 o068-copy176) (doublebond s072 o068-copy177) (doublebond s072 o068-copy178) (doublebond s072 o068-copy179) (doublebond s072 o068-copy180) (doublebond s072 o068-copy181) (doublebond s072 o068-copy182) (doublebond s072 o068-copy183) (doublebond s072 o068-copy184) (doublebond s072 o068-copy185) (doublebond s072 o068-copy186) (doublebond s072 o068-copy187) (doublebond s072 o068-copy188) (doublebond s072 o068-copy189) (doublebond s072 o068-copy190) (doublebond s072 o068-copy191) (doublebond s072 o068-copy192) (doublebond s072 o068-copy193) (doublebond s072 o068-copy194) (doublebond s072 o068-copy195) (doublebond s072 o068-copy196) (doublebond s072 o068-copy197) (doublebond s072 o068-copy198) (doublebond s072 o068-copy199) (doublebond s072 o068-copy200) (doublebond s072 o068-copy201) (doublebond s072 o068-copy202) (doublebond s072 o068-copy203) (doublebond s072 o068-copy204) (doublebond s072 o068-copy205) (doublebond s072 o068-copy206) (doublebond s072 o068-copy207) (doublebond s072 o068-copy208) (doublebond s072 o068-copy209) (doublebond s072 o068-copy210) (doublebond s072 o068-copy211) (doublebond s072 o068-copy212) (doublebond s072 o068-copy213) (doublebond s072 o068-copy214) (doublebond s072 o068-copy215) (doublebond s072 o068-copy216) (doublebond s072 o068-copy217) (doublebond s072 o068-copy218) (doublebond s072 o068-copy219) (doublebond s072 o068-copy220) (doublebond s072 o068-copy221) (doublebond s072 o068-copy222) (doublebond s072 o068-copy223) (doublebond s072 o068-copy224) (doublebond s072 o068-copy225) (doublebond s072 o068-copy226) (doublebond s072 o068-copy227) (doublebond s072 o068-copy228) (doublebond s072 o068-copy229) (doublebond s072 o068-copy230) (doublebond s072 o068-copy231) (doublebond s072 o068-copy232) (doublebond s072 o068-copy233) (doublebond s072 o068-copy234) (doublebond s072 o068-copy235) (doublebond s072 o068-copy236) (doublebond s072 o068-copy237) (doublebond s072 o068-copy238) (doublebond s072 o068-copy239) (doublebond s072 o068-copy240) (doublebond s072 o068-copy241) (doublebond s072 o068-copy242) (doublebond s072 o068-copy243) (doublebond s072 o068-copy244) (doublebond s072 o068-copy245) (doublebond s072 o068-copy246) (doublebond s072 o068-copy247) (doublebond s072 o068-copy248) (doublebond s072 o068-copy249) (doublebond s072 o068-copy250) (doublebond s072 o068-copy251) (doublebond s072 o068-copy252) (doublebond s072 o068-copy253) (doublebond s072 o068-copy254) (doublebond s072 o068-copy255) (doublebond s072 o068-copy256) (doublebond s072 o068-copy257) (doublebond s072 o068-copy258) (doublebond s072 o068-copy259) (doublebond s072 o068-copy260) (doublebond s072 o068-copy261) (doublebond s072 o068-copy262) (doublebond s072 o068-copy263) (doublebond s072 o068-copy264) (doublebond s072 o068-copy265) (doublebond s072 o068-copy266) (doublebond s072 o068-copy267) (doublebond s072 o068-copy268) (doublebond s072 o068-copy269) (doublebond s072 o068-copy270) (doublebond s072 o068-copy271) (doublebond s072 o068-copy272) (doublebond s072 o068-copy273) (doublebond s072 o068-copy274) (doublebond s072 o068-copy275) (doublebond s072 o068-copy276) (doublebond s072 o068-copy277) (doublebond s072 o068-copy278) (doublebond s072 o068-copy279) (doublebond s072 o068-copy280) (doublebond s072 o068-copy281) (doublebond s072 o068-copy282) (doublebond s072 o068-copy283) (doublebond s072 o068-copy284) (doublebond s072 o068-copy285) (doublebond s072 o068-copy286) (doublebond s072 o068-copy287) (doublebond s072 o068-copy288) (doublebond s072 o068-copy289) (doublebond s072 o068-copy290) (doublebond s072 o068-copy291) (doublebond s072 o068-copy292) (doublebond s072 o068-copy293) (doublebond s072 o068-copy294) (doublebond s072 o068-copy295) (doublebond s072 o068-copy296) (doublebond s072 o068-copy297) (doublebond s072 o068-copy298) (doublebond s072 o068-copy299) (doublebond s072 o068-copy300) (doublebond s072 o068-copy301) (doublebond s072 o068-copy302) (doublebond s072 o068-copy303) (doublebond s072 o068-copy304) (doublebond s072 o068-copy305) (doublebond s072 o068-copy306) (doublebond s072 o068-copy307) (doublebond s072 o068-copy308) (doublebond s072 o068-copy309) (doublebond s072 o068-copy310) (doublebond s072 o068-copy311) (doublebond s072 o068-copy312) (doublebond s072 o068-copy313) (doublebond s072 o068-copy314) (doublebond s072 o068-copy315) (doublebond s072 o068-copy316) (doublebond s072 o068-copy317) (doublebond s072 o068-copy318) (doublebond s072 o068-copy319) (doublebond s072 o068-copy320) (doublebond s072 o068-copy321) (doublebond s072 o068-copy322) (doublebond s072 o068-copy323) (doublebond s072 o068-copy324) (doublebond s072 o068-copy325) (doublebond s072 o068-copy326) (doublebond s072 o068-copy327) (doublebond s072 o068-copy328) (doublebond s072 o068-copy329) (doublebond s072 o068-copy330) (doublebond s072 o068-copy331) (doublebond s072 o068-copy332) (doublebond s072 o068-copy333) (doublebond s072 o068-copy334) (doublebond s072 o068-copy335) (doublebond s072 o068-copy336) (doublebond s072 o068-copy337) (doublebond s072 o068-copy338) (doublebond s072 o068-copy339) (doublebond s072 o068-copy340) (doublebond s072 o068-copy341) (doublebond s072 o068-copy342) (doublebond s072 o068-copy343) (doublebond s072 o068-copy344) (doublebond s072 o068-copy345) (doublebond s072 o068-copy346) (doublebond s072 o068-copy347) (doublebond s072 o068-copy348) (doublebond s072 o068-copy349) (doublebond s072 o068-copy350) (doublebond s072 o068-copy351) (doublebond s072 o068-copy352) (doublebond s072 o068-copy353) (doublebond s072 o068-copy354) (doublebond s072 o068-copy355) (doublebond s072 o068-copy356) (doublebond s072 o068-copy357) (doublebond s072 o068-copy358) (doublebond s072 o068-copy359) (doublebond s072 o068-copy360) (doublebond s072 o068-copy361) (doublebond s072 o068-copy362) (doublebond s072 o068-copy363) (doublebond s072 o068-copy364) (doublebond s072 o068-copy365) (doublebond s072 o068-copy366) (doublebond s072 o068-copy367) (doublebond s072 o068-copy368) (doublebond s072 o068-copy369) (doublebond s072 o068-copy370) (doublebond s072 o068-copy371) (doublebond s072 o068-copy372) (doublebond s072 o068-copy373) (doublebond s072 o068-copy374) (doublebond s072 o068-copy375) (doublebond s072 o068-copy376) (doublebond s072 o068-copy377) (doublebond s072 o068-copy378) (doublebond s072 o068-copy379) (doublebond s072 o068-copy380) (doublebond s072 o068-copy381) (doublebond s072 o068-copy382) (doublebond s072 o068-copy383) (doublebond s072 o068-copy384) (doublebond s072 o068-copy385) (doublebond s072 o068-copy386) (doublebond s072 o068-copy387) (doublebond s072 o068-copy388) (doublebond s072 o068-copy389) (doublebond s072 o068-copy390) (doublebond s072 o068-copy391) (doublebond s072 o068-copy392) (doublebond s072 o068-copy393) (doublebond s072 o068-copy394) (doublebond s072 o068-copy395) (doublebond s072 o068-copy396) (doublebond s072 o068-copy397) (doublebond s072 o068-copy398) (doublebond s072 o068-copy399) (doublebond s072 o068-copy400) (doublebond s072 o068-copy401) (doublebond s072 o068-copy402) (doublebond s072 o068-copy403) (doublebond s072 o068-copy404) (doublebond s072 o068-copy405) (doublebond s072 o068-copy406) (doublebond s072 o068-copy407) (doublebond s072 o068-copy408) (doublebond s072 o068-copy409) (doublebond s072 o068-copy410) (doublebond s072 o068-copy411) (doublebond s072 o068-copy412) (doublebond s072 o068-copy413) (doublebond s072 o068-copy414) (doublebond s072 o068-copy415) (doublebond s072 o068-copy416) (doublebond s072 o068-copy417) (doublebond s072 o068-copy418) (doublebond s072 o068-copy419) (doublebond s072 o068-copy420) (doublebond s072 o068-copy421) (doublebond s072 o068-copy422) (doublebond s072 o068-copy423) (doublebond s072 o068-copy424) (doublebond s072 o068-copy425) (doublebond s072 o068-copy426) (doublebond s072 o068-copy427) (doublebond s072 o068-copy428) (doublebond s072 o068-copy429) (doublebond s072 o068-copy430) (doublebond s072 o068-copy431) (doublebond s072 o068-copy432) (doublebond s072 o068-copy433) (doublebond s072 o068-copy434) (doublebond s072 o068-copy435) (doublebond s072 o068-copy436) (doublebond s072 o068-copy437) (doublebond s072 o068-copy438) (doublebond s072 o068-copy439) (doublebond s072 o068-copy440) (doublebond s072 o068-copy441) (doublebond s072 o068-copy442) (doublebond s072 o068-copy443) (doublebond s072 o068-copy444) (doublebond s072 o068-copy445) (doublebond s072 o068-copy446) (doublebond s072 o068-copy447) (doublebond s072 o068-copy448) (doublebond s072 o068-copy449) (doublebond s072 o068-copy450) (doublebond s072 o068-copy451) (doublebond s072 o068-copy452) (doublebond s072 o068-copy453) (doublebond s072 o068-copy454) (doublebond s072 o068-copy455) (doublebond s072 o068-copy456) (doublebond s072 o068-copy457) (doublebond s072 o068-copy458) (doublebond s072 o068-copy459) (doublebond s072 o068-copy460) (doublebond s072 o068-copy461) (doublebond s072 o068-copy462) (doublebond s072 o068-copy463) (doublebond s072 o068-copy464) (doublebond s072 o068-copy465) (doublebond s072 o068-copy466) (doublebond s072 o068-copy467) (doublebond s072 o068-copy468) (doublebond s072 o068-copy469) (doublebond s072 o068-copy470) (doublebond s072 o068-copy471) (doublebond s072 o068-copy472) (doublebond s072 o068-copy473) (doublebond s072 o068-copy474) (doublebond s072 o068-copy475) (doublebond s072 o068-copy476) (doublebond s072 o068-copy477) (doublebond s072 o068-copy478) (doublebond s072 o068-copy479) (doublebond s072 o068-copy480) (doublebond s072 o068-copy481) (doublebond s072 o068-copy482) (doublebond s072 o068-copy483) (doublebond s072 o068-copy484) (doublebond s072 o068-copy485) (doublebond s072 o068-copy486) (doublebond s072 o068-copy487) (doublebond s072 o068-copy488) (doublebond s072 o068-copy489) (doublebond s072 o068-copy490) (doublebond s072 o068-copy491) (doublebond s072 o068-copy492) (doublebond s072 o068-copy493) (doublebond s072 o068-copy494) (doublebond s072 o068-copy495) (doublebond s072 o068-copy496) (doublebond s072 o068-copy497) (doublebond s072 o068-copy498)

(doublebond o069 s072)
(doublebond s072 o069)
)
(:goal
(and
(bond c039 c040)
(bond c040 c039)

(bond c039 h147)
(bond h147 c039)

(bond c039 h145)
(bond h145 c039)

(bond c039 h146)
(bond h146 c039)

(bond c040 c045)
(bond c045 c040)

(bond c040 c041)
(bond c041 c040)

(bond c040 h060)
(bond h060 c040)

(bond c041 c042)
(bond c042 c041)

(bond c041 o065)
(bond o065 c041)

(bond c041 h148)
(bond h148 c041)

(bond c042 c043)
(bond c043 c042)

(bond c042 h149)
(bond h149 c042)

(bond c042 h150)
(bond h150 c042)

(bond c043 c044)
(bond c044 c043)

(bond c043 h152)
(bond h152 c043)

(bond c043 h151)
(bond h151 c043)

(bond c044 c045)
(bond c045 c044)

(bond c044 h154)
(bond h154 c044)

(bond c044 h153)
(bond h153 c044)

(bond c045 h155)
(bond h155 c045)

(bond c045 h156)
(bond h156 c045)

(doublebond c046 c047)
(doublebond c047 c046)

(bond c046 h157)
(bond h157 c046)

(bond c046 h158)
(bond h158 c046)

(bond c047 c048)
(bond c048 c047)

(bond c047 h159)
(bond h159 c047)

(bond c048 c049)
(bond c049 c048)

(bond c048 h161)
(bond h161 c048)

(bond c048 h160)
(bond h160 c048)

(bond c049 c050)
(bond c050 c049)

(bond c049 h163)
(bond h163 c049)

(bond c049 h162)
(bond h162 c049)

(bond c050 o065)
(bond o065 c050)

(bond c050 h165)
(bond h165 c050)

(bond c050 h164)
(bond h164 c050)
)
)
)