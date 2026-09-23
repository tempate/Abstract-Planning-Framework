"""The outcome handling every planner entry point shares."""

import sys
import traceback

from core.abstraction.collapse import AbstractionError
from core.integrations.unified_planning import PddlError
from core.outcomes import PlanningOutcomeError


def run(parser, compute, report):
    """Parse the arguments and compute, returning the exit code the benchmark runner reads the outcome from."""
    args = parser.parse_args()
    try:
        print("Starting")
        result = compute(args)
    except PlanningOutcomeError as error:
        print(f"{error.label}: {error}")
        return error.exit_code
    except (AbstractionError, PddlError, OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    except Exception as error:
        # Left uncaught it exits 1, which reads as a task proved unsolvable.
        print(f"Error: {error!r}")
        traceback.print_exc(file=sys.stdout)
        return PlanningOutcomeError.exit_code
    return report(result)
