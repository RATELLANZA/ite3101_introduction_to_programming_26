from typing import Any


def distance_from_zero(d: Any)->Any:
    if type(d) == int or type(d) == float:
        return abs(d)
    else:
