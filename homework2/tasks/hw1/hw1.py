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
    """Using regex to find words, then sorting and set"""

    # Regex pattern for words search and words accumulator
    pattern = r"\b\w+\b"
    words = []

    # Read all words line by line using regEx
    with open(file_path) as fi:
        for line in fi:
            line_words = re.findall(pattern, line.strip())
            if line_words:
                words += re.findall(pattern, line.strip())

    # Sort words by  1) length and  2) unique numbers and get 10 last
    words_len_sorted = sorted(words, key=lambda w: (len(w), len(set(w))))[-9:]

    return words_len_sorted


def get_rarest_char(file_path: str) -> str:
    """Using regex to find words, then collections.Counter"""

    # Words accumulator
    words = ""

    # Read all words line by line using regEx
    with open(file_path) as fi:
        for line in fi:
            if line:
                words += line

    rarest_symbol = Counter(list(words)).most_common()[-1][0]

    return rarest_symbol


def count_punctuation_chars(file_path: str) -> int:
    """Using regex to find chars, Counter to count rarest"""

    # Regex pattern for chars search and chars accumulator
    pattern = r"[^a-zA-Z0-9_\\]"
    p_chars = []

    # Read all p_chars line by line using regEx
    with open(file_path) as fi:
        for line in fi:
            line_p_chars = re.findall(pattern, line.strip())
            if line_p_chars:
                p_chars += re.findall(pattern, line.strip())

    return len(p_chars)


# def count_non_ascii_chars(file_path: str) -> int:
#     ...
#
#
# def get_most_common_non_ascii_char(file_path: str) -> str:
#     ...