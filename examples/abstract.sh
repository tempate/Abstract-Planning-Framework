#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

run_no_mystery() {
    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain data/examples/no_mystery/abstract/domain.pddl \
        --abstract-problem data/examples/no_mystery/abstract/problem.pddl \
        --concrete-domain data/examples/no_mystery/concrete/domain.pddl \
        --concrete-problem data/examples/no_mystery/concrete/problem.pddl \
        --horizon 14 \
        --encoding exact \
        --plan-source clingo
}

run_beluga() {
    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/benchmarks/beluga/abstract/hangar/domain.pddl \
        --abstract-problem data/benchmarks/beluga/abstract/hangar/problem_3_s45_j3_r2_oc44_f3_abs.pddl \
        --concrete-domain data/benchmarks/beluga/concrete/standard/domain.pddl \
        --concrete-problem data/benchmarks/beluga/concrete/standard/problem_3_s45_j3_r2_oc44_f3.pddl \
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
