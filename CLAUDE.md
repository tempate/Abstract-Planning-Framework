# CLAUDE.md

Tests: `python -m unittest discover -s tests -p 'test_*.py'`. No pytest.
Integration tests need `RUN_PLANNER_INTEGRATION=1`.

pre-commit runs black on commit. It reformats and aborts — re-stage and commit again.

`benchmarks/results.csv` is the benchmark artifact. A `running` row is a job that
was killed without a terminal status, not live work; check for them before
drawing conclusions from a run.
