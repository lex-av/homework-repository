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


from multiprocessing.pool import Pool

from homework3.pack_task2.worker import slow_calculate


def launch(iterable):
    with Pool(48) as p:
        output = p.map(slow_calculate, iterable)

    return output


if __name__ == "__main__":
    pass