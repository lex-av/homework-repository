import pytest

from ..pack_task5.module_task5 import find_maximal_subarray_sum

test_data_positive = [
    ([-1, 0, 0, 10, 25, 25, 25], 1, 25),
    ([-1, 0, 0, 10, 25, 25, 25], 2, 50),
    ([-1, 0, 0, 10, 25, 25, 25], 3, 75),
    ([-1, 0, 0, 10, 25, 25, 25], 4, 85),
    ([-1, 0, 0, 10, 25, 25, 25], 7, 85),
]


@pytest.mark.parametrize("input_value_1, input_value_2, expected_value", test_data_positive)
def test_positive_case(input_value_1, input_value_2, expected_value):
    assert find_maximal_subarray_sum(input_value_1, input_value_2) == expected_value
