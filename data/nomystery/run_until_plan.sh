#!/bin/bash

# Usage:
# ./run_until_plan.sh p11
# ./run_until_plan.sh p08 p09 p10

OUTPUT_FILE="results_until_plan.txt"
> "$OUTPUT_FILE"

for PROB in "$@"
do
    echo "===================================" >> "$OUTPUT_FILE"
    echo "Problem: $PROB" >> "$OUTPUT_FILE"
    echo "===================================" >> "$OUTPUT_FILE"

    ATTEMPT=1

    while true
    do
        echo "Running $PROB (attempt $ATTEMPT)"

        echo "--- Attempt $ATTEMPT ---" >> "$OUTPUT_FILE"

        RESULT=$(timeout 1200 python ../../../TestScript/test_script_abstraction.py \
            --abstract-domain domain.pddl \
            --abstract-problem "${PROB}.pddl" \
            --concrete-domain nomystery_original/domain.pddl \
            --concrete-problem "nomystery_original/${PROB}.pddl" \
            --mode inc 2>&1)

        echo "$RESULT" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"

        # stop if timeout
        if [ $? -eq 124 ]; then
            echo "TIMEOUT after 20 minutes" >> "$OUTPUT_FILE"
            break
        fi

        # extract Plans found number
        PLANS=$(echo "$RESULT" | grep "Plans found:" | awk '{print $3}')

        # if plans > 0 then stop
        if [ -n "$PLANS" ] && [ "$PLANS" -gt 0 ]; then
            echo "PLAN FOUND after $ATTEMPT attempt(s)" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
            break
        fi

        ATTEMPT=$((ATTEMPT + 1))
    done
done

echo "All results saved to $OUTPUT_FILE"
