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
h095 h095-copy1 h095-copy2 h095-copy3 h095-copy4 h095-copy5 h095-copy6 h095-copy7 h095-copy8 h095-copy9 h095-copy10 h095-copy11 h095-copy12 h095-copy13 h095-copy14 h095-copy15 h095-copy16 h095-copy17 h095-copy18 h095-copy19 h095-copy20 h095-copy21 h095-copy22 h095-copy23 h095-copy24 h095-copy25 h095-copy26 h095-copy27 h095-copy28 h095-copy29 h095-copy30 h095-copy31 h095-copy32 h095-copy33 h095-copy34 h095-copy35 h095-copy36 h095-copy37 h095-copy38 h095-copy39 h095-copy40 h095-copy41 h095-copy42 h095-copy43 h095-copy44 h095-copy45 h095-copy46 h095-copy47 h095-copy48 h095-copy49 h095-copy50 h095-copy51 h095-copy52 h095-copy53 h095-copy54 h095-copy55 h095-copy56 h095-copy57 h095-copy58 h095-copy59 h095-copy60 h095-copy61 h095-copy62 h095-copy63 h095-copy64 h095-copy65 h095-copy66 h095-copy67 h095-copy68 h095-copy69 h095-copy70 h095-copy71 h095-copy72 h095-copy73 h095-copy74 h095-copy75 h095-copy76 h095-copy77 h095-copy78 h095-copy79 h095-copy80 h095-copy81 h095-copy82 h095-copy83 h095-copy84 h095-copy85 h095-copy86 h095-copy87 h095-copy88 h095-copy89 h095-copy90 h095-copy91 h095-copy92 h095-copy93 h095-copy94 h095-copy95 h095-copy96 h095-copy97 h095-copy98 - hydrogen
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

