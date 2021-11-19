# -*- coding: utf-8 -*-
"""
    Here's a not very efficient calculation function that calculates something important:

    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        Some weird voodoo magic calculations
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))
    Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
    Calculation time should not take more than a minute. Use functional capabilities
    of multiprocessing module. You are not allowed to modify slow_calculate function.
"""

import hashlib
import random
import struct
import time
from multiprocessing.pool import ThreadPool as Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def mul(value):
    return value * 10


if __name__ == '__main__':
    max_val = 500
    nums = [i for i in range(max_val)]
    with Pool(40) as pl:
        output = pl.map(slow_calculate, nums)

    print("ready")
