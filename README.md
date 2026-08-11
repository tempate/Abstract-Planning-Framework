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
- Abstract planning with refinement (incremental / decremental)

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

Two refinement strategies are used:

- **Incremental (inc)** -> gradually builds constraints
- **Decremental (dec)** -> removes invalid abstract actions step-by-step

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
├── scripts/test_script_concrete.py
├── scripts/test_script_abstraction.py
├── scripts/test_script_abstraction_no_mystery.py
│
├── core/clingo_utils.py
├── core/clingo_utils_api.py
├── core/clingo_utils_api_no_mystery.py
│
├── scripts/fastdownward_service.py
├── core/plasp_utils.py
│
├── scripts/create_excel.py
├── core/json_logger.py
├── core/log_utils.py
├── core/symmetry_abstraction.py
│
├── requirements.txt
├── README.md
│
├── temp/     (auto-generated, NOT tracked in Git)
│   ├── beluga/
│   ├── noMystery/
│   └── jsonFiles/
│
└── lib/
    ├── clingo/
    ├── fast-downward/
    └── planpilot/
```

---

## Running the System

### Concrete Planning

```bash
python -m scripts.test_script_concrete \
    --domain DOMAIN.pddl \
    --problem PROBLEM.pddl \
    --horizon H \
    --encoding exact \
    --time-step
```

### Beluga Abstraction Planning

```bash
python -m scripts.test_script_abstraction \
    --abstract-domain ABSTRACT_DOMAIN.pddl \
    --abstract-problem ABSTRACT_PROBLEM.pddl \
    --concrete-domain CONCRETE_DOMAIN.pddl \
    --concrete-problem CONCRETE_PROBLEM.pddl \
    --abstract-symbol SYMBOL \
    --concrete-objects OBJ1 OBJ2 ... \
    --mode inc \
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
| `--mode` | `inc` (incremental) or `dec` (decremental) |
| `--plan-source` | `clingo` or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Optional planning horizon |
| `--encoding` | ASP encoding type |
| `--time-step` | Enables time-step based encoding |

### NoMystery Abstraction Planning

```bash
python -m scripts.test_script_abstraction_no_mystery \
    --abstract-domain ABSTRACT_DOMAIN.pddl \
    --abstract-problem ABSTRACT_PROBLEM.pddl \
    --concrete-domain CONCRETE_DOMAIN.pddl \
    --concrete-problem CONCRETE_PROBLEM.pddl \
    --horizon H \
    --encoding exact \
    --time-step \
    --mode inc|dec \
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
| `--mode` | `inc` or `dec` |
| `--plan-source` | `clingo` or `fd` — chooses whether to compute the abstract plan using Clingo or use a Fast Downward-generated plan |
| `--horizon` | Optional planning horizon |
| `--encoding` | ASP encoding type |
| `--time-step` | Enables time-step based encoding |

---
