# -*- coding: utf-8 -*-
"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""


import re
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Using regex to find words, then sorting by two parameters to
    find 10 longest words consisting from largest amount of unique symbols
    """

    # Regex pattern for words search and words accumulator
    pattern = r"\b\w+\b"
    words = []

    # Read all words line by line using regEx
    with open(file_path) as fi:
        for line in fi:
            line_words = re.findall(pattern, line.strip())
            if line_words:
                words += line_words

    # Sort words by  1) length and  2) unique numbers and 3) get 10 last
    words_len_sorted = sorted(words, key=lambda w: (len(w), len(set(w))))[-10:]

    return words_len_sorted


def get_rarest_char(file_path: str) -> str:
    """
    For line in file extend accumulator by
    chars in line. Then Counter to get
    rarest char
    """

    # Words accumulator
    words = []

    # Read all chars in file lines
    with open(file_path) as fi:
        for line in fi:
            if line:
                words.extend(line)

    rarest_symbol = Counter(words).most_common()[-1][0]

    return rarest_symbol


def count_punctuation_chars(file_path: str) -> int:
    """Using regex to find chars, Counter to count rarest"""

    # Regex pattern for chars search and chars accumulator
    pattern = r"[^a-zA-Z0-9_\\ ]{1}"
    p_chars = []

    # Read all p_chars line by line using regEx
    with open(file_path) as fi:
        for line in fi:
            line_p_chars = re.findall(pattern, line.strip())
            if line_p_chars:
                p_chars += line_p_chars

    return len(p_chars)


def count_non_ascii_chars(file_path: str) -> int:
    """Search for non-ascii chars"""

    # Regex pattern
    pattern = r"[\u0080-\uFFFF]"

    # fi = open(file_path, encoding="unicode-escape")
    # chars = re.findall(pattern, fi.read())
    # fi.close()

    acc = []
    with open(file_path, encoding="unicode-escape") as src:
        """
        Used that clumsy logic here for a reason:
        File is probably broken at some potion(s)
        I could not catch the exception in for loop,
        so used while True with next() method
        worked great
        """

        while True:
            try:
                try:
                    line = next(src)
                    line_chars = re.findall(pattern, line)
                    acc.extend(line_chars)

                except StopIteration:
                    break  # regular loop exit on stop iteration

            except UnicodeDecodeError:
                pass  # skipping damaged sections

    return len(acc)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Search for most common non-ascii chars"""

    # Regex pattern
    pattern = r"[\u0080-\uFFFF]"

    # fi = open(file_path, encoding="unicode-escape")
    # chars = re.findall(pattern, fi.read())
    # fi.close()

    acc = []
    with open(file_path, encoding="unicode-escape") as src:
        """
        Used that clumsy logic here for a reason:
        File is probably broken at some potion(s)
        I could not catch the exception in for loop,
        so used while True with next() method
        worked great
        """

        while True:
            try:
                try:
                    line = next(src)
                    line_chars = re.findall(pattern, line)
                    acc.extend(line_chars)

                except StopIteration:
                    break  # regular loop exit on stop iteration

            except UnicodeDecodeError:
                pass  # skipping damaged sections

    rarest_symbol = Counter(acc).most_common()[0][0]

    return rarest_symbol


if __name__ == "__main__":

    a = count_non_ascii_chars("data.txt")
    b = get_most_common_non_ascii_char("data.txt")
    print()
