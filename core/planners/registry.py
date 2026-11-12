"""The planner each mode names, without its abs- prefix, built for one run's config."""

from functools import partial

from core.integrations.fast_downward import BLIND_OSS, LAMA, LMCUT
from core.planners.asp import Asp
from core.planners.fd import FastDownward
from core.planners.ms import MsUnsat

PLANNERS = {
    "asp": Asp,
    "lama": partial(FastDownward, LAMA),
    "lmcut": partial(FastDownward, LMCUT),
    "ms": MsUnsat,
    "oss": partial(FastDownward, BLIND_OSS),
}
