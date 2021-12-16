# -*- coding: utf-8 -*-

"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
with supressor(IndexError):
...    [][2]
"""

from contextlib import contextmanager


class ExceptionSuppressor:
    """Context manager to suppress given Exception"""

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context")
        return exc_type == self.exception


def suppressor(exception_name):
    return ExceptionSuppressor(exception_name)


@contextmanager
def suppressor_gen(exception):
    try:
        yield
    except exception:
        pass


if __name__ == "__main__":
    with suppressor_gen(IndexError):
        [][2]

    print()
