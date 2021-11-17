# -*- coding: utf-8 -*-
from ..pack_hw1.module_hw1 import (count_punctuation_chars,
                                   get_longest_diverse_words, get_rarest_char)


def test_longest_diverse_words_1():
    """Testing order of words"""
    assert get_longest_diverse_words(r"homework2/tests/src_hw1_1.txt") == ['abbb', 'abcc', 'adcd', 'adcde']


def test_longest_diverse_words_2():
    """Testing order of words and slicing"""
    assert get_longest_diverse_words(r"homework2/tests/src_hw1_2.txt") == ['ad', 'ad',
                                                                           'am', 'am',
                                                                           'ag', 'ag',
                                                                           'abbb', 'abcc',
                                                                           'adcd', 'adcde']


def test_rarest_symbol_1():
    """Testing rarest symbol counting"""
    assert get_rarest_char(r"homework2/tests/src_hw1_3.txt") == '.'


def test_rarest_symbol_2():
    """Testing rarest symbol counting, but for special symbol"""
    assert get_rarest_char(r"homework2/tests/src_hw1_4.txt") == '\n'


def test_count_punctuation_chars():
    """Testing punctuation chars counting"""
    assert count_punctuation_chars(r"homework2/tests/src_hw1_5.txt") == 4
    assert count_punctuation_chars(r"homework2/tests/src_hw1_6.txt") == 0
    # Function need to ignore spaces
    assert count_punctuation_chars(r"homework2/tests/src_hw1_7.txt") == 11
