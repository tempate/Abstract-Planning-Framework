"""The planner each mode names, without its abs- prefix."""

from core.integrations.fast_downward import LAMA, LMCUT
from core.planning import asp, ms
from core.planning.fd import FastDownward

BACKENDS = {"asp": asp, "lama": FastDownward(LAMA), "lmcut": FastDownward(LMCUT), "ms": ms}
