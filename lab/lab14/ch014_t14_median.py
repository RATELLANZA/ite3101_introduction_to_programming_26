
from typing import List



def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        index_1 = len(sorted_lst) // 2 - 1
        index_2 = len(sorted_lst) // 2
        (sorted_lst[index_1] + sorted_lst[index_2]) / 2.0
    index = length // 2
    return sorted_lst[index]
