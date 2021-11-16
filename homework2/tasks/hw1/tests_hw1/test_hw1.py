# -*- coding: utf-8 -*-
from hw1.hw1 import *


def test_longest_diverse_words_1():
    """Testing order of words"""
    assert get_longest_diverse_words(r"tasks/tests/src_hw1_1.txt") == ['abbb', 'abcc', 'adcd', 'adcde']


def test_longest_diverse_words_2():
    """Testing order of words and slicing"""
    assert get_longest_diverse_words(r"tasks/tests/src_hw1_2.txt") == ['ad', 'ad',
                                                                       'am', 'am',
                                                                       'ag', 'ag',
                                                                       'abbb', 'abcc',
                                                                       'adcd', 'adcde']


def test_rarest_symbol_1():
    """Testing rarest symbol counting"""
    assert get_rarest_char(r"tasks/tests/src_hw1_3.txt") == '.'


def test_rarest_symbol_2():
    """Testing rarest symbol counting, but for special symbol"""
    assert get_rarest_char(r"tasks/tests/src_hw1_4.txt") == '\n'


def test_count_punctuation_chars():
    """Testing punctuation chars counting"""
    assert count_punctuation_chars(r"tasks/tests/src_hw1_5.txt") == 4
    assert count_punctuation_chars(r"tasks/tests/src_hw1_6.txt") == 0
    # Function need to ignore spaces
    assert count_punctuation_chars(r"tasks/tests/src_hw1_7.txt") == 11
