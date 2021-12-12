# Created by allex at 09.11.2021
# -*- coding: utf-8 -*-
"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from math import sqrt
from typing import Sequence


def _fib_gen(value_1=0, value_2=1, max_len=2):
    """
    A fibonacci numbers finite generator
    Starting values should be both following
    fib nums
    """

    curr_len = 0
    while curr_len < max_len:
        yield value_1
        next_val = value_1 + value_2
        value_1 = value_2
        value_2 = next_val
        curr_len += 1


def is_fib_num(num):
    """Checks in num is a fib-num"""
    if (sqrt(5 * (num ** 2) + 4) % 1) == 0 or (sqrt(5 * (num ** 2) - 4) % 1) == 0:
        return True
    return False


def get_prev_fib_num(num):
    """Returns previous fib number of given"""
    return round(num / ((1 + sqrt(5)) / 2.0))


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checks fib sequence using generator-magic"""

    if (len(data) == 1 and data[0] in (0, 1)) or not data:
        return True

    # If just one number, get previous fib num and shuffle generator
    # 1 step further
    if len(data) == 1:
        if not is_fib_num(data[0]):
            return False
        else:
            val_2 = data[0]
            val_1 = get_prev_fib_num(val_2)
            fib_nums_gen = _fib_gen(val_1, val_2, len(data))
            next(fib_nums_gen)
    else:
        # If more than one number, use generator as it is
        if not is_fib_num(data[0]) and not is_fib_num(data[1]):
            return False
        else:
            val_1 = data[0]
            val_2 = data[1]
            fib_nums_gen = _fib_gen(val_1, val_2, len(data))

    for seq_value, gen_value in zip(data, fib_nums_gen):
        if seq_value != gen_value:
            return False

    return True


if __name__ == "__main__":

    print()
    print(check_fibonacci([3]))
    print(check_fibonacci([2]))
    print()
