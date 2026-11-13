from typing import List


def list_function(x: List[int]) -> List[int]:
    x[1] += 3
    return x


n = [3, 5, 7]
print(list_function(n))
