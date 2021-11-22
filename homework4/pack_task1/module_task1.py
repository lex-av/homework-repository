"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
Write a test for that function using pytest library.
You should create files required for the testing inside the test run and remove them after the test run.
(Opposite to previous homeworks when you used files created manually before the test.)
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - tests do a cleanup and remove remove files generated by tests
You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.
* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""


import os


def read_magic_number(path: str) -> bool:
    """
    If first line is a number return true if number in an interval [1, 3)
    and false otherwise.
    """

    try:
        src = open(path)
    except Exception:
        raise ValueError("Wrong file path")

    first_line = src.readline()
    num = int(first_line)

    if 1 <= num < 3:
        src.close()
        return True
    src.close()
    return False


if __name__ == '__main__':
    print(os.path.abspath('text_file_example.txt'))
    # print(read_magic_number('text1_file_example.txt'))