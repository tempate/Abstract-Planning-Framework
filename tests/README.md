# Tests

The default suite uses test doubles for external planners. Real workflow and
PDDL Symmetries tests are opt-in.

```bash
# Fast/default suite
python -m unittest discover -s tests -p 'test_*.py' -v

# Real external-tool workflows as well
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest discover -s tests -p 'test_*.py' -v
```

To run only the real integrations:

```bash
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest \
        tests.test_example_workflows_integration \
        tests.test_symmetry_abstraction.RealSymmetryIntegrationTests -v
```

The integration tests execute the public Bash examples in temporary output
directories. Performance examples are intentionally excluded because they can
take a minute or longer.
