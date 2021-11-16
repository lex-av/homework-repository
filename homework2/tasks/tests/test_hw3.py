# -*- coding: utf-8 -*-
from hw3.hw3 import combinations


def test_combinations():
    """Testing cases"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
    assert combinations([1, 2], [3, 4], [5, 6]) == [[1, 3, 5], [1, 3, 6], [1, 4, 5],
                                                    [1, 4, 6], [2, 3, 5], [2, 3, 6],
                                                    [2, 4, 5], [2, 4, 6]]
    assert combinations([1, 2], [3, 4], [5, 6], [7, 8]) == [[1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 6, 7],
                                                            [1, 3, 6, 8], [1, 4, 5, 7], [1, 4, 5, 8],
                                                            [1, 4, 6, 7], [1, 4, 6, 8], [2, 3, 5, 7],
                                                            [2, 3, 5, 8], [2, 3, 6, 7], [2, 3, 6, 8],
                                                            [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 6, 7],
                                                            [2, 4, 6, 8]]
