# Created by allex at 11.11.2021
# -*- coding: utf-8 -*-
"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""


from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Use naive approach to find triplets and then
    find quadruples, using search (standard or binary for example)"""

    quads = []
    quads_count = 0

    for a_i in a:
        for b_i in b:
            for c_i in c:
                triplet_sum = a_i + b_i + c_i
                if -triplet_sum in d:
                    quads_count += 1
                    quads += [a_i, b_i, c_i, -triplet_sum]

    return quads


lst_1 = [1, 4, 5, 6]
lst_2 = [2, 3, 7, 8]
lst_3 = [1, 4, 6, 10]
lst_4 = [2, -4, -7, -9]
print(sum(check_sum_of_four(lst_1, lst_2, lst_3, lst_4)))
