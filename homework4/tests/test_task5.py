# -*- coding: utf-8 -*-

import pytest

from homework4.pack_task5.module_task5 import fizzbuzz

test_data = [
    (3, ["1", "2", "fizz"]),
    (5, ["1", "2", "fizz", "4", "buzz"]),
    (15, ["1", "2", "fizz", "4", "buzz", "6", "fizz", "8", "buzz", "10", "fizz", "12", "buzz", "14", "fizzbuzz"]),
]


@pytest.mark.parametrize("input, expected", test_data)
def test_fizz_buzz(input, expected):
    assert list(fizzbuzz(input)) == expected
