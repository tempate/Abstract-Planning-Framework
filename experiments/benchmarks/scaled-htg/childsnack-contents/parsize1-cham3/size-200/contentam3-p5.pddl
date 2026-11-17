
(define (problem example-problem)
  (:domain htg-child-snack)
  (:objects
    child0 child1 child2 - child
    bread0 bread1 bread2 - bread-portion
    content-0 content-1 content-2 - content-description
    content-0-0 content-0-1 content-0-2 content-0-3 content-0-4 content-0-5 content-0-6 - content-portion
    content-1-0 content-1-1 content-1-2 content-1-3 content-1-4 content-1-5 - content-portion
    content-2-0 content-2-1 content-2-2 content-2-3 content-2-4 - content-portion
    tray0 tray0-copy1 tray0-copy2 tray0-copy3 tray0-copy4 tray0-copy5 tray0-copy6 tray0-copy7 tray0-copy8 tray0-copy9 tray0-copy10 tray0-copy11 tray0-copy12 tray0-copy13 tray0-copy14 tray0-copy15 tray0-copy16 tray0-copy17 tray0-copy18 tray0-copy19 tray0-copy20 tray0-copy21 tray0-copy22 tray0-copy23 tray0-copy24 tray0-copy25 tray0-copy26 tray0-copy27 tray0-copy28 tray0-copy29 tray0-copy30 tray0-copy31 tray0-copy32 tray0-copy33 tray0-copy34 tray0-copy35 tray0-copy36 tray0-copy37 tray0-copy38 tray0-copy39 tray0-copy40 tray0-copy41 tray0-copy42 tray0-copy43 tray0-copy44 tray0-copy45 tray0-copy46 tray0-copy47 tray0-copy48 tray0-copy49 tray0-copy50 tray0-copy51 tray0-copy52 tray0-copy53 tray0-copy54 tray0-copy55 tray0-copy56 tray0-copy57 tray0-copy58 tray0-copy59 tray0-copy60 tray0-copy61 tray0-copy62 tray0-copy63 tray0-copy64 tray0-copy65 tray0-copy66 tray0-copy67 tray0-copy68 tray0-copy69 tray0-copy70 tray0-copy71 tray0-copy72 tray0-copy73 tray0-copy74 tray0-copy75 tray0-copy76 tray0-copy77 tray0-copy78 tray0-copy79 tray0-copy80 tray0-copy81 tray0-copy82 tray0-copy83 tray0-copy84 tray0-copy85 tray0-copy86 tray0-copy87 tray0-copy88 tray0-copy89 tray0-copy90 tray0-copy91 tray0-copy92 tray0-copy93 tray0-copy94 tray0-copy95 tray0-copy96 tray0-copy97 tray0-copy98 tray0-copy99 tray0-copy100 tray0-copy101 tray0-copy102 tray0-copy103 tray0-copy104 tray0-copy105 tray0-copy106 tray0-copy107 tray0-copy108 tray0-copy109 tray0-copy110 tray0-copy111 tray0-copy112 tray0-copy113 tray0-copy114 tray0-copy115 tray0-copy116 tray0-copy117 tray0-copy118 tray0-copy119 tray0-copy120 tray0-copy121 tray0-copy122 tray0-copy123 tray0-copy124 tray0-copy125 tray0-copy126 tray0-copy127 tray0-copy128 tray0-copy129 tray0-copy130 tray0-copy131 tray0-copy132 tray0-copy133 tray0-copy134 tray0-copy135 tray0-copy136 tray0-copy137 tray0-copy138 tray0-copy139 tray0-copy140 tray0-copy141 tray0-copy142 tray0-copy143 tray0-copy144 tray0-copy145 tray0-copy146 tray0-copy147 tray0-copy148 tray0-copy149 tray0-copy150 tray0-copy151 tray0-copy152 tray0-copy153 tray0-copy154 tray0-copy155 tray0-copy156 tray0-copy157 tray0-copy158 tray0-copy159 tray0-copy160 tray0-copy161 tray0-copy162 tray0-copy163 tray0-copy164 tray0-copy165 tray0-copy166 tray0-copy167 tray0-copy168 tray0-copy169 tray0-copy170 tray0-copy171 tray0-copy172 tray0-copy173 tray0-copy174 tray0-copy175 tray0-copy176 tray0-copy177 tray0-copy178 tray0-copy179 tray0-copy180 tray0-copy181 tray0-copy182 tray0-copy183 tray0-copy184 tray0-copy185 tray0-copy186 tray0-copy187 tray0-copy188 tray0-copy189 tray0-copy190 tray0-copy191 tray0-copy192 tray0-copy193 tray0-copy194 tray0-copy195 tray0-copy196 tray0-copy197 tray1 tray2 - tray
    table0 table1 table2 table3 table4 - place
    sandw0 sandw1 sandw2 - sandwich
  )
  (:init
     ;; everythin starts in the kitchen
     (at tray0 kitchen) (at tray0-copy1 kitchen) (at tray0-copy2 kitchen) (at tray0-copy3 kitchen) (at tray0-copy4 kitchen) (at tray0-copy5 kitchen) (at tray0-copy6 kitchen) (at tray0-copy7 kitchen) (at tray0-copy8 kitchen) (at tray0-copy9 kitchen) (at tray0-copy10 kitchen) (at tray0-copy11 kitchen) (at tray0-copy12 kitchen) (at tray0-copy13 kitchen) (at tray0-copy14 kitchen) (at tray0-copy15 kitchen) (at tray0-copy16 kitchen) (at tray0-copy17 kitchen) (at tray0-copy18 kitchen) (at tray0-copy19 kitchen) (at tray0-copy20 kitchen) (at tray0-copy21 kitchen) (at tray0-copy22 kitchen) (at tray0-copy23 kitchen) (at tray0-copy24 kitchen) (at tray0-copy25 kitchen) (at tray0-copy26 kitchen) (at tray0-copy27 kitchen) (at tray0-copy28 kitchen) (at tray0-copy29 kitchen) (at tray0-copy30 kitchen) (at tray0-copy31 kitchen) (at tray0-copy32 kitchen) (at tray0-copy33 kitchen) (at tray0-copy34 kitchen) (at tray0-copy35 kitchen) (at tray0-copy36 kitchen) (at tray0-copy37 kitchen) (at tray0-copy38 kitchen) (at tray0-copy39 kitchen) (at tray0-copy40 kitchen) (at tray0-copy41 kitchen) (at tray0-copy42 kitchen) (at tray0-copy43 kitchen) (at tray0-copy44 kitchen) (at tray0-copy45 kitchen) (at tray0-copy46 kitchen) (at tray0-copy47 kitchen) (at tray0-copy48 kitchen) (at tray0-copy49 kitchen) (at tray0-copy50 kitchen) (at tray0-copy51 kitchen) (at tray0-copy52 kitchen) (at tray0-copy53 kitchen) (at tray0-copy54 kitchen) (at tray0-copy55 kitchen) (at tray0-copy56 kitchen) (at tray0-copy57 kitchen) (at tray0-copy58 kitchen) (at tray0-copy59 kitchen) (at tray0-copy60 kitchen) (at tray0-copy61 kitchen) (at tray0-copy62 kitchen) (at tray0-copy63 kitchen) (at tray0-copy64 kitchen) (at tray0-copy65 kitchen) (at tray0-copy66 kitchen) (at tray0-copy67 kitchen) (at tray0-copy68 kitchen) (at tray0-copy69 kitchen) (at tray0-copy70 kitchen) (at tray0-copy71 kitchen) (at tray0-copy72 kitchen) (at tray0-copy73 kitchen) (at tray0-copy74 kitchen) (at tray0-copy75 kitchen) (at tray0-copy76 kitchen) (at tray0-copy77 kitchen) (at tray0-copy78 kitchen) (at tray0-copy79 kitchen) (at tray0-copy80 kitchen) (at tray0-copy81 kitchen) (at tray0-copy82 kitchen) (at tray0-copy83 kitchen) (at tray0-copy84 kitchen) (at tray0-copy85 kitchen) (at tray0-copy86 kitchen) (at tray0-copy87 kitchen) (at tray0-copy88 kitchen) (at tray0-copy89 kitchen) (at tray0-copy90 kitchen) (at tray0-copy91 kitchen) (at tray0-copy92 kitchen) (at tray0-copy93 kitchen) (at tray0-copy94 kitchen) (at tray0-copy95 kitchen) (at tray0-copy96 kitchen) (at tray0-copy97 kitchen) (at tray0-copy98 kitchen) (at tray0-copy99 kitchen) (at tray0-copy100 kitchen) (at tray0-copy101 kitchen) (at tray0-copy102 kitchen) (at tray0-copy103 kitchen) (at tray0-copy104 kitchen) (at tray0-copy105 kitchen) (at tray0-copy106 kitchen) (at tray0-copy107 kitchen) (at tray0-copy108 kitchen) (at tray0-copy109 kitchen) (at tray0-copy110 kitchen) (at tray0-copy111 kitchen) (at tray0-copy112 kitchen) (at tray0-copy113 kitchen) (at tray0-copy114 kitchen) (at tray0-copy115 kitchen) (at tray0-copy116 kitchen) (at tray0-copy117 kitchen) (at tray0-copy118 kitchen) (at tray0-copy119 kitchen) (at tray0-copy120 kitchen) (at tray0-copy121 kitchen) (at tray0-copy122 kitchen) (at tray0-copy123 kitchen) (at tray0-copy124 kitchen) (at tray0-copy125 kitchen) (at tray0-copy126 kitchen) (at tray0-copy127 kitchen) (at tray0-copy128 kitchen) (at tray0-copy129 kitchen) (at tray0-copy130 kitchen) (at tray0-copy131 kitchen) (at tray0-copy132 kitchen) (at tray0-copy133 kitchen) (at tray0-copy134 kitchen) (at tray0-copy135 kitchen) (at tray0-copy136 kitchen) (at tray0-copy137 kitchen) (at tray0-copy138 kitchen) (at tray0-copy139 kitchen) (at tray0-copy140 kitchen) (at tray0-copy141 kitchen) (at tray0-copy142 kitchen) (at tray0-copy143 kitchen) (at tray0-copy144 kitchen) (at tray0-copy145 kitchen) (at tray0-copy146 kitchen) (at tray0-copy147 kitchen) (at tray0-copy148 kitchen) (at tray0-copy149 kitchen) (at tray0-copy150 kitchen) (at tray0-copy151 kitchen) (at tray0-copy152 kitchen) (at tray0-copy153 kitchen) (at tray0-copy154 kitchen) (at tray0-copy155 kitchen) (at tray0-copy156 kitchen) (at tray0-copy157 kitchen) (at tray0-copy158 kitchen) (at tray0-copy159 kitchen) (at tray0-copy160 kitchen) (at tray0-copy161 kitchen) (at tray0-copy162 kitchen) (at tray0-copy163 kitchen) (at tray0-copy164 kitchen) (at tray0-copy165 kitchen) (at tray0-copy166 kitchen) (at tray0-copy167 kitchen) (at tray0-copy168 kitchen) (at tray0-copy169 kitchen) (at tray0-copy170 kitchen) (at tray0-copy171 kitchen) (at tray0-copy172 kitchen) (at tray0-copy173 kitchen) (at tray0-copy174 kitchen) (at tray0-copy175 kitchen) (at tray0-copy176 kitchen) (at tray0-copy177 kitchen) (at tray0-copy178 kitchen) (at tray0-copy179 kitchen) (at tray0-copy180 kitchen) (at tray0-copy181 kitchen) (at tray0-copy182 kitchen) (at tray0-copy183 kitchen) (at tray0-copy184 kitchen) (at tray0-copy185 kitchen) (at tray0-copy186 kitchen) (at tray0-copy187 kitchen) (at tray0-copy188 kitchen) (at tray0-copy189 kitchen) (at tray0-copy190 kitchen) (at tray0-copy191 kitchen) (at tray0-copy192 kitchen) (at tray0-copy193 kitchen) (at tray0-copy194 kitchen) (at tray0-copy195 kitchen) (at tray0-copy196 kitchen) (at tray0-copy197 kitchen)
     (at tray1 kitchen)
     (at tray2 kitchen)
			    (at_kitchen_bread bread0)
			    (at_kitchen_bread bread1)
			    (at_kitchen_bread bread2)
			    (at_kitchen_content content-0-0)
			    (at_kitchen_content content-0-1)
			    (at_kitchen_content content-0-2)
			    (at_kitchen_content content-0-3)
			    (at_kitchen_content content-0-4)
			    (at_kitchen_content content-0-5)
			    (at_kitchen_content content-0-6)
			    (at_kitchen_content content-1-0)
			    (at_kitchen_content content-1-1)
			    (at_kitchen_content content-1-2)
			    (at_kitchen_content content-1-3)
			    (at_kitchen_content content-1-4)
			    (at_kitchen_content content-1-5)
			    (at_kitchen_content content-2-0)
			    (at_kitchen_content content-2-1)
			    (at_kitchen_content content-2-2)
			    (at_kitchen_content content-2-3)
			    (at_kitchen_content content-2-4) 

     ;; content descriptions
                (descr content-0-0 content-0)
                (descr content-0-1 content-0)
                (descr content-0-2 content-0)
                (descr content-0-3 content-0)
                (descr content-0-4 content-0)
                (descr content-0-5 content-0)
                (descr content-0-6 content-0)
                (descr content-1-0 content-1)
                (descr content-1-1 content-1)
                (descr content-1-2 content-1)
                (descr content-1-3 content-1)
                (descr content-1-4 content-1)
                (descr content-1-5 content-1)
                (descr content-2-0 content-2)
                (descr content-2-1 content-2)
                (descr content-2-2 content-2)
                (descr content-2-3 content-2)
                (descr content-2-4 content-2)
     
     ;; which sandwichs the kids accept
     (likes child2 content-1)
     (likes child1 content-0)
     (likes child1 content-2)
     (likes child0 content-0)
     (likes child0 content-2)
     (likes child2 content-2)
     (likes child2 content-0)
     (likes child1 content-1)
     (likes child0 content-1)

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

