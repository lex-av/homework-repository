# -*- coding: utf-8 -*-
"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""


from typing import Callable


def cache(func: Callable) -> Callable:
    buffer = {}

    def wrapper(*args):
        if str(args) not in buffer:
            buffer[str(args)] = func(*args)
        return buffer[str(args)]
    return wrapper


def functional(a, b) -> int:
    return (a ** b) ** 2


if __name__ == '__main__':
    cache_func = cache(functional)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
