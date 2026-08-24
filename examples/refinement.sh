#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

usage() {
    echo "Usage: $0"
}

if (( $# > 0 )); then
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        *)
            usage >&2
            exit 2
            ;;
    esac
fi

"$python_bin" -m scripts.planner concrete \
    --domain benchmarks/downward-benchmarks/gripper/domain.pddl \
    --problem benchmarks/downward-benchmarks/gripper/prob01.pddl \
    --horizon 11 \
    --encoding exact

"$python_bin" -m scripts.planner abstract \
    --domain benchmarks/downward-benchmarks/gripper/domain.pddl \
    --problem benchmarks/downward-benchmarks/gripper/prob01.pddl \
    --abstract-name ball_abs \
    --bliss-time-limit 300 \
    --horizon 11 \
    --encoding exact \
    --plan-source clingo
