# Created by allex at 09.11.2021
# -*- coding: utf-8 -*-
"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from math import sqrt
from typing import List


def is_fib_num(num):
    """Checks in num is a fib-num"""
    if (sqrt(5 * (num ** 2) + 4) % 1) == 0 or (sqrt(5 * (num ** 2) - 4) % 1) == 0:
        return True
    return False


def get_prev_fib_num(num):
    """Returns previous fib number of given"""
    return round(num / ((1 + sqrt(5)) / 2.0))


def check_fibonacci(data: List[int]) -> bool:
    """Checks fib sequence using generator-magic"""

    if not data:
        return False

    if len(data) == 1:  # 1-num sequence cases
        return is_fib_num(data[0])

    if data == [0, 1] or data == [1, 1] or data == [0, 1, 1]:  # Cut simple cases from loop here
        return True

    starting_pivot = 2
    if len(data) > 3 and data[:3] == [0, 1, 1]:  # Special check for seqs, that start from 0, 1, 1
        starting_pivot = 3
    else:
        data.insert(0, get_prev_fib_num(data[0]))

    for index, num in enumerate(data[starting_pivot:], starting_pivot):
        if num != data[index - 1] + data[index - 2]:
            return False

    return True


if __name__ == "__main__":
    print()
    print(check_fibonacci([3]))
    print(check_fibonacci([2]))
    print()
