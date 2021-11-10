from check_file.find_maximum_and_minimum import find_maximum_and_minimum

def test_1():
    assert find_maximum_and_minimum('src_1') == (-1, 10)


def test_2():
    assert find_maximum_and_minimum('src_2') == (-100, 2)


def test_3():
    assert find_maximum_and_minimum('src_3') == (12, 50)
