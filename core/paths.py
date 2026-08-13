from pathlib import Path

# Project filesystem layout. Keep fixed paths here so callers do not need to
# know where bundled tools and generated artifacts live.
_ROOT = Path(__file__).resolve().parents[1]


def _project_path(*parts):
    return str(_ROOT.joinpath(*parts))


PLASP_BIN = _project_path("lib", "planpilot", "bin", "plasp")
EXACT_HORIZON_ENCODING = _project_path("lib", "planpilot", "encodings", "exact-sequential-horizon.lp")
BOUNDED_HORIZON_ENCODING = _project_path("lib", "planpilot", "encodings", "bounded-sequential-horizon.lp")
ABSTRACT_TIME_STEPS_ENCODING = _project_path("lib", "planpilot", "encodings", "abstract-time-steps.lp")
ACTION_PER_TIME_STEP_ENCODING = _project_path("lib", "planpilot", "encodings", "action-per-time-step.lp")
OCCURRENCE_VALIDATION_ENCODING = _project_path("encodings", "occurrence-validation.lp")

FAST_DOWNWARD_SCRIPT = _project_path("lib", "downward", "fast-downward.py")
TEMP_DIR = _project_path("scripts", "utils", "temp")
BASE_JSON_DIR = _project_path("scripts", "utils", "temp", "jsonFiles")
EXCEL_FILE = _project_path("scripts", "utils", "results_automatically.xlsx")
