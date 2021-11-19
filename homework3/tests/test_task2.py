# -*- coding: utf-8 -*-

import time

from ..pack_task2.module_task2 import multiprocess_calculate

data = [i for i in range(500)]


def timing_decorator(func):

    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_stop = time.time()
        return time_stop - time_start
    return wrapper


slow_calculate = timing_decorator(multiprocess_calculate)


def test_one_minute():
    assert slow_calculate(data) < 60
