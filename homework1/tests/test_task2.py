import pytest

from ..pack_task2.module_task2 import check_fibonacci

test_data_positive_single_nums_case = [[0], [1], [2], [3]]

test_data_positive_sequence_case = [[0, 1], [1, 1], [1, 2], [13, 21]]

test_data_positive_long_sequence_case = [
    [0, 1, 1],
    [0, 1, 1, 2],
    [3, 5, 8, 13, 21, 34],
    [0, 1, 1, 2, 3, 5, 8],
    [13, 21, 34],
]

test_data_false_sequence_case = [
    [0, 1, 4],
    [4, 6, 7, 2],
    [3, 5, 13, 13, 21, 34],
    [0, 1, 1, 0, 3, 5, 8],
    [13, 34, 21],
]


@pytest.mark.parametrize("input_value", test_data_positive_single_nums_case)
def test_single_nums_case(input_value):
    """Testing that single nums of Fibonacci sequence give True"""
    assert check_fibonacci(input_value)


@pytest.mark.parametrize("input_value", test_data_positive_sequence_case)
def test_sequence_case(input_value):
    """Testing that subsequences of Fibonacci sequence with len() < 3 give True"""
    assert check_fibonacci(input_value)


@pytest.mark.parametrize("input_value", test_data_positive_long_sequence_case)
def test_long_sequence_case(input_value):
    """Testing that long subsequences of Fibonacci sequence with len() < 3 give True"""
    assert check_fibonacci(input_value)


@pytest.mark.parametrize("input_value", test_data_false_sequence_case)
def test_wrong_sequence_case(input_value):
    """Testing that wrong subsequences of Fibonacci sequence with len() < 3 give True"""
    assert not check_fibonacci(input_value)
