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

    fizz_buzz_lst = []
    n += 1

    for num in range(1, n):
        fizz_buzz_lst.append(num)
    for num in range(3, n, 3):
        fizz_buzz_lst[num - 1] = "Fizz"
    for num in range(5, n, 5):
        fizz_buzz_lst[num - 1] = "Buzz"
    for num in range(15, n, 15):
        fizz_buzz_lst[num - 1] = "FizzBuzz"

    for value in fizz_buzz_lst:
        yield str(value)


if __name__ == "__main__":
    print(list(fizzbuzz(32)))
    print()
