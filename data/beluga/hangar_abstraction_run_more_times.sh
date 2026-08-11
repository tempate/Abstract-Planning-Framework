#!/usr/bin/env bash

cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small || exit 1

OUTFILE="hangar_abstraction_runs_more_times.txt"
> "$OUTFILE"

run_case () {
    PROBLEM_BASE="$1"
    HANGARS="$2"

    for MODE in inc dec; do
        echo "===================================" | tee -a "$OUTFILE"
        echo "Run: ${RUN}"
        echo "Problem: ${PROBLEM_BASE} | Mode: ${MODE}" | tee -a "$OUTFILE"
        echo "Hangars: ${HANGARS}" | tee -a "$OUTFILE"
        echo "Timeout: 30 minutes" | tee -a "$OUTFILE"
        echo "===================================" | tee -a "$OUTFILE"

        timeout 30m python3 ../../../TestScript/test_script_abstraction.py \
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

# Repeat entire experiment 10 times
for RUN in {1..10}; do
    echo "###################################" | tee -a "$OUTFILE"
    echo "########## RUN ${RUN} ##########" | tee -a "$OUTFILE"
    echo "###################################" | tee -a "$OUTFILE"

    #run_case "problem_3_s45_j3_r2_oc44_f3"  "hangar1 hangar2 hangar3"
    #run_case "problem_14_s56_j6_r2_oc77_f3" "hangar1 hangar2 hangar3"
    run_case "problem_26_s68_j6_r2_oc87_f4" "hangar1 hangar2"
    run_case "problem_33_s76_j9_r2_oc85_f3" "hangar1 hangar2"
    #run_case "problem_36_s79_j9_r2_oc62_f4" "hangar1 hangar2 hangar3"
    #run_case "problem_41_s84_j10_r2_oc64_f3" "hangar1 hangar2"
    #run_case "problem_43_s86_j7_r2_oc44_f5" "hangar1 hangar2"

    echo "" | tee -a "$OUTFILE"
done

echo "Finished. Results saved in $OUTFILE"
