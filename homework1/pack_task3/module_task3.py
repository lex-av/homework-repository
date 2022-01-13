# -*- coding: utf-8 -*-
"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
import os
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    Return maximum and minimum int from file. Each int
    should be on a new line
    """

    min_value = float("inf")
    max_value = -float("inf")
    with open(file_name) as fi:
        for line in fi:
            current_value = int(line.strip())

            if current_value < min_value:
                min_value = current_value

            if current_value > max_value:
                max_value = current_value

    return min_value, max_value


if __name__ == "__main__":
    print(os.getcwd())
