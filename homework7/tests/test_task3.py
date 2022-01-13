# -*- coding: utf-8 -*-

import pytest

from homework7.pack_task3.module_task3 import tic_tac_toe_checker

test_data = [
    ([["x", "x", "x"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
    ([["x", "o", "-"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
    ([["-", "-", "o"], ["o", "o", "o"], ["x", "o", "x"]], "o wins!"),
    ([["o", "o", "o"], ["-", "x", "o"], ["x", "x", "x"]], "draw!"),
    ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
]


@pytest.mark.parametrize("board, expected", test_data)
def test_positive_win_x(board, expected):
    assert tic_tac_toe_checker(board) == expected
