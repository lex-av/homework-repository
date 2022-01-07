# -*- coding: utf-8 -*-
"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""


from itertools import product
from typing import List


def combinations(*args: List[int]) -> List[List[int]]:
    """Itertools do all the work"""
    combos = list(product(*args))
    return list(map(list, combos))


if __name__ == "__main__":
    pass
