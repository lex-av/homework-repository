# -*- coding: utf-8 -*-
"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""

import re
from collections import namedtuple


def backspace_compare(first: str, second: str):
    """
    Returns True is two strings are equal when both are
    typed into empty text editors. # means a backspace character.
    """

    def eraser(input_str):
        """Function to delete all backspace and erased chars from original str"""
        input_str = input_str.lstrip("#")
        input_str_listed = [char for char in input_str]

        BackspaceIndexes = namedtuple("BackspaceIndexes", "start end")  # Holds #'s occurrences
        backspace_occurrences = [BackspaceIndexes._make([m.start(0), m.end(0)]) for m in re.finditer(r"#+", input_str)]

        pop_indexes = set()
        new_str_listed = []

        for occurrence in backspace_occurrences:
            # Calculate the zone, that should be erased
            backspace_count = occurrence.end - occurrence.start
            current_index = occurrence.end - 1
            left_border = occurrence.end - (2 * backspace_count) - 1

            # Calculate indexes in erase-zone
            while current_index >= 0 and current_index != left_border:
                pop_indexes.add(current_index)
                current_index -= 1

        # Build new str without symbols in erase-zones
        for index, _ in enumerate(input_str_listed):
            if index not in pop_indexes:
                new_str_listed.append(input_str_listed[index])

        return "".join(new_str_listed)

    return eraser(first) == eraser(second)


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    print(backspace_compare(s, t))

    s = "a##c"
    t = "#a#c"
    print(backspace_compare(s, t))

    s = "a##c"
    t = "########a#c"
    print(backspace_compare(s, t))

    print()