(bond c010 h095) (bond c010 h095-copy1) (bond c010 h095-copy2) (bond c010 h095-copy3) (bond c010 h095-copy4) (bond c010 h095-copy5) (bond c010 h095-copy6) (bond c010 h095-copy7) (bond c010 h095-copy8) (bond c010 h095-copy9) (bond c010 h095-copy10) (bond c010 h095-copy11) (bond c010 h095-copy12) (bond c010 h095-copy13) (bond c010 h095-copy14) (bond c010 h095-copy15) (bond c010 h095-copy16) (bond c010 h095-copy17) (bond c010 h095-copy18) (bond c010 h095-copy19) (bond c010 h095-copy20) (bond c010 h095-copy21) (bond c010 h095-copy22) (bond c010 h095-copy23) (bond c010 h095-copy24) (bond c010 h095-copy25) (bond c010 h095-copy26) (bond c010 h095-copy27) (bond c010 h095-copy28) (bond c010 h095-copy29) (bond c010 h095-copy30) (bond c010 h095-copy31) (bond c010 h095-copy32) (bond c010 h095-copy33) (bond c010 h095-copy34) (bond c010 h095-copy35) (bond c010 h095-copy36) (bond c010 h095-copy37) (bond c010 h095-copy38) (bond c010 h095-copy39) (bond c010 h095-copy40) (bond c010 h095-copy41) (bond c010 h095-copy42) (bond c010 h095-copy43) (bond c010 h095-copy44) (bond c010 h095-copy45) (bond c010 h095-copy46) (bond c010 h095-copy47) (bond c010 h095-copy48) (bond c010 h095-copy49) (bond c010 h095-copy50) (bond c010 h095-copy51) (bond c010 h095-copy52) (bond c010 h095-copy53) (bond c010 h095-copy54) (bond c010 h095-copy55) (bond c010 h095-copy56) (bond c010 h095-copy57) (bond c010 h095-copy58) (bond c010 h095-copy59) (bond c010 h095-copy60) (bond c010 h095-copy61) (bond c010 h095-copy62) (bond c010 h095-copy63) (bond c010 h095-copy64) (bond c010 h095-copy65) (bond c010 h095-copy66) (bond c010 h095-copy67) (bond c010 h095-copy68) (bond c010 h095-copy69) (bond c010 h095-copy70) (bond c010 h095-copy71) (bond c010 h095-copy72) (bond c010 h095-copy73) (bond c010 h095-copy74) (bond c010 h095-copy75) (bond c010 h095-copy76) (bond c010 h095-copy77) (bond c010 h095-copy78) (bond c010 h095-copy79) (bond c010 h095-copy80) (bond c010 h095-copy81) (bond c010 h095-copy82) (bond c010 h095-copy83) (bond c010 h095-copy84) (bond c010 h095-copy85) (bond c010 h095-copy86) (bond c010 h095-copy87) (bond c010 h095-copy88) (bond c010 h095-copy89) (bond c010 h095-copy90) (bond c010 h095-copy91) (bond c010 h095-copy92) (bond c010 h095-copy93) (bond c010 h095-copy94) (bond c010 h095-copy95) (bond c010 h095-copy96) (bond c010 h095-copy97) (bond c010 h095-copy98)
(bond h095 c010) (bond h095-copy1 c010) (bond h095-copy2 c010) (bond h095-copy3 c010) (bond h095-copy4 c010) (bond h095-copy5 c010) (bond h095-copy6 c010) (bond h095-copy7 c010) (bond h095-copy8 c010) (bond h095-copy9 c010) (bond h095-copy10 c010) (bond h095-copy11 c010) (bond h095-copy12 c010) (bond h095-copy13 c010) (bond h095-copy14 c010) (bond h095-copy15 c010) (bond h095-copy16 c010) (bond h095-copy17 c010) (bond h095-copy18 c010) (bond h095-copy19 c010) (bond h095-copy20 c010) (bond h095-copy21 c010) (bond h095-copy22 c010) (bond h095-copy23 c010) (bond h095-copy24 c010) (bond h095-copy25 c010) (bond h095-copy26 c010) (bond h095-copy27 c010) (bond h095-copy28 c010) (bond h095-copy29 c010) (bond h095-copy30 c010) (bond h095-copy31 c010) (bond h095-copy32 c010) (bond h095-copy33 c010) (bond h095-copy34 c010) (bond h095-copy35 c010) (bond h095-copy36 c010) (bond h095-copy37 c010) (bond h095-copy38 c010) (bond h095-copy39 c010) (bond h095-copy40 c010) (bond h095-copy41 c010) (bond h095-copy42 c010) (bond h095-copy43 c010) (bond h095-copy44 c010) (bond h095-copy45 c010) (bond h095-copy46 c010) (bond h095-copy47 c010) (bond h095-copy48 c010) (bond h095-copy49 c010) (bond h095-copy50 c010) (bond h095-copy51 c010) (bond h095-copy52 c010) (bond h095-copy53 c010) (bond h095-copy54 c010) (bond h095-copy55 c010) (bond h095-copy56 c010) (bond h095-copy57 c010) (bond h095-copy58 c010) (bond h095-copy59 c010) (bond h095-copy60 c010) (bond h095-copy61 c010) (bond h095-copy62 c010) (bond h095-copy63 c010) (bond h095-copy64 c010) (bond h095-copy65 c010) (bond h095-copy66 c010) (bond h095-copy67 c010) (bond h095-copy68 c010) (bond h095-copy69 c010) (bond h095-copy70 c010) (bond h095-copy71 c010) (bond h095-copy72 c010) (bond h095-copy73 c010) (bond h095-copy74 c010) (bond h095-copy75 c010) (bond h095-copy76 c010) (bond h095-copy77 c010) (bond h095-copy78 c010) (bond h095-copy79 c010) (bond h095-copy80 c010) (bond h095-copy81 c010) (bond h095-copy82 c010) (bond h095-copy83 c010) (bond h095-copy84 c010) (bond h095-copy85 c010) (bond h095-copy86 c010) (bond h095-copy87 c010) (bond h095-copy88 c010) (bond h095-copy89 c010) (bond h095-copy90 c010) (bond h095-copy91 c010) (bond h095-copy92 c010) (bond h095-copy93 c010) (bond h095-copy94 c010) (bond h095-copy95 c010) (bond h095-copy96 c010) (bond h095-copy97 c010) (bond h095-copy98 c010)

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

