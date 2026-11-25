"""Names for the object classes an abstraction can collapse."""

import hashlib


def class_id(object_type, objects):
    """The name a class goes by in classes.txt and the results: its type, its size and a digest of its objects.

    A rescan that finds other classes reorders the list, so a position would name another class.
    """
    digest = hashlib.sha1(" ".join(sorted(objects)).encode()).hexdigest()[:6]
    return f"{object_type}-{len(objects)}-{digest}"
