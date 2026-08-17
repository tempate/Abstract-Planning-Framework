#!/usr/bin/env bash
set -euo pipefail

# Run from any directory while keeping all paths relative to the repository.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"
example_root="data/examples/no_mystery"
benchmark_root="data/benchmarks/nomystery"

run_concrete() {
    "$python_bin" -m scripts.concrete_planner \
        --domain "$example_root/concrete/domain.pddl" \
        --problem "$example_root/concrete/problem.pddl" \
        --horizon 14 \
        --encoding exact
}

run_abstract() {
    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain "$example_root/abstract/domain.pddl" \
        --abstract-problem "$example_root/abstract/problem.pddl" \
        --concrete-domain "$example_root/concrete/domain.pddl" \
        --concrete-problem "$example_root/concrete/problem.pddl" \
        --horizon 14 \
        --encoding exact \
        --plan-source clingo
}

run_refinement() {
    "$python_bin" -m scripts.concrete_planner \
        --domain "$benchmark_root/concrete/domain.pddl" \
        --problem "$benchmark_root/concrete/p01.pddl" \
        --horizon 11 \
        --encoding exact

    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain "$benchmark_root/abstract/domain.pddl" \
        --abstract-problem "$benchmark_root/abstract/p01.pddl" \
        --concrete-domain "$benchmark_root/concrete/domain.pddl" \
        --concrete-problem "$benchmark_root/concrete/p01.pddl" \
        --horizon 11 \
        --encoding exact \
        --plan-source clingo
}

run_performance() {
    "$python_bin" -m scripts.concrete_planner \
        --domain "$benchmark_root/concrete/domain.pddl" \
        --problem "$benchmark_root/concrete/p04.pddl" \
        --horizon 19 \
        --encoding exact

    "$python_bin" -m scripts.abstract_planner \
        --profile no_mystery \
        --abstract-domain "$benchmark_root/abstract/domain.pddl" \
        --abstract-problem "$benchmark_root/abstract/p04.pddl" \
        --concrete-domain "$benchmark_root/concrete/domain.pddl" \
        --concrete-problem "$benchmark_root/concrete/p04.pddl" \
        --horizon 19 \
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
