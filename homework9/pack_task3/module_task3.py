# -*- coding: utf-8 -*-

"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    """Function to count lines in files with given extension or tokenizer"""

    dir_path = dir_path.glob(f"**/*.{file_extension}")
    file_list = [file for file in dir_path if file.is_file()]
    counter = 0

    for file in file_list:
        with open(file) as f:
            for line in f:
                if tokenizer:
                    counter += len(tokenizer(line))
                else:
                    counter += 1

    return counter


if __name__ == "__main__":
    path = Path.cwd()
    res = universal_file_counter(path, "txt", str.split)
