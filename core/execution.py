"""Manage planning workspaces and logging."""

import logging
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

LOGGER_NAME = "planner"


def get_logger():
    """Return the logger shared by the planning pipeline."""
    return logging.getLogger(LOGGER_NAME)


@contextmanager
def temp_run_dir(dir_name="concrete"):
    """Yield an isolated planner directory and delete it after the run."""
    with TemporaryDirectory(prefix=f"{dir_name}-") as run_dir:
        yield run_dir, Path(run_dir).name
