"""The scaled unsat suite, one <domain>/size-N directory per domain and class size. See README.md."""

SIZES = (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000)
# The domains whose problems M&S-alpha proves unsolvable by collapsing a class,
# with the class sizes their base problems start from beyond SIZES.
DOMAINS = ("cave-diving", "document-transfer", "over-nomystery", "over-rovers")
BASE_SIZES = (4, 8, 12)
SUITE = [f"{domain}/size-{size}" for domain in DOMAINS for size in sorted(set(SIZES) | set(BASE_SIZES))]
