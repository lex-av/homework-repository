from check_file.find_maximum_and_minimum import find_maximum_and_minimum


def test_1():
    assert find_maximum_and_minimum("tests/src_1.txt") == (-1, 10)


def test_2():
    assert find_maximum_and_minimum("tests/src_2.txt") == (-100, 2)


def test_3():
    assert find_maximum_and_minimum("tests/src_3.txt") == (12, 50)
