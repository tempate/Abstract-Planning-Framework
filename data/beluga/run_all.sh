#!/usr/bin/env bash

# Usage:
# ./run_all.sh p10.pddl p11.pddl p12.pddl


# Go to your instance directory
cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small || exit 1

# Output file
OUTFILE="all_runs_output.txt"

# Clear old output
> "$OUTFILE"

# Loop over all problem files
for PROBLEM_FILE in "$@"
do
    echo "===================================" | tee -a "$OUTFILE"
    echo "Running: $PROBLEM_FILE" | tee -a "$OUTFILE"
    echo "===================================" | tee -a "$OUTFILE"

    timeout 1200s python ../../../TestScript/test_script_concrete.py \
        --domain domain.pddl \
        --problem "$PROBLEM_FILE" \
        >> "$OUTFILE" 2>&1

    if [ $? -eq 124 ]; then
        echo "TIMEOUT (20 min reached) for $PROBLEM_FILE" | tee -a "$OUTFILE"
    fi

    echo "" >> "$OUTFILE"
done

echo "Finished. Results saved in $OUTFILE"
