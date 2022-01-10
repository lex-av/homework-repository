# -*- coding: utf-8 -*-

import pytest

from homework4.pack_task5.module_task5 import fizzbuzz

test_data = [
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
]


@pytest.mark.parametrize("input, expected", test_data)
def test_fizz_buzz(input, expected):
    assert list(fizzbuzz(input)) == expected
