#!/usr/bin/env bash

cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small/TryMoreInstances || exit 1

OUTFILE="hangar_abstraction_runs.txt"
> "$OUTFILE"

run_case () {
    PROBLEM_BASE="$1"
    HANGARS="$2"

    for MODE in inc dec; do
        echo "===================================" | tee -a "$OUTFILE"
        echo "Problem: ${PROBLEM_BASE} | Mode: ${MODE}" | tee -a "$OUTFILE"
        echo "Hangars: ${HANGARS}" | tee -a "$OUTFILE"
        echo "Timeout: 10 minutes" | tee -a "$OUTFILE"
        echo "===================================" | tee -a "$OUTFILE"

        timeout 10m python3 ../../../../TestScript/test_script_abstraction.py \
            --abstract-domain HangarAbstraction/domain_abs.pddl \
            --abstract-problem "HangarAbstraction/${PROBLEM_BASE}_abs.pddl" \
            --concrete-domain domain.pddl \
            --concrete-problem "${PROBLEM_BASE}.pddl" \
            --abstract-symbol hangarabs \
            --concrete-objects ${HANGARS} \
            --mode ${MODE} \
            >> "$OUTFILE" 2>&1

        EXITCODE=$?

        if [ $EXITCODE -eq 124 ]; then
            echo ">>> TIMED OUT after 10 minutes" | tee -a "$OUTFILE"
        elif [ $EXITCODE -ne 0 ]; then
            echo ">>> FAILED with exit code $EXITCODE" | tee -a "$OUTFILE"
        else
            echo ">>> FINISHED successfully" | tee -a "$OUTFILE"
        fi

        echo "" >> "$OUTFILE"
    done
}

# ----------------------------
# Define cases: "problem|hangar_count"
# ----------------------------
cases=(
"problem_0_s42_j10_r2_oc31_f4|3"
"problem_10_s52_j6_r2_oc81_f4|2"
"problem_11_s53_j6_r2_oc73_f4|2"
"problem_15_s57_j11_r2_oc86_f3|3"
"problem_19_s61_j9_r2_oc80_f5|2"
"problem_20_s62_j14_r2_oc32_f3|3"
"problem_23_s65_j6_r2_oc23_f3|2"
"problem_25_s67_j6_r2_oc50_f4|2"
"problem_27_s69_j7_r2_oc66_f3|3"
"problem_28_s70_j6_r2_oc54_f4|2"
"problem_30_s73_j5_r2_oc80_f3|2"
"problem_31_s74_j6_r2_oc55_f4|2"
"problem_32_s75_j3_r2_oc25_f3|2"
"problem_35_s78_j11_r2_oc34_f4|2"
"problem_38_s81_j5_r2_oc31_f4|3"
"problem_40_s83_j10_r2_oc80_f4|2"
"problem_42_s85_j9_r2_oc22_f4|2"
"problem_45_s88_j5_r2_oc58_f3|2"
"problem_46_s89_j3_r2_oc32_f3|2"
"problem_47_s90_j6_r2_oc59_f3|2"
"problem_48_s91_j6_r2_oc81_f5|3"
"problem_2_s44_j7_r2_oc83_f3|2"
"problem_4_s46_j6_r2_oc73_f3|2"
"problem_6_s48_j8_r2_oc80_f3|2"
"problem_7_s49_j13_r2_oc80_f5|2"
"problem_8_s50_j4_r2_oc84_f4|2"
"problem_9_s51_j8_r2_oc90_f5|2"
)

# ----------------------------
# Run loop
# ----------------------------
for entry in "${cases[@]}"; do
    PROBLEM_BASE="${entry%|*}"
    N="${entry#*|}"

    HANGARS=""
    for ((i=1; i<=N; i++)); do
        HANGARS+="hangar${i} "
    done
    HANGARS="${HANGARS% }"

    run_case "$PROBLEM_BASE" "$HANGARS"
done

echo "Finished. Results saved in $OUTFILE"
