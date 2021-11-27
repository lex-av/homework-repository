from find_sum.find_maximal_subarray_sum import find_maximal_subarray_sum


def test_1():
    assert find_maximal_subarray_sum([-1, 0, 0, 10, 25, 25, 25], 1) == 25


def test_2():
    assert find_maximal_subarray_sum([-1, 0, 0, 10, 25, 25, 25], 2) == 50


def test_3():
    assert find_maximal_subarray_sum([-1, 0, 0, 10, 25, 25, 25], 3) == 75


def test_4():
    assert find_maximal_subarray_sum([-1, 0, 0, 10, 25, 25, 25], 4) == 85


def test_5():
    assert find_maximal_subarray_sum([-1, 0, 0, 10, 25, 25, 25], 7) == 85
