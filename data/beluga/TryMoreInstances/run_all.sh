#!/usr/bin/env bash

# Go to your instance directory
cd ~/Documents/Arbeit/TestFilesBeluga/NewInstances/beluga-small/TryMoreInstances || exit 1

# Output file
OUTFILE="all_runs_output.txt"

# Clear old output
> "$OUTFILE"

# Loop over all matching problem files automatically
for PROBLEM_FILE in problem*.pddl
do
    # skip if no match
    [ -e "$PROBLEM_FILE" ] || continue

    echo "===================================" | tee -a "$OUTFILE"
    echo "Running: $PROBLEM_FILE" | tee -a "$OUTFILE"
    echo "===================================" | tee -a "$OUTFILE"

    timeout 600s python ../../../../TestScript/test_script_concrete.py \
        --domain domain.pddl \
        --problem "$PROBLEM_FILE" \
        >> "$OUTFILE" 2>&1

    if [ $? -eq 124 ]; then
        echo "TIMEOUT (10 min reached) for $PROBLEM_FILE" | tee -a "$OUTFILE"
    fi

    echo "" >> "$OUTFILE"
done

echo "Finished. Results saved in $OUTFILE"
