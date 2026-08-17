# Tests

The suite is layered so that ordinary development does not require invoking
the bundled planner executables.

| Layer | Coverage | Default |
| --- | --- | --- |
| Unit/component | ASP I/O, abstraction transforms, mappings, logs, helpers | yes |
| Symmetry abstraction | Explicit rewriting and mocked symmetry selection | yes |
| Solver | Clingo control setup and decremental switch relaxation | yes |
| Orchestration | Planner calls replaced by deterministic test doubles | yes |
| Workflow | Real planners and PDDL Symmetries on benchmark inputs | opt-in |

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
and do not update the JSON plan history.

GitHub Actions runs the complete suite, including the real planner workflows,
on every push and pull request. Its clean Linux runner initializes the PDDL
Symmetries submodule and builds both Fast Downward and the pybliss extension
before executing the tests.

The deliberately long `performance` example modes are demonstrations, not
test cases. CI covers their argument wiring without running the minute-scale
concrete searches; the smaller real workflows cover the external toolchain.
