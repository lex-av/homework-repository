# -*- coding: utf-8 -*-
"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""


from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Returns a list of fizzbuzz numbers

    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(3)
    ['1', '2', 'Fizz']
    """

    def fizzbuzz_replacer(num):

        if num % 15 == 0:
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"

        return num

    fizzbuzz_numbers = list(map(fizzbuzz_replacer, list(i for i in range(1, n + 1))))
    fizzbuzz_numbers = list(map(str, fizzbuzz_numbers))

    return fizzbuzz_numbers


if __name__ == "__main__":
    pass
