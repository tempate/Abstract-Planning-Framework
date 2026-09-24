# CLAUDE.md

Tests: `python -m unittest discover -s tests -p 'test_*.py'`. No pytest.
Only `.venv` has `unified_planning`, so run them with the venv active, or spell
out `.venv/bin/python`.
Integration tests need `RUN_PLANNER_INTEGRATION=1`.

Before calling a change to `core/abstraction` behavior-preserving, run
`python -m scripts.compare_abstractions main`; it compares the abstract task of
each domain's first problem against that commit. The tests cannot show this.

pre-commit runs black on commit. It reformats and aborts — re-stage and commit again.

`experiments/plan/symmetries/results.csv` is the benchmark artifact. A `running` row is a job that
was killed without a terminal status, not live work; check for them before
drawing conclusions from a run. `interrupted` is runsolver's memory limit.
