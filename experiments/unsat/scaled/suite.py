"""The scaled unsat suite, one size-N domain per class size. See README.md."""

SIZES = (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000)
SUITE = [f"size-{size}" for size in SIZES]
