# -*- coding: utf-8 -*-
"""
Given a Tic-Tac-Toe 3x3 some_board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If some_board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks:
    If there is "x" winner, returns "x wins!"
    If there is "o" winner, returns "o wins!"
    If there is a draw, returns "draw!"
    If some_board is unfinished, returns "unfinished!"

    Example input:
        [["-", "-", "o"],
         ["-", "x", "o"],
         ["x", "o", "x"]]
    """

    def is_winning(dot):
        """
        Checks if one of the players have a winning combo.
        dot is either x or o
        """

        win_condition = [dot, dot, dot]

        for line in board:
            if line == win_condition:
                return True

        for row in list(map(list, zip(*board))):
            if row == win_condition:
                return True

        # Diagonal
        if [r[i] for i, r in enumerate(board)] == win_condition:
            return True

        # Opposite diagonal
        if [r[-i - 1] for i, r in enumerate(board)] == win_condition:
            return True

        return False

    def is_empty_dots():
        return any("-" in line for line in board)

    # End conditions:
    if is_winning("x") and not is_winning("o"):
        return "x wins!"

    if is_winning("o") and not is_winning("x"):
        return "x wins!"

    if is_winning("o") and is_winning("x"):
        return "draw"

    if not is_winning("o") and not is_winning("x") and is_empty_dots():
        return "unfinished!"


if __name__ == "__main__":
    some_board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    print(tic_tac_toe_checker(some_board))
    print()
