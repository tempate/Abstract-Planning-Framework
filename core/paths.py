from pathlib import Path

# Project filesystem layout. Keep fixed paths here so callers do not need to
# know where bundled tools and generated artifacts live.
_ROOT = Path(__file__).resolve().parents[1]


def _project_path(*parts):
    return str(_ROOT.joinpath(*parts))


PLASP_BIN = _project_path("lib", "plasp", "bin", "plasp")
EXACT_HORIZON_ENCODING = _project_path("encodings", "exact-sequential-incremental.lp")
ABSTRACT_TIME_STEPS_ENCODING = _project_path("encodings", "abstract-time-steps-incremental.lp")
ACTION_PER_TIME_STEP_ENCODING = _project_path("encodings", "action-per-time-step.lp")

FAST_DOWNWARD_SCRIPT = _project_path("lib", "downward", "fast-downward.py")

PDDL_SYMMETRIES_TRANSLATOR = _project_path("lib", "pddl-symmetries", "src", "translate", "translate.py")
