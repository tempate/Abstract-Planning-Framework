(define (problem TPP)
(:domain TPP-Propositional)
(:objects
	goods1 goods1-copy1 goods1-copy2 goods1-copy3 goods2 - goods
	truck1 - truck
	market1 - market
	depot1 - depot
	level0 level1 - level)

(:init
	(next level1 level0)
	(ready-to-load goods1 market1 level0) (ready-to-load goods1-copy1 market1 level0) (ready-to-load goods1-copy2 market1 level0) (ready-to-load goods1-copy3 market1 level0)
	(ready-to-load goods2 market1 level0)
	(stored goods1 level0) (stored goods1-copy1 level0) (stored goods1-copy2 level0) (stored goods1-copy3 level0)
	(stored goods2 level0)
	(loaded goods1 truck1 level0) (loaded goods1-copy1 truck1 level0) (loaded goods1-copy2 truck1 level0) (loaded goods1-copy3 truck1 level0)
	(loaded goods2 truck1 level0)
	(connected depot1 market1)
	(connected market1 depot1)
	(on-sale goods1 market1 level1) (on-sale goods1-copy1 market1 level1) (on-sale goods1-copy2 market1 level1) (on-sale goods1-copy3 market1 level1)
	(on-sale goods2 market1 level1)
	(at truck1 depot1))

(:goal (and
	(stored goods1 level1) (stored goods1-copy1 level1) (stored goods1-copy2 level1) (stored goods1-copy3 level1)
	(stored goods2 level1)))

)
