"""Manage temporary planning workspaces."""

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory


@contextmanager
def temp_run_dir(dir_name="concrete"):
    """Yield an isolated planner directory and delete it after the run."""
    with TemporaryDirectory(prefix=f"{dir_name}-") as run_dir:
        yield run_dir, Path(run_dir).name
