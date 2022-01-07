# -*- coding: utf-8 -*-
"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
    list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""

from typing import Generator


def fizzbuzz(n: int) -> Generator:
    map_table = {}
    n += 1
    for i in range(1, n):
        map_table[i] = i
    for i in range(3, n, 2):
        map_table[i] = "fizz"
    for i in range(5, n, 4):
        map_table[i] = "buzz"
    for i in range(15, n, 15):
        map_table[i] = "fizzbuzz"

    for _, value in map_table.items():
        yield str(value)


if __name__ == "__main__":
    print(list(fizzbuzz(32)))
    print()
