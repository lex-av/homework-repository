# -*- coding: utf-8 -*-

import os

import pytest

from homework2.pack_hw1.module_hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

test_data_diverse_words = [
    ("/homework2/tests/test_data/src_hw1_1.txt", ["abbb", "abcc", "adcd", "adcde"]),
    ("/homework2/tests/test_data/src_hw1_2.txt", ["ad", "ad", "am", "am", "ag", "ag", "abbb", "abcc", "adcd", "adcde"]),
]

test_data_rarest_symbols = [
    ("/homework2/tests/test_data/src_hw1_3.txt", "."),
    ("/homework2/tests/test_data/src_hw1_4.txt", "\n"),
]

test_data_count_punctuation = [
    ("/homework2/tests/test_data/src_hw1_5.txt", 4),
    ("/homework2/tests/test_data/src_hw1_6.txt", 0),
    ("/homework2/tests/test_data/src_hw1_7.txt", 11),
]


@pytest.mark.parametrize("test_file_path, expected", test_data_diverse_words)
def test_longest_diverse_words_1(test_file_path, expected):
    """Testing order of words"""
    path_to_hws = os.getcwd()
    assert get_longest_diverse_words(path_to_hws + test_file_path) == expected


@pytest.mark.parametrize("test_file_path, expected", test_data_rarest_symbols)
def test_rarest_symbol_1(test_file_path, expected):
    """Testing rarest symbol counting"""
    path_to_hws = os.getcwd()
    assert get_rarest_char(path_to_hws + test_file_path) == expected


@pytest.mark.parametrize("test_file_path, expected", test_data_count_punctuation)
def test_count_punctuation_chars(test_file_path, expected):
    """Testing punctuation chars counting"""
    path_to_hws = os.getcwd()

    assert count_punctuation_chars(path_to_hws + test_file_path) == expected


def test_count_non_ascii():
    """Testing non ascii chars counting"""
    path_to_hws = os.getcwd()

    assert count_non_ascii_chars(path_to_hws + "/homework2/tests/test_data/src_hw1_8.txt") == 15


def test_count_most_common_non_ascii():
    """Testing most common non ascii chars counting"""
    path_to_hws = os.getcwd()

    assert get_most_common_non_ascii_char(path_to_hws + "/homework2/tests/test_data/src_hw1_8.txt") == "\u00f6"
