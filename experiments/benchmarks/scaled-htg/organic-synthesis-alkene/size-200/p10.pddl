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
o068 o068-copy1 o068-copy2 o068-copy3 o068-copy4 o068-copy5 o068-copy6 o068-copy7 o068-copy8 o068-copy9 o068-copy10 o068-copy11 o068-copy12 o068-copy13 o068-copy14 o068-copy15 o068-copy16 o068-copy17 o068-copy18 o068-copy19 o068-copy20 o068-copy21 o068-copy22 o068-copy23 o068-copy24 o068-copy25 o068-copy26 o068-copy27 o068-copy28 o068-copy29 o068-copy30 o068-copy31 o068-copy32 o068-copy33 o068-copy34 o068-copy35 o068-copy36 o068-copy37 o068-copy38 o068-copy39 o068-copy40 o068-copy41 o068-copy42 o068-copy43 o068-copy44 o068-copy45 o068-copy46 o068-copy47 o068-copy48 o068-copy49 o068-copy50 o068-copy51 o068-copy52 o068-copy53 o068-copy54 o068-copy55 o068-copy56 o068-copy57 o068-copy58 o068-copy59 o068-copy60 o068-copy61 o068-copy62 o068-copy63 o068-copy64 o068-copy65 o068-copy66 o068-copy67 o068-copy68 o068-copy69 o068-copy70 o068-copy71 o068-copy72 o068-copy73 o068-copy74 o068-copy75 o068-copy76 o068-copy77 o068-copy78 o068-copy79 o068-copy80 o068-copy81 o068-copy82 o068-copy83 o068-copy84 o068-copy85 o068-copy86 o068-copy87 o068-copy88 o068-copy89 o068-copy90 o068-copy91 o068-copy92 o068-copy93 o068-copy94 o068-copy95 o068-copy96 o068-copy97 o068-copy98 o068-copy99 o068-copy100 o068-copy101 o068-copy102 o068-copy103 o068-copy104 o068-copy105 o068-copy106 o068-copy107 o068-copy108 o068-copy109 o068-copy110 o068-copy111 o068-copy112 o068-copy113 o068-copy114 o068-copy115 o068-copy116 o068-copy117 o068-copy118 o068-copy119 o068-copy120 o068-copy121 o068-copy122 o068-copy123 o068-copy124 o068-copy125 o068-copy126 o068-copy127 o068-copy128 o068-copy129 o068-copy130 o068-copy131 o068-copy132 o068-copy133 o068-copy134 o068-copy135 o068-copy136 o068-copy137 o068-copy138 o068-copy139 o068-copy140 o068-copy141 o068-copy142 o068-copy143 o068-copy144 o068-copy145 o068-copy146 o068-copy147 o068-copy148 o068-copy149 o068-copy150 o068-copy151 o068-copy152 o068-copy153 o068-copy154 o068-copy155 o068-copy156 o068-copy157 o068-copy158 o068-copy159 o068-copy160 o068-copy161 o068-copy162 o068-copy163 o068-copy164 o068-copy165 o068-copy166 o068-copy167 o068-copy168 o068-copy169 o068-copy170 o068-copy171 o068-copy172 o068-copy173 o068-copy174 o068-copy175 o068-copy176 o068-copy177 o068-copy178 o068-copy179 o068-copy180 o068-copy181 o068-copy182 o068-copy183 o068-copy184 o068-copy185 o068-copy186 o068-copy187 o068-copy188 o068-copy189 o068-copy190 o068-copy191 o068-copy192 o068-copy193 o068-copy194 o068-copy195 o068-copy196 o068-copy197 o068-copy198 - oxygen
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

