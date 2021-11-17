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
from typing import AnyStr, List, Sequence, Union


def custom_range(iterable: Sequence,
                 start: Union[int, AnyStr] = None,
                 stop: Union[int, AnyStr] = None,
                 step: int = None) -> List:
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
        return iterable[start:stop:step]

    # Str object given
    if isinstance(iterable, str):
        elems_to_indexes = dict(zip(list(iterable), range(len(iterable))))
        elems_to_indexes[None] = None
        iterable = list(iterable)

        if isinstance(start, str) or start is None:
            return iterable[elems_to_indexes[start]:elems_to_indexes[stop]:step]
        elif isinstance(start, int) or start is None:
            return iterable[start:stop:step]
        else:
            raise Exception("Got wrong args for slicing")

    # Tuple/list/Set/Iterator object given
    else:
        iterable = list(iterable)

        if isinstance(start, int) or start is None:
            return iterable[start:stop:step]
        else:
            raise Exception("Got wrong args for slicing")


if __name__ == '__main__':
    import string
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
