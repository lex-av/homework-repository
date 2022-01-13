import pytest

from ..pack_calc.module_calc import check_power_of_2

test_data_positive = [2, 32, 64, 65536]

test_data_negative = [0, 12, 10]


@pytest.mark.parametrize("input_value", test_data_positive)
def test_positive_case(input_value):
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(input_value)


@pytest.mark.parametrize("input_value", test_data_negative)
def test_negative_case(input_value):
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(input_value)
