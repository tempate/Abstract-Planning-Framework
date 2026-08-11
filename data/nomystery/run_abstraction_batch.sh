#!/bin/bash

# Usage:
# ./run_abstraction_batch.sh p08 p09 p10 ...

OUTPUT_FILE="results_abstraction.txt"
> "$OUTPUT_FILE"

for PROB in "$@"
do
    ABSTRACT_PROBLEM="./${PROB}.pddl"
    CONCRETE_PROBLEM="nomystery_original/${PROB}.pddl"

    echo "===================================" >> "$OUTPUT_FILE"
    echo "Problem: $PROB" >> "$OUTPUT_FILE"
    echo "===================================" >> "$OUTPUT_FILE"

    for MODE in inc dec
    do
        echo "Running $PROB ($MODE)"

        echo "--- MODE: $MODE ---" >> "$OUTPUT_FILE"

        timeout 1200 python ../../../TestScript/test_script_abstraction_no_mystery.py \
            --abstract-domain domain.pddl \
            --abstract-problem "$ABSTRACT_PROBLEM" \
            --concrete-domain nomystery_original/domain.pddl \
            --concrete-problem "$CONCRETE_PROBLEM" \
            --mode "$MODE" >> "$OUTPUT_FILE" 2>&1

        if [ $? -eq 124 ]; then
            echo "TIMEOUT after 20 minutes" >> "$OUTPUT_FILE"
        fi

        echo "" >> "$OUTPUT_FILE"
    done

done

echo "All results saved to $OUTPUT_FILE"
