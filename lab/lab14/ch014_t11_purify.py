from typing import List



def purify(seq: List[int]) -> List[int]:
    result =[]
    for item in seq:
        if item % 2 == 0:
            result.append(item)
    return result