(doublebond o068 s072) (doublebond o068-copy1 s072) (doublebond o068-copy2 s072) (doublebond o068-copy3 s072) (doublebond o068-copy4 s072) (doublebond o068-copy5 s072) (doublebond o068-copy6 s072) (doublebond o068-copy7 s072) (doublebond o068-copy8 s072) (doublebond o068-copy9 s072) (doublebond o068-copy10 s072) (doublebond o068-copy11 s072) (doublebond o068-copy12 s072) (doublebond o068-copy13 s072) (doublebond o068-copy14 s072) (doublebond o068-copy15 s072) (doublebond o068-copy16 s072) (doublebond o068-copy17 s072) (doublebond o068-copy18 s072) (doublebond o068-copy19 s072) (doublebond o068-copy20 s072) (doublebond o068-copy21 s072) (doublebond o068-copy22 s072) (doublebond o068-copy23 s072) (doublebond o068-copy24 s072) (doublebond o068-copy25 s072) (doublebond o068-copy26 s072) (doublebond o068-copy27 s072) (doublebond o068-copy28 s072) (doublebond o068-copy29 s072) (doublebond o068-copy30 s072) (doublebond o068-copy31 s072) (doublebond o068-copy32 s072) (doublebond o068-copy33 s072) (doublebond o068-copy34 s072) (doublebond o068-copy35 s072) (doublebond o068-copy36 s072) (doublebond o068-copy37 s072) (doublebond o068-copy38 s072) (doublebond o068-copy39 s072) (doublebond o068-copy40 s072) (doublebond o068-copy41 s072) (doublebond o068-copy42 s072) (doublebond o068-copy43 s072) (doublebond o068-copy44 s072) (doublebond o068-copy45 s072) (doublebond o068-copy46 s072) (doublebond o068-copy47 s072) (doublebond o068-copy48 s072) (doublebond o068-copy49 s072) (doublebond o068-copy50 s072) (doublebond o068-copy51 s072) (doublebond o068-copy52 s072) (doublebond o068-copy53 s072) (doublebond o068-copy54 s072) (doublebond o068-copy55 s072) (doublebond o068-copy56 s072) (doublebond o068-copy57 s072) (doublebond o068-copy58 s072) (doublebond o068-copy59 s072) (doublebond o068-copy60 s072) (doublebond o068-copy61 s072) (doublebond o068-copy62 s072) (doublebond o068-copy63 s072) (doublebond o068-copy64 s072) (doublebond o068-copy65 s072) (doublebond o068-copy66 s072) (doublebond o068-copy67 s072) (doublebond o068-copy68 s072) (doublebond o068-copy69 s072) (doublebond o068-copy70 s072) (doublebond o068-copy71 s072) (doublebond o068-copy72 s072) (doublebond o068-copy73 s072) (doublebond o068-copy74 s072) (doublebond o068-copy75 s072) (doublebond o068-copy76 s072) (doublebond o068-copy77 s072) (doublebond o068-copy78 s072) (doublebond o068-copy79 s072) (doublebond o068-copy80 s072) (doublebond o068-copy81 s072) (doublebond o068-copy82 s072) (doublebond o068-copy83 s072) (doublebond o068-copy84 s072) (doublebond o068-copy85 s072) (doublebond o068-copy86 s072) (doublebond o068-copy87 s072) (doublebond o068-copy88 s072) (doublebond o068-copy89 s072) (doublebond o068-copy90 s072) (doublebond o068-copy91 s072) (doublebond o068-copy92 s072) (doublebond o068-copy93 s072) (doublebond o068-copy94 s072) (doublebond o068-copy95 s072) (doublebond o068-copy96 s072) (doublebond o068-copy97 s072) (doublebond o068-copy98 s072) (doublebond o068-copy99 s072) (doublebond o068-copy100 s072) (doublebond o068-copy101 s072) (doublebond o068-copy102 s072) (doublebond o068-copy103 s072) (doublebond o068-copy104 s072) (doublebond o068-copy105 s072) (doublebond o068-copy106 s072) (doublebond o068-copy107 s072) (doublebond o068-copy108 s072) (doublebond o068-copy109 s072) (doublebond o068-copy110 s072) (doublebond o068-copy111 s072) (doublebond o068-copy112 s072) (doublebond o068-copy113 s072) (doublebond o068-copy114 s072) (doublebond o068-copy115 s072) (doublebond o068-copy116 s072) (doublebond o068-copy117 s072) (doublebond o068-copy118 s072) (doublebond o068-copy119 s072) (doublebond o068-copy120 s072) (doublebond o068-copy121 s072) (doublebond o068-copy122 s072) (doublebond o068-copy123 s072) (doublebond o068-copy124 s072) (doublebond o068-copy125 s072) (doublebond o068-copy126 s072) (doublebond o068-copy127 s072) (doublebond o068-copy128 s072) (doublebond o068-copy129 s072) (doublebond o068-copy130 s072) (doublebond o068-copy131 s072) (doublebond o068-copy132 s072) (doublebond o068-copy133 s072) (doublebond o068-copy134 s072) (doublebond o068-copy135 s072) (doublebond o068-copy136 s072) (doublebond o068-copy137 s072) (doublebond o068-copy138 s072) (doublebond o068-copy139 s072) (doublebond o068-copy140 s072) (doublebond o068-copy141 s072) (doublebond o068-copy142 s072) (doublebond o068-copy143 s072) (doublebond o068-copy144 s072) (doublebond o068-copy145 s072) (doublebond o068-copy146 s072) (doublebond o068-copy147 s072) (doublebond o068-copy148 s072) (doublebond o068-copy149 s072) (doublebond o068-copy150 s072) (doublebond o068-copy151 s072) (doublebond o068-copy152 s072) (doublebond o068-copy153 s072) (doublebond o068-copy154 s072) (doublebond o068-copy155 s072) (doublebond o068-copy156 s072) (doublebond o068-copy157 s072) (doublebond o068-copy158 s072) (doublebond o068-copy159 s072) (doublebond o068-copy160 s072) (doublebond o068-copy161 s072) (doublebond o068-copy162 s072) (doublebond o068-copy163 s072) (doublebond o068-copy164 s072) (doublebond o068-copy165 s072) (doublebond o068-copy166 s072) (doublebond o068-copy167 s072) (doublebond o068-copy168 s072) (doublebond o068-copy169 s072) (doublebond o068-copy170 s072) (doublebond o068-copy171 s072) (doublebond o068-copy172 s072) (doublebond o068-copy173 s072) (doublebond o068-copy174 s072) (doublebond o068-copy175 s072) (doublebond o068-copy176 s072) (doublebond o068-copy177 s072) (doublebond o068-copy178 s072) (doublebond o068-copy179 s072) (doublebond o068-copy180 s072) (doublebond o068-copy181 s072) (doublebond o068-copy182 s072) (doublebond o068-copy183 s072) (doublebond o068-copy184 s072) (doublebond o068-copy185 s072) (doublebond o068-copy186 s072) (doublebond o068-copy187 s072) (doublebond o068-copy188 s072) (doublebond o068-copy189 s072) (doublebond o068-copy190 s072) (doublebond o068-copy191 s072) (doublebond o068-copy192 s072) (doublebond o068-copy193 s072) (doublebond o068-copy194 s072) (doublebond o068-copy195 s072) (doublebond o068-copy196 s072) (doublebond o068-copy197 s072) (doublebond o068-copy198 s072)
(doublebond s072 o068) (doublebond s072 o068-copy1) (doublebond s072 o068-copy2) (doublebond s072 o068-copy3) (doublebond s072 o068-copy4) (doublebond s072 o068-copy5) (doublebond s072 o068-copy6) (doublebond s072 o068-copy7) (doublebond s072 o068-copy8) (doublebond s072 o068-copy9) (doublebond s072 o068-copy10) (doublebond s072 o068-copy11) (doublebond s072 o068-copy12) (doublebond s072 o068-copy13) (doublebond s072 o068-copy14) (doublebond s072 o068-copy15) (doublebond s072 o068-copy16) (doublebond s072 o068-copy17) (doublebond s072 o068-copy18) (doublebond s072 o068-copy19) (doublebond s072 o068-copy20) (doublebond s072 o068-copy21) (doublebond s072 o068-copy22) (doublebond s072 o068-copy23) (doublebond s072 o068-copy24) (doublebond s072 o068-copy25) (doublebond s072 o068-copy26) (doublebond s072 o068-copy27) (doublebond s072 o068-copy28) (doublebond s072 o068-copy29) (doublebond s072 o068-copy30) (doublebond s072 o068-copy31) (doublebond s072 o068-copy32) (doublebond s072 o068-copy33) (doublebond s072 o068-copy34) (doublebond s072 o068-copy35) (doublebond s072 o068-copy36) (doublebond s072 o068-copy37) (doublebond s072 o068-copy38) (doublebond s072 o068-copy39) (doublebond s072 o068-copy40) (doublebond s072 o068-copy41) (doublebond s072 o068-copy42) (doublebond s072 o068-copy43) (doublebond s072 o068-copy44) (doublebond s072 o068-copy45) (doublebond s072 o068-copy46) (doublebond s072 o068-copy47) (doublebond s072 o068-copy48) (doublebond s072 o068-copy49) (doublebond s072 o068-copy50) (doublebond s072 o068-copy51) (doublebond s072 o068-copy52) (doublebond s072 o068-copy53) (doublebond s072 o068-copy54) (doublebond s072 o068-copy55) (doublebond s072 o068-copy56) (doublebond s072 o068-copy57) (doublebond s072 o068-copy58) (doublebond s072 o068-copy59) (doublebond s072 o068-copy60) (doublebond s072 o068-copy61) (doublebond s072 o068-copy62) (doublebond s072 o068-copy63) (doublebond s072 o068-copy64) (doublebond s072 o068-copy65) (doublebond s072 o068-copy66) (doublebond s072 o068-copy67) (doublebond s072 o068-copy68) (doublebond s072 o068-copy69) (doublebond s072 o068-copy70) (doublebond s072 o068-copy71) (doublebond s072 o068-copy72) (doublebond s072 o068-copy73) (doublebond s072 o068-copy74) (doublebond s072 o068-copy75) (doublebond s072 o068-copy76) (doublebond s072 o068-copy77) (doublebond s072 o068-copy78) (doublebond s072 o068-copy79) (doublebond s072 o068-copy80) (doublebond s072 o068-copy81) (doublebond s072 o068-copy82) (doublebond s072 o068-copy83) (doublebond s072 o068-copy84) (doublebond s072 o068-copy85) (doublebond s072 o068-copy86) (doublebond s072 o068-copy87) (doublebond s072 o068-copy88) (doublebond s072 o068-copy89) (doublebond s072 o068-copy90) (doublebond s072 o068-copy91) (doublebond s072 o068-copy92) (doublebond s072 o068-copy93) (doublebond s072 o068-copy94) (doublebond s072 o068-copy95) (doublebond s072 o068-copy96) (doublebond s072 o068-copy97) (doublebond s072 o068-copy98) (doublebond s072 o068-copy99) (doublebond s072 o068-copy100) (doublebond s072 o068-copy101) (doublebond s072 o068-copy102) (doublebond s072 o068-copy103) (doublebond s072 o068-copy104) (doublebond s072 o068-copy105) (doublebond s072 o068-copy106) (doublebond s072 o068-copy107) (doublebond s072 o068-copy108) (doublebond s072 o068-copy109) (doublebond s072 o068-copy110) (doublebond s072 o068-copy111) (doublebond s072 o068-copy112) (doublebond s072 o068-copy113) (doublebond s072 o068-copy114) (doublebond s072 o068-copy115) (doublebond s072 o068-copy116) (doublebond s072 o068-copy117) (doublebond s072 o068-copy118) (doublebond s072 o068-copy119) (doublebond s072 o068-copy120) (doublebond s072 o068-copy121) (doublebond s072 o068-copy122) (doublebond s072 o068-copy123) (doublebond s072 o068-copy124) (doublebond s072 o068-copy125) (doublebond s072 o068-copy126) (doublebond s072 o068-copy127) (doublebond s072 o068-copy128) (doublebond s072 o068-copy129) (doublebond s072 o068-copy130) (doublebond s072 o068-copy131) (doublebond s072 o068-copy132) (doublebond s072 o068-copy133) (doublebond s072 o068-copy134) (doublebond s072 o068-copy135) (doublebond s072 o068-copy136) (doublebond s072 o068-copy137) (doublebond s072 o068-copy138) (doublebond s072 o068-copy139) (doublebond s072 o068-copy140) (doublebond s072 o068-copy141) (doublebond s072 o068-copy142) (doublebond s072 o068-copy143) (doublebond s072 o068-copy144) (doublebond s072 o068-copy145) (doublebond s072 o068-copy146) (doublebond s072 o068-copy147) (doublebond s072 o068-copy148) (doublebond s072 o068-copy149) (doublebond s072 o068-copy150) (doublebond s072 o068-copy151) (doublebond s072 o068-copy152) (doublebond s072 o068-copy153) (doublebond s072 o068-copy154) (doublebond s072 o068-copy155) (doublebond s072 o068-copy156) (doublebond s072 o068-copy157) (doublebond s072 o068-copy158) (doublebond s072 o068-copy159) (doublebond s072 o068-copy160) (doublebond s072 o068-copy161) (doublebond s072 o068-copy162) (doublebond s072 o068-copy163) (doublebond s072 o068-copy164) (doublebond s072 o068-copy165) (doublebond s072 o068-copy166) (doublebond s072 o068-copy167) (doublebond s072 o068-copy168) (doublebond s072 o068-copy169) (doublebond s072 o068-copy170) (doublebond s072 o068-copy171) (doublebond s072 o068-copy172) (doublebond s072 o068-copy173) (doublebond s072 o068-copy174) (doublebond s072 o068-copy175) (doublebond s072 o068-copy176) (doublebond s072 o068-copy177) (doublebond s072 o068-copy178) (doublebond s072 o068-copy179) (doublebond s072 o068-copy180) (doublebond s072 o068-copy181) (doublebond s072 o068-copy182) (doublebond s072 o068-copy183) (doublebond s072 o068-copy184) (doublebond s072 o068-copy185) (doublebond s072 o068-copy186) (doublebond s072 o068-copy187) (doublebond s072 o068-copy188) (doublebond s072 o068-copy189) (doublebond s072 o068-copy190) (doublebond s072 o068-copy191) (doublebond s072 o068-copy192) (doublebond s072 o068-copy193) (doublebond s072 o068-copy194) (doublebond s072 o068-copy195) (doublebond s072 o068-copy196) (doublebond s072 o068-copy197) (doublebond s072 o068-copy198)

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