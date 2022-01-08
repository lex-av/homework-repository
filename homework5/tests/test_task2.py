# -*- coding: utf-8 -*-

from homework5.pack_task2.module_task2 import custom_sum


def test_deep_wraps_func_doc():
    custom_sum(1, 2, 3, 4)
    assert (
        custom_sum.__doc__ == "This function can sum any objects which have __add___"
        and custom_sum.__name__ == "custom_sum"
    )
