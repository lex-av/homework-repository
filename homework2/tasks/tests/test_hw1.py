# -*- coding: utf-8 -*-
from hw1.hw1 import get_longest_diverse_words


def test_longest_diverse_words():
    assert get_longest_diverse_words(r"tasks/tests/src_hw1_1.txt") == ['abcc', 'abbb', 'adcd']
