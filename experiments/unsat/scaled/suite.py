"""The scaled unsat suite, one <domain>-size-N domain per domain and class size. See README.md."""

SIZES = (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000)
SUITE = [f"over-nomystery-size-{size}" for size in SIZES]
