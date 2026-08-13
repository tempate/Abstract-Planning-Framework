# Examples

## NoMystery

The example runs the verified PDDL inputs without writing spreadsheet or JSON
experiment summaries:

```bash
python -m examples.no_mystery concrete
python -m examples.no_mystery abstract
python -m examples.no_mystery all
```

These commands exercise the bundled Fast Downward and PlanPilot executables.
Run them from the repository root after installing `requirements.txt`.

## Beluga

The Beluga example uses a small checked-in benchmark instance and its hangar
abstraction. The abstract object `hangarabs` represents `hangar1`,
`hangar2`, and `hangar3`.

```bash
python -m examples.beluga concrete
python -m examples.beluga abstract
python -m examples.beluga all
```

As with NoMystery, omitting the argument runs both workflows.
