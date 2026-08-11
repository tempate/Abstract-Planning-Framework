#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PROJECT_DIR}/venv/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
    PYTHON_BIN="python3"
fi

EXAMPLE_DIR="${PROJECT_DIR}/data/examples/no_mystery"
CASE="${1:-all}"

print_case_header() {
    local title="$1"
    printf '\n%s\n%s\n%s\n' \
        '========================================================================' \
        "${title}" \
        '========================================================================'
}

run_concrete() {
    print_case_header "CONCRETE NOMYSTERY"
    "${PYTHON_BIN}" -m scripts.concrete_planner \
        --domain "${EXAMPLE_DIR}/concrete/domain.pddl" \
        --problem "${EXAMPLE_DIR}/concrete/problem.pddl"
}

run_abstract() {
    local mode="$1"
    local label
    if [[ "${mode}" == "inc" ]]; then
        label="INCREMENTAL ABSTRACTION"
    else
        label="DECREMENTAL ABSTRACTION"
    fi
    print_case_header "${label} — NOMYSTERY"
    "${PYTHON_BIN}" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain "${EXAMPLE_DIR}/abstract/domain.pddl" \
        --abstract-problem "${EXAMPLE_DIR}/abstract/problem.pddl" \
        --concrete-domain "${EXAMPLE_DIR}/concrete/domain.pddl" \
        --concrete-problem "${EXAMPLE_DIR}/concrete/problem.pddl" \
        --mode "${mode}" \
        --plan-source clingo
}

cd "${PROJECT_DIR}"

case "${CASE}" in
    concrete)
        run_concrete
        ;;
    inc|dec)
        run_abstract "${CASE}"
        ;;
    all)
        run_concrete
        run_abstract inc
        run_abstract dec
        ;;
    *)
        echo "Usage: $0 [concrete|inc|dec|all]" >&2
        exit 2
        ;;
esac
