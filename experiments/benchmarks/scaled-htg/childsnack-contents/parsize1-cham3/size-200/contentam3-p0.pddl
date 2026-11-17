
(define (problem example-problem)
  (:domain htg-child-snack)
  (:objects
    child0 child1 child2 - child
    bread0 bread0-copy1 bread0-copy2 bread0-copy3 bread0-copy4 bread0-copy5 bread0-copy6 bread0-copy7 bread0-copy8 bread0-copy9 bread0-copy10 bread0-copy11 bread0-copy12 bread0-copy13 bread0-copy14 bread0-copy15 bread0-copy16 bread0-copy17 bread0-copy18 bread0-copy19 bread0-copy20 bread0-copy21 bread0-copy22 bread0-copy23 bread0-copy24 bread0-copy25 bread0-copy26 bread0-copy27 bread0-copy28 bread0-copy29 bread0-copy30 bread0-copy31 bread0-copy32 bread0-copy33 bread0-copy34 bread0-copy35 bread0-copy36 bread0-copy37 bread0-copy38 bread0-copy39 bread0-copy40 bread0-copy41 bread0-copy42 bread0-copy43 bread0-copy44 bread0-copy45 bread0-copy46 bread0-copy47 bread0-copy48 bread0-copy49 bread0-copy50 bread0-copy51 bread0-copy52 bread0-copy53 bread0-copy54 bread0-copy55 bread0-copy56 bread0-copy57 bread0-copy58 bread0-copy59 bread0-copy60 bread0-copy61 bread0-copy62 bread0-copy63 bread0-copy64 bread0-copy65 bread0-copy66 bread0-copy67 bread0-copy68 bread0-copy69 bread0-copy70 bread0-copy71 bread0-copy72 bread0-copy73 bread0-copy74 bread0-copy75 bread0-copy76 bread0-copy77 bread0-copy78 bread0-copy79 bread0-copy80 bread0-copy81 bread0-copy82 bread0-copy83 bread0-copy84 bread0-copy85 bread0-copy86 bread0-copy87 bread0-copy88 bread0-copy89 bread0-copy90 bread0-copy91 bread0-copy92 bread0-copy93 bread0-copy94 bread0-copy95 bread0-copy96 bread0-copy97 bread0-copy98 bread0-copy99 bread0-copy100 bread0-copy101 bread0-copy102 bread0-copy103 bread0-copy104 bread0-copy105 bread0-copy106 bread0-copy107 bread0-copy108 bread0-copy109 bread0-copy110 bread0-copy111 bread0-copy112 bread0-copy113 bread0-copy114 bread0-copy115 bread0-copy116 bread0-copy117 bread0-copy118 bread0-copy119 bread0-copy120 bread0-copy121 bread0-copy122 bread0-copy123 bread0-copy124 bread0-copy125 bread0-copy126 bread0-copy127 bread0-copy128 bread0-copy129 bread0-copy130 bread0-copy131 bread0-copy132 bread0-copy133 bread0-copy134 bread0-copy135 bread0-copy136 bread0-copy137 bread0-copy138 bread0-copy139 bread0-copy140 bread0-copy141 bread0-copy142 bread0-copy143 bread0-copy144 bread0-copy145 bread0-copy146 bread0-copy147 bread0-copy148 bread0-copy149 bread0-copy150 bread0-copy151 bread0-copy152 bread0-copy153 bread0-copy154 bread0-copy155 bread0-copy156 bread0-copy157 bread0-copy158 bread0-copy159 bread0-copy160 bread0-copy161 bread0-copy162 bread0-copy163 bread0-copy164 bread0-copy165 bread0-copy166 bread0-copy167 bread0-copy168 bread0-copy169 bread0-copy170 bread0-copy171 bread0-copy172 bread0-copy173 bread0-copy174 bread0-copy175 bread0-copy176 bread0-copy177 bread0-copy178 bread0-copy179 bread0-copy180 bread0-copy181 bread0-copy182 bread0-copy183 bread0-copy184 bread0-copy185 bread0-copy186 bread0-copy187 bread0-copy188 bread0-copy189 bread0-copy190 bread0-copy191 bread0-copy192 bread0-copy193 bread0-copy194 bread0-copy195 bread0-copy196 bread0-copy197 bread1 bread2 - bread-portion
    content-0 content-1 content-2 - content-description
    content-0-0 - content-portion
    content-1-0 - content-portion
    content-2-0 - content-portion
    tray0 tray1 tray2 - tray
    table0 table1 table2 table3 table4 - place
    sandw0 sandw1 sandw2 - sandwich
  )
  (:init
     ;; everythin starts in the kitchen
     (at tray0 kitchen)
     (at tray1 kitchen)
     (at tray2 kitchen)
			    (at_kitchen_bread bread0) (at_kitchen_bread bread0-copy1) (at_kitchen_bread bread0-copy2) (at_kitchen_bread bread0-copy3) (at_kitchen_bread bread0-copy4) (at_kitchen_bread bread0-copy5) (at_kitchen_bread bread0-copy6) (at_kitchen_bread bread0-copy7) (at_kitchen_bread bread0-copy8) (at_kitchen_bread bread0-copy9) (at_kitchen_bread bread0-copy10) (at_kitchen_bread bread0-copy11) (at_kitchen_bread bread0-copy12) (at_kitchen_bread bread0-copy13) (at_kitchen_bread bread0-copy14) (at_kitchen_bread bread0-copy15) (at_kitchen_bread bread0-copy16) (at_kitchen_bread bread0-copy17) (at_kitchen_bread bread0-copy18) (at_kitchen_bread bread0-copy19) (at_kitchen_bread bread0-copy20) (at_kitchen_bread bread0-copy21) (at_kitchen_bread bread0-copy22) (at_kitchen_bread bread0-copy23) (at_kitchen_bread bread0-copy24) (at_kitchen_bread bread0-copy25) (at_kitchen_bread bread0-copy26) (at_kitchen_bread bread0-copy27) (at_kitchen_bread bread0-copy28) (at_kitchen_bread bread0-copy29) (at_kitchen_bread bread0-copy30) (at_kitchen_bread bread0-copy31) (at_kitchen_bread bread0-copy32) (at_kitchen_bread bread0-copy33) (at_kitchen_bread bread0-copy34) (at_kitchen_bread bread0-copy35) (at_kitchen_bread bread0-copy36) (at_kitchen_bread bread0-copy37) (at_kitchen_bread bread0-copy38) (at_kitchen_bread bread0-copy39) (at_kitchen_bread bread0-copy40) (at_kitchen_bread bread0-copy41) (at_kitchen_bread bread0-copy42) (at_kitchen_bread bread0-copy43) (at_kitchen_bread bread0-copy44) (at_kitchen_bread bread0-copy45) (at_kitchen_bread bread0-copy46) (at_kitchen_bread bread0-copy47) (at_kitchen_bread bread0-copy48) (at_kitchen_bread bread0-copy49) (at_kitchen_bread bread0-copy50) (at_kitchen_bread bread0-copy51) (at_kitchen_bread bread0-copy52) (at_kitchen_bread bread0-copy53) (at_kitchen_bread bread0-copy54) (at_kitchen_bread bread0-copy55) (at_kitchen_bread bread0-copy56) (at_kitchen_bread bread0-copy57) (at_kitchen_bread bread0-copy58) (at_kitchen_bread bread0-copy59) (at_kitchen_bread bread0-copy60) (at_kitchen_bread bread0-copy61) (at_kitchen_bread bread0-copy62) (at_kitchen_bread bread0-copy63) (at_kitchen_bread bread0-copy64) (at_kitchen_bread bread0-copy65) (at_kitchen_bread bread0-copy66) (at_kitchen_bread bread0-copy67) (at_kitchen_bread bread0-copy68) (at_kitchen_bread bread0-copy69) (at_kitchen_bread bread0-copy70) (at_kitchen_bread bread0-copy71) (at_kitchen_bread bread0-copy72) (at_kitchen_bread bread0-copy73) (at_kitchen_bread bread0-copy74) (at_kitchen_bread bread0-copy75) (at_kitchen_bread bread0-copy76) (at_kitchen_bread bread0-copy77) (at_kitchen_bread bread0-copy78) (at_kitchen_bread bread0-copy79) (at_kitchen_bread bread0-copy80) (at_kitchen_bread bread0-copy81) (at_kitchen_bread bread0-copy82) (at_kitchen_bread bread0-copy83) (at_kitchen_bread bread0-copy84) (at_kitchen_bread bread0-copy85) (at_kitchen_bread bread0-copy86) (at_kitchen_bread bread0-copy87) (at_kitchen_bread bread0-copy88) (at_kitchen_bread bread0-copy89) (at_kitchen_bread bread0-copy90) (at_kitchen_bread bread0-copy91) (at_kitchen_bread bread0-copy92) (at_kitchen_bread bread0-copy93) (at_kitchen_bread bread0-copy94) (at_kitchen_bread bread0-copy95) (at_kitchen_bread bread0-copy96) (at_kitchen_bread bread0-copy97) (at_kitchen_bread bread0-copy98) (at_kitchen_bread bread0-copy99) (at_kitchen_bread bread0-copy100) (at_kitchen_bread bread0-copy101) (at_kitchen_bread bread0-copy102) (at_kitchen_bread bread0-copy103) (at_kitchen_bread bread0-copy104) (at_kitchen_bread bread0-copy105) (at_kitchen_bread bread0-copy106) (at_kitchen_bread bread0-copy107) (at_kitchen_bread bread0-copy108) (at_kitchen_bread bread0-copy109) (at_kitchen_bread bread0-copy110) (at_kitchen_bread bread0-copy111) (at_kitchen_bread bread0-copy112) (at_kitchen_bread bread0-copy113) (at_kitchen_bread bread0-copy114) (at_kitchen_bread bread0-copy115) (at_kitchen_bread bread0-copy116) (at_kitchen_bread bread0-copy117) (at_kitchen_bread bread0-copy118) (at_kitchen_bread bread0-copy119) (at_kitchen_bread bread0-copy120) (at_kitchen_bread bread0-copy121) (at_kitchen_bread bread0-copy122) (at_kitchen_bread bread0-copy123) (at_kitchen_bread bread0-copy124) (at_kitchen_bread bread0-copy125) (at_kitchen_bread bread0-copy126) (at_kitchen_bread bread0-copy127) (at_kitchen_bread bread0-copy128) (at_kitchen_bread bread0-copy129) (at_kitchen_bread bread0-copy130) (at_kitchen_bread bread0-copy131) (at_kitchen_bread bread0-copy132) (at_kitchen_bread bread0-copy133) (at_kitchen_bread bread0-copy134) (at_kitchen_bread bread0-copy135) (at_kitchen_bread bread0-copy136) (at_kitchen_bread bread0-copy137) (at_kitchen_bread bread0-copy138) (at_kitchen_bread bread0-copy139) (at_kitchen_bread bread0-copy140) (at_kitchen_bread bread0-copy141) (at_kitchen_bread bread0-copy142) (at_kitchen_bread bread0-copy143) (at_kitchen_bread bread0-copy144) (at_kitchen_bread bread0-copy145) (at_kitchen_bread bread0-copy146) (at_kitchen_bread bread0-copy147) (at_kitchen_bread bread0-copy148) (at_kitchen_bread bread0-copy149) (at_kitchen_bread bread0-copy150) (at_kitchen_bread bread0-copy151) (at_kitchen_bread bread0-copy152) (at_kitchen_bread bread0-copy153) (at_kitchen_bread bread0-copy154) (at_kitchen_bread bread0-copy155) (at_kitchen_bread bread0-copy156) (at_kitchen_bread bread0-copy157) (at_kitchen_bread bread0-copy158) (at_kitchen_bread bread0-copy159) (at_kitchen_bread bread0-copy160) (at_kitchen_bread bread0-copy161) (at_kitchen_bread bread0-copy162) (at_kitchen_bread bread0-copy163) (at_kitchen_bread bread0-copy164) (at_kitchen_bread bread0-copy165) (at_kitchen_bread bread0-copy166) (at_kitchen_bread bread0-copy167) (at_kitchen_bread bread0-copy168) (at_kitchen_bread bread0-copy169) (at_kitchen_bread bread0-copy170) (at_kitchen_bread bread0-copy171) (at_kitchen_bread bread0-copy172) (at_kitchen_bread bread0-copy173) (at_kitchen_bread bread0-copy174) (at_kitchen_bread bread0-copy175) (at_kitchen_bread bread0-copy176) (at_kitchen_bread bread0-copy177) (at_kitchen_bread bread0-copy178) (at_kitchen_bread bread0-copy179) (at_kitchen_bread bread0-copy180) (at_kitchen_bread bread0-copy181) (at_kitchen_bread bread0-copy182) (at_kitchen_bread bread0-copy183) (at_kitchen_bread bread0-copy184) (at_kitchen_bread bread0-copy185) (at_kitchen_bread bread0-copy186) (at_kitchen_bread bread0-copy187) (at_kitchen_bread bread0-copy188) (at_kitchen_bread bread0-copy189) (at_kitchen_bread bread0-copy190) (at_kitchen_bread bread0-copy191) (at_kitchen_bread bread0-copy192) (at_kitchen_bread bread0-copy193) (at_kitchen_bread bread0-copy194) (at_kitchen_bread bread0-copy195) (at_kitchen_bread bread0-copy196) (at_kitchen_bread bread0-copy197)
			    (at_kitchen_bread bread1)
			    (at_kitchen_bread bread2)
			    (at_kitchen_content content-0-0)
			    (at_kitchen_content content-1-0)
			    (at_kitchen_content content-2-0) 

     ;; content descriptions
                (descr content-0-0 content-0)
                (descr content-1-0 content-1)
                (descr content-2-0 content-2)
     
     ;; which sandwichs the kids accept
     (likes child1 content-1)
     (likes child2 content-2)
     (likes child0 content-0)

     ;; where children are
     (waiting child0 table0)
     (waiting child1 table1)
     (waiting child2 table2)

     ;;sandwich dummies
     (notexist sandw0)
     (notexist sandw1)
     (notexist sandw2)
  )
  (:goal
    (and
     (served child0)
     (served child1)
     (served child2)
    )
  )
)

