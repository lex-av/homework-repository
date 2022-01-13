import os

from ..pack_task3.module_task3 import find_maximum_and_minimum


def test_positive_1():
    path_to_tests = os.getcwd()
    assert find_maximum_and_minimum(path_to_tests + "/homework1/tests/tst_data/src_1.txt") == (-1, 10)


def test_positive_2():
    path_to_tests = os.getcwd()
    print("test message  ", path_to_tests)
    assert find_maximum_and_minimum(path_to_tests + "/homework1/tests/tst_data/src_2.txt") == (-100, 2)


def test_positive_3():
    path_to_tests = os.getcwd()
    assert find_maximum_and_minimum(path_to_tests + "/homework1/tests/tst_data/src_3.txt") == (12, 50)
