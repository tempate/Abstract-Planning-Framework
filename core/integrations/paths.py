from pathlib import Path

# Project filesystem layout. Keep fixed paths here so callers do not need to
# know where bundled tools and generated artifacts live.
_ROOT = Path(__file__).resolve().parents[2]


def _project_path(*parts):
    return str(_ROOT.joinpath(*parts))


PLASP_BIN = _project_path("lib", "plasp", "bin", "plasp")
SEQUENTIAL_ENCODING = _project_path("core", "encodings", "sequential-incremental.lp")

FAST_DOWNWARD_SCRIPT = _project_path("lib", "downward", "fast-downward.py")
# Silvan Sievers' fork of Fast Downward, whose A* prunes states symmetric to ones it has seen.
STRUCTURAL_SYMMETRIES_SCRIPT = _project_path("lib", "structural-symmetries", "fast-downward.py")

PDDL_SYMMETRIES_TRANSLATOR = _project_path("lib", "pddl-symmetries", "src", "translate", "translate.py")

NUMERIC_FAST_DOWNWARD_SCRIPT = _project_path("lib", "numeric-fast-downward", "fast-downward.py")
NUMERIC_FAST_DOWNWARD_BIN = _project_path("lib", "numeric-fast-downward", "builds", "release64", "bin", "downward")

MS_UNSAT_TRANSLATOR = _project_path("lib", "ms-unsat", "src", "translate", "translate.py")
MS_UNSAT_PREPROCESSOR = _project_path("lib", "ms-unsat", "src", "preprocess", "preprocess")
MS_UNSAT_SEARCH = _project_path("lib", "ms-unsat", "src", "search", "downward-release")
