"""The planner each mode names, without its abs- prefix, built for one run's config."""

from functools import partial

from core.integrations.fast_downward import LAMA, LMCUT
from core.planners.asp import Asp
from core.planners.fd import FastDownward

PLANNERS = {
    "asp": Asp,
    "lama": partial(FastDownward, LAMA),
    "lmcut": partial(FastDownward, LMCUT),
}
