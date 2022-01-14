# -*- coding: utf-8 -*-

from ..pack_task2.module_task2 import suppressor, suppressor_gen


def test_positive_context_manager_class():
    with suppressor(IndexError):
        [][2]


def test_positive_context_manager_generator():
    with suppressor_gen(IndexError):
        [][2]
