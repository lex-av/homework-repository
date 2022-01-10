# -*- coding: utf-8 -*-

import os

from homework9.pack_task1.module_task1 import merge_sorted_files


def test_positive_read_one_file():
    path_to_test = os.getcwd()
    filepath = path_to_test + "/homework9/tests/tests_data/task1_file1.txt"
    assert list(merge_sorted_files([filepath])) == [1, 3, 5]


def test_positive_merge_several_file():
    path_to_test = os.getcwd()
    file_paths = [
        path_to_test + "/homework9/tests/tests_data/task1_file1.txt",
        path_to_test + "/homework9/tests/tests_data/task1_file2.txt",
        path_to_test + "/homework9/tests/tests_data/task1_file3.txt",
    ]
    assert list(merge_sorted_files(file_paths)) == [0, 1, 1, 2, 2, 2, 3, 4, 5, 6, 10, 110]


def test_positive_read_empty_file():
    path_to_test = os.getcwd()
    filepath = path_to_test + "/homework9/tests/tests_data/task1_file4.txt"
    assert list(merge_sorted_files([filepath])) == []


def test_positive_merge_empty_file():
    path_to_test = os.getcwd()
    file_paths = [
        path_to_test + "/homework9/tests/tests_data/task1_file1.txt",
        path_to_test + "/homework9/tests/tests_data/task1_file4.txt",
    ]
    assert list(merge_sorted_files(file_paths)) == [1, 3, 5]
