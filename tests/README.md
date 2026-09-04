# Tests

The default suite uses inline PDDL models and test doubles for external planners.
Integration tests are opt-in and run the real toolchain on benchmark tasks.

```bash
python -m unittest discover -s tests -p 'test_*.py'

RUN_PLANNER_INTEGRATION=1 python -m unittest discover -s tests -p 'test_*.py'
```

Only the integrations:

```bash
RUN_PLANNER_INTEGRATION=1 python -m unittest \
    tests.test_example_workflows_integration \
    tests.test_abstraction_symmetry.RealSymmetryIntegrationTests
```
