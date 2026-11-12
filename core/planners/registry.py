"""The planner each mode names, without its abs- prefix."""

from core.integrations.fast_downward import BLIND_OSS, LAMA, LMCUT
from core.planners import asp, ms
from core.planners.fd import FastDownward

PLANNERS = {
    "asp": asp,
    "lama": FastDownward(LAMA),
    "lmcut": FastDownward(LMCUT),
    "ms": ms,
    "oss": FastDownward(BLIND_OSS),
}
