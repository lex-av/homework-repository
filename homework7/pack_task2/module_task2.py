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

??????????????????????????????????????????????????

-я уже второй раз об этом думаю, поэтому пораб бы спросить:
если я внутри, например, разрабатываемой функции определяю
вспомогательную функцию, нужно ли мне её отдельно тестировать?
Если это так, то каким образом это лучше сделать? Обращаться через
dot notation?

- Я уже второй раз провожу этот мув со вспомогательной функцией
внутри основной. Верно ли я использую этот подход. Правильно ли
это в принципе? В чём, может, ошибся?


"""

from typing import Generator


def backspace_compare(first: str, second: str) -> bool:
    """Using generator logic to transform"""

    def erasing_generator(reversed_str: str) -> Generator:
        """Yields input reversed_str char by char"""

        # Accumulator for #
        sharp_counter = 0

        for char in list(reversed_str):
            if char == "#":
                sharp_counter += 1

            if char != "#" and sharp_counter == 0:
                yield char
            elif sharp_counter != 0 and char != "#":
                sharp_counter -= 1

    return "".join(erasing_generator(first[::-1])) == "".join(erasing_generator(second[::-1]))


if __name__ == "__main__":
    pass
