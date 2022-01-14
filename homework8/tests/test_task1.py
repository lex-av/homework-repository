import os

import pytest

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


def test_positive_storage_sync():
    path_to_tests = os.getcwd()
    tst_storage = KeyValueStorage(path_to_tests + "/homework8/tests/tst_data/tst_data_task1_1.txt")
    tst_storage["new_num"] = 99
    del tst_storage["new_num"]
    with pytest.raises(KeyError):
        tst_storage["new_num"]
