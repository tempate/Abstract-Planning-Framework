"""The planner each mode names, without its abs- prefix, built for one run's config."""

from functools import partial

from core.integrations.fast_downward import LAMA, LAMA_SYMMETRY_PRUNING, LMCUT, LMCUT_SYMMETRY_PRUNING
from core.planners.asp import Asp
from core.planners.fd import FastDownward
from core.planners.homomorphism import Homomorphism
from core.planners.powerlifted import Powerlifted
from core.planners.symmetry_pruning import SymmetryPruning

PLANNERS = {
    "asp": Asp,
    "lama": partial(FastDownward, LAMA),
    "lama-symmetry-pruning": partial(SymmetryPruning, LAMA_SYMMETRY_PRUNING),
    "lmcut": partial(FastDownward, LMCUT),
    "powerlifted": Powerlifted,
    "lmcut-symmetry-pruning": partial(SymmetryPruning, LMCUT_SYMMETRY_PRUNING),
    "rnd-g": Homomorphism,
}
# The concrete modes that take the class an abstract mode would collapse.
CLASS_MODES = ("lama-symmetry-pruning", "lmcut-symmetry-pruning")
