from typing import List


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists: List[List[int]])->List[int]:
    results = []
    for level1 in lists:
        for level2 in level1:
            results.append(level2)
    return results



print(flatten(n))
