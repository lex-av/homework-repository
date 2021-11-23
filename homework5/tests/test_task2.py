# -*- coding: utf-8 -*-

from ..pack_task2.module_task2 import custom_sum


def test_parameters_capture_decorator_func_doc():
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_parameters_capture_decorator_func_name():
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__name__ == "custom_sum"
