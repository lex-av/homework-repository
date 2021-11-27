from ..pack_task4.module_task4 import check_sum_of_four


def test_positive_case():
    lst_1 = [1, 4, 5, 6]
    lst_2 = [2, 3, 7, 8]
    lst_3 = [1, 4, 6, 10]
    lst_4 = [2, -4, -7, -9]
    assert check_sum_of_four(lst_1, lst_2, lst_3, lst_4) == 0
