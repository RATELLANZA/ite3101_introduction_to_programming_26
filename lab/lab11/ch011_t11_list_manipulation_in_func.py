from typing import List


n = [3, 5, 7]
# Add your function here


def list_extender(l: List[int]) -> List[int]:
    l.append(9)
    return l


print(list_extender(n))
