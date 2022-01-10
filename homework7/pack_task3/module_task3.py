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

    def _transpose(board: List[List]) -> List[List]:
        """Returns board columns"""
        return list(map(list, zip(*board)))

    def _diagonal(board: List[List]) -> List[List]:
        return [r[i] for i, r in enumerate(board)]

    def _opposite_diagonal(board: List[List]) -> List[List]:
        return [r[-i - 1] for i, r in enumerate(board)]

    def is_winning(dot: str) -> bool:
        """
        Checks if one of the players have a winning combo.
        dot is either x or o
        """

        win_condition = [dot, dot, dot]

        if any(row == win_condition for row in board):
            return True

        if any(row == win_condition for row in _transpose(board)):
            return True

        if _diagonal(board) == win_condition:
            return True

        if _opposite_diagonal(board) == win_condition:
            return True

        return False

    def is_empty_dots():
        return any("-" in line for line in board)

    # End conditions:
    if is_winning("x") and not is_winning("o"):
        return "x wins!"

    if is_winning("o") and not is_winning("x"):
        return "o wins!"

    if is_winning("o") and is_winning("x"):
        return "draw!"

    if not is_winning("o") and not is_winning("x") and is_empty_dots():
        return "unfinished!"


if __name__ == "__main__":
    pass
