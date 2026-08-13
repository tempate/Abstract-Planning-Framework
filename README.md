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

Refinement removes invalid abstract actions step-by-step using the decremental
solver.

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
│   ├── AbstractPlanner.py
│   ├── BelugaPlanner.py
│   ├── NoMysteryPlanner.py
│   └── factory.py
├── core/solvers/
│   ├── AbstractSolver.py
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

Run one concrete plan followed by abstract-plan refinement:

```bash
./scripts/run_examples.sh
```

Each case uses the small NoMystery example in `data/examples/` and should find
a plan in a few seconds. Use `./scripts/run_examples.sh concrete` or
`abstract` to run one case. See [`data/README.md`](data/README.md) for the data
layout; the larger PDDL collections are under `data/benchmarks/`.

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
| `--plan-source` | `clingo` or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Optional planning horizon |
| `--encoding` | ASP encoding type |
| `--time-step` | Enables time-step based encoding |

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
| `--plan-source` | `clingo` or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Optional planning horizon |
| `--encoding` | ASP encoding type |
| `--time-step` | Enables time-step based encoding |

---
