# -*- coding: utf-8 -*-
"""In previous homework task 4, you wrote a cache function that remembers other function
output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""


def cache(times=3):
    def outer_decorator(func):
        cached_values = {}
        outer_times = times

        def wrapper(*args):
            times = outer_times

            if times != 0:
                if args in cached_values:
                    times -= 1
                    return cached_values[args]
                else:
                    cached_values[args] = func(*args)
                    return cached_values[args]

            cached_values[args] = func(*args)
            return cached_values[args]

        return wrapper

    return outer_decorator
