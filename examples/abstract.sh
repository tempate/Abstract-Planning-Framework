#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

run_no_mystery() {
    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain data/no_mystery/abstract/domain.pddl \
        --abstract-problem data/no_mystery/abstract/p02.pddl \
        --concrete-domain data/no_mystery/concrete/domain.pddl \
        --concrete-problem data/no_mystery/concrete/p02.pddl \
        --horizon 14 \
        --encoding exact \
        --plan-source clingo
}

run_beluga() {
    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/beluga/abstract/hangar/domain.pddl \
        --abstract-problem data/beluga/abstract/hangar/problem_3_s45_j3_r2_oc44_f3_abs.pddl \
        --concrete-domain data/beluga/concrete/standard/domain.pddl \
        --concrete-problem data/beluga/concrete/standard/problem_3_s45_j3_r2_oc44_f3.pddl \
        --abstract-symbol hangarabs \
        --concrete-objects hangar1 hangar2 hangar3 \
        --horizon 17 \
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
