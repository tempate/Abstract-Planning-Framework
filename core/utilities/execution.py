"""A planning run: its temporary workspace, its metrics, and the result it reports."""

import os
import shutil
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from tempfile import mkdtemp

from core.utilities.metrics import PlanningMetrics

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


@dataclass(frozen=True)
class PlanningRun:
    base_dir: str
    run_id: str
    metrics: PlanningMetrics

    def plan_result(self, config, plan):
        """What a run that searched for a plan reports, once it has ended."""
        return {
            "configuration": config.as_dict(),
            "plan": plan,
            "success": plan is not None,
            "run_id": self.run_id,
            "metrics": self.metrics.as_dict(),
        }

    def verdict_result(self, config, verdict):
        """What a run that decided solvability reports, once it has ended."""
        return {
            "configuration": config.as_dict(),
            "verdict": verdict,
            "run_id": self.run_id,
            "metrics": self.metrics.as_dict(),
        }


@contextmanager
def planning_run(label, on_update=None):
    """Measure a run as total, in a directory of its own."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir(label) as (base_dir, run_id):
            yield PlanningRun(base_dir, run_id, metrics)
