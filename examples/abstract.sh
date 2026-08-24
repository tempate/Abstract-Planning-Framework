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

"$python_bin" -m scripts.planner abstract \
    --domain lib/downward-benchmarks/gripper/domain.pddl \
    --problem lib/downward-benchmarks/gripper/prob01.pddl \
    --abstract-name ball_abs \
    --horizon 11 \
    --plan-source clingo
