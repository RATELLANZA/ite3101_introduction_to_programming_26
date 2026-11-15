
from typing import List



def median(lsi: List[int]) -> float:
    sorted_lst = sorted(lst)
    if len(sorted_lst) % 2 == 0:
        index_1 = len(sorted_lst) // 2 - 1
        index_2 = len(sorted_lst) // 2
        m = (sorted_lst[index_1] + sorted_lst[index_2]) / 2.0
        return m
    index = length // 2
    return sorted_lst[index]
