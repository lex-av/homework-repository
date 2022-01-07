# -*- coding: utf-8 -*-

import os

import pytest

from homework2.pack_hw5.module_hw5 import custom_range

# Data for test_range_list
test_data_1 = [(["a", "b", "c"], ["a", "b", "c"]), ([1, 2, 3], [1, 2, 3]), ([], [])]

test_data_2 = [("abc", ["a", "b", "c"]), ([1, 2, 3], [1, 2, 3])]

test_data_3 = [
    ("abcdefgh", ["a", "h"], ["a", "b", "c", "d", "e", "f", "g"]),
    ("abcdefgh", ["a", "f"], ["a", "b", "c", "d", "e"]),
    ("abcdefgh", ["a", "f", 2], ["a", "c", "e"]),
    ("abcdefgh", [None, None, -1], ["h", "g", "f", "e", "d", "c", "b", "a"]),
]


@pytest.mark.parametrize("test_input, expected", test_data_1)
def test_custom_range_list(test_input, expected):
    assert list(custom_range(test_input)) == expected


@pytest.mark.parametrize("test_input, expected", test_data_2)
def test_custom_range_chars_list(test_input, expected):
    assert list(custom_range(test_input)) == expected


@pytest.mark.parametrize("test_input, test_pivots, expected", test_data_3)
def test_custom_range_chars_list_pivots(test_input, test_pivots, expected):
    assert list(custom_range(test_input, *test_pivots)) == expected


def test_custom_range_file():
    path_to_hws = os.getcwd()
    file_data = open(path_to_hws + "/homework2/tests/test_data/src_hw5_1.txt")
    assert list(custom_range(file_data)) == ["abcc", "abbb", "adcd", "adcde"]
    file_data.close()
