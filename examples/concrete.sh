#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

run_no_mystery() {
    "$python_bin" -m scripts.concrete_planner \
        --domain data/no_mystery/concrete/domain.pddl \
        --problem data/no_mystery/concrete/p02.pddl \
        --horizon 14 \
        --encoding exact
}

run_beluga() {
    "$python_bin" -m scripts.concrete_planner \
        --domain data/beluga/concrete/standard/domain.pddl \
        --problem data/beluga/concrete/standard/problem_3_s45_j3_r2_oc44_f3.pddl \
        --horizon 17 \
        --encoding exact
}

usage() {
    echo "Usage: $0 [no_mystery|beluga|all]"
}

domain="${1:-beluga}"
case "$domain" in
    no_mystery)
        run_no_mystery
        ;;
    beluga)
        run_beluga
        ;;
    all)
        run_no_mystery
        run_beluga
        ;;
    -h|--help)
        usage
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac
