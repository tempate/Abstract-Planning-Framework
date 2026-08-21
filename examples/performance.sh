#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

run_no_mystery() {
    "$python_bin" -m scripts.planner concrete \
        --domain data/no_mystery/concrete/domain.pddl \
        --problem data/no_mystery/concrete/p04.pddl \
        --bliss-time-limit 300 \
        --horizon 19 \
        --encoding exact

    "$python_bin" -m scripts.planner abstract \
        --domain data/no_mystery/concrete/domain.pddl \
        --problem data/no_mystery/concrete/p04.pddl \
        --horizon 19 \
        --encoding exact \
        --plan-source clingo
}

run_beluga() {
    local problem="problem_38_s81_j5_r2_oc31_f4"

    "$python_bin" -m scripts.planner concrete \
        --domain data/beluga/concrete/standard/domain.pddl \
        --problem "data/beluga/concrete/standard/${problem}.pddl" \
        --horizon 26 \
        --encoding exact

    "$python_bin" -m scripts.planner abstract \
        --domain data/beluga/concrete/standard/domain.pddl \
        --problem "data/beluga/concrete/standard/${problem}.pddl" \
        --objects-to-abstract hangar1 hangar2 hangar3 \
        --abstract-name hangarabs \
        --horizon 26 \
        --encoding exact \
        --plan-source clingo
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
