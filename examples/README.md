# Examples

## NoMystery

The example runs the same verified PDDL inputs as `scripts/run_examples.sh`
without writing spreadsheet or JSON experiment summaries:

```bash
python -m examples.no_mystery concrete
python -m examples.no_mystery abstract
python -m examples.no_mystery all
```

These commands exercise the bundled Fast Downward and PlanPilot executables.
Run them from the repository root after installing `requirements.txt`.
