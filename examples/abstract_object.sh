#!/usr/bin/env bash
set -euo pipefail

# Run from any directory while keeping all paths relative to the repository.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python}"
output_root="${APF_TEMP_DIR:-scripts/utils/temp}/abstract_object"
domain="data/beluga/concrete/standard/domain.pddl"
problem="data/beluga/concrete/standard/problem_3_s45_j3_r2_oc44_f3.pddl"

run_explicit() {
    "$python_bin" -m scripts.abstract_object \
        --domain "$domain" \
        --problem "$problem" \
        --output-domain "$output_root/explicit/domain.pddl" \
        --output-problem "$output_root/explicit/problem.pddl" \
        --objects hangar1 hangar2 hangar3 \
        --abstract-name hangarabs
}

run_auto() {
    "$python_bin" -m scripts.abstract_object \
        --domain "$domain" \
        --problem "$problem" \
        --output-domain "$output_root/auto/domain.pddl" \
        --output-problem "$output_root/auto/problem.pddl" \
        --auto \
        --abstract-name hangarabs \
        --bliss-time-limit 300
}

usage() {
    echo "Usage: $0 [explicit|auto|all]"
}

workflow="${1:-explicit}"
case "$workflow" in
    explicit)
        run_explicit
        ;;
    auto)
        run_auto
        ;;
    all)
        run_explicit
        run_auto
        ;;
    -h|--help)
        usage
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac
