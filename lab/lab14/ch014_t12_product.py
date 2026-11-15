from typing import List



def product(seq: List[int])->int:
    result = 1
    for item in seq:
        result *= item
    return result