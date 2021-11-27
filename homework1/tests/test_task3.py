from ..pack_task3.module_task3 import find_maximum_and_minimum


def test_positive_1():
    assert find_maximum_and_minimum("tst_data/src_1.txt") == (-1, 10)


def test_positive_2():
    assert find_maximum_and_minimum("tst_data/src_2.txt") == (-100, 2)


def test_positive_3():
    assert find_maximum_and_minimum("tst_data/src_3.txt") == (12, 50)
