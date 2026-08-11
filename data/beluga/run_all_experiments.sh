#!/usr/bin/env bash

cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small || exit 1

PROBLEMS=(
  "problem_1_s43_j5_r2_oc51_f3"
  "problem_3_s45_j3_r2_oc44_f3"
  "problem_12_s54_j8_r2_oc86_f4"
  "problem_14_s56_j6_r2_oc77_f3"
  "problem_26_s68_j6_r2_oc87_f4"
  "problem_33_s76_j9_r2_oc85_f3"
  "problem_39_s82_j4_r2_oc23_f3"
)

############################
# 1) CONCRETE RUNS
############################

OUTFILE1="all_runs_output_concrete_new.txt"
> "$OUTFILE1"

for problem in "${PROBLEMS[@]}"; do
    file="InstancesWithMoreHangars/${problem}.pddl"

    echo "===================================" | tee -a "$OUTFILE1"
    echo "Running: $file" | tee -a "$OUTFILE1"
    echo "Timeout: 20 minutes" | tee -a "$OUTFILE1"
    echo "===================================" | tee -a "$OUTFILE1"

    timeout 20m python3 ../../../TestScript/test_script_concrete.py \
        --domain domain.pddl \
        --problem "$file" \
        >> "$OUTFILE1" 2>&1

    echo "" >> "$OUTFILE1"
done

echo "Concrete runs finished."

############################
# 2) ABSTRACTION RUNS (standard)
############################

OUTFILE2="hangar_abstraction_runs_new.txt"
> "$OUTFILE2"

run_abstraction () {
    PROBLEM_BASE="$1"
    HANGARS="$2"

    for MODE in inc dec; do
        echo "===================================" | tee -a "$OUTFILE2"
        echo "Problem: ${PROBLEM_BASE} | Mode: ${MODE}" | tee -a "$OUTFILE2"
        echo "Hangars: ${HANGARS}" | tee -a "$OUTFILE2"

        timeout 40m python3 ../../../TestScript/test_script_abstraction.py \
            --abstract-domain HangarAbstraction/domain_abs.pddl \
            --abstract-problem "HangarAbstraction/${PROBLEM_BASE}_abs.pddl" \
            --concrete-domain domain.pddl \
            --concrete-problem "${PROBLEM_BASE}.pddl" \
            --abstract-symbol hangarabs \
            --concrete-objects ${HANGARS} \
            --mode ${MODE} \
            >> "$OUTFILE2" 2>&1

        echo "" >> "$OUTFILE2"
    done
}

for problem in "${PROBLEMS[@]}"; do
    run_abstraction "$problem" "hangar1 hangar2 hangar3"
done

echo "Standard abstraction runs finished."

############################
# 3) ABSTRACTION RUNS (more hangars version)
############################

OUTFILE3="more_hangar_abstraction_runs_new.txt"
> "$OUTFILE3"

run_more_hangars () {
    PROBLEM_BASE="$1"
    HANGARS="$2"

    for MODE in inc dec; do
        echo "===================================" | tee -a "$OUTFILE3"
        echo "Problem: ${PROBLEM_BASE} | Mode: ${MODE}" | tee -a "$OUTFILE3"
        echo "Hangars: ${HANGARS}" | tee -a "$OUTFILE3"

        timeout 20m python3 ../../../TestScript/test_script_abstraction.py \
            --abstract-domain HangarAbstraction/domain_abs.pddl \
            --abstract-problem "HangarAbstraction/${PROBLEM_BASE}_abs.pddl" \
            --concrete-domain domain.pddl \
            --concrete-problem "InstancesWithMoreHangars/${PROBLEM_BASE}.pddl" \
            --abstract-symbol hangarabs \
            --concrete-objects ${HANGARS} \
            --mode ${MODE} \
            >> "$OUTFILE3" 2>&1

        echo "" >> "$OUTFILE3"
    done
}

for problem in "${PROBLEMS[@]}"; do
    run_more_hangars "$problem" "hangar1 hangar2 hangar3"
done

echo "More-hangar abstraction runs finished."

echo "ALL DONE."
