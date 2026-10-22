"""The planner each mode names, without its abs- prefix."""

from core.integrations.fast_downward import LAMA, LMCUT, MS
from core.planning import asp
from core.planning.fd import FastDownward

BACKENDS = {"asp": asp, "lama": FastDownward(LAMA), "lmcut": FastDownward(LMCUT), "ms": FastDownward(MS)}
