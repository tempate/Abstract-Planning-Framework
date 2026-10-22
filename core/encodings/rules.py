"""Rules of the sequential encoding that callers swap for variants of it."""

# Must match the action rule in sequential-incremental.lp, or replacing it silently does nothing.
EXACTLY_ONE_ACTION = "1 {occurs(Action, t) : action(Action)} 1"
AT_MOST_ONE_ACTION = "{occurs(Action, t) : action(Action)} 1"
