"""Manage temporary planning workspaces."""

import os
import shutil
from contextlib import contextmanager
from pathlib import Path
from tempfile import mkdtemp

KEEP_FAILED_RUNS = "APF_KEEP_FAILED_RUNS"


@contextmanager
def temp_run_dir(dir_name="concrete"):
    """Yield an isolated planner directory and delete it after the run."""
    run_dir = mkdtemp(prefix=f"{dir_name}-")
    keep = False
    try:
        yield run_dir, Path(run_dir).name
    except BaseException:
        # The generated PDDL, SAS and ASP are what explain a failure, and they
        # are gone by the time the error reaches a terminal. Off by default, or
        # a cluster run's failures would fill the temporary filesystem.
        keep = bool(os.environ.get(KEEP_FAILED_RUNS))
        if keep:
            print(f"Kept the files of the failed run in {run_dir}", flush=True)
        raise
    finally:
        if not keep:
            shutil.rmtree(run_dir, ignore_errors=True)
