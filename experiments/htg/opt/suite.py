"""The hard-to-ground optimal suite, one directory of htg-domains per entry.

The same directories as the satisficing suite, with labyrinth/OPT in place of
labyrinth/SAT, since labyrinth is the only domain with separate optimal instances.
"""

from experiments.htg.sat.suite import SUITE as SATISFICING_SUITE

SUITE = ["labyrinth/OPT" if domain == "labyrinth/SAT" else domain for domain in SATISFICING_SUITE]
