from typing import Any


def cube(number: int) -> int:
    return number * number * number


def by_three(number: int) -> Any:
    if number % 3 == 0:
        return cube(number)
    return False
