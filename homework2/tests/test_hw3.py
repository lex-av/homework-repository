# -*- coding: utf-8 -*-

import pytest

from homework2.pack_hw3.module_hw3 import combinations

expected_list_1 = [[1, 3], [1, 4], [2, 3], [2, 4]]
expected_list_2 = [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
expected_list_3 = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
expected_list_4 = [
    [1, 3, 5, 7],
    [1, 3, 5, 8],
    [1, 3, 6, 7],
    [1, 3, 6, 8],
    [1, 4, 5, 7],
    [1, 4, 5, 8],
    [1, 4, 6, 7],
    [1, 4, 6, 8],
    [2, 3, 5, 7],
    [2, 3, 5, 8],
    [2, 3, 6, 7],
    [2, 3, 6, 8],
    [2, 4, 5, 7],
    [2, 4, 5, 8],
    [2, 4, 6, 7],
    [2, 4, 6, 8],
]

test_data = [
    ([[1, 2], [3, 4]], expected_list_1),
    ([[1, 2, 3], [4, 5, 6]], expected_list_2),
    ([[1, 2], [3, 4], [5, 6]], expected_list_3),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], expected_list_4),
]


@pytest.mark.parametrize("args, expected", test_data)
def test_combinations(args, expected):
    """Testing cases"""

    assert combinations(*args) == expected
