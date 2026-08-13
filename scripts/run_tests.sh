#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PROJECT_DIR}/venv/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
    PYTHON_BIN="python3"
fi

SUITE="${1:-unit}"
cd "${PROJECT_DIR}"

case "${SUITE}" in
    unit)
        "${PYTHON_BIN}" -m unittest discover -s tests -p 'test_*.py' -v
        ;;
    integration)
        RUN_PLANNER_INTEGRATION=1 \
            "${PYTHON_BIN}" -m unittest tests.test_planning_integration -v
        ;;
    all)
        RUN_PLANNER_INTEGRATION=1 \
            "${PYTHON_BIN}" -m unittest discover -s tests -p 'test_*.py' -v
        ;;
    *)
        echo "Usage: $0 [unit|integration|all]" >&2
        exit 2
        ;;
esac
