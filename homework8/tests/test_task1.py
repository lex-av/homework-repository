import os

from ..pack_task1.module_task1 import KeyValueStorage


def test_positive_str_value():
    path_to_tests = os.getcwd()
    tst_storage = KeyValueStorage(path_to_tests + "/homework8/tests/tst_data/tst_data_task1_1.txt")
    assert tst_storage["soft_name"] == "new_sft"


def test_positive_str_value_dot():
    path_to_tests = os.getcwd()
    tst_storage = KeyValueStorage(path_to_tests + "/homework8/tests/tst_data/tst_data_task1_1.txt")
    assert tst_storage.soft_name == "new_sft"


def test_positive_int_value():
    path_to_tests = os.getcwd()
    tst_storage = KeyValueStorage(path_to_tests + "/homework8/tests/tst_data/tst_data_task1_1.txt")
    assert tst_storage["int_num"] == 54


def test_positive_int_value_dot():
    path_to_tests = os.getcwd()
    tst_storage = KeyValueStorage(path_to_tests + "/homework8/tests/tst_data/tst_data_task1_1.txt")
    assert tst_storage.int_num == 54
