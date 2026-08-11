#!/usr/bin/env bash

cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small || exit 1

OUTFILE="more_hangar_abstraction_runs.txt"
> "$OUTFILE"

run_case () {
    PROBLEM_BASE="$1"
    HANGARS="$2"

    for MODE in inc dec; do
        echo "===================================" | tee -a "$OUTFILE"
        echo "Problem: ${PROBLEM_BASE} | Mode: ${MODE}" | tee -a "$OUTFILE"
        echo "Hangars: ${HANGARS}" | tee -a "$OUTFILE"
        echo "Timeout: 20 minutes" | tee -a "$OUTFILE"
        echo "===================================" | tee -a "$OUTFILE"

        timeout 20m python3 ../../../TestScript/test_script_abstraction.py \
            --abstract-domain HangarAbstraction/domain_abs.pddl \
            --abstract-problem "HangarAbstraction/${PROBLEM_BASE}_abs.pddl" \
            --concrete-domain domain.pddl \
            --concrete-problem "InstancesWithMoreHangars/${PROBLEM_BASE}.pddl" \
            --abstract-symbol hangarabs \
            --concrete-objects ${HANGARS} \
            --mode ${MODE} \
            >> "$OUTFILE" 2>&1

        EXITCODE=$?

        if [ $EXITCODE -eq 124 ]; then
            echo ">>> TIMED OUT after 20 minutes" | tee -a "$OUTFILE"
        elif [ $EXITCODE -ne 0 ]; then
            echo ">>> FAILED with exit code $EXITCODE" | tee -a "$OUTFILE"
        else
            echo ">>> FINISHED successfully" | tee -a "$OUTFILE"
        fi

        echo "" >> "$OUTFILE"
    done
}

#run_case "problem_1_s43_j5_r2_oc51_f3"  "hangar1 hangar2 hangar3"
#run_case "problem_3_s45_j3_r2_oc44_f3"  "hangar1 hangar2 hangar3 hangar4 hangar5 hangar6 hangar7"
run_case "problem_12_s54_j8_r2_oc86_f4" "hangar1 hangar2 hangar3"
#run_case "problem_14_s56_j6_r2_oc77_f3" "hangar1 hangar2 hangar3 hangar4 hangar5"
#run_case "problem_26_s68_j6_r2_oc87_f4" "hangar1 hangar2 hangar3 hangar4"
#run_case "problem_39_s82_j4_r2_oc23_f3" "hangar1 hangar2 hangar3 hangar4 hangar5"

echo "Finished. Results saved in $OUTFILE"
