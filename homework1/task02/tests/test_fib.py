from check_fib.check_fibonacci import check_fibonacci


def test_single_nums_case():
    """Testing that single nums of Fibonacci sequence give True"""
    assert check_fibonacci([0])
    assert check_fibonacci([1])
    assert check_fibonacci([2])
    assert check_fibonacci([3])
    print("Single nums case test successful")


def test_sequence_case():
    """Testing that subsequences of Fibonacci sequence with len() < 3 give True"""
    assert check_fibonacci([0, 1])
    assert check_fibonacci([1, 1])
    assert check_fibonacci([1, 2])
    assert check_fibonacci([13, 21])


def test_long_sequence_case():
    """Testing that long subsequences of Fibonacci sequence with len() < 3 give True"""
    assert check_fibonacci([0, 1, 1])
    assert check_fibonacci([0, 1, 1, 2])
    assert check_fibonacci([3, 5, 8, 13, 21, 34])
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])
    assert check_fibonacci([13, 21, 34])


def test_wrong_sequence_case():
    """Testing that wrong subsequences of Fibonacci sequence with len() < 3 give True"""
    assert not check_fibonacci([0, 1, 4])
    assert not check_fibonacci([4, 6, 7, 2])
    assert not check_fibonacci([3, 5, 13, 13, 21, 34])
    assert not check_fibonacci([0, 1, 1, 0, 3, 5, 8])
    assert not check_fibonacci([13, 34, 21])
