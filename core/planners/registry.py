"""The planner each mode names, without its abs- prefix."""

from core.integrations.fast_downward import BLIND_OSS, LAMA, LMCUT
from core.planners.asp import Asp
from core.planners.ms import MsUnsat
from core.planners.fd import FastDownward

PLANNERS = {
    "asp": Asp(),
    "lama": FastDownward(LAMA),
    "lmcut": FastDownward(LMCUT),
    "ms": MsUnsat(),
    "oss": FastDownward(BLIND_OSS),
}
