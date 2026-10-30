(define (problem unsolv-problem-6)
(:domain document)
(:objects
	fuel1 - document
	fuel2 - document
	document1 document1-copy1 document1-copy2 document1-copy3 document1-copy4 document1-copy5 document1-copy6 document1-copy7 document1-copy8 document1-copy9 document1-copy10 document1-copy11 document1-copy12 document1-copy13 document1-copy14 document1-copy15 document1-copy16 document1-copy17 document1-copy18 document1-copy19 document1-copy20 document1-copy21 document1-copy22 document1-copy23 document1-copy24 document1-copy25 document1-copy26 document1-copy27 document1-copy28 document1-copy29 document1-copy30 document1-copy31 document1-copy32 document1-copy33 document1-copy34 document1-copy35 document1-copy36 document1-copy37 document1-copy38 document1-copy39 document1-copy40 document1-copy41 document1-copy42 document1-copy43 document1-copy44 document1-copy45 document1-copy46 document1-copy47 document1-copy48 document1-copy49 document1-copy50 document1-copy51 document1-copy52 document1-copy53 document1-copy54 document1-copy55 document1-copy56 document1-copy57 document1-copy58 document1-copy59 document1-copy60 document1-copy61 document1-copy62 document1-copy63 document1-copy64 document1-copy65 document1-copy66 document1-copy67 document1-copy68 document1-copy69 document1-copy70 document1-copy71 document1-copy72 document1-copy73 document1-copy74 document1-copy75 document1-copy76 document1-copy77 document1-copy78 document1-copy79 document1-copy80 document1-copy81 document1-copy82 document1-copy83 document1-copy84 document1-copy85 document1-copy86 document1-copy87 document1-copy88 document1-copy89 document1-copy90 document1-copy91 document1-copy92 document1-copy93 document1-copy94 document1-copy95 document1-copy96 document1-copy97 document1-copy98 document1-copy99 document1-copy100 document1-copy101 document1-copy102 document1-copy103 document1-copy104 document1-copy105 document1-copy106 document1-copy107 document1-copy108 document1-copy109 document1-copy110 document1-copy111 document1-copy112 document1-copy113 document1-copy114 document1-copy115 document1-copy116 document1-copy117 document1-copy118 document1-copy119 document1-copy120 document1-copy121 document1-copy122 document1-copy123 document1-copy124 document1-copy125 document1-copy126 document1-copy127 document1-copy128 document1-copy129 document1-copy130 document1-copy131 document1-copy132 document1-copy133 document1-copy134 document1-copy135 document1-copy136 document1-copy137 document1-copy138 document1-copy139 document1-copy140 document1-copy141 document1-copy142 document1-copy143 document1-copy144 document1-copy145 document1-copy146 document1-copy147 document1-copy148 document1-copy149 document1-copy150 document1-copy151 document1-copy152 document1-copy153 document1-copy154 document1-copy155 document1-copy156 document1-copy157 document1-copy158 document1-copy159 document1-copy160 document1-copy161 document1-copy162 document1-copy163 document1-copy164 document1-copy165 document1-copy166 document1-copy167 document1-copy168 document1-copy169 document1-copy170 document1-copy171 document1-copy172 document1-copy173 document1-copy174 document1-copy175 document1-copy176 document1-copy177 document1-copy178 document1-copy179 document1-copy180 document1-copy181 document1-copy182 document1-copy183 document1-copy184 document1-copy185 document1-copy186 document1-copy187 document1-copy188 document1-copy189 document1-copy190 document1-copy191 document1-copy192 document1-copy193 document1-copy194 document1-copy195 document1-copy196 document1-copy197 - document
	document2 - document
	document3 - document
	document4 - document
	document5 - document
	document6 - document
	document7 - document
	document8 - document
	document9 - document
	document10 - document
	office1 - location
	office2 - location
	office3 - location
	office4 - location
	office5 - location
	office6 - location
	office7 - location
	depot - location
)
(:init
	(train-at office1)
	(in-train fuel1)
	(in-train fuel2)
	(at document1 office4) (at document1-copy1 office4) (at document1-copy2 office4) (at document1-copy3 office4) (at document1-copy4 office4) (at document1-copy5 office4) (at document1-copy6 office4) (at document1-copy7 office4) (at document1-copy8 office4) (at document1-copy9 office4) (at document1-copy10 office4) (at document1-copy11 office4) (at document1-copy12 office4) (at document1-copy13 office4) (at document1-copy14 office4) (at document1-copy15 office4) (at document1-copy16 office4) (at document1-copy17 office4) (at document1-copy18 office4) (at document1-copy19 office4) (at document1-copy20 office4) (at document1-copy21 office4) (at document1-copy22 office4) (at document1-copy23 office4) (at document1-copy24 office4) (at document1-copy25 office4) (at document1-copy26 office4) (at document1-copy27 office4) (at document1-copy28 office4) (at document1-copy29 office4) (at document1-copy30 office4) (at document1-copy31 office4) (at document1-copy32 office4) (at document1-copy33 office4) (at document1-copy34 office4) (at document1-copy35 office4) (at document1-copy36 office4) (at document1-copy37 office4) (at document1-copy38 office4) (at document1-copy39 office4) (at document1-copy40 office4) (at document1-copy41 office4) (at document1-copy42 office4) (at document1-copy43 office4) (at document1-copy44 office4) (at document1-copy45 office4) (at document1-copy46 office4) (at document1-copy47 office4) (at document1-copy48 office4) (at document1-copy49 office4) (at document1-copy50 office4) (at document1-copy51 office4) (at document1-copy52 office4) (at document1-copy53 office4) (at document1-copy54 office4) (at document1-copy55 office4) (at document1-copy56 office4) (at document1-copy57 office4) (at document1-copy58 office4) (at document1-copy59 office4) (at document1-copy60 office4) (at document1-copy61 office4) (at document1-copy62 office4) (at document1-copy63 office4) (at document1-copy64 office4) (at document1-copy65 office4) (at document1-copy66 office4) (at document1-copy67 office4) (at document1-copy68 office4) (at document1-copy69 office4) (at document1-copy70 office4) (at document1-copy71 office4) (at document1-copy72 office4) (at document1-copy73 office4) (at document1-copy74 office4) (at document1-copy75 office4) (at document1-copy76 office4) (at document1-copy77 office4) (at document1-copy78 office4) (at document1-copy79 office4) (at document1-copy80 office4) (at document1-copy81 office4) (at document1-copy82 office4) (at document1-copy83 office4) (at document1-copy84 office4) (at document1-copy85 office4) (at document1-copy86 office4) (at document1-copy87 office4) (at document1-copy88 office4) (at document1-copy89 office4) (at document1-copy90 office4) (at document1-copy91 office4) (at document1-copy92 office4) (at document1-copy93 office4) (at document1-copy94 office4) (at document1-copy95 office4) (at document1-copy96 office4) (at document1-copy97 office4) (at document1-copy98 office4) (at document1-copy99 office4) (at document1-copy100 office4) (at document1-copy101 office4) (at document1-copy102 office4) (at document1-copy103 office4) (at document1-copy104 office4) (at document1-copy105 office4) (at document1-copy106 office4) (at document1-copy107 office4) (at document1-copy108 office4) (at document1-copy109 office4) (at document1-copy110 office4) (at document1-copy111 office4) (at document1-copy112 office4) (at document1-copy113 office4) (at document1-copy114 office4) (at document1-copy115 office4) (at document1-copy116 office4) (at document1-copy117 office4) (at document1-copy118 office4) (at document1-copy119 office4) (at document1-copy120 office4) (at document1-copy121 office4) (at document1-copy122 office4) (at document1-copy123 office4) (at document1-copy124 office4) (at document1-copy125 office4) (at document1-copy126 office4) (at document1-copy127 office4) (at document1-copy128 office4) (at document1-copy129 office4) (at document1-copy130 office4) (at document1-copy131 office4) (at document1-copy132 office4) (at document1-copy133 office4) (at document1-copy134 office4) (at document1-copy135 office4) (at document1-copy136 office4) (at document1-copy137 office4) (at document1-copy138 office4) (at document1-copy139 office4) (at document1-copy140 office4) (at document1-copy141 office4) (at document1-copy142 office4) (at document1-copy143 office4) (at document1-copy144 office4) (at document1-copy145 office4) (at document1-copy146 office4) (at document1-copy147 office4) (at document1-copy148 office4) (at document1-copy149 office4) (at document1-copy150 office4) (at document1-copy151 office4) (at document1-copy152 office4) (at document1-copy153 office4) (at document1-copy154 office4) (at document1-copy155 office4) (at document1-copy156 office4) (at document1-copy157 office4) (at document1-copy158 office4) (at document1-copy159 office4) (at document1-copy160 office4) (at document1-copy161 office4) (at document1-copy162 office4) (at document1-copy163 office4) (at document1-copy164 office4) (at document1-copy165 office4) (at document1-copy166 office4) (at document1-copy167 office4) (at document1-copy168 office4) (at document1-copy169 office4) (at document1-copy170 office4) (at document1-copy171 office4) (at document1-copy172 office4) (at document1-copy173 office4) (at document1-copy174 office4) (at document1-copy175 office4) (at document1-copy176 office4) (at document1-copy177 office4) (at document1-copy178 office4) (at document1-copy179 office4) (at document1-copy180 office4) (at document1-copy181 office4) (at document1-copy182 office4) (at document1-copy183 office4) (at document1-copy184 office4) (at document1-copy185 office4) (at document1-copy186 office4) (at document1-copy187 office4) (at document1-copy188 office4) (at document1-copy189 office4) (at document1-copy190 office4) (at document1-copy191 office4) (at document1-copy192 office4) (at document1-copy193 office4) (at document1-copy194 office4) (at document1-copy195 office4) (at document1-copy196 office4) (at document1-copy197 office4)
	(at document2 office4)
	(at document3 office4)
	(at document4 office4)
	(at document5 office4)
	(at document6 office5)
	(at document7 office5)
	(at document8 office5)
	(at document9 office6)
	(at document10 office2)
	(track office1 depot)
	(track office1 office2)
	(track office2 office3)
	(track office4 office1)
	(track office4 office5)
	(track office5 office1)
	(track office5 office6)
	(track office6 office4)
	(track office6 office7)
	(track office7 office1)
	(track office7 office2)
	(track office7 depot)
	(track depot office4)
)
(:goal (and
	(at document4 depot)
	(at document5 depot)
	(at document6 depot)
	(at document10 depot)
)))
