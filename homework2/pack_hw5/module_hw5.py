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
from typing import Any, List


def custom_range(iterable: Any, *args: int) -> List:
    if isinstance(iterable, TextIOWrapper):
        iterable = list(map(str.strip, iterable.readlines()))
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
