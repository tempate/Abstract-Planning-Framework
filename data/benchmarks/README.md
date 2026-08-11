# Benchmark inputs

This directory contains only the unique PDDL inputs retained from the original
research data dump.

- `nomystery/abstract/` contains the fuel-abstracted NoMystery domain and
  problems; `nomystery/concrete/` contains the matching exact-fuel inputs.
  Each directory is self-contained with its own `domain.pddl`.
- `beluga/concrete/standard/` contains the standard concrete domain and all 48
  available problems.
- `beluga/concrete/more_hangars/` and `more_trailers/` contain the two modified
  concrete variants. Each folder is self-contained with its own `domain.pddl`.
- `beluga/abstract/hangar/` and `trailer/` contain the corresponding abstract
  domains and all available abstract problems. The corrected trailer domain is
  `trailer/domain.pddl`; the superseded version is retained as
  `trailer/domain_legacy.pddl`.

Experiment results and generated files belong under `scripts/utils/temp/`, not
in this input directory.
