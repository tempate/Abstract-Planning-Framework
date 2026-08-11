#!/bin/bash

# Usage:
# ./run_tests.sh domain.pddl p10.pddl p11.pddl p12.pddl

DOMAIN_FILE="$1"
shift

OUTPUT_FILE="results.txt"

# Clear old output
> "$OUTPUT_FILE"

for PROBLEM_FILE in "$@"
do
    echo "Running: $PROBLEM_FILE"

    echo "===== $PROBLEM_FILE =====" >> "$OUTPUT_FILE"

    # Run with 10 minute timeout (600 seconds)
    timeout 600 python ../../../../TestScript/test_script_concrete.py \
        --domain "$DOMAIN_FILE" \
        --problem "$PROBLEM_FILE" >> "$OUTPUT_FILE" 2>&1

    # Check if timeout happened
    if [ $? -eq 124 ]; then
        echo "TIMEOUT after 10 minutes" >> "$OUTPUT_FILE"
    fi

    echo "" >> "$OUTPUT_FILE"
done

echo "All results saved to $OUTPUT_FILE"
