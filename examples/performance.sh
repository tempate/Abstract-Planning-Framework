#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"

run_no_mystery() {
    "$python_bin" -m scripts.concrete_planner \
        --domain data/benchmarks/nomystery/concrete/domain.pddl \
        --problem data/benchmarks/nomystery/concrete/p04.pddl \
        --horizon 19 \
        --encoding exact

    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain data/benchmarks/nomystery/abstract/domain.pddl \
        --abstract-problem data/benchmarks/nomystery/abstract/p04.pddl \
        --concrete-domain data/benchmarks/nomystery/concrete/domain.pddl \
        --concrete-problem data/benchmarks/nomystery/concrete/p04.pddl \
        --horizon 19 \
        --encoding exact \
        --plan-source clingo
}

run_beluga() {
    local problem="problem_38_s81_j5_r2_oc31_f4"

    "$python_bin" -m scripts.concrete_planner \
        --domain data/benchmarks/beluga/concrete/standard/domain.pddl \
        --problem "data/benchmarks/beluga/concrete/standard/${problem}.pddl" \
        --horizon 26 \
        --encoding exact

    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/benchmarks/beluga/abstract/hangar/domain.pddl \
        --abstract-problem "data/benchmarks/beluga/abstract/hangar/${problem}_abs.pddl" \
        --concrete-domain data/benchmarks/beluga/concrete/standard/domain.pddl \
        --concrete-problem "data/benchmarks/beluga/concrete/standard/${problem}.pddl" \
        --abstract-symbol hangarabs \
        --concrete-objects hangar1 hangar2 hangar3 \
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
