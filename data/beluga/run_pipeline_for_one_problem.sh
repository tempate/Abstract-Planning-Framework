#!/bin/bash

INPUT1="$1"
INPUT2="$2"
INPUT3="$3"

if [ $# -ne 3 ]; then
  echo "Usage: $0 <problem_name> <base_objects> <extended_objects>"
  echo "Example: $0 problem1 \"a b c\" \"a b c d e\""
  exit 1
fi

run_step () {
  DESC="$1"
  shift

  echo ""
  echo "===================="
  echo "$DESC"
  echo "===================="

  timeout 30m "$@"
  STATUS=$?

  if [ $STATUS -eq 124 ]; then
    echo "[WARN] Timeout occurred in: $DESC"
  elif [ $STATUS -ne 0 ]; then
    echo "[ERROR] Failure in: $DESC (exit code $STATUS)"
  else
    echo "[OK] Success: $DESC"
  fi

  return 0  # NEVER propagate failure
}

echo "Running pipeline for: $INPUT1"
echo "Base objects: $INPUT2"
echo "Extended objects: $INPUT3"


# =========================
# 1) Concrete base
# =========================
run_step "Concrete base" python ../../../TestScript/test_script_concrete.py \
  --domain domain.pddl \
  --problem "${INPUT1}.pddl"


# =========================
# 2) Abstraction INC base
# =========================
#run_step "Abstraction INC (base)" python ../../../TestScript/test_script_abstraction.py \
#  --abstract-domain HangarAbstraction/domain_abs.pddl \
#  --abstract-problem "HangarAbstraction/${INPUT1}_abs.pddl" \
#  --concrete-domain domain.pddl \
#  --concrete-problem "${INPUT1}.pddl" \
#  --abstract-symbol hangarabs \
#  --concrete-objects "${INPUT2}" \
#  --mode inc


# =========================
# 3) Abstraction DEC base
# =========================
#run_step "Abstraction DEC (base)" python ../../../TestScript/test_script_abstraction.py \
#  --abstract-domain HangarAbstraction/domain_abs.pddl \
#  --abstract-problem "HangarAbstraction/${INPUT1}_abs.pddl" \
#  --concrete-domain domain.pddl \
#  --concrete-problem "${INPUT1}.pddl" \
#  --abstract-symbol hangarabs \
#  --concrete-objects "${INPUT2}" \
#  --mode dec


# =========================
# 4) Concrete extended
# =========================
run_step "Concrete extended" python ../../../TestScript/test_script_concrete.py \
  --domain InstancesWithMoreHangars/domain.pddl \
  --problem "InstancesWithMoreHangars/${INPUT1}.pddl"


# =========================
# 5) Abstraction INC extended
# =========================
run_step "Abstraction INC (extended)" python ../../../TestScript/test_script_abstraction.py \
  --abstract-domain HangarAbstraction/domain_abs.pddl \
  --abstract-problem "HangarAbstraction/${INPUT1}_abs.pddl" \
  --concrete-domain InstancesWithMoreHangars/domain.pddl \
  --concrete-problem "InstancesWithMoreHangars/${INPUT1}.pddl" \
  --abstract-symbol hangarabs \
  --concrete-objects "${INPUT3}" \
  --mode inc


# =========================
# 6) Abstraction DEC extended
# =========================
run_step "Abstraction DEC (extended)" python ../../../TestScript/test_script_abstraction.py \
  --abstract-domain HangarAbstraction/domain_abs.pddl \
  --abstract-problem "HangarAbstraction/${INPUT1}_abs.pddl" \
  --concrete-domain InstancesWithMoreHangars/domain.pddl \
  --concrete-problem "InstancesWithMoreHangars/${INPUT1}.pddl" \
  --abstract-symbol hangarabs \
  --concrete-objects "${INPUT3}" \
  --mode dec


echo ""
echo "===================="
echo "PIPELINE COMPLETE (with possible failures)"
echo "===================="
