# -*- coding: utf-8 -*-

import pytest

from ..pack_hw5.module_hw5 import custom_range

# Data for test_range_list
test_data_1 = [
    (['a', 'b', 'c'], ['a', 'b', 'c']),
    ([1, 2, 3], [1, 2, 3]),
    ([], [])
]


@pytest.mark.parametrize("test_input, expected", test_data_1)
def test_custom_range_list(test_input, expected):
    assert custom_range(test_input) == expected
