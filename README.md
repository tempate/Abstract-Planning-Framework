# Planning Framework (Concrete vs Abstract Planning)

## Overview

This project is an experimental planning framework for evaluating **concrete vs abstract planning** across multiple domains and abstraction types.

It supports:

- **Beluga domain**
  - Hangar abstraction
  - Trailer abstraction

- **NoMystery domain**
  - Fuel abstraction

The system compares:

- Classical (concrete) planning
- Abstract planning with decremental refinement

It uses:

- Clingo
- Fast Downward
- PlanPilot

---

## Planning Modes

### 1. Concrete Planning

- Direct planning without abstraction
- Uses Fast Downward + Clingo encoding
- Produces a plan if one exists

---

### 2. Abstract Planning

- Starts from an abstract representation of the problem
- Generates an abstract plan
- Maps it back to the concrete level
- If the plan is invalid, refinement is applied

The decremental solver starts with the abstract-plan constraints and relaxes
them in reverse order. It stops at the first concrete plan it finds. The
concrete plan does not have to ground the complete abstract plan.

---

## Project Setup

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

---

## External Dependencies

The following tools must be available in the `lib/` directory:

```text
lib/
├── clingo/
├── fast-downward/
└── planpilot/
```

---

## Project Structure

```text
project/
│
├── scripts/concrete_planner.py
├── scripts/abstract_planner.py
│
├── core/paths.py
├── core/asp.py
├── core/planners/
│   ├── BasePlanner.py
│   ├── BelugaPlanner.py
│   ├── NoMysteryPlanner.py
│   └── factory.py
├── core/solvers/
│   ├── BaseSolver.py
│   ├── DecrementalSolver.py
├── core/integrations/
│   ├── clingo.py
│   ├── fast_downward.py
│   └── plasp.py
├── core/execution.py
├── tools/symmetry_abstraction.py
│
├── scripts/utils/reporting.py
├── scripts/utils/abstract_plan_log.py
│
├── requirements.txt
├── README.md
│
├── scripts/utils/temp/     (auto-generated, NOT tracked in Git)
│   ├── beluga/
│   ├── noMystery/            (NoMystery profile output)
│   └── jsonFiles/
│
└── lib/
    ├── clingo/
    ├── fast-downward/
    └── planpilot/
```

---

## Running the System

### Quick start with verified examples

Run the quick concrete, fully realizable abstract, and matched refinement
examples:

```bash
python -m examples.no_mystery
```

The concrete and abstract baselines use the small NoMystery problem in
`data/examples/`. The refinement mode solves benchmark `p01` both concretely
and through the abstraction, then prints their timings side by side. See
[`data/README.md`](data/README.md) for the data layout.

The Python API options are documented in
[`examples/README.md`](examples/README.md).
The NoMystery and Beluga examples each include a matched `refinement` mode and
an opt-in `performance` mode. The latter compares a deliberately slow concrete
search with the abstract workflow on exactly the same problem:

```bash
python -m examples.no_mystery performance
python -m examples.beluga performance
```

These runs can take a minute or longer. Their final tables report the measured
end-to-end ratio rather than assuming that abstraction is faster.

The examples pass explicit horizons, so Fast Downward only translates their
PDDL inputs to SAS. If the Python API is called without a horizon, Fast
Downward planning is used explicitly as an automatic horizon oracle; with
`plan_source="fd"`, its actual plan drives refinement.

### Tests

Run the fast unit, component, and solver suite:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

The real planning workflows are kept as an opt-in integration layer because
they invoke Fast Downward and PlanPilot:

```bash
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest tests.test_planning_integration -v
```

See [`tests/README.md`](tests/README.md) for the test layers and the command
that runs the complete suite.

### Planning configuration

Programmatic runs use one immutable configuration object per workflow. Paths
and behavior options are assembled once at the entry point and then passed
through the planning pipeline together:

```python
from core.planning.config import ConcretePlanningConfig
from core.planning.concrete import compute_concrete_plan

config = ConcretePlanningConfig(
    domain_path="domain.pddl",
    problem_path="problem.pddl",
    horizon=None,
    encoding="exact",
    time_step=False,
)
result = compute_concrete_plan(config)
```

`AbstractPlanningConfig` provides the equivalent API for abstraction-based
runs. Shared default constants in `core.planning.config` are authoritative,
and each result includes the submitted configuration under
`result["configuration"]`.

### Concrete Planning

```bash
python -m scripts.concrete_planner \
    --domain DOMAIN.pddl \
    --problem PROBLEM.pddl \
    --horizon H \
    --encoding exact \
    --time-step
```

### Beluga Abstraction Planning

`abstract_planner` is the shared entry point for both domains. Domain planners
in `core/planners/abstraction.py` inherit common hooks and implement their own
switch mapping and refinement behavior. Beluga is the default profile; it
requires an abstract symbol and the concrete objects it represents.

```bash
python -m scripts.abstract_planner \
    --abstract-domain ABSTRACT_DOMAIN.pddl \
    --abstract-problem ABSTRACT_PROBLEM.pddl \
    --concrete-domain CONCRETE_DOMAIN.pddl \
    --concrete-problem CONCRETE_PROBLEM.pddl \
    --abstract-symbol SYMBOL \
    --concrete-objects OBJ1 OBJ2 ... \
    --plan-source clingo
```

#### Parameters

| Parameter | Description |
|------------|------------|
| `--abstract-domain` | Abstract domain file |
| `--abstract-problem` | Abstract problem file |
| `--concrete-domain` | Concrete domain file |
| `--concrete-problem` | Concrete problem file |
| `--abstract-symbol` | Abstract object symbol (e.g. `hangarabs`, `beluga_abs_trailer`) |
| `--concrete-objects` | Concrete objects mapped to abstraction |
| `--plan-source` | `clingo` (default) or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Planning horizon; by default Fast Downward infers it |
| `--encoding` | ASP encoding type (default: `exact`) |
| `--time-step` | Enables time-step based encoding (default: disabled) |

### NoMystery Abstraction Planning

The `no_mystery` profile selects NoMystery's fuel-aware mapping and drive-action
refinement.  It does not require `--abstract-symbol` or `--concrete-objects`.

```bash
python -m scripts.abstract_planner \
    --profile no_mystery \
    --abstract-domain ABSTRACT_DOMAIN.pddl \
    --abstract-problem ABSTRACT_PROBLEM.pddl \
    --concrete-domain CONCRETE_DOMAIN.pddl \
    --concrete-problem CONCRETE_PROBLEM.pddl \
    --horizon H \
    --encoding exact \
    --time-step \
    --plan-source clingo|fd
```

#### Parameters

| Parameter | Description |
|------------|------------|
| `--abstract-domain` | Abstract domain file |
| `--abstract-problem` | Abstract problem file |
| `--concrete-domain` | Concrete domain file |
| `--concrete-problem` | Concrete problem file |
| `--abstract-symbol` | Abstract object symbol |
| `--concrete-objects` | Concrete objects represented by the abstraction |
| `--plan-source` | `clingo` (default) or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Planning horizon; by default Fast Downward infers it |
| `--encoding` | ASP encoding type (default: `exact`) |
| `--time-step` | Enables time-step based encoding (default: disabled) |

---
