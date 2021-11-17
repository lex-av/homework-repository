# -*- coding: utf-8 -*-
"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


from io import TextIOWrapper
from typing import Any, AnyStr, List, Union


def custom_range(iterable: Any, *args: Union[int, AnyStr]) -> List:
    """Converts given iterable to [optionally sliced] list.

    Slicing pivots for file object corresponds to character
    position in file and should be integers.
    Slicing pivots for tuple and list works normally and
    should be integers.
    Slicing pivots for string may be str or int. So,
    slicing by index and element is available.

    Dict will be converted to list of keys

    Set wil be converted to list"""

    # If file object given
    if isinstance(iterable, TextIOWrapper):
        iterable = list(map(str.strip, iterable.readlines()))

        if args:
            return iterable[args[0]:args[1]:args[2]]
        else:
            return iterable

    # Str object given
    elif isinstance(iterable, str):
        elems_to_indexes = dict(zip(list(iterable), range(len(iterable))))
        iterable = list(iterable)

        if args:
            # Slicing for str args
            if isinstance(args[0], str) and isinstance(args[0], str) and isinstance(args[0], str):
                return iterable[elems_to_indexes[args[0]]:elems_to_indexes[args[1]]:elems_to_indexes[args[2]]]
            # Slicing for int args
            elif isinstance(args[0], int) and isinstance(args[0], int) and isinstance(args[0], int):
                return iterable[args[0]:args[1]:args[2]]
        else:
            raise Exception("Got wrong args for slicing")

    # Tuple/list/Set/Iterator object given
    else:
        iterable = list(iterable)
        if args:
            return iterable[args[0]:args[1]:args[2]]
        else:
            return iterable


if __name__ == '__main__':
    import string
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
