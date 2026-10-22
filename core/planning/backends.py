"""The module that plans with each planner a mode can name."""

from core.planning import asp, fd

BACKENDS = {"asp": asp, "lama": fd, "lmcut": fd}
