# -*- coding: utf-8 -*-

from ..pack_task3.module_task3 import tic_tac_toe_checker

board_win_x = [["x", "x", "x"], ["-", "x", "o"], ["x", "o", "x"]]
board_win_x_diagonal = [["x", "o", "-"], ["-", "x", "o"], ["x", "o", "x"]]
board_win_o = [["-", "-", "o"], ["o", "o", "o"], ["x", "o", "x"]]
board_draw = [["o", "o", "o"], ["-", "x", "o"], ["x", "x", "x"]]
board_unfinished = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]


def test_positive_win_x():
    assert tic_tac_toe_checker(board_win_x) == "x wins!"


def test_positive_win_x_diagonal():
    assert tic_tac_toe_checker(board_win_x_diagonal) == "x wins!"


def test_positive_win_o():
    assert tic_tac_toe_checker(board_win_o) == "o wins!"


def test_positive_draw():
    assert tic_tac_toe_checker(board_draw) == "draw!"


def test_positive_unfinished():
    assert tic_tac_toe_checker(board_unfinished) == "unfinished!"
