"""Score candidate abstractions to pick the one that shrinks the task most."""


def abstraction_score(abstraction):
    """Score one candidate abstraction, lowest first.

    Collapsing more objects is what lowers the abstract horizon, so the largest
    class wins and nothing else is weighed.
    """
    return -len(abstraction.objects)
