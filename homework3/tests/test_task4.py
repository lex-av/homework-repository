# -*- coding: utf-8 -*-

import pytest

from ..pack_task4.module_task4 import is_armstrong

test_data = [
    (0, True),
    (1, True),
    (153, True),
    (-1, False),
    (22, False),
    (-110, False)
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_is_armstrong(test_input, expected):
    assert is_armstrong(test_input) == expected
