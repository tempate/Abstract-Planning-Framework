#!/usr/bin/env bash

# Go to your instance directory
cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small || exit 1

# Output file
OUTFILE="all_runs_output_more_hangars.txt"

# Clear old output
> "$OUTFILE"

# Loop over all problem files
for problem in InstancesWithMoreHangars/problem_*.pddl; do
    echo "===================================" | tee -a "$OUTFILE"
    echo "Running: $problem" | tee -a "$OUTFILE"
    echo "Timeout: 20 minutes" | tee -a "$OUTFILE"
    echo "===================================" | tee -a "$OUTFILE"

    timeout 20m python3 ../../../TestScript/test_script_concrete.py \
        --domain domain.pddl \
        --problem "$problem" \
        >> "$OUTFILE" 2>&1

    status=$?

    if [ $status -eq 124 ]; then
        echo "ERROR: TIMEOUT after 20 minutes for $problem" | tee -a "$OUTFILE"
    elif [ $status -ne 0 ]; then
        echo "ERROR: Process exited with code $status for $problem" | tee -a "$OUTFILE"
    fi

    echo "" >> "$OUTFILE"
done

echo "Finished. Results saved in $OUTFILE"
