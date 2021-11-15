# -*- coding: utf-8 -*-
from hw1.hw1 import *


def test_longest_diverse_words():
    assert get_longest_diverse_words(r"homework2\tests\src_hw1_1") == ['abcc', 'abbb', 'adcd']
