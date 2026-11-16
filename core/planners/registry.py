"""The planner each mode names, without its abs- prefix, built for one run's config."""

from functools import partial

from core.integrations.fast_downward import LAMA, LAMA_SYMMETRY_PRUNING, LMCUT, LMCUT_SYMMETRY_PRUNING
from core.planners.asp import Asp
from core.planners.fd import FastDownward
from core.planners.powerlifted import Powerlifted

PLANNERS = {
    "asp": Asp,
    "lama": partial(FastDownward, LAMA),
    "lama-symmetry-pruning": partial(FastDownward, LAMA_SYMMETRY_PRUNING),
    "lmcut": partial(FastDownward, LMCUT),
    "powerlifted": Powerlifted,
    "lmcut-symmetry-pruning": partial(FastDownward, LMCUT_SYMMETRY_PRUNING),
}
