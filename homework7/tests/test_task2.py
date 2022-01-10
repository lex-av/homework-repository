# -*- coding: utf-8 -*-

import pytest

from homework7.pack_task2.module_task2 import backspace_compare

positive_tst_data = [
    ("ab#c", "ad#c", True),
    ("a##c", "#a#c", True),
    ("###ac", "#ac", True),
    ("a##c", "a###c", True),
]

negative_tst_data = [
    ("ab#c", "ad#bc", False),
    ("aa##c", "aa#c", False),
    ("###ac", "#aac", False),
    ("a#c", "d", False),
]


@pytest.mark.parametrize("first_str, second_str, output", positive_tst_data)
def test_positive_backspace_compare(first_str, second_str, output):
    assert backspace_compare(first_str, second_str) == output


@pytest.mark.parametrize("first_str, second_str, output", negative_tst_data)
def test_negative_backspace_compare(first_str, second_str, output):
    assert backspace_compare(first_str, second_str) == output
