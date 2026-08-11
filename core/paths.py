from pathlib import Path

# Project filesystem layout. Keep fixed paths here so callers do not need to
# know where bundled tools and generated artifacts live.
_REPO_ROOT_PATH = Path(__file__).resolve().parents[1]
REPO_ROOT = str(_REPO_ROOT_PATH)
LIB_DIR = str(_REPO_ROOT_PATH / "lib")

CLINGO_BIN = str(_REPO_ROOT_PATH / "lib" / "clingo" / "build" / "bin" / "clingo")

PLANPILOT_DIR = str(_REPO_ROOT_PATH / "lib" / "planpilot")
PLASP_BIN = str(_REPO_ROOT_PATH / "lib" / "planpilot" / "bin" / "plasp")
PLANPILOT_ENCODINGS_DIR = str(_REPO_ROOT_PATH / "lib" / "planpilot" / "encodings")
EXACT_HORIZON_ENCODING = str(Path(PLANPILOT_ENCODINGS_DIR) / "exact-sequential-horizon.lp")
BOUNDED_HORIZON_ENCODING = str(Path(PLANPILOT_ENCODINGS_DIR) / "bounded-sequential-horizon.lp")
ABSTRACT_TIME_STEPS_ENCODING = str(Path(PLANPILOT_ENCODINGS_DIR) / "abstract-time-steps.lp")
ACTION_PER_TIME_STEP_ENCODING = str(Path(PLANPILOT_ENCODINGS_DIR) / "action-per-time-step.lp")

FAST_DOWNWARD_SCRIPT = str(_REPO_ROOT_PATH / "lib" / "downward" / "fast-downward.py")

SCRIPTS_UTILS_DIR = str(_REPO_ROOT_PATH / "scripts" / "utils")
TEMP_DIR = str(Path(SCRIPTS_UTILS_DIR) / "temp")
BASE_JSON_DIR = str(Path(TEMP_DIR) / "jsonFiles")
EXCEL_FILE = str(Path(SCRIPTS_UTILS_DIR) / "results_automatically.xlsx")
