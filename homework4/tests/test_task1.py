# -*- coding: utf-8 -*-


import pytest

from ..pack_task1.module_task1 import read_magic_number

data_positive_case = [
    ('1', True),
    ('2', True)
]

data_negative_case = [
    ('0', False),
    ('3', False)
]


@pytest.mark.parametrize("live_value, expected", data_positive_case)
def test_positive_case_read_magic_number(tmpdir, live_value, expected):
    positive_case_file = tmpdir.join('file.txt')
    positive_case_file.write(live_value)
    positive_result = read_magic_number(positive_case_file)

    assert positive_result == expected


@pytest.mark.parametrize("live_value, expected", data_negative_case)
def test_negative_case_read_magic_number(tmpdir, live_value, expected):
    negative_case_file = tmpdir.join('file.txt')
    negative_case_file.write(live_value)
    negative_result = read_magic_number(negative_case_file)

    assert negative_result == expected


def test_negative_case_read_magic_number_wrong_path():
    path = "C:/non_existent_file.txt"

    with pytest.raises(ValueError):
        read_magic_number(path)


@pytest.mark.parametrize("wrong_input", [' ', '1 2', '\n'])
def test_negative_case_read_magic_number_wrong_line(tmpdir, wrong_input):
    negative_case_file = tmpdir.join('file.txt')
    negative_case_file.write(wrong_input)

    with pytest.raises(ValueError):
        read_magic_number(negative_case_file)
