# Created by allex at 09.11.2021
# -*- coding: utf-8 -*-
"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from typing import Sequence
from math import sqrt


def check_fibonacci(data: Sequence[int]) -> bool:
    """Returns True is given sequence is Fibonacci Sequence. Returns False if otherwise"""

    # Try to normalise data to list
    data = list(data)

    # Check if sequence has elements
    if not data:
        return False

    # Single number check case
    if len(data) == 1:
        if data[0] == 0:
            return True
        if (sqrt(5 * (data[0] ** 2) - 4) % 1) == 0 or (sqrt(5 * (data[0] ** 2) + 4) % 1) == 0:
            return True
        else:
            return False

    # Divide sequence cases into len > 2 or less
    if len(data) > 2:
        # Check if first and second seq element is fib number, consider num == 0 case
        # Verification is based on Fibonacci numbers mathematical attribute
        if data[0] != 0:
            if not ((sqrt(5 * (data[0] ** 2) - 4) % 1) == 0 or (sqrt(5 * (data[0] ** 2) + 4) % 1) == 0):
                return False
        if data[1] != 0:
            if not ((sqrt(5 * (data[1] ** 2) - 4) % 1) == 0 or (sqrt(5 * (data[1] ** 2) + 4) % 1) == 0):
                return False

        # Check sequence itself
        for index, num in enumerate(data[2:], 2):
            if num != data[index - 1] + data[index - 2]:
                return False

        return True

    else:
        # Is data - start of the Fib sequence?
        if data == [0, 1]:
            return True
        else:
            # Is data - [0, 2] or similar?
            if data[0] == 0:
                return False
            else:
                # Is data[0] - fib number?
                if not ((sqrt(5 * (data[0] ** 2) - 4) % 1) == 0 or (sqrt(5 * (data[0] ** 2) + 4) % 1) == 0):
                    return False
                else:
                    # Get previous fib number
                    if data[0] == 1 and data[1] != 1:
                        prev_num = 1
                    else:
                        prev_num = int(data[0] / ((1 + sqrt(5)) / 2.0))

                    # Is data[1] - next fib number?
                    if data[1] == prev_num + data[0]:
                        return True
                    else:
                        return False


if __name__ == '__main__':
    print(check_fibonacci([0, 1, 4]))
