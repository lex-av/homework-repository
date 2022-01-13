# Created by allex at 11.11.2021
# -*- coding: utf-8 -*-
"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Use itertools.product to find triplets and then
    find quadruples, using search"""

    quads_count = 0
    triplets = product(a, b, c)
    triplets_sums = list(map(sum, triplets))

    for value in triplets_sums:
        if -value in d:
            quads_count += 1

    return quads_count


if __name__ == "__main__":
    lst_1 = [1, 4, 5, 6]
    lst_2 = [2, 3, 7, 8]
    lst_3 = [1, 4, 6, 10]
    lst_4 = [2, -4, -7, -9]
    print(check_sum_of_four(lst_1, lst_2, lst_3, lst_4))
