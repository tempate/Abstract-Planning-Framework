#!/usr/bin/env bash
set -euo pipefail

# Run from any directory while keeping all paths relative to the repository.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"
problem="problem_3_s45_j3_r2_oc44_f3"
concrete_domain="data/benchmarks/beluga/concrete/standard/domain.pddl"
concrete_problem="data/benchmarks/beluga/concrete/standard/${problem}.pddl"

run_concrete() {
    "$python_bin" -m scripts.concrete_planner \
        --domain "$concrete_domain" \
        --problem "$concrete_problem" \
        --horizon 17 \
        --encoding exact
}

run_abstract() {
    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/benchmarks/beluga/abstract/hangar/domain.pddl \
        --abstract-problem "data/benchmarks/beluga/abstract/hangar/${problem}_abs.pddl" \
        --concrete-domain "$concrete_domain" \
        --concrete-problem "$concrete_problem" \
        --abstract-symbol hangarabs \
        --concrete-objects hangar1 hangar2 hangar3 \
        --horizon 17 \
        --encoding exact \
        --plan-source clingo
}

run_refinement() {
    run_concrete
    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/benchmarks/beluga/abstract/trailer/domain.pddl \
        --abstract-problem "data/benchmarks/beluga/abstract/trailer/${problem}_abs.pddl" \
        --concrete-domain "$concrete_domain" \
        --concrete-problem "$concrete_problem" \
        --abstract-symbol beluga_abs_trailer \
        --concrete-objects beluga_trailer_1 beluga_trailer_2 \
        --horizon 17 \
        --encoding exact \
        --plan-source clingo
}

run_performance() {
    local performance_problem="problem_38_s81_j5_r2_oc31_f4"

    "$python_bin" -m scripts.concrete_planner \
        --domain "$concrete_domain" \
        --problem "data/benchmarks/beluga/concrete/standard/${performance_problem}.pddl" \
        --horizon 26 \
        --encoding exact

    "$python_bin" -m scripts.abstract_planner \
        --profile beluga \
        --abstract-domain data/benchmarks/beluga/abstract/hangar/domain.pddl \
        --abstract-problem "data/benchmarks/beluga/abstract/hangar/${performance_problem}_abs.pddl" \
        --concrete-domain "$concrete_domain" \
        --concrete-problem "data/benchmarks/beluga/concrete/standard/${performance_problem}.pddl" \
        --abstract-symbol hangarabs \
        --concrete-objects hangar1 hangar2 hangar3 \
        --horizon 26 \
        --encoding exact \
        --plan-source clingo
}

usage() {
    echo "Usage: $0 [concrete|abstract|refinement|performance|quick|all]"
}

workflow="${1:-quick}"
case "$workflow" in
    concrete)
        run_concrete
        ;;
    abstract)
        run_abstract
        ;;
    refinement)
        run_refinement
        ;;
    performance)
        run_performance
        ;;
    quick)
        run_concrete
        run_abstract
        run_refinement
        ;;
    all)
        run_concrete
        run_abstract
        run_refinement
        run_performance
        ;;
    -h|--help)
        usage
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac
