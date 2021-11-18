# -*- coding: utf-8 -*-

from ..pack_task1.module_task1 import cache


# Decorator to count tested function calls
def count_calls(func):

    def wrapper(*args, **kwargs):
        wrapper.calls_count += 1
        func(*args, **kwargs)

    wrapper.calls_count = 0
    return wrapper


@cache()
@count_calls
def example_func():
    return 5


@cache
def add_func(a, b):
    return a + b


def test_example_func():

    ...


def test_func_with_args():
    ...
