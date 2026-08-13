# Tests

The suite is layered so that ordinary development does not require invoking
the bundled planner executables.

| Layer | Coverage | Default |
| --- | --- | --- |
| Unit/component | ASP I/O, abstraction transforms, mappings, logs, helpers | yes |
| Solver | Clingo control setup and decremental switch relaxation | yes |
| Orchestration | Planner calls replaced by deterministic test doubles | yes |
| Workflow | Real Fast Downward, PlanPilot, and Clingo on NoMystery | opt-in |

Run the fast suite from the repository root:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Run only the real planner workflows:

```bash
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest tests.test_planning_integration -v
```

Run every test, including the workflow layer:

```bash
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest discover -s tests -p 'test_*.py' -v
```

The tests use Python's standard `unittest` runner, so no development-only
package is required. Workflow tests create isolated temporary run directories
and do not update the experiment spreadsheet or JSON plan history.
