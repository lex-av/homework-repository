# -*- coding: utf-8 -*-
"""
Write a function that merges integer from sorted files and returns an iterator
task1_file1.txt:
1
3
5
task1_file2.txt:
2
4
6

list(merge_sorted_files(["task1_file1.txt", "task1_file2.txt"]))
[1, 2, 3, 4, 5, 6]

"""


from contextlib import contextmanager
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


@contextmanager
def open_double(file1_path: str, file2_path: str):
    """
    Context manager to open 2 files
    Could be generalised to n files
    """

    files = {"file1": open(file1_path), "file2": open(file2_path)}
    yield files
    for file in files.values():
        file.close()


def file_read(path: str) -> List[int]:
    """Reads file lines into list"""

    output_list = []
    with open(path) as src:
        for line in src:
            try:
                output_list.append(int(line.strip()))
            except ValueError:
                pass

    return output_list


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    file_values_lists = [file_read(file_name) for file_name in file_list]
    yield from merge(*file_values_lists)


def merge_two_sorted_files(file1_path: str, file2_path: str) -> Iterator:
    with open_double(file1_path, file2_path) as src:
        file1 = src["file1"]
        file2 = src["file2"]

        while True:
            # Try to get next items from both files
            try:
                num1 = int(next(file1).strip())
            except StopIteration:
                file1 = None
                break
            try:
                num2 = int(next(file2).strip())
            except StopIteration:
                file2 = None
                yield num1  # If file2 is over, yield num1 from file1 before next loop
                break

            yield min(num1, num2)
            yield max(num1, num2)

        if file1 is None:
            file1 = file2
        while True:
            try:
                next_num = int(next(file1).strip())
                yield next_num
            except StopIteration:
                break


if __name__ == "__main__":
    pass
