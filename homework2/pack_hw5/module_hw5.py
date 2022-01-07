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
from typing import AnyStr, Generator, Sequence, TextIO, Union


def custom_range(iterable: Union[Sequence, TextIO], *args: Union[int, AnyStr]) -> Generator:
    """
    Behaves as extended range
    On top of range base functional:
    -iterates through strs by chars
    -iterates through strs by indexes
    -iterates through files by lines
    -iterates through collections by indexes
    -fully supports slices (by chars too)
    -works as generator
    """

    # Start, stop, step initialisation for slices
    args_count = len(args)
    stop = None
    start = None
    step = None

    if args_count == 1:
        stop = args[0]
    if args_count == 2:
        start = args[0]
        stop = args[1]
        if type(start) != type(stop):
            raise TypeError("Start and stop should be one type")
    if args_count == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if type(start) != type(stop):
            raise TypeError("Start and stop should be one type")

    if isinstance(step, str):
        raise TypeError("Wrong type for step parameter")

    # Container for slicing parameters
    slice_params = {"start": start, "stop": stop, "step": step}

    # Data container for types except str
    data = []

    # Building lists to iterate through
    if isinstance(iterable, TextIOWrapper):
        if isinstance(stop, str) or isinstance(start, str):
            raise TypeError("Start and stop for file obj should be int")

        for line in map(str.strip, iterable.readlines()):
            data.append(line)
        data_to_iterate = data[slice(*slice_params.values())]

    else:
        data = list(iterable)

        # Convert str-type start/stop back to int
        # Can give unexpected results with non unique chars in given str
        if isinstance(slice_params["start"], str) and isinstance(iterable, str):
            slice_params["start"] = iterable.find(slice_params["start"])
        if isinstance(slice_params["stop"], str) and isinstance(iterable, str):
            slice_params["stop"] = iterable.find(slice_params["stop"])

        data_to_iterate = data[slice(*slice_params.values())]

    for element in data_to_iterate:
        yield element


if __name__ == "__main__":
    import string

    a = custom_range(string.ascii_lowercase, "g", "a", -1)
    print()
