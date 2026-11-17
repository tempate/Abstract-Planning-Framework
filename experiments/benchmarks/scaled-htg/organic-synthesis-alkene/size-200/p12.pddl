; The variants of the Organic Synthesis domain were created by
; Dr. Russell Viirre, Hadi Qovaizi, and Prof. Mikhail Soutchanski.
;
; This work is licensed under a Creative Commons Attribution,
; NonCommercial, ShareAlike 3.0 Unported License.
;
; For further information, please access the following web page:
; https://www.cs.ryerson.ca/~mes/publications/
(define (problem Alkene_P12) (:domain Chemical)
(:objects
c007 - carbon
c008 - carbon
c009 - carbon
c010 - carbon
c011 - carbon
c012 - carbon
c013 - carbon
c014 - carbon
c015 - carbon
h056 - hydrogen
h057 - hydrogen
h088 - hydrogen
h089 - hydrogen
h090 - hydrogen
h091 - hydrogen
h092 - hydrogen
h093 - hydrogen
h094 - hydrogen
h095 h095-copy1 h095-copy2 h095-copy3 h095-copy4 h095-copy5 h095-copy6 h095-copy7 h095-copy8 h095-copy9 h095-copy10 h095-copy11 h095-copy12 h095-copy13 h095-copy14 h095-copy15 h095-copy16 h095-copy17 h095-copy18 h095-copy19 h095-copy20 h095-copy21 h095-copy22 h095-copy23 h095-copy24 h095-copy25 h095-copy26 h095-copy27 h095-copy28 h095-copy29 h095-copy30 h095-copy31 h095-copy32 h095-copy33 h095-copy34 h095-copy35 h095-copy36 h095-copy37 h095-copy38 h095-copy39 h095-copy40 h095-copy41 h095-copy42 h095-copy43 h095-copy44 h095-copy45 h095-copy46 h095-copy47 h095-copy48 h095-copy49 h095-copy50 h095-copy51 h095-copy52 h095-copy53 h095-copy54 h095-copy55 h095-copy56 h095-copy57 h095-copy58 h095-copy59 h095-copy60 h095-copy61 h095-copy62 h095-copy63 h095-copy64 h095-copy65 h095-copy66 h095-copy67 h095-copy68 h095-copy69 h095-copy70 h095-copy71 h095-copy72 h095-copy73 h095-copy74 h095-copy75 h095-copy76 h095-copy77 h095-copy78 h095-copy79 h095-copy80 h095-copy81 h095-copy82 h095-copy83 h095-copy84 h095-copy85 h095-copy86 h095-copy87 h095-copy88 h095-copy89 h095-copy90 h095-copy91 h095-copy92 h095-copy93 h095-copy94 h095-copy95 h095-copy96 h095-copy97 h095-copy98 h095-copy99 h095-copy100 h095-copy101 h095-copy102 h095-copy103 h095-copy104 h095-copy105 h095-copy106 h095-copy107 h095-copy108 h095-copy109 h095-copy110 h095-copy111 h095-copy112 h095-copy113 h095-copy114 h095-copy115 h095-copy116 h095-copy117 h095-copy118 h095-copy119 h095-copy120 h095-copy121 h095-copy122 h095-copy123 h095-copy124 h095-copy125 h095-copy126 h095-copy127 h095-copy128 h095-copy129 h095-copy130 h095-copy131 h095-copy132 h095-copy133 h095-copy134 h095-copy135 h095-copy136 h095-copy137 h095-copy138 h095-copy139 h095-copy140 h095-copy141 h095-copy142 h095-copy143 h095-copy144 h095-copy145 h095-copy146 h095-copy147 h095-copy148 h095-copy149 h095-copy150 h095-copy151 h095-copy152 h095-copy153 h095-copy154 h095-copy155 h095-copy156 h095-copy157 h095-copy158 h095-copy159 h095-copy160 h095-copy161 h095-copy162 h095-copy163 h095-copy164 h095-copy165 h095-copy166 h095-copy167 h095-copy168 h095-copy169 h095-copy170 h095-copy171 h095-copy172 h095-copy173 h095-copy174 h095-copy175 h095-copy176 h095-copy177 h095-copy178 h095-copy179 h095-copy180 h095-copy181 h095-copy182 h095-copy183 h095-copy184 h095-copy185 h095-copy186 h095-copy187 h095-copy188 h095-copy189 h095-copy190 h095-copy191 h095-copy192 h095-copy193 h095-copy194 h095-copy195 h095-copy196 h095-copy197 h095-copy198 - hydrogen
h096 - hydrogen
h097 - hydrogen
h098 - hydrogen
h099 - hydrogen
h100 - hydrogen
h101 - hydrogen
h102 - hydrogen
h103 - hydrogen
h104 - hydrogen
h105 - hydrogen
o063 - oxygen
)
(:init
(bond c007 h088)
(bond h088 c007)

(bond c007 h089)
(bond h089 c007)

(bond c007 h090)
(bond h090 c007)

(bond c007 c008)
(bond c008 c007)

(bond c008 h091)
(bond h091 c008)

(bond c008 h092)
(bond h092 c008)

(bond c008 c009)
(bond c009 c008)

(bond c009 h094)
(bond h094 c009)

(bond c009 h093)
(bond h093 c009)

(bond c009 c010)
(bond c010 c009)

(bond c010 h096)
(bond h096 c010)

(bond c010 h095) (bond c010 h095-copy1) (bond c010 h095-copy2) (bond c010 h095-copy3) (bond c010 h095-copy4) (bond c010 h095-copy5) (bond c010 h095-copy6) (bond c010 h095-copy7) (bond c010 h095-copy8) (bond c010 h095-copy9) (bond c010 h095-copy10) (bond c010 h095-copy11) (bond c010 h095-copy12) (bond c010 h095-copy13) (bond c010 h095-copy14) (bond c010 h095-copy15) (bond c010 h095-copy16) (bond c010 h095-copy17) (bond c010 h095-copy18) (bond c010 h095-copy19) (bond c010 h095-copy20) (bond c010 h095-copy21) (bond c010 h095-copy22) (bond c010 h095-copy23) (bond c010 h095-copy24) (bond c010 h095-copy25) (bond c010 h095-copy26) (bond c010 h095-copy27) (bond c010 h095-copy28) (bond c010 h095-copy29) (bond c010 h095-copy30) (bond c010 h095-copy31) (bond c010 h095-copy32) (bond c010 h095-copy33) (bond c010 h095-copy34) (bond c010 h095-copy35) (bond c010 h095-copy36) (bond c010 h095-copy37) (bond c010 h095-copy38) (bond c010 h095-copy39) (bond c010 h095-copy40) (bond c010 h095-copy41) (bond c010 h095-copy42) (bond c010 h095-copy43) (bond c010 h095-copy44) (bond c010 h095-copy45) (bond c010 h095-copy46) (bond c010 h095-copy47) (bond c010 h095-copy48) (bond c010 h095-copy49) (bond c010 h095-copy50) (bond c010 h095-copy51) (bond c010 h095-copy52) (bond c010 h095-copy53) (bond c010 h095-copy54) (bond c010 h095-copy55) (bond c010 h095-copy56) (bond c010 h095-copy57) (bond c010 h095-copy58) (bond c010 h095-copy59) (bond c010 h095-copy60) (bond c010 h095-copy61) (bond c010 h095-copy62) (bond c010 h095-copy63) (bond c010 h095-copy64) (bond c010 h095-copy65) (bond c010 h095-copy66) (bond c010 h095-copy67) (bond c010 h095-copy68) (bond c010 h095-copy69) (bond c010 h095-copy70) (bond c010 h095-copy71) (bond c010 h095-copy72) (bond c010 h095-copy73) (bond c010 h095-copy74) (bond c010 h095-copy75) (bond c010 h095-copy76) (bond c010 h095-copy77) (bond c010 h095-copy78) (bond c010 h095-copy79) (bond c010 h095-copy80) (bond c010 h095-copy81) (bond c010 h095-copy82) (bond c010 h095-copy83) (bond c010 h095-copy84) (bond c010 h095-copy85) (bond c010 h095-copy86) (bond c010 h095-copy87) (bond c010 h095-copy88) (bond c010 h095-copy89) (bond c010 h095-copy90) (bond c010 h095-copy91) (bond c010 h095-copy92) (bond c010 h095-copy93) (bond c010 h095-copy94) (bond c010 h095-copy95) (bond c010 h095-copy96) (bond c010 h095-copy97) (bond c010 h095-copy98) (bond c010 h095-copy99) (bond c010 h095-copy100) (bond c010 h095-copy101) (bond c010 h095-copy102) (bond c010 h095-copy103) (bond c010 h095-copy104) (bond c010 h095-copy105) (bond c010 h095-copy106) (bond c010 h095-copy107) (bond c010 h095-copy108) (bond c010 h095-copy109) (bond c010 h095-copy110) (bond c010 h095-copy111) (bond c010 h095-copy112) (bond c010 h095-copy113) (bond c010 h095-copy114) (bond c010 h095-copy115) (bond c010 h095-copy116) (bond c010 h095-copy117) (bond c010 h095-copy118) (bond c010 h095-copy119) (bond c010 h095-copy120) (bond c010 h095-copy121) (bond c010 h095-copy122) (bond c010 h095-copy123) (bond c010 h095-copy124) (bond c010 h095-copy125) (bond c010 h095-copy126) (bond c010 h095-copy127) (bond c010 h095-copy128) (bond c010 h095-copy129) (bond c010 h095-copy130) (bond c010 h095-copy131) (bond c010 h095-copy132) (bond c010 h095-copy133) (bond c010 h095-copy134) (bond c010 h095-copy135) (bond c010 h095-copy136) (bond c010 h095-copy137) (bond c010 h095-copy138) (bond c010 h095-copy139) (bond c010 h095-copy140) (bond c010 h095-copy141) (bond c010 h095-copy142) (bond c010 h095-copy143) (bond c010 h095-copy144) (bond c010 h095-copy145) (bond c010 h095-copy146) (bond c010 h095-copy147) (bond c010 h095-copy148) (bond c010 h095-copy149) (bond c010 h095-copy150) (bond c010 h095-copy151) (bond c010 h095-copy152) (bond c010 h095-copy153) (bond c010 h095-copy154) (bond c010 h095-copy155) (bond c010 h095-copy156) (bond c010 h095-copy157) (bond c010 h095-copy158) (bond c010 h095-copy159) (bond c010 h095-copy160) (bond c010 h095-copy161) (bond c010 h095-copy162) (bond c010 h095-copy163) (bond c010 h095-copy164) (bond c010 h095-copy165) (bond c010 h095-copy166) (bond c010 h095-copy167) (bond c010 h095-copy168) (bond c010 h095-copy169) (bond c010 h095-copy170) (bond c010 h095-copy171) (bond c010 h095-copy172) (bond c010 h095-copy173) (bond c010 h095-copy174) (bond c010 h095-copy175) (bond c010 h095-copy176) (bond c010 h095-copy177) (bond c010 h095-copy178) (bond c010 h095-copy179) (bond c010 h095-copy180) (bond c010 h095-copy181) (bond c010 h095-copy182) (bond c010 h095-copy183) (bond c010 h095-copy184) (bond c010 h095-copy185) (bond c010 h095-copy186) (bond c010 h095-copy187) (bond c010 h095-copy188) (bond c010 h095-copy189) (bond c010 h095-copy190) (bond c010 h095-copy191) (bond c010 h095-copy192) (bond c010 h095-copy193) (bond c010 h095-copy194) (bond c010 h095-copy195) (bond c010 h095-copy196) (bond c010 h095-copy197) (bond c010 h095-copy198)
(bond h095 c010) (bond h095-copy1 c010) (bond h095-copy2 c010) (bond h095-copy3 c010) (bond h095-copy4 c010) (bond h095-copy5 c010) (bond h095-copy6 c010) (bond h095-copy7 c010) (bond h095-copy8 c010) (bond h095-copy9 c010) (bond h095-copy10 c010) (bond h095-copy11 c010) (bond h095-copy12 c010) (bond h095-copy13 c010) (bond h095-copy14 c010) (bond h095-copy15 c010) (bond h095-copy16 c010) (bond h095-copy17 c010) (bond h095-copy18 c010) (bond h095-copy19 c010) (bond h095-copy20 c010) (bond h095-copy21 c010) (bond h095-copy22 c010) (bond h095-copy23 c010) (bond h095-copy24 c010) (bond h095-copy25 c010) (bond h095-copy26 c010) (bond h095-copy27 c010) (bond h095-copy28 c010) (bond h095-copy29 c010) (bond h095-copy30 c010) (bond h095-copy31 c010) (bond h095-copy32 c010) (bond h095-copy33 c010) (bond h095-copy34 c010) (bond h095-copy35 c010) (bond h095-copy36 c010) (bond h095-copy37 c010) (bond h095-copy38 c010) (bond h095-copy39 c010) (bond h095-copy40 c010) (bond h095-copy41 c010) (bond h095-copy42 c010) (bond h095-copy43 c010) (bond h095-copy44 c010) (bond h095-copy45 c010) (bond h095-copy46 c010) (bond h095-copy47 c010) (bond h095-copy48 c010) (bond h095-copy49 c010) (bond h095-copy50 c010) (bond h095-copy51 c010) (bond h095-copy52 c010) (bond h095-copy53 c010) (bond h095-copy54 c010) (bond h095-copy55 c010) (bond h095-copy56 c010) (bond h095-copy57 c010) (bond h095-copy58 c010) (bond h095-copy59 c010) (bond h095-copy60 c010) (bond h095-copy61 c010) (bond h095-copy62 c010) (bond h095-copy63 c010) (bond h095-copy64 c010) (bond h095-copy65 c010) (bond h095-copy66 c010) (bond h095-copy67 c010) (bond h095-copy68 c010) (bond h095-copy69 c010) (bond h095-copy70 c010) (bond h095-copy71 c010) (bond h095-copy72 c010) (bond h095-copy73 c010) (bond h095-copy74 c010) (bond h095-copy75 c010) (bond h095-copy76 c010) (bond h095-copy77 c010) (bond h095-copy78 c010) (bond h095-copy79 c010) (bond h095-copy80 c010) (bond h095-copy81 c010) (bond h095-copy82 c010) (bond h095-copy83 c010) (bond h095-copy84 c010) (bond h095-copy85 c010) (bond h095-copy86 c010) (bond h095-copy87 c010) (bond h095-copy88 c010) (bond h095-copy89 c010) (bond h095-copy90 c010) (bond h095-copy91 c010) (bond h095-copy92 c010) (bond h095-copy93 c010) (bond h095-copy94 c010) (bond h095-copy95 c010) (bond h095-copy96 c010) (bond h095-copy97 c010) (bond h095-copy98 c010) (bond h095-copy99 c010) (bond h095-copy100 c010) (bond h095-copy101 c010) (bond h095-copy102 c010) (bond h095-copy103 c010) (bond h095-copy104 c010) (bond h095-copy105 c010) (bond h095-copy106 c010) (bond h095-copy107 c010) (bond h095-copy108 c010) (bond h095-copy109 c010) (bond h095-copy110 c010) (bond h095-copy111 c010) (bond h095-copy112 c010) (bond h095-copy113 c010) (bond h095-copy114 c010) (bond h095-copy115 c010) (bond h095-copy116 c010) (bond h095-copy117 c010) (bond h095-copy118 c010) (bond h095-copy119 c010) (bond h095-copy120 c010) (bond h095-copy121 c010) (bond h095-copy122 c010) (bond h095-copy123 c010) (bond h095-copy124 c010) (bond h095-copy125 c010) (bond h095-copy126 c010) (bond h095-copy127 c010) (bond h095-copy128 c010) (bond h095-copy129 c010) (bond h095-copy130 c010) (bond h095-copy131 c010) (bond h095-copy132 c010) (bond h095-copy133 c010) (bond h095-copy134 c010) (bond h095-copy135 c010) (bond h095-copy136 c010) (bond h095-copy137 c010) (bond h095-copy138 c010) (bond h095-copy139 c010) (bond h095-copy140 c010) (bond h095-copy141 c010) (bond h095-copy142 c010) (bond h095-copy143 c010) (bond h095-copy144 c010) (bond h095-copy145 c010) (bond h095-copy146 c010) (bond h095-copy147 c010) (bond h095-copy148 c010) (bond h095-copy149 c010) (bond h095-copy150 c010) (bond h095-copy151 c010) (bond h095-copy152 c010) (bond h095-copy153 c010) (bond h095-copy154 c010) (bond h095-copy155 c010) (bond h095-copy156 c010) (bond h095-copy157 c010) (bond h095-copy158 c010) (bond h095-copy159 c010) (bond h095-copy160 c010) (bond h095-copy161 c010) (bond h095-copy162 c010) (bond h095-copy163 c010) (bond h095-copy164 c010) (bond h095-copy165 c010) (bond h095-copy166 c010) (bond h095-copy167 c010) (bond h095-copy168 c010) (bond h095-copy169 c010) (bond h095-copy170 c010) (bond h095-copy171 c010) (bond h095-copy172 c010) (bond h095-copy173 c010) (bond h095-copy174 c010) (bond h095-copy175 c010) (bond h095-copy176 c010) (bond h095-copy177 c010) (bond h095-copy178 c010) (bond h095-copy179 c010) (bond h095-copy180 c010) (bond h095-copy181 c010) (bond h095-copy182 c010) (bond h095-copy183 c010) (bond h095-copy184 c010) (bond h095-copy185 c010) (bond h095-copy186 c010) (bond h095-copy187 c010) (bond h095-copy188 c010) (bond h095-copy189 c010) (bond h095-copy190 c010) (bond h095-copy191 c010) (bond h095-copy192 c010) (bond h095-copy193 c010) (bond h095-copy194 c010) (bond h095-copy195 c010) (bond h095-copy196 c010) (bond h095-copy197 c010) (bond h095-copy198 c010)

(bond c010 c011)
(bond c011 c010)

(doublebond c011 c013)
(doublebond c013 c011)

(bond c011 c012)
(bond c012 c011)

(bond c012 h098)
(bond h098 c012)

(bond c012 h099)
(bond h099 c012)

(bond c012 h097)
(bond h097 c012)

(bond c013 c015)
(bond c015 c013)

(bond c013 c014)
(bond c014 c013)

(bond c014 h102)
(bond h102 c014)

(bond c014 h100)
(bond h100 c014)

(bond c014 h101)
(bond h101 c014)

(bond c015 h104)
(bond h104 c015)

(bond c015 h105)
(bond h105 c015)

(bond c015 h103)
(bond h103 c015)

(bond h056 o063)
(bond o063 h056)

(bond h057 o063)
(bond o063 h057)
)
(:goal
(and
(bond c007 c008)
(bond c008 c007)

(bond c007 h088)
(bond h088 c007)

(bond c007 h090)
(bond h090 c007)

(bond c007 h089)
(bond h089 c007)

(bond c008 c009)
(bond c009 c008)

(bond c008 h091)
(bond h091 c008)

(bond c008 h092)
(bond h092 c008)

(bond c009 c010)
(bond c010 c009)

(bond c009 h094)
(bond h094 c009)

(bond c009 h093)
(bond h093 c009)

(bond c010 c011)
(bond c011 c010)

(bond c010 h096)
(bond h096 c010)

(bond c010 h095) (bond c010 h095-copy1) (bond c010 h095-copy2) (bond c010 h095-copy3) (bond c010 h095-copy4) (bond c010 h095-copy5) (bond c010 h095-copy6) (bond c010 h095-copy7) (bond c010 h095-copy8) (bond c010 h095-copy9) (bond c010 h095-copy10) (bond c010 h095-copy11) (bond c010 h095-copy12) (bond c010 h095-copy13) (bond c010 h095-copy14) (bond c010 h095-copy15) (bond c010 h095-copy16) (bond c010 h095-copy17) (bond c010 h095-copy18) (bond c010 h095-copy19) (bond c010 h095-copy20) (bond c010 h095-copy21) (bond c010 h095-copy22) (bond c010 h095-copy23) (bond c010 h095-copy24) (bond c010 h095-copy25) (bond c010 h095-copy26) (bond c010 h095-copy27) (bond c010 h095-copy28) (bond c010 h095-copy29) (bond c010 h095-copy30) (bond c010 h095-copy31) (bond c010 h095-copy32) (bond c010 h095-copy33) (bond c010 h095-copy34) (bond c010 h095-copy35) (bond c010 h095-copy36) (bond c010 h095-copy37) (bond c010 h095-copy38) (bond c010 h095-copy39) (bond c010 h095-copy40) (bond c010 h095-copy41) (bond c010 h095-copy42) (bond c010 h095-copy43) (bond c010 h095-copy44) (bond c010 h095-copy45) (bond c010 h095-copy46) (bond c010 h095-copy47) (bond c010 h095-copy48) (bond c010 h095-copy49) (bond c010 h095-copy50) (bond c010 h095-copy51) (bond c010 h095-copy52) (bond c010 h095-copy53) (bond c010 h095-copy54) (bond c010 h095-copy55) (bond c010 h095-copy56) (bond c010 h095-copy57) (bond c010 h095-copy58) (bond c010 h095-copy59) (bond c010 h095-copy60) (bond c010 h095-copy61) (bond c010 h095-copy62) (bond c010 h095-copy63) (bond c010 h095-copy64) (bond c010 h095-copy65) (bond c010 h095-copy66) (bond c010 h095-copy67) (bond c010 h095-copy68) (bond c010 h095-copy69) (bond c010 h095-copy70) (bond c010 h095-copy71) (bond c010 h095-copy72) (bond c010 h095-copy73) (bond c010 h095-copy74) (bond c010 h095-copy75) (bond c010 h095-copy76) (bond c010 h095-copy77) (bond c010 h095-copy78) (bond c010 h095-copy79) (bond c010 h095-copy80) (bond c010 h095-copy81) (bond c010 h095-copy82) (bond c010 h095-copy83) (bond c010 h095-copy84) (bond c010 h095-copy85) (bond c010 h095-copy86) (bond c010 h095-copy87) (bond c010 h095-copy88) (bond c010 h095-copy89) (bond c010 h095-copy90) (bond c010 h095-copy91) (bond c010 h095-copy92) (bond c010 h095-copy93) (bond c010 h095-copy94) (bond c010 h095-copy95) (bond c010 h095-copy96) (bond c010 h095-copy97) (bond c010 h095-copy98) (bond c010 h095-copy99) (bond c010 h095-copy100) (bond c010 h095-copy101) (bond c010 h095-copy102) (bond c010 h095-copy103) (bond c010 h095-copy104) (bond c010 h095-copy105) (bond c010 h095-copy106) (bond c010 h095-copy107) (bond c010 h095-copy108) (bond c010 h095-copy109) (bond c010 h095-copy110) (bond c010 h095-copy111) (bond c010 h095-copy112) (bond c010 h095-copy113) (bond c010 h095-copy114) (bond c010 h095-copy115) (bond c010 h095-copy116) (bond c010 h095-copy117) (bond c010 h095-copy118) (bond c010 h095-copy119) (bond c010 h095-copy120) (bond c010 h095-copy121) (bond c010 h095-copy122) (bond c010 h095-copy123) (bond c010 h095-copy124) (bond c010 h095-copy125) (bond c010 h095-copy126) (bond c010 h095-copy127) (bond c010 h095-copy128) (bond c010 h095-copy129) (bond c010 h095-copy130) (bond c010 h095-copy131) (bond c010 h095-copy132) (bond c010 h095-copy133) (bond c010 h095-copy134) (bond c010 h095-copy135) (bond c010 h095-copy136) (bond c010 h095-copy137) (bond c010 h095-copy138) (bond c010 h095-copy139) (bond c010 h095-copy140) (bond c010 h095-copy141) (bond c010 h095-copy142) (bond c010 h095-copy143) (bond c010 h095-copy144) (bond c010 h095-copy145) (bond c010 h095-copy146) (bond c010 h095-copy147) (bond c010 h095-copy148) (bond c010 h095-copy149) (bond c010 h095-copy150) (bond c010 h095-copy151) (bond c010 h095-copy152) (bond c010 h095-copy153) (bond c010 h095-copy154) (bond c010 h095-copy155) (bond c010 h095-copy156) (bond c010 h095-copy157) (bond c010 h095-copy158) (bond c010 h095-copy159) (bond c010 h095-copy160) (bond c010 h095-copy161) (bond c010 h095-copy162) (bond c010 h095-copy163) (bond c010 h095-copy164) (bond c010 h095-copy165) (bond c010 h095-copy166) (bond c010 h095-copy167) (bond c010 h095-copy168) (bond c010 h095-copy169) (bond c010 h095-copy170) (bond c010 h095-copy171) (bond c010 h095-copy172) (bond c010 h095-copy173) (bond c010 h095-copy174) (bond c010 h095-copy175) (bond c010 h095-copy176) (bond c010 h095-copy177) (bond c010 h095-copy178) (bond c010 h095-copy179) (bond c010 h095-copy180) (bond c010 h095-copy181) (bond c010 h095-copy182) (bond c010 h095-copy183) (bond c010 h095-copy184) (bond c010 h095-copy185) (bond c010 h095-copy186) (bond c010 h095-copy187) (bond c010 h095-copy188) (bond c010 h095-copy189) (bond c010 h095-copy190) (bond c010 h095-copy191) (bond c010 h095-copy192) (bond c010 h095-copy193) (bond c010 h095-copy194) (bond c010 h095-copy195) (bond c010 h095-copy196) (bond c010 h095-copy197) (bond c010 h095-copy198)
(bond h095 c010) (bond h095-copy1 c010) (bond h095-copy2 c010) (bond h095-copy3 c010) (bond h095-copy4 c010) (bond h095-copy5 c010) (bond h095-copy6 c010) (bond h095-copy7 c010) (bond h095-copy8 c010) (bond h095-copy9 c010) (bond h095-copy10 c010) (bond h095-copy11 c010) (bond h095-copy12 c010) (bond h095-copy13 c010) (bond h095-copy14 c010) (bond h095-copy15 c010) (bond h095-copy16 c010) (bond h095-copy17 c010) (bond h095-copy18 c010) (bond h095-copy19 c010) (bond h095-copy20 c010) (bond h095-copy21 c010) (bond h095-copy22 c010) (bond h095-copy23 c010) (bond h095-copy24 c010) (bond h095-copy25 c010) (bond h095-copy26 c010) (bond h095-copy27 c010) (bond h095-copy28 c010) (bond h095-copy29 c010) (bond h095-copy30 c010) (bond h095-copy31 c010) (bond h095-copy32 c010) (bond h095-copy33 c010) (bond h095-copy34 c010) (bond h095-copy35 c010) (bond h095-copy36 c010) (bond h095-copy37 c010) (bond h095-copy38 c010) (bond h095-copy39 c010) (bond h095-copy40 c010) (bond h095-copy41 c010) (bond h095-copy42 c010) (bond h095-copy43 c010) (bond h095-copy44 c010) (bond h095-copy45 c010) (bond h095-copy46 c010) (bond h095-copy47 c010) (bond h095-copy48 c010) (bond h095-copy49 c010) (bond h095-copy50 c010) (bond h095-copy51 c010) (bond h095-copy52 c010) (bond h095-copy53 c010) (bond h095-copy54 c010) (bond h095-copy55 c010) (bond h095-copy56 c010) (bond h095-copy57 c010) (bond h095-copy58 c010) (bond h095-copy59 c010) (bond h095-copy60 c010) (bond h095-copy61 c010) (bond h095-copy62 c010) (bond h095-copy63 c010) (bond h095-copy64 c010) (bond h095-copy65 c010) (bond h095-copy66 c010) (bond h095-copy67 c010) (bond h095-copy68 c010) (bond h095-copy69 c010) (bond h095-copy70 c010) (bond h095-copy71 c010) (bond h095-copy72 c010) (bond h095-copy73 c010) (bond h095-copy74 c010) (bond h095-copy75 c010) (bond h095-copy76 c010) (bond h095-copy77 c010) (bond h095-copy78 c010) (bond h095-copy79 c010) (bond h095-copy80 c010) (bond h095-copy81 c010) (bond h095-copy82 c010) (bond h095-copy83 c010) (bond h095-copy84 c010) (bond h095-copy85 c010) (bond h095-copy86 c010) (bond h095-copy87 c010) (bond h095-copy88 c010) (bond h095-copy89 c010) (bond h095-copy90 c010) (bond h095-copy91 c010) (bond h095-copy92 c010) (bond h095-copy93 c010) (bond h095-copy94 c010) (bond h095-copy95 c010) (bond h095-copy96 c010) (bond h095-copy97 c010) (bond h095-copy98 c010) (bond h095-copy99 c010) (bond h095-copy100 c010) (bond h095-copy101 c010) (bond h095-copy102 c010) (bond h095-copy103 c010) (bond h095-copy104 c010) (bond h095-copy105 c010) (bond h095-copy106 c010) (bond h095-copy107 c010) (bond h095-copy108 c010) (bond h095-copy109 c010) (bond h095-copy110 c010) (bond h095-copy111 c010) (bond h095-copy112 c010) (bond h095-copy113 c010) (bond h095-copy114 c010) (bond h095-copy115 c010) (bond h095-copy116 c010) (bond h095-copy117 c010) (bond h095-copy118 c010) (bond h095-copy119 c010) (bond h095-copy120 c010) (bond h095-copy121 c010) (bond h095-copy122 c010) (bond h095-copy123 c010) (bond h095-copy124 c010) (bond h095-copy125 c010) (bond h095-copy126 c010) (bond h095-copy127 c010) (bond h095-copy128 c010) (bond h095-copy129 c010) (bond h095-copy130 c010) (bond h095-copy131 c010) (bond h095-copy132 c010) (bond h095-copy133 c010) (bond h095-copy134 c010) (bond h095-copy135 c010) (bond h095-copy136 c010) (bond h095-copy137 c010) (bond h095-copy138 c010) (bond h095-copy139 c010) (bond h095-copy140 c010) (bond h095-copy141 c010) (bond h095-copy142 c010) (bond h095-copy143 c010) (bond h095-copy144 c010) (bond h095-copy145 c010) (bond h095-copy146 c010) (bond h095-copy147 c010) (bond h095-copy148 c010) (bond h095-copy149 c010) (bond h095-copy150 c010) (bond h095-copy151 c010) (bond h095-copy152 c010) (bond h095-copy153 c010) (bond h095-copy154 c010) (bond h095-copy155 c010) (bond h095-copy156 c010) (bond h095-copy157 c010) (bond h095-copy158 c010) (bond h095-copy159 c010) (bond h095-copy160 c010) (bond h095-copy161 c010) (bond h095-copy162 c010) (bond h095-copy163 c010) (bond h095-copy164 c010) (bond h095-copy165 c010) (bond h095-copy166 c010) (bond h095-copy167 c010) (bond h095-copy168 c010) (bond h095-copy169 c010) (bond h095-copy170 c010) (bond h095-copy171 c010) (bond h095-copy172 c010) (bond h095-copy173 c010) (bond h095-copy174 c010) (bond h095-copy175 c010) (bond h095-copy176 c010) (bond h095-copy177 c010) (bond h095-copy178 c010) (bond h095-copy179 c010) (bond h095-copy180 c010) (bond h095-copy181 c010) (bond h095-copy182 c010) (bond h095-copy183 c010) (bond h095-copy184 c010) (bond h095-copy185 c010) (bond h095-copy186 c010) (bond h095-copy187 c010) (bond h095-copy188 c010) (bond h095-copy189 c010) (bond h095-copy190 c010) (bond h095-copy191 c010) (bond h095-copy192 c010) (bond h095-copy193 c010) (bond h095-copy194 c010) (bond h095-copy195 c010) (bond h095-copy196 c010) (bond h095-copy197 c010) (bond h095-copy198 c010)

(bond c011 c013)
(bond c013 c011)

(bond c011 c012)
(bond c012 c011)

(bond c011 o063)
(bond o063 c011)

(bond c012 h098)
(bond h098 c012)

(bond c012 h097)
(bond h097 c012)

(bond c012 h099)
(bond h099 c012)

(bond c013 c015)
(bond c015 c013)

(bond c013 c014)
(bond c014 c013)

(bond c013 h057)
(bond h057 c013)

(bond c014 h102)
(bond h102 c014)

(bond c014 h100)
(bond h100 c014)

(bond c014 h101)
(bond h101 c014)

(bond c015 h104)
(bond h104 c015)

(bond c015 h103)
(bond h103 c015)

(bond c015 h105)
(bond h105 c015)

(bond h056 o063)
(bond o063 h056)
)
)
)