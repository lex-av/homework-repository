# -*- coding: utf-8 -*-
"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6

list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]

"""


from pathlib import Path
from typing import Iterator, List, Union


class MergingIterator:
    """
    Iterator to handle merging of sorted files, containing ints.
    Needs a list of str-paths as input.
    Does not read entire files in memory.
    Closes files automatically
    """

    def __init__(self, file_names_list):
        self.file_names_list = file_names_list
        self.file_objects = [open(file_name) for file_name in file_names_list]
        self.file_objects_values = []

        """
            file_objects and file_objects_values are synchronised lists.
            Used them instead dict for more flexibility.
        """

        for opened_file in self.file_objects:
            try:
                self.file_objects_values.append(int(next(opened_file)))

            except StopIteration:
                opened_file.close()

    def __next__(self):
        try:
            next_to_merge = min(self.file_objects_values)
        except ValueError:
            """
            Value error is raised, when file_objects_values is empty.
            This means, that iteration should be stopped.
            So, StopIteration
            """
            raise StopIteration

        # Narrow point here: index search only first appearance. But so do min(). Indexes should be equal
        file_object_index = self.file_objects_values.index(next_to_merge)

        try:
            self.file_objects_values[file_object_index] = int(next(self.file_objects[file_object_index]))
            return next_to_merge

        except StopIteration:
            # Synchronous lists editing here
            self.file_objects[file_object_index].close()
            self.file_objects.pop(file_object_index)
            self.file_objects_values.pop(file_object_index)
            return next_to_merge

    def __iter__(self):
        return self


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    return MergingIterator(file_list)


if __name__ == "__main__":
    merge_iter = MergingIterator(["file1.txt", "file2.txt", "file3.txt"])

    a = [i for i in merge_iter]
    print()
