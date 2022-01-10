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


from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


class MergingIterator:
    """
    Iterator to handle merging of sorted files, containing ints.
    Needs a list of str-paths as input.
    Does not read entire files in memory.
    Closes files automatically
    """

    @staticmethod
    def _file_read(path: str) -> List[int]:
        """Reads file lines into list"""

        output_list = []
        with open(path) as src:
            for line in src:
                try:
                    output_list.append(int(line.strip()))
                except ValueError:
                    pass

        return output_list

    def __init__(self, file_names_list):
        self.file_names_list = file_names_list
        self.file_values_lists = [self._file_read(file_name) for file_name in file_names_list]
        self.resulting_iterator = iter(merge(*self.file_values_lists))

    def __next__(self):
        try:
            return next(self.resulting_iterator)
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    return MergingIterator(file_list)


if __name__ == "__main__":
    merge_iter = merge_sorted_files(["file1.txt", "file2.txt"])

    merged_lst = [i for i in merge_iter]
    print(merged_lst)