(bond c010 h095) (bond c010 h095-copy1) (bond c010 h095-copy2) (bond c010 h095-copy3) (bond c010 h095-copy4) (bond c010 h095-copy5) (bond c010 h095-copy6) (bond c010 h095-copy7) (bond c010 h095-copy8) (bond c010 h095-copy9) (bond c010 h095-copy10) (bond c010 h095-copy11) (bond c010 h095-copy12) (bond c010 h095-copy13) (bond c010 h095-copy14) (bond c010 h095-copy15) (bond c010 h095-copy16) (bond c010 h095-copy17) (bond c010 h095-copy18) (bond c010 h095-copy19) (bond c010 h095-copy20) (bond c010 h095-copy21) (bond c010 h095-copy22) (bond c010 h095-copy23) (bond c010 h095-copy24) (bond c010 h095-copy25) (bond c010 h095-copy26) (bond c010 h095-copy27) (bond c010 h095-copy28) (bond c010 h095-copy29) (bond c010 h095-copy30) (bond c010 h095-copy31) (bond c010 h095-copy32) (bond c010 h095-copy33) (bond c010 h095-copy34) (bond c010 h095-copy35) (bond c010 h095-copy36) (bond c010 h095-copy37) (bond c010 h095-copy38) (bond c010 h095-copy39) (bond c010 h095-copy40) (bond c010 h095-copy41) (bond c010 h095-copy42) (bond c010 h095-copy43) (bond c010 h095-copy44) (bond c010 h095-copy45) (bond c010 h095-copy46) (bond c010 h095-copy47) (bond c010 h095-copy48) (bond c010 h095-copy49) (bond c010 h095-copy50) (bond c010 h095-copy51) (bond c010 h095-copy52) (bond c010 h095-copy53) (bond c010 h095-copy54) (bond c010 h095-copy55) (bond c010 h095-copy56) (bond c010 h095-copy57) (bond c010 h095-copy58) (bond c010 h095-copy59) (bond c010 h095-copy60) (bond c010 h095-copy61) (bond c010 h095-copy62) (bond c010 h095-copy63) (bond c010 h095-copy64) (bond c010 h095-copy65) (bond c010 h095-copy66) (bond c010 h095-copy67) (bond c010 h095-copy68) (bond c010 h095-copy69) (bond c010 h095-copy70) (bond c010 h095-copy71) (bond c010 h095-copy72) (bond c010 h095-copy73) (bond c010 h095-copy74) (bond c010 h095-copy75) (bond c010 h095-copy76) (bond c010 h095-copy77) (bond c010 h095-copy78) (bond c010 h095-copy79) (bond c010 h095-copy80) (bond c010 h095-copy81) (bond c010 h095-copy82) (bond c010 h095-copy83) (bond c010 h095-copy84) (bond c010 h095-copy85) (bond c010 h095-copy86) (bond c010 h095-copy87) (bond c010 h095-copy88) (bond c010 h095-copy89) (bond c010 h095-copy90) (bond c010 h095-copy91) (bond c010 h095-copy92) (bond c010 h095-copy93) (bond c010 h095-copy94) (bond c010 h095-copy95) (bond c010 h095-copy96) (bond c010 h095-copy97) (bond c010 h095-copy98)
(bond h095 c010) (bond h095-copy1 c010) (bond h095-copy2 c010) (bond h095-copy3 c010) (bond h095-copy4 c010) (bond h095-copy5 c010) (bond h095-copy6 c010) (bond h095-copy7 c010) (bond h095-copy8 c010) (bond h095-copy9 c010) (bond h095-copy10 c010) (bond h095-copy11 c010) (bond h095-copy12 c010) (bond h095-copy13 c010) (bond h095-copy14 c010) (bond h095-copy15 c010) (bond h095-copy16 c010) (bond h095-copy17 c010) (bond h095-copy18 c010) (bond h095-copy19 c010) (bond h095-copy20 c010) (bond h095-copy21 c010) (bond h095-copy22 c010) (bond h095-copy23 c010) (bond h095-copy24 c010) (bond h095-copy25 c010) (bond h095-copy26 c010) (bond h095-copy27 c010) (bond h095-copy28 c010) (bond h095-copy29 c010) (bond h095-copy30 c010) (bond h095-copy31 c010) (bond h095-copy32 c010) (bond h095-copy33 c010) (bond h095-copy34 c010) (bond h095-copy35 c010) (bond h095-copy36 c010) (bond h095-copy37 c010) (bond h095-copy38 c010) (bond h095-copy39 c010) (bond h095-copy40 c010) (bond h095-copy41 c010) (bond h095-copy42 c010) (bond h095-copy43 c010) (bond h095-copy44 c010) (bond h095-copy45 c010) (bond h095-copy46 c010) (bond h095-copy47 c010) (bond h095-copy48 c010) (bond h095-copy49 c010) (bond h095-copy50 c010) (bond h095-copy51 c010) (bond h095-copy52 c010) (bond h095-copy53 c010) (bond h095-copy54 c010) (bond h095-copy55 c010) (bond h095-copy56 c010) (bond h095-copy57 c010) (bond h095-copy58 c010) (bond h095-copy59 c010) (bond h095-copy60 c010) (bond h095-copy61 c010) (bond h095-copy62 c010) (bond h095-copy63 c010) (bond h095-copy64 c010) (bond h095-copy65 c010) (bond h095-copy66 c010) (bond h095-copy67 c010) (bond h095-copy68 c010) (bond h095-copy69 c010) (bond h095-copy70 c010) (bond h095-copy71 c010) (bond h095-copy72 c010) (bond h095-copy73 c010) (bond h095-copy74 c010) (bond h095-copy75 c010) (bond h095-copy76 c010) (bond h095-copy77 c010) (bond h095-copy78 c010) (bond h095-copy79 c010) (bond h095-copy80 c010) (bond h095-copy81 c010) (bond h095-copy82 c010) (bond h095-copy83 c010) (bond h095-copy84 c010) (bond h095-copy85 c010) (bond h095-copy86 c010) (bond h095-copy87 c010) (bond h095-copy88 c010) (bond h095-copy89 c010) (bond h095-copy90 c010) (bond h095-copy91 c010) (bond h095-copy92 c010) (bond h095-copy93 c010) (bond h095-copy94 c010) (bond h095-copy95 c010) (bond h095-copy96 c010) (bond h095-copy97 c010) (bond h095-copy98 c010)

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