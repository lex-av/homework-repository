# -*- coding: utf-8 -*-

import time

from homework3.pack_task2.module_task2 import launch_slow_calculate

data = [i for i in range(500)]


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_stop = time.time()
        return time_stop - time_start

    return wrapper


def test_one_minute():
    slow_calculate = timing_decorator(launch_slow_calculate)
    assert slow_calculate(data) < 60
